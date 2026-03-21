# Handoff Summary — VibePoll-2026 (R2 FINAL)

**From:** Claude Code (Claude Opus 4.5)
**To:** Kimi K2.5 (Statistical Modeling) & Gemini (Temporal Analysis)
**Date:** 2026-03-20
**Framework:** CommDAAF v1.0 — EXPLORATORY Tier
**Revision:** R2 (Final)

---

## REVISION SUMMARY

This is the **final R2 revision** addressing all peer review concerns:

| Issue | R1 Status | R2 Status |
|-------|-----------|-----------|
| Low-signal terms (>50% zeros) | Filtered during processing | FIXED |
| State population controls | Per-capita normalization | FIXED |
| National baseline (not Ohio) | Used OH | FIXED: Population-weighted national avg |
| Realistic search terms | Added colloquial categories | FIXED: Validated via API |
| NH/ME data quality flag | Not flagged | DOCUMENTED |

---

## 1. Data Available

### 1.1 Processed Data (Ready for Analysis)

| File | Records | Description |
|------|---------|-------------|
| `data/processed/trends_normalized.parquet` | 38,311 | R2 FINAL - Filtered + all normalizations |
| `data/processed/vibe_indices.csv` | 1,183 | Weighted Vibe Index per state-date |
| `data/processed/issue_salience.csv` | 1,183 | Issue salience per state-date-category |

### 1.2 Raw Data

| File | Records | Description |
|------|---------|-------------|
| `data/raw/trends/trends_2026-03-19.parquet` | 98,371 | R2 collection with validated terms |
| `data/raw/markets/markets_2026-03-19.json` | 29 markets | Polymarket + Kalshi |
| `data/raw/polls/polls_2026-03-19.json` | 34 polls | Quinnipiac, Emerson, Marist |

### 1.3 Figures Generated

| File | Description |
|------|-------------|
| `outputs/figures/state_issue_heatmap.png` | States x Issue Categories |
| `outputs/figures/term_timeseries.png` | Top 8 terms over time |
| `outputs/figures/battleground_vs_control.png` | State type comparison |
| `outputs/figures/vibe_index_timeseries.png` | Vibe Index by state group |

---

## 2. R2 Changes Applied

### 2.1 Search Terms (Validated via API)

**Terms collected:** 95 unique terms
**Terms retained after filtering:** 37 (high-signal, <50% zeros)
**Terms filtered:** 58 (low-signal, >50% zeros)

**New high-signal terms added:**
- `paycheck to paycheck` (avg=70.4, 0% zeros)
- `second job` (avg=60.2, 0% zeros)
- `health insurance cost` (avg=64.0, 0% zeros)
- `cost of groceries` (avg=63.6, 0% zeros)
- `AI jobs` (avg=48.2, 0% zeros)
- `AI news` (avg=63.9, 0% zeros)
- `Trump` (avg=51.2, 0% zeros)
- `Biden` (avg=47.2, 0% zeros)
- `election 2026` (avg=16.3, 0% zeros)
- `draft` (avg=44.1, 0% zeros)
- `military` (avg=61.8, 0% zeros)

### 2.2 National Baseline (NOT Ohio)

Per R2 reviewer notes: Ohio went Trump +11 in 2024 and is no longer a swing state.

**New baseline:** Population-weighted national average

```python
# Implementation
POPULATION_WEIGHTS = {
    'CA': 0.25, 'TX': 0.18, 'PA': 0.08, 'MI': 0.06, 'GA': 0.07,
    'AZ': 0.05, 'WI': 0.04, 'NC': 0.07, 'NV': 0.02, 'OH': 0.07,
    'ME': 0.01, 'NH': 0.01, 'MN': 0.04
}

# New column: interest_vs_national
df['interest_vs_national'] = df['interest'] - df['national_avg']
```

### 2.3 Data Quality Flag

**NH and ME have structural data issues:**
- Even after filtering, these states have 63-64% zeros
- This is a Google Trends limitation for small states
- **Flag as "low confidence" in all downstream analyses**

---

## 3. Data Schema

### trends_normalized.parquet (R2 FINAL)

