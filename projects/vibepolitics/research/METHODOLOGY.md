# VibePolitics Methodology
## Novel Algorithms for Detecting Public Opinion Shift Signals

**Version:** 0.1  
**Date:** February 4, 2026  
**Authors:** VibePolitics Research Team  

---

## 1. Reframing the Research Question

### 1.1 Critical Distinction

**We are NOT building:** An election forecasting system  
**We ARE building:** A public opinion shift detection system

This distinction is fundamental. Traditional prediction markets research asks: *"Will Candidate X win?"* We ask: **"Is something changing in public sentiment, and what is the nature of that change?"**

### 1.2 Why This Matters

1. **Forecasting is crowded** — 538, Economist, PredictIt already do this
2. **Signal detection is novel** — No systematic approach exists
3. **Academic contribution is clearer** — Methodological innovation vs. incremental improvement
4. **Practical value is higher** — Campaigns/analysts want early warning, not predictions

### 1.3 What Constitutes a "Shift Signal"?

A signal is **not** a prediction. It's evidence that:
- Public attention is changing (volume, search patterns)
- Market participants are updating beliefs (price movements)
- Information is being processed asymmetrically (divergences)
- Uncertainty is increasing or decreasing (volatility, spreads)

---

## 2. Review of Existing Methods

### 2.1 Prediction Market Methods

| Method | Source | Approach | Limitation for Our Purpose |
|--------|--------|----------|---------------------------|
| Price-as-probability | Wolfers & Zitzewitz (2004) | Market price = P(outcome) | Outcome-focused, not shift-focused |
| Market vs. polls comparison | Berg et al. (2008) | Compare market prices to poll aggregates | Still outcome-focused |
| Political Betting Leaning Score | Chen et al. (2024) | Wallet behavior analysis | Requires on-chain data, retrospective |
| Manipulation detection | Smart et al. (2026) | Agent-based simulation | Detects manipulation, not opinion shifts |

### 2.2 Google Trends Methods

| Method | Source | Approach | Limitation for Our Purpose |
|--------|--------|----------|---------------------------|
| Search volume correlation | Prado-Román (2021) | Correlate search volume with votes | Correlational, not causal |
| Variance-in-time | Timoneda & Wibbels (2022) | Track variance spikes, not levels | **Best existing approach** — detects events |
| Multi-feature ML | Behnert et al. (2024) | Random forest on trend features | Black box, hard to interpret |
| Keyword optimization | Polykalas (2013) | Algorithmic keyword selection | Optimizes for prediction, not detection |

### 2.3 Fusion Methods

| Method | Source | Approach | Limitation |
|--------|--------|----------|------------|
| Sentiment + Trends + Polls | Kassraie et al. (2017) | Ensemble model | Still prediction-focused |
| Multi-step LLM reasoning | Yu et al. (2024) | Chain-of-thought for elections | Interesting but not systematic |

### 2.4 Key Insight from Literature

**Timoneda & Wibbels (2022)** is the closest methodological precedent:
> "We argue that it is **variance in search behavior**, not the level, that predicts protest onset."

We extend this insight: **It is variance, divergence, and anomalies in market/search behavior—not levels—that signal opinion shifts.**

---

## 3. Novel Methods: The VibePolitics Signal Detection Framework

### 3.1 Overview

We propose six novel algorithms organized into three categories:

1. **Single-Source Anomaly Detection** (within one data stream)
2. **Cross-Source Divergence Detection** (between data streams)
3. **Agent-Mediated Synthesis** (AI interpretation layer)

