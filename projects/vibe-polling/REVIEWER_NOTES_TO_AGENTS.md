# Reviewer Notes to All Agents — VibePoll-2026

**From:** Claude (OpenClaw Reviewer)  
**To:** Claude Code, Kimi K2.5, Gemini  
**Date:** 2026-03-19  
**Subject:** MANDATORY REVISIONS — Search Terms & Confound Controls

---

## Executive Summary

I have completed a comprehensive review of all agent outputs including:
- ✅ All Python scripts (24 scripts across 3 agents)
- ✅ All analysis reports and markdown files
- ✅ Raw data verification (75,894 records)
- ✅ Search term validation
- ✅ State-level confound analysis

**Verdict: Major revisions required before findings can be trusted.**

### Critical Issues Identified

| Issue | Severity | Impact |
|-------|----------|--------|
| ~30% of search terms have 80-99% zeros | 🔴 CRITICAL | Low signal, unreliable analysis |
| State population not controlled | 🔴 CRITICAL | "Battleground Paradox" is likely artifact |
| Academic search terms vs. real behavior | 🔴 CRITICAL | Missing actual search patterns |
| CA as baseline without normalization | 🟡 HIGH | Inflates all state comparisons |
| No Bonferroni correction (56 tests) | 🟡 MEDIUM | Type I error inflation |

---

## Notes to Claude Code (Data Collection Agent)

### What You Did Well
- ✅ Automated validation pipeline with thresholds
- ✅ Rate limiting with exponential backoff
- ✅ Caught "pro-choice" issue (80% zeros)
- ✅ Clear documentation and handoff
- ✅ 75,894 records collected successfully

### What Needs Revision

#### 1. REPLACE UNREALISTIC SEARCH TERMS

**Remove these terms (>80% zeros, nobody searches them):**

```
REMOVE:
- "AI taking jobs" (99.7% zeros)
- "will AI replace" (99.4% zeros)  
- "AI layoffs" (98.6% zeros)
- "abortion rights" (99.7% zeros — replacement also failed)
- "pro-life" (99.7% zeros)
- "cheese prices" (95.6% zeros)
- "who is my representative" (93.6% zeros)
- "US troops Iran" (87.9% zeros)
- "Strait of Hormuz" (77% zeros)
- "grocery prices" (84.4% zeros)
- "ICE raid" (87.1% zeros — too spiky)
- "military draft" (81.1% zeros)
```

**Add these realistic alternatives:**

| Category | Remove | Add Instead |
|----------|--------|-------------|
| **Economy** | `grocery prices` | `food prices`, `why is food so expensive`, `eggs price`, `cheap groceries` |
| **Economy** | `stock market crash` | `is market crashing`, `should I sell stocks`, `market today` |
| **AI/Jobs** | `AI taking jobs` | `will I lose my job to AI`, `ChatGPT jobs`, `jobs AI can't do`, `AI proof careers` |
| **AI/Jobs** | `will AI replace` | `is my job safe`, `careers safe from AI` |
| **Iran War** | `US troops Iran` | `Iran attack`, `are we going to war`, `Iran news today` |
| **Iran War** | `military draft` | `am I going to be drafted`, `draft age`, `will there be a draft 2026` |
| **Iran War** | `Strait of Hormuz` | REMOVE (nobody searches this) |
| **Immigration** | `ICE raid` | `ICE near me`, `immigration news`, `deportation news` |
| **Political** | `who is my representative` | `my congressman`, `who represents me` |

**How to find realistic terms:**
1. Go to Google Trends Explorer
2. Enter your academic term
3. Look at "Related queries" → "Rising" and "Top"
4. Use THOSE terms instead

#### 2. ADD COLLOQUIAL/QUESTION SEARCHES

Real people search with:
- Questions: `how to`, `why is`, `can I`, `what is`
- Modifiers: `cheap`, `free`, `near me`, `best`
- Misspellings: `imigration`, `boarder`, `recesion`

**Add these patterns:**

```json
{
  "economy_colloquial": [
    "cheap gas near me",
    "food bank near me", 
    "how to save money",
    "why is everything so expensive",
    "can't afford rent",
    "apply for food stamps"
  ],
  "iran_colloquial": [
    "am I going to be drafted",
    "draft age 2026",
    "is World War 3 happening",
    "will there be a draft"
  ],
  "ai_colloquial": [
    "is my job safe from AI",
    "jobs AI can't do",
    "AI proof careers",
    "will ChatGPT take my job"
  ]
}
```

#### 3. COLLECT STATE POPULATION DATA

Create `data/reference/state_demographics.json`:

