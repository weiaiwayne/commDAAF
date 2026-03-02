#!/usr/bin/env python3
"""Simple GDELT collection for Nigeria conflict study."""
import requests
import json
import time
import os

OUTPUT_DIR = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def search_gdelt(query, delay=6):
    """Search GDELT with rate limiting."""
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {"query": query, "mode": "artlist", "maxrecords": 250, "format": "json"}
    time.sleep(delay)
    try:
        resp = requests.get(url, params=params, timeout=60)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"  Error {resp.status_code}: {resp.text[:100]}")
            return None
    except Exception as e:
        print(f"  Exception: {e}")
        return None

print("=" * 50)
print("GDELT Collection: Nigeria Christian-Fulani")
print("=" * 50)

queries = [
    ('q1_fulani_christian', 'Fulani Nigeria Christian attack'),
    ('q2_farmer_herder', 'farmer herder Nigeria conflict'),
    ('q3_plateau_violence', 'Plateau Nigeria violence'),
]

all_articles = []
seen_urls = set()

for name, query in queries:
    print(f"\nQuery: {query}")
    result = search_gdelt(query, delay=6)
    
    if result and "articles" in result:
        articles = result["articles"]
        new_count = 0
        for art in articles:
            url = art.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                all_articles.append(art)
                new_count += 1
        print(f"  Found {len(articles)}, {new_count} new")
        
        with open(f"{OUTPUT_DIR}/{name}.json", "w") as f:
            json.dump(result, f, indent=2)
    else:
        print("  No results")

# Save combined
with open(f"{OUTPUT_DIR}/gdelt_combined.json", "w") as f:
    json.dump(all_articles, f, indent=2)

print(f"\n{'=' * 50}")
print(f"Total unique articles: {len(all_articles)}")
print(f"Saved to: {OUTPUT_DIR}/gdelt_combined.json")
print("=" * 50)
