# Polymarket API Documentation
*Compiled: 2026-02-05*

## API Endpoints Overview

### 1. Gamma API (`gamma-api.polymarket.com`)
Primary API for market/event metadata.

#### Events
```
GET /events
  ?slug={event-slug}
  ?id={event-id}
  ?active=true|false
  ?closed=true|false
  ?archived=true|false
  ?limit={n}
  ?offset={n}
```

**Event Fields:**
- `id` - Unique event ID
- `slug` - Human-readable identifier
- `title` - Event title
- `description` - Full description
- `commentCount` - Number of comments
- `volume` - Total trading volume (USDC)
- `volume24hr`, `volume1wk`, `volume1mo`, `volume1yr` - Volume periods
- `liquidity` - Current liquidity
- `liquidityClob` - CLOB liquidity
- `competitive` - Competitiveness score (0-1)
- `startDate`, `endDate`, `createdAt`, `updatedAt`
- `active`, `closed`, `archived` - Status flags
- `negRisk` - Supports negative risk trading
- `tags[]` - Associated tags
- `markets[]` - Array of sub-markets

#### Markets
```
GET /markets
  ?slug={market-slug}
  ?id={market-id}
  ?tag={tag-slug}
  ?active=true|false
  ?limit={n}
  ?order={field}
  ?ascending=true|false
```

**Market Fields:**
- `id` - Market ID
- `slug` - Human-readable slug
- `question` - Market question
- `description` - Resolution criteria
- `outcomes` - JSON string of outcome names (e.g., `["Yes", "No"]`)
- `outcomePrices` - JSON string of current prices
- `clobTokenIds` - JSON string of CLOB token IDs for each outcome
- `groupItemTitle` - Name for multi-option markets
- `volume`, `volumeNum` - Trading volume
- `liquidity`, `liquidityNum` - Liquidity
- `oneDayPriceChange`, `oneWeekPriceChange`, `oneMonthPriceChange`
- `bestBid`, `bestAsk`, `spread`
- `conditionId` - Blockchain condition ID
- `questionID` - UMA question ID

#### Tags
```
GET /tags
  ?limit={n}
  ?order={field}
```

Returns all available tags for categorization.

---

### 2. CLOB API (`clob.polymarket.com`)
Central Limit Order Book API for trading data.

#### Price History (PUBLIC - NO AUTH)
```
GET /prices-history
  ?market={token_id}
  ?interval=all|max|1h|6h|1d|1w|1m
  ?fidelity={minutes}  # 1=minute, 60=hourly
  ?startTs={unix_timestamp}
  ?endTs={unix_timestamp}
```

**Response:**
```json
{
  "history": [
    {"t": 1767646819, "p": 0.0175},
    ...
  ]
}
```

#### Real-Time Price Data (PUBLIC)
```
GET /price?token_id={id}&side=buy|sell
GET /midpoint?token_id={id}
GET /spread?token_id={id}
GET /last-trade-price?token_id={id}
```

#### Order Book (PUBLIC)
```
GET /book?token_id={id}
```
Note: Returns error if market has no active order book.

#### Markets List
```
GET /markets
  ?limit={n}
  ?next_cursor={cursor}
```

Returns paginated list of CLOB markets with tokens.

#### Trades (REQUIRES API KEY)
```
GET /trades
  ?token_id={id}
  ?condition_id={id}
  ?limit={n}
```

---

### 3. Key Identifiers

| Type | Format | Example |
|------|--------|---------|
| Event ID | Numeric | `35908` |
| Event Slug | String | `who-will-trump-nominate-as-fed-chair` |
| Market ID | Numeric | `561263` |
| Condition ID | Hex | `0x4714f41...` |
| Token ID | Long numeric | `57761428076807364758801249497410455358987881775226117256631754592198558850468` |

---

### 4. Data Relationships

```
Event (slug: "dem-nominee-2028")
├── commentCount: 474
├── volume: $602M
└── markets[] (128 sub-markets)
    ├── Market (groupItemTitle: "Gretchen Whitmer")
    │   ├── outcomePrices: ["0.0175", "0.9825"]
    │   └── clobTokenIds: ["token_yes", "token_no"]
    ├── Market (groupItemTitle: "Josh Shapiro")
    │   └── ...
    └── ...
```

---

### 5. Comments API
Comments exist (see `commentCount` field) but the public endpoint requires specific parameters:
- `parent_entity_id` - Event or Market ID
- `entity_entity_type` - "event" or "market"

May require authentication or frontend-specific access.

---

### 6. Useful Query Patterns

