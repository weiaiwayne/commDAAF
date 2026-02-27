# Tiered Validation System

Match validation to your stakes.

## The Three Tiers

| Tier | Time | Use Case |
|------|------|----------|
| **🟢 Exploratory** | 30-60 min | Hypothesis generation, learning |
| **🟡 Pilot** | 2-4 hours | Committee presentation, working paper |
| **🔴 Publication** | 1-2 days | Journal submission, dissertation |

---

## 🟢 Exploratory (30-60 min)

**Goal**: Quick sanity check

**Checks**:
- [ ] Data loaded correctly
- [ ] Output looks reasonable
- [ ] Results stable to ±20% parameter changes
- [ ] 2-3 sentence limitation note

**Outcome**: Proceed with heavy caveats. Do not publish.

---

## 🟡 Pilot (2-4 hours)

**Goal**: Core validation for defensible preliminary findings

**Checks**:
- [ ] Coverage and bias assessment
- [ ] Basic bot/spam detection
- [ ] Method validation:
  - Topic modeling: coherence > 0.4, stability > 70%
  - Network: bot < 20%, top 5 nodes verified
  - Sentiment: human sample N ≥ 100, κ ≥ 0.6
- [ ] Subsample replication (80%)
- [ ] Alternative explanations paragraph

**Outcome**: Present as preliminary. Publish with caveats.

---

## 🔴 Publication (1-2 days)

**Goal**: Full validation for robust, reproducible claims

**Checks**:
- [ ] Exhaustive data quality with visualization
- [ ] Multi-method bot detection (< 15%)
- [ ] Method validation (strict):
  - Topic modeling: 5 runs, stability ≥ 80%, N ≥ 50 human validation
  - Network: all top 10 nodes verified, community stability ≥ 80%
  - Sentiment: N ≥ 200, κ ≥ 0.7, multi-model comparison
- [ ] Bootstrap confidence intervals (1000 samples)
- [ ] Multiple robustness checks
- [ ] Replication package prepared

**Outcome**: Submit to journals. Make claims with confidence.

---

## Declare Your Tier (MANDATORY)

**Do not proceed without explicit tier declaration.**

At the start of EVERY analysis:

```
What's your validation tier?

1. 🟢 EXPLORATORY — Learning, exploring
2. 🟡 PILOT — Committee review, working paper
3. 🔴 PUBLICATION — Journal submission

Your selection: ___
```

This shapes all subsequent guidance. If user says "just analyze" without declaring tier, **ask again**.

---

## Single-Model vs Multi-Model Validation

### Understanding What CommDAAF Provides

| Mode | Quality Control Type | Catches | Misses |
|------|---------------------|---------|--------|
| **Single-model + CommDAAF** | Protocol compliance | Forgotten steps, missing parameters | Model's own calculation/interpretation errors |
| **Multi-model + CommDAAF** | Independent verification | Divergent interpretations, some errors | Errors all models make identically |
| **Human validation** | Ground truth | Systematic model biases | Limited by sample size |

### Key Insight

> CommDAAF in single-model mode is a **methodology scaffold**, not a fact-checker.
> 
> It ensures you follow research protocols but cannot verify your conclusions are correct.

### Multi-Model ≠ Human Validation

Even with 3-model convergence:
- Models may share systematic biases
- Models may all misunderstand ambiguous content
- Models cannot assess real-world validity

**For 🔴 Publication tier**: Multi-model agreement is helpful but does NOT substitute for human validation (N ≥ 200, κ ≥ 0.7).

---

## Validation Requirements Summary

| Tier | Human Sample | κ Threshold | Multi-Model | Replication |
|------|--------------|-------------|-------------|-------------|
| 🟢 Exploratory | — | — | Optional | — |
| 🟡 Pilot | N ≥ 100 | κ ≥ 0.6 | Recommended | 80% subsample |
| 🔴 Publication | N ≥ 200 | κ ≥ 0.7 | Recommended | Bootstrap CI |

---

*Tiered Validation | CommDAAF v0.4*
