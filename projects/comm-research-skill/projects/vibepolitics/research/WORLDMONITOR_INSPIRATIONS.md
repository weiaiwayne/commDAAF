# VibePolitics: Inspirations from World Monitor

**Source:** https://github.com/koala73/worldmonitor  
**Date:** February 11, 2026  
**Purpose:** Technical patterns to incorporate into VibePolitics

---

## 1. Temporal Baseline Anomaly Detection

**What it does:** Uses Welford's online algorithm for numerically stable streaming computation of mean/variance, stored with a 90-day rolling window. Separate baselines for each weekday and month.

**Z-Score Thresholds:**
| Z-Score | Severity | Example |
|---------|----------|---------|
| ≥ 1.5 | Low | Slightly elevated activity |
| ≥ 2.0 | Medium | Unusual presence |
| ≥ 3.0 | High/Critical | 3x above baseline |

**Why it matters for VibePolitics:** This is exactly what we need for detecting opinion SHIFTS rather than absolute levels. Instead of "Trump approval is 45%", we detect "Trump approval dropped 2.3 standard deviations below its Tuesday baseline for February."

**Implementation notes:**
- Minimum 10 historical samples before reporting anomalies (prevents false positives during learning phase)
- Weekday + month segmentation accounts for cyclical patterns (politics differs on weekends, election months, etc.)
- Redis storage for persistence

```python
# Welford's online algorithm
def update_baseline(existing_mean, existing_var, existing_count, new_value):
    count = existing_count + 1
    delta = new_value - existing_mean
    mean = existing_mean + delta / count
    delta2 = new_value - mean
    var = existing_var + delta * delta2
    return mean, var, count

def z_score(value, mean, var, count):
    if count < 10:
        return None  # Not enough data
    std = (var / count) ** 0.5
    return (value - mean) / std if std > 0 else 0
```

---

## 2. Hybrid Classification Pipeline

**Architecture:**
1. **Keyword classifier (instant)** — Pattern-matches against ~120 keywords by severity tier. Returns immediately with confidence score.
2. **LLM classifier (async)** — Fires in background via Edge Function. Results cached 24h by headline hash. Overrides keyword result only if confidence is higher.

**Why it matters for VibePolitics:** UI is never blocked waiting for AI. Users see keyword results instantly, with LLM refinements arriving within seconds.

**For VibePolitics:**
- Instant: Keyword-based sentiment (MAGA, crisis, approval, etc.)
- Async: LLM-refined sentiment with nuance detection
- Cache by content hash to avoid redundant API calls

---

## 3. Prediction Markets as Leading Indicators

**Their approach:** Polymarket queried using tag-based filters with 5-minute caching. Market probability shifts correlated with news volume.

**Key insight:** "If a prediction market moves significantly before matching news arrives, this is flagged as a potential early-warning signal."

**For VibePolitics:** This validates our core thesis. We should:
- Track rate of change in market prices, not just levels
- Correlate market moves with news/social volume
- Flag divergences as high-alpha signals

---

## 4. Country Instability Index (CII) Architecture

**Weighted multi-signal blend:**
| Component | Weight | Details |
|-----------|--------|---------|
| Baseline risk | 40% | Pre-configured structural fragility |
| Detected events | 20% | Protests, incidents (log-scaled for democracies) |
| Security activity | 20% | Military presence, foreign forces |
| Information velocity | 20% | News frequency × severity multiplier |

**Additional mechanics:**
- Conflict-zone floors (Ukraine pinned at ≥55, Syria at ≥50)
- Linear regression on 48-hour history for trend detection
- Boosts for hotspot proximity, focal point urgency

**For VibePolitics — "Sentiment Shift Index" (SSI):**
| Component | Weight | Source |
|-----------|--------|--------|
| Market baseline | 40% | Polymarket 7-day average |
| Market velocity | 25% | Rate of price change |
| Search momentum | 20% | Google Trends delta |
| Retail sentiment | 15% | $TRUMP token price/volume |

---

## 5. Signal Aggregation Pattern

**Their flow:**
```
[Multiple Data Sources]
        ↓
[Central Signal Aggregator]
        ↓
[Per-Country/Region Clustering]
        ↓
[Downstream Analysis Modules]
```

**For VibePolitics:**
```
[Polymarket API] + [Google Trends] + [$TRUMP Token] + [News RSS]
        ↓
[Signal Aggregator]
        ↓
[Per-Topic Clustering] (Trump, Economy, Foreign Policy, etc.)
        ↓
[Agent Analysis] → [Alpha vs Beta Debate]
```

---

## 6. Convergence Detection

**Their approach:** Events binned into 1°×1° geographic cells within 24-hour window. When 3+ distinct event types converge in one cell, a convergence alert fires.

**For VibePolitics — Topic Convergence:**
When multiple signal types spike on the same topic simultaneously:
- Polymarket price drop + Google Trends spike + $TRUMP volume surge = high-confidence shift
- Scoring: ×25pts per unique signal type + event count bonuses

---

## 7. Intelligence Gap Reporting

**Principle:** Explicitly report what analysts CAN'T see. Data source status categories:
- `fresh` (<15 min)
- `stale` (1h)
- `very_stale` (6h)
- `no_data`
- `error`
- `disabled`

**For VibePolitics:** Build trust by showing:
- "Polymarket data: fresh (2 min ago)"
- "Google Trends: stale (47 min) — interpret with caution"
- "⚠️ $TRUMP API unavailable — retail sentiment blind"

---

## 8. Circuit Breakers

**Their approach:** Per-feed circuit breakers with 5-minute cooldowns to prevent cascading failures.

**For VibePolitics:** Essential for robustness:
- If Polymarket API fails 3x → circuit open → fallback to cached data
- If Google Trends rate-limited → exponential backoff
- Never let one failing source crash the whole pipeline

---

## Implementation Priority

1. **Welford's Baseline Algorithm** — Core to shift detection
2. **Hybrid Keyword + LLM Pipeline** — Fast + accurate
3. **Signal Aggregator Architecture** — Clean data flow
4. **Intelligence Gap Reporting** — Trust through transparency
5. **Convergence Detection** — Multi-signal validation
6. **Circuit Breakers** — Production robustness

---

## Discussion Topics for Agents

1. How should we adapt Welford's algorithm for political sentiment specifically?
2. What keyword lists should power the instant classifier?
3. How do we weight conflicting signals (market up, search down)?
4. Should we implement geographic convergence or stick to topic-based?
5. What's our minimum data threshold before declaring a "shift"?

---

*Document prepared for agent discussion on Slack, February 11, 2026*