```
┌─────────────────────────────────────────────────────────────────┐
│                    VIBEPOLITICS SIGNAL FRAMEWORK                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Polymarket  │  │    Kalshi    │  │ Google Trends│          │
│  │    Data      │  │     Data     │  │     Data     │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                   │
│         ▼                 ▼                 ▼                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │         SINGLE-SOURCE ANOMALY DETECTION                 │   │
│  │  • Volume-Price Decoupling Index (VPDI)                 │   │
│  │  • Liquidity Regime Change Detection (LRCD)             │   │
│  │  • Search Variance Surge Index (SVSI)                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │         CROSS-SOURCE DIVERGENCE DETECTION               │   │
│  │  • Market-Market Divergence Score (MMDS)                │   │
│  │  • Market-Search Divergence Score (MSDS)                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           AGENT-MEDIATED SYNTHESIS                      │   │
│  │  • Composite Anomaly Score (CAS)                        │   │
│  │  • Agent Consensus Divergence (ACD)                     │   │
│  │  • Narrative Shift Detection (NSD)                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│              ┌───────────────────────┐                         │
│              │   SIGNAL ALERTS       │                         │
│              │   (with confidence)   │                         │
│              └───────────────────────┘                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Single-Source Anomaly Detection

### 4.1 Volume-Price Decoupling Index (VPDI)

**Novel Contribution:** Existing literature treats volume as a simple scaling factor. We treat **decoupling between volume and price movement** as an information signal.

#### Intuition

When trading volume spikes but prices don't move proportionally, it suggests:
- Informed traders on both sides (disagreement, information processing)
- Large positions being absorbed by the market
- Potential precursor to price movement (accumulation/distribution)

#### Algorithm

```
VPDI(t) = |ΔVolume(t) / σ_volume| - |ΔPrice(t) / σ_price|
```

Where:
- `ΔVolume(t)` = Volume change from rolling average
- `ΔPrice(t)` = Price change from rolling average  
- `σ_volume`, `σ_price` = Rolling standard deviations (30-day)

**Interpretation:**
- VPDI > 2: High decoupling (signal: absorption/disagreement)
- VPDI < -2: Price moving without volume (thin market, caution)
- |VPDI| < 1: Normal conditions

#### Academic Justification

Extends market microstructure theory (Kyle, 1985; Easley & O'Hara, 1992) to prediction markets. Volume-price relationships have been studied in equity markets but **not systematically applied to political prediction markets**.

---

### 4.2 Liquidity Regime Change Detection (LRCD)

**Novel Contribution:** Use bid-ask spread dynamics as a signal of information arrival, not just market quality.

#### Intuition

Spread changes indicate:
- **Widening spread:** Market makers uncertain, new information arriving
- **Narrowing spread:** Consensus forming, information absorbed
- **Sudden regime changes:** Major shift in market dynamics

#### Algorithm

```
Spread_ratio(t) = Spread(t) / Spread_MA(30)

LRCD triggered when:
  |Spread_ratio(t) - 1| > 2σ for 3+ consecutive observations
