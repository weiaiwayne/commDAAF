#!/usr/bin/env python3
"""
Analyze Claude's coding results for Congressional AI Framing study.
"""

import json
from collections import Counter
from pathlib import Path

# Load Claude's codes
with open('claude_codes_final.json') as f:
    codes = json.load(f)

# Load sample segments for metadata
with open('sample_segments.json') as f:
    segments = json.load(f)

# Create lookup
seg_lookup = {s['id']: s for s in segments}

# Merge codes with segment metadata
for c in codes:
    seg = seg_lookup.get(c['id'], {})
    c['period'] = seg.get('period', 'unknown')
    c['chamber'] = seg.get('chamber', 'unknown')
    c['date'] = seg.get('date', 'unknown')

# Primary frame distribution
print("=" * 60)
print("CLAUDE CODING RESULTS: CONGRESSIONAL AI FRAMING")
print("=" * 60)
print(f"\nTotal segments coded: {len(codes)}")

print("\n## Primary Frame Distribution")
primary_dist = Counter(c['primary_frame'] for c in codes)
for frame, count in primary_dist.most_common():
    pct = 100 * count / len(codes)
    print(f"  {frame}: {count:3d} ({pct:5.1f}%)")

# Valence distribution
print("\n## Valence Distribution")
valence_dist = Counter(c['valence'] for c in codes)
for val, count in valence_dist.most_common():
    pct = 100 * count / len(codes)
    print(f"  {val}: {count:3d} ({pct:5.1f}%)")

# Confidence distribution
print("\n## Confidence Distribution")
conf_dist = Counter(c['confidence'] for c in codes)
for conf, count in conf_dist.most_common():
    pct = 100 * count / len(codes)
    print(f"  {conf}: {count:3d} ({pct:5.1f}%)")

# Pre vs Post ChatGPT analysis
print("\n## H1: Existential Framing by Period")
pre = [c for c in codes if c['period'] == 'pre_chatgpt']
post = [c for c in codes if c['period'] == 'post_chatgpt']

pre_exi = sum(1 for c in pre if c['primary_frame'] == 'EXI')
post_exi = sum(1 for c in post if c['primary_frame'] == 'EXI')

print(f"  Pre-ChatGPT:  {pre_exi}/{len(pre)} = {100*pre_exi/len(pre):.1f}% EXI")
print(f"  Post-ChatGPT: {post_exi}/{len(post)} = {100*post_exi/len(post):.1f}% EXI")

# All frames by period
print("\n## Frame Distribution by Period")
print("\nPre-ChatGPT (N={}):".format(len(pre)))
pre_dist = Counter(c['primary_frame'] for c in pre)
for frame, count in pre_dist.most_common():
    pct = 100 * count / len(pre)
    print(f"  {frame}: {count:3d} ({pct:5.1f}%)")

print("\nPost-ChatGPT (N={}):".format(len(post)))
post_dist = Counter(c['primary_frame'] for c in post)
for frame, count in post_dist.most_common():
    pct = 100 * count / len(post)
    print(f"  {frame}: {count:3d} ({pct:5.1f}%)")

# Chamber analysis (H2)
print("\n## H2: Regulation Framing by Chamber")
house = [c for c in codes if c['chamber'] == 'house']
senate = [c for c in codes if c['chamber'] == 'senate']

house_reg = sum(1 for c in house if c['primary_frame'] == 'REG')
senate_reg = sum(1 for c in senate if c['primary_frame'] == 'REG')

print(f"  House:  {house_reg}/{len(house)} = {100*house_reg/len(house):.1f}% REG")
print(f"  Senate: {senate_reg}/{len(senate)} = {100*senate_reg/len(senate):.1f}% REG")

# Security framing over time (H3)
print("\n## H3: Security Framing Over Time")
# Group by year
year_sec = {}
for c in codes:
    year = c.get('date', '2020')[:4]
    if year not in year_sec:
        year_sec[year] = {'sec': 0, 'total': 0}
    year_sec[year]['total'] += 1
    if c['primary_frame'] == 'SEC':
        year_sec[year]['sec'] += 1

for year in sorted(year_sec.keys()):
    data = year_sec[year]
    pct = 100 * data['sec'] / data['total'] if data['total'] > 0 else 0
    print(f"  {year}: {data['sec']}/{data['total']} = {pct:.1f}% SEC")

print("\n" + "=" * 60)
print("NOTE: 3-model validation (GLM + Kimi) pending")
print("=" * 60)
