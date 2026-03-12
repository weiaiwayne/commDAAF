#!/usr/bin/env python3
"""
Extract speaker segments from congressional hearing transcripts
and generate stratified sample for coding.
"""

import json
import re
import random
from pathlib import Path
from collections import defaultdict

DATA_DIR = Path("data")
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
OUTPUT_DIR = Path("coding")

# Sampling parameters
SAMPLE_SIZE = 200
MIN_SEGMENT_WORDS = 100
MAX_SEGMENTS_PER_HEARING = 3

def parse_speaker_turns(text: str, hearing_id: str) -> list:
    """Parse transcript into speaker turns."""
    segments = []
    
    # Pattern for speaker names in congressional transcripts
    # Matches: "    Chair Blumenthal." or "    Mr. ALTMAN." or "    Senator HAWLEY."
    speaker_pattern = r'\n\s{2,}((?:Chair|Chairman|Chairwoman|Senator|Representative|Mr\.|Ms\.|Mrs\.|Dr\.|The Chair|The Chairman|The Chairwoman)\s+[A-Za-z\-\']+)\.'
    
    # Split by speaker
    parts = re.split(speaker_pattern, text)
    
    current_speaker = None
    for i, part in enumerate(parts):
        part = part.strip()
        
        # Check if this is a speaker name
        if re.match(r'^(?:Chair|Chairman|Chairwoman|Senator|Representative|Mr|Ms|Mrs|Dr|The Chair|The Chairman|The Chairwoman)', part):
            current_speaker = part
        elif current_speaker and len(part) > 50:
            # This is the speaker's content
            content = part
            
            # Clean up the content
            content = re.sub(r'\[.*?\]', '', content)  # Remove bracketed notes
            content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
            content = content.strip()
            
            # Skip table of contents, page numbers, etc.
            if content.startswith('Page') or '.....' in content[:100]:
                continue
            
            word_count = len(content.split())
            
            if word_count >= MIN_SEGMENT_WORDS:
                segments.append({
                    "hearing_id": hearing_id,
                    "speaker": current_speaker,
                    "text": content[:2000],  # Truncate very long segments
                    "word_count": word_count,
                    "full_text": content
                })
    
    return segments

def classify_hearing(metadata: dict) -> dict:
    """Classify hearing by period and chamber."""
    date = metadata.get("date_issued", "")
    pkg_id = metadata.get("package_id", "")
    
    # Determine period
    year = int(date[:4]) if date else 0
    if year <= 2022:
        period = "pre_chatgpt"
    else:
        period = "post_chatgpt"
    
    # Determine chamber
    if "hhrg" in pkg_id.lower():
        chamber = "house"
    elif "shrg" in pkg_id.lower():
        chamber = "senate"
    else:
        chamber = "joint"
    
    # Sub-period for post-ChatGPT
    if period == "post_chatgpt":
        if year == 2023:
            sub_period = "2023"
        else:
            sub_period = "2024_25"
    else:
        sub_period = "pre"
    
    return {
        "period": period,
        "chamber": chamber,
        "sub_period": sub_period,
        "year": year,
        "stratum": f"{period}_{chamber}_{sub_period}"
    }

