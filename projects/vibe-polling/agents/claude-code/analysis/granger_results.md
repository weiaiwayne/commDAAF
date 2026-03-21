# Granger Causality Results — Claude Code Independent Analysis

**Date:** 2026-03-20
**Framework:** CommDAAF v1.0

---

## ⚠️ CRITICAL DATA LIMITATION

**The results in this report are NOT valid for real inference.**

The market data collected is from 2020 elections, while Google Trends data spans Dec 2025 - Mar 2026. Without overlapping time series, Granger causality tests used a **synthetic market proxy** to demonstrate methodology.

**These results demonstrate the METHODOLOGY only, not real causal relationships.**

To answer the research question "Does Google Trends predict prediction markets?", we would need market data that overlaps temporally with the Trends data.

---

## Methodology

- **Test:** Granger causality (F-test)
- **Max lag:** 4 days
- **Note:** Using synthetic market proxy due to data availability

## Vibe Index → Market Proxy

Does Google Trends (Vibe Index) predict market movements?

| State | Type | Min p-value | Best Lag | Significant |
|-------|------|-------------|----------|-------------|
| AZ | BG | 0.0105 | 4 | Yes |
| CA | CTRL | 0.1590 | 1 | No |
| GA | BG | 0.0245 | 1 | Yes |
| ME | WATCH | 0.3890 | 1 | No |
| MI | BG | 0.0048 | 1 | Yes |
| MN | WATCH | 0.0153 | 1 | Yes |
| NC | BG | 0.0281 | 1 | Yes |
| NH | WATCH | 0.0074 | 1 | Yes |
| NV | BG | 0.0018 | 1 | Yes |
| OH | CTRL | 0.0071 | 1 | Yes |
| PA | BG | 0.2933 | 1 | No |
| TX | CTRL | 0.0038 | 1 | Yes |
| WI | BG | 0.0000 | 1 | Yes |

## Market Proxy → Vibe Index

Do markets predict Google Trends?

| State | Type | Min p-value | Best Lag | Significant |
|-------|------|-------------|----------|-------------|
| AZ | BG | 0.0012 | 4 | Yes |
| CA | CTRL | 0.0465 | 1 | Yes |
| GA | BG | 0.0997 | 1 | No |
| ME | WATCH | 0.5768 | 1 | No |
| MI | BG | 0.0790 | 1 | No |
| MN | WATCH | 0.1692 | 2 | No |
| NC | BG | 0.3592 | 3 | No |
| NH | WATCH | 0.0077 | 1 | Yes |
| NV | BG | 0.0146 | 1 | Yes |
| OH | CTRL | 0.4458 | 4 | No |
| PA | BG | 0.5650 | 3 | No |
| TX | CTRL | 0.0371 | 1 | Yes |
| WI | BG | 0.0001 | 1 | Yes |

## Summary

- Vibe → Market significant: 10/13 states
- Market → Vibe significant: 6/13 states

---

*Independent analysis by Claude Code (Claude Opus 4.5)*