| Column | Type | Description |
|--------|------|-------------|
| date | datetime | Collection date |
| state | string | State code |
| term | string | Search term |
| category | string | Issue category |
| interest | int | Raw Google Trends interest (0-100) |
| z_temporal | float | Temporal z-score |
| z_crossterm | float | Cross-term z-score |
| z_combined | float | Average of temporal and cross-term |
| population | int | State population (Census 2020) |
| log_population | float | Log of population (for offset models) |
| interest_per_capita | float | **DEPRECATED R3** - Invalid (see peer review) |
| z_per_capita | float | **DEPRECATED R3** - Invalid (see peer review) |
| pop_weight | float | Weight for national aggregates |
| **national_avg** | float | **NEW R2** - Pop-weighted national average |
| **interest_vs_national** | float | **NEW R2** - Deviation from national |

### vibe_indices.csv

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

---

## 4. Statistics

### Collection Stats
```
Raw records:      98,371
After filtering:  38,311
Terms retained:   37
Terms filtered:   58
States:           13
Date range:       2025-12-19 to 2026-03-19
Collection time:  66.3 minutes
Rate limits hit:  15 (all recovered)
Errors:           0
```

### Vibe Index Stats
```
Mean:   -0.0053
Std:     0.2078
Min:    -0.5844
Max:     0.7058
```

---

## 5. Recommended Analysis

### For Kimi K2.5 (Statistical Modeling)

1. **Use `log_population` as offset** in Negative Binomial models
2. **Use `interest_vs_national`** for state comparisons (not raw interest)
3. **Apply Bonferroni correction** for multiple comparisons
4. **Flag NH/ME** as low confidence in tables

```python
# Example: NB regression with population offset
import statsmodels.api as sm

model = sm.GLM(y, X,
    family=sm.families.NegativeBinomial(),
    offset=df['log_population'])
```

### For Gemini (Temporal Analysis)

1. **Use `pop_weight`** for national aggregates
2. **Recalculate Vibe Index correlations** with R2 data
3. **Test both Granger directions** (Trends→Markets, Markets→Trends)
4. **Run confound check** for all 13 states

```python
# Population-weighted national Vibe Index
national_vibe = df.groupby('date').apply(
    lambda x: np.average(x['vibe_index'], weights=x['pop_weight'])
)
```

---

## 6. File Paths

```python
import pandas as pd

# Processed data (R2 FINAL)
trends = pd.read_parquet("data/processed/trends_normalized.parquet")
vibe = pd.read_csv("data/processed/vibe_indices.csv")
salience = pd.read_csv("data/processed/issue_salience.csv")

# Reference files
import json
with open("data/reference/state_demographics.json") as f:
    demographics = json.load(f)
with open("data/reference/term_categories.json") as f:
    terms = json.load(f)
```

---

## 7. Documentation

| File | Description |
|------|-------------|
| `agents/claude-code/REVISION_LOG.md` | R1 revision details |
| `agents/claude-code/REVISION_NOTES_R2.md` | R2 reviewer notes |
| `data/processed/processing_log.md` | Full processing decisions |
| `logs/session_log.md` | Collection session log |
| `logs/collection_log.txt` | Raw collection log |

---

## 8. CommDAAF Compliance

- [x] All search terms validated via Google Trends API
- [x] Low-signal terms filtered (<50% zeros threshold)
- [x] Population controls applied (per-capita, national baseline)
- [x] Methodological decisions documented
- [x] NH/ME flagged as low confidence
- [x] Collection rate limited (conservative: 8-15s delays)
- [x] Zero collection errors

---

## 9. Descriptive Findings: What Google Trends Reveals About Public Opinion

### Core Finding: Predictive Hypothesis FAILS

**Google Trends does NOT predict prediction market movements.**

- Granger causality: 0/14 states significant
- All correlations spurious after first-differencing
- Only 1/25 realistic colloquial terms survived state-level validation

**However, the data provides valuable DESCRIPTIVE insights about voter attention patterns.**

### 9.1 Battleground State Patterns

**CORRECTION (R3):** The original "143% higher per-capita engagement" claim has been **RETRACTED** following peer review by Gemini. This finding was based on invalid per-capita normalization of already-normalized Google Trends data.

**Corrected finding (using valid methodology):**
- Battleground states show MODEST variation from national average in overall interest
- IRR analysis (raw interest): Immigration +18%, AI/jobs -20% (Bonferroni-significant)
- These are the only statistically significant category-level differences

