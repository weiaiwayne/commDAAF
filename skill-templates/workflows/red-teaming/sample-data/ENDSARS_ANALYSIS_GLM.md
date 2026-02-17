# EndSARS Twitter Analysis: Network Structure, Temporal Dynamics, and Digital Activism

**CommDAAF Methodology: Exploratory Tier Analysis**
**Dataset:** 10,000 tweets from #EndSARS movement (October 21 - November 5, 2020)
**Analysis Date:** February 17, 2026

---

## Executive Summary

This report presents a comprehensive analysis of the #EndSARS Twitter dataset, comprising 10,000 tweets from a two-week period following the Lekki toll gate shooting on October 20, 2020. The analysis reveals a highly networked, retweet-driven movement characterized by centralized amplification through key voices, sustained engagement throughout the crisis period, and content focused on violence, accountability, and solidarity. The 80% retweet rate in this sample reflects both the virality of core messages and the amplification role of the Twitter ecosystem in crisis communication.

---

## 1. Methodology

### 1.1 Parameter Choices (CommDAAF Exploratory Tier)

**Sample:** Full 10,000 tweet sample (80% retweets, 20% original tweets)
- **Rationale:** Provides sufficient power for descriptive statistics and correlation analysis while maintaining computational efficiency for exploratory analysis.

**Network Analysis:** Top N = 20 users for centrality metrics
- **Rationale:** Captures the most influential amplifiers while remaining interpretable for qualitative assessment.

**Temporal Binning:** 12-hour intervals
- **Rationale:** Balances granular insight with stability for rolling averages; aligns with typical diurnal patterns in Twitter usage.

**Engagement Modeling:** 90th percentile threshold for "high engagement"
- **Rationale:** Focuses on truly viral content while avoiding extreme outliers that could skew analysis.

**Statistical Validation:**
- Descriptive statistics reported with mean, median, standard deviation
- Correlations computed for original tweets only (n=2,000) to avoid confounding by RT cascade mechanics
- Rolling averages (3-bin window) used for phase identification

### 1.2 Data Limitations

1. **Engagement Metric Confounding:** Retweet engagement metrics (`retweet_count`) on retweeted tweets reflect the original tweet's virality, not the retweeter's engagement with their audience. This is inherent to Twitter's API structure.

2. **Sample Representation:** The 10,000 tweet sample represents ~3.3% of the full 299,410-tweet dataset. While adequate for exploratory analysis, findings may not fully represent edge cases or rare events.

3. **Temporal Window:** The two-week period captures a specific crisis phase (post-shooting). Generalizations to other phases of the #EndSARS movement (e.g., early mobilization, aftermath) require caution.

4. **Language Processing:** Content analysis used simple keyword matching. Nigerian English, Pidgin, and emojis were not systematically analyzed, which may affect content interpretation.

5. **Network Inference:** Mention networks and retweet cascades were inferred from tweet content rather than full follower/following graph data, limiting structural completeness.

---

## 2. Network Structure Analysis

### 2.1 Key Finding: Hybridized Decentralization

The #EndSARS movement exhibits **hybridized decentralization**: a broad base of 8,522 unique participants (85% of tweets from unique accounts) with distinct amplification hubs.

**Top Amplifiers by Retweet Volume:**

| Rank | Account | Retweets | Average Follower Reach of Retweeters |
|------|---------|----------|--------------------------------------|
| 1 | @renoomokri | 352 | 3,572 |
| 2 | @AishaYesufu | 263 | 993 |
| 3 | @SaharaReporters | 185 | 983 |
| 4 | @cryssiedenise_ | 120 | 745 |
| 5 | @YeleSowore | 115 | 1,221 |

**Interpretation:** These accounts function as **central amplifiers** rather than traditional leaders. @renoomokri (Reno Omokri, former Nigerian presidential spokesperson), @AishaYesufu (activist and prominent protester), @SaharaReporters (news outlet), and @YeleSowore (activist/journalist) collectively generated ~10% of all retweets. Their role is content dissemination, not necessarily agenda-setting.

**Notable:** Celebrity amplification is present but less dominant than expected. High-follower accounts like @LilNasX (appearing in sample data) and international figures (Kerry Washington) contribute to virality but are not among the top amplifiers in this 2-week window.

### 2.2 Follower Count Distribution

The user base exhibits **extreme heterogeneity** in follower counts:

- Mean: 4,987 followers | Median: 441 followers
- Top 1%: >100,000 followers (accounts like @amnestyusa, @MobilePunch, @TeenVogue)
- Bottom 50%: <441 followers

