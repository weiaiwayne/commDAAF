# Cross-Layer Behavioral Discordance in Social Media: A Negative Finding and Multi-Model Validation Workflow

**Authors:** Wayne Xu¹, AI Research Collective (Claude, GLM-4, Kimi)²

¹ Boston University  
² AgentAcademy Multi-Model Research Initiative

**Preprint | March 2026**

---

## Abstract

We investigated whether cross-layer behavioral discordance—the tendency to retweet different accounts than one replies to—could serve as an indicator of coordinated inauthentic behavior on social media. Analysis of 266,242 Ukraine-related tweets (June 2023) revealed that 80% of multi-layer users exhibit zero overlap between their retweet and conversation targets. Contrary to our initial hypothesis, baseline analysis stratified by account characteristics showed this discordance is *more* pronounced among established accounts (83.5% zero overlap for accounts >3 years old) than new accounts (53.1% for accounts <3 months old). This finding invalidates cross-layer discordance as a coordination detection signal but reveals that cross-layer specialization is a normal feature of mature social media engagement.

We also document our multi-model AI peer review workflow guided by the CommDAAF (Communication Data Analysis Augmentation Framework) methodology. Three large language models independently critiqued the methodology, with the second reviewer (GLM-4) identifying the flawed foundational assumption that the initial analysis missed. This workflow demonstrates how AI-assisted peer review, when combined with systematic validation protocols, can catch conceptual errors before publication.

**Keywords:** social network analysis, coordination detection, multi-layer networks, negative results, AI-assisted research, CommDAAF

---

## 1. Introduction

### 1.1 The Challenge of Coordination Detection

Detecting coordinated inauthentic behavior (CIB) on social media remains a critical challenge for platform integrity and democratic discourse. Existing methods primarily rely on content-based signals: CooRnet (Giglietto et al., 2020) and CooRTweet (Righetti & Balluff, 2025) detect coordination through shared URLs posted by multiple accounts within temporal windows. These methods are effective but require content matching and detect group-level rather than individual-level coordination.

### 1.2 The Cross-Layer Hypothesis

We hypothesized that network structure—specifically, behavioral consistency across interaction types—might provide a content-independent coordination signal. The intuition was straightforward: organic users who find an account valuable enough to retweet might also engage with that account through replies or quotes. Coordinated amplification accounts, designed for single-purpose reach maximization, might show "discordant" behavior—retweeting high-profile targets while conversing (if at all) with entirely different accounts.

We operationalized this as **Cross-Layer Behavioral Discordance (CLBD)**: the Jaccard similarity between a user's retweet targets and conversation targets (replies + quotes). Low similarity indicated high discordance, hypothesized as a potential coordination indicator.

### 1.3 The Importance of Negative Findings

As documented below, our hypothesis was wrong. However, negative findings serve critical scientific functions: they prevent duplication of failed approaches, refine theoretical understanding, and establish empirical boundaries for future research (Fanelli, 2012). We report this negative finding in full, along with the methodological lessons learned.

### 1.4 Research Questions

**RQ1:** Does cross-layer behavioral discordance differ between user types (established vs. new accounts)?

**RQ2:** Can CLBD serve as a coordination detection signal?

**RQ3:** Can multi-model AI peer review identify flawed assumptions before empirical testing?

---

## 2. Methods

### 2.1 Methodological Framework

This study was conducted within the **CommDAAF (Communication Data Analysis Augmentation Framework)** methodology, which provides structured protocols for computational communication research. CommDAAF emphasizes:
- Probing questions before analysis
- Baseline validation before anomaly claims
- Multi-model review for methodological rigor
- Explicit falsification criteria

Notably, the initial analysis **did not rigorously follow** CommDAAF's baseline validation protocols—an omission that allowed the flawed assumption to persist until the multi-model review phase. This serves as a case study in why systematic validation matters.

### 2.2 Dataset

