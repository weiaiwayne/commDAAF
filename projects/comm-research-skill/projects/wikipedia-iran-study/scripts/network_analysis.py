#!/usr/bin/env python3
"""
Network Analysis: Identify editor camps from revert patterns.
"""

import json
from pathlib import Path
from collections import defaultdict
import math

ANALYSIS_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study/analysis")

def load_network(cluster_name):
    """Load revert network for a cluster."""
    with open(ANALYSIS_DIR / cluster_name / "revert_network.json") as f:
        return json.load(f)

def load_editors(cluster_name):
    """Load editor profiles."""
    with open(ANALYSIS_DIR / cluster_name / "editors.json") as f:
        return json.load(f)

def simple_community_detection(edges, min_weight=2):
    """
    Simple community detection based on mutual reverts.
    Editors who revert each other are likely in opposing camps.
    """
    # Build adjacency with weights
    graph = defaultdict(lambda: defaultdict(int))
    for e in edges:
        if e["weight"] >= min_weight:
            graph[e["source"]][e["target"]] += e["weight"]
            graph[e["target"]][e["source"]] += e["weight"]
    
    # Find editors with mutual reverts (conflict pairs)
    conflict_pairs = []
    seen = set()
    for u in graph:
        for v in graph[u]:
            if graph[v].get(u, 0) > 0:  # Mutual revert
                pair = tuple(sorted([u, v]))
                if pair not in seen:
                    conflict_pairs.append({
                        "editor1": pair[0],
                        "editor2": pair[1],
                        "mutual_reverts": graph[u][v] + graph[v][u]
                    })
                    seen.add(pair)
    
    conflict_pairs.sort(key=lambda x: x["mutual_reverts"], reverse=True)
    return conflict_pairs

def identify_prolific_reverters(edges, editors, top_n=20):
    """Identify most active reverters."""
    revert_counts = defaultdict(int)
    for e in edges:
        revert_counts[e["source"]] += e["weight"]
    
    top_reverters = sorted(revert_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    results = []
    for user, count in top_reverters:
        editor_info = editors.get(user, {})
        results.append({
            "user": user,
            "reverts_made": count,
            "total_edits": editor_info.get("edit_count", 0),
            "articles_edited": editor_info.get("article_count", 0),
            "revert_ratio": count / max(editor_info.get("edit_count", 1), 1)
        })
    
    return results

def identify_most_reverted(edges, editors, top_n=20):
    """Identify most frequently reverted editors."""
    reverted_counts = defaultdict(int)
    for e in edges:
        reverted_counts[e["target"]] += e["weight"]
    
    top_reverted = sorted(reverted_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    results = []
    for user, count in top_reverted:
        editor_info = editors.get(user, {})
        results.append({
            "user": user,
            "times_reverted": count,
            "total_edits": editor_info.get("edit_count", 0),
            "reverted_ratio": count / max(editor_info.get("edit_count", 1), 1)
        })
    
    return results

def analyze_cluster(cluster_name):
    """Full network analysis for a cluster."""
    print(f"\n{'='*60}")
    print(f"NETWORK ANALYSIS: {cluster_name}")
    print(f"{'='*60}")
    
    edges = load_network(cluster_name)
    editors = load_editors(cluster_name)
    
    print(f"\nNetwork: {len(edges)} edges, {len(editors)} nodes")
    
    # Conflict pairs (mutual reverters)
    conflicts = simple_community_detection(edges, min_weight=1)
    print(f"\nMutual revert pairs: {len(conflicts)}")
    print("\nTop conflict pairs (potential opposing camps):")
    for c in conflicts[:10]:
        print(f"  {c['editor1']} <-> {c['editor2']}: {c['mutual_reverts']} mutual reverts")
    
    # Prolific reverters
    reverters = identify_prolific_reverters(edges, editors)
    print(f"\nTop reverters:")
    for r in reverters[:10]:
        print(f"  {r['user']}: {r['reverts_made']} reverts ({r['revert_ratio']:.1%} of edits)")
    
    # Most reverted
    reverted = identify_most_reverted(edges, editors)
    print(f"\nMost reverted editors:")
    for r in reverted[:10]:
        print(f"  {r['user']}: reverted {r['times_reverted']} times")
    
    # Save results
    results = {
        "cluster": cluster_name,
        "network_stats": {
            "edges": len(edges),
            "nodes": len(editors),
            "conflict_pairs": len(conflicts)
        },
        "top_conflict_pairs": conflicts[:20],
        "top_reverters": reverters,
        "most_reverted": reverted
    }
    
    with open(ANALYSIS_DIR / cluster_name / "network_analysis.json", "w") as f:
        json.dump(results, f, indent=2)
    
    return results

def main():
    print("Wikipedia Editor Network Analysis")
    print("=" * 60)
    
    iran_results = analyze_cluster("iran_cluster")
    gaza_results = analyze_cluster("gaza_cluster")
    
    # Cross-cluster analysis
    print(f"\n{'='*60}")
    print("CROSS-CLUSTER COMPARISON")
    print("="*60)
    
    # Find editors active in both
    iran_editors = set(load_editors("iran_cluster").keys())
    gaza_editors = set(load_editors("gaza_cluster").keys())
    shared = iran_editors & gaza_editors
    
    print(f"\nEditors in both clusters: {len(shared)}")
    
    # Check if top reverters overlap
    iran_top = {r["user"] for r in iran_results["top_reverters"][:20]}
    gaza_top = {r["user"] for r in gaza_results["top_reverters"][:20]}
    overlap = iran_top & gaza_top
    
    print(f"Top reverters in both: {overlap if overlap else 'None'}")
    
    # Save cross-cluster analysis
    cross_analysis = {
        "shared_editors": len(shared),
        "shared_editor_sample": list(shared)[:50],
        "top_reverter_overlap": list(overlap)
    }
    
    with open(ANALYSIS_DIR / "cross_cluster_analysis.json", "w") as f:
        json.dump(cross_analysis, f, indent=2)

if __name__ == "__main__":
    main()
