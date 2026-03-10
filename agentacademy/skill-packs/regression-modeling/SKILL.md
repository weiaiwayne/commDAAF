# Regression Modeling Skill Pack

**Version:** 0.1.0  
**Status:** Pending Validation  
**Maintainer:** UMass Computational Communication Lab

---

## Overview

Proper statistical modeling for social science research, with emphasis on avoiding common pitfalls.

**⚠️ This skill exists because of repeated failures using OLS on engagement data.**

---

## Capabilities

- Distribution diagnostics
- Model selection decision tree
- Effect size calculation and interpretation
- Multiple comparison correction

---

## Probing Questions (ALL REQUIRED)

```
Q1: What is your dependent variable?
    ✓ Count (likes, shares, comments)
    ✓ Proportion (engagement rate)
    ✓ Continuous (sentiment score)
    ✓ Binary (viral/not viral)
    ✗ "Engagement" — SPECIFY THE METRIC

Q2: Have you run distribution diagnostics?
    ✓ Yes, I checked skewness, zeros, variance/mean ratio
    ✗ No — STOP. RUN DIAGNOSTICS FIRST.

Q3: What model will you use and WHY?
    ✓ Negative Binomial (overdispersed counts)
    ✓ Poisson (equidispersed counts)
    ✓ Zero-inflated (excess zeros)
    ✓ Logistic (binary outcome)
    ✓ Beta (proportions)
    ✓ OLS (approximately normal residuals)
    ✗ "OLS" without justification — FLAG FOR REVIEW

Q4: How will you report effect sizes?
    ✓ IRR for count models
    ✓ OR for logistic models
    ✓ Standardized β for OLS
    ✗ "Coefficients" — TRANSFORM TO INTERPRETABLE UNITS
```

---

## Distribution Diagnostics (MANDATORY)

**NEVER run regression without these checks:**

```python
import numpy as np
from scipy import stats

def distribution_diagnostics(y, name="DV"):
    print(f"=== Distribution Diagnostics: {name} ===")
    
    # Basic stats
    print(f"N: {len(y)}")
    print(f"Mean: {np.mean(y):.3f}")
    print(f"Median: {np.median(y):.3f}")
    print(f"SD: {np.std(y):.3f}")
    print(f"Range: {np.min(y):.3f} - {np.max(y):.3f}")
    
    # Skewness
    skewness = stats.skew(y)
    print(f"Skewness: {skewness:.3f}")
    if abs(skewness) > 1:
        print("  ⚠️ Highly skewed (|skew| > 1)")
    
    # Zeros
    n_zeros = np.sum(y == 0)
    pct_zeros = n_zeros / len(y) * 100
    print(f"Zeros: {n_zeros} ({pct_zeros:.1f}%)")
    if pct_zeros > 15:
        print("  ⚠️ High zero proportion (>15%)")
    
    # Overdispersion
    var_mean_ratio = np.var(y) / np.mean(y) if np.mean(y) > 0 else float('inf')
    print(f"Var/Mean ratio: {var_mean_ratio:.3f}")
    if var_mean_ratio > 1.5:
        print("  ⚠️ Overdispersed (var/mean > 1.5)")
    
    # Recommendation
    print("\n=== Model Recommendation ===")
    if pct_zeros > 30:
        print("→ Zero-inflated model or Hurdle model")
    elif var_mean_ratio > 1.5:
        print("→ Negative Binomial regression")
    elif skewness > 1:
        print("→ Log-transform or Negative Binomial")
    else:
        print("→ OLS may be appropriate (verify residuals)")
    
    return {
        'skewness': skewness,
        'pct_zeros': pct_zeros,
        'var_mean_ratio': var_mean_ratio
    }
```

---

## Model Selection Decision Tree

```
Is DV a count/engagement metric?
├── Yes → Check overdispersion (var/mean > 1.5?)
│   ├── Yes → Negative Binomial
│   └── No → Check zeros (>30%?)
│       ├── Yes → Zero-inflated or Hurdle
│       └── No → Poisson (rare for social media)
├── Is DV proportion/bounded (0-1)?
│   └── Yes → Beta regression or fractional logit
├── Is DV binary (0/1)?
│   └── Yes → Logistic regression
└── Is DV continuous and ~normal?
    └── Yes → OLS (verify residuals after fitting)

⚠️ NEVER use OLS on raw engagement counts without justification.
```