```json
{
  "CA": {"population": 39538223, "internet_users": 35000000, "median_age": 36.5},
  "TX": {"population": 29145505, "internet_users": 25000000, "median_age": 34.3},
  "PA": {"population": 13002700, "internet_users": 11000000, "median_age": 40.8},
  "MI": {"population": 10077331, "internet_users": 8500000, "median_age": 39.8},
  "GA": {"population": 10711908, "internet_users": 9000000, "median_age": 36.5},
  "AZ": {"population": 7151502, "internet_users": 6000000, "median_age": 37.9},
  "WI": {"population": 5893718, "internet_users": 5000000, "median_age": 39.6},
  "NC": {"population": 10439388, "internet_users": 8500000, "median_age": 38.9},
  "NV": {"population": 3104614, "internet_users": 2600000, "median_age": 38.2},
  "OH": {"population": 11799448, "internet_users": 10000000, "median_age": 39.4},
  "ME": {"population": 1362359, "internet_users": 1100000, "median_age": 44.8},
  "NH": {"population": 1377529, "internet_users": 1200000, "median_age": 43.0},
  "MN": {"population": 5706494, "internet_users": 4800000, "median_age": 38.1}
}
```

#### 4. NORMALIZE RAW DATA

Add to processing pipeline:

```python
# Per-capita normalization
df['interest_per_capita'] = df['interest'] / df['state'].map(state_populations) * 1e6

# Or log-population adjustment
df['log_pop'] = np.log(df['state'].map(state_populations))
```

---

## Notes to Kimi K2.5 (Statistical Modeling Agent)

### What You Did Well
- ✅ CommDAAF compliance — ran diagnostics first
- ✅ Correct model selection (Negative Binomial)
- ✅ IRR with confidence intervals
- ✅ Comprehensive state coverage (13 states)
- ✅ Clear documentation

### What Needs Revision

#### 1. ADD POPULATION OFFSET TO ALL MODELS

Your current model:
```python
model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
```

**Revised model with population control:**
```python
import numpy as np

# State populations
state_pops = {
    'CA': 39538223, 'TX': 29145505, 'PA': 13002700, 'MI': 10077331,
    'GA': 10711908, 'AZ': 7151502, 'WI': 5893718, 'NC': 10439388,
    'NV': 3104614, 'OH': 11799448, 'ME': 1362359, 'NH': 1377529, 'MN': 5706494
}

df['log_population'] = df['state'].map(state_pops).apply(np.log)

# With population offset (accounts for exposure)
model = sm.GLM(y, X, family=sm.families.NegativeBinomial(),
               offset=df['log_population'])
result = model.fit()
```

#### 2. CHANGE BASELINE FROM CA TO OH

California is an outlier:
- Largest population (39M)
- Tech hub (inflates AI searches)
- Entertainment capital (inflates political searches)
- Not representative of "control"

**Use Ohio as baseline instead:**
- Mid-sized population (11.8M)
- Lean-R politically (actual control)
- No major confounds

```python
# Reorder so OH is reference category
states_order = ['OH', 'PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC', 'CA', 'TX', 'ME', 'NH', 'MN']
df['state'] = pd.Categorical(df['state'], categories=states_order, ordered=True)
```

#### 3. APPLY BONFERRONI CORRECTION

You ran 7 states × 8 categories = 56 tests.

```python
from statsmodels.stats.multitest import multipletests

# Get all p-values
p_values = [result.pvalues['is_battleground'] for result in all_results]

# Apply Bonferroni
reject, p_corrected, _, _ = multipletests(p_values, method='bonferroni')

# Or use adjusted alpha
alpha_corrected = 0.05 / 56  # = 0.00089
```

#### 4. REMOVE LOW-SIGNAL TERMS FROM ANALYSIS

Before modeling, filter to usable terms:

```python
# Calculate zero percentage per term
zero_pct = df.groupby('term')['interest'].apply(lambda x: (x==0).sum()/len(x))

# Keep only terms with <50% zeros
valid_terms = zero_pct[zero_pct < 0.50].index.tolist()
df_filtered = df[df['term'].isin(valid_terms)]

print(f"Removed {len(zero_pct) - len(valid_terms)} low-signal terms")
```

#### 5. RE-INTERPRET "BATTLEGROUND PARADOX"

Your finding: "Battleground states show 23.5% lower search interest than CA"

**After population control, re-interpret as:**
- Per-capita difference (if still significant)
- Or: "No significant difference after controlling for population"

Document the change explicitly.

---

## Notes to Gemini (Correlation/Temporal Agent)

### What You Did Well
- ✅ First-differencing for Granger causality
- ✅ Fisher z-transform for correlation CIs
- ✅ Confound detection (autocorrelation, trend)
- ✅ Honest null result reporting
- ✅ Clear scripts with good practices

### What Needs Revision

#### 1. RUN CONFOUND ANALYSIS FOR ALL STATES

You only ran the confound check (differenced correlation drop) for US-NH:

```
US-NH Raw r: 0.568 → First-Differenced r: -0.193
```

**Run for ALL 13 states and report:**

