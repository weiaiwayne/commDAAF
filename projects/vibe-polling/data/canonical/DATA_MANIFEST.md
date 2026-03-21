# VibePoll-2026 Canonical Data Manifest

**Generated:** 2026-03-20 21:55
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
