#!/usr/bin/env python3
"""
Code congressional hearing segments using LLM.
Outputs structured frame codes for each segment.
"""

import json
from pathlib import Path

CODING_DIR = Path("coding")

# Frame definitions for prompt
FRAME_DEFINITIONS = """
## Frame Codes

| Code | Frame | Definition | Key Indicators |
|------|-------|------------|----------------|
| ECO | Economic Opportunity | AI as driver of growth, competitiveness, jobs | innovation, leadership, competitiveness, economic growth, jobs creation, productivity |
| SEC | National Security | AI as defense/intelligence asset or threat | China, adversaries, defense, military, intelligence, strategic competition |
| EXI | Existential Risk | AI as potential civilizational threat | alignment, extinction, superintelligence, control problem, catastrophic |
| REG | Regulation/Governance | AI requiring oversight and rules | oversight, accountability, transparency, regulation, guardrails, legislation |
| CIV | Civil Rights | AI and bias, privacy, discrimination | bias, discrimination, fairness, privacy, civil liberties, surveillance |
| LAB | Labor/Automation | AI impact on workforce | displacement, automation, workforce, reskilling, jobs loss, workers |
| HEA | Healthcare | AI in medical applications | diagnosis, treatment, patients, healthcare, medical, clinical |
| CON | Consumer Protection | AI risks to consumers | scams, fraud, deepfakes, misinformation, consumer harm |

## Valence Codes
- POS: Positive framing (opportunity, benefit, progress)
- NEG: Negative framing (risk, threat, harm, concern)
- NEU: Neutral/balanced framing (descriptive, both sides)

## Confidence Levels
- high: Clear frame, obvious indicators
- medium: Frame present but less explicit
- low: Ambiguous, could be multiple frames
"""

def generate_coding_prompt(segments: list) -> str:
    """Generate prompt for coding a batch of segments."""
    prompt = f"""You are coding congressional hearing testimony for a framing analysis study.

{FRAME_DEFINITIONS}

## Instructions
1. For each segment, identify the PRIMARY frame (most dominant)
2. List any SECONDARY frames present (0-2 max)
3. Assign a VALENCE (POS/NEG/NEU)
4. Rate your CONFIDENCE (high/medium/low)
5. Add brief NOTES explaining your coding decision

## Segments to Code

"""
    for seg in segments:
        prompt += f"""
---
ID: {seg['id']}
Speaker: {seg['speaker']}
Date: {seg['date']}
Hearing: {seg['title']}

TEXT:
{seg['text']}
---
"""
    
    prompt += """

## Output Format
Return a JSON array with one object per segment:
```json
[
  {
    "id": 1,
    "primary_frame": "ECO",
    "secondary_frames": ["REG"],
    "valence": "POS",
    "confidence": "high",
    "notes": "Speaker emphasizes economic competitiveness and innovation"
  },
  ...
]
```

Code all segments now. Output ONLY the JSON array, no other text.
"""
    return prompt


def main():
    # Load segments
    with open(CODING_DIR / "sample_segments.json") as f:
        segments = json.load(f)
    
    print(f"Loaded {len(segments)} segments for coding")
    
    # Generate batch prompts
    batch_size = 25
    batches = []
    
    for i in range(0, len(segments), batch_size):
        batch = segments[i:i+batch_size]
        prompt = generate_coding_prompt(batch)
        batches.append({
            "batch_num": len(batches) + 1,
            "segment_ids": [s["id"] for s in batch],
            "prompt": prompt
        })
    
    print(f"Generated {len(batches)} batches of {batch_size} segments each")
    
    # Save batch prompts
    for batch in batches:
        batch_file = CODING_DIR / f"batch_{batch['batch_num']:02d}_prompt.txt"
        with open(batch_file, "w") as f:
            f.write(batch["prompt"])
        print(f"  Saved {batch_file}")
    
    # Save batch index
    index = {
        "total_segments": len(segments),
        "batch_size": batch_size,
        "num_batches": len(batches),
        "batches": [
            {"batch_num": b["batch_num"], "segment_ids": b["segment_ids"]}
            for b in batches
        ]
    }
    
    with open(CODING_DIR / "batch_index.json", "w") as f:
        json.dump(index, f, indent=2)
    
    print(f"\n✓ Saved batch index to {CODING_DIR / 'batch_index.json'}")
    print(f"\nReady for coding. Run each batch prompt through Claude/GLM/Kimi.")

if __name__ == "__main__":
    main()
