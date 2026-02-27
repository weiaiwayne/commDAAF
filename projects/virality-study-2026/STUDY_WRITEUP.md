# Frame Effects on Viral Engagement in the #MahsaAmini Protest Movement: An Exploratory Multi-Model LLM Analysis

**Status:** Pilot Study (Preprint Draft)  
**Version:** 1.0  
**Date:** 2026-02-27

---

## Abstract

This exploratory study examines how message framing affects viral engagement in social media protest movements, using the 2022 #MahsaAmini movement as a case study. We employ a novel multi-model LLM annotation approach using three large language models (Claude, GLM-4.7, Kimi K2.5) with majority voting to code 380 tweets across seven frames. Results suggest that INFORMATIONAL framing and high emotional arousal are associated with greater engagement, though findings should be interpreted cautiously given frame-specific reliability limitations and small cell sizes.

---

## 1. Introduction

[To be expanded]

The #MahsaAmini movement emerged in September 2022 following the death of Mahsa Amini in Iranian morality police custody. The movement generated substantial social media activity, particularly on Twitter/X, with content in Persian, English, and Arabic.

**Research Question:** Which message frames are associated with higher viral engagement in protest movements?

---

## 2. Methods

### 2.1 Data Collection

**Platform:** Twitter/X  
**Time Period:** [NEEDS DOCUMENTATION - September-October 2022]  
**Sample Size:** N = 380 tweets  
**Sampling Strategy:** Stratified by engagement tier
- Viral tier: n = 105
- High tier: n = 103  
- Medium tier: n = 93
- Low tier: n = 79

**Note:** The "low" tier consists entirely of zero-engagement posts, suggesting the sampling strategy intentionally captured the full engagement distribution.

### 2.2 Dependent Variable

**Engagement Metric:** Composite log-transformed score  
**Formula:** [NEEDS CONFIRMATION] `log(retweets + 1) + log(likes + 1) + log(quotes + 1)`  
**Range:** 0.00 - 11.99  
**Distribution:** Right-skewed (skewness = 1.73), 20.8% zeros

### 2.3 Frame Typology

Seven frames adapted from social movement and crisis communication literature:

| Frame | Definition | Key Signals |
|-------|------------|-------------|
| SOLIDARITY | Unity, collective identity | "We stand together", collective pronouns |
| INJUSTICE | Wrongdoing with explicit perpetrator | Blame assigned, "They killed" |
| CONFLICT | Active clash between parties | "Clashes", both sides active |
| HUMANITARIAN | Suffering without perpetrator focus | Victim focus, "Lives lost" |
| HOPE | Optimism, future vision | "We will win", positive future |
| INFORMATIONAL | Neutral facts/updates | "Update:", factual language |
| CALL_TO_ACTION | Appeals to act | "Share this", imperatives |

### 2.4 Multi-Model LLM Annotation

**Models Used:**
1. Claude Opus 4.5 (Anthropic)
2. GLM-4.7 (Zhipu AI)
3. Kimi K2.5 (Moonshot AI)

**Procedure:**
- Each model independently coded all 380 posts
- Used CommDAAF v0.5 methodology with explicit decision rules
- Final coding determined by majority vote (2/3 agreement)

**Reliability:**
- Overall Fleiss' κ = 0.633 (Substantial agreement)
- 3-way agreement: 58.2%
- Majority (2/3) agreement: 94.5%

### 2.5 Statistical Analysis

**Model:** OLS regression with HC3 heteroscedasticity-robust standard errors

**Specification:**  
`Engagement = β₀ + β₁(HOPE) + β₂(CONFLICT) + β₃(HUMANITARIAN) + β₄(INJUSTICE) + β₅(INFORMATIONAL) + β₆(CALL_TO_ACTION) + β₇(arousal:medium) + β₈(arousal:high) + ε`

**Reference Categories:** SOLIDARITY (most common frame), low arousal

**Note on Valence:** Valence was excluded from the model due to near-perfect confounding with frame (see Limitations).

---

## 3. Results

### 3.1 Descriptive Statistics

**Frame Distribution (Majority Vote):**

| Frame | N | % | Mean Engagement | SD |
|-------|---|---|-----------------|-----|
| SOLIDARITY | 122 | 32.1% | 1.73 | 2.28 |
| CALL_TO_ACTION | 69 | 18.2% | 1.83 | 2.69 |
| INJUSTICE | 49 | 12.9% | 2.41 | 2.34 |
| HOPE | 46 | 12.1% | 2.35 | 2.25 |
| HUMANITARIAN | 42 | 11.1% | 1.76 | 1.77 |
| INFORMATIONAL | 34 | 8.9% | 2.34 | 2.31 |
| CONFLICT | 18 | 4.7% | 3.48 | 2.96 |

### 3.2 Frame-Specific Reliability

| Frame | N | 3-Way Agreement | Flag |
|-------|---|-----------------|------|
| SOLIDARITY | 122 | 66% | ✅ |
| HOPE | 46 | 65% | ✅ |
| CALL_TO_ACTION | 69 | 65% | ✅ |
| INFORMATIONAL | 34 | 50% | ✅ |
| INJUSTICE | 49 | 49% | ⚠️ Low reliability |
| HUMANITARIAN | 42 | 45% | ⚠️ Low reliability |
| CONFLICT | 18 | 33% | ⚠️ Low reliability, small n |

### 3.3 Regression Results

