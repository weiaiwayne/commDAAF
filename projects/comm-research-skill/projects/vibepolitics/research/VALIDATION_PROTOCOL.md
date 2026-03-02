# VibePolitics Validation Protocol
## Experimental Studies Before MVP Development

**Version:** 1.0  
**Date:** February 5, 2026  
**Purpose:** Address peer review critiques through systematic empirical validation

---

## 1. Validation Philosophy

### 1.1 Core Principle

Before claiming the system detects "public opinion shifts," we must demonstrate:

1. **Signal Validity:** Do our signals measure what we claim?
2. **Predictive Value:** Do signals precede observable opinion changes?
3. **Added Value:** Do signals provide information beyond existing methods?
4. **Robustness:** Do signals work across different contexts and time periods?

### 1.2 Publication-First Strategy

```
Phase 1: Retrospective Validation Studies (Months 1-4)
         ↓
Phase 2: Real-Time Pilot Studies (Months 5-8)
         ↓
Phase 3: Peer-Reviewed Publications (Months 9-12)
         ↓
Phase 4: MVP Development (Only after validation)
```

---

## 2. Ground Truth Definition

### 2.1 The Core Problem

"Opinion shift" is not directly observable. We need proxy measures that are:
- Independently measurable
- Temporally precise
- Plausibly connected to actual opinion change

### 2.2 Ground Truth Options

| Ground Truth | Source | Temporal Resolution | Validity |
|--------------|--------|---------------------|----------|
| **Polling Aggregates** | 538, RCP, Silver Bulletin | Daily | High (direct measure) |
| **Individual Polls** | YouGov, Emerson, etc. | 2-4 days | Medium (sampling noise) |
| **News Events** | Manual coding / NewsAPI | Hourly | Medium (proxy for stimuli) |
| **Social Media Volume** | Twitter/Reddit APIs | Hourly | Low (different population) |
| **Google Trends (external)** | Separate keywords | Daily | Medium (circular risk) |

### 2.3 Primary Ground Truth: Polling Movement

**Definition:** A "validated shift" occurs when:
```
|Poll_aggregate(t+7) - Poll_aggregate(t)| > 2 percentage points
```

