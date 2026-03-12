#!/usr/bin/env python3
"""Scrape India Parliament debates for AI-related content."""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from pathlib import Path
from urllib.parse import urljoin

OUTPUT_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data/india")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# India Parliament sources
LOK_SABHA_DEBATES = "https://eparlib.nic.in/handle/123456789/7"
SANSAD_DEBATES = "https://sansad.in/ls/debates"
RS_DEBATES = "https://rsdebate.nic.in/"

# AI keywords for search
AI_KEYWORDS = [
    "artificial intelligence",
    "machine learning", 
    "AI policy",
    "digital india",
    "data protection",
    "automation",
    "robotics",
    "algorithm",
    "deepfake",
    "ChatGPT",
    "fourth industrial revolution",
    "cyber security",
]

def search_prs_india():
    """Search PRS India for AI-related legislative content."""
    print("Searching PRS India for AI legislation...")
    
    results = []
    base_url = "https://prsindia.org"
    
    for keyword in ["artificial intelligence", "digital", "data protection", "technology"]:
        search_url = f"{base_url}/search/site/{keyword.replace(' ', '%20')}"
        print(f"  Searching: '{keyword}'...")
        
        try:
            resp = requests.get(search_url, timeout=30)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                # Find search results
                for item in soup.select('.search-result, .views-row, li.search-result'):
                    link = item.select_one('a')
                    if link:
                        title = link.get_text(strip=True)
                        href = link.get('href', '')
                        if href and not href.startswith('http'):
                            href = urljoin(base_url, href)
                        
                        # Check if AI-related
                        text = item.get_text().lower()
                        if any(kw in text for kw in ['artificial intelligence', 'ai ', ' ai', 'digital', 'data', 'technology']):
                            results.append({
                                'title': title,
                                'url': href,
                                'source': 'PRS India',
                                'keyword': keyword
                            })
                
            time.sleep(1)
        except Exception as e:
            print(f"    Error: {e}")
    
    # Deduplicate
    seen = set()
    unique = []
    for r in results:
        if r['url'] not in seen:
            seen.add(r['url'])
            unique.append(r)
    
    return unique

def search_lok_sabha_questions():
    """Search Lok Sabha Q&A for AI mentions."""
    print("\nSearching Lok Sabha Questions...")
    
    # Try the search endpoint
    base_url = "https://sansad.in"
    results = []
    
    # Search for starred and unstarred questions mentioning AI
    search_terms = ["artificial intelligence", "AI policy", "digital india"]
    
    for term in search_terms:
        print(f"  Searching: '{term}'...")
        try:
            # Try sansad.in search
            search_url = f"{base_url}/ls/questions/questions-search"
            params = {'search': term}
            
            resp = requests.get(search_url, params=params, timeout=30, 
                              headers={'User-Agent': 'Mozilla/5.0'})
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                for item in soup.select('tr, .question-item, article'):
                    text = item.get_text()
                    if 'artificial intelligence' in text.lower() or ' ai ' in text.lower():
                        link = item.select_one('a')
                        if link:
                            results.append({
                                'title': link.get_text(strip=True)[:200],
                                'url': urljoin(base_url, link.get('href', '')),
                                'source': 'Lok Sabha Questions',
                                'snippet': text[:500]
                            })
            
            time.sleep(1)
        except Exception as e:
            print(f"    Error: {e}")
    
    return results

def fetch_india_ai_bills():
    """Fetch known AI-related bills from PRS India."""
    print("\nFetching known AI-related bills...")
    
    # Known AI-related bills in India Parliament
    known_bills = [
        {
            'title': 'Digital Personal Data Protection Act, 2023',
            'url': 'https://prsindia.org/billtrack/digital-personal-data-protection-bill-2023',
            'year': 2023,
            'status': 'Enacted'
        },
        {
            'title': 'Digital India Bill (Draft)',
            'url': 'https://prsindia.org/billtrack/draft-digital-india-bill',
            'year': 2023,
            'status': 'Draft'
        },
        {
            'title': 'Information Technology (Intermediary Guidelines) Rules',
            'url': 'https://prsindia.org/theprsblog/explained-it-rules-2021',
            'year': 2021,
            'status': 'In Force'
        },
        {
            'title': 'Bharatiya Nyaya Sanhita - AI/Deepfake provisions',
            'url': 'https://prsindia.org/billtrack/bharatiya-nyaya-sanhita-2023',
            'year': 2023,
            'status': 'Enacted'
        }
    ]
    
    results = []
    
    for bill in known_bills:
        print(f"  Fetching: {bill['title']}...")
        try:
            resp = requests.get(bill['url'], timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                # Get main content
                content_div = soup.select_one('.field-item, article, .content, main')
                content = content_div.get_text(separator='\n', strip=True) if content_div else ''
                
                bill['content'] = content[:20000]  # Truncate
                bill['fetched'] = True
                results.append(bill)
            else:
                bill['fetched'] = False
                bill['content'] = ''
                results.append(bill)
                
            time.sleep(1)
        except Exception as e:
            print(f"    Error: {e}")
            bill['fetched'] = False
            bill['content'] = ''
            results.append(bill)
    
    return results

def search_rajya_sabha():
    """Search Rajya Sabha debates for AI content."""
    print("\nSearching Rajya Sabha debates...")
    
    results = []
    base_url = "https://rsdebate.nic.in"
    
    # Try to search the debate archive
    try:
        # Search page
        search_url = f"{base_url}/searchdebate.aspx"
        
        resp = requests.get(search_url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
        if resp.status_code == 200:
            print("  Found Rajya Sabha search page")
            # Note: This likely requires POST requests with form data
            # For now, we'll note the source exists
            results.append({
                'source': 'Rajya Sabha Debates',
                'url': search_url,
                'note': 'Manual search required - form-based interface'
            })
    except Exception as e:
        print(f"  Error accessing RS debates: {e}")
    
    return results

def main():
    print("=" * 60)
    print("India Parliament AI Data Scraper")
    print("=" * 60)
    
    all_results = {
        'prs_india': [],
        'lok_sabha': [],
        'bills': [],
        'rajya_sabha': []
    }
    
    # 1. Search PRS India
    all_results['prs_india'] = search_prs_india()
    print(f"  PRS India results: {len(all_results['prs_india'])}")
    
    # 2. Search Lok Sabha
    all_results['lok_sabha'] = search_lok_sabha_questions()
    print(f"  Lok Sabha results: {len(all_results['lok_sabha'])}")
    
    # 3. Fetch known AI bills
    all_results['bills'] = fetch_india_ai_bills()
    print(f"  Known AI bills: {len(all_results['bills'])}")
    
    # 4. Check Rajya Sabha
    all_results['rajya_sabha'] = search_rajya_sabha()
    
    # Save results
    with open(OUTPUT_DIR / "search_results.json", 'w') as f:
        json.dump(all_results, f, indent=2)
    
    # Create combined index
    combined = []
    for source, items in all_results.items():
        for item in items:
            item['source_category'] = source
            combined.append(item)
    
    with open(OUTPUT_DIR / "ai_content_index.json", 'w') as f:
        json.dump(combined, f, indent=2)
    
    print(f"\n{'=' * 60}")
    print("India data collection complete!")
    print(f"  PRS India: {len(all_results['prs_india'])} items")
    print(f"  Lok Sabha: {len(all_results['lok_sabha'])} items")
    print(f"  Known Bills: {len(all_results['bills'])} items")
    print(f"  Total: {len(combined)} items")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 60)
    
    return all_results

if __name__ == "__main__":
    main()
