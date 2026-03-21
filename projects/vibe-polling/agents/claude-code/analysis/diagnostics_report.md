# Distribution Diagnostics Report — Claude Code Independent Analysis

**Date:** 2026-03-20
**Framework:** CommDAAF v1.0

---

## Overall Statistics

| Metric | Value |
|--------|-------|
| N | 38,311 |
| Mean | 25.92 |
| Std | 27.42 |
| Median | 14.00 |
| Min | 0 |
| Max | 100 |
| Skewness | 0.782 |
| Kurtosis | -0.628 |
| % Zeros | 19.9% |
| Variance/Mean | 29.02 |

## Overdispersion Assessment

Variance/Mean ratio = 29.02 > 1

**Conclusion:** Data is OVERDISPERSED. Negative Binomial regression is appropriate.

## By State

| State | Type | Mean | % Zeros | V/M | Skewness |
|-------|------|------|---------|-----|----------|
| AZ | BG | 27.1 | 15.1% | 26.2 | 0.69 |
| CA | CTRL | 30.6 | 0.2% | 25.7 | 0.67 |
| GA | BG | 29.4 | 6.7% | 25.0 | 0.67 |
| ME | WATCH | 16.7 | 60.3% | 41.0 | 1.31 |
| MI | BG | 29.8 | 10.3% | 25.1 | 0.58 |
| MN | WATCH | 24.7 | 22.2% | 28.3 | 0.85 |
| NC | BG | 27.3 | 7.8% | 27.1 | 0.72 |
| NH | WATCH | 16.3 | 58.2% | 39.0 | 1.36 |
| NV | BG | 22.3 | 40.5% | 34.1 | 0.93 |
| OH | CTRL | 27.6 | 7.8% | 24.4 | 0.67 |
| PA | BG | 29.6 | 3.3% | 25.2 | 0.70 |
| TX | CTRL | 28.4 | 0.9% | 27.1 | 0.75 |
| WI | BG | 26.6 | 26.9% | 30.6 | 0.70 |

## By Category

| Category | Mean | % Zeros | Skewness |
|----------|------|---------|----------|
| ai_jobs | 14.9 | 19.4% | 1.73 |
| economy | 28.9 | 16.9% | 0.70 |
| economy_colloquial | 41.6 | 15.5% | 0.16 |
| epstein | 16.9 | 18.6% | 1.92 |
| immigration | 37.4 | 24.9% | 0.05 |
| iran_war | 22.5 | 21.9% | 0.85 |
| partisan_pairs | 39.6 | 8.0% | -0.13 |
| political | 15.7 | 28.2% | 1.36 |
| state_specific | 40.2 | 11.6% | 0.27 |

---

*Independent analysis by Claude Code (Claude Opus 4.5)*