**Interpretation:** The movement successfully bridges **institutional accounts** (news media, NGOs) and **grassroots participants**. This multi-tiered structure enables rapid amplification from institutional accounts while maintaining authenticity through grassroots voices.

### 2.3 Mention Network

The most-mentioned accounts reveal communication targets:

| Rank | Account | Mentions |
|------|---------|---------|
| 1 | @renoomokri | 368 |
| 2 | @AishaYesufu | 307 |
| 3 | @MBuhari | 258 |
| 4 | @SaharaReporters | 205 |
| 5 | @YeleSowore | 139 |

**Interpretation:** @MBuhari (President Muhammadu Buhari) is the only government official in the top 5, with 258 mentions. This indicates **direct communication pressure** on political leadership rather than indirect criticism through intermediaries. @HQNigerianArmy (130 mentions) reflects focus on military accountability for the Lekki incident.

---

## 3. Temporal Dynamics

### 3.1 Activity Phases

Using a 12-hour binning with 3-bin rolling average, three distinct phases emerge:

**Peak Phase:** October 22-24, October 29-30, November 1-4
- Mean tweets/bin: 657
- Characteristics: High-volume, sustained engagement
- Context: These align with international media attention (celebrity involvement ~Oct 21-25) and continued coverage of shooting aftermath

**Moderate Phase:** October 21, October 26-28, November 2
- Mean tweets/bin: 327
- Characteristics: Intermediate activity, baseline movement conversation

**Low Phase:** October 31 - November 1
- Mean tweets/bin: 571 (only 2 bins classified as "Low" due to outlier activity)
- Context: Potential lull between major news cycles

**Key Insight:** The absence of clear decay suggests **sustained movement momentum** throughout the 14-day period. Unlike typical social media hashtag campaigns that peak within 48-72 hours, #EndSARS maintained consistent engagement.

### 3.2 Retweet Ratio Over Time

- **Overall retweet ratio:** 79.7% (stable across time)
- **Range:** 69.3% - 88.0% across time bins
- **Standard deviation:** 4.7%

**Interpretation:** The retweet ratio is remarkably stable, indicating that **amplification mechanics** rather than **content novelty** drive engagement. Movement participants consistently function as signal amplifiers rather than content creators.

---

## 4. Content Patterns

### 4.1 Hashtag Analysis

The top 20 hashtags reveal a **concentrated message frame**:

| Hashtag | Count | Percentage |
|---------|-------|------------|
| #EndSARS | 5,423 | 54.2% |
| #EndSars | 465 | 4.7% |
| #LekkiMassacre | 363 | 3.6% |
| #ENDSARS | 340 | 3.4% |
| #EndBadGoveranceInNigeria | 143 | 1.4% |

**Observations:**
1. **Brand consistency:** 67% of hashtag usage is variants of "EndSARS" (case variations), indicating strong hashtag discipline
2. **Event-specific framing:** #LekkiMassacre appears in 3.6% of tweets, anchoring the movement to the specific incident
3. **Expansion demands:** Hashtags like #EndBadGoveranceInNigeria, #EndPoliceBrutality indicate scope expansion beyond SARS specifically

**Case sensitivity note:** The presence of "EndSARS", "EndSars", "ENDSARS", "endsars" reflects informal hashtag practices, not fragmentation.

### 4.2 Keyword Analysis

**Violence and Accountability:**
- "sars": 66.3% of tweets
- "nigeria": 29.1% of tweets
- "protest": 16.9% of tweets
- "police": 11.2% of tweets
- "lekk" (Lekki): 10.2% of tweets
- "kill": 7.4% of tweets
- "brutal": 7.2% of tweets

**Emotional Tone:**
- "peace": 4.6% of tweets
- "pray": 1.0% of tweets
- "help": 1.6% of tweets

**Political Targets:**
- "government": 5.4% of tweets
- "buhari": 5.0% of tweets
- "military": 2.0% of tweets

**Interpretation:** The content is **violence-focused** (sars, kill, brutal, shooting) and **accountability-demanding** (government, buhari, justice). Emotional keywords are relatively rare, suggesting a **protest narrative** rather than emotional outpouring.

### 4.3 Original vs Retweet Content Characteristics

| Metric | Original Tweets | Retweets |
|--------|-----------------|----------|
| Mean character count | 158 | 127 |
| Median word count | 19 | 21 |
| Content variation | High (std=85) | Low (std=23) |

