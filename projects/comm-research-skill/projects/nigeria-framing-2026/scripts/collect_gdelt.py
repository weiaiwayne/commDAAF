#!/usr/bin/env python3
"""
GDELT data collection for Nigeria Christian-Fulani conflict framing study.
"""
import requests
import json
import time
import os
from datetime import datetime

OUTPUT_DIR = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data/raw"

def search_gdelt(query, mode="artlist", maxrecords=250, delay=6):
    """Search GDELT DOC API with rate limiting."""
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": query,
        "mode": mode,
        "maxrecords": maxrecords,
        "format": "json"
    }
    
    time.sleep(delay)  # Rate limiting
    
    try:
        resp = requests.get(url, params=params, timeout=60)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"Error {resp.status_code}: {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def collect_articles():
    """Collect articles about Nigeria Christian-Fulani conflict."""
    
    # Core search queries
    queries = [
        # Main conflict terms
        '("Fulani herdsmen" OR "Fulani herders") AND Nigeria AND (Christian OR church OR attack)',
        '"farmer herder conflict" Nigeria',
        'Nigeria (Christian OR Christians) (killed OR attack OR violence) (Fulani OR herdsmen)',
        'Plateau Nigeria violence (Christian OR Fulani)',
        'Benue Nigeria (attack OR killing) (farmer OR herder)',
    ]
    
    all_articles = []
    seen_urls = set()
    
    for i, query in enumerate(queries):
        print(f"\n[{i+1}/{len(queries)}] Query: {query[:60]}...")
        
        result = search_gdelt(query, maxrecords=250, delay=6)
        
        if result and "articles" in result:
            articles = result["articles"]
            new_count = 0
            for art in articles:
                url = art.get("url", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_articles.append(art)
                    new_count += 1
            print(f"  Found {len(articles)} articles, {new_count} new (total: {len(all_articles)})")
        else:
            print(f"  No articles found")
    
    return all_articles

def collect_tone_timeline():
    """Get tone timeline for the conflict."""
    query = '("Fulani" OR "herdsmen") AND Nigeria AND (Christian OR church)'
    
    print("\nCollecting tone timeline...")
    result = search_gdelt(query, mode="timelinetone", delay=6)
    
    return result

def collect_volume_timeline():
    """Get volume timeline for the conflict."""
    query = '("Fulani" OR "herdsmen") AND Nigeria AND (Christian OR church)'
    
    print("\nCollecting volume timeline...")
    result = search_gdelt(query, mode="timelinevol", delay=6)
    
    return result

def main():
    print("=" * 60)
    print("GDELT Data Collection: Nigeria Christian-Fulani Conflict")
    print("=" * 60)
    print(f"Started: {datetime.now().isoformat()}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Collect articles
    articles = collect_articles()
    
    # Save articles
    articles_file = os.path.join(OUTPUT_DIR, "gdelt_articles.json")
    with open(articles_file, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"\nSaved {len(articles)} articles to {articles_file}")
    
    # Collect timelines
    tone_data = collect_tone_timeline()
    if tone_data:
        with open(os.path.join(OUTPUT_DIR, "gdelt_tone_timeline.json"), "w") as f:
            json.dump(tone_data, f, indent=2)
        print("Saved tone timeline")
    
    vol_data = collect_volume_timeline()
    if vol_data:
        with open(os.path.join(OUTPUT_DIR, "gdelt_volume_timeline.json"), "w") as f:
            json.dump(vol_data, f, indent=2)
        print("Saved volume timeline")
    
    print(f"\nCompleted: {datetime.now().isoformat()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
