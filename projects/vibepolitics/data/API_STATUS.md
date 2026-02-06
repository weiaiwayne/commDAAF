# API Data Availability Status
*Last updated: 2026-02-06*

## Polymarket

### ✅ Available (Public)
| Endpoint | Data | Notes |
|----------|------|-------|
| `/events` | Event metadata, title, description, total volume | Via Gamma API |
| `/markets` | Market metadata, outcomes, current prices | Via Gamma API |
| `/prices-history` | Historical prices | Max 14-day window per request, daily/hourly |
| `/midpoint` | Current mid price | Real-time |
| `/spread` | Current bid-ask spread | Real-time |
| `commentCount` | Number of comments | Count only, not content |

### ❌ Missing / Requires Auth
| Data | Status | Workaround |
|------|--------|------------|
| Volume per candle | Auth required (`/trades`) | Only snapshot volume available |
| Trade history | Auth required | None |
| Comment text | Browser/JS required | Would need browser automation |
| Open Interest | Not available | N/A |
| Order book depth | Partial (spread only) | N/A |

### API Quirks
- `clobTokenIds` returned as JSON string, needs parsing
- Time window max 14 days (chunk requests for longer history)
- Some older markets have no price history

---

## Kalshi

### ✅ Available (With Auth)
| Endpoint | Data | Notes |
|----------|------|-------|
| `/markets` | Full market metadata | Requires RSA signature |
| `/series` | Event categories | 8,346 total series |
| `/candlesticks` | OHLCV + Open Interest | Daily/hourly, requires `start_ts` |
| `/orderbook` | Current order book | Real-time |
| `/exchange/status` | Exchange status | |

### ❌ Missing / Limitations
| Data | Status | Notes |
|------|--------|-------|
| Settled market history | Purged after settlement | High-volume 2024 election data gone |
| Trade-level data | May require special access | |
| Comments | Not available | Kalshi doesn't have comments |

### Auth Details
- RSA key signing required
- Sign: `{timestamp}{method}{path}`
- Headers: `KALSHI-ACCESS-KEY`, `KALSHI-ACCESS-SIGNATURE`, `KALSHI-ACCESS-TIMESTAMP`

---

## Data Quality Notes

### Polymarket
- Price = probability (0.0 - 1.0)
- Volume in USDC
- Liquidity reflects current market depth
- Some markets have gaps in price history

### Kalshi
- Price in cents (0-100)
- Volume in contracts
- Open Interest = outstanding contracts
- OHLC provides intraday price range