---

## Running Negative Binomial

```python
import statsmodels.api as sm
import numpy as np
import pandas as pd

def run_negative_binomial(data, dv, ivs, reference_frame='SOLIDARITY'):
    """Run NB regression with proper effect size reporting."""
    
    # Create dummy variables
    X = pd.get_dummies(data[ivs], drop_first=False)
    
    # Drop reference category
    ref_cols = [c for c in X.columns if reference_frame in c]
    X = X.drop(columns=ref_cols)
    
    # Add constant
    X = sm.add_constant(X)
    
    # Fit model
    y = data[dv]
    model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
    results = model.fit()
    
    # Calculate IRR
    irr = np.exp(results.params)
    ci = np.exp(results.conf_int())
    
    return results, irr, ci
```

---

## Effect Size Interpretation

### For Negative Binomial (IRR)

| IRR | Interpretation |
|-----|----------------|
| > 2.5 | Large positive effect |
| 1.5 - 2.5 | Medium positive effect |
| 1.2 - 1.5 | Small positive effect |
| 0.8 - 1.2 | Negligible effect |
| 0.5 - 0.8 | Small negative effect |
| < 0.5 | Large negative effect |

**Translation to practical terms:**

| IRR | Meaning |
|-----|---------|
| 1.5 | 50% more engagement |
| 2.0 | Double the engagement |
| 2.72 | ~3x engagement |
| 0.5 | Half the engagement |

### For Logistic (OR)

| OR | Interpretation |
|----|----------------|
| > 3.0 | Large effect |
| 1.5 - 3.0 | Medium effect |
| 1.2 - 1.5 | Small effect |
| 0.8 - 1.2 | Negligible |

### For OLS (Cohen's d / Standardized β)

| |d| / |β| | Interpretation |
|-----------|----------------|
| > 0.8 | Large |
| 0.5 - 0.8 | Medium |
| 0.2 - 0.5 | Small |
| < 0.2 | Negligible |

---

## Multiple Comparison Correction

When testing multiple predictors:

```python
from statsmodels.stats.multitest import multipletests

# Get p-values for all comparisons
p_values = [results.pvalues[var] for var in predictors]

# Apply FDR correction (Benjamini-Hochberg)
rejected, p_adj, _, _ = multipletests(p_values, method='fdr_bh')

# Report BOTH raw and adjusted p-values
for var, p_raw, p_adj in zip(predictors, p_values, p_adj):
    print(f"{var}: p={p_raw:.4f}, p_adj={p_adj:.4f}")
```

---

## Output Schema

```json
{
  "model_type": "negative_binomial | poisson | logistic | ols | beta",
  "diagnostics": {
    "skewness": "number",
    "pct_zeros": "number",
    "var_mean_ratio": "number",
    "model_justification": "string"
  },
  "results": [
    {
      "predictor": "string",
      "effect_size": "number (IRR/OR/β)",
      "ci_lower": "number",
      "ci_upper": "number",
      "p_value": "number",
      "p_adjusted": "number (if multiple comparisons)",
      "interpretation": "string"
    }
  ],
  "model_fit": {
    "aic": "number",
    "bic": "number",
    "pseudo_r2": "number (if applicable)"
  }
}
```

---

## Common Errors to Avoid

| Error | Why It's Wrong | Correct Approach |
|-------|----------------|------------------|
| OLS on counts | Violates assumptions, biased estimates | Negative Binomial |
| Raw coefficients | Not interpretable | IRR/OR/standardized β |
| Ignoring multiple comparisons | Inflated Type I error | FDR correction |
| No diagnostics | Don't know if model appropriate | Always run diagnostics |
| Skipping residual checks | Model may be misspecified | Plot residuals |

---

## Validation Requirements

| Tier | Requirement |
|------|-------------|
| 🟢 Exploratory | Distribution diagnostics, appropriate model |
| 🟡 Pilot | + Residual diagnostics, effect sizes reported |
| 🔴 Publication | + Sensitivity analysis, multiple comparison correction |

---

## TODO

- [ ] Add examples for each model type
- [ ] Create diagnostic visualization functions
- [ ] Add Bayesian alternative guidance
- [ ] Peer validation

---

## References

- Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
- Hilbe, J. M. (2011). Negative binomial regression.
- Long, J. S. (1997). Regression models for categorical and limited dependent variables.
