# Tiered Validation System

> **"Validation should match your stakes, not a one-size-fits-all bar."**

---

## The Three Tiers

| Tier | Time | Effort | Use Case |
|------|------|--------|----------|
| **🟢 Exploratory** | 30-60 min | Light | Hypothesis generation, learning methods |
| **🟡 Pilot** | 2-4 hours | Moderate | Preliminary findings, committee review |
| **🔴 Publication** | 1-2 days | Intensive | Journal submission, public claims |

---

## Tier Selection Guide

### Choose 🟢 Exploratory When:
- Learning a new method
- Initial data exploration
- Generating hypotheses
- Quick sanity check
- **Not** planning to publish

### Choose 🟡 Pilot When:
- Preliminary findings for advisor
- Internal presentation
- Grant proposal preliminary data
- Deciding whether to pursue full study
- Conference poster (early stage)

### Choose 🔴 Publication When:
- Journal article submission
- Dissertation chapter
- Policy recommendations
- High-stakes claims
- Generalizable findings

---

## 🟢 Tier 1: Exploratory (30-60 min)

### Goal
Quick sanity check that you're not producing nonsense.

### Required Checks

#### Data Quality (10 min)
- [ ] Data loaded correctly (expected shape)
- [ ] No obvious duplicates
- [ ] Date ranges reasonable
- [ ] Missing data pattern noted

#### Method Sanity (15 min)
- [ ] Output looks reasonable (not all NaN)
- [ ] Sample of results interpretable
- [ ] No obvious execution errors

#### Quick Robustness (15 min)
- [ ] Results stable to ±20% parameter changes
- [ ] Direction of effects consistent

#### Limitation Note (10 min)
Write 2-3 sentences acknowledging this is exploratory.

### Outcome
- ✅ Proceed to interpretation with **heavy caveats**
- ✅ Present as "preliminary exploration"
- ❌ **Do not publish**

---

## 🟡 Tier 2: Pilot (2-4 hours)

### Goal
Core validation that findings are likely real and defensible.

### Required Checks

#### Data Quality (30 min)
- [ ] Coverage analysis (what's missing and why)
- [ ] Bias assessment (over/under-represented groups)
- [ ] Temporal patterns (collection artifacts)
- [ ] Basic bot/spam detection
- [ ] Missing data strategy documented

#### Method Validation (1 hour)

**For Topic Modeling:**
- [ ] Coherence score > 0.4
- [ ] Stability check (3 runs) > 70%
- [ ] Sample validation (20 documents)

**For Network Analysis:**
- [ ] Bot check (< 20% flagged)
- [ ] Basic structure validation
- [ ] Top 5 nodes manually verified

**For Sentiment/Classification:**
- [ ] Human validation sample (N ≥ 100)
- [ ] Agreement κ ≥ 0.6

#### Robustness (1 hour)
- [ ] Subsample replication (80% samples)
- [ ] Alternative specification test
- [ ] Key findings directionally stable

#### Alternative Explanations (30 min)
Write 1 paragraph addressing:
1. Alternative explanation #1
2. Alternative explanation #2
3. How you address or acknowledge them

### Outcome
- ✅ Proceed to interpretation with **moderate caveats**
- ✅ Present to committee as "preliminary findings"
- ✅ Publish in working papers with caveats
- ❌ **Do not submit to top journals without upgrading**

---

## 🔴 Tier 3: Publication (1-2 days)

### Goal
Full validation that findings are robust, defensible, and reproducible.

### Required Checks

#### Data Quality (2-4 hours)
- [ ] Complete coverage analysis with visualization
- [ ] Bias assessment with statistical tests
- [ ] Temporal pattern diagnostics
- [ ] Bot detection with multiple methods
- [ ] Coordinated behavior check
- [ ] Missing data imputation validated
- [ ] Data provenance fully documented

#### Method Validation (4-6 hours)

**For Topic Modeling:**
- [ ] Exhaustive K optimization (5-50, step 2)
- [ ] Stability check (5 runs) ≥ 80%
- [ ] Human interpretability validation (50 docs)
- [ ] Human coding validation (N ≥ 200, κ ≥ 0.67)

**For Network Analysis:**
- [ ] Bot detection < 15%
- [ ] All top 10 nodes manually verified
- [ ] Community detection stability ≥ 80%
- [ ] Modularity > 0.3

**For Sentiment/Classification:**
- [ ] Human validation (N ≥ 200)
- [ ] Agreement κ ≥ 0.7
- [ ] Multi-model comparison
- [ ] Error analysis on disagreements

#### Comprehensive Robustness (3-4 hours)
- [ ] Bootstrap confidence intervals (1000 samples)
- [ ] Multiple subsample replications (90%, 80%, 70%)
- [ ] Parameter sweep across reasonable range
- [ ] Outlier influence analysis
- [ ] Alternative operationalizations
- [ ] Bot-filtered sensitivity analysis

#### Replication Package (2 hours)
- [ ] Complete analysis scripts
- [ ] Requirements with versions
- [ ] Random seeds documented
- [ ] README with step-by-step instructions
- [ ] Expected output documented

### Outcome
- ✅ Proceed to interpretation with **confidence**
- ✅ Submit to journals
- ✅ Make policy recommendations (with uncertainty)

---

## Validation Comparison Matrix

| Check | 🟢 Exploratory | 🟡 Pilot | 🔴 Publication |
|-------|----------------|----------|----------------|
| Data quality | Basic (10 min) | Comprehensive (30 min) | Exhaustive (2-4 hrs) |
| Bot detection | None | Basic heuristics | Multiple methods |
| Stability runs | None | 3 runs, 70% | 5+ runs, 80% |
| Human validation | None | N=20-50 | N=50-200 |
| Robustness | Parameter check | Subsample + alt specs | Bootstrap + exhaustive |
| Replication package | No | Partial | Full |

---

## Escalation Path

You can **upgrade** validation as research progresses:

```
🟢 Exploratory → 🟡 Pilot → 🔴 Publication
     (30 min)      (+4 hrs)     (+2 days)
```

**You don't start over** — each tier builds on the previous.

---

## Time Estimates by Method

| Method | 🟢 Exploratory | 🟡 Pilot | 🔴 Publication |
|--------|----------------|----------|----------------|
| Topic Modeling | 45 min | 3 hrs | 8 hrs |
| Network Analysis | 30 min | 2 hrs | 6 hrs |
| Sentiment Analysis | 30 min | 2 hrs | 5 hrs |
| Content Analysis | 1 hr | 4 hrs | 12 hrs |
| LLM Annotation | 30 min | 2 hrs | 6 hrs |

---

## Declaring Your Tier

At the start of any analysis, CommDAAF asks:

```
What's your validation tier for this analysis?

1. 🟢 EXPLORATORY (30-60 min)
   → Learning, exploring, hypothesis generation
   
2. 🟡 PILOT (2-4 hours)
   → Preliminary findings, committee review
   
3. 🔴 PUBLICATION (1-2 days)
   → Journal submission, public claims

Your selection: ___
```

**This shapes all subsequent guidance** — exploratory gets lighter checks, publication gets comprehensive validation.

---

## Key Principle

> **"The goal is not to prevent all research without full validation. The goal is to match validation to stakes and be honest about limitations at each level."**

Exploratory work is valuable. Pilot findings are useful. But only publication-tier validation supports strong claims.

---

*Tiered Validation System | CommDAAF v0.3*
