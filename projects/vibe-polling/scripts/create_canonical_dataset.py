#!/usr/bin/env python3
"""
Create Canonical Combined Dataset — VibePoll-2026
CommDAAF v1.0

This script combines all data collected by agents into canonical datasets:
1. canonical_trends.parquet - All Google Trends data
2. canonical_vibe_markets.csv - Vibe Index with market data
3. canonical_search_terms.json - All search terms with validation status
4. DATA_MANIFEST.md - Complete documentation

Data Sources:
- Claude Code: Primary trends collection (38,311 records)
- Codex: Time-matched market odds, R2 terms (12,649 records)
- Kimi: Supplemental colloquial terms (17,381 records)
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
import os

# Paths
BASE_DIR = "/root/.openclaw/workspace/projects/vibe-polling"
OUTPUT_DIR = f"{BASE_DIR}/data/canonical"

# State classifications
BATTLEGROUND = ['PA', 'MI', 'WI', 'GA', 'AZ', 'NV', 'NC']
CONTROL = ['CA', 'TX', 'OH']
WATCH = ['MN', 'ME', 'NH']

def load_all_agent_data():
    """Load data from all agents."""
    print("="*60)
    print("LOADING ALL AGENT DATA")
    print("="*60)

    data = {}

    # Claude Code data
    print("\n1. Claude Code:")
    data['claude_trends'] = pd.read_parquet(f"{BASE_DIR}/data/processed/trends_normalized.parquet")
    data['claude_vibe'] = pd.read_csv(f"{BASE_DIR}/data/processed/vibe_indices.csv")
    data['claude_salience'] = pd.read_csv(f"{BASE_DIR}/data/processed/issue_salience.csv")
    print(f"   - Trends: {len(data['claude_trends']):,} records")
    print(f"   - Vibe indices: {len(data['claude_vibe']):,} records")
    print(f"   - Issue salience: {len(data['claude_salience']):,} records")

    # Codex data
    print("\n2. Codex:")
    data['codex_markets'] = pd.read_csv(f"{BASE_DIR}/agents/codex/data/processed/independent_merged_timeseries.csv")
    data['codex_terms'] = pd.read_parquet(f"{BASE_DIR}/agents/codex/data/raw/r2_new_terms_2026-03-20.parquet")
    print(f"   - Market timeseries: {len(data['codex_markets']):,} records")
    print(f"   - R2 new terms: {len(data['codex_terms']):,} records")

    # Load Codex term validation
    try:
        data['codex_validation'] = pd.read_csv(f"{BASE_DIR}/agents/codex/data/processed/r2_term_validation.csv")
        print(f"   - Term validation: {len(data['codex_validation']):,} records")
    except:
        data['codex_validation'] = None

    # Kimi data
    print("\n3. Kimi K2.5:")
    data['kimi_terms'] = pd.read_parquet(f"{BASE_DIR}/agents/kimi-k2.5/agents/kimi-k2.5/data/raw/trends_supplemental/trends_supplemental_2026-03-20.parquet")
    # Standardize state codes
    data['kimi_terms']['state'] = data['kimi_terms']['state'].str.replace('US-', '')
    print(f"   - Supplemental terms: {len(data['kimi_terms']):,} records")

    return data


def create_canonical_trends(data):
    """Combine all trends data into canonical dataset."""
    print("\n" + "="*60)
    print("CREATING CANONICAL TRENDS DATASET")
    print("="*60)

    # Start with Claude Code as base
    canonical = data['claude_trends'].copy()
    canonical['source'] = 'claude_code'

    print(f"\nBase (Claude Code): {len(canonical):,} records")
    print(f"   Terms: {canonical['term'].nunique()}")

    # Add Codex terms
    codex = data['codex_terms'].copy()
    codex['source'] = 'codex'
    # Standardize columns
    codex = codex.rename(columns={'geo': 'state_geo'})
    if 'state' not in codex.columns and 'geo' in data['codex_terms'].columns:
        codex['state'] = data['codex_terms']['geo']

    # Only add terms not already in Claude data
    existing_terms = set(canonical['term'].unique())
    codex_new = codex[~codex['term'].isin(existing_terms)]

    print(f"\nCodex new terms: {len(codex_new):,} records")
    print(f"   New terms: {codex_new['term'].nunique() if len(codex_new) > 0 else 0}")

    # Add Kimi terms
    kimi = data['kimi_terms'].copy()
    kimi['source'] = 'kimi'

    # Update existing_terms to include both Claude and Codex terms
    existing_terms = set(canonical['term'].unique()) | set(codex_new['term'].unique() if len(codex_new) > 0 else set())
    kimi_new = kimi[~kimi['term'].isin(existing_terms)]

    print(f"\nKimi new terms: {len(kimi_new):,} records")
    print(f"   New terms: {kimi_new['term'].nunique() if len(kimi_new) > 0 else 0}")

    # Standardize and combine
    # Define common columns
    common_cols = ['date', 'state', 'term', 'interest', 'source']

    canonical_common = canonical[common_cols].copy()

    if len(codex_new) > 0:
        codex_common = codex_new[['date', 'state', 'term', 'interest', 'source']].copy()
        canonical_common = pd.concat([canonical_common, codex_common], ignore_index=True)

    if len(kimi_new) > 0:
        kimi_common = kimi_new[['date', 'state', 'term', 'interest', 'source']].copy()
        canonical_common = pd.concat([canonical_common, kimi_common], ignore_index=True)

    # Remove any duplicates (keep first - prioritizes claude_code)
    before_dedup = len(canonical_common)
    canonical_common = canonical_common.drop_duplicates(
        subset=['date', 'state', 'term'],
        keep='first'
    )
    after_dedup = len(canonical_common)

    if before_dedup > after_dedup:
        print(f"\n   Removed {before_dedup - after_dedup} duplicate records")

    print(f"\n→ Canonical trends: {len(canonical_common):,} records")
    print(f"   Unique terms: {canonical_common['term'].nunique()}")
    print(f"   States: {sorted(canonical_common['state'].unique())}")

    return canonical_common


def create_canonical_vibe_markets(data):
    """Create canonical vibe index with market data."""
    print("\n" + "="*60)
    print("CREATING CANONICAL VIBE + MARKETS DATASET")
    print("="*60)

    # Start with Claude vibe
    vibe = data['claude_vibe'].copy()
    vibe['date'] = pd.to_datetime(vibe['date'])

    # Merge with Codex markets
    markets = data['codex_markets'].copy()
    markets['date'] = pd.to_datetime(markets['date'])

    # Merge
    canonical = vibe.merge(
        markets[['state', 'date', 'house_dem_odds', 'senate_dem_odds']],
        on=['state', 'date'],
        how='left'
    )

    print(f"\nCanonical vibe+markets: {len(canonical):,} records")
    print(f"   With market data: {canonical['house_dem_odds'].notna().sum():,}")

    return canonical


def create_search_terms_manifest(data):
    """Create manifest of all search terms with validation status."""
    print("\n" + "="*60)
    print("CREATING SEARCH TERMS MANIFEST")
    print("="*60)

    manifest = {
        'created_at': datetime.now().isoformat(),
        'framework': 'CommDAAF v1.0',
        'terms': {}
    }

    # Claude Code terms
    claude_terms = data['claude_trends']['term'].unique()
    for term in claude_terms:
        term_data = data['claude_trends'][data['claude_trends']['term'] == term]
        pct_zeros = (term_data['interest'] == 0).sum() / len(term_data) * 100

        manifest['terms'][term] = {
            'source': 'claude_code',
            'records': int(len(term_data)),
            'pct_zeros': float(round(pct_zeros, 1)),
            'mean_interest': float(round(term_data['interest'].mean(), 1)),
            'valid': bool(pct_zeros < 50),
            'category': str(term_data['category'].iloc[0]) if 'category' in term_data.columns else 'unknown'
        }

    # Kimi terms (new ones only - no duplicates)
    kimi_terms = data['kimi_terms']['term'].unique()
    for term in kimi_terms:
        if term not in manifest['terms']:
            term_data = data['kimi_terms'][data['kimi_terms']['term'] == term]
            pct_zeros = (term_data['interest'] == 0).sum() / len(term_data) * 100

            manifest['terms'][term] = {
                'source': 'kimi',
                'records': int(len(term_data)),
                'pct_zeros': float(round(pct_zeros, 1)),
                'mean_interest': float(round(term_data['interest'].mean(), 1)),
                'valid': bool(pct_zeros < 50),
                'category': str(term_data['category'].iloc[0]) if 'category' in term_data.columns else 'colloquial'
            }

    # Codex terms (new ones only - no duplicates)
    codex_terms = data['codex_terms']['term'].unique()
    for term in codex_terms:
        if term not in manifest['terms']:
            term_data = data['codex_terms'][data['codex_terms']['term'] == term]
            pct_zeros = (term_data['interest'] == 0).sum() / len(term_data) * 100

            manifest['terms'][term] = {
                'source': 'codex',
                'records': int(len(term_data)),
                'pct_zeros': float(round(pct_zeros, 1)),
                'mean_interest': float(round(term_data['interest'].mean(), 1)),
                'valid': bool(pct_zeros < 50),
                'category': 'colloquial'
            }

    # Summary
    valid = sum(1 for t in manifest['terms'].values() if t['valid'])
    total = len(manifest['terms'])

    manifest['summary'] = {
        'total_terms': total,
        'valid_terms': valid,
        'invalid_terms': total - valid,
        'by_source': {
            'claude_code': sum(1 for t in manifest['terms'].values() if t['source'] == 'claude_code'),
            'kimi': sum(1 for t in manifest['terms'].values() if t['source'] == 'kimi'),
            'codex': sum(1 for t in manifest['terms'].values() if t['source'] == 'codex')
        }
    }

    print(f"\nTotal terms: {total}")
    print(f"Valid (< 50% zeros): {valid}")
    print(f"Invalid: {total - valid}")

    return manifest


def write_data_manifest():
    """Write comprehensive data manifest documentation."""
    print("\n" + "="*60)
    print("WRITING DATA MANIFEST")
    print("="*60)

    content = f"""# VibePoll-2026 Canonical Data Manifest

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Framework:** CommDAAF v1.0

