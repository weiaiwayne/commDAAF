# CommDAAF Analysis: Chinese Digital Diplomacy TikTok Dataset
## RUN8_KIMI_ANALYSIS.md

**Analysis Date:** 2026-02-22  
**Analyst:** CommDAAF Research Agent (Kimi)  
**Validation Tier:** 🟡 Pilot (2-4 hours)  
**Data Source:** `cn_digital_diplomacy_tiktok.rda`

---

## 📋 EXECUTIVE SUMMARY

This analysis applies the **CommDAAF Critical Checks framework** to a Chinese digital diplomacy TikTok dataset containing 1,994 videos across four topics (Xinjiang, China, Taiwan, HK) plus 48,070 Xinjiang comments and People's Daily state media data.

### Key Findings:
1. **Extreme engagement disparity**: 60:1 ratio (China 5.3B vs Xinjiang 87M plays)
2. **Coordination markers detected**: 13.9% duplicate comments, high-volume commenters
3. **Temporal anomalies**: Peak/trough ratios 31:1 to 96:1 across topics
4. **State media presence**: People's Daily accounts identified with limited metadata

---

## 🚨 CRITICAL CHECKS APPLIED

### Check #1: Data Provenance
**Status:** ⚠️ FLAGGED

| Item | Finding |
|------|---------|
| **Collection Method** | Scraped data (pre-2023 TikTok API restrictions) |
| **Time Period** | 2017-2022 (clustered in 2021-2022) |
| **Missing Data** | Private accounts, deleted videos, age-restricted content |
| **Pre-processing** | Unknown filters or sampling applied |

**Warning:** TikTok API access severely restricted since 2023. This dataset likely collected via scraping tools. Data provenance documentation incomplete.

---

### Check #2: Bot/State Media Detection
**Status:** ⚠️ PARTIAL

**People's Daily State Media Data:**
- `pd` + `pd2`: 60 video entries (limited metadata)
- `pd_comments` + `pd_comments2`: 343 comments from 295 unique users
- Account verification status: Unknown

**High-Volume Creators (Potential Indicators):**
- **Xinjiang:** @kieutravel (77 videos, 17.9M plays)
- **China:** @kim_yeon_7 (24 videos, 203.8M plays)
- No obvious bot usernames detected
- State media keywords ('people', 'daily', 'official') found in account names

**High-Volume Commenters:**
| User | Comments | Topic |
|------|----------|-------|
| . | 276 | Xinjiang |
| Tik Toker | 120 | Xinjiang |
| tp22 | 53 | Xinjiang |
| Kiều Phùng | 52 | Xinjiang |

---

### Check #3: Content Type Mixing
**Status:** ✅ CLEAR

- All data is TikTok video content (homogeneous)
- Engagement metrics (plays, likes, shares) comparable across topics
- No mixed media types detected

---

### Check #4: Temporal Distribution
**Status:** ⚠️ EVENT-DRIVEN DATA

| Topic | Peak Year | % in Peak | Peak/Trough Ratio | Peak Period |
|-------|-----------|-----------|-------------------|-------------|
| Xinjiang | 2021 | 48.8% | 96:1 | May 2021 |
| China | 2022 | 44.3% | 31:1 | Mar 2022 |
| Taiwan | 2022 | 41.6% | 64:1 | Aug 2022 |
| HK | 2022 | 41.6% | 41:1 | Sep 2022 |

**Critical Flags:**
- ⚠️ All topics show peak/trough ratios >4:1 (event-driven, not baseline)
- ⚠️ May 2021 Xinjiang spike (96 videos) - H&M boycott period?
- ⚠️ 2021-2022 clustering - COVID/China tensions peak period

---

### Check #5: Metric Comparability
**Status:** ⚠️ OUTLIERS PRESENT

**Extreme Outliers Detected:**

| Topic | Max Plays | 99th Percentile | Outlier Ratio |
|-------|-----------|-----------------|---------------|
| China | 78,800,000 | 55,896,000 | 1.4x |
| Taiwan | 56,700,000 | 24,580,000 | 2.3x |
| HK | 25,600,000 | 15,678,000 | 1.6x |
| Xinjiang | 6,100,000 | 2,801,000 | 2.2x |

