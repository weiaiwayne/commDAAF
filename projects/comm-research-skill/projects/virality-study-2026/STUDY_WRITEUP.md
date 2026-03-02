# Frame Effects on Viral Engagement in the #MahsaAmini Protest Movement: An Exploratory Multi-Model LLM Analysis

**Status:** Pilot Study (Preprint Draft)  
**Version:** 1.0  
**Date:** 2026-02-27

---

## Abstract

This exploratory study examines how message framing affects viral engagement in social media protest movements, using the 2022 #MahsaAmini movement as a case study. We employ a novel multi-model LLM annotation approach using three large language models (Claude, GLM-4.7, Kimi K2.5) with majority voting to code 380 tweets across seven frames. Results suggest that INFORMATIONAL framing and high emotional arousal are associated with greater engagement, though findings should be interpreted cautiously given frame-specific reliability limitations and small cell sizes.

---

## 1. Introduction

The #MahsaAmini movement emerged in September 2022 following the death of 22-year-old Mahsa Amini in Iranian morality police custody. The movement generated unprecedented social media activity, with Twitter/X serving as a primary coordination platform for global solidarity and protest mobilization (Tufekci, 2017). Content spanned Persian, English, and Arabic, reflecting both domestic Iranian voices and diaspora communities.

Understanding what makes protest content spread is critical for both social movement organizers and platform researchers. Prior work has established that moralized and emotional content spreads more readily than neutral content (Brady et al., 2017; Stieglitz & Dang-Xuan, 2013), and that framing choices shape public understanding of political events (Entman, 1993; Gamson & Modigliani, 1989). However, less is known about which specific frames predict virality in real-time protest contexts.

**Research Question:** Which message frames are associated with higher viral engagement in the #MahsaAmini protest movement?

This exploratory study applies multi-model LLM annotation using the CommDAAF methodology to examine frame–engagement relationships across 380 Twitter posts from the first two weeks of the movement.

---

## 2. Methods

### 2.1 Data Collection

