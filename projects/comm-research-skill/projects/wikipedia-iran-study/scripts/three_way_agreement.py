#!/usr/bin/env python3
"""Calculate three-way agreement between Claude, GLM, and Kimi."""

import json
from pathlib import Path

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
    with open(CODING_DIR / filename) as f:
        return {item["id"]: item for item in json.load(f)}

def main():
    claude = load_codings("claude_batch_1.json")
    kimi = load_codings("kimi_batch_1.json")
    glm = load_codings("glm_batch_1.json")
    
    # Find common IDs
    common_ids = set(claude.keys()) & set(kimi.keys()) & set(glm.keys())
    print(f"Common excerpts: {sorted(common_ids)}")
    print(f"\n{'='*60}")
    print("THREE-WAY AGREEMENT (Claude + GLM + Kimi)")
    print("="*60)
    
    for construct in CONSTRUCTS:
        all_agree = 0
        two_agree = 0
        none_agree = 0
        
        for id_ in common_ids:
            c = claude[id_].get(construct, 0)
            k = kimi[id_].get(construct, 0)
            g = glm[id_].get(construct, 0)
            
            if c == k == g:
                all_agree += 1
            elif c == k or c == g or k == g:
                two_agree += 1
            else:
                none_agree += 1
        
        total = len(common_ids)
        print(f"{construct}:")
        print(f"  All 3 agree: {all_agree}/{total} ({all_agree/total:.0%})")
        print(f"  2 of 3 agree: {two_agree}/{total}")
        print(f"  None agree: {none_agree}/{total}")
    
    # Show detailed comparison
    print(f"\n{'='*60}")
    print("DETAILED COMPARISON")
    print("="*60)
    
    for id_ in sorted(common_ids):
        print(f"\n{id_}:")
        for c in CONSTRUCTS:
            cv = claude[id_].get(c, 0)
            kv = kimi[id_].get(c, 0)
            gv = glm[id_].get(c, 0)
            
            if cv == kv == gv:
                status = "✓" if cv == 1 else "·"
            else:
                status = f"C:{cv} K:{kv} G:{gv}"
            
            print(f"  {c[:20]:20s}: {status}")

if __name__ == "__main__":
    main()
