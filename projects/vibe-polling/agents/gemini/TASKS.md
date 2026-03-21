# Gemini Tasks — VibePoll-2026

**Agent:** Gemini (Google)  
**Study:** Vibe Polling  
**Framework:** CommDAAF v1.0  
**Role:** Correlation Analysis & Market Data Integration

---

## ⚠️ CRITICAL: READ BEFORE EXECUTING

**Gemini Notes:**
- Large context window available
- Strong at data analysis and reasoning
- May need explicit JSON formatting instructions

---

## Task 0: CommDAAF Activation (MANDATORY)

```
FIRST, read and activate CommDAAF:

1. Read: /root/.openclaw/workspace/skills/commdaaf/SKILL.md
2. Read: /root/.openclaw/workspace/projects/comm-research-skill/agent-academy-study-protocol.md
3. Read: PLAN.md in this directory

Confirm activation by stating exactly:
"CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."

Key guardrails for your role:
- ✅ Report correlation coefficients WITH confidence intervals
- ✅ Flag any r > 0.7 as potentially spurious
- ✅ Document all analytical decisions
- ✅ Check for confounding variables
- ✅ Use appropriate lag windows

Proceed only after confirming activation.
```

---

## Task 1: Load and Merge Data Sources

```
Load all data sources and create merged analysis dataset:

1. Google Trends (processed):
   - Load: data/processed/trends_normalized.parquet
   - Load: data/processed/vibe_indices.csv

2. Prediction Markets:
   - Load: data/raw/markets/*.json
   - Parse Polymarket odds (Democrats win House, etc.)
   - Parse Kalshi odds (if available)
   - Normalize to 0-100 scale

3. Traditional Polls:
   - Load: data/raw/polls/*.json
   - Extract generic ballot margins
   - Extract approval ratings

4. Create merged time series:
   - Align all sources by date
   - Handle missing dates (forward-fill, interpolate, or flag)
   - Document merge decisions

Save merged dataset to: data/processed/merged_timeseries.parquet
Save merge log to: agents/gemini/data_merge_log.md
```

---

## Task 2: Correlation Analysis — Concurrent

```
Calculate concurrent correlations between data sources:

Pairs to analyze:
1. Vibe Index (per state) ↔ Polymarket Dem odds
2. Vibe Index (per state) ↔ Generic ballot margin
3. Issue salience (economy) ↔ Market movement
4. Issue salience (immigration) ↔ Market movement
5. Issue salience (Iran war) ↔ Market movement
6. Individual search terms ↔ Market movement (top 20 terms)

For each pair:
- Pearson correlation coefficient
- 95% confidence interval (use Fisher z-transform)
- P-value
- Sample size (N)
- Interpretation

Flag correlations:
- ⚠️ r > 0.7: "Potentially spurious — check for confounds"
- ⚠️ p > 0.05: "Not statistically significant"
- ⚠️ N < 30: "Small sample — interpret with caution"

Output format:
| Variable 1 | Variable 2 | r | 95% CI | p | N | Flag |
|------------|------------|---|--------|---|---|------|

Save to: analysis/correlations/concurrent_correlations.csv
Save readable report to: agents/gemini/correlation_report.md
```

---

## Task 3: Lag Analysis — Lead/Lag Relationships

```
Determine if Google Trends leads or lags prediction markets:

Method: Cross-correlation analysis at lags -7 to +7 days

For each Trends-Market pair:
1. Calculate correlation at each lag (-7, -6, ..., 0, ..., +6, +7)
2. Identify optimal lag (highest absolute correlation)
3. Test significance at optimal lag
4. Interpret direction:
   - Positive lag (e.g., +3): Trends leads market by 3 days
   - Negative lag (e.g., -2): Market leads Trends by 2 days
   - Zero lag: Synchronous movement

Python approach:
```python
from scipy import stats
import numpy as np

def lag_correlation(x, y, max_lag=7):
    results = []
    for lag in range(-max_lag, max_lag + 1):
        if lag > 0:
            x_shifted = x[:-lag]
            y_aligned = y[lag:]
        elif lag < 0:
            x_shifted = x[-lag:]
            y_aligned = y[:lag]
        else:
            x_shifted, y_aligned = x, y
        
        r, p = stats.pearsonr(x_shifted, y_aligned)
        results.append({'lag': lag, 'r': r, 'p': p})
    return results
```

Output:
| Pair | Optimal Lag | r at Optimal | p | Interpretation |
|------|-------------|--------------|---|----------------|

Save to: analysis/correlations/lag_analysis.csv
Save visualization to: outputs/figures/lag_correlation.png
```