We analyzed 266,242 Ukraine-related tweets collected June 7-9, 2023, comprising:
- **102,706** unique users
- **191,566** retweets (72% of tweets)
- **74,676** original tweets and replies (28%)
- **27,657** quote tweets

Data included user metadata: follower count, account creation date, and total tweet count.

### 2.3 Network Construction

Three directed networks were constructed from explicit Twitter relationships:

| Network | Definition | Nodes | Edges |
|---------|------------|-------|-------|
| Retweet | A→B if A retweeted B | 87,267 | 150,581 |
| Reply | A→B if A replied to B | 11,153 | 11,504 |
| Quote | A→B if A quoted B | 9,362 | 10,387 |

### 2.4 Cross-Layer Behavioral Discordance (CLBD)

For users appearing in multiple network layers (n=3,211), we calculated:

$$CLBD = \frac{|RT_{targets} \cap Convo_{targets}|}{|RT_{targets} \cup Convo_{targets}|}$$

Where:
- $RT_{targets}$ = set of accounts the user retweeted
- $Convo_{targets}$ = set of accounts the user replied to OR quoted

CLBD ranges from 0 (complete discordance) to 1 (perfect consistency).

### 2.5 Baseline Analysis

To test whether discordance indicates coordination (rather than normal behavior), we stratified CLBD by user characteristics:

- **Account age:** <3 months, 3mo-1yr, 1-3yr, >3yr
- **Follower count:** <100, 100-1K, 1K-10K, >10K  
- **Activity level:** <1K, 1K-10K, 10K-100K, >100K total tweets

**Hypothesis:** If discordance indicates coordination, established accounts (older, more followers, more active) should show *higher* CLBD (more consistency). If discordance is normal platform behavior, all user types should show similar patterns.

### 2.6 Statistical Analysis

Mann-Whitney U tests compared CLBD distributions between user groups. Significance threshold: p < 0.05.

### 2.7 Multi-Model Review Protocol

Following CommDAAF guidelines, we subjected the methodology to review by three large language models:

1. **Claude (Anthropic):** Initial analysis and self-critique
2. **GLM-4 (Zhipu AI):** Independent skeptical review
3. **Kimi (Moonshot AI):** Balanced synthesis

Each model was instructed to identify methodological flaws, challenge assumptions, and recommend whether findings were publication-ready.

---

## 3. Results

### 3.1 Overall Discordance Distribution

Among 3,211 users with calculable CLBD scores:
- **80.3%** showed zero cross-layer overlap (CLBD = 0)
- Mean CLBD: 0.074
- Median CLBD: 0.000
- Standard deviation: 0.215

### 3.2 CLBD by Account Characteristics

**Table 1: CLBD by Account Age**

| Account Age | n | Mean CLBD | Zero Overlap Rate |
|-------------|---|-----------|-------------------|
| <3 months | 147 | 0.283 | 53.1% |
| 3mo-1yr | 396 | 0.078 | 78.3% |
| 1-3 years | 661 | 0.070 | 77.6% |
| >3 years | 2,004 | 0.060 | **83.5%** |

**Table 2: CLBD by Follower Count**

| Followers | n | Mean CLBD | Zero Overlap Rate |
|-----------|---|-----------|-------------------|
| <100 | 521 | 0.109 | 79.1% |
| 100-1K | 1,259 | 0.060 | 82.1% |
| 1K-10K | 1,251 | 0.069 | 79.7% |
| >10K | 166 | 0.100 | 74.7% |

**Table 3: CLBD by Activity Level**

| Total Tweets | n | Mean CLBD | Zero Overlap Rate |
|--------------|---|-----------|-------------------|
| <1K | 248 | 0.214 | 69.8% |
| 1K-10K | 965 | 0.076 | 82.3% |
| 10K-100K | 1,589 | 0.056 | 81.1% |
| >100K | 409 | 0.054 | 78.5% |

### 3.3 Statistical Tests

**High-follower vs. Low-follower accounts:**
- High followers (>1K): mean CLBD = 0.072, n = 1,417
- Low followers (<100): mean CLBD = 0.113, n = 532
- Mann-Whitney U: p = 0.777
- **Result:** No significant difference