**Sources:**
- FiveThirtyEight polling averages (historical data available)
- RealClearPolitics averages
- Silver Bulletin (Nate Silver's new site)

**Why 2 points?** 
- Typical polling margin of error is ±3 points
- Movement > 2 points is more likely signal than noise
- Sensitivity analysis will test 1, 2, 3 point thresholds

### 2.4 Secondary Ground Truth: Major News Events

**Definition:** Events coded by political scientists as "potentially opinion-moving"

**Categories:**
1. Debate performances
2. Major endorsements
3. Scandal revelations
4. Policy announcements
5. Legal developments (indictments, rulings)
6. External shocks (economic data, international events)

**Source:** Retrospective coding from news archives (AP, Reuters, NYT)

---

## 3. Experimental Study 1: Retrospective 2024 Validation

### 3.1 Objective

Test whether VibePolitics signals would have detected known opinion shifts during the 2024 US Presidential election.

### 3.2 Data Collection

**Time Period:** January 1, 2024 – November 5, 2024 (election day)

**Polymarket Data:**
- Historical market data from Polymarket API (if available)
- Alternative: Wayback Machine snapshots of polymarket.com
- Alternative: Academic datasets (Prediction Market Archive)

**Google Trends Data:**
- pytrends historical queries for:
  - "Biden", "Trump", "Harris", "election"
  - Issue keywords: "immigration", "economy", "abortion"
- Daily resolution, US national + swing states

**Polling Data:**
- FiveThirtyEight historical polling averages
- Individual poll results from 538 database

### 3.3 Known Events to Validate Against

| Date | Event | Expected Signal | Polling Impact |
|------|-------|-----------------|----------------|
| June 27, 2024 | Biden-Trump Debate | High VSR, SVS | Biden -3 to -5 pts |
| July 21, 2024 | Biden withdraws | Extreme all signals | Reset baseline |
| July 22, 2024 | Harris announced | High VSR, PVI | Harris +5 pts initial |
| Aug 19-22, 2024 | DNC Convention | High SVS, VSR | Harris +2-3 pts (typical bounce) |
| Sept 10, 2024 | Harris-Trump Debate | High VSR, SVS | Harris +1-2 pts |
| Oct 2024 | October surprises (various) | Variable | To be measured |

### 3.4 Analysis Plan

**Step 1: Compute All Signals**
```python
for each day in study_period:
    compute SDI, VSR, PVI for all political markets
    compute SVS, RDS for all tracked keywords
    compute MSD for market-search pairs
```

**Step 2: Identify Signal Exceedances**
```python
for each signal:
    exceedances = days where signal > threshold
    # Test multiple thresholds: 1.5, 2, 2.5, 3 SD
```

**Step 3: Correlate with Ground Truth**
```python
for each polling shift > 2 points:
    check if any signal exceeded threshold in [-7, 0] day window
    compute lead time (days before shift became apparent in polls)
```

**Step 4: Compute Validation Metrics**
- **Precision:** Of signals fired, what % preceded real shifts?
- **Recall:** Of real shifts, what % were preceded by signals?
- **Lead Time:** How many days before polling showed shift?
- **False Positive Rate:** Signals with no subsequent shift

### 3.5 Deliverable

**Paper 1:** "Retrospective Validation of Prediction Market Signals for Detecting Opinion Shifts: Evidence from the 2024 US Presidential Election"

**Target Venue:** *Political Analysis* or *Journal of Politics*

---

## 4. Experimental Study 2: Threshold Calibration

### 4.1 Objective

Empirically determine optimal signal thresholds rather than using arbitrary values.

### 4.2 Method: ROC Curve Analysis

For each signal (SDI, VSR, PVI, SVS, RDS, MSD):

```python
thresholds = np.arange(0.5, 5.0, 0.1)  # Test range of thresholds
for threshold in thresholds:
    true_positives = signals_before_real_shifts(threshold)
    false_positives = signals_without_shifts(threshold)
    
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    
# Plot ROC curve
# Select threshold maximizing F1 score or user-specified precision/recall tradeoff
```

### 4.3 Cross-Validation

- **Training set:** 2020-2023 election cycles
- **Test set:** 2024 election cycle
- Prevents overfitting to specific events

### 4.4 Deliverable

**Paper 2:** "Calibrating Prediction Market Signals: Optimal Thresholds for Political Opinion Shift Detection"

**Target Venue:** *Political Analysis* (methods focus) or *EPJ Data Science*

---

## 5. Experimental Study 3: Representativeness Analysis

### 5.1 Objective

Address the core critique: Do prediction market movements actually reflect public opinion?

### 5.2 Method: Granger Causality Tests

Test whether Polymarket price changes **precede** polling changes:

```python
# Granger causality test
from statsmodels.tsa.stattools import grangercausalitytests

# H0: Polymarket does not Granger-cause polling
# H1: Polymarket Granger-causes polling

results = grangercausalitytests(
    data[['polymarket_price', 'polling_average']], 
    maxlag=7  # Test up to 7 days lag
)
```

### 5.3 Comparison with Polling Aggregates

| Metric | Polymarket | Polling Average | Interpretation |
|--------|------------|-----------------|----------------|
| Correlation with outcome | ? | ? | Which is more accurate? |
| Lead time to shifts | ? | ? | Which detects shifts earlier? |
| Volatility | ? | ? | Which is noisier? |

### 5.4 Demographic Analysis (If Data Available)

If Polymarket releases trader demographics or we can infer from on-chain data:
- Compare trader population to voter population
- Weight signals by demographic representativeness
- Test whether weighted signals improve validity

### 5.5 Deliverable

**Paper 3:** "Do Prediction Markets Reflect Public Opinion? Evidence from the 2024 Election"

**Target Venue:** *Public Opinion Quarterly* or *Political Behavior*

---

## 6. Experimental Study 4: Real-Time Pilot (2026 Midterms)

### 6.1 Objective

Test the system prospectively with pre-registered predictions.

### 6.2 Pre-Registration

Before data collection begins, publicly register:
- Exact signal definitions (code)
- Exact thresholds (from Study 2)
- Exact ground truth definition
- Exact validation metrics
- Analysis plan

**Platform:** OSF (Open Science Framework) or AsPredicted

### 6.3 Timeline

| Phase | Dates | Activity |
|-------|-------|----------|
| Setup | March 2026 | Deploy data collection infrastructure |
| Baseline | April 2026 | Collect 4 weeks baseline, verify thresholds |
| Primary Season | May-Aug 2026 | Monitor primary elections |
| General Election | Sept-Nov 2026 | Monitor midterm campaigns |
| Analysis | Dec 2026-Jan 2027 | Validate against outcomes |

### 6.4 Monitoring Protocol

```
Daily:
- Collect Polymarket data (all political markets)
- Collect Google Trends data (tracked keywords)
- Compute all 6 signals
- Log any threshold exceedances

When signal fires:
- Record timestamp, signal values, market context
- DO NOT adjust thresholds mid-study
- Document in real-time log

Post-election:
- Compare signals to polling shifts and outcomes
- Compute validation metrics
- Report regardless of results (publication bias prevention)
```

### 6.5 Deliverable

**Paper 4:** "Real-Time Detection of Political Opinion Shifts: A Pre-Registered Validation Study of the 2026 US Midterm Elections"

**Target Venue:** *Science* (if results strong), *PNAS*, or *Political Analysis*

---

## 7. Agent System Validation

### 7.1 Objective

Test whether the 2-agent interpretation system adds value beyond raw signals.

### 7.2 Experimental Design

**Condition 1: Signals Only**
- Alert when any signal > threshold
- No AI interpretation

**Condition 2: Single Agent**
- One LLM interprets all signals
- Outputs recommendation

**Condition 3: Two Agents (Alpha/Beta)**
- Full VibePolitics system
- Disagreement as uncertainty signal

### 7.3 Evaluation Metrics

- **Accuracy:** Which condition better predicts shifts?
- **Calibration:** Which condition's confidence matches actual accuracy?
- **Interpretability:** Which provides more useful explanations?

### 7.4 Deliverable

**Paper 5:** "Multi-Agent AI for Political Signal Interpretation: Does Adversarial Debate Improve Detection?"

**Target Venue:** *AAAI*, *NeurIPS*, or *Computational Social Science*

---

## 8. Addressing Peer Review Critiques

### 8.1 Mapping Critiques to Studies

| Critique | Addressed By |
|----------|--------------|
| Arbitrary thresholds | Study 2 (Calibration) |
| No validation framework | Studies 1, 3, 4 |
| Signals not novel | Reframe as "novel application" |
| Representativeness problem | Study 3 |
| Agent system unfalsifiable | Study 5 |
| Circular validation | Use external polling as ground truth |
| No baseline comparison | All studies include null/random baselines |

### 8.2 Revised Novelty Claims

After validation, we can legitimately claim:

1. **First empirically-validated combination** of prediction market + search signals for political shift detection
2. **Calibrated thresholds** derived from historical data, not intuition
3. **Demonstrated lead time** over traditional polling (if validated)
4. **Transparent methodology** with pre-registered validation

---

## 9. Data Requirements & Feasibility

### 9.1 Polymarket Historical Data

**Status:** Need to investigate availability

**Options:**
1. Direct API (may have historical endpoints)
2. Academic data sharing request
3. Blockchain data (on-chain transactions)
4. Wayback Machine / web archives

**Action:** Contact Polymarket for research data access

### 9.2 Google Trends Data

**Status:** Available via pytrends

**Limitations:**
- Rate limited
- Historical data may shift (resampling)
- Need consistent collection protocol

**Action:** Set up dedicated collection infrastructure

### 9.3 Polling Data

**Status:** Freely available

**Sources:**
- FiveThirtyEight GitHub (historical)
- RealClearPolitics (scraping required)
- Wikipedia election pages (aggregated)

---

## 10. Publication Timeline

| Paper | Draft | Submission | Target Venue |
|-------|-------|------------|--------------|
| Paper 1: Retrospective 2024 | Month 4 | Month 5 | Political Analysis |
| Paper 2: Threshold Calibration | Month 5 | Month 6 | EPJ Data Science |
| Paper 3: Representativeness | Month 6 | Month 7 | POQ |
| Paper 4: 2026 Pre-Registered | Month 15 | Month 16 | Science/PNAS |
| Paper 5: Agent Validation | Month 8 | Month 9 | NeurIPS |

---

## 11. Success Criteria

### 11.1 Minimum Viable Validation

The methodology is validated if:
- Precision > 50% (more true positives than false)
- Recall > 30% (catches at least 1/3 of real shifts)
- Lead time > 2 days (earlier than polling consensus)
- Granger causality test p < 0.05

### 11.2 Strong Validation

The methodology is strongly validated if:
- Precision > 70%
- Recall > 50%
- Lead time > 5 days
- Results replicate in 2026 prospective study

### 11.3 Failure Criteria

The methodology fails if:
- Precision < 30% (mostly false positives)
- No significant Granger causality
- No lead time advantage over polling
- Results don't replicate prospectively

**Commitment:** We will publish results regardless of outcome (preventing publication bias).

---

## 12. Resource Requirements

### 12.1 Compute & Infrastructure

- Cloud server for data collection ($50-100/month)
- Database for signal storage (PostgreSQL)
- LLM API costs for agent system (~$100/month)

### 12.2 Data Costs

- Polymarket: Free (API) or academic request
- Google Trends: Free (rate-limited)
- Polling data: Free (public sources)

### 12.3 Time Investment

- Study 1 (Retrospective): 2-3 months
- Study 2 (Calibration): 1-2 months (parallel with Study 1)
- Study 3 (Representativeness): 1-2 months
- Study 4 (2026 Pilot): 9-12 months
- Study 5 (Agent Validation): 2-3 months

---

## Appendix A: Pre-Registration Template

```yaml
title: "VibePolitics Signal Validation Study"
date_registered: [DATE]
authors: [AUTHORS]

hypotheses:
  H1: "SDI > [threshold] precedes polling shifts > 2 points within 7 days"
  H2: "VSR > [threshold] precedes polling shifts > 2 points within 7 days"
  H3: "Combined signal exceedance improves precision over individual signals"
  H4: "Polymarket prices Granger-cause polling averages"

methods:
  data_sources:
    - polymarket_api
    - pytrends
    - fivethirtyeight_polling
  
  time_period: "[START] to [END]"
  
  signal_thresholds:
    SDI: [value]
    VSR: [value]
    PVI: [value]
    SVS: [value]
    RDS: [value]
    MSD: [value]
  
  ground_truth: "Polling aggregate shift > 2 points within 7 days"
  
  metrics:
    - precision
    - recall
    - f1_score
    - lead_time_days
    - granger_causality_pvalue

analysis_plan:
  - "Compute signals for entire study period"
  - "Identify all threshold exceedances"
  - "Match exceedances to subsequent polling shifts"
  - "Compute validation metrics"
  - "Run Granger causality tests"
  - "Report all results regardless of significance"

commitment: "Results will be published regardless of whether hypotheses are supported."
```

---

*Validation Protocol for VibePolitics Methodology*  
*February 2026*
