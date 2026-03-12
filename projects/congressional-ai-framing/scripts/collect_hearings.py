#!/usr/bin/env python3
"""
Collect AI-related congressional hearing data from GovInfo API.
"""

import json
import os
import time
import requests
from pathlib import Path
from typing import Optional

# Configuration
API_KEY = os.environ.get("GOVINFO_API_KEY", "7g37X8beUtfLsj8RZ008nb96tfRZ33LdRfWPayeV")
BASE_URL = "https://api.govinfo.gov"
OUTPUT_DIR = Path(__file__).parent.parent / "data"

def search_hearings(
    query: str = '"artificial intelligence" collection:CHRG',
    page_size: int = 100,
    max_results: Optional[int] = None,
    skip_existing: Optional[set] = None
) -> list:
    """Search for hearings matching query."""
    
    results = []
    offset_mark = "*"
    page_num = 0
    
    while True:
        page_num += 1
        payload = {
            "query": query,
            "pageSize": page_size,
            "offsetMark": offset_mark,
            "sorts": [{"field": "dateIssued", "sortOrder": "DESC"}]
        }
        
        response = requests.post(
            f"{BASE_URL}/search",
            headers={
                "X-Api-Key": API_KEY,
                "Content-Type": "application/json"
            },
            json=payload
        )
        
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break
            
        data = response.json()
        raw_batch = data.get("results", [])
        
        # Filter out already collected
        if skip_existing:
            batch = [h for h in raw_batch if h.get("packageId") not in skip_existing]
            skipped = len(raw_batch) - len(batch)
            if skipped > 0:
                print(f"  (skipped {skipped} existing)")
        else:
            batch = raw_batch
        
        results.extend(batch)
        
        print(f"Page {page_num}: Collected {len(results)} new hearings total...")
        
        if max_results and len(results) >= max_results:
            results = results[:max_results]
            break
        
        # Get next page marker - use offsetMark from response (not nextOffsetMark)
        new_offset = data.get("offsetMark")
        if not new_offset or new_offset == offset_mark or not raw_batch:
            print(f"Pagination complete. Total available in search: {data.get('count', 'unknown')}")
            break
            
        offset_mark = new_offset
        time.sleep(0.5)  # Rate limiting
    
    return results


def get_transcript(package_id: str) -> Optional[str]:
    """Fetch HTML transcript for a hearing."""
    
    url = f"{BASE_URL}/packages/{package_id}/htm"
    response = requests.get(url, params={"api_key": API_KEY})
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to get transcript for {package_id}: {response.status_code}")
        return None


def get_metadata(package_id: str) -> Optional[dict]:
    """Fetch metadata for a hearing."""
    
    url = f"{BASE_URL}/packages/{package_id}/summary"
    response = requests.get(url, params={"api_key": API_KEY})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get metadata for {package_id}: {response.status_code}")
        return None


def collect_sample(n: int = 100, output_dir: Optional[Path] = None, skip_existing: bool = True):
    """Collect a sample of AI hearings with transcripts."""
    
    output_dir = output_dir or OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "transcripts").mkdir(exist_ok=True)
    (output_dir / "metadata").mkdir(exist_ok=True)
    
    # Find existing transcripts to skip
    existing = set()
    if skip_existing:
        transcript_dir = output_dir / "transcripts"
        for f in transcript_dir.glob("CHRG-*"):
            pkg_id = f.stem.replace(".html", "").replace(".txt", "")
            existing.add(pkg_id)
        if existing:
            print(f"Found {len(existing)} existing transcripts, will skip these...")
    
    # Search for hearings
    print(f"Searching for AI hearings (max {n})...")
    hearings = search_hearings(max_results=n, skip_existing=existing if skip_existing else None)
    
    # Save search results
    with open(output_dir / "search_results.json", "w") as f:
        json.dump(hearings, f, indent=2)
    print(f"Saved {len(hearings)} search results")
    
    # Collect transcripts and metadata
    collected = []
    for i, hearing in enumerate(hearings):
        package_id = hearing.get("packageId")
        if not package_id:
            continue
            
        print(f"[{i+1}/{len(hearings)}] Processing {package_id}...")
        
        # Get transcript
        transcript = get_transcript(package_id)
        if transcript:
            transcript_path = output_dir / "transcripts" / f"{package_id}.html"
            with open(transcript_path, "w") as f:
                f.write(transcript)
        
        # Get metadata
        metadata = get_metadata(package_id)
        if metadata:
            metadata_path = output_dir / "metadata" / f"{package_id}.json"
            with open(metadata_path, "w") as f:
                json.dump(metadata, f, indent=2)
        
        collected.append({
            "packageId": package_id,
            "title": hearing.get("title"),
            "dateIssued": hearing.get("dateIssued"),
            "hasTranscript": transcript is not None,
            "hasMetadata": metadata is not None
        })
        
        time.sleep(0.3)  # Rate limiting
    
    # Save collection summary
    with open(output_dir / "collection_summary.json", "w") as f:
        json.dump(collected, f, indent=2)
    
    success_count = sum(1 for c in collected if c["hasTranscript"])
    print(f"\nCollection complete: {success_count}/{len(collected)} transcripts retrieved")
    
    return collected


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Collect congressional AI hearing data")
    parser.add_argument("-n", "--num", type=int, default=100, help="Number of hearings to collect")
    parser.add_argument("-o", "--output", type=str, help="Output directory")
    
    args = parser.parse_args()
    
    output_dir = Path(args.output) if args.output else None
    collect_sample(n=args.num, output_dir=output_dir)
