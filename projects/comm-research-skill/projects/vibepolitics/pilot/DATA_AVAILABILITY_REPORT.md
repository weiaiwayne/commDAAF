# VibePolitics Data Availability Report
## Honest Assessment of What We Can Actually Access

**Date:** February 5, 2026  
**Status:** ✅ Both APIs accessible, real data confirmed

---

## Summary

| Platform | API Access | Auth Required | Politics Markets | Data Quality |
|----------|-----------|---------------|------------------|--------------|
| **Polymarket** | ✅ Working | No | 149 active | ✅ Excellent |
| **Kalshi** | ✅ Working | No (read-only) | 119 events | ⚠️ Lower liquidity |

---

## Polymarket (gamma-api.polymarket.com)

### Access Status: ✅ FULLY ACCESSIBLE

**Endpoint tested:**
```
https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=500
```

### Data Available

| Field | Status | Example Value |
|-------|--------|---------------|
| `volume` (total) | ✅ Yes | $1,054,290 |
| `volume24hr` | ✅ Yes | $6,349 |
| `liquidity` | ✅ Yes | $12,894 |
| `outcomePrices` | ✅ Yes | ["0.0555", "0.9445"] |
| `bestBid` | ✅ Yes | 0.053 |
| `bestAsk` | ✅ Yes | 0.058 |
| `oneDayPriceChange` | ✅ Yes | 0.021 (2.1%) |
| `spread` | ✅ Yes | 0.005 |

### Market Coverage

- **Total active markets:** 500
- **Politics-related:** 149 (Trump, Congress, elections, tariffs, etc.)
- **Economy-related:** 15 (Fed, GDP, Bitcoin, recession)

### Sample Real Data (fetched Feb 5, 2026)

**Market: "Will Trump deport less than 250,000?"**
- Current price: Yes 5.5%, No 94.5%
- 24h volume: $6,349
- Total volume: $1,054,290
- Liquidity: $12,894
- 1-day price change: +2.1%
- Spread: 0.5%

### Limitations
- No historical tick data (only current snapshot)
- Must poll for time series
- Rate limits unknown but generous

---

## Kalshi (api.elections.kalshi.com)

### Access Status: ✅ ACCESSIBLE (Read-Only)

**Endpoint tested:**
```
https://api.elections.kalshi.com/trade-api/v2/events?limit=200&status=open
https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXGDP
```

### Data Available

| Field | Status | Notes |
|-------|--------|-------|
| `volume` | ✅ Yes | Often lower than Polymarket |
| `volume_24h` | ✅ Yes | Many markets show $0 |
| `liquidity` | ✅ Yes | Available |
| `yes_bid` / `yes_ask` | ✅ Yes | Bid-ask spread |
| `last_price` | ✅ Yes | Last trade price |
| `open_interest` | ✅ Yes | Available |

### Market Coverage by Category

| Category | Count |
|----------|-------|
| Politics | 119 |
| Entertainment | 23 |
| Climate and Weather | 9 |
| Economics | 8 |
| Science and Technology | 8 |
| World | 7 |

### Sample Real Data

**Series: KXGDP (GDP Growth)**
- 6% bracket: Yes 1-2¢, Vol $21,052
- 5% bracket: Yes 10-11¢, Vol $28,623
- 4.5% bracket: Yes 16-17¢, Vol $46,401
- 4% bracket: Yes 30-31¢, Vol $42,630

**Series: KXFED (Fed Funds Rate)**
- 4.25% by year-end: Yes 0-37¢, Vol $89
- 3.75% by year-end: Yes 5-48¢, Vol $304
- 3.25% by year-end: Yes 30-54¢, Vol $1,627

### Limitations
- Many political markets have LOW or ZERO 24h volume
- Sports markets dominate by activity
- Political/economic markets exist but are less liquid than Polymarket
- API recently migrated (was trading-api.kalshi.com → api.elections.kalshi.com)

---

## Comparison: Which Platform Has Better Data?

### For Politics/Trump/Policy Markets:
**Winner: Polymarket**
- Higher volume
- More active trading
- Better price discovery on current events

### For Economic Indicators (GDP, Fed):
**Winner: Kalshi (marginally)**
- Has specific brackets for GDP, Fed rates
- But lower overall liquidity

### For Time-Sensitive Signal Detection:
**Winner: Polymarket**
- 24h volume data is more meaningful
- Price changes are more frequent

---

## Recommendations for Pilot Study

1. **Primary data source: Polymarket**
   - Better liquidity, more active trading
   - Better price change data
   - Easier API (no auth)

2. **Secondary data source: Kalshi**
   - Use for GDP/Fed rate specific brackets
   - Lower priority due to liquidity issues

3. **Data collection strategy:**
   - Poll Polymarket every 15-30 minutes
   - Store snapshots for time-series analysis
   - Focus on markets with >$10K daily volume

4. **What we CANNOT do without additional work:**
   - Historical backtesting (no historical API)
   - Order book depth analysis (not exposed)
   - Individual trade data (not available)

---

## API Access Summary

### No API key needed for:
- Polymarket (all read endpoints)
- Kalshi (all read endpoints)

### API key needed for:
- Kalshi trading (placing bets)
- Polymarket trading (blockchain wallet required)

---

## Conclusion

**We have real, working access to both prediction market platforms.**

Polymarket is the better data source for political signal detection due to higher liquidity and more active trading. Kalshi provides useful economic indicator markets but with lower activity.

The pilot study CAN proceed with real data. We should focus on Polymarket for now and add Kalshi as a secondary source for specific economic indicators.

---

*Report generated from live API tests on February 5, 2026*