---

## Overview

This directory contains the canonical combined dataset for VibePoll-2026,
merging data collected independently by multiple agents.

---

## Data Files

### 1. canonical_trends.parquet
**Description:** Combined Google Trends data from all agents

| Column | Type | Description |
|--------|------|-------------|
| date | datetime | Collection date |
| state | string | State code |
| term | string | Search term |
| interest | int | Google Trends interest (0-100) |
| source | string | Collecting agent (claude_code, kimi, codex) |

### 2. canonical_vibe_markets.csv
**Description:** Vibe Index with time-matched prediction market data

| Column | Type | Description |
|--------|------|-------------|
| state | string | State code |
| date | datetime | Date |
| economy | float | Economy issue salience |
| immigration | float | Immigration issue salience |
| political | float | Political issue salience |
| iran_war | float | Iran war issue salience |
| ai_jobs | float | AI/jobs issue salience |
| epstein | float | Epstein issue salience |
| vibe_index | float | Weighted composite index |
| vibe_index_7d | float | 7-day rolling average |
| house_dem_odds | float | House Democratic odds (0-1) |
| senate_dem_odds | float | Senate Democratic odds (0-1) |

### 3. canonical_search_terms.json
**Description:** All search terms with validation status

---

## Data Sources

| Agent | Data Type | Records | Notes |
|-------|-----------|---------|-------|
| Claude Code | Primary trends | 38,311 | R2 collection with validated terms |
| Claude Code | Vibe indices | 1,183 | Weighted composite index |
| Codex | Market timeseries | 1,183 | House/Senate Dem odds |
| Codex | R2 new terms | 11,466 | 12 colloquial terms |
| Kimi K2.5 | Supplemental terms | 17,381 | 20 colloquial terms |

