# Regression Modeling for Communication Research

## The Problem

Social media engagement data (likes, shares, retweets, comments) almost NEVER meets OLS assumptions:
- **Highly right-skewed** (many zeros/low values, few viral posts)
- **Zero-inflated** (many posts get no engagement)
- **Overdispersed** (variance >> mean)
- **Count data** (non-negative integers)

Running OLS on this data produces **biased estimates** and **incorrect p-values**.

## Distribution Diagnostics (REQUIRED)

Before ANY regression, run these checks:

```python
import numpy as np
from scipy import stats

def diagnose_dv(y, var_name="DV"):
    """Run before choosing regression model."""
    print(f"=== {var_name} Distribution Diagnostics ===")
    print(f"N = {len(y)}")
    print(f"Mean = {np.mean(y):.3f}, Median = {np.median(y):.3f}")
    print(f"SD = {np.std(y):.3f}, Variance = {np.var(y):.3f}")
    print(f"Min = {np.min(y):.3f}, Max = {np.max(y):.3f}")
    
    # Skewness
    skew = stats.skew(y)
    print(f"\nSkewness = {skew:.3f}", end="")
    if abs(skew) > 1:
        print(" ⚠️ HIGHLY SKEWED")
    elif abs(skew) > 0.5:
        print(" ⚠️ Moderately skewed")
    else:
        print(" ✅ Approximately symmetric")
    
    # Zero inflation
    pct_zero = 100 * np.sum(y == 0) / len(y)
    print(f"% Zeros = {pct_zero:.1f}%", end="")
    if pct_zero > 10:
        print(" ⚠️ ZERO-INFLATED")
    else:
        print(" ✅ OK")
    
    # Overdispersion
    var_mean = np.var(y) / np.mean(y) if np.mean(y) > 0 else np.inf
    print(f"Variance/Mean = {var_mean:.3f}", end="")
    if var_mean > 1.5:
        print(" ⚠️ OVERDISPERSED (use NB over Poisson)")
    else:
        print(" ✅ OK for Poisson")
    
    # Normality test (subset for large N)
    test_y = y[:min(5000, len(y))]
    stat, p = stats.shapiro(test_y) if len(test_y) < 5000 else stats.normaltest(test_y)
    print(f"Normality test p = {p:.4f}", end="")
    if p < 0.05:
        print(" ⚠️ NOT NORMAL")
    else:
        print(" ✅ Approximately normal")
    
    return {
        'skewness': skew,
        'pct_zeros': pct_zero,
        'var_mean_ratio': var_mean,
        'normal_p': p
    }
```

## Model Selection Decision Tree

```
                    Is DV continuous or count?
                           /          \
                      Continuous      Count
                         /               \
                  Normal residuals?    Overdispersed?
                   /        \           /         \
                 Yes        No        No          Yes
                  |          |         |           |
                OLS    Transform    Poisson    Neg Binomial
                        or GLM
                                    
                    Many zeros (>15%)?
                           |
                          Yes
                           |
                    Zero-Inflated or
                    Hurdle Model
```

## Model Recommendations by DV Type

### Engagement Metrics (RT, likes, shares)

| Condition | Recommended Model | R Package | Python |
|-----------|-------------------|-----------|--------|
| Overdispersed | **Negative Binomial** | `MASS::glm.nb()` | `statsmodels.GLM(family=NegBinom)` |
| Many zeros + overdispersed | **Zero-Inflated NB** | `pscl::zeroinfl()` | `statsmodels.ZeroInflatedNegativeBinomialP` |
| Structural zeros | **Hurdle Model** | `pscl::hurdle()` | Two-part model |

### Proportions (% positive, share of voice)

| Condition | Recommended Model |
|-----------|-------------------|
| Bounded 0-1 | Beta regression |
| Binary | Logistic regression |

### Continuous but Skewed

| Condition | Recommended Model |
|-----------|-------------------|
| Log-transformable | OLS on log(y+1) |
| Heavy tails | Robust regression |
| Heteroscedastic | Weighted LS or HC-robust SEs |

## Reporting Requirements

### Always Report:
1. **Distribution diagnostics** (skewness, % zeros, overdispersion)
2. **Model choice justification** ("NB chosen due to overdispersion")
3. **Effect size in interpretable units** (IRR for NB, OR for logistic)
4. **Model fit** (AIC, deviance, pseudo-R²)

### For Negative Binomial:
```
We used negative binomial regression due to overdispersion 
(variance/mean ratio = X.XX). Results are reported as 
Incidence Rate Ratios (IRR), representing multiplicative 
effects on engagement.
```

### Example Results Table

| Predictor | IRR | 95% CI | p |
|-----------|-----|--------|---|
| Frame: CONFLICT | 1.71 | [0.92, 3.18] | .090 |
| Frame: INFORMATIONAL | 2.72 | [1.65, 4.49] | <.001 |
| High arousal | 1.58 | [1.03, 2.43] | .038 |

## Common Mistakes to Catch

### ❌ OLS on Count Data
```
# WRONG
model = sm.OLS(retweets, X).fit()

# RIGHT
model = sm.GLM(retweets, X, family=sm.families.NegativeBinomial()).fit()
```

### ❌ Ignoring Zero Inflation
If >15% zeros, test whether zero-inflated model fits better:
```python
# Compare AIC: lower is better
print(f"NB AIC: {nb_model.aic}")
print(f"ZINB AIC: {zinb_model.aic}")
```

### ❌ Reporting β Instead of IRR
For count models, exponentiate coefficients:
```python
IRR = np.exp(model.params)  # Incidence Rate Ratio
```

## Probing Questions

Before running regression, ask:

1. **What is your dependent variable?** (counts, proportions, continuous?)
2. **Have you checked the distribution?** (skewness, zeros, variance)
3. **What model are you planning to use?** (If OLS on counts → flag)
4. **How will you report effect sizes?** (IRR, OR, standardized β?)

## Quick Diagnostic Code

```python
# One-liner diagnostic
y = df['engagement'].values
diagnose_dv(y, "Engagement")

# Model comparison
from statsmodels.discrete.count_model import ZeroInflatedNegativeBinomialP
import statsmodels.api as sm

# Compare Poisson vs NB vs ZINB
pois = sm.GLM(y, X, family=sm.families.Poisson()).fit()
nb = sm.GLM(y, X, family=sm.families.NegativeBinomial()).fit()

print(f"Poisson AIC: {pois.aic:.1f}")
print(f"NB AIC: {nb.aic:.1f}")
# Lower AIC = better fit
```

## References

- Cameron, A. C., & Trivedi, P. K. (2013). *Regression Analysis of Count Data*. Cambridge.
- Hilbe, J. M. (2011). *Negative Binomial Regression*. Cambridge.
- Long, J. S. (1997). *Regression Models for Categorical and Limited Dependent Variables*. Sage.
