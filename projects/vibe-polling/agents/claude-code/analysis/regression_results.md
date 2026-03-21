# Negative Binomial Regression Results — Claude Code Independent Analysis

**Date:** 2026-03-20
**Framework:** CommDAAF v1.0

---

## Model Specification

```
Interest ~ is_battleground + log(population)
Family: Negative Binomial (alpha=1.0)
Link: Log
```

## Overall Battleground Effect

| Metric | Value |
|--------|-------|
| IRR (Incidence Rate Ratio) | 0.9933 |
| 95% CI Lower | 0.9704 |
| 95% CI Upper | 1.0167 |
| p-value | 5.6899e-01 |
| Coefficient | -0.0068 |
| Std Error | 0.0119 |

**Interpretation:** Battleground states have 0.7% LOWER search interest than control/watch states.

## By Category (with Bonferroni Correction)

Bonferroni correction: α = 0.05 / 9 = 0.0056

| Category | IRR | 95% CI | p-value | Bonferroni Sig |
|----------|-----|--------|---------|----------------|
| ai_jobs | 0.7994 | [0.7525, 0.8491] | 3.6884e-13 | YES |
| economy | 0.9342 | [0.8850, 0.9862] | 1.3840e-02 | NO |
| economy_colloquial | 1.0252 | [0.9374, 1.1214] | 5.8555e-01 | NO |
| epstein | 1.0427 | [0.9504, 1.1439] | 3.7664e-01 | NO |
| immigration | 1.1814 | [1.1006, 1.2682] | 3.9836e-06 | YES |
| iran_war | 0.9898 | [0.9329, 1.0502] | 7.3555e-01 | NO |
| partisan_pairs | 1.0454 | [0.9750, 1.1209] | 2.1180e-01 | NO |
| political | 0.9684 | [0.9093, 1.0314] | 3.1847e-01 | NO |
| state_specific | 39.2034 | [1.4530, 1057.7411] | 2.9094e-02 | NO |

---

*Independent analysis by Claude Code (Claude Opus 4.5)*
