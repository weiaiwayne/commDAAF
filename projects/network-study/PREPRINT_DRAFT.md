# Cross-Layer Behavioral Discordance in Social Media: An Empirical Finding and Multi-Model Validation Workflow

**Authors:** [Anonymous for review]

**Abstract:** We investigated whether cross-layer behavioral discordance (the tendency to retweet different accounts than one replies to) could serve as an indicator of coordinated inauthentic behavior on social media. Analysis of 266,242 Ukraine-related tweets revealed that 80% of multi-layer users exhibit zero overlap between their retweet and conversation targets. Contrary to our initial hypothesis, baseline analysis showed this discordance is *more* pronounced among established accounts (83.5% for accounts >3 years old) than new accounts (53.1% for accounts <3 months old). This finding invalidates cross-layer discordance as a coordination detection signal but reveals an interesting pattern about how users engage across interaction modalities. We also document our multi-model AI peer review workflow, in which three large language models (Claude, GLM-4, Kimi) independently critiqued the methodology, leading to the identification of fundamental assumption errors before publication. This workflow demonstrates how AI-assisted peer review can catch conceptual flaws early in the research process.

**Keywords:** social network analysis, coordination detection, multi-layer networks, AI-assisted research, peer review

---

## 1. Introduction

### 1.1 Motivation

Detecting coordinated inauthentic behavior on social media remains a critical challenge. Existing methods like CooRnet (Giglietto et al., 2020) detect coordination through shared content (URLs posted by multiple accounts within time windows). We hypothesized that structural network patterns—specifically, consistency across interaction types—might provide a content-independent coordination signal.

### 1.2 The Cross-Layer Hypothesis

Our initial hypothesis was intuitive: organic users should engage consistently across interaction modalities. If a user finds an account valuable enough to retweet, they might also reply to or quote that account occasionally. Coordinated amplification accounts, by contrast, might show "discordant" behavior—retweeting high-profile targets for visibility while conversing (if at all) with different accounts.

We operationalized this as **Cross-Layer Behavioral Discordance (CLBD)**: the Jaccard similarity between a user's retweet targets and conversation targets. Low similarity (high discordance) was hypothesized to indicate potential coordination.

### 1.3 What We Found

Our hypothesis was wrong. Baseline analysis revealed that cross-layer discordance is the *norm*, not an anomaly—and is actually *more* pronounced among established, active accounts. This paper documents both the negative finding and the multi-model AI workflow that helped identify the flawed assumption before publication.

---

## 2. Data and Methods

### 2.1 Dataset

We analyzed 266,242 Ukraine-related tweets collected June 7-9, 2023, comprising:
- 102,706 unique users
- 191,566 retweets (72%)
- 11,504 reply relationships
- 10,387 quote relationships

### 2.2 Network Construction

We built three directed networks from explicit Twitter relationships:

1. **Retweet network:** Edge A→B if user A retweeted user B (87,267 nodes, 150,581 edges)
2. **Reply network:** Edge A→B if user A replied to user B (11,153 nodes, 11,504 edges)
3. **Quote network:** Edge A→B if user A quoted user B (9,362 nodes, 10,387 edges)

### 2.3 Cross-Layer Behavioral Discordance (CLBD)

For each user appearing in multiple network layers, we calculated:

```
RT_targets = {accounts user retweeted}
Convo_targets = {accounts user replied to OR quoted}

CLBD = |RT_targets ∩ Convo_targets| / |RT_targets ∪ Convo_targets|
```

- CLBD = 1.0: Perfect consistency (same targets across layers)
- CLBD = 0.0: Complete discordance (no overlap)

### 2.4 Baseline Analysis

To test whether discordance indicates coordination, we stratified CLBD scores by user characteristics that proxy for "established" accounts:
- Follower count (>1K vs <100)
- Account age (>3 years vs <3 months)
- Activity level (>100K total tweets vs <1K)

If discordance indicated coordination, established accounts should show *higher* CLBD (more consistency). If discordance is normal, all user types should show similar patterns.

---

## 3. Results

### 3.1 Overall Discordance Distribution

