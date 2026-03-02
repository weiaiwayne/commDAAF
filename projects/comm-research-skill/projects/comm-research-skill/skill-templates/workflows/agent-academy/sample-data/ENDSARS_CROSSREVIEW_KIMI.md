# Critical Peer Review: GLM's #EndSARS Analysis

**Reviewer:** Kimi (CommDAAF Red-Team Workflow)  
**Review Target:** GLM-4.7's #EndSARS Analysis  
**Review Date:** February 17, 2026  
**Cross-Reference:** Kimi's parallel analysis of same dataset

---

## Executive Summary

GLM's analysis provides a thorough descriptive overview of the #EndSARS Twitter dataset with strong theoretical framing and practical implications. However, **several methodological issues warrant correction**, most notably a potentially inflated correlation coefficient (r=0.412 vs. r=0.251 for the same relationship). This review identifies statistical concerns, unsupported claims, missing considerations, and areas where GLM's analysis excels.

---

## 1. Critical Issue: The Correlation Discrepancy

### The Problem

| Metric | GLM's Report | Kimi's Report | Issue |
|--------|--------------|---------------|-------|
| Follower→Likes correlation | **r = 0.412** | **r = 0.251** | **64% difference** |
| Activity→Likes correlation | r = 0.222 | r = 0.222 | ✅ Consistent |

The 64% discrepancy in the follower count correlation is substantial and requires explanation.

### Root Cause Analysis

**Most Likely Explanation: Data Transformation**

My analysis explicitly used **log-transformed follower counts** (noted as "Follower count (log)" in Table 5.1), while GLM appears to have used **raw follower counts**. This explains:

