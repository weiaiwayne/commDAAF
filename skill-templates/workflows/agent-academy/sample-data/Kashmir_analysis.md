# Kashmir-Modi Political Communication Analysis

**Dataset:** KashmirWithModi20190801to20200801.csv  
**Analysis Date:** 2026-02-19  
**Methodology:** CommDAAF (Communication Data Analysis & Annotation Framework)  
**Context:** Twitter discourse around the revocation of Article 370 (August 5, 2019)

---

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| Total Tweets | 99,216 |
| Unique Authors | ~56,000 (estimated from distribution) |
| Date Range | Aug 3, 2019 – Jul 30, 2020 |
| Primary Language | English (49.8%), Hindi (39.8%) |
| Peak Day | **August 8, 2019** (33,442 tweets) |

### Data Structure
- 18 columns including: id, text, created_at, author_id, retweet_count, like_count, hashtags, mentions
- Mixed repost_id types (DtypeWarning noted - potential data quality issue for CommDAAF consideration)

---

## 2. Research Questions

Based on Wayne's research areas in **Political Communication**, **Coordinated Behavior**, and **Platform Studies**:

### RQ1: Hashtag Campaign Orchestration (Coordinated Behavior)
**How was the #KashmirWithModi hashtag campaign orchestrated, and what indicators of coordinated amplification exist?**

*Justification:* The hashtag appears manufactured to project domestic support immediately following a controversial political action. The ironic framing ("Kashmiri Brothers and Sisters trending #KashmirWithModi even without the Internet") suggests awareness of information asymmetry.

### RQ2: Media-Political Symbiosis (Political Communication)
**What role did pro-government media outlets play in amplifying official narratives, and how did this interact with grassroots/astroturf participation?**

*Justification:* @TimesNow appears in 1,552 mentions, with their content heavily retweeted. Understanding the media-amplification pipeline is crucial for studying political communication in hybrid media systems.

### RQ3: Temporal Dynamics of Manufactured Consent (Platform Studies)
**What do the extreme temporal patterns (71K tweets in first week → 39 tweets in January 2020) reveal about campaign sustainability and platform affordances?**

*Justification:* The 84.8% week-over-week decay rate suggests either campaign termination or hashtag lifecycle exhaustion—important for understanding platform-based political mobilization.

---

## 3. Key Findings

### 3.1 Temporal Dynamics

| Period | Tweet Volume | % of Peak Week |
|--------|-------------|----------------|
| Aug 7-14, 2019 | 71,284 | 100% |
| Aug 15-22, 2019 | 10,849 | 15.2% |
| September 2019 | 7,853 | 11.0% |
| January 2020 | 39 | 0.05% |
| July 2020 | 9 | 0.01% |

**Critical Observation:** The hashtag surged **2 days after** Article 370 revocation (Aug 5), peaking on Aug 8. This delay suggests organized mobilization rather than organic response. The near-total collapse by January 2020 indicates campaign-driven rather than sustained grassroots engagement.

**Peak Hour Analysis (UTC):** 15:00-17:00 UTC (8:30-11:30 PM IST) — prime evening hours in India, consistent with coordinated domestic campaign.

### 3.2 Content Type Distribution

| Type | Count | Percentage |
|------|-------|------------|
| Retweets | 63,477 | 64.0% |
| Original | 25,389 | 25.6% |
| Replies | 5,863 | 5.9% |
| Quotes | 4,368 | 4.4% |

**Amplification Ratio:** 2.5:1 retweets to original content — indicates high amplification campaign structure typical of coordinated hashtag campaigns.

### 3.3 Discourse Framing

Using keyword-based frame detection:

| Frame | Count | Percentage |
|-------|-------|------------|
| Neutral/Mixed | 80,384 | 81.0% |
| Pro-Government | 16,888 | 17.0% |
| Critical | 1,944 | **2.0%** |

**Key Finding:** Despite being ostensibly about Kashmir, critical voices (freedom, curfew, lockdown, human rights) represent only **2%** of the discourse. This suggests either:
1. Selection bias in data collection (hashtag-based sampling)
2. Suppression of counter-narratives
3. Successful framing control by pro-government actors

### 3.4 Key Actors

#### Most Mentioned Accounts
1. **@narendramodi** — 10,681 mentions
2. **@AmitShah** — 2,159 mentions
3. **@ImranKhanPTI** — 2,110 mentions (positioned as antagonist)
4. **@TimesNow** — 1,553 mentions (key media amplifier)
5. **@BJP4India** — 1,547 mentions

#### High-Volume Accounts (Potential Coordination Indicators)

| Author ID | Tweets | Unique Texts | RT Ratio | Days Active |
|-----------|--------|--------------|----------|-------------|
| 1154155053965385728 | 445 | 24 | 0% | 25 |
| 430371604 | 308 | 102 | 0% | 9 |
| 1155893332838502400 | 190 | 94 | 0% | 7 |

**Flag:** Top poster has 445 tweets with only 24 unique texts = **18.5 tweets per unique message**. This is a strong indicator of automated/scripted behavior.

**86 accounts** with 50+ tweets generated **7,444 tweets (7.5% of total)**. These "super-spreaders" warrant further investigation.

### 3.5 Media Outlet Amplification

| Outlet | Mentions |
|--------|----------|
| @TimesNow | 1,552 |
| @ANI | 1,302 |
| @NDTV | 561 |
| @republic | 357 |
| @ABPNews | 115 |

