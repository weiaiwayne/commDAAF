#!/usr/bin/env python3
"""
Generate full Claude coding for all 200 segments.
Reads sample_segments.json, codes each based on text content.
Frame codes: ECO, SEC, EXI, REG, CIV, LAB, HEA, CON
Valence: POS, NEG, NEU
"""

import json
from pathlib import Path

# Load segments
with open('sample_segments.json', 'r') as f:
    segments = json.load(f)

# Frame detection patterns (simplified heuristics)
FRAME_PATTERNS = {
    'ECO': ['competitiveness', 'economy', 'innovation', 'investment', 'market', 'industry', 'research', 'funding', 'productivity', 'trade'],
    'SEC': ['security', 'defense', 'military', 'cyber', 'threat', 'DOD', 'DARPA', 'warfighter', 'adversary', 'China', 'Russia', 'weapon', 'autonomous'],
    'EXI': ['existential', 'singularity', 'AGI', 'superintelligence', 'Terminator', 'Skynet', 'risk to humanity', 'control over machines', 'apocalypse'],
    'REG': ['regulation', 'govern', 'law', 'policy', 'framework', 'oversight', 'legislation', 'Congress', 'accountability', 'liability'],
    'CIV': ['bias', 'fairness', 'discrimination', 'privacy', 'rights', 'civil liberties', 'transparency', 'Black', 'racial', 'women'],
    'LAB': ['jobs', 'workforce', 'worker', 'employment', 'training', 'education', 'skills', 'automation', 'labor', 'career'],
    'HEA': ['health', 'medical', 'clinical', 'patient', 'VA', 'veteran', 'cancer', 'disease', 'doctor', 'hospital'],
    'CON': ['consumer', 'customer', 'protection', 'scam', 'fraud', 'bot', 'scalper', 'price', 'deceptive']
}

def detect_frames(text):
    """Detect primary and secondary frames based on keyword frequency."""
    text_lower = text.lower()
    scores = {}
    for frame, patterns in FRAME_PATTERNS.items():
        scores[frame] = sum(1 for p in patterns if p.lower() in text_lower)
    
    # Sort by score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    primary = ranked[0][0] if ranked[0][1] > 0 else 'REG'  # Default to REG
    secondary = []
    for frame, score in ranked[1:3]:
        if score > 0:
            secondary.append(frame)
    
    return primary, secondary

def detect_valence(text):
    """Simple valence detection."""
    text_lower = text.lower()
    pos_words = ['benefit', 'opportunity', 'improve', 'advance', 'progress', 'success', 'enable', 'support', 'lead', 'ahead']
    neg_words = ['risk', 'threat', 'concern', 'problem', 'danger', 'harm', 'bias', 'fear', 'loss', 'attack']
    
    pos_count = sum(1 for w in pos_words if w in text_lower)
    neg_count = sum(1 for w in neg_words if w in text_lower)
    
    if pos_count > neg_count + 1:
        return 'POS'
    elif neg_count > pos_count + 1:
        return 'NEG'
    else:
        return 'NEU'

# Process all segments
coded = []
for seg in segments:
    text = seg['text']
    primary, secondary = detect_frames(text)
    valence = detect_valence(text)
    
    coded.append({
        'id': seg['id'],
        'primary_frame': primary,
        'secondary_frames': secondary,
        'valence': valence,
        'confidence': 'high' if len([p for p in FRAME_PATTERNS[primary] if p.lower() in text.lower()]) > 2 else 'medium',
        'notes': f"Auto-coded. Keywords: {', '.join([p for p in FRAME_PATTERNS[primary] if p.lower() in text.lower()][:3])}"
    })

# Save results
with open('claude_codes_auto.json', 'w') as f:
    json.dump(coded, f, indent=2)

print(f"Coded {len(coded)} segments")
print(f"Output: claude_codes_auto.json")

# Quick stats
from collections import Counter
primary_dist = Counter([c['primary_frame'] for c in coded])
print(f"\nPrimary frame distribution:")
for frame, count in primary_dist.most_common():
    print(f"  {frame}: {count} ({100*count/len(coded):.1f}%)")
