#!/usr/bin/env python3
"""Scrape PMG.org.za for AI-related committee meeting transcripts."""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from pathlib import Path

BASE_URL = "https://pmg.org.za"
OUTPUT_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data/south-africa")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def get_search_page(query="artificial intelligence", page_idx=0):
    """Fetch search results page. page_idx is 0-based."""
    # PMG uses /search/N/ format where N is 0-based page index
    if page_idx == 0:
        url = f'{BASE_URL}/search/'
    else:
        url = f'{BASE_URL}/search/{page_idx}/'
    
    params = {
        'q': f'"{query}"',
        'filter[type]': 'committee_meeting'
    }
    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    return resp.text

def parse_search_page(html):
    """Extract meeting links and metadata from search results."""
    soup = BeautifulSoup(html, 'html.parser')
    meetings = []
    
    for li in soup.select('ul li'):
        h4 = li.select_one('h4 a')
        if not h4 or '/committee-meeting/' not in h4.get('href', ''):
            continue
            
        title = h4.get_text(strip=True)
        href = h4.get('href')
        meeting_id = href.rstrip('/').split('/')[-1]
        
        # Get date
        li_text = li.get_text()
        date_match = re.search(r'(\d{2}\s+\w{3}\s+\d{4})', li_text)
        date = date_match.group(1) if date_match else ''
        
        # Get committee from small tag
        small = li.select_one('small')
        committee = small.get_text(strip=True) if small else ''
        
        # Get snippet
        snippet = ''
        for p in li.select('p'):
            snippet += p.get_text(strip=True) + ' '
        snippet = snippet[:500].strip()
        
        meetings.append({
            'title': title,
            'url': BASE_URL + href,
            'date': date,
            'committee': committee,
            'meeting_id': meeting_id,
            'snippet': snippet
        })
    
    return meetings

def get_max_pages(html):
    """Get the maximum page index from pagination."""
    soup = BeautifulSoup(html, 'html.parser')
    max_idx = 0
    
    for link in soup.select('.pagination a'):
        href = link.get('href', '')
        match = re.search(r'/search/(\d+)/', href)
        if match:
            max_idx = max(max_idx, int(match.group(1)))
    
    return max_idx

def scrape_all_search_results():
    """Scrape all pages of search results."""
    all_meetings = []
    seen_ids = set()
    
    # Get first page
    print("Fetching page 1 (index 0)...")
    html = get_search_page(page_idx=0)
    meetings = parse_search_page(html)
    max_pages = get_max_pages(html)
    
    for m in meetings:
        if m['meeting_id'] not in seen_ids:
            seen_ids.add(m['meeting_id'])
            all_meetings.append(m)
    
    print(f"  Found {len(meetings)} meetings (unique: {len(all_meetings)})")
    print(f"  Max page index: {max_pages}")
    
    # Scrape remaining pages
    for page_idx in range(1, max_pages + 1):
        print(f"Fetching page {page_idx + 1} (index {page_idx})...")
        try:
            time.sleep(1)  # Be polite
            html = get_search_page(page_idx=page_idx)
            meetings = parse_search_page(html)
            
            new_count = 0
            for m in meetings:
                if m['meeting_id'] not in seen_ids:
                    seen_ids.add(m['meeting_id'])
                    all_meetings.append(m)
                    new_count += 1
            
            print(f"  Found {len(meetings)} meetings (new: {new_count}, total unique: {len(all_meetings)})")
            
            if new_count == 0:
                print("  No new meetings found, stopping...")
                break
                
        except Exception as e:
            print(f"  Error: {e}")
            break
    
    return all_meetings

def get_meeting_content(url):
    """Fetch full content of a committee meeting."""
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # PMG meeting pages have content in article or specific divs
    # Try multiple selectors
    for selector in ['.article-content', '.meeting-report', 'article .content', 'article', 'main']:
        content_div = soup.select_one(selector)
        if content_div:
            # Remove navigation, scripts, etc.
            for tag in content_div.select('nav, header, footer, .sidebar, script, style, .share-links, .pagination'):
                tag.decompose()
            text = content_div.get_text(separator='\n', strip=True)
            if len(text) > 500:  # Must have substantial content
                return text
    
    # Fallback: get all text
    body = soup.select_one('body')
    if body:
        for tag in body.select('nav, header, footer, script, style'):
            tag.decompose()
        return body.get_text(separator='\n', strip=True)
    
    return ""

def main():
    print("=" * 60)
    print("PMG South Africa AI Committee Meetings Scraper")
    print("=" * 60)
    
    # Step 1: Get all meeting URLs
    print("\n[1/2] Scraping search results...")
    meetings = scrape_all_search_results()
    print(f"\nTotal unique meetings found: {len(meetings)}")
    
    # Save index
    index_path = OUTPUT_DIR / "meetings_index.json"
    with open(index_path, 'w') as f:
        json.dump(meetings, f, indent=2)
    print(f"Saved index to {index_path}")
    
    # Step 2: Download transcripts
    target_count = min(150, len(meetings))
    print(f"\n[2/2] Downloading {target_count} meeting transcripts...")
    
    transcripts_dir = OUTPUT_DIR / "transcripts"
    transcripts_dir.mkdir(exist_ok=True)
    
    downloaded = 0
    failed = 0
    
    for i, meeting in enumerate(meetings[:target_count]):
        meeting_id = meeting['meeting_id']
        output_file = transcripts_dir / f"{meeting_id}.txt"
        
        if output_file.exists():
            print(f"  [{i+1}/{target_count}] {meeting_id} - already exists, skipping")
            downloaded += 1
            continue
        
        try:
            print(f"  [{i+1}/{target_count}] Downloading {meeting_id}...", end=" ", flush=True)
            content = get_meeting_content(meeting['url'])
            
            if content and len(content) > 500:
                with open(output_file, 'w') as f:
                    f.write(f"Title: {meeting['title']}\n")
                    f.write(f"Date: {meeting['date']}\n")
                    f.write(f"Committee: {meeting['committee']}\n")
                    f.write(f"URL: {meeting['url']}\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(content)
                downloaded += 1
                print(f"OK ({len(content)} chars)")
            else:
                failed += 1
                print(f"SKIP (too short: {len(content) if content else 0} chars)")
            
            time.sleep(0.5)  # Be polite
            
        except Exception as e:
            failed += 1
            print(f"ERROR: {e}")
    
    print(f"\n{'=' * 60}")
    print(f"Download complete!")
    print(f"  Meetings indexed: {len(meetings)}")
    print(f"  Transcripts downloaded: {downloaded}")
    print(f"  Failed/skipped: {failed}")
    print(f"  Output directory: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
