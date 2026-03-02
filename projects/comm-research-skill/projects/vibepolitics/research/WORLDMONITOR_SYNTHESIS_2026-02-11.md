# WorldMonitor → VibePolitics: Agent Synthesis

*Date: February 11, 2026*
*Source: https://github.com/koala73/worldmonitor*
*All 5 Agents Reviewed*

---

## Executive Summary

WorldMonitor is an open-source OSINT dashboard that has already solved many problems VibePolitics faces. All 5 agents agree: **don't fork the whole project — borrow the algorithms and patterns**.

**Universal consensus:**
1. **Welford's algorithm** for streaming anomaly detection (HIGH priority)
2. **Hybrid classifier** (instant keyword + async LLM) validates our Layer 1/2 architecture
3. **Three-tier caching** (in-memory → Redis → upstream) reduces costs ~80%
4. **Intelligence gap reporting** — never silently degrade

---

## Agent Contributions Summary

| Agent | Focus | Key Contribution |
|-------|-------|------------------|
| **OpenClaw** 🎯 | Architecture mapping | Detailed feature-by-feature translation |
| **Mei** 🔗 | System coherence | "Signal fusion" core insight; what NOT to borrow |
| **Priya** 📚 | Academic framing | OSINT literature connection; prioritized borrow list |
| **Kenji** 🔬 | Implementation | PSSI formula; source tiering; phased roadmap |
| **Arjun** 🔥 | Practical execution | "git clone to vendor"; blind spots; RPi constraints |
| **Wei** 📊 | Novel metrics | VII formula; hunch calibration; research differentiation |

---

## Part 1: Unanimous Adoptions (All Agents Agree)

### 1.1 Welford's Algorithm for Anomaly Detection

**What WorldMonitor does:**
- Streaming mean/variance computation (numerically stable)
- Separate baselines per **weekday + month** (Tuesday differs from weekend!)
- Z-score thresholds: 1.5 (watch) → 2.0 (alert) → 3.0 (critical)
- Minimum 10 samples before reporting (prevents learning-phase false positives)
- 90-day rolling window stored in Redis

**VibePolitics adaptation:**
```python
# Current: Static thresholds (e.g., price change > 2%)
# Proposed: Learned baselines per market, per day of week

# Example output:
# "Polymarket Trump approval normally varies ±1.2% on Mondays"
# "Today's ±3.8% movement is 2.7σ above Monday baseline"

class WelfordAnomalyDetector:
    def __init__(self, window_days=90):
        self.n = 0
        self.mean = 0
        self.M2 = 0  # For variance computation
        
    def update(self, x):
        self.n += 1
        delta = x - self.mean
        self.mean += delta / self.n
        delta2 = x - self.mean
        self.M2 += delta * delta2
        
    def zscore(self, x):
        if self.n < 2:
            return 0
        variance = self.M2 / (self.n - 1)
        std = variance ** 0.5
        return (x - self.mean) / std if std > 0 else 0
        
    def is_anomaly(self, x, threshold=2.0):
        return abs(self.zscore(x)) > threshold
```

**Why all agents agree:** Solves the "regime change" blind spot Wei identified. Adapts to changing political environments automatically.

---

### 1.2 Hybrid Classification Pipeline

**What WorldMonitor does:**
```
Keyword classifier (instant, ~120 patterns)
        ↓
    UI shows result immediately
        ↓ (async)
LLM classifier (Groq Llama 3.1)
        ↓
    Overrides ONLY if higher confidence
        ↓
Redis cache (24h TTL, keyed by headline hash)
```

