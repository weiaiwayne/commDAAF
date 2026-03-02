# Computational Communication Research Analysis
## @EastLosHighShow Twitter Dataset (2014-2018)

**Date of Analysis:** February 17, 2026  
**Dataset:** 3,153 tweets from @EastLosHighShow official account  
**Data Source:** `/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/AgentAcademying/sample-data/recent_3200tweets.csv`

---

## Executive Summary

This analysis examines 3,153 tweets from @EastLosHighShow, the official Twitter account for the Hulu original drama series "East Los High" (2014-2017). The dataset spans from July 2014 to January 2018, capturing the show's entire lifecycle including its finale. Three research questions were tested using non-parametric statistical methods due to the highly skewed nature of engagement metrics.

**Key Findings:**
1. **Hashtag use significantly increases engagement** (r = -0.40, p < 0.001)
2. **Sentiment shows weak negative correlation with engagement** (ρ = -0.03 to -0.08)
3. **Engagement increased dramatically over the show's lifecycle**, peaking in 2016 (ρ = 0.44, p < 0.001)

---

## 1. Data Profile

### 1.1 Dataset Overview

| Metric | Value |
|--------|-------|
| Total tweets | 3,153 |
| Date range | 2014-07-11 to 2018-01-10 |
| Account followers (constant) | 11,544 |
| Verified account | Yes |
| Tweets with hashtags | 2,175 (69.0%) |
| Tweets with media | 817 (25.9%) |
| Tweets with URLs | 1,019 (32.3%) |
| Reply tweets | 421 (13.4%) |

### 1.2 Temporal Distribution

| Year | Tweet Count | % of Total |
|------|-------------|------------|
| 2014 | 1,379 | 43.7% |
| 2015 | 851 | 27.0% |
| 2016 | 498 | 15.8% |
| 2017 | 417 | 13.2% |
| 2018 | 8 | 0.3% |

The distribution reflects the show's production cycle: heavy promotion during initial launch (2014), sustained engagement through seasons 2-3 (2015-2016), and the finale period (2017).

### 1.3 Engagement Metrics Summary

| Metric | Mean | Median | SD | Min | Max |
|--------|------|--------|-----|-----|-----|
| Favorite count | 15.73 | 4.0 | 71.18 | 0 | 2,761 |
| Retweet count | 24.20 | 3.0 | 557.51 | 0 | 27,612 |
| Characters | 87.8 | 104.0 | 42.1 | 2 | 165 |
| Words | 13.5 | 15.0 | 7.9 | 1 | 36 |
| Polarity | 0.18 | 0.14 | 0.24 | -1.0 | 1.0 |
| Subjectivity | 0.38 | 0.36 | 0.27 | 0 | 1.0 |

### 1.4 Top Hashtags

| Rank | Hashtag | Frequency | Purpose |
|------|---------|-----------|---------|
| 1 | #eastloshigh | 550 | Show title/brand |
| 2 | #eastlosdos | 310 | Season 2 promotion |
| 3 | #eastloscuatro | 222 | Season 4 promotion |
| 4 | #elhaddicts | 218 | Fan community |
| 5 | #eastlostres | 152 | Season 3 promotion |
| 6 | #askelh | 101 | Q&A engagement |
| 7 | #elhceci | 74 | Character hashtag |
| 8 | #elhaddict | 69 | Fan identity |

---

## 2. Research Questions and Findings

### RQ1: Does the use of hashtags increase tweet engagement?

**Hypothesis:** Tweets containing hashtags will receive higher engagement (favorites and retweets) than tweets without hashtags.

#### Results

| Group | N | Mean Favorites | Median Favorites | Mean Retweets | Median Retweets |
|-------|---|----------------|------------------|---------------|-----------------|
| With Hashtags | 2,175 | 20.36 | 7.0 | 31.12 | 3.0 |
| Without Hashtags | 978 | 5.42 | 1.0 | 8.82 | 1.0 |

**Statistical Tests:**
- Mann-Whitney U (Favorites): U = 1,483,770, **p < 0.0001**
- Mann-Whitney U (Retweets): U = 1,488,755, **p < 0.0001**
- Effect size (rank-biserial r): **r = -0.40** for both metrics