def main():
    print("=" * 60)
    print("Extracting Speaker Segments")
    print("=" * 60)
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Load metadata
    with open(DATA_DIR / "hearings_metadata.json") as f:
        metadata = json.load(f)
    
    # Create lookup
    meta_lookup = {h["package_id"]: h for h in metadata}
    
    # Extract all segments
    all_segments = []
    segments_by_stratum = defaultdict(list)
    
    for transcript_file in sorted(TRANSCRIPTS_DIR.glob("*.txt")):
        hearing_id = transcript_file.stem
        
        # Get metadata
        meta = meta_lookup.get(hearing_id, {})
        classification = classify_hearing(meta)
        
        # Parse transcript
        text = transcript_file.read_text(encoding="utf-8", errors="ignore")
        segments = parse_speaker_turns(text, hearing_id)
        
        # Add metadata to segments
        for seg in segments:
            seg.update({
                "title": meta.get("title", ""),
                "date": meta.get("date_issued", ""),
                **classification
            })
            all_segments.append(seg)
            segments_by_stratum[classification["stratum"]].append(seg)
        
        if segments:
            print(f"  {hearing_id}: {len(segments)} segments")
    
    print(f"\nTotal segments extracted: {len(all_segments)}")
    print(f"\nBy stratum:")
    for stratum, segs in sorted(segments_by_stratum.items()):
        print(f"  {stratum}: {len(segs)}")
    
    # Stratified sampling
    print(f"\n{'=' * 60}")
    print("Generating Stratified Sample")
    print("=" * 60)
    
    # Define strata and targets
    strata_targets = {
        "pre_chatgpt_house_pre": 30,
        "pre_chatgpt_senate_pre": 30,
        "post_chatgpt_house_2023": 35,
        "post_chatgpt_senate_2023": 35,
        "post_chatgpt_house_2024_25": 35,
        "post_chatgpt_senate_2024_25": 35,
    }
    
    sample = []
    hearing_counts = defaultdict(int)
    
    for stratum, target in strata_targets.items():
        available = segments_by_stratum.get(stratum, [])
        
        # Filter to respect max per hearing
        filtered = []
        for seg in available:
            if hearing_counts[seg["hearing_id"]] < MAX_SEGMENTS_PER_HEARING:
                filtered.append(seg)
        
        # Sample
        n_sample = min(target, len(filtered))
        if filtered:
            sampled = random.sample(filtered, n_sample)
            for seg in sampled:
                hearing_counts[seg["hearing_id"]] += 1
            sample.extend(sampled)
            print(f"  {stratum}: sampled {n_sample}/{target} (available: {len(available)})")
        else:
            print(f"  {stratum}: NO SEGMENTS AVAILABLE")
    
    print(f"\nTotal sample size: {len(sample)}")
    
    # Prepare for coding (remove full_text, keep truncated version)
    coding_sample = []
    for i, seg in enumerate(sample):
        coding_sample.append({
            "id": i + 1,
            "hearing_id": seg["hearing_id"],
            "title": seg["title"][:80],
            "date": seg["date"],
            "speaker": seg["speaker"],
            "chamber": seg["chamber"],
            "period": seg["period"],
            "text": seg["text"],
            "word_count": seg["word_count"],
            # Coding fields (to be filled)
            "primary_frame": None,
            "secondary_frames": [],
            "valence": None,
            "confidence": None,
            "notes": None
        })
    
    # Save sample
    sample_path = OUTPUT_DIR / "sample_segments.json"
    with open(sample_path, "w", encoding="utf-8") as f:
        json.dump(coding_sample, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Saved sample to {sample_path}")
    
    # Save all segments for reference
    all_segments_path = OUTPUT_DIR / "all_segments.json"
    with open(all_segments_path, "w", encoding="utf-8") as f:
        # Remove full_text to save space
        for seg in all_segments:
            seg.pop("full_text", None)
        json.dump(all_segments, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved all segments to {all_segments_path}")
    
    # Generate coding instructions
    instructions = """# Coding Instructions

## Frame Codes

| Code | Frame | Key Indicators |
|------|-------|----------------|
| ECO | Economic Opportunity | innovation, competitiveness, growth, jobs creation |
| SEC | National Security | China, defense, adversaries, military, intelligence |
| EXI | Existential Risk | alignment, extinction, superintelligence, catastrophic |
| REG | Regulation/Governance | oversight, accountability, transparency, legislation |
| CIV | Civil Rights | bias, discrimination, privacy, surveillance |
| LAB | Labor/Automation | displacement, workforce, reskilling, jobs loss |
| HEA | Healthcare | diagnosis, treatment, patients, medical |
| CON | Consumer Protection | scams, fraud, deepfakes, misinformation |

## Valence Codes

| Code | Meaning |
|------|---------|
| POS | Positive (opportunity, benefit) |
| NEG | Negative (risk, threat, harm) |
| NEU | Neutral/balanced |

## Output Format

For each segment, provide:
```json
{
  "id": 1,
  "primary_frame": "ECO",
  "secondary_frames": ["SEC"],
  "valence": "POS",
  "confidence": "high",
  "notes": "Speaker emphasizes US competitiveness"
}
```
"""
    
    instructions_path = OUTPUT_DIR / "CODING_INSTRUCTIONS.md"
    instructions_path.write_text(instructions)
    print(f"✓ Saved coding instructions to {instructions_path}")
    
    # Summary stats
    print(f"\n{'=' * 60}")
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Total segments: {len(all_segments)}")
    print(f"Sample size: {len(coding_sample)}")
    print(f"Unique hearings in sample: {len(set(s['hearing_id'] for s in coding_sample))}")

if __name__ == "__main__":
    random.seed(42)  # Reproducibility
    main()
