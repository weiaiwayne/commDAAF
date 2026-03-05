#!/usr/bin/env python3
"""
Wikipedia Data Collection for Epistemic Contestation Study v2
Fixed: Added proper headers and better error handling
"""

import requests
import json
import time
import os
from datetime import datetime
from pathlib import Path

# Base paths
BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
DATA_DIR = BASE_DIR / "data"

# Wikipedia API endpoint
API_URL = "https://en.wikipedia.org/w/api.php"

# Required headers for Wikipedia API
HEADERS = {
    "User-Agent": "EpistemicContestationStudy/1.0 (Academic Research; UMass Amherst; Contact: research@example.edu)",
    "Accept": "application/json"
}

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests (be nice to Wikipedia)
MAX_RETRIES = 3

# Article lists (shortened for initial test)
IRAN_ARTICLES = [
    "2026 Iran war",
    "Prelude to the 2026 Iran war",
    "Timeline of the 2026 Iran war",
    "Reactions to the 2026 Iran war",
    "2026 Israeli–United States strikes on Iran",
    "Assassination of Ali Khamenei",
    "2025–2026 Iranian protests",
    "Iran–Israel war",
    "2024 Iran–Israel conflict",
    "Middle Eastern crisis (2023–present)",
]

GAZA_ARTICLES = [
    "Gaza war",
    "7 October attacks",
    "Israeli invasion of the Gaza Strip (2023–present)",
    "Gaza genocide",
    "Al-Ahli Arab Hospital explosion",
    "Nuseirat rescue and massacre",
    "Wikipedia and the Israeli–Palestinian conflict",
    "Reactions to the Gaza war",
    "Hamas",
    "Benjamin Netanyahu",
]


def api_request(params, retries=MAX_RETRIES):
    """Make a Wikipedia API request with retries."""
    for attempt in range(retries):
        try:
            response = requests.get(API_URL, params=params, headers=HEADERS, timeout=30)
            response.raise_for_status()
            
            # Check if we got valid JSON
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"    Attempt {attempt+1}/{retries} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
        except json.JSONDecodeError as e:
            print(f"    JSON decode error: {e}")
            print(f"    Response text: {response.text[:200]}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise


def get_revisions(title, limit=500):
    """Fetch revision history for an article."""
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "ids|timestamp|user|userid|comment|size|flags",
        "rvlimit": min(limit, 500),
        "format": "json",
        "formatversion": "2"
    }
    
    all_revisions = []
    while True:
        data = api_request(params)
        
        pages = data.get("query", {}).get("pages", [])
        for page_data in pages:
            if page_data.get("missing"):
                print(f"    ⚠️ Article not found: {title}")
                return None
            revisions = page_data.get("revisions", [])
            all_revisions.extend(revisions)
        
        # Check for continuation
        if "continue" in data:
            params["rvcontinue"] = data["continue"]["rvcontinue"]
            time.sleep(REQUEST_DELAY)
        else:
            break
        
        if len(all_revisions) >= limit:
            break
    
    return {
        "title": title,
        "revisions": all_revisions[:limit],
        "total_revisions": len(all_revisions),
        "collected_at": datetime.utcnow().isoformat()
    }


def get_talk_page(title):
    """Fetch talk page content."""
    params = {
        "action": "parse",
        "page": f"Talk:{title}",
        "prop": "wikitext|sections",
        "format": "json",
        "formatversion": "2"
    }
    
    try:
        data = api_request(params)
    except Exception as e:
        print(f"    ⚠️ Could not fetch talk page: {e}")
        return None
    
    if "error" in data:
        print(f"    ⚠️ Talk page not found: Talk:{title}")
        return None
    
    parse_data = data.get("parse", {})
    return {
        "title": f"Talk:{title}",
        "wikitext": parse_data.get("wikitext", ""),
        "sections": parse_data.get("sections", []),
        "collected_at": datetime.utcnow().isoformat()
    }