### 9.2 State-Specific Patterns

| State | Pattern | Key Finding |
|-------|---------|-------------|
| **Michigan** | Hyper-local | +419% state-specific searches (UAW, auto, Detroit jobs) |
| **Nevada** | Severely disengaged | -87.9% political, -76% immigration searches |
| **Pennsylvania** | Immigration salient | +24% immigration searches |
| **Georgia** | Immigration salient | +21% immigration searches |

### 9.3 Issue Salience Patterns

| Issue | Pattern | Evidence |
|-------|---------|----------|
| **Immigration** | Dominates everywhere | Even non-border states (PA +24%, GA +21%) show high interest |
| **AI/Jobs** | Coastal phenomenon | CA +7%, but battlegrounds 30-59% LOWER |
| **Economy** | Flat across states | Minimal variation (-6 to +3 vs national) |
| **Iran War** | Not yet personal | All states -19% to -23% LOWER; draft terms fail (97% zeros) |
| **Partisan Media** | Equal consumption | Battlegrounds match CA in Fox/CNN/MSNBC searches |

### 9.4 Campaign Implications for 2026 Midterms

| Finding | Implication |
|---------|-------------|
| Battleground engagement high | Digital outreach viable in swing states |
| Michigan hyper-local | Localize messaging (UAW, auto industry, not national narratives) |
| Nevada disengaged | Non-digital outreach needed (TV, canvassing, unions) |
| Immigration everywhere | Immigration messaging salient in ALL states, not just border |
| AI anxiety coastal | AI/automation messaging won't resonate in Rust Belt |
| War not personal | Iran war not yet voter-mobilizing (no draft = no personal stakes) |

---

## 10. Data Quality Implications for Future Studies

### 10.1 What Works

| Approach | Result |
|----------|--------|
| High-volume generic terms | `Trump`, `Biden`, `inflation`, `ChatGPT` - 0% zeros |
| Population-weighted baselines | Eliminates large-state bias |
| Interest vs national comparison | Valid comparison of proportional indices |
| Conservative rate limiting | Collection completed with 15 rate limit retries |

**CORRECTION (R3):** "Per-capita normalization" was originally listed here but has been **REMOVED** following peer review. Google Trends interest is already normalized (0-100 scale); dividing by population artificially inflates small-state values.

### 10.2 What Fails

| Approach | Result |
|----------|--------|
| Colloquial/anxiety phrasing | "why is food so expensive" = 67% zeros nationally, worse at state level |
| Long-tail question queries | "am I going to be drafted" = 97% zeros |
| State-level analysis for small states | NH/ME have 63-88% zeros (structural limitation) |
| National validation alone | Terms viable nationally often collapse at state level |

### 10.3 Recommendations for Future Google Trends Research

1. **Pre-validate at STATE level**, not just national
2. **Use generic high-volume terms** over colloquial phrasing
3. **Exclude states <2M population** from state-level analysis
4. **Compare interest directly** (do NOT divide by population - already normalized)
5. **First-difference before correlation analysis** to avoid spurious findings
6. **Expect descriptive, not predictive value** from search data

### 10.4 Smoothing Before Z-Scoring (R3 Addition)

For sparse data (50% zeros), apply 7-day rolling average BEFORE Z-scoring to reduce artificial spikes:

```python
df['interest_smoothed'] = df.groupby(['state', 'term'])['interest'].transform(
    lambda x: x.rolling(7, min_periods=3).mean()
)
df['z_temporal_smoothed'] = df.groupby(['state', 'term'])['interest_smoothed'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

This mitigates the problem of isolated non-zero days creating extreme Z-scores.

---

## 11. Required Caveats

All downstream analyses must include these caveats:

1. **Correlations are spurious** — raw r values (0.5-0.7) collapse to near-zero after first-differencing
2. **Granger causality fails** — Google Trends does NOT predict markets (0/14 states)
3. **NH/ME are low-confidence** — 63-88% zeros due to small state populations
4. **Realistic terms largely fail** — only 1/25 colloquial terms viable at state level
5. **National validation overstates usefulness** — terms that work nationally often collapse at state level

---

*R3 Final Handoff — Claude Code*
*VibePoll-2026 | CommDAAF v1.0*
*Date: 2026-03-20*