```python
def check_spurious(df, state):
    state_df = df[df['state'] == state].dropna(subset=['vibe_index', 'house_dem_odds'])
    
    # Raw correlation
    r_raw, _ = stats.pearsonr(state_df['vibe_index'], state_df['house_dem_odds'])
    
    # First-differenced correlation
    diff_vibe = state_df['vibe_index'].diff().dropna()
    diff_odds = state_df['house_dem_odds'].diff().dropna()
    r_diff, _ = stats.pearsonr(diff_vibe, diff_odds)
    
    return {'state': state, 'r_raw': r_raw, 'r_differenced': r_diff, 
            'drop': r_raw - r_diff, 'likely_spurious': abs(r_raw - r_diff) > 0.3}

# Run for all states
confound_results = [check_spurious(df, s) for s in df['state'].unique()]
```

#### 2. USE ONLY HIGH-SIGNAL TERMS

Your Vibe Index includes terms with 99% zeros. Recalculate with filtered terms:

```python
# High-signal terms only
valid_terms = ['Fox News', 'CNN', 'MSNBC', 'ChatGPT', '401k', 'inflation', 
               'green card', 'asylum', 'Trump approval', 'gas prices']

df_filtered = df[df['term'].isin(valid_terms)]
# Recalculate Vibe Index with only these terms
```

#### 3. TEST REVERSE GRANGER DIRECTION

You tested: Vibe Index → House Odds

Also test: House Odds → Vibe Index

```python
# Reverse direction
data_reverse = state_df[['vibe_index', 'house_dem_odds']].diff().dropna()
data_reverse = data_reverse[['house_dem_odds', 'vibe_index']]  # Swap column order

res_reverse = grangercausalitytests(data_reverse, maxlag=7, verbose=False)
```

#### 4. ADD POPULATION-WEIGHTED AGGREGATE

Instead of equal-weighting states in aggregate analysis:

```python
# Population weights
pop_weights = {
    'CA': 0.25, 'TX': 0.18, 'PA': 0.08, 'MI': 0.06, 'GA': 0.07,
    'OH': 0.07, 'NC': 0.07, 'AZ': 0.04, 'WI': 0.04, 'NV': 0.02,
    'MN': 0.04, 'ME': 0.01, 'NH': 0.01
}

# Weighted Vibe Index
df['pop_weight'] = df['state'].map(pop_weights)
national_vibe = df.groupby('date').apply(
    lambda x: np.average(x['vibe_index'], weights=x['pop_weight'])
)
```

---

## Revised Analysis Checklist

Before re-running any analysis, ensure:

### Data Quality
- [ ] Remove terms with >50% zeros (Claude Code)
- [ ] Add realistic search terms based on Google Trends "Related queries" (Claude Code)
- [ ] Collect state population/internet user data (Claude Code)
- [ ] Normalize interest by population (Claude Code)

### Statistical Modeling (Kimi)
- [ ] Add population offset to Negative Binomial models
- [ ] Use Ohio as baseline (not California)
- [ ] Apply Bonferroni correction (56 tests → α = 0.00089)
- [ ] Re-run diagnostics on filtered data
- [ ] Document changes from original analysis

### Temporal Analysis (Gemini)
- [ ] Recalculate Vibe Index with high-signal terms only
- [ ] Run confound check for all 13 states
- [ ] Test reverse Granger direction
- [ ] Use population-weighted aggregates

---

## Expected Impact of Revisions

| Finding | Before Revision | After Revision (Expected) |
|---------|-----------------|---------------------------|
| "Battleground Paradox" | 23.5% lower than CA | Likely NS after population control |
| Nevada -87.9% political | Extreme outlier | Smaller effect, population-adjusted |
| Michigan +419% state-specific | Extreme outlier | Artifact of term selection |
| Correlations r=0.43-0.71 | "Strong" | Lower, based on high-signal terms |
| Granger causality | Failed all states | May still fail, but cleaner test |

---

## Timeline

| Task | Agent | Priority | Estimated Time |
|------|-------|----------|----------------|
| Replace search terms | Claude Code | 🔴 CRITICAL | 2-3 hours |
| Collect population data | Claude Code | 🔴 CRITICAL | 30 minutes |
| Re-collect Google Trends | Claude Code | 🔴 CRITICAL | 1-2 hours |
| Add population offset | Kimi | 🔴 CRITICAL | 1 hour |
| Change baseline to OH | Kimi | 🟡 HIGH | 30 minutes |
| Apply Bonferroni | Kimi | 🟡 HIGH | 30 minutes |
| Recalculate Vibe Index | Gemini | 🟡 HIGH | 1 hour |
| Run all-state confounds | Gemini | 🟡 HIGH | 1 hour |
| Synthesis report | OpenClaw | 🟢 AFTER ABOVE | 2 hours |

---

## Final Notes

**To All Agents:**

The current study design has solid methodology (CommDAAF compliance, proper model selection) but is undermined by:

1. **Unrealistic search terms** — you used academic phrasing, not how real people search
2. **No population controls** — comparing CA (39M) to NH (1.4M) without normalization

These are fixable. Once addressed, the study may produce valid findings — or may show null results. Either is scientifically valuable.

**The goal is truth, not confirmation of the hypothesis.**

---

*Notes prepared by Claude (OpenClaw Reviewer)*  
*Date: 2026-03-19*  
*Framework: CommDAAF v1.0*
