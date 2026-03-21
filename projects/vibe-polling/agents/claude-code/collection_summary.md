# Data Collection Summary — VibePoll-2026

**Agent:** Claude Code (Claude Opus 4.5)
**Collection Date:** 2026-03-19
**Framework:** CommDAAF v1.0
**Validation Tier:** EXPLORATORY

---

## Executive Summary

| Data Source | Records/Items | Status |
|-------------|---------------|--------|
| **Google Trends** | 75,894 records | ✅ Complete |
| **Polymarket** | 17 markets | ✅ Complete |
| **Kalshi** | 12 markets | ✅ Complete |
| **Quinnipiac Polls** | 16 polls | ✅ Complete |
| **Marist Polls** | 1 poll | ⚠️ Limited |
| **Emerson Polls** | 17 polls | ✅ Complete |

---

## 1. Google Trends Data

### Collection Statistics

| Metric | Value |
|--------|-------|
| Total Records | 75,894 |
| States Collected | 13 |
| Unique Terms | 76 |
| Categories | 8 |
| Date Range | 2025-12-19 to 2026-03-19 |
| Collection Time | 21.5 minutes |
| Rate Limits Hit | 2 |
| Errors | 0 |

### States Collected

**Battleground (7):**
- PA, MI, WI, AZ, GA, NV, NC

**Control (3):**
- CA (Safe D), TX (Safe R), OH (Lean R)

**Watch (3):**
- ME, NH, MN

### Records per State

| State | Records | Type |
|-------|---------|------|
| PA | 6,006 | Battleground + State-specific |
| MI | 6,006 | Battleground + State-specific |
| WI | 6,006 | Battleground + State-specific |
| AZ | 6,006 | Battleground + State-specific |
| GA | 6,006 | Battleground + State-specific |
| NV | 5,733 | Battleground |
| NC | 5,733 | Battleground |
| CA | 5,733 | Control |
| TX | 5,733 | Control |
| OH | 5,733 | Control |
| ME | 5,733 | Watch |
| NH | 5,733 | Watch |
| MN | 5,733 | Watch |

### Categories Collected

| Category | Weight | Description |
|----------|--------|-------------|
| economy | 0.35 | Gas prices, inflation, cost of living |
| immigration | 0.20 | ICE raids, deportation, asylum |
| political | 0.15 | Voting, registration, approval |
| iran_war | 0.15 | Iran conflict, draft, casualties |
| ai_jobs | 0.10 | AI displacement, automation |
| epstein | 0.05 | Epstein files interest |
| partisan_pairs | — | Media, framing comparisons |
| state_specific | — | Local issues by state |

### Output File
```
data/raw/trends/trends_2026-03-19.parquet
```

---

## 2. Prediction Markets Data

### Polymarket (17 markets)

Election-related markets found via gamma-api.polymarket.com. Note: Some 2026-specific slugs returned 422 errors — markets may use different naming conventions.

### Kalshi (12 markets)

Election markets found via api.elections.kalshi.com. Event tickers for 2026 Congress still being established.

### Output File
```
data/raw/markets/markets_2026-03-19.json
```

---

## 3. Polling Data

### Sources Collected

| Pollster | Polls Found | Notes |
|----------|-------------|-------|
| Quinnipiac | 16 | Iran, Pennsylvania, Trump approval |
| Emerson | 17 | State polls, 2026 races |
| Marist | 1 | Iran war (March 2026) |

### Known Limitations

1. **270toWin**: Uses JavaScript rendering — basic scraping doesn't capture map/race data. Would need Selenium for full support.

2. **RCP (RealClearPolitics)**: Blocks automated requests (HTTP 403). Not included.

3. **VoteHub API**: Returns 403 — may require authentication.

4. **Pollster scrapers**: Extract poll titles/links but not full crosstab data. Marist has PDF crosstabs available for manual download.

### Top-Rated Pollsters (Reference)

Per Silver Bulletin 2026 ratings:
- **Elite tier**: Washington Post, Marquette University, NYT/Siena
- **High quality**: Quinnipiac, Marist, Emerson

### Output File
```
data/raw/polls/polls_2026-03-19.json
```

---

## 4. Data Quality Notes

### Trends Data
- ✅ All 13 states collected successfully
- ✅ No missing categories
- ✅ Consistent record counts per state (varies by state-specific terms)
- ✅ 3-month timeframe provides ~91 daily data points per term

### Markets Data
- ⚠️ Some Polymarket slugs need discovery (2026-specific markets)
- ⚠️ Kalshi event tickers may change as election approaches
- ✅ Historical/closed markets also captured for reference

### Polls Data
- ⚠️ Limited to poll metadata (title, URL, date)
- ⚠️ Full crosstabs require manual PDF download (Marist)
- ⚠️ 270toWin race ratings not captured (JS rendering)

---

## 5. File Manifest

```
data/raw/
├── trends/
│   └── trends_2026-03-19.parquet    (75,894 records)
├── markets/
│   └── markets_2026-03-19.json      (29 markets)
└── polls/
    └── polls_2026-03-19.json        (34 polls)
```

---

## 6. Next Steps

1. **Data Processing (Task 5)**
   - Normalize trends data
   - Calculate z-scores
   - Build issue salience indices

2. **Visualization (Task 6)**
   - State × Issue heatmaps
   - Time series with event annotations
   - Battleground vs control comparisons

3. **Handoff to Other Agents**
   - GLM-4.7: Correlation analysis
   - Kimi K2.5: Statistical modeling

---

## 7. CommDAAF Compliance

- ✅ Realistic search terms validated (78/79 passed)
- ✅ "pro-choice" replaced with "abortion rights"
- ✅ All methodological decisions documented
- ✅ Rate limiting handled gracefully
- ✅ Collection logs maintained

---

*Report generated by Claude Code following CommDAAF v1.0 protocol*
*Collection completed: 2026-03-19 02:50 UTC*
