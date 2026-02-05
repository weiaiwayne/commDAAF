# VibePolitics: Agentic Unconventional Polling System

**Project Codename:** VibePolitics  
**Version:** 0.1 (MVP Specification)  
**Date:** February 4, 2026  
**Location:** Boston, MA  

---

## Executive Summary

VibePolitics is an autonomous multi-agent system designed to poll American public opinion through unconventional data sources. Rather than traditional surveys, the system analyzes revealed preferences via prediction markets and search behavior patterns. The goal is to provide a novel, continuous survey of public sentiment regarding the 2026 midterm elections and the Trump presidency.

This project is designed with academic rigor, aiming for publication in peer-reviewed scientific journals.

---

## Part 1: Theoretical Foundation

### 1.1 The Problem with Traditional Polling

Traditional polling faces several well-documented challenges:

1. **Response bias** — People say what they think pollsters want to hear
2. **Social desirability bias** — Reluctance to express controversial views
3. **Nonresponse bias** — Who answers polls ≠ who votes
4. **Timing** — Polls are snapshots; attitudes are continuous
5. **Cost** — High-quality polls are expensive and infrequent
6. **2016/2020 misses** — Systematic underestimation of Trump support

### 1.2 Revealed vs. Stated Preferences

The core insight: **When people put money on an outcome, they reveal their true beliefs.**

| Stated Preferences (Polls) | Revealed Preferences (Markets) |
|---------------------------|-------------------------------|
| "Who will you vote for?" | "Where is your money?" |
| Subject to social pressure | Financial incentive for accuracy |
| Periodic snapshots | Continuous real-time data |
| Self-reported | Behaviorally observed |

### 1.3 Prediction Markets as Polls

Prediction markets aggregate distributed information. Each trade represents someone's updated belief given their private information. The market price thus reflects the crowd's aggregated probability assessment.

**Key advantages:**
- Continuous updating (24/7)
- Financial incentives align with truthfulness
- Skin in the game reduces cheap talk
- Historical accuracy often exceeds polls (especially for elections)

### 1.4 Search Behavior as Sentiment

Google Trends data reveals what people are *actually curious about*, not what they claim to care about. Search volume for politically relevant terms can predict:

