# WorldMonitor Analysis for VibePolitics

*Date: February 11, 2026*
*Source: https://github.com/koala73/worldmonitor*

---

## Executive Summary

WorldMonitor is an open-source real-time global intelligence dashboard that implements many of the patterns we designed for VibePolitics. This analysis identifies transferable components.

---

## Key Technical Components

### 1. Welford's Algorithm for Anomaly Detection

**How it works:**
- Streaming computation of mean and variance (numerically stable)
- Per-event-type baselines (military flights, protests, news velocity, etc.)
- **Weekday and month-specific** baselines (Tuesdays differ from weekends!)
- 90-day rolling window
- Minimum 10 samples before reporting anomalies

**Z-score thresholds:**
| Z-Score | Severity | Example |
|---------|----------|---------|
| ≥ 1.5 | Low | Slightly elevated activity |
| ≥ 2.0 | Medium | Unusual presence |
| ≥ 3.0 | High/Critical | 3x above baseline |

**VibePolitics adaptation:**
- Track Polymarket price volatility per market category, per day-of-week
- "Trump approval market 2.3x above Thursday baseline" is more meaningful than "3% price move"
- Store streaming stats in Redis via Upstash

### 2. Hybrid Classification Pipeline

```
News Item
    │
    ├──► Keyword classifier (instant)
    │         │
    │         ├──► UI shows result immediately
    │         │
    │         └──► Fires LLM classifier (async)
    │                   │
    │                   ├──► Groq Llama 3.1 8B (temperature 0)
    │                   │
    │                   └──► Redis cache (24h TTL, keyed by headline hash)
    │                             │
    │                             └──► Overrides keyword result ONLY if higher confidence
    ▼
Final Classification
```

**Key insight:** UI is never blocked waiting for AI. Users see keyword results instantly, LLM refinements arrive within seconds.

**VibePolitics adaptation:**
- ML anomaly detection shows instantly
- LLM interpretation arrives async and upgrades the signal
- Cache results to avoid re-processing same events

### 3. Country Instability Index (CII)

**Formula:**
| Component | Weight | Details |
|-----------|--------|---------|
| Baseline risk | 40% | Pre-configured per country |
| Unrest events | 20% | Log-scaled for democracies, linear for authoritarian |
| Security activity | 20% | Military flights + vessels |
| Information velocity | 20% | News mentions weighted by severity |

**Additional modifiers:**
- Floor scores for active conflicts (Ukraine ≥55, Syria ≥50)
- Hotspot proximity boosts
- Focal point urgency boosts

**VibePolitics adaptation → Political Volatility Index (PVI):**
| Component | Weight | Details |
|-----------|--------|---------|
| Baseline volatility | 40% | Historical norm for this market |
| Price momentum | 20% | Returns, direction, acceleration |
| Volume surge | 20% | vs. rolling average |
| News velocity | 20% | Mentions weighted by outlet tier |

Floor scores for major events (debate week, election week, scandal breaking).

### 4. Convergence Detection

**WorldMonitor approach:**
- Geographic binning: 1°×1° cells
- 24-hour window
- Alert when 3+ distinct event types converge in one cell
- Scoring: 25pts per unique event type + 2pts per event count

**VibePolitics adaptation → Topic Convergence:**
- "Topic binning" instead of geographic
- Alert when multiple signals align:
  - Price move in Polymarket
  - Volume spike
  - Google Trends surge
  - News velocity increase
  - Kalshi corroboration
- Score by signal diversity: 25pts per unique signal type

### 5. Hotspot Escalation Scoring

**WorldMonitor formula:**
| Signal | Weight |
|--------|--------|
| News activity | 35% |
| Country instability (CII) | 25% |
| Geo-convergence alerts | 25% |
| Military activity | 15% |

**Blend:** 40% static baseline + 60% detected events

**Trend tracking:** Linear regression on 48-hour history

**Signal cooldown:** 2 hours to prevent alert fatigue

