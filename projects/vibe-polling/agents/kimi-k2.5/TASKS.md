# Kimi K2.5 Tasks — VibePoll-2026

**Agent:** Kimi K2.5 via OpenCode  
**Command:** `opencode -m kimi-coding/k2p5`  
**Study:** Vibe Polling  
**Framework:** CommDAAF v1.0  
**Role:** Statistical Modeling & Distribution Diagnostics

---

## ⚠️ CRITICAL: READ BEFORE EXECUTING

**Kimi K2.5 Constraints (from AgentAcademy Protocol):**
- **25-item batch limit** — JSON truncates on larger batches
- **262K token context limit** — split large files if needed
- PTY mode required for OpenCode

---

## Execution Command

Run via OpenCode:

```bash
opencode -m kimi-coding/k2p5 run "$(cat agents/kimi-k2.5/TASKS.md)"
```

Or run tasks individually (recommended).

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
- ✅ MANDATORY distribution diagnostics before ANY regression
- ✅ Model selection via decision tree (Section 7.2 of protocol)
- ✅ Effect sizes with confidence intervals (IRR for count models)
- ✅ Multiple comparison correction (Bonferroni/FDR)
- ❌ NEVER use OLS on raw count/engagement data

Proceed only after confirming activation.
```

---

## Task 1: Load and Verify Data

```
Load the processed data prepared by Claude Code:

1. Load: data/processed/trends_normalized.parquet
2. Load: data/processed/vibe_indices.csv
3. Load: data/raw/markets/*.json (merge into single DataFrame)
4. Load: data/raw/polls/*.json (merge into single DataFrame)

Verify data integrity:
- Check for missing values
- Check date alignment across sources
- Report basic stats (N, date range, states covered)

Save verification report to: agents/kimi-k2.5/data_verification.md
```

---

## Task 2: Distribution Diagnostics (MANDATORY — CommDAAF Section 7.1)

```
⚠️ THIS TASK IS NON-NEGOTIABLE — DO NOT SKIP

For EVERY numeric variable that might be a DV, run full diagnostics:

Variables to diagnose:
- Raw search volume (per term)
- Normalized search volume (z-scores)
- Vibe Index (per state)
- Market prices/odds
- Polling margins

For each variable, calculate and report:
1. N (sample size)
2. Mean, Median, SD
3. Min, Max, Range
4. Skewness (flag if |skew| > 1)
5. % Zeros (flag if > 15%)
6. Variance/Mean ratio (flag if > 1.5 = overdispersion)
7. Shapiro-Wilk normality test (if N < 5000)

Output format for each variable:
```
=== Variable: [name] ===
N: X
Mean: X.XX | Median: X.XX | SD: X.XX
Range: X.XX - X.XX
Skewness: X.XX [⚠️ HIGHLY SKEWED if |skew| > 1]
% Zeros: X.X% [⚠️ HIGH ZERO PROPORTION if > 15%]
Var/Mean: X.XX [⚠️ OVERDISPERSED if > 1.5]

→ MODEL RECOMMENDATION: [OLS / Negative Binomial / Zero-Inflated / Beta]
```

Save full diagnostics to: analysis/descriptives/distribution_diagnostics.json
Save readable report to: agents/kimi-k2.5/diagnostics_report.md
```

---

## Task 3: Model Selection Decision Tree

```
Based on diagnostics from Task 2, determine appropriate models:

DECISION TREE (from CommDAAF Section 7.2):

1. Is DV a count/engagement metric?
   ├── Yes → Check overdispersion (var/mean > 1.5?)
   │   ├── Yes → Negative Binomial
   │   └── No → Poisson (rare for social media data)
   
2. Is DV a proportion/bounded [0,1]?
   └── Yes → Beta regression

3. Is DV continuous and approximately normal?
   └── Yes → OLS (but verify residuals after fitting)

4. Are there > 15% zeros?
   └── Yes → Zero-inflated or Hurdle model

⚠️ CRITICAL: If diagnostics show skewed count data, you MUST use 
Negative Binomial, NOT OLS. Document your reasoning.

Save model selection rationale to: agents/kimi-k2.5/model_selection.md
```

---

## Task 4: Statistical Modeling

```
Run the selected models:

Primary analysis: Vibe Index → Prediction Market Movement

If using Negative Binomial:
```python
import statsmodels.api as sm
import numpy as np

# Example structure
X = sm.add_constant(predictors)
model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
results = model.fit()

# Calculate IRR (Incidence Rate Ratio)
irr = np.exp(results.params)
ci = np.exp(results.conf_int())
```

If using OLS (only if justified by diagnostics):
```python
import statsmodels.api as sm

model = sm.OLS(y, X)
results = model.fit()

# Check residuals
residuals = results.resid
# Shapiro-Wilk, Q-Q plot, etc.
```

For all models, report:
1. Coefficients / IRR
2. 95% Confidence Intervals
3. P-values (raw)
4. Adjusted p-values (Bonferroni or FDR if multiple tests)
5. Model fit statistics (AIC, BIC, pseudo-R²)

Save results to: analysis/models/regression_results.json
Save readable table to: agents/kimi-k2.5/regression_table.md
```

---

## Task 5: Effect Size Interpretation

```
Translate statistical results to practical meaning:

For Negative Binomial (IRR):
| IRR | Interpretation |
|-----|----------------|
| 0.5 | 50% decrease |
| 0.8 | 20% decrease |
| 1.0 | No effect |
| 1.2 | 20% increase |
| 1.5 | 50% increase |
| 2.0 | 100% increase (doubled) |
| 2.72 | ~172% increase |

For each significant predictor, write a plain-English interpretation:
"A one-unit increase in [X] is associated with a [IRR]x change in [Y], 
95% CI [lower, upper], p = [value]."

Flag any effects that are:
- Statistically significant but tiny (IRR 0.95-1.05)
- Large but with wide CIs (uncertain)
- Significant only before multiple comparison correction

Save interpretations to: agents/kimi-k2.5/effect_interpretations.md
```

---

## Task 6: Validation Against Polls

```
Compare Vibe Index predictions to actual polling data:

1. Concurrent validity:
   - Correlate Vibe Index with same-week polling average
   - Report Pearson r with 95% CI

2. Predictive validity:
   - Does this week's Vibe Index predict next week's polling?
   - Lag correlation analysis

3. State-level validation:
   - Do battleground states show different patterns than control?
   - ANOVA or mixed-effects model

Report:
- Correlation coefficients with CIs
- Explained variance (R²)
- Any systematic biases detected

Save to: agents/kimi-k2.5/validation_results.md
```

---

## Task 7: Prepare Synthesis Handoff

```
Summarize all findings for the Coordinator (OpenClaw):

1. Key statistical findings (with effect sizes)
2. Model diagnostics summary
3. Validation results
4. Limitations and caveats
5. Recommendations for interpretation

Format as structured JSON for easy parsing:

{
  "agent": "kimi-k2.5",
  "task": "statistical_modeling",
  "validation_tier": "exploratory",
  "key_findings": [...],
  "effect_sizes": [...],
  "model_fit": {...},
  "validation": {...},
  "limitations": [...],
  "confidence_level": "low|medium|high"
}

Save to: agents/kimi-k2.5/synthesis_handoff.json
```

---

## Outputs Checklist

After completing all tasks, verify these files exist:

```
agents/kimi-k2.5/
├── data_verification.md
├── diagnostics_report.md
├── model_selection.md
├── regression_table.md
├── effect_interpretations.md
├── validation_results.md
└── synthesis_handoff.json

analysis/
├── descriptives/
│   └── distribution_diagnostics.json
└── models/
    └── regression_results.json
```

---

## Failure Modes to Watch

| Issue | Detection | Action |
|-------|-----------|--------|
| Context overflow | Slow/truncated output | Split into smaller tasks |
| OLS on skewed data | Diagnostics show skew > 1 | Switch to NB |
| Multiple comparison inflation | Many p < 0.05 | Apply FDR correction |
| Overfitting | AIC much higher than null | Simplify model |

---

## CommDAAF Compliance Checklist

Before submitting results:

- [ ] Distribution diagnostics run for ALL DVs
- [ ] Model selection justified by diagnostics
- [ ] Effect sizes reported (IRR or d), not just coefficients
- [ ] Confidence intervals included
- [ ] Multiple comparison correction applied
- [ ] Limitations documented
- [ ] No OLS on raw count data (unless justified)