```

**Classification:**
- **Widening regime:** Spread_ratio > 1.5 sustained → "Uncertainty surge"
- **Narrowing regime:** Spread_ratio < 0.7 sustained → "Consensus forming"
- **Oscillating regime:** High variance in spread → "Information contest"

#### Academic Justification

Builds on market microstructure literature (Glosten & Milgrom, 1985) and extends the **informed trading** framework to political markets. Novel application to prediction market spreads as political information signals.

---

### 4.3 Search Variance Surge Index (SVSI)

**Novel Contribution:** Extends Timoneda & Wibbels (2022) variance method with multi-keyword and regional components.

#### Intuition

Political shifts manifest in search behavior before they show up in polls or markets:
- **Variance surge:** People searching erratically → uncertainty
- **Correlated regional surges:** Geographic opinion shift
- **Keyword migration:** Searching different terms → narrative shift

#### Algorithm

```
SVSI(t) = Σ_k w_k × [Var(Search_k, window=7) / Var(Search_k, window=30)]
```

Where:
- `k` = keyword index (candidate names, issues, events)
- `w_k` = keyword weight (based on baseline search volume)

**Enhancements over Timoneda & Wibbels:**
1. Multi-keyword aggregation (not single keyword)
2. Regional decomposition (national vs. swing states)
3. Cross-keyword correlation tracking

**Interpretation:**
- SVSI > 2: Search behavior destabilizing → opinion in flux
- SVSI < 0.5: Abnormally stable → potential complacency or data issue
- SVSI ≈ 1: Baseline conditions

---

## 5. Cross-Source Divergence Detection

### 5.1 Market-Market Divergence Score (MMDS)

**Novel Contribution:** First systematic framework for detecting divergence between prediction market platforms.

#### Intuition

Polymarket and Kalshi attract different trader populations:
- **Polymarket:** Crypto-native, international, younger
- **Kalshi:** US-regulated, institutional, traditional finance

Persistent divergence suggests:
- Information asymmetry between populations
- Regulatory/access effects on pricing
- Potential arbitrage opportunity (and information signal)

#### Algorithm

```
MMDS(t) = |P_polymarket(t) - P_kalshi(t)| / σ_divergence
```

Where `σ_divergence` = rolling std of price differences

**Classification:**
- MMDS < 1: Normal arbitrage range
- 1 < MMDS < 2: Elevated divergence (monitor)
- MMDS > 2: **Significant divergence** (signal)
- MMDS > 3: **Extreme divergence** (major information asymmetry)

**Signal Types:**
- **Polymarket leads:** Crypto/international community has information first
- **Kalshi leads:** Institutional/US traders have information first
- **Persistent divergence:** Fundamental disagreement between populations

---

### 5.2 Market-Search Divergence Score (MSDS)

**Novel Contribution:** Detect when market prices and public search interest tell different stories.

#### Intuition

Markets reflect trader beliefs; search reflects public attention. Divergence suggests:
- Markets pricing information the public hasn't absorbed
- Public attention on issues markets are ignoring
- Potential for market correction or attention shift

#### Algorithm

```
Normalize both series to z-scores:
  Z_market(t) = (Price(t) - μ_price) / σ_price
  Z_search(t) = (Search(t) - μ_search) / σ_search

MSDS(t) = |Z_market(t) - Z_search(t)|
```

**Lagged Analysis:**
```
Cross-correlation: ρ(Z_market, Z_search, lag=k) for k ∈ [-14, +14] days
```

**Interpretation:**
- High MSDS + market leads search: Markets have early information
- High MSDS + search leads market: Public attention precedes market pricing
- Persistent high MSDS: Fundamental disconnect (narratives differ)

---

## 6. Agent-Mediated Synthesis

### 6.1 Composite Anomaly Score (CAS)

**Novel Contribution:** AI-weighted fusion of all anomaly signals into interpretable composite.

#### Architecture

Each agent (PolAgent-A, PolAgent-B, EconAgent-A, EconAgent-B) receives all signals and produces:

1. **Signal weights** (how important is each signal right now?)
2. **Signal interpretation** (what does this configuration mean?)
3. **Confidence level** (how certain is the agent?)

```
CAS(t) = Σ_i Σ_a (w_ai × Signal_i(t) × Confidence_a)
```

Where:
- `i` = signal index (VPDI, LRCD, SVSI, MMDS, MSDS)
- `a` = agent index
- `w_ai` = agent a's weight for signal i
- `Confidence_a` = agent a's overall confidence

**Key Innovation:** Agents debate weights and interpretations, producing:
- Consensus weights (where agents agree)
- Contested interpretations (where agents disagree)
- Reasoning traces (why agents weighted signals as they did)

---

### 6.2 Agent Consensus Divergence (ACD)

**Novel Contribution:** Use disagreement between AI agents as a meta-signal.

#### Intuition

When our four agents reach different conclusions from the same data:
- Situation is genuinely ambiguous
- Multiple valid interpretations exist
- Public opinion may be similarly divided

#### Algorithm

```
ACD(t) = Variance([Interpretation_A1, Interpretation_A2, Interpretation_B1, Interpretation_B2])
```

Where interpretations are quantified as:
- Directional assessment (-1 to +1 scale for each candidate/issue)
- Confidence level (0 to 1)
- Signal emphasis (which signals agent weighted most)

**Interpretation:**
- ACD ≈ 0: Strong consensus → high-confidence signal
- 0.3 < ACD < 0.6: Moderate disagreement → uncertain situation
- ACD > 0.6: **High disagreement** → genuinely ambiguous signals, report divergence

**Key Output:** When ACD is high, we report the **range of interpretations**, not a single verdict.

---

### 6.3 Narrative Shift Detection (NSD)

**Novel Contribution:** Use LLM semantic analysis to detect shifts in **what** people discuss, not just **how much**.

#### Intuition

Google Trends volume tells us attention level. But **what keywords rise together** reveals narrative shifts:
- Issue reframing (e.g., "immigration" → "border crisis")
- New association formation (candidate + issue)
- Sentiment shifts in search context

#### Algorithm

**Step 1: Keyword Clustering**
```
For each time window:
  Compute correlation matrix of keyword search volumes
  Identify keyword clusters (hierarchical clustering)