- Issue salience (what's top of mind)
- Information-seeking behavior (uncertainty, curiosity)
- Grassroots interest vs. media-driven attention
- Regional variation in concerns

---

## Part 2: System Architecture

### 2.1 Framing

We are an **agentic research team based in Boston, MA**, tasked with polling American public opinion using unconventional methodologies. The team consists of four autonomous AI agents, each with specialized expertise and the ability to collaborate, debate, and reason transparently.

### 2.2 The Four Agents

| Agent | Domain | Role | Personality |
|-------|--------|------|-------------|
| **PolAgent-A** | Political Analysis | Tracks political markets, candidate dynamics, party movements | Analytical, data-driven |
| **PolAgent-B** | Political Analysis | Counter-analyst, challenges PolAgent-A's interpretations | Skeptical, contrarian |
| **EconAgent-A** | Economic Analysis | Monitors economic policy markets, Fed, fiscal policy | Macro-focused, quantitative |
| **EconAgent-B** | Economic Analysis | Counter-analyst, alternative economic interpretations | Heterodox, considers second-order effects |

### 2.3 Agent Behaviors

Each agent is fully autonomous and can:

1. **Analyze data sources** — Pull from Polymarket, Kalshi, Google Trends
2. **Search for context** — Use AI APIs to research news, historical context, academic literature
3. **Decide to act or not act** — Evaluate whether a signal warrants attention
4. **Choose keywords** — Autonomously decide what to query in Google Trends
5. **Engage other agents** — Initiate debates, request peer review, casual discussion
6. **Abstain from engagement** — Choose not to respond if they have nothing to add

### 2.4 Agent Interaction Modes

| Mode | Description |
|------|-------------|
| **Debate** | Structured disagreement on interpretation of signals |
| **Peer Review** | One agent reviews another's analysis for errors/blind spots |
| **Casual Chat** | Informal discussion, hypothesis generation, brainstorming |
| **Solo Analysis** | Independent deep-dive without collaboration |
| **Consensus Building** | Attempt to synthesize views into unified assessment |

### 2.5 Data Sources

#### Primary: Prediction Markets

| Source | API | Coverage |
|--------|-----|----------|
| **Polymarket** | `gamma-api.polymarket.com` | Political events, policy outcomes, elections |
| **Kalshi** | `api.elections.kalshi.com` | CFTC-regulated, US-focused, economic events |

**Key metrics extracted:**
- Current prices (probability estimates)
- Price velocity & acceleration
- Volume (conviction signal)
- Liquidity depth
- Bid-ask spread (uncertainty)
- 24h/1wk/1mo price changes

#### Secondary: Search Behavior

| Source | Access | Coverage |
|--------|--------|----------|
| **Google Trends** | PyTrends / API | Search interest over time, regional breakdown, related queries |

**Key metrics extracted:**
- Relative search volume (0-100 index)
- Geographic distribution (state-level)
- Temporal patterns (when do people search)
- Related queries (what else are they curious about)
- Rising vs. top queries (emerging vs. established interests)

### 2.6 Transparency & Reasoning

All agent reasoning is logged and made transparent:

```
┌─────────────────────────────────────────────────────────────┐
│ [2026-02-04 14:32:17] PolAgent-A                            │
│ SIGNAL: Polymarket "Trump approval Q2 2026" moved +3.2%     │
│ CONTEXT: Searched news → Found: deportation numbers released│
│ REASONING: Market responding to ICE report showing 450k     │
│            deportations in Jan, exceeding expectations.     │
│ CONFIDENCE: 0.78                                            │
│ ACTION: Flag for daily digest, request EconAgent-A review   │
│         on economic implications of labor supply change.    │
└─────────────────────────────────────────────────────────────┘
```

---

## Part 3: Signal Detection Framework

### 3.1 Attitude Shift Indicators

Based on our earlier analysis, the system monitors:

#### Price-Based Signals
| Signal | Detection | Interpretation |
|--------|-----------|----------------|
| Conviction Flip | Price crosses 50% with high volume | Majority belief reversed |
| Momentum Shift | 3+ days same direction, acceleration increasing | Trend forming |
| Velocity Spike | >2σ daily price change | Rapid belief updating |

#### Volume-Based Signals
| Signal | Detection | Interpretation |
|--------|-----------|----------------|
| Volume Surge | Volume/liquidity ratio >3σ | Unusual activity |
| Volume Without Movement | High volume, stable price | Disagreement, uncertainty |
| Smart Money | Volume spike precedes price move | Informed traders active |

#### Market Health Signals
| Signal | Detection | Interpretation |
|--------|-----------|----------------|
| Spread Blowout | Spread doubles in <24h | Extreme uncertainty |
| Liquidity Drain | Liquidity drops >20% | Market makers retreating |
| Coherence Break | Correlated markets diverge >10% | Belief fragmentation |

### 3.2 Cross-Source Validation

Agents cross-reference signals across sources:

```
If Polymarket shows rising probability for X
AND Google Trends shows rising searches for X
AND Kalshi confirms with similar movement
→ High-confidence signal

If sources diverge:
→ Flag for debate between agents
→ Investigate cause of divergence
```

### 3.3 Composite Metrics

**Attitude Shift Score (ASS):**
```
ASS = (
    0.30 × normalized_price_velocity +
    0.25 × volume_surge_ratio +
    0.20 × cross_market_divergence +
    0.15 × spread_change +
    0.10 × search_trend_correlation
)
```

**Cascade Probability:**
- Track how often movement in market A predicts movement in related markets B, C, D
- High cascade = fluid attitudes, domino effects
- Low cascade = isolated event

---

## Part 4: Research Focus

### 4.1 Primary Research Questions

1. **Can prediction market data serve as a valid continuous poll of public opinion?**
   - How do market movements correlate with subsequent poll shifts?
   - What is the lead time (if any) of markets over polls?

2. **What patterns in market data indicate genuine attitude change vs. noise?**
   - Volume, velocity, cross-market coherence as quality signals
   - Distinguishing information shocks from market manipulation

3. **How can multi-agent debate improve interpretation accuracy?**
   - Does adversarial review catch errors?
   - Do heterogeneous perspectives reduce blind spots?

4. **Can this methodology predict 2026 midterm outcomes?**
   - Benchmark against traditional polling aggregators
   - Post-hoc accuracy assessment

### 4.2 Target Outcomes (2026 Midterms)

| Outcome | Data Sources | Agents |
|---------|--------------|--------|
| Senate control | Polymarket, Kalshi | PolAgent-A/B |
| House control | Polymarket, Kalshi | PolAgent-A/B |
| Trump approval trajectory | Polymarket, Google Trends | All |
| Key policy sentiment (immigration, economy) | All sources | All |
| Swing state dynamics | Regional Google Trends | PolAgent-A/B |

### 4.3 Academic Publication Strategy

**Target venues:**
- *Political Analysis* (Cambridge)
- *Public Opinion Quarterly*
- *Journal of Politics*
- *American Political Science Review* (ambitious)
- *PNAS* (if findings are significant)
- Conference: APSA, MPSA, PolMeth

**Paper structure:**
1. Literature review: prediction markets, collective intelligence, AI agents in research
2. Methodology: agent architecture, data sources, signal detection
3. Validation: comparison with traditional polls, accuracy metrics
4. Results: 2026 midterm tracking and predictions
5. Discussion: implications for polling methodology

---

## Part 5: Technical Implementation

### 5.1 MVP Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND                                  │
│              (Kalshi-inspired dashboard)                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐                │
│  │ Markets │ │ Agents  │ │ Debates │ │ Reports │                │
│  │  View   │ │  Feed   │ │   Log   │ │  (PDF)  │                │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    AGENT ORCHESTRATOR                     │   │
│  │  ┌────────────┐  ┌────────────┐                          │   │
│  │  │ PolAgent-A │◄─┤ PolAgent-B │  (Debate/Review)         │   │
│  │  └────────────┘  └────────────┘                          │   │
│  │         │                │                                │   │
│  │         └───────┬────────┘                                │   │
│  │                 │                                         │   │
│  │  ┌────────────┐ │ ┌────────────┐                          │   │
│  │  │EconAgent-A │◄┴─┤EconAgent-B │  (Debate/Review)         │   │
│  │  └────────────┘   └────────────┘                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                   │
│  ┌───────────────────────────┴───────────────────────────────┐  │
│  │                     DATA LAYER                             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │  │
│  │  │Polymarket│  │  Kalshi  │  │  Google  │  │   News   │   │  │
│  │  │   API    │  │   API    │  │  Trends  │  │   APIs   │   │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│  ┌───────────────────────────┴───────────────────────────────┐  │
│  │                   STORAGE (SQLite/Postgres)                │  │
│  │  • Market snapshots (5-min intervals)                      │  │
│  │  • Agent reasoning logs                                    │  │
│  │  • Debate transcripts                                      │  │
│  │  • Generated reports                                       │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Technology Stack (Proposed)

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Agent Framework | LangGraph / CrewAI | Multi-agent orchestration |
| LLM Backend | Claude API / GPT-4 | Reasoning, debate, analysis |
| Database | PostgreSQL + TimescaleDB | Time-series market data |
| Frontend | Next.js + Tailwind | Kalshi-inspired UI |
| API Layer | FastAPI | Python ecosystem, async |
| Scheduling | APScheduler / Celery | Data collection, agent runs |

### 5.3 MVP Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| **Phase 1: Data Pipeline** | 2 weeks | Polymarket + Kalshi + Trends collection |
| **Phase 2: Single Agent** | 2 weeks | One working analyst agent |
| **Phase 3: Multi-Agent** | 3 weeks | Four agents with debate capability |
| **Phase 4: Frontend** | 2 weeks | Basic dashboard |
| **Phase 5: Validation** | Ongoing | Compare to polls, refine |

---

## Part 6: Appendix

### 6.1 Polymarket API Reference

**Base URL:** `https://gamma-api.polymarket.com`

**Key Endpoints:**
- `GET /markets` — List markets with filters
- `GET /markets?slug={slug}` — Specific market by slug
- `GET /events` — Event groupings

**Key Fields:**
```json
{
  "question": "Market question",
  "outcomePrices": "[\"0.65\", \"0.35\"]",
  "volume": "1234567.89",
  "volume24hr": "12345.67",
  "liquidity": "50000.00",
  "bestBid": 0.64,
  "bestAsk": 0.66,
  "oneDayPriceChange": 0.02,
  "oneWeekPriceChange": -0.05
}
```

### 6.2 Sample Market Data (Feb 4, 2026)

| Market | Yes Price | 24h Volume | Interpretation |
|--------|-----------|------------|----------------|
| Trump nominates Warsh as Fed Chair | 97% | $1.67M | Near-certain |
| Fed rate cut March 2026 | 2% | $2.0M | Unlikely |
| Trump deportations >1M in 2025 | 68% | $110K | Lean yes |

### 6.3 Google Trends Keywords (Initial Set)

**Political:**
- "Trump approval"
- "2026 midterm elections"
- "Republican congress"
- "Democrat senate"
- "immigration policy"

**Economic:**
- "inflation 2026"
- "interest rates"
- "federal reserve"
- "tariffs"
- "job market"

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-02-04 | Initial specification |

---

*VibePolitics — Polling the vibe, not just the vote.*
