#!/usr/bin/env python3
"""
Multi-model framing analysis: Claude + GLM + Kimi
Each model analyzes the same dataset with identical prompts.
"""
import json
import subprocess
import os
from datetime import datetime

PROJECT_DIR = "/root/.openclaw/workspace/projects/nigeria-framing-2026"
DATA_FILE = f"{PROJECT_DIR}/data/processed/titles_for_analysis.json"
OUTPUT_DIR = f"{PROJECT_DIR}/analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
with open(DATA_FILE) as f:
    articles = json.load(f)

print(f"Loaded {len(articles)} articles for analysis")

# Prepare analysis prompt
ANALYSIS_PROMPT = f'''You are analyzing news coverage of the Christian-Fulani conflict in Nigeria.

## Dataset
{len(articles)} news article titles from various sources (GDELT + MediaCloud, Nov 2025 - Feb 2026).

## Research Questions
1. **Problem Definition**: How is the conflict framed? (religious persecution, ethnic conflict, resource competition, state failure, criminal violence)
2. **Causal Attribution**: Who/what is blamed? (Fulani actors, Islamic ideology, climate/environment, government failure)
3. **Actor Portrayal**: How are Christians vs Fulani portrayed? (victims, aggressors, communities)
4. **Solution Framing**: What remedies are implied? (military, legislative, dialogue, international, none)
5. **Source Patterns**: Do framing patterns differ by source type?

## Hypotheses to Test
- H1: Religious framing dominates over economic/structural framing
- H2: Fulani receive more blame than structural factors
- H3: Christians portrayed as victims more than Fulani
- H4: Conservative/religious sources show stronger religious framing
- H5: Nigerian sources show more diverse framing

## Article Titles by Source
'''

# Group by source
from collections import defaultdict
by_source = defaultdict(list)
for art in articles:
    by_source[art["source"]].append(art["title"])

# Add grouped titles to prompt
for source in sorted(by_source.keys(), key=lambda x: -len(by_source[x]))[:30]:
    titles = by_source[source]
    ANALYSIS_PROMPT += f"\n### {source} ({len(titles)} articles)\n"
    for t in titles[:10]:  # Limit to 10 per source
        ANALYSIS_PROMPT += f"- {t}\n"
    if len(titles) > 10:
        ANALYSIS_PROMPT += f"- ... and {len(titles)-10} more\n"

ANALYSIS_PROMPT += '''

## Task
Analyze this dataset and provide:

1. **Frame Prevalence Estimates**: For each frame type, estimate percentage of coverage
2. **Hypothesis Assessment**: For each H1-H5, assess whether supported/unsupported with evidence
3. **Source Comparison**: Compare framing across source types (conservative US, mainstream, Nigerian, religious)
4. **Key Patterns**: Notable patterns, anomalies, or insights
5. **Limitations**: Caveats about your analysis

Format your response with clear sections and quantitative estimates where possible.
'''

# Save prompt for reference
with open(f"{OUTPUT_DIR}/analysis_prompt.txt", "w") as f:
    f.write(ANALYSIS_PROMPT)

print(f"Prompt saved ({len(ANALYSIS_PROMPT)} chars)")
print(f"\nReady for multi-model analysis:")
print("1. Claude (main) - direct")
print("2. GLM-4.7 via opencode")
print("3. Kimi K2.5 via opencode")