**Finding:** Pro-government outlets (TimesNow, Republic) heavily over-represented compared to critical outlets (NDTV). @TimesNow content was systematically amplified (102 RTs on Ajit Doval "biryani" video).

### 3.6 Hashtag Ecosystem

**Top 10 Co-occurring Hashtags:**
1. #KashmirWithModi — 54,150 (primary)
2. #KashmirWelcomesChange — 11,810
3. #Kashmir — 5,262
4. #KashmirIsOurWeAreKashmir — 3,461
5. #Article370 — 3,385
6. #KashmirHamaraHai — 2,734
7. #Pakistan — 2,221
8. #PKMKB — 872 (vulgar anti-Pakistan slogan)
9. #KashmirWantsFreedom — 852 (counter-narrative)
10. #SaveKashmirFromModi — 617 (counter-narrative)

**Counter-narrative hashtags** (#KashmirWantsFreedom, #KashmirBleedsUNSleeps, #SaveKashmirFromModi) are present but marginalized (combined ~2,000 vs 54,000 for primary hashtag).

### 3.7 Notable Viral Content

**Most Retweeted Original Tweet (2,994 RTs):**
> "Thank you Kashmiri Brothers and Sisters for trending #KashmirWithModi even without the Internet."

**Critical Observation:** This tweet explicitly acknowledges that Kashmiris had no internet access yet claims they were "trending" the hashtag — a performative contradiction that became the campaign's most viral content.

**Counter-narrative with high engagement (2,061 RTs):**
> "1 Smiling 'Kashmiri woman' put up by Vijay Goel is actually a tourist  
> 2 Kashmiri woman supporting govt in a video turns out to be Sindhi  
> 3 Kashmiri Muslim tricolor rally turns out to be from Bengaluru  
> Entire #KashmirWithModi nonsense is based on lies"

---

## 4. Coordination Indicators Summary

| Indicator | Evidence | Assessment |
|-----------|----------|------------|
| Timing coordination | 10 minutes with 100+ tweets; peak 116/minute | **Moderate** |
| Content repetition | Top account: 445 tweets, 24 unique | **Strong** |
| Automated sources | 473 tweets (0.5%) from scheduling tools | **Weak** (low volume) |
| Amplification ratio | 64% retweets | **Moderate-High** |
| Temporal spike | 33K tweets on single day, 85% decay by week 2 | **Strong** |
| Narrative homogeneity | 98% pro-govt or neutral framing | **Strong** |

---

## 5. Limitations & Methodological Notes

1. **Sampling Bias:** Dataset collected via hashtag (#KashmirWithModi) inherently captures campaign participants, not broader Kashmir discourse
2. **Frame Detection:** Keyword-based classification is crude; LLM-based frame analysis would provide nuance
3. **Account Metadata Absence:** No account creation dates, follower counts, or profile data to assess bot probability
4. **Missing Context:** No data on deleted tweets, suspended accounts, or platform interventions
5. **Language Gap:** 40% Hindi content not fully analyzed for frame detection

---

## 6. Recommendations for CommDAAF Improvement

### Recommendation 1: Implement Bot Probability Scoring Module

**Problem:** Current analysis cannot definitively identify automated accounts without account-level metadata.

**Solution:** CommDAAF should include:
- Botometer API integration (or Botometer-lite heuristics)
- Account age calculation (ID-based estimation)
- Posting velocity normalization metrics
- Text repetition scoring (unique/total ratio)

**Justification:** The Kashmir dataset shows clear signals (18.5 tweets per unique text) but lacks systematic scoring.

### Recommendation 2: Develop Temporal Anomaly Detection Pipeline

**Problem:** Coordinated campaigns exhibit distinctive temporal signatures that manual inspection may miss.

**Solution:** Build automated detection for:
- Burst detection (tweets/minute exceeding baseline)
- Inter-arrival time analysis (regular spacing = automation)
- Campaign lifecycle modeling (surge → plateau → decay patterns)
- Cross-account synchronization scoring

**Justification:** The 33K single-day spike and 85% weekly decay are clear signals that should trigger automated alerts.

### Recommendation 3: Create Multi-Hashtag Network Mapping

**Problem:** Single-hashtag analysis misses coordinated multi-hashtag campaigns.

**Solution:** Implement:
- Hashtag co-occurrence networks
- Author overlap between hashtag campaigns
- Temporal alignment across hashtag surges
- Counter-narrative vs dominant narrative mapping

**Justification:** This dataset shows clear hashtag ecosystem (#KashmirWithModi → #KashmirWelcomesChange → #LadakhWelcomesChange) suggesting centralized messaging.

---

## 7. Conclusion

The #KashmirWithModi campaign exhibits multiple signatures of **coordinated political communication**:

1. **Manufactured timing** — surge 2-3 days post-event, not real-time
2. **High amplification** — 64% retweet rate with media outlet integration
3. **Suppressed counter-narrative** — only 2% critical content
4. **Performative contradiction** — celebrating "Kashmiri support" while acknowledging information blackout
5. **Super-spreader accounts** — 86 accounts with anomalous posting patterns

This aligns with Wayne's research interests in **coordinated inauthentic behavior** and **platform-mediated political communication**. The dataset represents a useful case study for developing CommDAAF detection modules.

---

*Analysis conducted following CommDAAF principles: no default parameters without justification, explicit methodology documentation, limitations acknowledged.*