**Top Video per Topic:**
- **China:** @saramart_global - 78.8M plays (product/business content)
- **Taiwan:** @lesbobaristas - 56.7M plays (coffee culture)
- **HK:** @7futsal - 25.6M plays (sports content)
- **Xinjiang:** @ohayolily - 6.1M plays (travel content)

---

### Check #6: Coordinated Behavior Markers
**Status:** ⚠️ COORDINATION INDICATORS FOUND

**Xinjiang Comments Analysis (48,070 comments):**

**Duplicate Comments:**
- 1,870 unique texts appear multiple times
- 6,658 total duplicate instances (13.9% of all comments)
- Top duplicates are emoji-only comments (🥰, 👍)

**Most Duplicated Comment Texts:**
| Comment | Count | % of Total |
|---------|-------|------------|
| 🥰🥰🥰 | 300 | 0.6% |
| 🥰 | 152 | 0.3% |
| 🥰🥰🥰🥰 | 147 | 0.3% |
| 🥰🥰 | 99 | 0.2% |
| 👍👍👍 | 70 | 0.1% |

**Temporal Clustering:**
- Peak day: May 22, 2021 (1,099 comments)
- Daily spike ratio: 21.7x average
- Peak hours: 3-5 PM (suggests timezone targeting)

**Interpretation:**
- Emoji-only duplicates likely organic (TikTok culture)
- However, 13.9% duplication rate + daily spike = coordination possible
- Peak hours suggest orchestrated campaigns or timezone clustering

---

## 📊 RESEARCH QUESTION FINDINGS

### RQ1: State Media vs Organic Creators

**Finding:** State media presence confirmed but engagement comparison limited

| Metric | People's Daily | Organic Creators (Avg) |
|--------|----------------|------------------------|
| Video Count | 60 entries | 1,994 total videos |
| Comment Count | 343 | 48,070 (Xinjiang only) |
| Engagement Metrics | Not available in dataset | Variable by topic |

**Limitations:**
- People's Daily dataset lacks play counts and detailed metadata
- Cannot calculate engagement rates for direct comparison
- Account verification status unknown

**Recommendation:** Need manual review of People's Daily accounts to verify:
- Video content vs organic creators
- Engagement patterns
- Follower authenticity

---

### RQ2: Coordinated Behavior in 48K Xinjiang Comments

**Finding:** Coordination markers present but interpretation ambiguous

**Evidence FOR Coordination:**
- ✅ 13.9% exact duplicate comments
- ✅ 4 high-volume commenters (>50 comments each)
- ✅ 21.7x daily spike on May 22, 2021
- ✅ Peak activity clustered in afternoon hours (3-5 PM)

**Evidence AGAINST Coordination:**
- ⚠️ Duplicates are mostly emoji-only (organic TikTok behavior)
- ⚠️ 35,680 unique commenters (low concentration)
- ⚠️ Average 1.3 comments per user (normal distribution)

**Confidence:** MODERATE
- Statistical signatures present
- But could reflect: viral content moments, organic copy-paste culture, or coordinated campaigns
- **Need qualitative review** of comment content to distinguish

---

### RQ3: Engagement Disparity (China 5.3B vs Xinjiang 87M)

**Finding:** 60:1 engagement ratio driven by multiple factors

| Metric | China | Xinjiang | Ratio |
|--------|-------|----------|-------|
| Total Plays | 5.3B | 87M | **60.6:1** |
| Avg Plays/Video | 10.6M | 175K | **60.7:1** |
| Median Plays | 7.2M | 31K | **232:1** |
| Max Plays | 78.8M | 6.1M | **12.9:1** |
| Videos | 499 | 500 | ~1:1 |

**Potential Explanations:**

1. **Algorithm Bias** (Possible)
   - #china content may be algorithmically promoted
   - "China" is broader topic with wider appeal
   - Cannot verify without platform data

2. **Organic Interest** (Likely)
   - General China content appeals to larger global audience
   - Xinjiang is niche/human rights topic (limited appeal)
   - Travel/lifestyle content (China) vs controversial topic (Xinjiang)

