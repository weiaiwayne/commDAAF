#!/usr/bin/env python3
"""
Phase 2: Computational Analysis
- Revert detection and network building
- Temporal analysis
- Editor profiling
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import csv

BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
DATA_DIR = BASE_DIR / "data"
ANALYSIS_DIR = BASE_DIR / "analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)

def load_cluster_revisions(cluster_name):
    """Load all revision data for a cluster."""
    cluster_dir = DATA_DIR / cluster_name / "revisions"
    all_revisions = []
    
    for rev_file in cluster_dir.glob("*.json"):
        with open(rev_file) as f:
            data = json.load(f)
            article_title = data.get("title", rev_file.stem)
            for rev in data.get("revisions", []):
                rev["article"] = article_title
                all_revisions.append(rev)
    
    return all_revisions


def detect_reverts(revisions):
    """
    Detect reverts based on edit comments.
    Returns list of (reverter, reverted_user, article, timestamp) tuples.
    """
    revert_patterns = [
        r"Reverted.*edits? by \[\[.*?:([^\]|]+)",  # "Reverted edits by [[User:Name"
        r"Undid revision.*by \[\[.*?:([^\]|]+)",   # "Undid revision by [[User:Name"
        r"rv\s+([^\s]+)",                           # "rv username"
        r"Revert(?:ed|ing)?\s+(?:to|by)\s+([^\s]+)", # "Reverted to/by username"
    ]
    
    reverts = []
    for rev in revisions:
        comment = rev.get("comment", "")
        reverter = rev.get("user", "Unknown")
        timestamp = rev.get("timestamp", "")
        article = rev.get("article", "Unknown")
        
        for pattern in revert_patterns:
            match = re.search(pattern, comment, re.IGNORECASE)
            if match:
                reverted_user = match.group(1).strip()
                # Clean up username
                reverted_user = reverted_user.replace("_", " ").split("|")[0]
                reverts.append({
                    "reverter": reverter,
                    "reverted": reverted_user,
                    "article": article,
                    "timestamp": timestamp,
                    "comment": comment[:200]
                })
                break
    
    return reverts


def build_revert_network(reverts):
    """
    Build editor-to-editor revert network.
    Returns edge list with weights.
    """
    edges = defaultdict(int)
    for rev in reverts:
        edge = (rev["reverter"], rev["reverted"])
        edges[edge] += 1
    
    return [{"source": e[0], "target": e[1], "weight": w} for e, w in edges.items()]


def analyze_editors(revisions):
    """Profile editors by activity."""
    editor_stats = defaultdict(lambda: {
        "edit_count": 0,
        "articles": set(),
        "first_edit": None,
        "last_edit": None,
        "reverts_made": 0,
        "reverts_received": 0
    })
    
    for rev in revisions:
        user = rev.get("user", "Unknown")
        timestamp = rev.get("timestamp", "")
        article = rev.get("article", "Unknown")
        
        stats = editor_stats[user]
        stats["edit_count"] += 1
        stats["articles"].add(article)
        
        if stats["first_edit"] is None or timestamp < stats["first_edit"]:
            stats["first_edit"] = timestamp
        if stats["last_edit"] is None or timestamp > stats["last_edit"]:
            stats["last_edit"] = timestamp
    
    # Convert sets to counts
    for user, stats in editor_stats.items():
        stats["article_count"] = len(stats["articles"])
        stats["articles"] = list(stats["articles"])[:10]  # Keep top 10
    
    return dict(editor_stats)


def temporal_analysis(revisions):
    """Analyze edit patterns over time."""
    daily_counts = defaultdict(int)
    hourly_counts = defaultdict(int)
    
    for rev in revisions:
        timestamp = rev.get("timestamp", "")
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                daily_counts[dt.strftime("%Y-%m-%d")] += 1
                hourly_counts[dt.hour] += 1
            except:
                pass
    
    return {
        "daily": dict(sorted(daily_counts.items())),
        "hourly": dict(sorted(hourly_counts.items()))
    }


def analyze_cluster(cluster_name):
    """Full analysis for a cluster."""
    print(f"\n{'='*60}")
    print(f"Analyzing {cluster_name}")
    print(f"{'='*60}")
    
    # Load data
    revisions = load_cluster_revisions(cluster_name)
    print(f"Loaded {len(revisions)} revisions")
    
    # Detect reverts
    reverts = detect_reverts(revisions)
    print(f"Detected {len(reverts)} reverts")
    
    # Build revert network
    network = build_revert_network(reverts)
    print(f"Built network with {len(network)} edges")
    
    # Analyze editors
    editors = analyze_editors(revisions)
    print(f"Profiled {len(editors)} unique editors")
    
    # Update editor stats with revert counts
    for rev in reverts:
        if rev["reverter"] in editors:
            editors[rev["reverter"]]["reverts_made"] += 1
        if rev["reverted"] in editors:
            editors[rev["reverted"]]["reverts_received"] += 1
    
    # Temporal analysis
    temporal = temporal_analysis(revisions)
    print(f"Temporal analysis: {len(temporal['daily'])} days of activity")
    
    # Save results
    output_dir = ANALYSIS_DIR / cluster_name
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "reverts.json", "w") as f:
        json.dump(reverts, f, indent=2)
    
    with open(output_dir / "revert_network.json", "w") as f:
        json.dump(network, f, indent=2)
    
    with open(output_dir / "editors.json", "w") as f:
        json.dump(editors, f, indent=2, default=list)
    
    with open(output_dir / "temporal.json", "w") as f:
        json.dump(temporal, f, indent=2)
    
    # Summary stats
    summary = {
        "cluster": cluster_name,
        "total_revisions": len(revisions),
        "total_reverts": len(reverts),
        "unique_editors": len(editors),
        "network_edges": len(network),
        "top_reverters": sorted(
            [(u, s["reverts_made"]) for u, s in editors.items()],
            key=lambda x: x[1], reverse=True
        )[:10],
        "most_reverted": sorted(
            [(u, s["reverts_received"]) for u, s in editors.items()],
            key=lambda x: x[1], reverse=True
        )[:10],
        "most_active": sorted(
            [(u, s["edit_count"]) for u, s in editors.items()],
            key=lambda x: x[1], reverse=True
        )[:10]
    }
    
    with open(output_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    
    return summary


def main():
    print("Phase 2: Computational Analysis")
    print("=" * 60)
    
    iran_summary = analyze_cluster("iran_cluster")
    gaza_summary = analyze_cluster("gaza_cluster")
    
    # Print key findings
    print("\n" + "=" * 60)
    print("KEY FINDINGS")
    print("=" * 60)
    
    for name, summary in [("IRAN", iran_summary), ("GAZA", gaza_summary)]:
        print(f"\n{name} CLUSTER:")
        print(f"  Revisions: {summary['total_revisions']}")
        print(f"  Reverts detected: {summary['total_reverts']}")
        print(f"  Unique editors: {summary['unique_editors']}")
        print(f"  Network edges: {summary['network_edges']}")
        print(f"  Top reverters: {summary['top_reverters'][:3]}")
        print(f"  Most reverted: {summary['most_reverted'][:3]}")


if __name__ == "__main__":
    main()
