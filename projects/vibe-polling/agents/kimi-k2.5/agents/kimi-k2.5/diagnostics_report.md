# Distribution Diagnostics Report

**Agent:** Kimi K2.5  
**Framework:** CommDAAF v1.0  
**Date:** 2026-03-19  
**Data Source:** Google Trends (Real Data)  

---

## ⚠️ CommDAAF Section 7.1 Compliance

✅ **MANDATORY diagnostics completed before regression**

## Summary

| Variable | N | Mean | Skewness | % Zeros | Var/Mean | Model Rec |
|----------|---|------|----------|---------|----------|-----------|
| interest | 10920 | 16.051 | 1.534⚠️ | 37.6⚠️ | 33.294⚠️ | Negative Binomial (count data)... |
| interest_economy | 2366 | 18.46 | 1.522⚠️ | 17.29⚠️ | 27.584⚠️ | Negative Binomial (count data)... |
| interest_immigration | 2002 | 21.369 | 1.032⚠️ | 35.11⚠️ | 28.865⚠️ | Negative Binomial (count data)... |
| interest_iran_war | 1274 | 4.796 | 4.444⚠️ | 48.27⚠️ | 32.207⚠️ | Negative Binomial (count data)... |
| interest_ai_jobs | 1365 | 16.236 | 1.615⚠️ | 51.58⚠️ | 36.771⚠️ | Negative Binomial (count data)... |
| interest_epstein | 910 | 8.184 | 3.411⚠️ | 33.19⚠️ | 36.537⚠️ | Negative Binomial (count data)... |
| interest_political | 1092 | 27.007 | 0.492 | 30.68⚠️ | 21.927⚠️ | Negative Binomial (count data)... |
| interest_partisan_pairs | 1638 | 13.437 | 1.634⚠️ | 50.18⚠️ | 43.008⚠️ | Negative Binomial (count data)... |
| interest_state_specific | 273 | 5.846 | 3.371⚠️ | 79.12⚠️ | 39.538⚠️ | Negative Binomial (count data)... |

## Detailed Results

### interest

- **N:** 10920
- **Mean:** 16.051 | **Median:** 4.0 | **SD:** 23.117
- **Range:** 0 - 100
- **Skewness:** 1.534
- **% Zeros:** 37.6%
- **Var/Mean Ratio:** 33.294
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_economy

- **N:** 2366
- **Mean:** 18.46 | **Median:** 10.0 | **SD:** 22.566
- **Range:** 0 - 100
- **Skewness:** 1.522
- **% Zeros:** 17.29%
- **Var/Mean Ratio:** 27.584
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_immigration

- **N:** 2002
- **Mean:** 21.369 | **Median:** 11.0 | **SD:** 24.836
- **Range:** 0 - 100
- **Skewness:** 1.032
- **% Zeros:** 35.11%
- **Var/Mean Ratio:** 28.865
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_iran_war

- **N:** 1274
- **Mean:** 4.796 | **Median:** 1.0 | **SD:** 12.428
- **Range:** 0 - 100
- **Skewness:** 4.444
- **% Zeros:** 48.27%
- **Var/Mean Ratio:** 32.207
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_ai_jobs

- **N:** 1365
- **Mean:** 16.236 | **Median:** 0.0 | **SD:** 24.434
- **Range:** 0 - 100
- **Skewness:** 1.615
- **% Zeros:** 51.58%
- **Var/Mean Ratio:** 36.771
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_epstein

- **N:** 910
- **Mean:** 8.184 | **Median:** 2.0 | **SD:** 17.292
- **Range:** 0 - 100
- **Skewness:** 3.411
- **% Zeros:** 33.19%
- **Var/Mean Ratio:** 36.537
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_political

- **N:** 1092
- **Mean:** 27.007 | **Median:** 26.0 | **SD:** 24.335
- **Range:** 0 - 100
- **Skewness:** 0.492
- **% Zeros:** 30.68%
- **Var/Mean Ratio:** 21.927
- **Flags:** HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_partisan_pairs

- **N:** 1638
- **Mean:** 13.437 | **Median:** 0.0 | **SD:** 24.039
- **Range:** 0 - 100
- **Skewness:** 1.634
- **% Zeros:** 50.18%
- **Var/Mean Ratio:** 43.008
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

### interest_state_specific

- **N:** 273
- **Mean:** 5.846 | **Median:** 0.0 | **SD:** 15.203
- **Range:** 0 - 100
- **Skewness:** 3.371
- **% Zeros:** 79.12%
- **Var/Mean Ratio:** 39.538
- **Flags:** HIGHLY_SKEWED, HIGH_ZERO_PROPORTION, OVERDISPERSED
- **Model Recommendation:** Negative Binomial (count data) or Zero-inflated

