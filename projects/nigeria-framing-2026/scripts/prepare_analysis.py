#!/usr/bin/env python3
"""Prepare combined dataset for multi-model analysis."""
import json
import glob
from collections import Counter

OUTPUT_DIR = "/root/.openclaw/workspace/projects/nigeria-framing-2026/data"

# Combine all sources
all_articles = []
seen_urls = set()

for f in glob.glob(f"{OUTPUT_DIR}/raw/*.json"):
    try:
        with open(f) as fp:
            data = json.load(fp)
            
            if isinstance(data, list):
                articles = data
            elif "articles" in data:
                articles = data["articles"]
            else:
                continue
            
            for art in articles:
                url = art.get("url", art.get("stories_id", ""))
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    # Normalize fields
                    normalized = {
                        "title": art.get("title", ""),
                        "url": art.get("url", ""),
                        "source": art.get("domain", art.get("media_name", "unknown")),
                        "date": art.get("seendate", art.get("publish_date", "")),
                    }
                    all_articles.append(normalized)
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"Total unique articles: {len(all_articles)}")

# Save combined
with open(f"{OUTPUT_DIR}/processed/combined_articles.json", "w") as f:
    json.dump(all_articles, f, indent=2, default=str)

# Create analysis sample (titles only for LLM analysis)
sample = []
for art in all_articles:
    sample.append({
        "title": art["title"],
        "source": art["source"]
    })

with open(f"{OUTPUT_DIR}/processed/titles_for_analysis.json", "w") as f:
    json.dump(sample, f, indent=2)

# Source distribution
sources = Counter(art["source"] for art in all_articles)
print("\nTop sources:")
for s, c in sources.most_common(20):
    print(f"  {s}: {c}")

print(f"\nSaved to {OUTPUT_DIR}/processed/")
