# VibePolitics: Exploratory Data Analysis Report
*Generated: 2026-02-06*

## Executive Summary

Analysis of 6 months of prediction market data from Polymarket (7 markets) and Kalshi (12 markets) reveals several actionable patterns for the VibePolitics system.

---

## 1. Data Overview

### Polymarket (Extended History)
| Market | Days | Price Change | Volatility |
|--------|------|--------------|------------|
| Fed Chair - Warsh | 184 | 19.5% → 95.2% (+388%) | 0.185 |
| Dem Nom - Newsom | 184 | 19.5% → 29.5% (+51%) | 0.044 |
| Dem Nom - Whitmer | 184 | 5.7% → 1.8% (-69%) | 0.012 |
| Dem Nom - Shapiro | 184 | 6.0% → 5.7% (-7%) | 0.009 |
| Fed Chair - Bessent | 184 | 5.0% → 0.1% (-99%) | 0.019 |
| Fed Chair - Kudlow | 184 | 0.5% → 0.1% (-91%) | 0.001 |
| GOP Nom - Trump Jr | 184 | 2.9% → 1.6% (-46%) | 0.005 |

### Kalshi (Daily OHLCV)
| Market | Days | Volume | Pattern |
|--------|------|--------|---------|
| Large Tariff | 174 | $739K | 52¢ → 99¢ (+90%) |
| Trump Resign | 171 | $100K | Stable 19-20¢ |
| Kansas Gov (EC) | 35 | $4.2K | Rising 58¢ → 73¢ |

---

## 2. Key Findings

### 2.1 Correlation Clusters

**Strongest correlations discovered:**

| Market Pair | Correlation | Interpretation |
|-------------|-------------|----------------|
| Whitmer ↔ Trump Jr | +0.83 | Both declining - common sentiment? |
| Whitmer ↔ Kudlow | +0.67 | Unexpected linkage |
| Newsom ↔ Whitmer | -0.65 | **Substitution effect** (zero-sum) |
| Shapiro ↔ Warsh | +0.63 | Cross-event correlation |
| Newsom ↔ Kudlow | -0.59 | Inverse relationship |

**Insight:** Markets that *should* be independent (Fed Chair vs Dem Nominee) show significant correlation, suggesting hidden common factors (likely Trump administration sentiment).

### 2.2 Regime Change Events

**Kevin Warsh Timeline:**
```
Aug-Sep 2025: 19.5% → 20.0% (+3%)   | Flat, low vol
Oct-Nov 2025: 19.0% → 12.0% (-37%)  | Declining
Dec 2025:     10.0% → 32.5% (+225%) | BREAKOUT
Jan 2026:     31.5% → 63.5% (+102%) | Continuation
Feb 2026:     97.5% → 95.2% (-2%)   | Consolidation
```

**Key Breakout: December 13, 2025**
- Single-day move: +173% (13% → 35.5%)
- Preceded by volatility cluster Dec 4-12
- Suggests news event caused regime change

### 2.3 Volume-Price Relationship (Kalshi)

| Volume Quartile | Avg Daily Price Move |
|-----------------|---------------------|
| Low | 2.10% |
| Med-Low | 2.04% |
| Med-High | 1.97% |
| **High** | **3.88%** |

**Insight:** High volume days show ~2x larger price moves. Volume can be a leading indicator of price action.

### 2.4 Market Efficiency Metrics

| Market | Autocorr (1d) | Var Ratio | Hurst | Pattern |
|--------|---------------|-----------|-------|---------|
| Newsom | +0.23 | 1.66 | 0.60 | **Momentum/Trending** |
| Shapiro | -0.03 | 1.09 | 0.53 | Efficient |
| Whitmer | -0.19 | 0.85 | 0.56 | Mean-reverting |
| Warsh | -0.05 | 0.92 | 0.53 | Efficient |
| Trump Jr | -0.22 | 0.57 | 0.46 | **Mean-reverting** |

**Insight:** 
- Newsom shows **momentum** - price increases predict further increases
- Trump Jr shows **mean-reversion** - price moves tend to reverse
- Warsh is **efficient** - prices reflect information quickly

### 2.5 Open Interest Analysis (Kalshi - Trump Resign)

```
Start:   20,616 contracts
Peak:    45,451 contracts
Current: 45,451 contracts (at peak)
Price:   Stable 19-20¢ throughout
```

**Insight:** Despite 2x growth in open interest, price remained stable. Market has reached **consensus** - high confidence in outcome.

---

## 3. Volatility Clusters (Warsh)

| Period | Dates | Price Movement | Interpretation |
|--------|-------|----------------|----------------|
| Cluster 1 | Aug 21-27 | 20.5% → 15.0% | Initial decline |
| Cluster 2 | Sep 9-15 | 22.5% → 19.5% | Continued uncertainty |
| Cluster 3 | **Dec 4-24** | 16.5% → 21.5% | **Pre-breakout warning** |
| Cluster 4 | Jan 21-23 | 46.5% → 45.5% | Consolidation |
| Cluster 5 | Jan 30-Feb 6 | 63.5% → 95.7% | **Final surge** |

**Insight:** Volatility clusters precede major moves. Dec 4-12 cluster preceded the Dec 13 breakout.

---

## 4. Actionable Signals for VibePolitics

### Signal 1: Volatility Clustering → Regime Change Alert
When 7-day rolling volatility exceeds 75th percentile for 3+ consecutive days, flag as potential regime change.

### Signal 2: Cross-Market Correlations
Monitor unexpected correlations between unrelated events. Current example: Shapiro ↔ Warsh (+0.63) suggests hidden common factor.

### Signal 3: Volume Spikes
Kalshi volume spikes (>2x average) correlate with 2x larger price moves. Use as confidence multiplier.

### Signal 4: Momentum vs Mean-Reversion
- **Momentum markets** (Newsom): Trend-following signals
- **Mean-reverting markets** (Trump Jr): Contrarian signals

### Signal 5: Open Interest Divergence
When OI rises but price is stable → Market consensus forming. Reduce position variance forecasts.

---

## 5. Key Dates for Event Correlation

| Date | Market(s) | Event | Price Impact |
|------|-----------|-------|--------------|
| Aug 20-21, 2025 | Newsom, Shapiro | Both spike | +17%, +43% |
| Oct 26-28, 2025 | Whitmer | Collapse | -41% |
| Dec 3-4, 2025 | Warsh | Pre-breakout vol | ±38% |
| Dec 13, 2025 | Warsh | **Major breakout** | +173% |
| Jan 30, 2026 | Warsh, Bessent | Final resolution | +131%, -93% |

---

## 6. Data Quality Notes

### Limitations
- Polymarket: No per-candle volume (requires auth)
- Kalshi: Settled markets purged (2024 election data lost)
- No comment/sentiment data

### Recommendations
1. Acquire Polymarket API credentials for volume data
2. Set up real-time collection before markets settle
3. Correlate dates with news events for interpretation

---

## Appendix: File Locations

```
projects/vibepolitics/data/
├── timeseries_extended/    # Polymarket 6-month daily (7 files)
├── timeseries/             # Polymarket 1-month hourly (14 files)
├── kalshi/timeseries/      # Kalshi daily OHLCV (12 files)
└── API_STATUS.md           # API availability reference
```