3. **State Amplification** (Uncertain)
   - Pro-China accounts may coordinate promotion
   - No direct evidence in this dataset
   - Would need network analysis of sharers

4. **Content Characteristics** (Partial)
   - China topic: More entertainment/lifestyle content
   - Xinjiang topic: More documentary/news content
   - Different content types = different engagement baselines

5. **Temporal Effects** (Unlikely)
   - Both topics span 2017-2022
   - Similar temporal distributions

**Confidence:** MODERATE
- Disparity is real and substantial
- Root cause is MULTIFACTORIAL
- Cannot isolate single explanation

---

### RQ4: Top Accounts by Topic

**Xinjiang (Top 5 by Plays):**
| Rank | Account | Plays | Followers | Videos | Play/Follower |
|------|---------|-------|-----------|--------|---------------|
| 1 | @ohayolily | 6.1M | 400K | 174 | 15.2x |
| 2 | @orientalworld_go | 17.7M | 1.2M | 12 | 14.8x |
| 3 | @kieutravel | 17.9M | 255K | 77 | 70.2x |
| 4 | @rayhangul_dilimurat | 4.4M | 17K | 30 | 259x |
| 5 | @markhore121 | 3.0M | 24K | 37 | 125x |

**China (Top 5 by Plays):**
| Rank | Account | Plays | Followers | Videos | Play/Follower |
|------|---------|-------|-----------|--------|---------------|
| 1 | @saramart_global | 78.8M | 1.0M | 2 | 78.8x |
| 2 | @kim_yeon_7 | 203.8M | 3.5M | 24 | 58.2x |
| 3 | @arys555 | 158.7M | 1.9M | 9 | 83.5x |
| 4 | @chinagirls74 | 155.2M | 2.4M | 7 | 64.7x |
| 5 | @mine_ja | 106.7M | 1.3M | 9 | 82.1x |

**Taiwan (Top 5 by Plays):**
| Rank | Account | Plays | Followers | Videos | Play/Follower |
|------|---------|-------|-----------|--------|---------------|
| 1 | @lesbobaristas | 56.7M | 673K | 2 | 84.2x |
| 2 | @roman_and_sharon | 115.9M | 533K | 13 | 217x |
| 3 | @canhhoatan1996 | 53.2M | 350K | 18 | 152x |
| 4 | @leogloria | 45.5M | 565K | 3 | 80.5x |
| 5 | @kawaii_taiwan_cheer.jp | 16.4M | 95K | 5 | 172x |

**Hong Kong (Top 5 by Plays):**
| Rank | Account | Plays | Followers | Videos | Play/Follower |
|------|---------|-------|-----------|--------|---------------|
| 1 | @7futsal | 25.6M | 510K | 3 | 50.2x |
| 2 | @slavinjoshua | 29.6M | 203K | 8 | 146x |
| 3 | @lavtify | 17.0M | 92K | 7 | 185x |
| 4 | @dha_vhydha | 17.3M | 222K | 11 | 78.0x |
| 5 | @kong_football | 17.1M | 61K | 2 | 280x |

**State-Adjacent Accounts:**
- No direct state media accounts in top creators
- Travel/lifestyle creators dominate (organic content)
- Play/follower ratios suggest viral content, not just follower-driven

---

### RQ5: Temporal Spikes and Real-World Events

**Identified Spikes:**

| Topic | Peak Period | Volume | Likely Trigger |
|-------|-------------|--------|----------------|
| Xinjiang | May 2021 | 96 videos | H&M boycott (March 2021) |
| China | Mar 2022 | 31 videos | Winter Olympics fallout |
| Taiwan | Aug 2022 | 64 videos | Pelosi visit (Aug 2022) |
| HK | Sep 2022 | 41 videos | National security law enforcement |

**Validation:**
- ✅ Temporal alignment with major geopolitical events
- ✅ Event-driven patterns (not organic baseline)
- ⚠️ Need external event timeline for full validation

---

## 📋 LIMITATIONS & CAUTIONS

### Methodological Limitations:

1. **Sample Balance**
   - People's Daily data incomplete (60 entries vs 1,994 organic videos)
   - Cannot make valid statistical comparisons
   - ⚠️ **BLOCKED:** Direct state vs organic comparison invalid

