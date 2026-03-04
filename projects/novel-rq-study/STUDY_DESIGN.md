# Novel Research Directions: #MahsaAmini Dataset
## AgentAcademy Autonomous Study

**Date:** 2026-03-04
**Tier:** 🟢 EXPLORATORY
**Agent:** Claude Opus 4.5 (autonomous RQ generation)

---

## Motivation

Previous CommDAAF study on #MahsaAmini found:
- INFORMATIONAL frame → IRR 2.72 (highest engagement)
- 3-model agreement confirmed findings

**What was NOT studied:**
1. Language dynamics (Persian vs English) — diaspora amplification
2. Temporal patterns — protest lifecycle effects
3. Coordination signals — organic vs amplified spread
4. Frame co-occurrence — how frames interact

---

## Literature Grounding (from Wayne's Zotero)

| Theme | Key Sources | Gap |
|-------|-------------|-----|
| **Networked publics** | boyd 2010; Gruzd "imagined community" | Language as public boundary |
| **Coordinated behavior** | Giglietto 2020; Kuznetsova 2025 (Russia/Belarus) | Not tested on protest data |
| **Attention economy** | Zotero collection "agentic attention" | Power-law distributions unexplored |
| **Alternative networking** | Mastodon papers; platform governance | Diaspora as alternative network |

---

## Novel Research Questions

### RQ1: Diaspora Amplification Dynamics
**"Does language choice (Persian vs English) moderate the relationship between content framing and engagement, and what does this reveal about diaspora amplification in transnational protest?"**

- **Theoretical basis:** Networked publics theory (boyd); imagined communities (Gruzd adaptation of Anderson)
- **Novel contribution:** Language as proxy for audience (domestic vs diaspora); tests if diaspora amplifies specific frames
- **Hypothesis:** 
  - H1a: English-language posts receive higher engagement (global reach)
  - H1b: Frame×Language interaction exists (diaspora amplifies SOLIDARITY/HOPE more than INJUSTICE)

### RQ2: Temporal Dynamics & Frame Competition
**"How do frame prevalence and effectiveness change across protest phases (onset → peak → sustained), and do frames compete or complement each other temporally?"**

- **Theoretical basis:** Issue-attention cycle (Downs 1972); protest event analysis
- **Novel contribution:** Dynamic framing effects; tests if "winning frames" shift over time
- **Hypothesis:**
  - H2a: SOLIDARITY dominant in early phase; INFORMATIONAL rises in sustained phase
  - H2b: Frame effectiveness varies by phase (what works early may not work later)

### RQ3: Engagement Concentration & Power Laws
**"Does engagement follow power-law distributions, and do different frames exhibit different concentration patterns (viral spikes vs steady diffusion)?"**

- **Theoretical basis:** Attention economy; preferential attachment; Barabási network effects
- **Novel contribution:** Structural analysis of virality; distinguishes "lottery" frames from "reliable" frames
- **Hypothesis:**
  - H3a: Overall engagement follows power-law (heavy tail)
  - H3b: INFORMATIONAL shows flatter distribution (steady); SOLIDARITY shows steeper (viral lottery)

### RQ4: Coordination Signals in Protest Amplification
**"Are there detectable temporal clustering patterns suggesting coordinated amplification, and which frames show strongest coordination signals?"**

- **Theoretical basis:** Coordinated behavior detection (Giglietto); inauthentic amplification
- **Novel contribution:** First coordination analysis on #MahsaAmini; tests organic vs manufactured virality
- **Hypothesis:**
  - H4a: Some frames show suspicious temporal clustering (>4:1 peak/trough ratio)
  - H4b: CALL_TO_ACTION most likely coordinated; INFORMATIONAL most organic

---

## Operationalizations

### Language Classification
- `en` → Diaspora/global audience
- `fa` (Farsi/Persian) → Domestic/regional audience
- `und`, `ar`, `ru`, `uk` → Exclude or separate analysis

### Temporal Phases
- **Phase 1 (Onset):** Sept 16-22, 2022 (Mahsa Amini death + immediate protest)
- **Phase 2 (Peak):** Sept 23 - Oct 3, 2022 (global attention peak)
- Note: Dataset starts June 16, includes pre-protest baseline

### Coordination Signals
- Temporal clustering: Posts within 60-second windows
- Engagement anomalies: Unusually rapid engagement accumulation
- Account patterns: Same engagement tier, similar followers

### Power-Law Analysis
- Fit Pareto distribution to engagement
- Calculate Gini coefficient per frame
- Compare α exponents across frames

---

## Analysis Plan

1. **Data preparation:** Merge existing codings with raw data; create language and temporal variables
2. **RQ1 analysis:** Two-way ANOVA or NB regression with Frame×Language interaction
3. **RQ2 analysis:** Time-series of frame prevalence; phase-stratified regression
4. **RQ3 analysis:** Power-law fitting; Gini coefficients; Kolmogorov-Smirnov tests
5. **RQ4 analysis:** Temporal clustering detection; peak/trough ratios

---

## Multi-Model Validation Strategy

Each model independently analyzes:
1. Frame×Language engagement patterns
2. Temporal trends
3. Distribution shapes
4. Coordination signals

Cross-validate: Flag divergences >10% on key statistics

---

## Why These RQs Are Novel

| RQ | Previous Study | This Study |
|----|----------------|------------|
| RQ1 | Ignored language | Language as key moderator |
| RQ2 | Cross-sectional | Temporal dynamics |
| RQ3 | Mean engagement | Distribution shape |
| RQ4 | Assumed organic | Tests coordination |

**These questions test whether the "INFORMATIONAL wins" finding holds across languages, time periods, and after accounting for potential coordination.**

---

## Expected Contributions

1. **Theoretical:** Extend networked publics theory to multilingual protest contexts
2. **Methodological:** Demonstrate autonomous RQ generation by AI agents
3. **Empirical:** First analysis of language dynamics in #MahsaAmini
4. **Practical:** Identify which frames diaspora activists should prioritize

---

*Study design generated autonomously by Claude Opus 4.5, grounded in Wayne Xu's Zotero library*