**VibePolitics adaptation:**
- News activity (35%) → News mentions for candidate/topic
- Market instability (25%) → PVI score
- Topic convergence (25%) → Multi-signal alignment
- Social activity (15%) → Truth Social/X engagement

### 6. Data Freshness Monitoring

**Status categories:**
- `fresh` (<15 min)
- `stale` (1h)
- `very_stale` (6h)
- `no_data`
- `error`
- `disabled`

**Intelligence gap reporting:** Explicitly reports what analysts CAN'T see.

**Circuit breakers:** Per-feed 5-minute cooldowns prevent cascading failures.

**VibePolitics adaptation:**
Track freshness for:
- Polymarket API
- Kalshi API
- Google Trends
- News RSS feeds
- Polling aggregators

If data source is stale/error, flag outputs as "degraded confidence."

### 7. Prediction Markets as Leading Indicators

**WorldMonitor approach:**
- Query Polymarket with tag-based filters
- 5-minute caching
- Correlate market probability shifts with news volume
- **Flag when market moves before news arrives** → early warning signal

**VibePolitics adoption:** This is core to our thesis. We're already doing this.

### 8. Focal Point Detection

Correlates entities across:
- News articles
- Market activity
- Protests/unrest
- Military movements

When multiple signals converge on same entity → focal point.

**VibePolitics adaptation:**
- Entity extraction from news headlines (NER)
- Correlate with market names
- "Trump" mentioned 47 times in 1 hour + Trump approval market moving = focal point

---

## Architecture Comparison

| Aspect | WorldMonitor | VibePolitics |
|--------|--------------|--------------|
| Signal sources | Military, protests, fires, outages | Markets, polls, social, news |
| Clustering dimension | Geographic (lat/lon) | Topical (candidate/issue) |
| Scope | Global (20 countries) | US-focused (2026 midterms) |
| Output format | Real-time dashboard | Daily briefings + alerts |
| LLM usage | Groq Llama 3.1 8B (single) | Multi-agent debate (3 agents) |
| Caching | Redis (Upstash) | TBD (recommend same) |
| Anomaly detection | Welford's algorithm | Kats + ruptures (upgrade to Welford) |

---

## Recommended Implementation Order

### Phase 1: Foundation (Week 1-2)
1. Implement Welford's algorithm for Polymarket baselines
2. Set up Redis/Upstash for streaming stats storage
3. Define Z-score thresholds for political markets

### Phase 2: Hybrid Pipeline (Week 3-4)
4. Add hybrid classifier pattern (instant ML + async LLM)
5. Implement caching with 24h TTL
6. Build confidence comparison logic

### Phase 3: Scoring Systems (Week 5-6)
7. Build Political Volatility Index (PVI)
8. Add topic convergence detection
9. Implement signal cooldowns

### Phase 4: Robustness (Week 7-8)
10. Data freshness monitoring
11. Circuit breakers
12. Intelligence gap reporting

### Phase 5: Enhancement (Week 9+)
13. Focal point detection with NER
14. Entity-market correlation
15. Story sharing / social export

---

## Code References

**Key technologies used by WorldMonitor:**
- **Frontend:** TypeScript, React
- **Caching:** Redis via Upstash
- **LLM:** Groq API (Llama 3.1 8B)
- **Edge functions:** Vercel Edge
- **Browser ML:** Transformers.js (NER, sentiment)

**Useful patterns:**
- Headline hashing for cache keys
- Temperature 0 for deterministic LLM output
- Virtual scrolling for large lists
- Circuit breakers with 5-minute cooldowns

---

## Key Insight

> WorldMonitor proves the hybrid ML+LLM approach works at scale for real-time intelligence. They've solved many of the same problems we're tackling — just in a different domain (geopolitical vs. political sentiment).

The architecture is validated. We should adopt their patterns rather than reinventing them.

---

*Document created: February 11, 2026*
*Location: projects/vibepolitics/research/WORLDMONITOR_ANALYSIS_2026-02-11.md*