**Model Fit:** R² = 0.051, Adj R² = 0.031, F(8, 371) = 2.68, p = .007

| Predictor | b | SE (HC3) | t | p | |
|-----------|---|----------|---|---|---|
| (Intercept) | 1.145 | 0.268 | 4.27 | <.001 | *** |
| HOPE | 0.408 | 0.402 | 1.01 | .310 | |
| CONFLICT | 1.172 | 0.801 | 1.46 | .143 | |
| HUMANITARIAN | -0.167 | 0.360 | -0.46 | .643 | |
| INJUSTICE | 0.262 | 0.483 | 0.54 | .587 | |
| **INFORMATIONAL** | **0.938** | **0.459** | **2.04** | **.041** | * |
| CALL_TO_ACTION | -0.191 | 0.393 | -0.49 | .626 | |
| arousal:medium | 0.625 | 0.302 | 2.07 | .039 | * |
| **arousal:high** | **1.235** | **0.432** | **2.86** | **.004** | ** |

Reference: SOLIDARITY, arousal:low  
Significance: * p<.05, ** p<.01, *** p<.001

### 3.4 Effect Sizes

| Frame vs SOLIDARITY | Cohen's d | Interpretation |
|---------------------|-----------|----------------|
| CONFLICT | 0.73 | Medium |
| INJUSTICE | 0.28 | Small |
| HOPE | 0.26 | Small |
| INFORMATIONAL | 0.25 | Small |
| CALL_TO_ACTION | 0.04 | Negligible |
| HUMANITARIAN | 0.01 | Negligible |

---

## 4. Discussion

### 4.1 Key Findings

1. **INFORMATIONAL framing predicts higher engagement** (b = 0.94, p = .041). Posts presenting factual updates received approximately one unit more (on the log scale) engagement than SOLIDARITY posts, holding arousal constant.

2. **High arousal strongly predicts engagement** (b = 1.24, p = .004). Emotionally intense content received substantially more engagement than low-arousal content.

3. **CONFLICT shows large effect size but not statistically significant** (d = 0.73, p = .143). The small sample (n = 18) and low reliability (33% 3-way agreement) limit confidence in this finding.

### 4.2 Interpretation

In protest contexts saturated with emotional SOLIDARITY content (32% of posts), INFORMATIONAL framing may stand out and attract engagement. This aligns with information-seeking behavior during crisis events.

The arousal effect is robust and suggests that emotional intensity, independent of frame, drives viral spread.

---

## 5. Limitations

### 5.1 Coding Reliability Concerns

Three frames showed poor inter-model agreement:
- **CONFLICT:** Only 33% 3-way agreement (n = 18)
- **HUMANITARIAN:** Only 45% 3-way agreement
- **INJUSTICE:** Only 49% 3-way agreement

Findings related to these frames should be interpreted with caution.

### 5.2 Frame-Valence Confounding

| Frame | % Negative Valence |
|-------|-------------------|
| CONFLICT | 100% |
| HUMANITARIAN | 100% |
| INJUSTICE | 98% |
| HOPE | 0% |
| SOLIDARITY | 3% |

This near-perfect confounding prevented including valence as a separate predictor. Frame effects may partially reflect valence effects.

### 5.3 Small Cell Sizes

CONFLICT (n = 18) is too small for stable regression estimates. Effect size (d = 0.73) is suggestive but the wide confidence interval limits conclusions.

### 5.4 No Human Validation

This study used LLM-only coding without human validation. Per CommDAAF guidelines, this qualifies as exploratory (Tier 🟢) and findings should be treated as hypothesis-generating rather than confirmatory.

### 5.5 Single Platform, Specific Context

Results may not generalize to:
- Other platforms (Instagram, TikTok, Telegram)
- Other protest movements
- Non-crisis contexts

### 5.6 Language Complexity

The dataset includes Persian, English, and Arabic text. LLM handling of Persian metaphorical language and cultural context was not validated.

---

## 6. Conclusion

This exploratory study suggests that INFORMATIONAL framing and high emotional arousal are associated with greater viral engagement in protest movements. However, the modest effect sizes (R² = 5%) and reliability concerns warrant replication with human-validated coding before drawing firm conclusions.

The study demonstrates the feasibility of multi-model LLM annotation for content analysis, achieving substantial overall agreement (κ = 0.633) while revealing frame-specific reliability challenges that should inform future research design.

---

## 7. Data Availability

- Coded data: `regression_data_380.json`
- Frame reliability: `frame_reliability.json`
- Regression results: `regression_corrected.json`
- Repository: https://github.com/weiaiwayne/commDAAF

---

## 8. References

[To be added - frame typology sources, CommDAAF methodology, etc.]

---

## Appendix A: CommDAAF Coding Protocol

See `commdaaf_coding_prompt.md` for full coding instructions provided to LLMs.

## Appendix B: Model-Specific Coding Patterns

| Frame | Claude % | GLM % | Kimi % |
|-------|----------|-------|--------|
| SOLIDARITY | 96% | 84% | 83% |
| HOPE | 91% | 80% | 87% |
| CALL_TO_ACTION | 91% | 77% | 93% |
| INFORMATIONAL | 79% | 79% | 88% |
| INJUSTICE | 76% | 84% | 80% |
| HUMANITARIAN | 64% | 86% | 93% |
| CONFLICT | 100% | 39% | 72% |

Note: GLM substantially under-coded CONFLICT (39% vs 100% Claude), suggesting model-specific interpretation differences.