---

## Task 4: Granger Causality Tests

```
Test whether Google Trends "Granger-causes" prediction market movements:

Granger causality tests whether past values of X help predict Y 
beyond what past values of Y alone can predict.

For key pairs:
1. Vibe Index → Polymarket odds
2. Economy salience → Polymarket odds
3. Individual high-correlation terms → Polymarket odds

Python approach:
```python
from statsmodels.tsa.stattools import grangercausalitytests

# Test at multiple lags
max_lag = 7
results = grangercausalitytests(data[['market_odds', 'vibe_index']], max_lag)

# Extract F-test p-values
for lag, result in results.items():
    f_stat = result[0]['ssr_ftest'][0]
    p_value = result[0]['ssr_ftest'][1]
```

Report for each pair:
- Optimal lag for Granger causality
- F-statistic
- P-value
- Interpretation (X Granger-causes Y / No Granger causality)

⚠️ CAVEAT: Granger causality ≠ true causality. Document this limitation.

Save to: analysis/correlations/granger_results.json
Save report to: agents/gemini/granger_report.md
```

---

## Task 5: State-Level Comparisons

```
Compare battleground states to control states:

Questions:
1. Do battleground states show higher search volume for political terms?
2. Do battleground states show stronger Trends-Market correlations?
3. Are there state-specific patterns?

Analyses:
1. ANOVA: Mean search volume by state category (battleground vs control)
2. T-tests: Battleground vs control for each issue category
3. Correlation comparison: Fisher z-test for correlation differences

State categories (from PLAN.md):
- Battleground: PA, MI, WI, AZ, GA, NV, NC
- Control: CA (D), TX (R), OH (lean R)

Report:
| Comparison | Battleground Mean | Control Mean | Difference | p | Effect Size |
|------------|-------------------|--------------|------------|---|-------------|

Effect size: Cohen's d for mean differences

Save to: analysis/correlations/state_comparison.csv
Save report to: agents/gemini/state_comparison_report.md
```

---

## Task 6: Confound Check

```
Check for potential confounding variables:

Potential confounds:
1. **Major events**: Iran war start, Epstein release, etc.
   - Do correlations change when controlling for event dummies?

2. **Seasonality**: Day-of-week effects, holidays
   - Check for weekly patterns

3. **Autocorrelation**: Both series may be trending
   - Calculate first differences and re-test correlations

4. **Platform effects**: Changes in Google algorithm
   - Check for structural breaks

For any correlation r > 0.5:
- Calculate partial correlation controlling for confounds
- Report both raw and adjusted correlations
- Flag if adjustment substantially changes results

Save to: agents/gemini/confound_analysis.md
```

---

## Task 7: Prepare Synthesis Handoff

```
Summarize all findings for the Coordinator (OpenClaw):

Create structured summary:

{
  "agent": "gemini",
  "task": "correlation_analysis",
  "validation_tier": "exploratory",
  
  "key_findings": [
    {
      "finding": "Description",
      "evidence": "r = X.XX, 95% CI [X.XX, X.XX], p = X.XX",
      "confidence": "low|medium|high"
    }
  ],
  
  "lead_lag_summary": {
    "trends_leads_market": true|false,
    "optimal_lag_days": X,
    "interpretation": "..."
  },
  
  "granger_causality": {
    "trends_causes_market": true|false,
    "evidence": "F = X.XX, p = X.XX at lag X"
  },
  
  "state_differences": {
    "battleground_vs_control": "summary",
    "notable_states": [...]
  },
  
  "limitations": [
    "Correlation ≠ causation",
    "Limited time range",
    "..."
  ],
  
  "recommendations": [
    "..."
  ]
}

Save to: agents/gemini/synthesis_handoff.json
```

---

## Outputs Checklist

After completing all tasks, verify these files exist:

```
agents/gemini/
├── data_merge_log.md
├── correlation_report.md
├── granger_report.md
├── state_comparison_report.md
├── confound_analysis.md
└── synthesis_handoff.json

data/processed/
└── merged_timeseries.parquet

analysis/correlations/
├── concurrent_correlations.csv
├── lag_analysis.csv
├── granger_results.json
└── state_comparison.csv

outputs/figures/
└── lag_correlation.png
```

---

## CommDAAF Compliance Checklist

Before submitting results:

- [x] All correlations reported with 95% CIs
- [x] High correlations (r > 0.7) flagged for review
- [x] Lag analysis completed
- [x] Granger causality tested with caveats noted
- [x] Confounds checked
- [x] Limitations documented
- [x] Findings structured for synthesis
