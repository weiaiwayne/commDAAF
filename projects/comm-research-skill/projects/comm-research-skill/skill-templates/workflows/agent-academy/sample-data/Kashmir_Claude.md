# Kashmir Dataset Analysis Report
**Analyst:** Claude (Anthropic)  
**Date:** 2026-02-19  
**Dataset:** KashmirWithModi20190801to20200801.csv

---

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| Total tweets | 99,216 |
| Unique authors | 44,265 |
| Date range | 2019-08-03 to 2020-07-30 |
| Languages | English (49.8%), Hindi (39.8%), Undetermined (5.9%), others |
| Primary event | Article 370 revocation (August 5, 2019) |

### Column Structure
18 columns including: tweet ID, language, timestamp, author ID, repost information, source app, text content, engagement metrics (retweet/reply/like/quote counts), mentions, hashtags, URLs.

---

## 2. Research Questions

### RQ1: Coordination Detection
*Is there evidence of coordinated inauthentic behavior (CIB) in this dataset? What are the indicators?*

### RQ2: Temporal Dynamics  
*How does posting activity relate to key political events? Are there anomalous temporal patterns suggesting organized campaigns?*

### RQ3: Discourse Homogeneity
*What is the diversity of discourse? Is there evidence of message amplification through repeated identical content?*

---

## 3. Key Findings

### 3.1 STRONG COORDINATION INDICATORS DETECTED

#### A. Extremely Low Text Uniqueness (26.8%)
- **73.2% of all content is duplicated text**
- Only 26,626 unique normalized texts across 99,216 tweets
- After removing RT prefixes, mentions, and URLs, most tweets are copies of each other

#### B. Mass Copy-Paste Campaigns
Top duplicated messages (each posted by thousands of unique accounts):

| Copies | Unique Authors | Message |
|--------|----------------|---------|
| 2,676 | 2,676 | "Thank you Kashmiri brothers and sisters for trending #KashmirWithModi even without the internet" |
| 1,770 | 1,770 | "Wave of celebration all across Ladakh..." |
| 1,767 | 1,766 | "1 smiling 'Kashmiri woman' put up by Vijay Goel is actually a tourist..." |

**Critical observation:** The 1:1 ratio of copies to unique authors indicates coordinated copy-paste campaigns—many accounts posting identical messages exactly once, suggesting orchestration.

#### C. Posting Burst Detection
- **106 instances** of 10+ accounts posting identical text within 5-minute windows
- Multiple bursts occurring around key news moments (August 7-8, 2019)

#### D. Suspicious Account Behaviors
- 41 accounts posted 5+ times with <30% unique content
- 463 accounts with 3+ posts received zero engagement
- 19 accounts posted >100 times during the period
- Top poster: 445 tweets in 28 days (15.89/day), 0% retweets (unusual for organic behavior)

### 3.2 TEMPORAL PATTERNS

#### Event-Driven Activity Spike
| Date | Posts | Event Context |
|------|-------|---------------|
| Aug 8, 2019 | 33,442 | Post-announcement amplification |
| Aug 9, 2019 | 19,699 | Continued campaign |
| Aug 10, 2019 | 7,886 | Declining |

**76% of all posts occurred in the first week after Article 370 revocation.**

#### Hourly Distribution (UTC)
Peak hours: 12:00-17:00 UTC (17:30-22:30 IST)
- Consistent with Indian evening posting patterns
- Sharp drop-off after 18:00 UTC suggests limited geographic diversity

#### Day of Week
Thursday (Aug 8, 2019) dominates with 36,829 posts (37% of dataset)

### 3.3 DISCOURSE ANALYSIS

#### Hashtag Dominance
| Hashtag | Count | % of Dataset |
|---------|-------|--------------|
| #KashmirWithModi | 55,674 | 56.1% |
| #KashmirWelcomesChange | 11,845 | 11.9% |
| #Kashmir | 5,767 | 5.8% |
| #Article370 | 3,406 | 3.4% |

#### Extreme Sentiment Imbalance
| Stance | Posts | Ratio |
|--------|-------|-------|
| Pro-government | 67,325 | **107:1** |
| Critical | 629 | - |
| Neutral | 31,262 | - |

**This 107:1 pro-government to critical ratio is highly anomalous for a controversial political event.**

