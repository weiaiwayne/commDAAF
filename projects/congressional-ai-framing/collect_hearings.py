#!/usr/bin/env python3
"""
Congressional AI Hearings Data Collection Script
Collects all AI-related congressional hearing transcripts from GovInfo API

Usage:
    python collect_hearings.py

Output:
    - data/hearings_metadata.json  (all hearing metadata)
    - data/transcripts/            (individual transcript files)
    - data/corpus_summary.json     (collection statistics)
"""

import json
import os
import time
import requests
from datetime import datetime
from pathlib import Path

# Configuration
API_KEY = "7g37X8beUtfLsj8RZ008nb96tfRZ33LdRfWPayeV"
BASE_URL = "https://api.govinfo.gov"
OUTPUT_DIR = Path("data")
TRANSCRIPTS_DIR = OUTPUT_DIR / "transcripts"

# Search terms for AI-related hearings
SEARCH_QUERIES = [
    'title:"artificial intelligence"',
    'title:"machine learning"', 
    'title:"ChatGPT"',
    'title:"generative AI"',
    'title:"AI regulation"',
    'title:"AI safety"',
    'title:"algorithmic"',
]

def search_hearings(query: str, page_size: int = 100) -> list:
    """Search for congressional hearings matching query."""
    all_results = []
    offset_mark = "*"
    
    while True:
        payload = {
            "query": f"{query} collection:CHRG",
            "pageSize": page_size,
            "offsetMark": offset_mark
        }
        
        response = requests.post(
            f"{BASE_URL}/search?api_key={API_KEY}",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break
            
        data = response.json()
        results = data.get("results", [])
        
        if not results:
            break
            
        all_results.extend(results)
        print(f"  Fetched {len(all_results)} results so far...")
        
        # Check for next page
        if "offsetMark" in data and data["offsetMark"] != offset_mark:
            offset_mark = data["offsetMark"]
            time.sleep(0.5)  # Rate limiting
        else:
            break
    
    return all_results

def get_package_details(package_id: str) -> dict:
    """Get detailed metadata for a hearing package."""
    url = f"{BASE_URL}/packages/{package_id}/summary?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return {}

def download_transcript(package_id: str, granule_id: str = None) -> str:
    """Download the HTML transcript for a hearing."""
    if granule_id:
        url = f"{BASE_URL}/packages/{package_id}/granules/{granule_id}/htm?api_key={API_KEY}"
    else:
        url = f"{BASE_URL}/packages/{package_id}/htm?api_key={API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    return None

def extract_text_from_html(html: str) -> str:
    """Extract plain text from HTML transcript."""
    # Simple extraction - the transcripts are in <pre> tags
    import re
    
    # Remove HTML tags but preserve structure
    text = re.sub(r'<[^>]+>', '', html)
    # Clean up whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def main():
    print("=" * 60)
    print("Congressional AI Hearings Data Collection")
    print("=" * 60)
    
    # Create output directories
    OUTPUT_DIR.mkdir(exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)
    
    # Collect all hearings across search terms
    all_hearings = {}
    
    for query in SEARCH_QUERIES:
        print(f"\nSearching: {query}")
        results = search_hearings(query)
        print(f"  Found {len(results)} results")
        
        for r in results:
            pkg_id = r.get("packageId")
            if pkg_id and pkg_id not in all_hearings:
                all_hearings[pkg_id] = r
    
    print(f"\n{'=' * 60}")
    print(f"Total unique hearings found: {len(all_hearings)}")
    print("=" * 60)
    
    # Enrich with detailed metadata and download transcripts
    hearings_data = []
    successful_downloads = 0
    
    for i, (pkg_id, hearing) in enumerate(all_hearings.items()):
        print(f"\n[{i+1}/{len(all_hearings)}] Processing: {pkg_id}")
        print(f"  Title: {hearing.get('title', 'N/A')[:70]}...")
        
        # Get detailed metadata
        details = get_package_details(pkg_id)
        time.sleep(0.3)
        
        # Merge data
        hearing_record = {
            "package_id": pkg_id,
            "title": hearing.get("title"),
            "date_issued": hearing.get("dateIssued"),
            "collection_code": hearing.get("collectionCode"),
            "government_author": hearing.get("governmentAuthor", []),
            "granule_id": hearing.get("granuleId"),
            "last_modified": hearing.get("lastModified"),
            "details": details,
            "transcript_file": None
        }
        
        # Download transcript
        granule_id = hearing.get("granuleId")
        transcript = download_transcript(pkg_id, granule_id)
        
        if transcript:
            # Save transcript
            safe_filename = pkg_id.replace("/", "_") + ".txt"
            transcript_path = TRANSCRIPTS_DIR / safe_filename
            
            text = extract_text_from_html(transcript)
            transcript_path.write_text(text, encoding="utf-8")
            
            hearing_record["transcript_file"] = safe_filename
            hearing_record["transcript_length"] = len(text)
            successful_downloads += 1
            print(f"  ✓ Downloaded transcript ({len(text):,} chars)")
        else:
            print(f"  ✗ No transcript available")
        
        hearings_data.append(hearing_record)
        time.sleep(0.3)  # Rate limiting
    
    # Save metadata
    metadata_path = OUTPUT_DIR / "hearings_metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(hearings_data, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Saved metadata to {metadata_path}")
    
    # Generate summary
    summary = {
        "collection_date": datetime.now().isoformat(),
        "total_hearings": len(hearings_data),
        "successful_transcripts": successful_downloads,
        "search_queries": SEARCH_QUERIES,
        "date_range": {
            "earliest": min(h["date_issued"] for h in hearings_data if h.get("date_issued")),
            "latest": max(h["date_issued"] for h in hearings_data if h.get("date_issued"))
        },
        "by_year": {},
        "by_chamber": {"House": 0, "Senate": 0, "Joint": 0}
    }
    
    # Count by year
    for h in hearings_data:
        if h.get("date_issued"):
            year = h["date_issued"][:4]
            summary["by_year"][year] = summary["by_year"].get(year, 0) + 1
        
        # Count by chamber
        pkg_id = h.get("package_id", "")
        if "hhrg" in pkg_id.lower():
            summary["by_chamber"]["House"] += 1
        elif "shrg" in pkg_id.lower():
            summary["by_chamber"]["Senate"] += 1
        elif "jhrg" in pkg_id.lower():
            summary["by_chamber"]["Joint"] += 1
    
    summary_path = OUTPUT_DIR / "corpus_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"✓ Saved summary to {summary_path}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("COLLECTION COMPLETE")
    print("=" * 60)
    print(f"Total hearings: {summary['total_hearings']}")
    print(f"Transcripts downloaded: {summary['successful_transcripts']}")
    print(f"Date range: {summary['date_range']['earliest']} to {summary['date_range']['latest']}")
    print(f"\nBy chamber:")
    for chamber, count in summary["by_chamber"].items():
        print(f"  {chamber}: {count}")
    print(f"\nBy year:")
    for year in sorted(summary["by_year"].keys()):
        print(f"  {year}: {summary['by_year'][year]}")

if __name__ == "__main__":
    main()