**Platform:** Twitter/X  
**Time Period:** September 21 – October 3, 2022 (12 days following Mahsa Amini's death on September 16, 2022)  
**Sample Size:** N = 380 tweets  
**Sampling Strategy:** Stratified by engagement tier
- Viral tier (top 5%): n = 105
- High tier (75th–95th percentile): n = 103  
- Medium tier (25th–75th percentile): n = 93
- Low tier (bottom 25%): n = 79

**Language Distribution:**
- Persian (fa): 263 posts (69.2%)
- English (en): 87 posts (22.9%)
- Arabic (ar): 17 posts (4.5%)
- Undefined: 13 posts (3.4%)

**Raw Engagement Descriptives:**
- Retweets: range 0–104, M = 4.5
- Likes: range 0–307, M = 9.5

**Note:** The "low" tier consists entirely of zero-engagement posts, representing baseline protest content that did not spread.

### 2.2 Dependent Variable

**Engagement Metric:** Composite log-transformed score  
**Formula:** `log(retweet_count + 1) + log(like_count + 1) + log(quote_count + 1)`

This composite measure follows recommendations for handling count-based social media engagement data (Bail, 2016; González-Bailón & Lelkes, 2023). The log transformation addresses the characteristic right-skew of viral distributions, while the +1 adjustment handles zero-engagement posts.

**Descriptives:**
- Range: 0.00 – 11.99  
- Mean: 2.05 (SD = 2.40)
- Median: 1.10
- Distribution: Right-skewed (skewness = 1.73), 20.8% zeros (n = 79)

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

**Distribution Diagnostics:**
- Skewness: 1.73 (right-skewed, as expected for viral distributions)
- Zero-inflation: 20.8% (n = 79 zero-engagement posts)
- Variance/mean ratio: 2.79 (overdispersion present)

**Model Selection:** Given overdispersion (var/mean > 1), negative binomial regression would typically be preferred for count outcomes (Hilbe, 2011). However, because the dependent variable is already log-transformed (composite log-engagement), we report OLS with HC3 heteroscedasticity-robust standard errors as the primary analysis. Supplementary negative binomial analysis on raw engagement counts yielded consistent substantive conclusions (INFORMATIONAL: IRR = 2.72, p < .001; High arousal: IRR = 1.58, p = .038).

**OLS Specification:**  
`Engagement = β₀ + β₁(HOPE) + β₂(CONFLICT) + β₃(HUMANITARIAN) + β₄(INJUSTICE) + β₅(INFORMATIONAL) + β₆(CALL_TO_ACTION) + β₇(arousal:medium) + β₈(arousal:high) + ε`

**Reference Categories:** SOLIDARITY (most common frame, n = 122), low arousal

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

### 5.4 Exploratory Tier (No Human Validation)

This study uses LLM-only coding without human validation, classified as **CommDAAF Tier 🟢 (Exploratory)**. Per CommDAAF v0.5 guidelines (DAAF Contribution Community, 2025), exploratory studies:

- Generate hypotheses for future confirmatory research
- Require multi-model agreement (achieved: κ = 0.633)
- Report frame-specific reliability transparently (see §3.2)
- Flag low-reliability frames for cautious interpretation

Human validation was deliberately omitted given the pilot nature of this study. Confirmatory replication with human-LLM calibration is recommended before policy application.

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

Bail, C. A. (2016). Combining natural language processing and network analysis to examine how advocacy organizations stimulate conversation on social media. *Proceedings of the National Academy of Sciences, 113*(42), 11823-11828. https://doi.org/10.1073/pnas.1607151113

Benford, R. D., & Snow, D. A. (2000). Framing processes and social movements: An overview and assessment. *Annual Review of Sociology, 26*(1), 611-639. https://doi.org/10.1146/annurev.soc.26.1.611

Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *Proceedings of the National Academy of Sciences, 114*(28), 7313-7318. https://doi.org/10.1073/pnas.1618923114

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

DAAF Contribution Community. (2025). *Data Analyst Augmentation Framework (DAAF): Guidelines for LLM-assisted content analysis*. GitHub. https://github.com/DAAF-Contribution-Community/daaf

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication, 43*(4), 51-58. https://doi.org/10.1111/j.1460-2466.1993.tb01304.x

Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. *Psychological Bulletin, 76*(5), 378-382. https://doi.org/10.1037/h0031619

Gamson, W. A., & Modigliani, A. (1989). Media discourse and public opinion on nuclear power: A constructionist approach. *American Journal of Sociology, 95*(1), 1-37. https://doi.org/10.1086/229213

González-Bailón, S., & Lelkes, Y. (2023). Do social media undermine social cohesion? A critical review. *Social Issues and Policy Review, 17*(1), 155-180. https://doi.org/10.1111/sipr.12091

Hilbe, J. M. (2011). *Negative binomial regression* (2nd ed.). Cambridge University Press.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159-174. https://doi.org/10.2307/2529310

Semetko, H. A., & Valkenburg, P. M. (2000). Framing European politics: A content analysis of press and television news. *Journal of Communication, 50*(2), 93-109. https://doi.org/10.1111/j.1460-2466.2000.tb02843.x

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media—Sentiment of microblogs and sharing behavior. *Journal of Management Information Systems, 29*(4), 217-248. https://doi.org/10.2753/MIS0742-1222290408

Tufekci, Z. (2017). *Twitter and tear gas: The power and fragility of networked protest*. Yale University Press.

van der Meer, T. G., & Vliegenthart, R. (2018). The complex job of mediating the campaign: Intermedia agenda-setting dynamics in online and traditional news media. *Political Communication, 35*(3), 472-491. https://doi.org/10.1080/10584609.2017.1356471

Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. *Science, 359*(6380), 1146-1151. https://doi.org/10.1126/science.aap9559

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