**Get top political markets by volume:**
```bash
curl "https://gamma-api.polymarket.com/markets?tag=politics&limit=10&order=volume&ascending=false"
```

**Get event with all sub-markets:**
```bash
curl "https://gamma-api.polymarket.com/events?slug=presidential-election-winner-2028"
```

**Get price history (hourly):**
```bash
curl "https://clob.polymarket.com/prices-history?market={token_id}&interval=max&fidelity=60"
```

**Get current mid price:**
```bash
curl "https://clob.polymarket.com/midpoint?token_id={token_id}"
```

---

### 7. Rate Limits
- Gamma API: Generous, no obvious rate limits for public endpoints
- CLOB API: Public endpoints appear unrestricted; authenticated endpoints may have limits

---

### 8. WebSocket (Real-time)
WebSocket feed available at `wss://ws-subscriptions-clob.polymarket.com/ws/`
Requires subscription message with token IDs.

---

### 9. Python Client
Official/community client: `pip install polymarket-apis`
GitHub: https://github.com/qualiaenjoyer/polymarket-apis

---

## Complete API Endpoint Reference

### Gamma API Endpoints (gamma-api.polymarket.com)

| Endpoint | Method | Status | Description |
|----------|--------|--------|-------------|
| `/events` | GET | ✅ Public | Get events by slug, id, filters |
| `/events/{id}` | GET | ✅ Public | Get single event with all fields |
| `/markets` | GET | ✅ Public | Get markets by tag, filters |
| `/markets/{id}` | GET | ✅ Public | Get single market |
| `/tags` | GET | ✅ Public | List all market tags |
| `/comments` | GET | ⚠️ Requires params | Needs `parent_entity_id` + `entity_entity_type` |
| `/users` | GET | 🔐 405 | Method not allowed (may need auth) |
| `/activity` | GET | ❌ 404 | Not found |
| `/leaderboard` | GET | ❌ 404 | Not found |

### CLOB API Endpoints (clob.polymarket.com)

| Endpoint | Method | Status | Description |
|----------|--------|--------|-------------|
| `/prices-history` | GET | ✅ Public | Historical price data (key endpoint!) |
| `/midpoint` | GET | ✅ Public | Current mid price |
| `/spread` | GET | ✅ Public | Bid-ask spread |
| `/last-trade-price` | GET | ✅ Public | Last trade with side |
| `/price` | GET | ✅ Public | Current price by side |
| `/book` | GET | ⚠️ Limited | Order book (if exists) |
| `/markets` | GET | ✅ Public | List CLOB markets |
| `/trades` | GET | 🔐 Auth | Trade history (requires API key) |

### Kalshi API Endpoints (api.elections.kalshi.com)

| Endpoint | Method | Status | Description |
|----------|--------|--------|-------------|
| `/trade-api/v2/markets` | GET | ✅ Public | List markets |
| `/trade-api/v2/events` | GET | ✅ Public | List events |
| `/trade-api/v2/series/{ticker}/markets` | GET | ⚠️ Varies | Markets by series |
| `/trade-api/v2/markets/{ticker}/candlesticks` | GET | ❌ 404 | Price history (may need auth) |

---

## Data Downloaded (2026-02-05)

### Time-Series Data
- **Total files:** 14 CSV files
- **Total data points:** ~10,361 hourly observations
- **Date range:** ~Jan 5 - Feb 5, 2026 (1 month)
- **Location:** `projects/vibepolitics/data/timeseries/`

### Markets Covered:
1. **Dem Nominee 2028:** Whitmer, Shapiro, Newsom, AOC
2. **Fed Chair:** Warsh, Kudlow, Bessent
3. **2028 Presidential:** JD Vance, Newsom
4. **GOP Nominee 2028:** Trump Jr
5. **Other:** Portugal Election, Fed March, Venezuela, Russia-Ukraine Ceasefire

### Summary Files
- `polymarket_top10_political_2026-02-05.csv` - Top 10 summary
- `polymarket_top10_detailed_2026-02-05.csv` - Sub-market breakdowns
- `kalshi_top5_political_2026-02-05.csv` - Kalshi top 5

---

## Notes on Comments API

The Polymarket `commentCount` field shows events have comments (e.g., Fed Chair: 1,317 comments), but the `/comments` endpoint requires specific authentication or parameters not documented publicly.

**Known requirements:**
- `parent_entity_id` - Event or market ID
- `entity_entity_type` - "event" or "market"

May require frontend session authentication. Alternative: Browser automation or authenticated API access.

---

## WebSocket for Real-Time Data

```
wss://ws-subscriptions-clob.polymarket.com/ws/
```

Subscribe to token IDs for real-time price updates.
