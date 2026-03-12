#!/usr/bin/env python3
"""Download remaining South Africa PMG transcripts."""

import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path

DATA_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data/south-africa")
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"

def get_meeting_content(url):
    """Fetch full content of a committee meeting."""
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    for selector in ['.article-content', '.meeting-report', 'article .content', 'article', 'main']:
        content_div = soup.select_one(selector)
        if content_div:
            for tag in content_div.select('nav, header, footer, .sidebar, script, style, .share-links, .pagination'):
                tag.decompose()
            text = content_div.get_text(separator='\n', strip=True)
            if len(text) > 500:
                return text
    
    body = soup.select_one('body')
    if body:
        for tag in body.select('nav, header, footer, script, style'):
            tag.decompose()
        return body.get_text(separator='\n', strip=True)
    
    return ""

def main():
    print("Downloading remaining South Africa transcripts...")
    
    # Load index
    with open(DATA_DIR / "meetings_index.json") as f:
        meetings = json.load(f)
    
    # Find what's already downloaded
    downloaded = set(p.stem for p in TRANSCRIPTS_DIR.glob("*.txt"))
    remaining = [m for m in meetings if m['meeting_id'] not in downloaded]
    
    print(f"Already downloaded: {len(downloaded)}")
    print(f"Remaining: {len(remaining)}")
    
    success = 0
    failed = 0
    
    for i, meeting in enumerate(remaining):
        meeting_id = meeting['meeting_id']
        output_file = TRANSCRIPTS_DIR / f"{meeting_id}.txt"
        
        print(f"  [{i+1}/{len(remaining)}] Downloading {meeting_id}...", end=" ", flush=True)
        
        try:
            content = get_meeting_content(meeting['url'])
            
            if content and len(content) > 500:
                with open(output_file, 'w') as f:
                    f.write(f"Title: {meeting['title']}\n")
                    f.write(f"Date: {meeting['date']}\n")
                    f.write(f"Committee: {meeting.get('committee', '')}\n")
                    f.write(f"URL: {meeting['url']}\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(content)
                success += 1
                print(f"OK ({len(content)} chars)")
            else:
                failed += 1
                print(f"SKIP (too short)")
            
            time.sleep(0.5)
            
        except Exception as e:
            failed += 1
            print(f"ERROR: {e}")
    
    print(f"\nComplete! Success: {success}, Failed: {failed}")
    print(f"Total transcripts now: {len(downloaded) + success}")

if __name__ == "__main__":
    main()
