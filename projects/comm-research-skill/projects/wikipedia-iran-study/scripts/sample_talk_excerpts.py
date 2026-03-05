#!/usr/bin/env python3
"""
Sample talk page excerpts for CDA coding.
Focus on high-conflict threads with policy invocations and disputes.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
DATA_DIR = BASE_DIR / "data"
CODING_DIR = BASE_DIR / "coding"
CODING_DIR.mkdir(exist_ok=True)

# Patterns indicating epistemic contestation
DISPUTE_PATTERNS = [
    # Policy invocations
    (r"WP:NPOV|WP:POV|neutral point of view", "policy_npov"),
    (r"WP:RS|reliable source|WP:V|verifiab", "policy_rs"),
    (r"WP:UNDUE|undue weight", "policy_undue"),
    (r"WP:SYNTH|synthesis|original research|WP:OR", "policy_synthesis"),
    (r"WP:BLP|biograph", "policy_blp"),
    
    # Naming disputes
    (r"should be (called|named|titled)|rename|move to|article title", "naming"),
    (r"\"war\"|\"conflict\"|\"strikes\"|terminology", "terminology"),
    
    # Source disputes
    (r"not reliable|unreliable|biased source|propaganda", "source_dispute"),
    (r"state media|government source|western source", "source_hierarchy"),
    
    # Credibility challenges
    (r"you (don't|do not) understand|new (user|editor|account)", "credibility"),
    (r"POV[ -]push|pushing|agenda", "pov_accusation"),
    
    # Framing disputes
    (r"genocide|massacre|terrorist|freedom fighter", "framing"),
    (r"civilian|military target|human shield", "framing_violence"),
]


def extract_threads(wikitext):
    """Extract discussion threads from talk page wikitext."""
    threads = []
    
    # Split by section headers
    sections = re.split(r'\n==\s*([^=]+?)\s*==\n', wikitext)
    
    current_title = "General"
    for i, part in enumerate(sections):
        if i % 2 == 1:  # Section title
            current_title = part.strip()
        else:  # Section content
            if part.strip():
                # Further split by subsections
                subsections = re.split(r'\n===\s*([^=]+?)\s*===\n', part)
                for j, sub in enumerate(subsections):
                    if j % 2 == 0 and sub.strip():
                        threads.append({
                            "section": current_title,
                            "content": sub.strip()[:5000]  # Limit length
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
            matches.extend(found[:3])  # Keep first 3 matches
    
    total_score = sum(scores.values())
    
    return {
        "total_score": total_score,
        "category_scores": dict(scores),
        "matches": matches[:10],
        "word_count": len(content.split())
    }


def sample_excerpts(cluster_name, n_excerpts=50):
    """Sample high-conflict excerpts from a cluster."""
    print(f"\nSampling from {cluster_name}...")
    
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
            
            # Only keep threads with some content and dispute indicators
            if thread["word_count"] > 50 and thread["total_score"] > 0:
                all_threads.append(thread)
    
    # Sort by score and sample diverse excerpts
    all_threads.sort(key=lambda x: x["total_score"], reverse=True)
    
    # Select top threads, ensuring diversity across articles
    selected = []
    articles_seen = set()
    
    # First pass: get top from each article
    for thread in all_threads:
        if thread["article"] not in articles_seen:
            selected.append(thread)
            articles_seen.add(thread["article"])
            if len(selected) >= n_excerpts // 2:
                break
    
    # Second pass: fill remaining with highest scores
    for thread in all_threads:
        if thread not in selected:
            selected.append(thread)
            if len(selected) >= n_excerpts:
                break
    
    print(f"  Found {len(all_threads)} candidate threads")
    print(f"  Selected {len(selected)} excerpts")
    
    return selected


def format_for_coding(excerpts, cluster_name):
    """Format excerpts for LLM coding."""
    coding_items = []
    
    for i, excerpt in enumerate(excerpts, 1):
        # Truncate content for coding
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
    print("Sampling Talk Page Excerpts for CDA Coding")
    print("=" * 60)
    
    # Sample from both clusters
    iran_excerpts = sample_excerpts("iran_cluster", n_excerpts=50)
    gaza_excerpts = sample_excerpts("gaza_cluster", n_excerpts=50)
    
    # Format for coding
    iran_items = format_for_coding(iran_excerpts, "iran")
    gaza_items = format_for_coding(gaza_excerpts, "gaza")
    
    all_items = iran_items + gaza_items
    
    # Save coding items
    with open(CODING_DIR / "excerpts_for_coding.json", "w") as f:
        json.dump(all_items, f, indent=2)
    
    # Save summary
    summary = {
        "total_excerpts": len(all_items),
        "iran_excerpts": len(iran_items),
        "gaza_excerpts": len(gaza_items),
        "iran_articles": list(set(e["article"] for e in iran_items)),
        "gaza_articles": list(set(e["article"] for e in gaza_items)),
        "category_distribution": defaultdict(int)
    }
    
    for item in all_items:
        for cat in item["categories_detected"]:
            summary["category_distribution"][cat] += 1
    
    summary["category_distribution"] = dict(summary["category_distribution"])
    
    with open(CODING_DIR / "sampling_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 60)
    print("SAMPLING SUMMARY")
    print("=" * 60)
    print(f"Total excerpts: {summary['total_excerpts']}")
    print(f"Iran: {summary['iran_excerpts']} from {len(summary['iran_articles'])} articles")
    print(f"Gaza: {summary['gaza_excerpts']} from {len(summary['gaza_articles'])} articles")
    print("\nCategory distribution:")
    for cat, count in sorted(summary["category_distribution"].items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    
    # Show sample excerpt
    print("\n" + "=" * 60)
    print("SAMPLE EXCERPT (highest scored):")
    print("=" * 60)
    top = all_items[0]
    print(f"ID: {top['id']}")
    print(f"Article: {top['article']}")
    print(f"Section: {top['section']}")
    print(f"Score: {top['dispute_score']}")
    print(f"Categories: {top['categories_detected']}")
    print(f"\nContent preview:\n{top['content'][:500]}...")


if __name__ == "__main__":
    main()
