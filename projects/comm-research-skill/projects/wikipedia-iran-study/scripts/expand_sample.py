#!/usr/bin/env python3
"""
Expand talk page sample from 100 to ~275 excerpts.
Maintains original 100 excerpts and adds 175 more.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
DATA_DIR = BASE_DIR / "data"
CODING_DIR = BASE_DIR / "coding"

# Same patterns as original
DISPUTE_PATTERNS = [
    (r"WP:NPOV|WP:POV|neutral point of view", "policy_npov"),
    (r"WP:RS|reliable source|WP:V|verifiab", "policy_rs"),
    (r"WP:UNDUE|undue weight", "policy_undue"),
    (r"WP:SYNTH|synthesis|original research|WP:OR", "policy_synthesis"),
    (r"WP:BLP|biograph", "policy_blp"),
    (r"should be (called|named|titled)|rename|move to|article title", "naming"),
    (r"\"war\"|\"conflict\"|\"strikes\"|terminology", "terminology"),
    (r"not reliable|unreliable|biased source|propaganda", "source_dispute"),
    (r"state media|government source|western source", "source_hierarchy"),
    (r"you (don't|do not) understand|new (user|editor|account)", "credibility"),
    (r"POV[ -]push|pushing|agenda", "pov_accusation"),
    (r"genocide|massacre|terrorist|freedom fighter", "framing"),
    (r"civilian|military target|human shield", "framing_violence"),
]


def extract_threads(wikitext):
    """Extract discussion threads from talk page wikitext."""
    threads = []
    sections = re.split(r'\n==\s*([^=]+?)\s*==\n', wikitext)
    
    current_title = "General"
    for i, part in enumerate(sections):
        if i % 2 == 1:
            current_title = part.strip()
        else:
            if part.strip():
                subsections = re.split(r'\n===\s*([^=]+?)\s*===\n', part)
                for j, sub in enumerate(subsections):
                    if j % 2 == 0 and sub.strip():
                        threads.append({
                            "section": current_title,
                            "content": sub.strip()[:5000]
                        })
    
    return threads


def score_thread(thread):
    """Score a thread for epistemic contestation indicators."""
    content = thread["content"].lower()
    scores = defaultdict(int)
    matches = []
    
    for pattern, category in DISPUTE_PATTERNS:
        found = re.findall(pattern, content, re.IGNORECASE)
        if found:
            scores[category] += len(found)
            matches.extend(found[:3])
    
    return {
        "total_score": sum(scores.values()),
        "category_scores": dict(scores),
        "matches": matches[:10],
        "word_count": len(content.split())
    }


def content_hash(content):
    """Create hash for deduplication."""
    # Use first 200 chars normalized
    return content[:200].lower().strip()


def get_all_threads(cluster_name, min_words=30, min_score=0):
    """Get all candidate threads from a cluster with relaxed criteria."""
    talk_dir = DATA_DIR / cluster_name / "talk_pages"
    all_threads = []
    
    for talk_file in talk_dir.glob("*.json"):
        with open(talk_file) as f:
            data = json.load(f)
        
        article = data.get("title", "").replace("Talk:", "")
        wikitext = data.get("wikitext", "")
        
        if not wikitext or len(wikitext) < 100:
            continue
        
        threads = extract_threads(wikitext)
        
        for thread in threads:
            thread["article"] = article
            thread["source_file"] = talk_file.name
            score_info = score_thread(thread)
            thread.update(score_info)
            
            # Relaxed criteria for expansion
            if thread["word_count"] >= min_words and thread["total_score"] >= min_score:
                thread["hash"] = content_hash(thread["content"])
                all_threads.append(thread)
    
    return all_threads


def load_existing():
    """Load existing excerpts to avoid duplicates."""
    existing_file = CODING_DIR / "excerpts_for_coding.json"
    if not existing_file.exists():
        return [], set()
    
    with open(existing_file) as f:
        existing = json.load(f)
    
    existing_hashes = {content_hash(e["content"]) for e in existing}
    return existing, existing_hashes


def select_new_excerpts(all_threads, existing_hashes, n_target, cluster_name):
    """Select new excerpts avoiding duplicates."""
    # Filter out existing
    new_candidates = [t for t in all_threads if t["hash"] not in existing_hashes]
    
    # Sort by score
    new_candidates.sort(key=lambda x: x["total_score"], reverse=True)
    
    selected = []
    articles_count = defaultdict(int)
    
    # Balanced selection across articles
    for thread in new_candidates:
        # Limit per article to ensure diversity
        if articles_count[thread["article"]] < 10:
            selected.append(thread)
            articles_count[thread["article"]] += 1
            if len(selected) >= n_target:
                break
    
    return selected


def format_for_coding(excerpts, cluster_name, start_id=1):
    """Format excerpts for LLM coding."""
    coding_items = []
    
    for i, excerpt in enumerate(excerpts, start_id):
        content = excerpt["content"]
        if len(content) > 2000:
            content = content[:2000] + "..."
        
        item = {
            "id": f"{cluster_name}_{i:03d}",
            "cluster": cluster_name,
            "article": excerpt["article"],
            "section": excerpt["section"],
            "content": content,
            "word_count": excerpt["word_count"],
            "dispute_score": excerpt["total_score"],
            "categories_detected": excerpt["category_scores"],
            "sample_matches": excerpt["matches"]
        }
        coding_items.append(item)
    
    return coding_items


def main():
    print("Expanding Talk Page Sample to ~275 Excerpts")
    print("=" * 60)
    
    # Load existing
    existing, existing_hashes = load_existing()
    existing_iran = [e for e in existing if e["cluster"] == "iran"]
    existing_gaza = [e for e in existing if e["cluster"] == "gaza"]
    
    print(f"Existing excerpts: {len(existing)} (Iran: {len(existing_iran)}, Gaza: {len(existing_gaza)})")
    
    # Target: 275 total, split ~137-138 each
    target_per_cluster = 138
    iran_needed = target_per_cluster - len(existing_iran)
    gaza_needed = target_per_cluster - len(existing_gaza)
    
    print(f"Need: Iran +{iran_needed}, Gaza +{gaza_needed}")
    
    # Get all threads with relaxed criteria (score >= 0 means any thread with disputes)
    iran_threads = get_all_threads("iran_cluster", min_words=30, min_score=0)
    gaza_threads = get_all_threads("gaza_cluster", min_words=30, min_score=0)
    
    print(f"Available candidates: Iran {len(iran_threads)}, Gaza {len(gaza_threads)}")
    
    # Select new excerpts
    new_iran = select_new_excerpts(iran_threads, existing_hashes, iran_needed, "iran")
    new_gaza = select_new_excerpts(gaza_threads, existing_hashes, gaza_needed, "gaza")
    
    print(f"Selected new: Iran {len(new_iran)}, Gaza {len(new_gaza)}")
    
    # Format new excerpts (continue IDs from existing)
    new_iran_items = format_for_coding(new_iran, "iran", start_id=len(existing_iran) + 1)
    new_gaza_items = format_for_coding(new_gaza, "gaza", start_id=len(existing_gaza) + 1)
    
    # Combine with existing
    all_items = existing + new_iran_items + new_gaza_items
    
    # Save expanded dataset
    with open(CODING_DIR / "excerpts_for_coding_v2.json", "w") as f:
        json.dump(all_items, f, indent=2)
    
    # Save just the new excerpts for incremental coding
    new_items = new_iran_items + new_gaza_items
    with open(CODING_DIR / "excerpts_new_batch.json", "w") as f:
        json.dump(new_items, f, indent=2)
    
    # Update summary
    summary = {
        "total_excerpts": len(all_items),
        "iran_excerpts": len(existing_iran) + len(new_iran_items),
        "gaza_excerpts": len(existing_gaza) + len(new_gaza_items),
        "new_excerpts": len(new_items),
        "iran_articles": list(set(e["article"] for e in all_items if e["cluster"] == "iran")),
        "gaza_articles": list(set(e["article"] for e in all_items if e["cluster"] == "gaza")),
        "category_distribution": defaultdict(int)
    }
    
    for item in all_items:
        for cat in item["categories_detected"]:
            summary["category_distribution"][cat] += 1
    
    summary["category_distribution"] = dict(summary["category_distribution"])
    
    with open(CODING_DIR / "sampling_summary_v2.json", "w") as f:
        json.dump(summary, f, indent=2)
    
    print("\n" + "=" * 60)
    print("EXPANDED SAMPLE SUMMARY")
    print("=" * 60)
    print(f"Total excerpts: {summary['total_excerpts']}")
    print(f"Iran: {summary['iran_excerpts']} from {len(summary['iran_articles'])} articles")
    print(f"Gaza: {summary['gaza_excerpts']} from {len(summary['gaza_articles'])} articles")
    print(f"New excerpts to code: {summary['new_excerpts']}")
    print("\nFiles saved:")
    print("  - excerpts_for_coding_v2.json (full expanded dataset)")
    print("  - excerpts_new_batch.json (just new excerpts for coding)")


if __name__ == "__main__":
    main()