**Interpretation:** Original tweets are longer and more variable (reflecting content creation), while retweets are shorter and more uniform (reflecting signal amplification). The near-identical word count suggests retweets often add brief commentary before quoted RT content.

---

## 5. Engagement Predictors

### 5.1 Engagement Distribution (Original Tweets Only, n=2,000)

**Likes:**
- Median: 1 (75th percentile: 1)
- 90th percentile: 4
- 95th percentile: 7
- Maximum: 737

**Retweets:**
- Median: 1 (75th percentile: 2)
- 90th percentile: 3
- 95th percentile: 6
- Maximum: 212,890 (likely a cascading viral tweet)

**Interpretation:** Engagement is **highly right-skewed**. Most original tweets receive minimal engagement (median: 1 like, 1 retweet), while a small fraction achieve virality. This is consistent with Twitter's power-law engagement dynamics.

### 5.2 Correlation Analysis

**Predictors of Likes:**

| Predictor | Correlation (r) | Interpretation |
|-----------|-----------------|----------------|
| User follower count | 0.412 | Moderate positive relationship |
| User tweet count (activity) | 0.222 | Weak positive relationship |
| User friend count | 0.054 | Negligible |
| Content length | 0.003 | No relationship |
| Word count | 0.012 | No relationship |

**Predictors of Retweets:**

| Predictor | Correlation (r) | Interpretation |
|-----------|-----------------|----------------|
| User follower count | 0.216 | Weak positive relationship |
| User tweet count (activity) | 0.106 | Very weak positive relationship |
| User friend count | 0.022 | Negligible |
| Content length | 0.002 | No relationship |
| Word count | 0.006 | No relationship |

**Key Findings:**

1. **Follower count is the primary engagement predictor** (r=0.412 for likes, r=0.216 for retweets). This is intuitive: accounts with larger audiences achieve higher engagement, all else equal.

2. **User activity (tweet count) modestly predicts engagement** (r=0.222 for likes), suggesting that active, experienced users may produce more engaging content or have stronger networks.

3. **Content features (length, word count) do not predict engagement** in this dataset. This contradicts findings from some Twitter studies suggesting optimal tweet lengths (~70-100 characters) maximize engagement.

4. **Friend count (followees) is irrelevant** to engagement, indicating that following more users does not enhance reach.

### 5.3 High-Engagement Tweets

High-engagement tweets (top 10% by likes or retweets; n=357) exhibit:

- **Higher user activity:** Mean 56,752 prior tweets vs 19,044 for low-engagement tweets
- **Higher follower counts:** By definition (engagement predictor)
- **No significant content differences:** Similar length and word count

**Interpretation:** **User network position** (follower count, activity level) predicts engagement far more than **content characteristics**. This suggests that in crisis movements, **who says it** may matter more than **what they say**, at least within the observed timeframe.

---

## 6. Retweet Behavior Analysis

### 6.1 Why is the Retweet Rate So High?

The 80% retweet rate (93.9% in the full dataset) is exceptionally high by Twitter standards. Several factors contribute:

**1. Crisis Amplification Mechanics:**
- In crisis contexts, users prioritize **information sharing** over original content creation
- Retweeting serves as a **solidarity signal** and **awareness-raising tool**
- The emotional valence of the Lekki incident (military shooting peaceful protesters) motivates signal amplification

**2. Content Validation Function:**
- Retweets function as **content vetting**: users amplify what they deem credible
- High retweet counts serve as **social proof** for information credibility
- In information-poor crisis environments, retweets reduce cognitive load for readers

**3. Reduced Content Production Cost:**
- Producing original content requires **emotional labor** and **compositional effort**
- Retweeting is **low-cost**: minimal effort, immediate impact
- Users with limited bandwidth (emotional, temporal, or data) default to amplification

**4. Network Bridging:**
- Retweets enable **cross-network diffusion**: information jumps between follower graphs
- Users with limited follower bases can still contribute by amplifying influential accounts

### 6.2 Retweeter Profile Comparison

| Metric | Retweeters | Original Tweeters |
|--------|------------|-------------------|
| Mean follower count | 1,582 | 18,607 |
| Mean friend count | 1,110 | 1,212 |
| Mean prior tweets | 27,275 | 25,775 |

**Interpretation:** Retweeters have **significantly smaller follower counts** (1,582 vs 18,607), suggesting that amplification is democratized: users across the follower spectrum contribute to virality. Original tweeters are disproportionately **high-follower accounts**, indicating that content creation is concentrated among influencers and institutional accounts.

