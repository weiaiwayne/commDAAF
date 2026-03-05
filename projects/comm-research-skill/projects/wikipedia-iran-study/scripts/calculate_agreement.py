#!/usr/bin/env python3
"""
Calculate inter-model agreement for epistemic injustice coding.
"""

import json
from pathlib import Path
from collections import defaultdict

CODING_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study/coding")

CONSTRUCTS = [
    "testimonial_injustice",
    "hermeneutical_injustice", 
    "epistemic_dispossession",
    "policy_weaponization",
    "naming_dispute",
    "source_hierarchy"
]


def load_codings(filename):
    """Load coding results from JSON file."""
    with open(CODING_DIR / filename) as f:
        data = json.load(f)
    return {item["id"]: item for item in data}


def calculate_agreement(codes1, codes2, construct):
    """Calculate agreement rate for a construct."""
    agree = 0
    total = 0
    
    for id_ in codes1:
        if id_ in codes2:
            v1 = codes1[id_].get(construct, 0)
            v2 = codes2[id_].get(construct, 0)
            if v1 == v2:
                agree += 1
            total += 1
    
    return agree / total if total > 0 else 0


def calculate_cohens_kappa(codes1, codes2, construct):
    """Calculate Cohen's kappa for a construct."""
    # Count contingency table
    a = b = c = d = 0  # a=both 1, b=1-0, c=0-1, d=both 0
    
    for id_ in codes1:
        if id_ in codes2:
            v1 = codes1[id_].get(construct, 0)
            v2 = codes2[id_].get(construct, 0)
            
            if v1 == 1 and v2 == 1:
                a += 1
            elif v1 == 1 and v2 == 0:
                b += 1
            elif v1 == 0 and v2 == 1:
                c += 1
            else:
                d += 1
    
    n = a + b + c + d
    if n == 0:
        return 0
    
    # Observed agreement
    po = (a + d) / n
    
    # Expected agreement
    pe = ((a + b) * (a + c) + (c + d) * (b + d)) / (n * n)
    
    # Kappa
    if pe == 1:
        return 1.0
    
    kappa = (po - pe) / (1 - pe)
    return kappa


def main():
    print("Calculating Inter-Model Agreement")
    print("=" * 60)
    
    # Load available codings
    available_files = list(CODING_DIR.glob("*_batch_1.json"))
    print(f"Found coding files: {[f.name for f in available_files]}")
    
    codings = {}
    for f in available_files:
        model = f.stem.replace("_batch_1", "")
        codings[model] = load_codings(f.name)
        print(f"Loaded {len(codings[model])} codings from {model}")
    
    # Calculate pairwise agreement
    models = list(codings.keys())
    
    print("\n" + "=" * 60)
    print("AGREEMENT BY CONSTRUCT")
    print("=" * 60)
    
    results = {}
    
    for i, m1 in enumerate(models):
        for m2 in models[i+1:]:
            print(f"\n{m1.upper()} vs {m2.upper()}:")
            
            pair_results = {}
            for construct in CONSTRUCTS:
                agreement = calculate_agreement(codings[m1], codings[m2], construct)
                kappa = calculate_cohens_kappa(codings[m1], codings[m2], construct)
                pair_results[construct] = {"agreement": agreement, "kappa": kappa}
                print(f"  {construct}: {agreement:.0%} agree, κ={kappa:.2f}")
            
            # Overall
            total_agree = sum(r["agreement"] for r in pair_results.values()) / len(pair_results)
            total_kappa = sum(r["kappa"] for r in pair_results.values()) / len(pair_results)
            print(f"  OVERALL: {total_agree:.0%} agree, κ={total_kappa:.2f}")
            
            results[f"{m1}_vs_{m2}"] = pair_results
    
    # Summary of disagreements
    print("\n" + "=" * 60)
    print("NOTABLE DISAGREEMENTS")
    print("=" * 60)
    
    for m1, m2 in [(models[0], models[1])] if len(models) >= 2 else []:
        for id_ in codings[m1]:
            if id_ in codings[m2]:
                disagreements = []
                for c in CONSTRUCTS:
                    v1 = codings[m1][id_].get(c, 0)
                    v2 = codings[m2][id_].get(c, 0)
                    if v1 != v2:
                        disagreements.append(f"{c}: {m1}={v1}, {m2}={v2}")
                
                if len(disagreements) >= 2:
                    print(f"\n{id_}: {len(disagreements)} disagreements")
                    for d in disagreements:
                        print(f"  - {d}")
    
    # Save results
    with open(CODING_DIR / "agreement_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Results saved to coding/agreement_results.json")


if __name__ == "__main__":
    main()