**Old vs. New accounts:**
- Old accounts (>3yr): mean CLBD = 0.059, n = 1,954
- New accounts (<3mo): mean CLBD = 0.281, n = 148
- Mann-Whitney U (testing if old > new): p = 1.000
- **Result:** Old accounts have *lower* CLBD (more discordance), opposite to hypothesis

### 3.4 Key Finding: Established Accounts Are MORE Discordant

**Figure 1** (described): Zero overlap rate increases with account age, from 53.1% for new accounts to 83.5% for accounts over 3 years old.

This finding **invalidates CLBD as a coordination detection signal.** If discordance indicated coordination:
- Established accounts should show HIGH consistency (low discordance)
- New/suspicious accounts should show LOW consistency (high discordance)

**Observed pattern is the opposite:** Established accounts show the highest discordance rates.

### 3.5 Multi-Model Review Results

**Table 4: Model Assessments of CLBD**

| Assessment | Claude | GLM-4 | Kimi |
|------------|--------|-------|------|
| Foundational assumption valid | 60% | 0% | ~30% |
| CLBD detects coordination | 40% | 15% | ~30% |
| Publish as novel method | No | No | No |
| Publish as exploratory | Yes | Conditional | Yes |

**GLM-4's critical insight** (identified before baseline analysis):
> "The assumption that organic users have high cross-layer consistency is asserted without evidence and likely incorrect. Users retweet *sources* (news outlets, journalists) but *reply to* community members and friends. These sets are fundamentally different in organic behavior."

**Kimi's synthesis:**
> "CLBD may be detecting *user types* (broadcasters vs. conversationalists) rather than *authenticity* (organic vs. coordinated)."

### 3.6 Comparison to CooRnet-Style Detection

To contextualize CLBD, we compared flagged accounts to a CooRnet-style analysis (accounts that co-retweet the same sources).

| Method | Accounts Flagged | Overlap |
|--------|------------------|---------|
| CLBD (top 165) | 165 | 2 (1.2%) |
| CooRnet-style (top 165) | 165 | 2 (1.2%) |

The 1.2% overlap initially suggested complementary detection. However, given CLBD's invalidation, this overlap may reflect that both methods flag different aspects of normal behavioral variation rather than different types of coordination.

---

## 4. Discussion

### 4.1 Why Discordance Is Normal

The baseline analysis reveals that cross-layer discordance is a feature of mature Twitter engagement, not a bug indicating coordination. We propose three explanations:

**Role differentiation:** Established users develop distinct engagement patterns. They retweet news sources, experts, and public figures for information amplification, while reserving replies and quotes for community members, colleagues, and friends. These target sets are naturally distinct.

**Network size effects:** As users' networks grow, the probability of overlap between retweet and conversation targets decreases mathematically. With more potential targets in each category, random overlap becomes less likely.

**Platform affordances:** Twitter's design encourages modality-specific behavior. Retweets serve amplification functions; replies serve conversational functions. Users learn to use these features for different purposes with different targets.

### 4.2 Why New Accounts Show Higher Consistency

New accounts (<3 months) showed surprisingly *higher* CLBD (mean = 0.283 vs. 0.060 for old accounts). Possible explanations:

- **Smaller networks:** New accounts engage with fewer targets overall, increasing overlap probability
- **Learning phase:** New users may not yet have differentiated their engagement patterns
- **Community entry:** New accounts may initially engage with the same accounts across modalities while establishing presence

### 4.3 Implications for Coordination Detection

This negative finding has direct implications for coordination detection research:

1. **Content-independent structural signals require validation:** The intuition that "inconsistency = suspicious" does not hold for cross-layer behavior
2. **Baseline establishment is essential:** Any anomaly detection method must establish what "normal" looks like across user types
3. **Existing methods (CooRnet) target different phenomena:** URL-sharing coordination remains a valid detection target; behavioral consistency does not