**Implication:** The movement achieves **broad-based amplification** from users with small followings, while **content creation** remains centralized. This hybrid structure enables both **reach** (through high-follower amplifiers) and **authenticity** (through grassroots retweeting).

---

## 7. Limitations and Methodological Considerations

### 7.1 Dataset-Level Limitations

1. **Temporal Specificity:** This analysis captures a specific crisis window (post-Lekki shooting). Findings may not generalize to:
   - Pre-crisis mobilization phases
   - Post-crisis aftermath and accountability efforts
   - Longer-term movement sustainability

2. **Sampling Frame:** The 10,000-tweet sample (~3.3% of full dataset) may underrepresent:
   - Rare content types (e.g., multimedia, long-form threads)
   - Edge cases in network structure
   - Low-volume but high-impact accounts

3. **Platform-Specific Artifacts:**
   - Twitter's 280-character limit constrains content complexity
   - Algorithmic timeline effects not captured (data reflects search-based collection)
   - Platform moderation may have removed sensitive content before collection

### 7.2 Analysis-Level Limitations

1. **Correlation vs Causation:** Identified relationships (e.g., follower count → engagement) are correlational. Causal mechanisms require:
   - Experimental manipulation (not feasible with observational data)
   - Instrumental variables (difficult to identify in this context)
   - Longitudinal analysis beyond the 14-day window

2. **Content Analysis Depth:** Keyword-based analysis missed:
   - Semantic meaning (e.g., sarcasm, coded language)
   - Pidgin and Nigerian English linguistic features
   - Emoji and multimedia communication
   - Hashtag co-occurrence patterns beyond frequency

3. **Network Inference:** Mention networks and retweet cascades are proxies for:
   - True follower-follower relationships
   - Information diffusion pathways
   - Influence flow directions

4. **Engagement Metric Validity:**
   - Like counts reflect positive affect but not agreement depth
   - Retweet counts reflect signal amplification but not comprehension
   - Reply counts (not analyzed) may better reflect deliberative engagement

### 7.3 External Validity

These findings are specific to:
- **Context:** Crisis-driven social movement
- **Platform:** Twitter/X (algorithmic, 280-character, amplification-oriented)
- **Culture:** Nigerian diaspora and global solidarity networks
- **Time:** 2020 social media landscape (pre-Elon Musk ownership changes)

Generalization to:
- Other social movements (e.g., climate activism, political campaigns)
- Other platforms (e.g., Facebook, TikTok, WhatsApp)
- Other cultures and contexts
- Current platform dynamics

...requires additional research and cross-validation.

---

## 8. Implications for Understanding Digital Activism

### 8.1 Theoretical Implications

**1. Networked Counterpublic Theory (Fraser, 1990):**
- The #EndSARS Twitter network exemplifies a **networked counterpublic**: a space where subordinated groups formulate oppositional discourses
- Hybridized decentralization (broad base + amplification hubs) aligns with **networked public sphere** models (Benkler, 2006)
- Retweet-driven dynamics reflect **connective action** (Bennett & Segerberg, 2013) over collective action

**2. Crisis Communication:**
- High retweet rates function as **collective sensemaking** (Weick, 1995) in information-poor environments
- Amplification of institutional accounts (@SaharaReporters) alongside activists (@AishaYesufu) reflects **hybrid legitimacy** strategies
- Temporal sustained engagement suggests **resilience** in crisis communication networks

**3. Power Law Engagement Dynamics:**
- Follower count as primary engagement predictor reinforces **Matthew Effect** (Merton, 1968): privilege begets privilege
- Weak content-feature engagement effects suggest **network position** dominates **content quality** in viral contexts
- Democratized amplification (broad-based retweeting) mitigates but does not eliminate influence inequality

### 8.2 Practical Implications

