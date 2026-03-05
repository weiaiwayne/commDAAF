#!/usr/bin/env python3
"""
Wikipedia Data Collection - Full 50+50 Articles
"""

import requests
import json
import time
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
DATA_DIR = BASE_DIR / "data"
API_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "EpistemicContestationStudy/1.0 (Academic Research; UMass Amherst)",
    "Accept": "application/json"
}
REQUEST_DELAY = 1.0

# FULL IRAN ARTICLES (50)
IRAN_ARTICLES = [
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
    "Evacuations during the 2026 Iran war",
    "Iranian rial",
    "International reactions to the 2026 Iran war",
    "Iran–United States relations",
    "Iran–Israel proxy conflict",
    "Iranian nuclear program",
    "2024 Iran–Israel conflict",
    "Middle Eastern crisis (2023–present)",
    "Iran–Israel relations",
    "Iran and state-sponsored terrorism",
    "Nuclear program of Iran",
    "Axis of Resistance",
    "Houthis",
    "Hezbollah",
    "Benjamin Netanyahu",
]

# FULL GAZA ARTICLES (50)
GAZA_ARTICLES = [
    "Gaza war",
    "2023 Hamas-led attack on Israel",
    "Israeli invasion of the Gaza Strip (2023–present)",
    "Timeline of the Gaza war",
    "International reactions to the 2023 Hamas-led attack on Israel",
    "Gaza genocide",
    "List of military engagements during the Gaza war",
    "Outline of the Gaza war",
    "International reactions to the Israeli invasion of the Gaza Strip",
    "Middle Eastern crisis (2023–present)",
    "Al-Ahli Arab Hospital explosion",
    "Flour Massacre",
    "Nuseirat rescue and massacre",
    "Israeli siege of Gaza",
    "2025 Gaza City offensive",
    "2024 Iran–Israel conflict",
    "2024 Israeli military operation in the West Bank",
    "Israeli invasion of Rafah",
    "2024 Nuseirat refugee camp hostage rescue",
    "2024 Lebanon pager attacks",
    "Israel–Hezbollah conflict (2023–present)",
    "2025 Gaza aid convoy killings",
    "Blockade of the Gaza Strip",
    "Gaza Pier",
    "Battle of Gaza (2023–present)",
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
    "Gaza humanitarian crisis",
    "Impact of the Gaza war on children",
    "Environmental impact of the Gaza war",
    "South Africa v. Israel (Genocide Convention)",
    "Nicaragua v. Germany (Genocide Convention)",
    "Allegations of genocide in the 2023 Israeli attack on Gaza",
    "Human shield",
    "Israeli–Palestinian conflict hostages",
    "2023 Israel–Hamas ceasefire",
    "Sde Teiman",
    "Misinformation in the Israel–Hamas war",
    "Journalists killed in the Israel–Hamas war",
    "Ministry of Health (Gaza Strip)",
    "Wikipedia and the Israeli–Palestinian conflict",
    "Protests against the Israeli invasion of the Gaza Strip",
]


def api_request(params):
    """Make Wikipedia API request with retry."""
    for attempt in range(3):
        try:
            response = requests.get(API_URL, params=params, headers=HEADERS, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                raise


def get_revisions(title, limit=500):
    """Fetch article revisions."""
    params = {
        "action": "query", "titles": title, "prop": "revisions",
        "rvprop": "ids|timestamp|user|userid|comment|size|flags",
        "rvlimit": min(limit, 500), "format": "json", "formatversion": "2"
    }
    
    all_revisions = []
    while len(all_revisions) < limit:
        data = api_request(params)
        pages = data.get("query", {}).get("pages", [])
        for page in pages:
            if page.get("missing"):
                return None
            all_revisions.extend(page.get("revisions", []))
        
        if "continue" not in data:
            break
        params["rvcontinue"] = data["continue"]["rvcontinue"]
        time.sleep(REQUEST_DELAY)
    
    return {"title": title, "revisions": all_revisions[:limit], "total": len(all_revisions),
            "collected_at": datetime.now(timezone.utc).isoformat()}


def get_talk_page(title):
    """Fetch talk page content."""
    params = {
        "action": "parse", "page": f"Talk:{title}",
        "prop": "wikitext|sections", "format": "json", "formatversion": "2"
    }
    try:
        data = api_request(params)
        if "error" in data:
            return None
        parse = data.get("parse", {})
        return {"title": f"Talk:{title}", "wikitext": parse.get("wikitext", ""),
                "sections": parse.get("sections", []),
                "collected_at": datetime.now(timezone.utc).isoformat()}
    except:
        return None


def collect_cluster(articles, cluster_name):
    """Collect all data for a cluster."""
    print(f"\n{'='*60}\nCollecting {cluster_name} ({len(articles)} articles)\n{'='*60}")
    
    cluster_dir = DATA_DIR / cluster_name
    (cluster_dir / "revisions").mkdir(parents=True, exist_ok=True)
    (cluster_dir / "talk_pages").mkdir(parents=True, exist_ok=True)
    
    metadata = {"cluster": cluster_name, "started": datetime.now(timezone.utc).isoformat(),
                "articles": [], "successful": 0, "failed": 0}
    
    for i, article in enumerate(articles, 1):
        safe = article.replace("/", "_").replace(" ", "_").replace("–", "-")
        print(f"[{i}/{len(articles)}] {article}")
        
        meta = {"title": article, "safe_name": safe, "status": "pending"}
        
        try:
            # Revisions
            revs = get_revisions(article)
            if revs:
                with open(cluster_dir / "revisions" / f"{safe}.json", "w") as f:
                    json.dump(revs, f)
                meta["revisions"] = revs["total"]
                print(f"  ✅ {revs['total']} revisions")
            
            time.sleep(REQUEST_DELAY)
            
            # Talk page
            talk = get_talk_page(article)
            if talk:
                with open(cluster_dir / "talk_pages" / f"{safe}.json", "w") as f:
                    json.dump(talk, f)
                meta["talk_chars"] = len(talk.get("wikitext", ""))
                meta["talk_sections"] = len(talk.get("sections", []))
                print(f"  ✅ Talk: {meta['talk_sections']} sections, {meta['talk_chars']} chars")
            
            meta["status"] = "success"
            metadata["successful"] += 1
            
        except Exception as e:
            print(f"  ❌ {e}")
            meta["status"] = "failed"
            meta["error"] = str(e)
            metadata["failed"] += 1
        
        metadata["articles"].append(meta)
        time.sleep(REQUEST_DELAY)
    
    metadata["finished"] = datetime.now(timezone.utc).isoformat()
    with open(cluster_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\n✅ {cluster_name}: {metadata['successful']}/{len(articles)} collected")
    return metadata


def main():
    print(f"Full Wikipedia Collection Started: {datetime.now(timezone.utc).isoformat()}")
    iran = collect_cluster(IRAN_ARTICLES, "iran_cluster")
    gaza = collect_cluster(GAZA_ARTICLES, "gaza_cluster")
    print(f"\n{'='*60}\nSUMMARY\n{'='*60}")
    print(f"Iran: {iran['successful']}/50 | Gaza: {gaza['successful']}/50")
    print(f"Finished: {datetime.now(timezone.utc).isoformat()}")


if __name__ == "__main__":
    main()
