# Statistical Modeling Results

**Agent:** Kimi K2.5  
**Framework:** CommDAAF v1.0  
**Date:** 2026-03-19  
**Model Type:** Negative Binomial Regression  
**Model Selection:** Based on distribution diagnostics (Section 7.1)  

## CommDAAF Compliance

✅ **Diagnostics-driven model selection:** Used Negative Binomial (not OLS) based on:  
   - High skewness (|skew| > 1)  
   - High zero proportion (>15%)  
   - Overdispersion (var/mean > 1.5)  

✅ **Effect sizes reported:** IRR with 95% CI  
✅ **Confidence intervals included:** All estimates have CIs  

## Model Results

### Category Effects (PA vs CA)

| Category | N | IRR (PA effect) | 95% CI | p-value |
|----------|---|-----------------|--------|---------|
| economy | 2,366 | 0.925 | 0.851 - 1.004 | 0.0634 |
| immigration | 2,002 | 0.795 | 0.727 - 0.870 | 0.0000 |
| iran_war | 1,274 | 0.720 | 0.627 - 0.828 | 0.0000 |
| ai_jobs | 1,365 | 0.454 | 0.404 - 0.511 | 0.0000 |
| epstein | 910 | 1.021 | 0.890 - 1.172 | 0.7680 |
| political | 1,092 | 0.822 | 0.728 - 0.927 | 0.0014 |
| partisan_pairs | 1,638 | 1.121 | 1.014 - 1.239 | 0.0263 |
| state_specific | 273 | 1.508 | 1.318 - 1.725 | 0.0000 |

## Effect Size Interpretations