2. **Metric Comparability**
   - Engagement disparities across topics not normalized
   - Follower counts vary dramatically
   - ⚠️ **WARNING:** Raw play counts not directly comparable

3. **Confounding Variables**
   - Platform algorithm effects unknown
   - Time period differences (2017-2022 spans major events)
   - Content type differences (travel vs news vs lifestyle)
   - ⚠️ **BLOCKED:** Cannot claim causation for engagement disparity

4. **Data Quality**
   - Scraped data (not official API)
   - Missing metadata (verification status, account creation dates)
   - Unknown sampling methodology
   - ⚠️ **WARNING:** Replication challenging

### Interpretation Limitations:

1. **Coordination ≠ Inauthenticity**
   - Detected patterns could be organic viral moments
   - Duplicate comments may reflect TikTok emoji culture
   - ⚠️ **DO NOT** claim "bot detection" without qualitative review

2. **State Media Ambiguity**
   - People's Daily accounts identified by name only
   - No verification status available
   - ⚠️ **BLOCKED:** Cannot definitively label state-affiliated

3. **Engagement Disparity Causes**
   - Multiple explanations possible (algorithm, organic interest, amplification)
   - Cannot isolate single cause
   - ⚠️ **WARNING:** Avoid monocausal explanations

---

## 🎯 CONFIDENCE ASSESSMENT

| Finding | Evidence | Confidence | Action Needed |
|---------|----------|------------|---------------|
| Extreme engagement disparity (60:1) | Strong statistical evidence | 🔴 High | Explain multiple causes |
| Temporal spikes align with events | Moderate correlation | 🟡 Medium | External event timeline |
| State media present in dataset | Account names suggestive | 🟡 Medium | Manual verification |
| Coordination markers in comments | Duplicate patterns exist | 🟡 Medium | Qualitative review |
| State media vs organic comparison | Insufficient data | 🔴 Low | ⚠️ Do not report |
| Bot/automated accounts | No conclusive evidence | 🔴 Low | ⚠️ Do not claim |

---

## 🔴 PUBLICATION READINESS

**Current Tier:** 🟡 **PILOT** (2-4 hours validation)

**Suitable for:**
- ✅ Committee presentation with explicit caveats
- ✅ Internal research discussion
- ✅ Grant proposal preliminary data
- ✅ Exploratory analysis

**NOT Suitable for:**
- ❌ Journal submission without upgrades
- ❌ Policy recommendations
- ❌ Public claims about coordination
- ❌ State media vs organic comparisons

**Required for 🔴 Publication Tier:**
1. **Manual verification** of top 50 accounts
2. **Qualitative coding** of duplicate comments (N=200)
3. **External event timeline** documentation
4. **Replication package** with full methodology
5. **Cross-validation** with second dataset
6. **Sensitivity analysis** on engagement metrics

---

## 📚 REPRODUCIBILITY

**Code:** `analyze_tiktok_dataset.py`  
**Data:** `cn_digital_diplomacy_tiktok.rda`  
**Framework:** CommDAAF v0.3.0  
**Checks Applied:** workflows/critical-checks.md  

**Reproduction Steps:**
```bash
python3 analyze_tiktok_dataset.py > RUN8_KIMI_ANALYSIS.md
```

---

## 📝 CITATION

If using this analysis, cite:

```
CommDAAF Research Agent (2026). Chinese Digital Diplomacy TikTok Dataset Analysis. 
Run 8 (Kimi). Pilot-tier validation. CommDAAF Framework v0.3.0.
```

---

## 🚨 FINAL RECOMMENDATIONS

1. **DO report:** Engagement disparities with multiple causal explanations
2. **DO report:** Temporal clustering with event correlation (tentative)
3. **DO report:** Coordination markers as "suggestive" not "confirmed"
4. **DO NOT report:** State media vs organic comparisons (insufficient data)
5. **DO NOT report:** Bot/automated account claims (no conclusive evidence)
6. **UPGRADE to 🔴 tier** before publication or policy claims

---

*Analysis completed using CommDAAF Critical Checks framework. For questions about methodology, refer to SKILL.md and workflows/critical-checks.md.*
