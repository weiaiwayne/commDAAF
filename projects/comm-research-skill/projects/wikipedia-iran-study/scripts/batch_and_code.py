#!/usr/bin/env python3
"""
Split new excerpts into sub-batches for multi-model coding.
"""

import json
from pathlib import Path

BASE_DIR = Path("/root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study")
CODING_DIR = BASE_DIR / "coding"

def main():
    # Load new excerpts
    with open(CODING_DIR / "excerpts_new_batch.json") as f:
        excerpts = json.load(f)
    
    print(f"Total new excerpts: {len(excerpts)}")
    
    # Split into batches of 25
    batch_size = 25
    batches = []
    for i in range(0, len(excerpts), batch_size):
        batch = excerpts[i:i+batch_size]
        batches.append(batch)
    
    print(f"Created {len(batches)} batches")
    
    # Save each batch
    for i, batch in enumerate(batches, 1):
        batch_file = CODING_DIR / f"new_batch_{i}.json"
        with open(batch_file, "w") as f:
            json.dump(batch, f, indent=2)
        print(f"  Batch {i}: {len(batch)} excerpts -> {batch_file.name}")
    
    # Save batch manifest
    manifest = {
        "total_excerpts": len(excerpts),
        "batch_size": batch_size,
        "num_batches": len(batches),
        "batches": [
            {
                "batch_num": i,
                "file": f"new_batch_{i}.json",
                "count": len(batch),
                "ids": [e["id"] for e in batch]
            }
            for i, batch in enumerate(batches, 1)
        ]
    }
    
    with open(CODING_DIR / "batch_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nManifest saved to batch_manifest.json")
    print("\nReady for 3-model coding!")


if __name__ == "__main__":
    main()
