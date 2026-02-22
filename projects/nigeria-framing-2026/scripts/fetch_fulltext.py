#!/usr/bin/env python3
"""Fetch full text for sampled articles."""
import json
import requests
import time
import re
from readability import Document
from bs4 import BeautifulSoup

INPUT = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data/processed/fulltext_sample.json"
OUTPUT = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data/processed/fulltext_articles.json"

def clean_text(html):
    """Extract clean text from HTML."""
    try:
        doc = Document(html)
        content = doc.summary()
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        return text[:5000]  # Limit to 5000 chars
    except:
        return ""

def fetch_article(url, delay=2):
    """Fetch and extract article text."""
    time.sleep(delay)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (research bot)'}
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 200:
            return clean_text(resp.text)
    except Exception as e:
        print(f"  Error: {e}")
    return ""

# Load sample
with open(INPUT) as f:
    articles = json.load(f)

print(f"Fetching full text for {len(articles)} articles...")

results = []
for i, art in enumerate(articles):
    url = art.get('url', '')
    if not url:
        continue
    
    print(f"[{i+1}/{len(articles)}] {art.get('source', 'unknown')}: {art.get('title', '')[:50]}...")
    
    text = fetch_article(url, delay=1)
    
    art['fulltext'] = text
    art['fulltext_len'] = len(text)
    results.append(art)
    
    if text:
        print(f"  ✓ Got {len(text)} chars")
    else:
        print(f"  ✗ Failed")

# Save results
with open(OUTPUT, "w") as f:
    json.dump(results, f, indent=2, default=str)

# Summary
success = len([r for r in results if r.get('fulltext')])
print(f"\nFetched {success}/{len(results)} articles successfully")
print(f"Saved to {OUTPUT}")