Among 3,211 users with calculable CLBD scores:
- **80.3%** showed zero cross-layer overlap (CLBD = 0)
- Mean CLBD: 0.074
- Median CLBD: 0.000

### 3.2 Baseline Analysis: Discordance is Normal

**Table 1: CLBD by Follower Count**

| Follower Tier | Mean CLBD | Zero Overlap Rate | n |
|---------------|-----------|-------------------|---|
| <100 | 0.109 | 79.1% | 521 |
| 100-1K | 0.060 | 82.1% | 1,259 |
| 1K-10K | 0.069 | 79.7% | 1,251 |
| >10K | 0.100 | 74.7% | 166 |

**Table 2: CLBD by Account Age**

| Account Age | Mean CLBD | Zero Overlap Rate | n |
|-------------|-----------|-------------------|---|
| <3 months | 0.283 | 53.1% | 147 |
| 3mo-1yr | 0.078 | 78.3% | 396 |
| 1-3 years | 0.070 | 77.6% | 661 |
| >3 years | 0.060 | **83.5%** | 2,004 |

**Table 3: CLBD by Activity Level**

| Total Tweets | Mean CLBD | Zero Overlap Rate | n |
|--------------|-----------|-------------------|---|
| <1K | 0.214 | 69.8% | 248 |
| 1K-10K | 0.076 | 82.3% | 965 |
| 10K-100K | 0.056 | 81.1% | 1,589 |
| >100K | 0.054 | 78.5% | 409 |

### 3.3 Key Finding: Established Accounts Are MORE Discordant

Counter to our hypothesis:
- Old accounts (>3 years) have **higher** discordance (83.5% zero overlap) than new accounts (53.1%)
- High-activity accounts (>100K tweets) have **higher** discordance (78.5%) than low-activity accounts (69.8%)
- Statistical tests (Mann-Whitney U) showed no significant difference between high-follower and low-follower accounts (p = 0.78)

### 3.4 Interpretation

The baseline analysis invalidates CLBD as a coordination detection metric. The finding that established accounts show *more* discordance suggests that cross-layer specialization is a feature of mature Twitter engagement, not a coordination signal.

**Possible explanations:**
1. **Role differentiation:** Established users develop distinct patterns—retweeting news sources and experts while conversing with community members and friends
2. **Network size effects:** As networks grow, the probability of overlap between retweet and conversation targets decreases
3. **Platform norms:** Twitter's design encourages different interaction types for different purposes (retweets for amplification, replies for conversation)

---

## 4. Multi-Model AI Peer Review Workflow

### 4.1 Motivation

Before conducting the baseline analysis, we subjected our methodology to review by three large language models to identify potential flaws. This workflow was designed to catch conceptual errors early.

### 4.2 Workflow

1. **Initial analysis (Claude):** Conducted network analysis, calculated CLBD, identified 165 "high-confidence anomalies"
2. **Self-critique (Claude):** Identified 8 methodological concerns including lack of baseline, short time window, and threshold arbitrariness
3. **Independent review (GLM-4):** Provided harsh critique, identifying the foundational assumption as "likely incorrect"
4. **Third review (Kimi):** Balanced assessment, agreed with GLM on core issues, recommended reframing as exploratory analysis
5. **Baseline analysis (Claude):** Conducted empirical test of the foundational assumption
6. **Conclusion:** Multi-model consensus led to hypothesis rejection before publication

### 4.3 Model Assessments

**Table 4: Multi-Model Confidence in CLBD**

| Question | Claude | GLM-4 | Kimi |
|----------|--------|-------|------|
| Foundational assumption valid? | 60% | 0% | ~30% |
| CLBD detects coordination? | 40% | 15% | ~30% |
| Ready for publication as method? | No | No | No |

### 4.4 Key Critiques Identified by AI Review

**GLM-4's critical insight:**
> "The assumption that organic users have high cross-layer consistency is asserted without evidence and likely incorrect. Users RT *sources* (news outlets, journalists) but *reply to* community members, friends. These sets are fundamentally different in organic behavior."

**Kimi's synthesis:**
> "CLBD may be detecting *user types* (broadcasters vs conversationalists) rather than *authenticity* (organic vs coordinated)."