1. **Why the activity correlation matches (r=0.222):** Tweet counts are less skewed and less affected by log transformation
2. **Why follower correlation differs:** Raw follower counts on Twitter follow an extreme power-law distribution (mean: 4,987; median: 441 per GLM's own report)

### Why GLM's r=0.412 May Be Misleading

Using Pearson correlation on raw follower counts has serious drawbacks:

1. **Outlier Inflation:** A few accounts with millions of followers (e.g., @amnestyusa, @TeenVogue) disproportionately inflate the correlation
2. **Violated Assumptions:** Pearson correlation assumes approximately normal distributions; raw follower counts are heavily right-skewed
3. **Interpretability Issues:** A 1-unit increase in followers (from 100→101 vs. 100,000→100,001) has vastly different meanings

### Correct Approach

**Log transformation** (typically natural log or log₁₀) is the standard practice for social media follower data because:
- It normalizes the distribution
- It reflects the multiplicative nature of social influence
- It reduces outlier dominance

**Recommendation:** GLM should recalculate using log-transformed follower counts or use Spearman rank correlation (non-parametric, handles skew). The r=0.251 figure from my analysis is more methodologically sound.

### Effect Size Interpretation Issues

GLM characterizes r=0.412 as a "moderate positive relationship." Even if we accept GLM's figure:
- r² = 0.17 (17% of variance explained)—this leaves **83% of engagement variance unexplained**
- With log transformation (r=0.251), r² = 0.06 (6% explained)—a "weak" relationship by conventional standards

GLM's interpretation of "moderate" overstates the practical significance of follower count.

---

## 2. Statistical and Methodological Errors

### 2.1 Network Metrics: Confusing Creators vs. Amplifiers

**GLM's Table 2.1** reports "Top Amplifiers by Retweet Volume" but mixes two distinct categories:

| Account | GLM's Characterization | Actual Role |
|---------|------------------------|-------------|
| @renoomokri | "Central amplifier" | Original content creator |
| @cryssiedenise_ | "Amplifier" | Likely amplifier (needs verification) |

**The Problem:** GLM conflates accounts that *create* viral content with accounts that *amplify* others' content. The table shows who was *retweeted*, not who did the retweeting.

**Correct Approach:** GLM should distinguish:
- **Source nodes:** Accounts whose tweets were retweeted (content creators)
- **Amplifier nodes:** Accounts doing the retweeting (if that data is available)

My analysis identifies this explicitly by noting @RTEndSars, @botofaweirdo as likely bot amplifiers vs. @renoomokri, @AishaYesufu as content creators.

### 2.2 Temporal Phase Classification Inconsistency

**GLM's Phase Definitions (Section 3.1):**

| Phase | Dates | GLM's Classification |
|-------|-------|---------------------|
| Peak | Oct 22-24, Oct 29-30, Nov 1-4 | "Peak" (657 tweets/bin) |
| Moderate | Oct 21, Oct 26-28, Nov 2 | "Moderate" (327 tweets/bin) |
| Low | Oct 31 - Nov 1 | "Low" (571 tweets/bin) |

**The Problem:** GLM notes that the "Low" phase has 571 tweets/bin—**higher than the "Moderate" phase's 327 tweets/bin**. This is contradictory.

**Evidence:** GLM states: "Mean tweets/bin: 571 (only 2 bins classified as 'Low' due to outlier activity)"

**Recommendation:** Either:
1. Relabel phases based on actual tweet volume (Low: Oct 26-28; Moderate: Oct 31-Nov 1), or
2. Use alternative classification (e.g., engagement rate, retweet virality)

My analysis uses different, event-aligned boundaries (Oct 26 = government response shift; Nov 1 = accountability focus) which are more theoretically grounded.

### 2.3 Engagement Metric Confounding Not Fully Addressed

GLM acknowledges in Section 1.2 that "retweet engagement metrics reflect the original tweet's virality, not the retweeter's engagement." However:

**In Section 5.1**, GLM reports engagement statistics for "Original Tweets Only (n=2,000)" but does not explicitly state whether the retweet counts analyzed are:
- (a) Retweets *of* the original tweet in the dataset, or
- (b) Retweets *of* the original tweet globally (including outside the sample)

**Implication:** If (b), the sample is biased toward already-viral content. GLM should clarify.

### 2.4 Missing Confidence Intervals

GLM reports correlations without confidence intervals or p-values. For research transparency:
- r = 0.412 [95% CI: ?, ?]
- Statistical significance should be reported

My analysis notes p<0.001 for the r=0.251 correlation, providing standard error context.

---

## 3. Claims Not Fully Supported by Evidence

### 3.1 "Sustained Movement Momentum" Claim

**GLM's Claim (Section 3.1):** "The absence of clear decay suggests **sustained movement momentum** throughout the 14-day period."

**Evidence Assessment:**
- GLM's own Figure 1 (referenced but not shown) likely shows declining volume
- My analysis shows declining average retweets per phase: 7,345 → 3,969 → 2,469
- Standard social movement theory expects peak-and-decay patterns

**Missing Evidence:** GLM does not provide:
- Statistical test for trend (e.g., Mann-Kendall)
- Comparison to baseline Twitter activity
- Engagement rate metrics (engagement per tweet, not raw volume)

**Alternative Interpretation:** The data shows **volume stability** but **virality decline**, which is consistent with movement normalization rather than sustained momentum.

### 3.2 "Democratized Amplification" Claim

**GLM's Claim (Section 6.2):** "amplification is democratized: users across the follower spectrum contribute to virality"

**Evidence Assessment:**
- GLM shows retweeters have lower follower counts (mean: 1,582) than original tweeters (mean: 18,607)
- However, **this does not demonstrate democratized influence**

**Missing Analysis:** 
- What proportion of total retweet volume comes from low-follower vs. high-follower accounts?
- Does retweeting behavior actually drive viral cascades, or just reflect them?
- Causal evidence that low-follower retweets contribute to virality

**Theoretical Issue:** Bennett & Segerberg's "connective action" does not imply democratized influence—it emphasizes personalized content sharing within unequal network structures.

### 3.3 Celebrity Amplification Assessment

**GLM's Claim (Section 2.1):** "Celebrity amplification is present but less dominant than expected."

**Evidence Assessment:**
- GLM notes @LilNasX and Kerry Washington but says they're "not among the top amplifiers"
- However, GLM's methodology for identifying "top amplifiers" (retweet volume) may miss celebrity impact

**Missing Consideration:** Celebrity tweets may have high engagement but low retweet volume if they:
- Tweeted outside the sample window
- Were retweeted less but favorited more
- Drove traffic to the hashtag without being retweeted themselves

My analysis identifies celebrity statements (@MiaFarrow, @LilNasX mentions) as driving high-engagement content patterns.

---

## 4. Missing Considerations

### 4.1 Bot Detection and Automated Amplification

**GLM's Coverage:** Minimal. GLM mentions "bot" usernames only in passing.

**What's Missing:**
- Systematic bot detection (e.g., Botometer scores, behavioral patterns)
- The top 4 most active accounts in my analysis have "bot" in their usernames:
  - @RTEndSars (41 tweets)
  - @botofaweirdo (31 tweets)
  - @TheEndSarsBot (17 tweets)
  - @sorosokebot (16 tweets)

**Implication:** Up to **10.5% of the sample** (105 tweets from top 4 bot accounts alone) may be automated. This affects:
- Retweet rate interpretation
- Engagement authenticity
- Network structure validity

**Recommendation:** GLM should acknowledge automated amplification as a significant confounding factor.

### 4.2 Platform Moderation and Content Removal

**GLM's Coverage:** Mentioned in limitations (Section 7.1): "Platform moderation may have removed sensitive content before collection"

**What's Missing:**
- Discussion of how content removal bias affects findings
- The Lekki shooting videos were reportedly removed by Twitter—how does this shape the dataset?
- Impact on content analysis (violence mentions may be underrepresented)

### 4.3 Cross-Platform and Offline Context

**GLM's Coverage:** Acknowledges external validity limits (Section 7.3)

**What's Missing:**
- Discussion of WhatsApp's role (primary platform for Nigerian activism)
- How Twitter discourse relates to on-ground protest dynamics
- Diaspora vs. domestic Nigerian user composition

### 4.4 Hashtag Variant Analysis

**GLM's Coverage:** Notes case sensitivity in hashtag usage (Section 4.1)

**What's Missing:**
- Analysis of whether variant spellings create fragmentation
- Network effects of different hashtags (#LekkiMassacre vs #LekkiGenocide)
- Temporal evolution of hashtag usage

My analysis notes variant spellings (#EndBadGovernanceInNigeria vs #EndBadGoveranceInNigeria) indicate organic rather than coordinated mobilization—an insight GLM misses.

### 4.5 Safety and Chilling Effects

**GLM's Coverage:** Not addressed

**What's Missing:**
- Why is the retweet rate so high (80%)? One explanation: safety concerns in authoritarian context
- Nigerian government arrested protesters; Twitter retweeting is lower-risk than original speech
- Implications for interpreting "amplification" as engagement vs. self-protection

My analysis raises this as a key theoretical contribution (Section 8.1): "High retweet rates may reflect safety-seeking behavior rather than passive participation."

---

## 5. What GLM Got Right (Fair Assessment)

### 5.1 Theoretical Framing

GLM's engagement with theory is stronger than my analysis in several areas:

| Theory | GLM's Application | Assessment |
|--------|-------------------|------------|
| Networked Counterpublics (Fraser, 1990) | Section 8.1 | Well-integrated, appropriate |
| Connective Action (Bennett & Segerberg, 2013) | Section 8.1 | Correctly applied |
| Matthew Effect (Merton, 1968) | Section 8.1 | Insightful connection |
| Collective Sensemaking (Weick, 1995) | Section 8.1 | Crisis context appropriate |

GLM's theoretical discussion (Section 8.1) is more developed and offers clearer connections between findings and established literature.

### 5.2 Methodological Transparency

**GLM's Strengths:**
- Explicit CommDAAF tier designation (Exploratory)
- Clear parameter choices with rationales (Section 1.1)
- Dedicated limitations section (Section 7)
- Data dictionary provided (Appendix B)

**Comparison:** My analysis is more concise but less transparent about specific analytical choices.

### 5.3 Practical Implications

GLM's Section 8.2 ("Practical Implications") provides actionable recommendations for:
- Activists (4 specific recommendations)
- Researchers (4 specific recommendations)
- Platform designers (3 specific recommendations)

This demonstrates research impact thinking that my analysis lacks.

### 5.4 Engagement Distribution Analysis

GLM's Table 5.1 provides more granular engagement percentiles than my analysis:

| Metric | GLM | Kimi |
|--------|-----|------|
| Likes 90th percentile | 4 | Not reported |
| Likes 95th percentile | 7 | Not reported |
| Maximum likes | 737 | 737 ✅ (consistent) |

GLM's detailed percentile reporting enables better assessment of skew.

### 5.5 Network Structure Characterization

GLM's "hybridized decentralization" concept (Section 2.1) is a useful theoretical contribution that accurately describes the observed structure. The characterization of top accounts as "central amplifiers rather than traditional leaders" is nuanced and appropriate.

---

## 6. Recommendations for Revision

### High Priority (Address Before Publication)

1. **Recalculate correlation with log-transformed follower counts** or use Spearman correlation
2. **Clarify the "Low" phase classification**—the current labeling contradicts the data
3. **Distinguish content creators from amplifiers** in network analysis tables
4. **Add confidence intervals** to correlation coefficients

### Medium Priority (Strengthens Analysis)

5. **Address bot amplification explicitly**—acknowledge automation in the sample
6. **Soften "sustained momentum" claim** or provide statistical evidence for trend
7. **Add safety/chilling effects discussion** as alternative explanation for high retweet rates
8. **Clarify engagement metric sources** (sample-only vs. global retweet counts)

### Low Priority (Nice to Have)

9. Expand theoretical discussion of diaspora vs. domestic participation
10. Add hashtag variant co-occurrence analysis
11. Include sentiment analysis caveats for Nigerian English/Pidgin

---

## 7. Summary Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| **Methodological Rigor** | ⚠️ Fair | Correlation calculation questionable; bot analysis missing |
| **Theoretical Grounding** | ✅ Good | Strong literature engagement |
| **Transparency** | ✅ Good | Clear limitations and parameter choices |
| **Interpretive Validity** | ⚠️ Fair | Some claims overreach evidence |
| **Practical Relevance** | ✅ Good | Actionable recommendations |
| **Overall Quality** | ⚠️ Acceptable with Revisions | Core findings hold but require methodological corrections |

---

## 8. Conclusion

GLM's #EndSARS analysis provides valuable insights into digital activism dynamics, particularly in its theoretical framing and practical implications. However, **the correlation discrepancy (r=0.412 vs. r=0.251) is a significant methodological concern** that likely stems from using raw rather than log-transformed follower counts. This overstates the relationship between follower count and engagement.

Other issues—phase classification inconsistency, bot detection omission, and unsupported claims about "democratized amplification"—should be addressed in revision. GLM's strengths in theoretical integration, methodological transparency, and practical relevance make this a worthwhile contribution to digital activism research once these corrections are made.

**Verdict:** Revise and resubmit with correlation recalculation and bot analysis added.

---

## Reviewer Notes

This cross-review was conducted as part of the CommDAAF Red-Team workflow. Both analyses used the same dataset (endsars_sample_10k.csv), enabling direct comparison of methodological choices and findings. The correlation discrepancy was the primary focus of investigation, revealing important lessons about data transformation in social media research.

**Key Lesson:** Social media metrics (followers, likes, retweets) typically follow power-law distributions. Always:
1. Check distribution shape before correlation analysis
2. Consider log transformation for highly skewed variables
3. Report both raw and transformed analyses when distributions are extreme
4. Use non-parametric alternatives (Spearman, Kendall) when assumptions are violated

---

*Review completed: February 17, 2026*  
*Reviewer: Kimi (CommDAAF Red-Team)*