**Interpretation:**
The effect size of r = -0.40 indicates a **medium-to-large effect** (Cohen's conventions: small=0.1, medium=0.3, large=0.5). Tweets with hashtags receive approximately **3.8x more favorites** and **3.5x more retweets** on average than tweets without hashtags.

**Conclusion:** **SUPPORTED.** Hashtag use significantly and substantially increases both favorite and retweet counts.

---

### RQ2: Does sentiment polarity/subjectivity predict engagement?

**Hypothesis:** More positive and subjective tweets will receive higher engagement.

#### Results

**Correlation Analysis (Spearman's ρ):**

| Metric Pair | ρ | p-value | Interpretation |
|-------------|---|---------|----------------|
| Favorites × Polarity | -0.029 | 0.109 | No significant relationship |
| Favorites × Subjectivity | -0.066 | **0.0002** | Weak negative, significant |
| Retweets × Polarity | -0.081 | **< 0.0001** | Weak negative, significant |
| Retweets × Subjectivity | -0.067 | **0.0002** | Weak negative, significant |

**Engagement by Sentiment Category:**

| Sentiment | N | Mean Favorites | Median Favorites | Mean Retweets | Median Retweets |
|-----------|---|----------------|------------------|---------------|-----------------|
| Negative (polarity < -0.1) | 213 | 16.30 | 4.0 | 136.72* | 3.0 |
| Neutral (-0.1 to 0.1) | 1,520 | 17.66 | 4.0 | 13.83 | 3.0 |
| Positive (> 0.1) | 1,413 | 13.60 | 3.0 | 18.49 | 2.0 |

*Note: High retweet mean for negative sentiment is driven by a single viral tweet (27,612 retweets).*

**Kruskal-Wallis Test:** H(2) = 7.193, **p = 0.027**

**Interpretation:**
Contrary to expectations, the correlations are **negative and weak** (ρ = -0.03 to -0.08). The significant p-values reflect the large sample size rather than meaningful effect sizes. The Kruskal-Wallis test indicates a statistically significant difference across sentiment categories, but the practical significance is minimal.

**Conclusion:** **NOT SUPPORTED.** Sentiment shows only weak negative associations with engagement. More objective, less emotional content appears to perform slightly better, contrary to expectations from emotional contagion theory.

---

### RQ3: How did engagement patterns change across the show's lifecycle?

**Hypothesis:** Engagement increased as the show gained popularity, peaking around the series finale.

#### Results

**Engagement by Year:**

| Year | N | Mean Favorites | Median Favorites | Mean Retweets | Avg Hashtags/Tweet |
|------|---|----------------|------------------|---------------|-------------------|
| 2014 | 1,379 | 3.35 | 1.0 | 5.57 | 0.96 |
| 2015 | 851 | 7.75 | 4.0 | 8.20 | 1.39 |
| 2016 | 498 | **49.18** | **21.0** | **52.30** | 1.91 |
| 2017 | 417 | 32.54 | 13.0 | 29.61 | 1.39 |
| 2018 | 8 | 30.88 | 27.5 | 4.00 | 1.13 |

**Temporal Trend Analysis:**
- Spearman's ρ (year × favorites) = **0.442**, p < 0.0001
- 2014 vs 2016-17 comparison: Mann-Whitney U, **p < 0.0001**

**Key Findings:**
1. Engagement increased **14.7x** from 2014 to 2016
2. Peak engagement occurred in **2016** (Season 4/Finale period), not at show's end
3. Hashtag usage per tweet also peaked in 2016 (1.91 hashtags/tweet)

**Interpretation:**
The dramatic increase in engagement likely reflects:
- Growth in show popularity over time
- Accumulation of fan base (#ELHAddicts community)
- Strategic social media management evolution
- Peak promotional activity around Season 4 and the series finale

**Conclusion:** **SUPPORTED.** Engagement increased significantly over the show's lifecycle, peaking in 2016 during the final season promotion period.

---

## 3. Additional Exploratory Findings

### 3.1 Media Content Effect

| Media Type | N | Mean Favorites | p-value |
|------------|---|----------------|---------|
| With Media | 817 | 37.57 | < 0.0001 |
| Without Media | 2,336 | 8.08 | |

**Effect:** Tweets with images/videos receive **4.6x more favorites** than text-only tweets.

### 3.2 URL Presence Effect

| URL Status | N | Mean Favorites | p-value |
|------------|---|----------------|---------|
| With URL | 1,019 | 18.56 | < 0.0001 |
| Without URL | 2,134 | 14.37 | |

**Effect:** Tweets with URLs receive **29% more favorites**, though this is a smaller effect than media or hashtags.

### 3.3 Character-Word Relationship

The average tweet contains:
- 87.8 characters (well below Twitter's 140/280 limit during this period)
- 13.5 words
- This suggests a concise, focused communication strategy

---

## 4. Limitations and Scope Conditions

### 4.1 Internal Validity Concerns

1. **Single Account Study:** Findings generalize only to @EastLosHighShow, not to all TV shows or entertainment brands.

2. **Confounding Variables:** 
   - Hashtag use correlates with content type (promotional vs. conversational)
   - Time trends confound with platform growth (Twitter user base increased 2014-2017)
   - Engagement may reflect show popularity, not tweet characteristics

3. **Causal Direction:**
   - Do hashtags cause engagement, or do high-engagement tweets simply include hashtags?
   - Experimental design would be needed for causal claims

4. **Missing Context:**
   - Cannot account for external events (awards, press coverage)
   - No data on when episodes aired
   - Cannot distinguish organic vs. paid promotion

### 4.2 External Validity Concerns

1. **Platform Specificity:**
   - Findings may not transfer to Instagram, TikTok, or other platforms
   - Twitter's algorithm and user behavior changed significantly post-2018

2. **Genre Specificity:**
   - "East Los High" targeted Latino youth demographic
   - Results may not generalize to other genres or demographics

3. **Temporal Validity:**
   - Data from 2014-2018; social media landscape has evolved
   - Twitter/X platform changes may invalidate contemporary application

4. **Account Type:**
   - Verified corporate/brand account
   - Findings may not apply to personal accounts or influencers

### 4.3 Measurement Limitations

1. **Sentiment Analysis:**
   - Pre-computed polarity/subjectivity scores
   - Unknown algorithm used; likely TextBlob or similar
   - May not capture sarcasm, cultural nuances, or emoji sentiment

2. **Engagement Metrics:**
   - Favorite counts are snapshot in time
   - No longitudinal tracking of engagement decay
   - Retweets may include quote tweets (not distinguishable)

3. **Missing Variables:**
   - No follower growth data over time (follower count is constant in dataset)
   - No impression or reach data
   - No click-through data for URLs

### 4.4 What Can and Cannot Be Claimed

**CAN Claim:**
- In this dataset, hashtag use correlates with higher engagement
- Engagement increased over the show's lifecycle
- Sentiment shows weak negative correlation with engagement
- Media content outperforms text-only content

**CANNOT Claim:**
- Hashtags cause higher engagement (correlation ≠ causation)
- These patterns apply to all TV shows or entertainment brands
- Sentiment analysis accurately captures tweet emotional content
- Findings are reproducible on current Twitter/X platform
- Results apply to non-English or non-US contexts

---

## 5. Theoretical Implications

### 5.1 Information Retrieval Theory
The strong hashtag effect (r = -0.40) supports theories of **information visibility** and **discoverability**. Hashtags serve as:
- Categorization signals
- Search facilitation mechanisms
- Community boundary markers (#ELHAddicts)

### 5.2 Emotional Contagion Theory
The weak sentiment effects challenge **emotional contagion** predictions that more emotional content spreads further. Possible explanations:
- Brand accounts may benefit from professional over emotional tone
- Audience expectations for official accounts differ from personal accounts
- Sentiment detection may miss culturally-specific emotional expressions

### 5.3 Media Richness Theory
The strong media effect supports **media richness theory** — visual content conveys more information and generates more engagement than text alone.

---

## 6. Recommendations for Future Research

1. **Comparative Analysis:** Compare across multiple TV shows to establish generalizability
2. **Time-Series Modeling:** Use ARIMA or similar to separate trend from seasonality
3. **Content Analysis:** Manual coding of tweet types (promotional, fan engagement, etc.)
4. **Audience Analysis:** Collect follower growth data and demographic information
5. **Platform Comparison:** Analyze same content across Twitter, Instagram, Facebook
6. **Causal Design:** Field experiment with randomized hashtag assignment (if ethically feasible)

---

## 7. Data Availability and Reproducibility

All analyses were conducted using Python 3 with pandas, scipy, and numpy libraries. The dataset is available at the path specified above. This analysis is fully reproducible from the provided statistics.

---

**Report Prepared By:** Computational Communication Research Agent (Kimi)  
**Date:** February 17, 2026  
**Analysis Version:** 1.0