### 4.5 Value of Multi-Model Review

The AI peer review workflow:
1. **Identified the core conceptual flaw** before empirical testing
2. **Provided diverse perspectives** (GLM-4 harsher, Kimi more balanced)
3. **Suggested the baseline analysis** that ultimately invalidated the hypothesis
4. **Prevented publication of flawed claims**

---

## 5. Discussion

### 5.1 The Negative Finding

Cross-layer behavioral discordance cannot serve as a coordination detection signal because discordance is the norm for Twitter users, particularly established accounts. This negative finding is valuable: it prevents future researchers from pursuing this particular dead end.

### 5.2 The Positive Finding

The observation that discordance *increases* with account maturity is itself interesting. It suggests that Twitter engagement becomes more specialized over time, with users developing distinct patterns for different interaction types. This could inform research on:
- Social media literacy and expertise
- Platform affordances and user behavior
- Network evolution and role differentiation

### 5.3 Limitations

1. **Single platform:** Findings may not generalize beyond Twitter
2. **Crisis context:** Ukraine war discourse may differ from routine engagement
3. **Short time window:** 3-day snapshot may not capture stable patterns
4. **Hashtag collection:** Data may oversample broadcast behavior

### 5.4 Implications for AI-Assisted Research

Our multi-model workflow demonstrates that AI peer review can:
- Identify conceptual flaws before empirical investment
- Provide diverse critical perspectives
- Suggest validation approaches
- Improve research quality through iterative critique

However, AI review cannot replace human judgment on:
- Domain expertise and literature context
- Ethical considerations
- Final publication decisions

---

## 6. Conclusion

We proposed Cross-Layer Behavioral Discordance (CLBD) as a potential coordination detection signal, hypothesizing that coordinated accounts would show inconsistent engagement patterns across network layers. Empirical baseline analysis revealed that discordance is normal—and actually more pronounced among established accounts—invalidating the hypothesis.

This paper contributes:
1. **A negative finding:** CLBD does not indicate coordination
2. **A positive finding:** Cross-layer specialization increases with account maturity
3. **A methodological demonstration:** Multi-model AI peer review can identify flawed assumptions early

We encourage researchers to:
- Test foundational assumptions empirically before claiming detection capability
- Use multi-model AI review as a supplement (not replacement) for human peer review
- Report negative findings to prevent duplication of failed approaches

---

## 7. Data and Code Availability

Analysis code and aggregated metrics available at [repository]. Raw Twitter data cannot be shared per platform terms of service.

---

## References

De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., ... & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X*, 3(4), 041022.

Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*, 23(6), 867-891.

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks*, 2(3), 203-271.

Righetti, N., & Balluff, P. (2025). CooRTweet: A Generalized R Software for Coordinated Network Detection. *Computational Communication Research*, 7(1), 1.

---

## Appendix A: Statistical Tests

**Mann-Whitney U Test: High-Follower vs Low-Follower CLBD**
- High followers (>1K): mean = 0.072, n = 1,417
- Low followers (<100): mean = 0.113, n = 532
- U statistic: [value]
- p-value: 0.777 (not significant)
- Interpretation: No evidence that established accounts have higher cross-layer consistency

**Mann-Whitney U Test: Old vs New Account CLBD**
- Old accounts (>3yr): mean = 0.059, n = 1,954
- New accounts (<3mo): mean = 0.281, n = 148
- U statistic: [value]
- p-value: 1.000 (not significant in hypothesized direction)
- Interpretation: Old accounts actually show *lower* consistency (higher discordance)

---

## Appendix B: Multi-Model Review Excerpts

### B.1 Claude Self-Critique (Selected)

> "Without a baseline, we can't claim 'discordance = suspicious.' It may just be 'discordance = normal.'"

### B.2 GLM-4 Critical Review (Selected)

> "The core premise is empirically unsupported and likely incorrect. This isn't just about missing baselines—it's building a method on an untested assumption."

### B.3 Kimi Synthesis (Selected)

> "Claude was wrong in degree, not in kind. The pattern is real; the interpretation is backwards."

---

*Preprint draft - Not yet peer reviewed*