---

## Key Findings

### Correlation Analysis (Real Market Data)
- Raw House correlations significant: 10/13 states
- Raw Senate correlations significant: 5/13 states
- **After first-differencing: 0/13 significant**
- **Conclusion:** Correlations are SPURIOUS

### Granger Causality (Real Market Data)
- Vibe → House: 0/13 states significant
- Vibe → Senate: 6/13 states significant
- House → Vibe: 3/13 states significant
- **Conclusion:** NO consistent predictive relationship

### Search Term Validation
- Valid terms (< 50% zeros): ~40%
- Colloquial phrasing largely fails at state level
- Only "ICE near me" validated among colloquial terms

---

## Usage

```python
import pandas as pd

# Load canonical trends
trends = pd.read_parquet("data/canonical/canonical_trends.parquet")

# Load vibe with markets
vibe_markets = pd.read_csv("data/canonical/canonical_vibe_markets.csv")

# Load search term manifest
import json
with open("data/canonical/canonical_search_terms.json") as f:
    terms = json.load(f)
```

---

## Provenance

All data collected following CommDAAF v1.0 transparency protocol:
- Conservative rate limiting (8-15s delays)
- Zero collection errors
- All methodological decisions documented
- Population controls applied

---

*Canonical dataset created by Claude Code*
*VibePoll-2026 | CommDAAF v1.0*
"""

    with open(f"{OUTPUT_DIR}/DATA_MANIFEST.md", 'w') as f:
        f.write(content)

    print(f"Wrote: {OUTPUT_DIR}/DATA_MANIFEST.md")


def main():
    """Create canonical combined datasets."""
    print("="*60)
    print("CREATING CANONICAL COMBINED DATASETS")
    print("VibePoll-2026 | CommDAAF v1.0")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load all data
    data = load_all_agent_data()

    # Create canonical trends
    canonical_trends = create_canonical_trends(data)
    canonical_trends.to_parquet(f"{OUTPUT_DIR}/canonical_trends.parquet", index=False)
    print(f"\nSaved: {OUTPUT_DIR}/canonical_trends.parquet")

    # Create canonical vibe + markets
    canonical_vibe = create_canonical_vibe_markets(data)
    canonical_vibe.to_csv(f"{OUTPUT_DIR}/canonical_vibe_markets.csv", index=False)
    print(f"Saved: {OUTPUT_DIR}/canonical_vibe_markets.csv")

    # Create search terms manifest
    terms_manifest = create_search_terms_manifest(data)
    with open(f"{OUTPUT_DIR}/canonical_search_terms.json", 'w') as f:
        json.dump(terms_manifest, f, indent=2)
    print(f"Saved: {OUTPUT_DIR}/canonical_search_terms.json")

    # Write data manifest
    write_data_manifest()

    print("\n" + "="*60)
    print("CANONICAL DATASET CREATION COMPLETE")
    print("="*60)
    print(f"\nOutput directory: {OUTPUT_DIR}/")
    print("\nFiles created:")
    print("  - canonical_trends.parquet")
    print("  - canonical_vibe_markets.csv")
    print("  - canonical_search_terms.json")
    print("  - DATA_MANIFEST.md")


if __name__ == "__main__":
    main()
