#!/usr/bin/env python3
"""
Large-scale data collection for Nigeria framing study.
Target: 1000+ articles from GDELT and MediaCloud.
"""
import requests
import json
import time
import os
from datetime import date, datetime

# Output
OUTPUT_DIR = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Custom JSON encoder
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def search_gdelt(query, delay=7, maxrecords=250):
    """Search GDELT DOC API with rate limiting."""
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {"query": query, "mode": "artlist", "maxrecords": maxrecords, "format": "json"}
    time.sleep(delay)
    try:
        resp = requests.get(url, params=params, timeout=60)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 429:
            print(f"    Rate limited, waiting 10s...")
            time.sleep(10)
            return search_gdelt(query, delay=delay+2, maxrecords=maxrecords)
        else:
            print(f"    Error {resp.status_code}")
            return None
    except Exception as e:
        print(f"    Exception: {e}")
        return None

print("=" * 70)
print("LARGE-SCALE DATA COLLECTION")
print("=" * 70)
print(f"Started: {datetime.now().isoformat()}")

# GDELT queries - expanded
GDELT_QUERIES = [
    # Core conflict
    ("core_fulani_christian", 'Nigeria (Fulani OR herdsmen) (Christian OR church)'),
    ("core_farmer_herder", 'Nigeria (farmer OR herder) (conflict OR clash OR violence)'),
    ("core_plateau", 'Plateau Nigeria (attack OR violence OR killed)'),
    ("core_benue", 'Benue Nigeria (attack OR violence OR killed)'),
    ("core_kaduna", 'Kaduna Nigeria (Fulani OR attack OR killed)'),
    
    # Persecution angle
    ("persecution", 'Nigeria Christian (persecution OR massacre OR targeted)'),
    ("church_attacks", 'Nigeria church (attack OR burn OR destroyed)'),
    
    # Solution focused
    ("solution_peace", 'Nigeria Fulani (peace OR dialogue OR reconciliation)'),
    ("solution_military", 'Nigeria (military OR army OR troops) (Fulani OR herdsmen OR bandits)'),
    ("solution_govt", 'Nigeria government (Fulani OR herder OR farmer) response'),
    
    # Structural framing
    ("structural_land", 'Nigeria (herder OR farmer) (land OR grazing OR territory)'),
    ("structural_climate", 'Nigeria (Fulani OR herder) (climate OR drought OR desertification)'),
    
    # Source diversity
    ("nigerian_sources", 'Nigeria Fulani Christian sourcecountry:NG'),
    ("uk_sources", 'Nigeria Fulani (Christian OR attack) domain:bbc.com'),
    ("wire_services", 'Nigeria Fulani domain:reuters.com OR domain:apnews.com'),
]

all_gdelt = []
seen_urls = set()

print("\n📰 GDELT COLLECTION")
print("-" * 50)

for name, query in GDELT_QUERIES:
    print(f"\n[{name}] {query[:50]}...")
    result = search_gdelt(query, delay=7)
    
    if result and "articles" in result:
        articles = result["articles"]
        new_count = 0
        for art in articles:
            url = art.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                art["query_source"] = name
                all_gdelt.append(art)
                new_count += 1
        print(f"    Found {len(articles)}, {new_count} new (total: {len(all_gdelt)})")
    else:
        print("    No results")

# Save GDELT data
with open(f"{OUTPUT_DIR}/gdelt_large.json", "w") as f:
    json.dump(all_gdelt, f, indent=2)
print(f"\n✓ Saved {len(all_gdelt)} GDELT articles")

# MediaCloud collection
print("\n📰 MEDIACLOUD COLLECTION")
print("-" * 50)

try:
    import mediacloud.api
    API_KEY = open(os.path.expanduser("~/.openclaw/secrets/mediacloud.key")).read().strip()
    mc_search = mediacloud.api.SearchApi(API_KEY)
    
    MC_QUERIES = [
        ("mc_core", "Nigeria (Fulani OR herdsmen) (Christian OR attack OR violence)"),
        ("mc_persecution", "Nigeria Christian persecution"),
        ("mc_farmer_herder", "Nigeria farmer herder conflict"),
        ("mc_military", "Nigeria military Fulani"),
    ]
    
    start = date(2025, 6, 1)  # Extended range
    end = date(2026, 2, 22)
    
    all_mc = []
    seen_mc_urls = set()
    
    for name, query in MC_QUERIES:
        print(f"\n[{name}] {query[:40]}...")
        
        stories = []
        next_token = None
        page_count = 0
        
        while page_count < 10:  # Up to 10 pages per query
            try:
                page, next_token = mc_search.story_list(
                    query,
                    start_date=start,
                    end_date=end,
                    pagination_token=next_token
                )
                stories.extend(page)
                page_count += 1
                
                if next_token is None:
                    break
                    
            except Exception as e:
                print(f"    Error on page {page_count}: {e}")
                break
        
        new_count = 0
        for s in stories:
            url = s.get("url", "")
            if url and url not in seen_mc_urls:
                seen_mc_urls.add(url)
                s["query_source"] = name
                all_mc.append(s)
                new_count += 1
        
        print(f"    Found {len(stories)}, {new_count} new (total: {len(all_mc)})")
    
    # Save MediaCloud data
    with open(f"{OUTPUT_DIR}/mediacloud_large.json", "w") as f:
        json.dump(all_mc, f, indent=2, cls=DateTimeEncoder)
    print(f"\n✓ Saved {len(all_mc)} MediaCloud stories")
    
except Exception as e:
    print(f"MediaCloud error: {e}")

# Summary
print("\n" + "=" * 70)
print("COLLECTION SUMMARY")
print("=" * 70)
print(f"GDELT articles: {len(all_gdelt)}")
print(f"MediaCloud stories: {len(all_mc) if 'all_mc' in dir() else 'N/A'}")
print(f"Total unique: {len(all_gdelt) + (len(all_mc) if 'all_mc' in dir() else 0)}")
print(f"Completed: {datetime.now().isoformat()}")
print("=" * 70)