### 4.4 Value of Multi-Model Review

The multi-model review workflow successfully identified the flawed assumption—but only because one model (GLM-4) was explicitly skeptical. Key observations:

- **Model diversity matters:** Claude's self-critique identified methodological issues but underestimated severity; GLM-4's harsher stance correctly identified the core flaw
- **Empirical testing remains essential:** The models' predictions were validated only through baseline analysis
- **AI review supplements, doesn't replace:** Human judgment on domain context, ethics, and publication decisions remains necessary

### 4.5 Limitations

1. **Single platform:** Findings may not generalize to other social media platforms
2. **Crisis context:** Ukraine war discourse may differ from routine engagement
3. **Short time window:** 3-day snapshot may not capture stable patterns
4. **Hashtag collection:** Data collection via hashtags may oversample broadcast behavior
5. **CommDAAF protocol violation:** Initial analysis did not follow baseline validation protocols, allowing the flaw to persist

### 4.6 Future Directions

1. **Cross-platform validation:** Test whether discordance patterns hold on Reddit, Mastodon, etc.
2. **Longitudinal analysis:** Track how individual users' CLBD evolves over time
3. **Community-specific baselines:** Some communities (e.g., academic Twitter) may have higher expected consistency
4. **Integration with other signals:** CLBD might contribute to ensemble models even if not discriminative alone

---

## 5. Conclusion

We proposed Cross-Layer Behavioral Discordance (CLBD) as a potential content-independent coordination detection signal. Baseline analysis stratified by account characteristics revealed that discordance is normal—and increases with account maturity—invalidating the hypothesis.

### Contributions

1. **Negative finding:** CLBD does not indicate coordination; cross-layer specialization is normal
2. **Empirical baseline:** Established accounts show 83.5% zero overlap vs. 53.1% for new accounts
3. **Methodological demonstration:** Multi-model AI review can identify flawed assumptions, but empirical validation remains essential
4. **Protocol lesson:** Skipping CommDAAF's baseline validation protocols allowed flawed assumptions to persist

### Recommendations

- **Test foundational assumptions empirically** before building detection methods
- **Establish baselines** across user types before claiming anomalies
- **Use multi-model review** as one component of methodological validation
- **Report negative findings** to prevent duplication of failed approaches

---

## Acknowledgments

This research was conducted using the CommDAAF (Communication Data Analysis Augmentation Framework) methodology. We thank the AgentAcademy initiative for supporting multi-model collaborative research.

---

## References

Fanelli, D. (2012). Negative results are disappearing from most disciplines and countries. *Scientometrics*, 90(3), 891-904.

Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*, 23(6), 867-891.

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks*, 2(3), 203-271.

Righetti, N., & Balluff, P. (2025). CooRTweet: A Generalized R Software for Coordinated Network Detection. *Computational Communication Research*, 7(1), 1.

---

## Appendix: Multi-Model Review Excerpts

### A.1 Claude Self-Critique

> "Without a baseline, we can't claim 'discordance = suspicious.' It may just be 'discordance = normal.' [...] Required validation: Ground truth dataset with labeled coordinated/organic accounts; compare CLBD distributions between groups."

### A.2 GLM-4 Critical Review

> "The core premise is empirically unsupported and likely incorrect. Users RT sources (news outlets, journalists, experts). Users reply to community members, friends, people in conversations. These sets are fundamentally different in organic behavior. Example: An organic user might RT @CNN, @BBCBreaking but reply to @neighbor_discussing_news. Jaccard = 0.0. Is this suspicious? No, this is normal topic-focused engagement."

### A.3 Kimi Synthesis

> "Claude was wrong in degree, not in kind. The pattern is real; the interpretation is backwards. CLBD may be detecting user types (broadcasters vs conversationalists) rather than authenticity (organic vs coordinated). [...] Recommendation: Reframe as exploratory structural analysis, not coordination detection method."

---

*AgentAcademy Preprint | March 2026 | CommDAAF-Guided Research*
