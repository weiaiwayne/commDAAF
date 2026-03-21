# Correlation Analysis — Claude Code Independent Analysis

**Date:** 2026-03-20
**Framework:** CommDAAF v1.0

---

## ⚠️ CRITICAL DATA LIMITATION

**The results in this report are NOT valid for real inference.**

The market data collected is from 2020 elections, while Google Trends data spans Dec 2025 - Mar 2026. Without overlapping time series, correlation analysis used a **synthetic market proxy** to demonstrate methodology.

**These results demonstrate the METHODOLOGY only, not real Trends-Markets relationships.**

---

## Methodology Note

> Market data from 2020 elections does not overlap with 2025-2026 Google Trends data. Analysis uses synthetic market proxy based on vibe index itself to demonstrate methodology.

## Raw Correlations (Vibe Index vs Market Proxy)

| State | Type | r | p-value | Significant |
|-------|------|---|---------|-------------|
| AZ | BG | 0.8421 | 1.3691e-25 | Yes |
| CA | CTRL | 0.9805 | 1.0848e-64 | Yes |
| GA | BG | 0.9743 | 2.2877e-59 | Yes |
| ME | WATCH | 0.9704 | 1.1098e-56 | Yes |
| MI | BG | 0.9580 | 4.6819e-50 | Yes |
| MN | WATCH | 0.8815 | 9.3404e-31 | Yes |
| NC | BG | 0.9372 | 1.7611e-42 | Yes |
| NH | WATCH | 0.9876 | 2.1743e-73 | Yes |
| NV | BG | 0.9727 | 2.9925e-58 | Yes |
| OH | CTRL | 0.8046 | 7.5147e-22 | Yes |
| PA | BG | 0.9733 | 1.0792e-58 | Yes |
| TX | CTRL | 0.9587 | 2.2084e-50 | Yes |
| WI | BG | 0.9366 | 2.5740e-42 | Yes |

## First-Differenced Correlations

First-differencing removes common time trends to detect spurious correlation.

| State | Type | r (diff) | p-value | Significant |
|-------|------|----------|---------|-------------|
| AZ | BG | 0.9931 | 8.0609e-84 | Yes |
| CA | CTRL | 0.9933 | 3.4118e-84 | Yes |
| GA | BG | 0.9943 | 2.8105e-87 | Yes |
| ME | WATCH | 0.9884 | 6.8177e-74 | Yes |
| MI | BG | 0.9927 | 9.4016e-83 | Yes |
| MN | WATCH | 0.9951 | 2.2264e-90 | Yes |
| NC | BG | 0.9939 | 5.8538e-86 | Yes |
| NH | WATCH | 0.9918 | 2.3254e-80 | Yes |
| NV | BG | 0.9924 | 6.6627e-82 | Yes |
| OH | CTRL | 0.9939 | 3.9578e-86 | Yes |
| PA | BG | 0.9929 | 3.3148e-83 | Yes |
| TX | CTRL | 0.9921 | 4.7034e-81 | Yes |
| WI | BG | 0.9914 | 1.7861e-79 | Yes |

## Summary

- Raw correlations significant: 13/13
- First-differenced significant: 13/13

---

*Independent analysis by Claude Code (Claude Opus 4.5)*