def collect_cluster(articles, cluster_name):
    """Collect data for an article cluster."""
    print(f"\n{'='*60}")
    print(f"Collecting {cluster_name} cluster ({len(articles)} articles)")
    print(f"{'='*60}")
    
    cluster_dir = DATA_DIR / cluster_name
    revisions_dir = cluster_dir / "revisions"
    talk_dir = cluster_dir / "talk_pages"
    
    # Ensure directories exist
    revisions_dir.mkdir(parents=True, exist_ok=True)
    talk_dir.mkdir(parents=True, exist_ok=True)
    
    metadata = {
        "cluster": cluster_name,
        "collection_started": datetime.utcnow().isoformat(),
        "articles": [],
        "successful": 0,
        "failed": 0
    }
    
    for i, article in enumerate(articles, 1):
        safe_name = article.replace("/", "_").replace(" ", "_").replace("–", "-")
        print(f"\n[{i}/{len(articles)}] {article}")
        
        article_meta = {
            "title": article,
            "safe_name": safe_name,
            "revision_file": None,
            "talk_file": None,
            "status": "pending"
        }
        
        try:
            # Collect article revisions
            print(f"  📄 Fetching article revisions...")
            revisions = get_revisions(article, limit=500)
            
            if revisions:
                rev_file = revisions_dir / f"{safe_name}.json"
                with open(rev_file, "w") as f:
                    json.dump(revisions, f, indent=2)
                article_meta["revision_file"] = str(rev_file.name)
                article_meta["revision_count"] = revisions["total_revisions"]
                print(f"  ✅ {revisions['total_revisions']} revisions saved")
            else:
                article_meta["revision_count"] = 0
            
            time.sleep(REQUEST_DELAY)
            
            # Collect talk page content
            print(f"  💬 Fetching talk page content...")
            talk = get_talk_page(article)
            if talk:
                talk_file = talk_dir / f"{safe_name}.json"
                with open(talk_file, "w") as f:
                    json.dump(talk, f, indent=2)
                article_meta["talk_file"] = str(talk_file.name)
                article_meta["talk_sections"] = len(talk.get("sections", []))
                article_meta["talk_length"] = len(talk.get("wikitext", ""))
                print(f"  ✅ Talk page saved ({len(talk.get('sections', []))} sections, {len(talk.get('wikitext', ''))} chars)")
            
            article_meta["status"] = "success"
            metadata["successful"] += 1
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            article_meta["status"] = "failed"
            article_meta["error"] = str(e)
            metadata["failed"] += 1
        
        metadata["articles"].append(article_meta)
        time.sleep(REQUEST_DELAY)
    
    metadata["collection_finished"] = datetime.utcnow().isoformat()
    
    # Save metadata
    meta_file = cluster_dir / "metadata.json"
    with open(meta_file, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\n✅ {cluster_name} collection complete:")
    print(f"   Successful: {metadata['successful']}/{len(articles)}")
    print(f"   Failed: {metadata['failed']}/{len(articles)}")
    
    return metadata


def main():
    print("Wikipedia Epistemic Contestation Study - Data Collection v2")
    print("=" * 60)
    print(f"Started: {datetime.utcnow().isoformat()}")
    
    # Test with smaller set first
    iran_meta = collect_cluster(IRAN_ARTICLES, "iran_cluster")
    gaza_meta = collect_cluster(GAZA_ARTICLES, "gaza_cluster")
    
    # Summary
    print("\n" + "=" * 60)
    print("COLLECTION SUMMARY")
    print("=" * 60)
    print(f"Iran cluster: {iran_meta['successful']}/{len(IRAN_ARTICLES)} articles")
    print(f"Gaza cluster: {gaza_meta['successful']}/{len(GAZA_ARTICLES)} articles")
    print(f"Finished: {datetime.utcnow().isoformat()}")


if __name__ == "__main__":
    main()