#### Most Mentioned Accounts
1. @narendramodi (10,681 mentions)
2. @ashutosh83B (2,679)
3. @kapsology (2,679)
4. @AmitShah (2,159)
5. @ImranKhanPTI (2,110)

### 3.4 ENGAGEMENT PATTERNS

#### Low Organic Engagement
- Mean retweet count: 260 (heavily skewed by viral content)
- Median like count: 0
- 64% of posts are retweets

#### Engagement by Stance (Original Posts Only)
| Stance | Avg Retweets | Avg Likes |
|--------|--------------|-----------|
| Pro-govt | 1.97 | 7.39 |
| Neutral | 1.32 | 2.27 |
| Critical | N/A | N/A |

### 3.5 PLATFORM SOURCE ANALYSIS

#### Dominant Sources
| Source | Posts | % |
|--------|-------|---|
| Twitter for Android | 73,917 | 74.5% |
| Twitter Web App | 12,873 | 13.0% |
| Twitter for iPhone | 10,724 | 10.8% |

#### Potential Bot Sources Detected
- IFTTT (184 posts)
- "Social6565", "Social999", etc. (automated tools, ~270 posts)
- Various named bots: "RT BOT Adyaveer", "Tamil_BOT", etc.

#### Source Text Uniqueness
| Source | Uniqueness Ratio |
|--------|------------------|
| Twitter for Android | 25.9% |
| Twitter Web App | 47.9% |
| Social6565 | 20.2% |
| IFTTT | 98.4% |

**Android posts showing only 25.9% unique content suggests widespread copy-paste behavior.**

---

## 4. Coordination Assessment

### Evidence Summary

| Indicator | Finding | Severity |
|-----------|---------|----------|
| Text duplication | 73.2% duplicate content | **HIGH** |
| Copy-paste campaigns | 2,676 accounts posting identical text | **HIGH** |
| Temporal bursts | 106 coordinated posting bursts | **HIGH** |
| Sentiment homogeneity | 107:1 pro-govt ratio | **HIGH** |
| Account behavior | High-velocity, low-uniqueness accounts | **MODERATE** |
| Bot sources | ~500 posts from automated tools | **LOW** |

### Conclusion
**STRONG EVIDENCE OF COORDINATED AMPLIFICATION**

This dataset exhibits multiple hallmarks of coordinated inauthentic behavior:
1. Mass deployment of identical messages across thousands of accounts
2. Extreme sentiment uniformity unusual for controversial political events
3. Temporal clustering around specific news moments
4. Low text diversity despite high account diversity

---

## 5. Methodological Notes

### Analytical Choices
1. **Text normalization:** Removed RT prefixes, @mentions, and URLs before comparing content to detect true duplicates vs. retweets
2. **Stance classification:** Simple keyword matching (pro-govt keywords vs. critical keywords). Limitations: May misclassify nuanced content
3. **Burst detection:** 10+ posts of identical text within 5-minute window as threshold
4. **Account age estimation:** Used Twitter Snowflake ID decoding (may have ~1 day margin of error)

### Limitations
1. **No ground truth:** Cannot definitively distinguish coordinated campaigns from organic viral spread
2. **Selection bias:** Dataset may over-represent certain hashtags due to collection methodology
3. **Missing data:** No follower counts, account metadata, or network graph data
4. **Language barriers:** Hindi content (40%) not fully analyzed for semantic patterns
5. **Retweet ambiguity:** High retweet % (64%) makes original content analysis more limited

### What This Analysis CANNOT Determine
- Attribution (who organized campaigns)
- Whether accounts are bots vs. humans copying text
- Authenticity of individual accounts
- Whether this represents astroturfing vs. genuine grassroots coordination

---

## 6. Recommendations for Further Analysis

1. **Network analysis:** Build mention/retweet graphs to identify coordinated clusters
2. **Account metadata:** Obtain follower counts, account ages, bio information
3. **Semantic similarity:** Use embeddings to detect near-duplicates and paraphrases
4. **Cross-platform:** Check if same campaigns appear on other platforms
5. **Comparative baseline:** Analyze similar events to establish "normal" duplication rates

---

## Appendix: Code Availability

Analysis performed using Python 3.12 with pandas and numpy. All code available upon request.

**Data hash (for reproducibility):** SHA256 of source CSV should be verified before replication.