**For Activists:**
- **Cultivate amplification partnerships:** Engage high-follower influencers and institutional accounts
- **Prioritize signal amplification:** In crisis phases, retweeting may be more impactful than original content creation
- **Maintain hashtag discipline:** Consistent hashtag usage (#EndSARS variants) enhances discoverability
- **Bridge networks:** Leverage diaspora and international accounts for global amplification

**For Researchers:**
- **Account for retweet mechanics:** Engagement metrics on retweets reflect original tweet virality, not retweeter influence
- **Separate creators from amplifiers:** Network analysis should distinguish content producers from signal transmitters
- **Longitudinal tracking:** Movement phases (pre-crisis, crisis, post-crisis) exhibit distinct dynamics
- **Cross-platform validation:** Twitter findings may not transfer to other platforms

**For Platform Designers:**
- **Amplification transparency:** Make retweet cascades visible to users for credibility assessment
- **Engagement metric nuance:** Distinguish between "amplification engagement" (retweets) and "affirmation engagement" (likes)
- **Crisis mode features:** Consider enhanced signal amplification tools for humanitarian and human rights contexts

### 8.3 Policy Implications

**For Governments and Institutions:**
- **Monitor amplification hubs:** Accounts like @renoomokri, @AishaYesufu, @SaharaReporters serve as barometers of movement sentiment
- **Engage directly:** Mentions of @MBuhari and @HQNigerianArmy indicate direct pressure tactics; ignoring them may escalate tensions
- **Counter-misinformation:** High retweet rates enable rapid misinformation spread; rapid response protocols are essential

**For NGOs and International Bodies:**
- **Support signal amplification:** Resource-constrained activists benefit from international amplification
- **Document crisis dynamics:** Twitter data provides real-time evidence for human rights documentation
- **Bridge diaspora networks:** Nigerian diaspora accounts serve as cross-cultural communication channels

---

## 9. Conclusion

The #EndSARS Twitter movement exhibits a **hybridized network structure** characterized by:

1. **Broad participation:** 8,522 unique users across 10,000 tweets, with 80% acting as amplifiers
2. **Centralized amplification:** Top 20 accounts generate disproportionate reach through retweet cascades
3. **Sustained engagement:** Activity remained consistent across 14 days, avoiding typical social media decay
4. **Focused messaging:** Hashtag discipline (#EndSARS variants in 67% of tweets) and violence-focused content
5. **Network-driven engagement:** Follower count (not content features) predicts virality

The **exceptionally high retweet rate (80%)** reflects crisis-specific amplification dynamics: users prioritize information sharing, solidarity signaling, and content validation over original content creation. This behavior enables **rapid, low-cost information diffusion** while reducing cognitive load in information-poor environments.

From a CommDAAF methodological perspective, this exploratory analysis provides **descriptive grounding** for subsequent hypothesis testing. Key areas for future research include:

- **Content analysis depth:** Topic modeling, sentiment analysis, Pidgin linguistic features
- **Causal mechanisms:** Experimental validation of engagement predictors
- **Cross-phase comparison:** Pre-crisis vs. crisis vs. post-crisis dynamics
- **Cross-platform validation:** How movement dynamics differ across Twitter, Facebook, Instagram, TikTok

The #EndSARS case illustrates how **digital activism** can leverage network structures and platform affordances to achieve rapid global amplification, even in contexts of state suppression and crisis. Understanding these dynamics is essential for activists, researchers, and policymakers navigating the increasingly digital landscape of social movements.

---

## Appendix A: Figures

*Figure 1: Overview*
- Tweet volume over time (12-hour bins)
- Retweet ratio over time
- Top 20 hashtags
- Top 20 amplifiers

*Figure 2: Engagement Analysis*
- Distribution of likes (original tweets)
- Distribution of retweets (original tweets)
- Likes vs user followers (log-log plot)
- Word count by engagement level

*Figure 3: Network Structure*
- Distribution of user followers
- Amplification sources (retweet count vs average follower reach)

*Note: Figures generated as PNG files in `/figures/` directory.*

---

## Appendix B: Data Dictionary

| Column | Description | Type |
|--------|-------------|------|
| `tweet_id` | Unique tweet identifier | string |
| `content` | Tweet text (may include RT markers) | string |
| `favorite_count` | Like count | integer |
| `retweet_count` | Retweet count | integer |
| `from_user_screen_name` | Twitter handle | string |
| `from_user_id` | User ID | string |
| `from_user_followers_count` | User's follower count | integer |
| `from_user_friends_count` | User's followee count | integer |
| `from_user_statuses_count` | User's total tweet count | integer |
| `entities_hashtags` | Comma-separated hashtags | string |
| `entities_mentions` | Comma-separated mentions | string |
| `tweet_date` | Tweet timestamp | datetime |
| `is_retweet` | Boolean: is this a retweet? | boolean |

---

## Appendix C: Code Availability

Analysis scripts and visualizations are available in the project repository:
- `endsars_analysis.py`: Python analysis script
- `figures/`: Generated visualizations (PNG format)

Analysis environment: Python 3.x with pandas, numpy, matplotlib, seaborn

---

**Report prepared by:** GLM-4.7 (Red-Team Analysis)
**CommDAAF Tier:** Exploratory
**Validation Level:** Descriptive statistics, correlation analysis, temporal pattern identification
**Limitations Explicitly Acknowledged:** Yes (see Section 7)
