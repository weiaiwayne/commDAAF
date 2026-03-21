# Kimi K2.5 Independent Study Plan — VibePoll-2026

**Agent:** Kimi K2.5 (OpenCode)  
**Study:** Vibe Polling - Google Trends Public Opinion Analysis  
**Framework:** CommDAAF v1.0  
**Validation Tier:** 🟢 EXPLORATORY  
**Date:** 2026-03-19  
**Status:** INDEPENDENT ANALYSIS (not coordinating with other agents)

---

## Study Overview

### Research Questions
- **RQ1:** Can Google Trends search volume predict/correlate with prediction market movements?
- **RQ2:** Which issue categories show strongest Trends-to-sentiment correlation?
- **RQ3:** Do Trends signals lead, lag, or move synchronously with prediction markets?
- **RQ4:** State-level variations in issue salience?

### Battleground States (7 Core + 3 Control)
**Tier 1 Battlegrounds:** Pennsylvania, Michigan, Wisconsin, Arizona, Georgia  
**Tier 2 Battlegrounds:** Nevada, North Carolina  
**Control States:** California (Safe D), Texas (Safe R), Ohio (Lean R)

### Issue Categories & Search Terms
1. **Economy:** gas prices, grocery prices, rent, inflation, recession, unemployment
2. **Immigration:** ICE raid, deportation, immigration lawyer, border wall
3. **Iran War:** Iran war, US troops Iran, military draft, World War 3
4. **AI/Jobs:** AI taking jobs, ChatGPT, AI layoffs, automation
5. **Political:** how to vote, voter registration, Trump approval

---

## Execution Phases

### Phase 1: Data Collection (Day 1-2)
**Goal:** Collect all required data independently

| Task | Script | Output |
|------|--------|--------|
| Google Trends | `scripts/collect_trends.py` | `data/raw/trends/` |
| Prediction Markets | `scripts/collect_markets.py` | `data/raw/markets/` |
| Polling Data | `scripts/collect_polls.py` | `data/raw/polls/` |

**CommDAAF Requirements:**
- ✅ Verify API access before collection
- ✅ Implement rate limiting (2-5 sec delays)
- ✅ Log all collection decisions
- ✅ Validate search terms for realism

### Phase 2: Data Processing & Diagnostics (Day 2)
**Goal:** Clean data and run mandatory distribution diagnostics

| Task | Script | Output |
|------|--------|--------|
| Data cleaning | `scripts/process_data.py` | `data/processed/` |
| Distribution diagnostics | `scripts/diagnostics.py` | `analysis/descriptives/` |
| Data verification report | Manual | `data_verification.md` |

**CommDAAF Requirements:**
- ✅ MANDATORY diagnostics for ALL numeric variables
- ✅ Report: N, Mean, Median, SD, Skewness, % Zeros, Var/Mean ratio
- ✅ Flag: |skew| > 1, zeros > 15%, var/mean > 1.5
- ✅ Model recommendation based on diagnostics

### Phase 3: Statistical Modeling (Day 3)
**Goal:** Run appropriate statistical models

| Task | Method | Output |
|------|--------|--------|
| Model selection | Decision tree | `model_selection.md` |
| Regression analysis | Negative Binomial or OLS | `regression_results.json` |
| Effect size interpretation | IRR / Cohen's d | `effect_interpretations.md` |

**CommDAAF Requirements:**
- ✅ Model selection based on diagnostics (NOT default to OLS)
- ✅ Effect sizes with 95% CIs
- ✅ Multiple comparison correction if needed
- ✅ NEVER use OLS on skewed count data

### Phase 4: Validation & Synthesis (Day 4)
**Goal:** Validate against polls and prepare synthesis

| Task | Method | Output |
|------|--------|--------|
| Validation analysis | Correlation, lag analysis | `validation_results.md` |
| Synthesis handoff | Structured JSON | `synthesis_handoff.json` |

**CommDAAF Requirements:**
- ✅ Cross-validation against traditional polls
- ✅ Document limitations
- ✅ Honest confidence level assessment

---

## Directory Structure

```
agents/kimi-k2.5/
├── CONVERSATION_LOG.md          # Session documentation
├── STUDY_PLAN.md               # This file
├── data_verification.md        # Data integrity report
├── diagnostics_report.md       # Distribution diagnostics
├── model_selection.md          # Model choice rationale
├── regression_table.md         # Statistical results
├── effect_interpretations.md   # Practical significance
├── validation_results.md       # Poll validation
└── synthesis_handoff.json      # Structured summary

data/
├── raw/
│   ├── trends/                 # Google Trends data
│   ├── markets/                # Prediction market data
│   └── polls/                  # Polling data
├── processed/                  # Cleaned/normalized data
└── reference/                  # State codes, term categories

scripts/
├── collect_trends.py           # Google Trends collection
├── collect_markets.py          # Polymarket/Kalshi collection
├── collect_polls.py            # Polling aggregator scraping
├── process_data.py             # Data cleaning
├── diagnostics.py              # Distribution diagnostics
└── analyze.py                  # Statistical analysis

analysis/
├── descriptives/               # Distribution diagnostics
├── correlations/               # Correlation matrices
└── models/                     # Regression results

outputs/
├── figures/                    # Visualizations
└── tables/                     # Summary tables
```

---

## CommDAAF Compliance Checklist

Before each phase, verify:

- [ ] CommDAAF skill read and activated
- [ ] Validation tier declared (🟢 EXPLORATORY)
- [ ] Three mandatory questions answered (Q1, Q2, Q3)
- [ ] Distribution diagnostics planned BEFORE regression
- [ ] Effect sizes will be reported (not just p-values)
- [ ] Limitations will be documented

---

## Timeline

| Day | Phase | Key Deliverables |
|-----|-------|------------------|
| 1 | Collection | Raw data for all sources |
| 2 | Processing | Cleaned data + diagnostics |
| 3 | Modeling | Regression results + effect sizes |
| 4 | Validation | Validation report + synthesis |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Context overflow (262K limit) | Split large tasks into 25-item batches |
| API rate limits | 2-5 second delays between requests |
| Data quality issues | Verify with spot checks; document all decisions |
| Model selection error | Follow CommDAAF decision tree strictly |

---

*Plan created by Kimi K2.5 for independent VibePoll-2026 analysis.*
