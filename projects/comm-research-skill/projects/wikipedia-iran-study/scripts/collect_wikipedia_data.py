#!/usr/bin/env python3
"""
Wikipedia Data Collection for Epistemic Contestation Study
Collects revision histories and talk pages for Iran war and Gaza war article clusters.
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

# Rate limiting
REQUEST_DELAY = 0.5  # seconds between requests

# Article lists
IRAN_ARTICLES = [
    # Core Articles
    "2026 Iran war",
    "Prelude to the 2026 Iran war",
    "Timeline of the 2026 Iran war",
    "Reactions to the 2026 Iran war",
    "List of attacks during the 2026 Iran war",
    "Economic impact of the 2026 Iran war",
    "2026 United States military buildup in the Middle East",
    "Iran–Israel war",
    "Twelve-Day War",
    "2025–2026 Iranian protests",
    # Strike/Attack Articles
    "2026 Israeli–United States strikes on Iran",
    "Assassination of Ali Khamenei",
    "2026 Iranian strikes on Israel",
    "2026 Iranian strikes on the United Arab Emirates",
    "2026 Iranian strikes on Qatar",
    "2026 Iranian strikes on Oman",
    "2026 Iranian strikes on Akrotiri and Dhekelia",
    "2026 Iranian strikes on Bahrain",
    "2026 Iranian strikes on Kuwait",
    "2026 Iranian strikes on Saudi Arabia",
    "2026 Iranian strikes on Jordan",
    "2026 Iranian strikes on Iraq",
    "Cyberwarfare during the 2026 Iran war",
    "List of Iranian officials killed during the 2026 Iran war",
    "2026 Iran massacres",
    # Actor Articles
    "Ali Khamenei",
    "Aziz Nasirzadeh",
    "Mohammad Pakpour",
    "Ali Shamkhani",
    "Abdolrahim Mousavi",
    "Islamic Revolutionary Guard Corps",
    "Islamic Republic of Iran Army",
    "United States Central Command",
    "Israel Defense Forces",
    "Donald Trump",
    # Thematic Articles
    "Evacuations during the 2026 Iran war",
    "Iranian rial",
    "International reactions to the 2026 Iran war",
    "Protests against the 2026 Iran war",
    "Casualties of the 2026 Iran war",
    # Related Context
    "Iran–United States relations",
    "Iran–Israel proxy conflict",
    "Iranian nuclear program",
    "2024 Iran–Israel conflict",
    "Middle Eastern crisis (2023–present)",
    # Additional to reach 50
    "Operation Roaring Lion",
    "Operation Epic Fury",
    "2026 oil price surge",
    "Media coverage of the 2026 Iran war",
    "Displacement during the 2026 Iran war",
]

GAZA_ARTICLES = [
    # Core Articles
    "Gaza war",
    "7 October attacks",
    "Israeli invasion of the Gaza Strip (2023–present)",
    "Timeline of the Gaza war",
    "Reactions to the 7 October attacks",
    "Gaza genocide",
    "List of military engagements during the Gaza war",
    "Outline of the Gaza war",
    "Reactions to the Gaza war",
    "Middle Eastern crisis (2023–present)",
    # Major Event Articles
    "Al-Ahli Arab Hospital explosion",
    "Flour Massacre",
    "Nuseirat rescue and massacre",
    "Siege of Gaza City",
    "2025 Gaza City offensive",
    "2024 Iran–Israel conflict",
    "2024 Israeli military operation in the West Bank",
    "2024 Rafah offensive",
    "2024 Rafah hostage raid",
    "2024 Lebanon electronic device attacks",
    "Israel–Hezbollah conflict (2023–present)",
    "2025 Gaza Strip aid distribution killings",
    "2023 Israeli blockade of the Gaza Strip",
    "Gaza floating pier",
    "Battle of Gaza (2023–present)",
    # Actor Articles
    "Hamas",
    "Izz ad-Din al-Qassam Brigades",
    "Benjamin Netanyahu",
    "Yoav Gallant",
    "Yahya Sinwar",
    "Ismail Haniyeh",
    "Israel Defense Forces",
    "Palestinian Islamic Jihad",
    "Hezbollah",
    "Houthis",
    # Humanitarian/Legal Articles
    "Gaza humanitarian crisis (2023–present)",
    "Effect of the Gaza war on children in the Gaza Strip",
    "Environmental impact of the Gaza war",
    "South Africa v. Israel",
    "Nicaragua v. Germany (2024)",
    "War crimes in the Gaza war",
    "Use of human shields in the Gaza war",
    "Hostages in the Gaza war",
    "Prisoner exchange in the Gaza war",
    "Sde Teiman detention camp",
    # Media/Information Articles
    "Misinformation in the Gaza war",
    "Killing of journalists in the Gaza war",
    "Gaza Ministry of Health",
    "Wikipedia and the Israeli–Palestinian conflict",
    "Protests against the Gaza war",
]


def get_revisions(title, rvstart=None, rvend=None, limit=500):
    """Fetch revision history for an article."""
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "ids|timestamp|user|userid|comment|size|flags",
        "rvlimit": limit,
        "format": "json",
    }
    if rvstart:
        params["rvstart"] = rvstart
    if rvend:
        params["rvend"] = rvend
    
    all_revisions = []
    while True:
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if page_id == "-1":
                print(f"  ⚠️ Article not found: {title}")
                return None
            revisions = page_data.get("revisions", [])
            all_revisions.extend(revisions)
        
        # Check for continuation
        if "continue" in data:
            params["rvcontinue"] = data["continue"]["rvcontinue"]
            time.sleep(REQUEST_DELAY)
        else:
            break
    
    return {
        "title": title,
        "revisions": all_revisions,
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
    }
    
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    if "error" in data:
        print(f"  ⚠️ Talk page not found: Talk:{title}")
        return None
    
    parse_data = data.get("parse", {})
    return {
        "title": f"Talk:{title}",
        "wikitext": parse_data.get("wikitext", {}).get("*", ""),
        "sections": parse_data.get("sections", []),
        "collected_at": datetime.utcnow().isoformat()
    }


def get_talk_revisions(title, limit=500):
    """Fetch revision history for a talk page."""
    return get_revisions(f"Talk:{title}", limit=limit)


def collect_cluster(articles, cluster_name, time_filter=None):
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
        safe_name = article.replace("/", "_").replace(" ", "_")
        print(f"\n[{i}/{len(articles)}] {article}")
        
        article_meta = {
            "title": article,
            "safe_name": safe_name,
            "revision_file": None,
            "talk_file": None,
            "talk_revisions_file": None,
            "status": "pending"
        }
        
        try:
            # Collect article revisions
            print(f"  📄 Fetching article revisions...")
            if time_filter:
                revisions = get_revisions(article, rvstart=time_filter["start"], rvend=time_filter["end"])
            else:
                revisions = get_revisions(article)
            
            if revisions:
                rev_file = revisions_dir / f"{safe_name}.json"
                with open(rev_file, "w") as f:
                    json.dump(revisions, f, indent=2)
                article_meta["revision_file"] = str(rev_file.relative_to(BASE_DIR))
                article_meta["revision_count"] = revisions["total_revisions"]
                print(f"  ✅ {revisions['total_revisions']} revisions saved")
            
            time.sleep(REQUEST_DELAY)
            
            # Collect talk page content
            print(f"  💬 Fetching talk page content...")
            talk = get_talk_page(article)
            if talk:
                talk_file = talk_dir / f"{safe_name}_content.json"
                with open(talk_file, "w") as f:
                    json.dump(talk, f, indent=2)
                article_meta["talk_file"] = str(talk_file.relative_to(BASE_DIR))
                article_meta["talk_sections"] = len(talk.get("sections", []))
                print(f"  ✅ Talk page saved ({len(talk.get('sections', []))} sections)")
            
            time.sleep(REQUEST_DELAY)
            
            # Collect talk page revisions
            print(f"  📝 Fetching talk page revisions...")
            talk_revs = get_talk_revisions(article)
            if talk_revs:
                talk_rev_file = talk_dir / f"{safe_name}_revisions.json"
                with open(talk_rev_file, "w") as f:
                    json.dump(talk_revs, f, indent=2)
                article_meta["talk_revisions_file"] = str(talk_rev_file.relative_to(BASE_DIR))
                article_meta["talk_revision_count"] = talk_revs["total_revisions"]
                print(f"  ✅ {talk_revs['total_revisions']} talk revisions saved")
            
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
    print("Wikipedia Epistemic Contestation Study - Data Collection")
    print("=" * 60)
    print(f"Started: {datetime.utcnow().isoformat()}")
    
    # Collect Iran cluster (past week only for revisions)
    # Note: Talk pages always get full content
    iran_time_filter = {
        "start": "2026-03-05T23:59:59Z",  # Most recent first
        "end": "2026-02-27T00:00:00Z"     # Past week
    }
    iran_meta = collect_cluster(IRAN_ARTICLES, "iran_cluster", time_filter=iran_time_filter)
    
    # Collect Gaza cluster (full history)
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