**VibePolitics adaptation (Arjun's framing):**
> "Keyword sentiment (VADER vibes) → async LLM (Kimi/Grok) override. Fits Layer1/2: Instant Fox tone → pollster hunch."

**Implementation:**
```python
class HybridPoliticalClassifier:
    def classify(self, headline, market_context):
        # Stage 1: Instant keyword match
        keyword_result = self.keyword_classifier(headline)
        
        # Stage 2: Async LLM (if needed)
        if keyword_result['confidence'] < 0.7:
            llm_result = self.llm_classifier(headline, market_context)
            if llm_result['confidence'] > keyword_result['confidence']:
                return llm_result
                
        return keyword_result

# Political keyword patterns
POLITICAL_KEYWORDS = {
    'critical': ['impeachment', 'resignation', 'indictment', 'scandal'],
    'high': ['approval rating', 'poll shift', 'primary challenge'],
    'medium': ['debate', 'endorsement', 'rally'],
    'low': ['interview', 'speech', 'campaign event']
}
```

**Cost impact (Priya):** Reduces LLM costs by ~70% while maintaining quality.

---

### 1.3 Three-Tier Caching Strategy

**WorldMonitor pattern:**
```
Request → [1] In-Memory (per instance) → [2] Redis (cross-user) → [3] Upstream API
          Stale data served on error with explicit "Data Gap" banner
```

**VibePolitics adaptation (Wei):**
- Layer 1 (ML) results cached in-memory
- Layer 2 (LLM) calls cached in Redis with content-hash deduplication
- Prevents 100 concurrent users from triggering 100 identical LLM calls

**Implementation (Mei):**
```python
def fetch_rcp_data():
    cache_key = f"rcp_trump_approval_{date.today()}"
    
    # Try in-memory
    if cache_key in memory_cache:
        return memory_cache[cache_key]
    
    # Try file cache (your memory/ directory)
    cached_file = f"memory/rcp_{date.today()}.json"
    if os.path.exists(cached_file):
        with open(cached_file) as f:
            data = json.load(f)
        memory_cache[cache_key] = data
        return data
    
    # Fetch fresh
    fresh_data = browser_fetch_rcp()
    
    # Cache to file
    with open(cached_file, 'w') as f:
        json.dump(fresh_data, f)
    
    memory_cache[cache_key] = fresh_data
    return fresh_data
```

**Cost impact:** ~80% reduction in API/LLM costs.

---

### 1.4 Intelligence Gap Reporting

**WorldMonitor approach:**
- Tracks 14 data sources with status: `fresh (<15 min) → stale (1h) → very_stale (6h) → no_data → error`
- Explicitly reports **what analysts CAN'T see**
- Never silently degrades

**VibePolitics adaptation (Kenji):**
```
DATA FRESHNESS STATUS:
✅ RCP averages: Fresh (2 min ago)
⚠️ Truth Social: Stale (35 min ago - browser timeout)
❌ Polymarket: No data (API key missing)
✅ Google Trends: Fresh (15 min ago)

INTELLIGENCE GAP: Truth Social data is 6h old; MAGA temperature may be inaccurate.
```

**Why this matters (Wei):** Prevents false confidence. Academic credibility requires transparency about data limitations.

---

## Part 2: Composite Index Proposals

### 2.1 Public Sentiment Shift Index (PSSI) — Kenji

```python
PSSI = (
    0.30 × Prediction_Market_Velocity  # normalized
    + 0.25 × Search_Trend_Variance      # Google Trends
    + 0.20 × News_Sentiment_Shift       # simple NLP
    + 0.15 × Social_Media_Engagement    # Truth Social
    + 0.10 × Cross_Source_Correlation   # market ↔ search
)
```

**Academic advantage:** Provides single metric for "how much is opinion shifting."

---

### 2.2 Vibe Instability Index (VII) — Wei

```python
VII = (
    0.30 × Market_Conviction_Score
    + 0.25 × Search_Variance_Spike
    + 0.20 × Media_Tone_Shift
    + 0.15 × Agent_Hunch_Agreement
    + 0.10 × Cross_Market_Correlation
)
```

**Key difference from PSSI:** Includes "Agent Hunch Agreement" — our unique multi-agent debate output becomes a signal.

---

### 2.3 Source Credibility Tiering — Kenji

| Tier | Sources | Weight |
|------|---------|--------|
| **Tier 1** | 538, RCP averages, official polls | 1.0 |
| **Tier 2** | Individual pollsters (YouGov, Emerson) | 0.9 |
| **Tier 3** | Prediction markets (Polymarket, Kalshi) | 0.7 |
| **Tier 4** | Social media sentiment | 0.5 |

**Implementation:**
```python
def weight_by_source(pollster, value):
    tier_multiplier = {
        'Tier 1': 1.0,
        'Tier 2': 0.9,
        'Tier 3': 0.7,
        'Tier 4': 0.5
    }
    return value * tier_multiplier.get(get_tier(pollster), 0.5)
```

---

## Part 3: Novel Contributions (VibePolitics Differentiation)

### 3.1 Hunch Calibration Logging — Wei

WorldMonitor tracks LLM classifier confidence. We should track **agent hunch accuracy**:

```python
# Log hunch with timestamp
[Agent-Beta: "Fox tone is defensive"] → Confidence: 0.72

# 72h later: Market moved -3%
[Hunch validated] → Update agent "calibration score"

# Future runs: Weight Agent-Beta higher for tone detection
```

**Research value:** Novel contribution on "Hunch-Based Signal Detection."

---

### 3.2 Narrative Convergence Detection — Wei

WorldMonitor detects **geographic convergence** (3+ event types in one cell).

VibePolitics should detect **narrative convergence**:
- When Polymarket + Google Trends + News Velocity all move same direction
- Flag "confidence multiplier" for that signal

---

### 3.3 Multi-Agent Debate Transparency — Wei

**Our competitive advantage:**
> "They use LLMs but don't expose the reasoning trace. Our adversarial agents are a competitive advantage."

WorldMonitor: Single LLM classification
VibePolitics: Alpha/Beta/Historian debate with visible reasoning

---

## Part 4: What NOT to Borrow

### 4.1 Mei's Warnings

| Don't Borrow | Why |
|--------------|-----|
| Geographic Map Layers | VibePolitics is US-focused, not geospatial |
| Military/Infrastructure Tracking | Not relevant to political opinion |
| Macro Signal Radar | We focus on political sentiment, not crypto |
| WebSocket Streaming | Daily cron workflow doesn't need real-time |

### 4.2 Arjun's Warnings

| Blind Spot | Concern |
|------------|---------|
| Overbuilt for RPi | WebGL/ML worker = CPU killer on Raspberry Pi |
| Geopolitics ≠ vibes | Adapt patterns, don't fork the whole project |
| No evals | They don't have accuracy metrics — we need to add them |

### 4.3 Kenji's Warning

> "Don't copy the massive 45+ edge function architecture. Do copy the signal fusion algorithms, caching strategy, and systematic approach to unreliable data."

---

## Part 5: Implementation Roadmap

### Phase 1: Signal Infrastructure (Week 1-2)
*Source: Kenji + Priya consensus*

1. **Implement Welford's algorithm** for market data baselines
2. **Add data freshness monitoring** with intelligence gap reporting
3. **Set up Redis caching** (Upstash free tier: 10K commands/day)

### Phase 2: Hybrid Classification (Week 3)
*Source: All agents*

4. **Implement hybrid classifier** — keyword patterns + async LLM
5. **Add time windows** — 1h/6h/24h/7d toggle
6. **Cache LLM results** by headline hash

### Phase 3: Composite Indices (Week 4-5)
*Source: Kenji + Wei*

7. **Build PSSI or VII** — choose one as primary metric
8. **Add source tiering** and weighting
9. **Implement convergence detection**

### Phase 4: Validation & Refinement (Week 6+)
*Source: Arjun + Wei*

10. **Track index accuracy** against subsequent polls
11. **Implement hunch calibration** logging
12. **Refine weights** based on performance

---

## Part 6: Immediate Actions

### Arjun's Practical Recommendation

```bash
# Clone to vendor directory
git clone https://github.com/koala73/worldmonitor vibepolitics/vendor/worldmonitor

# Port key modules to OpenClaw exec/cron
# - anomaly.py (Welford's algorithm)
# - classifiers (hybrid keyword/LLM)

# Prototype hunch convergence next
```

### Priya's Week-by-Week

**Week 1: Quick Wins**
1. Implement hybrid classifier — keyword patterns, LLM override only for <0.7 confidence
2. Add time windows — 1h/6h/24h/7d toggle
3. Redis caching — cache LLM results by headline hash

**Week 2: Core Improvements**
4. Welford anomaly detection — replace static thresholds
5. Focal point detection — correlate Polymarket + news + search

**Week 3: Advanced Features**
6. Composite index scoring (PSSI or VII)
7. Circuit breakers — resilience for API failures

---

## Part 7: Academic Framing

### Priya's Positioning

> "Geospatial intelligence methodologies applied to political forecasting"

Connects VibePolitics to:
- OSINT (Open Source Intelligence) literature
- Crisis early warning systems
- Multi-source data fusion research

**Key citation:** WorldMonitor's approach mirrors how intelligence agencies (CIA Open Source Center, EU INTCEN) process multiple signal types — VP applies this to domestic political monitoring.

### Wei's Research Differentiation

| Our Opportunity | Why WorldMonitor Doesn't Have It |
|-----------------|----------------------------------|
| Multi-Agent Debate Transparency | They use LLMs but don't expose reasoning trace |
| "Hunch" as First-Class Signal | Their system is fully data-driven; we have expert intuition layer |
| US Midterm-Specific Framing | Their global focus dilutes domestic political nuance |

---

## Part 8: Key Quotes

**Mei (Integrator):**
> "World Monitor is fundamentally about signal fusion — taking noisy data from many sources and detecting when they converge into meaningful intelligence. VibePolitics does this conceptually (your 'seasoned pollster' intuition), but World Monitor shows how to operationalize it systematically."

**Kenji (Methodologist):**
> "WorldMonitor provides battle-tested patterns for exactly what VibePolitics needs: transforming noisy, unreliable signals into actionable intelligence. The key insight isn't the dashboard—it's the statistical rigor behind the dashboard."

**Arjun (Skeptic):**
> "Not vibes, but signal fusion gold... Action: git clone to vibepolitics/vendor/worldmonitor; port anomaly.py + classifiers to OpenClaw exec/cron. Prototype hunch convergence next?"

**Wei (Empiricist):**
> "Their approach is highly complementary to VibePolitics—they focus on geopolitical/infrastructure intelligence while we focus on domestic political sentiment. We can directly adopt several of their patterns."

**Priya (Theorist):**
> "WorldMonitor is an impressive reference architecture. The hybrid classifier and temporal baseline detection are the two highest-value elements to port to VP immediately — they solve your cost and calibration problems respectively."

---

## Appendix: Decision Matrix

| Feature | Effort | Impact | Priority | Owner |
|---------|--------|--------|----------|-------|
| Welford's algorithm | Medium | High | 🔴 Critical | TBD |
| Hybrid classifier | Low | High | 🔴 Critical | TBD |
| Three-tier caching | Low | Medium | 🟡 High | TBD |
| Intelligence gaps | Low | Medium | 🟡 High | TBD |
| PSSI/VII index | Medium | Medium | 🟢 Medium | TBD |
| Hunch calibration | Medium | High | 🟢 Medium | TBD |
| Circuit breakers | Low | Medium | 🟢 Medium | TBD |
| Browser-side ML | High | Medium | 🔵 Low | TBD |

---

*Document created: February 11, 2026*
*All 5 agents contributed*
*Location: projects/vibepolitics/research/WORLDMONITOR_SYNTHESIS_2026-02-11.md*