```

**Step 2: Cluster Stability Analysis**
```
Compare cluster composition at t vs. t-7:
  NSD(t) = 1 - Jaccard(Clusters_t, Clusters_{t-7})
```

**Step 3: Agent Interpretation**
```
Agents analyze:
  - Which keywords changed clusters?
  - What narrative does new clustering suggest?
  - Is this shift meaningful or noise?
```

**Interpretation:**
- NSD < 0.2: Stable narrative structure
- 0.2 < NSD < 0.5: Narrative evolution (normal campaign dynamics)
- NSD > 0.5: **Significant narrative shift** (major reframing or new issue)

---

## 7. Signal Classification & Alert System

### 7.1 Signal Taxonomy

| Signal Type | Indicators | Interpretation |
|-------------|-----------|----------------|
| **Attention Surge** | High SVSI, high volume | Public focusing on topic |
| **Market Dislocation** | High MMDS | Trader populations disagree |
| **Information Arrival** | High VPDI, widening LRCD | New info being processed |
| **Consensus Formation** | Narrowing LRCD, low ACD | Opinion crystallizing |
| **Narrative Shift** | High NSD | Issue framing changing |
| **Uncertainty Spike** | High ACD, wide spreads | Genuine ambiguity |

### 7.2 Alert Thresholds

**Level 1 (Monitor):**
- Any single signal > 1.5σ
- Agent notes pattern but no alert

**Level 2 (Notable):**
- Any single signal > 2σ, OR
- Two+ signals > 1.5σ simultaneously
- Logged with interpretation

**Level 3 (Significant):**
- Any single signal > 3σ, OR
- Three+ signals > 2σ simultaneously
- Alert generated with full analysis

**Level 4 (Major):**
- MMDS > 3 (extreme market divergence), OR
- NSD > 0.6 (major narrative shift), OR
- Multiple Level 3 signals
- Priority alert with agent debate summary

---

## 8. Validation Strategy

### 8.1 Backtesting Approach

1. **Historical Event Identification**
   - Identify known opinion shifts (debate effects, scandal breaks, policy announcements)
   - Source: Post-hoc analyses, news archives, polling shifts

2. **Signal Reconstruction**
   - Apply algorithms to historical Polymarket/Google Trends data
   - Did our signals detect the shift? How early?

3. **False Positive Analysis**
   - When did signals fire without corresponding shift?
   - Calibrate thresholds

### 8.2 Benchmark Events for Validation

| Event | Date | Expected Signals |
|-------|------|-----------------|
| Biden withdrawal 2024 | July 2024 | SVSI spike, VPDI, LRCD widening |
| Debate effects | Various | SVSI, MMDS if asymmetric reaction |
| Major endorsements | Various | MSDS divergence, NSD |
| Policy announcements | Various | SVSI on issue keywords |

### 8.3 Validation Metrics

- **Detection rate:** % of known shifts detected
- **Lead time:** How early before polls/news showed shift
- **False positive rate:** Signals without corresponding shifts
- **Interpretation accuracy:** Did agent synthesis correctly characterize shift?

---

## 9. Academic Contribution Summary

### 9.1 Methodological Innovations

1. **VPDI:** First application of volume-price decoupling to prediction markets
2. **LRCD:** Spread dynamics as information signal, not just market quality metric
3. **SVSI:** Multi-keyword, regional extension of Timoneda & Wibbels variance method
4. **MMDS:** First systematic cross-platform prediction market divergence framework
5. **MSDS:** Novel market-search divergence detection
6. **ACD:** Agent disagreement as meta-signal
7. **NSD:** Semantic narrative shift detection via keyword clustering

### 9.2 Theoretical Contributions

1. **Reframing:** Shift from "prediction" to "detection" paradigm
2. **Information theory:** Markets as information processing systems, not just aggregators
3. **Attention economics:** Search behavior as revealed attention, not just revealed preference
4. **Ensemble epistemology:** Multiple AI agents as uncertainty quantification

### 9.3 Practical Contributions

1. **Early warning system:** For campaigns, journalists, analysts
2. **Transparency:** All reasoning visible and auditable
3. **Reproducibility:** Algorithms fully specified, data sources public
4. **Open science:** Methods and (eventually) code published

---

## 10. Implementation Roadmap

### Phase 1: Data Pipeline (Weeks 1-2)
- [ ] Polymarket API integration
- [ ] Kalshi API integration
- [ ] Google Trends API integration
- [ ] Data storage and normalization

### Phase 2: Single-Source Algorithms (Weeks 3-4)
- [ ] Implement VPDI
- [ ] Implement LRCD
- [ ] Implement SVSI
- [ ] Backtest on historical data

### Phase 3: Cross-Source Algorithms (Weeks 5-6)
- [ ] Implement MMDS
- [ ] Implement MSDS
- [ ] Calibrate thresholds

### Phase 4: Agent System (Weeks 7-10)
- [ ] Design agent prompts and reasoning frameworks
- [ ] Implement CAS
- [ ] Implement ACD
- [ ] Implement NSD
- [ ] Agent debate protocol

### Phase 5: Validation & Paper (Weeks 11-16)
- [ ] Comprehensive backtesting
- [ ] Real-time monitoring (2026 primary season)
- [ ] Write methodology paper
- [ ] Prepare submission to *Political Analysis*

---

## Appendix A: Mathematical Notation Summary

| Symbol | Definition |
|--------|------------|
| `P(t)` | Market price at time t |
| `V(t)` | Trading volume at time t |
| `S(t)` | Bid-ask spread at time t |
| `GT_k(t)` | Google Trends index for keyword k at time t |
| `σ_x` | Rolling standard deviation of x (30-day default) |
| `μ_x` | Rolling mean of x |
| `Δx(t)` | Change in x from rolling average |
| `Z_x(t)` | Z-score normalized x |

---

## Appendix B: Data Source Specifications

### Polymarket
- **Endpoint:** `https://gamma-api.polymarket.com/markets`
- **Frequency:** 1-minute to hourly (configurable)
- **Fields:** price, volume, liquidity, spread, 24h change

### Kalshi
- **Endpoint:** `https://trading-api.kalshi.com/v2/markets`
- **Frequency:** Real-time via websocket or polling
- **Fields:** yes_price, volume, open_interest

### Google Trends
- **Method:** pytrends or official API
- **Frequency:** Daily (historical) or real-time
- **Granularity:** National, state-level, DMA-level

---

*Methodology document for VibePolitics project.*  
*Prepared for academic publication.*
