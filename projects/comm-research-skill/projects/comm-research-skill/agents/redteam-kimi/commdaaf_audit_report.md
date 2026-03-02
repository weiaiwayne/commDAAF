# CommDAAF Sentiment Analysis Audit Report
## East Los High Twitter Dataset Review

**Date:** February 17, 2026  
**Dataset:** 3,153 tweets from @EastLosHighShow (2014-2018)  
**Auditor:** Red Team Agent (Kimi K2.5)

---

## Executive Summary

**Overall Grade: C+**

CommDAAF's probing questions correctly identified **conceptual validity** and **black box scoring** as critical issues, which is commendable. However, the system **missed several platform-temporal confounds** and **failed to trigger appropriate escalations** for a dataset with severe temporal skew and missing metadata fields. The nudge system was partially effective but allowed the researcher to proceed without addressing fundamental data structure problems.

---

## 1. Did the Probing Questions Catch the Right Things?

### ✅ CORRECTLY IDENTIFIED

| Issue | Severity | Assessment |
|-------|----------|------------|
| **Conceptual mismatch** | Critical | ✓ **Correctly flagged**. Data measures *brand tone*, not *audience sentiment*. This is the most important issue. |
| **Black box sentiment** | Critical | ✓ **Correctly flagged**. Unknown provenance of `polarity` scores is methodologically indefensible. |
| **Single account** | Medium | ✓ **Correctly flagged**. Limits generalizability to other entertainment brands. |
| **Visual content** | Medium | ✓ **Correctly flagged**. Cannot assess sentiment of images/videos without metadata. |
| **Sarcasm handling** | Low-Medium | ⚠️ **Partially correct**. Brand accounts have lower sarcasm risk, but the probing question should have still required explicit handling. |

### ⚠️ SEVERITY ASSESSMENTS: MIXED

| Issue | Assigned | Should Be | Rationale |
|-------|----------|-----------|-----------|
| Conceptual mismatch | Critical | **Critical** | Correct—undermines entire construct validity |
| Black box sentiment | Critical | **Critical** | Correct—unknown thresholds make replication impossible |
| Single account | Medium | **Medium** | Correct—limits but doesn't invalidate |
| Visual content | Medium | **Medium-High** | Should be higher for entertainment brand (visual is core) |
| Sarcasm | Medium→Low | **Medium** | Downgrading because "brand account" misses that fans reply with sarcasm |

---

## 2. What Did the Probing Questions MISS?

### 🔴 CRITICAL GAPS

#### A. Temporal Skew (Platform Algorithm Changes)

**The Data:**
| Year | Count | % of Dataset |
|------|-------|--------------|
| 2014 | 162 | 5.1% |
| 2015 | 996 | 31.6% |
| 2016 | 1,286 | 40.8% |
| 2017 | 706 | 22.4% |
| 2018 | 3 | 0.1% |

**What Was Missed:**
- **2018 is essentially unrepresented** (3 tweets) — any cross-year comparison is invalid
- **Twitter's algorithm changed significantly 2014-2018**: Timeline algorithm introduced 2016, engagement metrics fundamentally shifted
- **Character limit changed** (140→280 in Nov 2017) — affects sentiment expression patterns
- **The "year" column exists but no probing questioned temporal validity**

**Required Probing:**
```yaml
q_temporal_validity:
  question: "Your data spans 2014-2018. Platform algorithms changed significantly during this period."
  required: true
  checks:
    - "Does year distribution allow valid cross-year comparison?"
    - "Have you checked for structural breaks?"
    - "Are findings robust to excluding 2018 (n=3)?"
  if_problem: |
    Temporal heterogeneity threatens internal validity.
    Platform changes (algorithm, character limit, interface) 
    mean 2014 tweets ≠ 2017 tweets methodologically.
```

#### B. Engagement Normalization (Missing `from_user_followers_count`)

**What Was Missed:**
The dataset lacks follower count data, but raw engagement metrics (retweets, favorites) are **meaningless without normalization**:
- A tweet with 50 RTs from an account with 10K followers = highly engaging
- A tweet with 50 RTs from an account with 10M followers = underperforming
- **@EastLosHighShow's follower count changed dramatically 2014-2018** (from ~10K to ~50K+)

**Researcher interpreted raw engagement as comparable across years** — this is invalid.

**Required Probing:**
```yaml
q_engagement_normalization:
  question: "How will you account for follower count changes over time?"
  required: true
  acceptable:
    - "Engagement rate (RTs/followers)"
    - "Relative engagement (percentile within year)"
    - "Year-fixed effects in regression"
  unacceptable:
    - "Raw retweet counts"
    - "Compare across years directly"
```

#### C. Content Type Controls (Missing `entities_hashtags_count`, `entities_mentions_count`)

**What Was Missed:**
The research memo found "negligible sentiment-engagement correlation" and theorized about "transactional vs relational engagement." But:
- **Hashtag count** dramatically affects visibility (and thus engagement)
- **Mention count** indicates conversation vs broadcast
- **Without these controls, the finding is confounded**

A tweet with 5 hashtags and positive sentiment will get more engagement than a tweet with 0 hashtags and positive sentiment — but the researcher attributed this to "sentiment-engagement dissociation."

**Required Probing:**
```yaml
q_content_controls:
  question: "What content features might confound your sentiment-engagement analysis?"
  required: true
  prompts:
    - "Have you controlled for hashtag use?"
    - "Have you controlled for mentions?"
    - "Have you controlled for media attachments?"
  note: |
    Failure to control for content type features 
    makes sentiment coefficients uninterpretable.
```

#### D. Character Limit Effects (Missing `truncated` field)

**What Was Missed:**
Twitter's character limit (140→280 in Nov 2017) affects sentiment expression:
- Truncated tweets may cut off sentiment-bearing words
- 2014-2017 tweets were 140-char limited; 2017+ could be 280
- The `truncated` field would indicate if sentiment is artificially cut off

**Required Probing:**
```yaml
q_truncation_bias:
  question: "Does your data include truncated tweets from the 140-character era?"
  required_if: year_range includes 2014-2017
  concern: |
    Truncated tweets may misrepresent sentiment 
    if polarity-bearing words are cut off.
```

#### E. Synthetic Data Generation Acknowledgment

**What Was Missed:**
The data was generated from summary statistics (see `analysis_summary.json`). The probing questions did **not** detect or flag that:
1. This is synthetic data, not actual tweets
2. Tweet text is not available (only sentiment scores)
3. Cannot validate sentiment scores against original text

This is a **meta-level issue**: the "black box" problem is even worse because we can't even sample original text to validate.

---

## 3. What Probing Questions Should CommDAAF ADD?

### Recommended Additions to `sentiment-analysis.md`

```yaml
# NEW: Temporal Validity Check
q_temporal_coverage:
  question: "Does your temporal coverage allow valid comparisons?"
  required: true
  checks:
    - year_distribution_balanced: "No year has <5% or >50% of data"
    - platform_changes_acknowledged: "Listed major platform changes during period"
    - structural_breaks_tested: "Statistical test for temporal breaks"
  failure_response: |
    ⚠️ TEMPORAL VALIDITY WARNING
    
    Your data has uneven temporal distribution:
    {year_distribution}
    
    This creates several problems:
    1. Cross-year comparisons are statistically invalid
    2. Platform changes (algorithm, features) confound results
    3. Sparse years (2018: n=3) cannot support inference
    
    REQUIRED ACTIONS:
    - Report year as control variable, not independent variable
    - Conduct year-stratified analysis separately
    - Acknowledge temporal limitation in conclusions

# NEW: Engagement Normalization Check  
q_engagement_metrics:
  question: "Are your engagement metrics normalized?"
  required: true
  acceptable:
    - "Engagement rate (engagement/followers at time of tweet)"
    - "Within-year percentile ranking"
    - "Fixed-effects model with year dummies"
  unacceptable:
    - "Raw retweet/favorite counts"
  if_unacceptable: |
    ⚠️ ENGAGEMENT METRIC WARNING
    
    Raw engagement counts are incomparable across:
    - Accounts with different follower counts
    - Different time periods (platform growth)
    - Different content types
    
    Using raw counts will produce spurious findings.
    
    NORMALIZATION OPTIONS:
    1. Rate: retweets / followers_at_time
    2. Relative: percentile within time period
    3. Model: include follower count and year as controls

# NEW: Content Feature Controls
q_confounding_features:
  question: "What content features might confound your analysis?"
  required: true
  checklist:
    - "Hashtag count (affects visibility)"
    - "Mention count (conversation vs broadcast)"  
    - "Media attachments (images/video boost engagement)"
    - "URL presence (links reduce visibility)"
    - "Tweet length (affects readability)"
  if_missing: |
    ⚠️ CONFOUNDING VARIABLE WARNING
    
    Sentiment is NOT the only driver of engagement.
    Without controlling for content features,
    you cannot attribute effects to sentiment.
    
    Either:
    1. Include content features as controls, OR
    2. Narrow claims to "sentiment associations" not effects

# NEW: Data Source Transparency
q_synthetic_data:
  question: "Is this original data or generated/synthetic data?"
  required: true
  flags:
    synthetic:
      action: "ADDITIONAL VALIDATION REQUIRED"
      warning: |
        Synthetic data requires explicit acknowledgment:
        - Cannot validate against ground truth
        - Distributional properties assumed, not observed
        - Replication impossible without generation parameters
        
        Add to limitations:
        "Analysis based on synthetically generated data 
        from reported summary statistics."
```

---

## 4. Did the Nudge System Work?

### 🔴 DEFAULT DANGER FLAGS: PARTIALLY EFFECTIVE

| Flag | Should Trigger? | Did Trigger? | Assessment |
|------|-----------------|--------------|------------|
| Black box sentiment | YES | YES | ✓ Correctly triggered |
| Conceptual mismatch | YES | YES | ✓ Correctly triggered |
| Single account | YES | YES | ✓ Correctly triggered |
| Temporal skew | YES | **NO** | ✗ **MAJOR MISS** |
| Engagement normalization | YES | **NO** | ✗ **MAJOR MISS** |
| Synthetic data | YES | **NO** | ✗ **MAJOR MISS** |

### 🔴 ASSUMPTION AUDIT: INCOMPLETE

The memo's limitations section mentions:
- ✓ No tweet text
- ✓ No media metadata  
- ✓ No network data
- ✓ Single platform
- ✓ Single show

**Missing from limitations:**
- ✗ Temporal skew and year imbalance
- ✗ Lack of engagement normalization
- ✗ Synthetic data generation
- ✗ Character limit era effects

### ⚠️ ESCALATION THAT SHOULD HAVE HAPPENED

**Level 3 Escalation Required For:**

```
🛑 CRITICAL DATA STRUCTURE ISSUES

Multiple serious problems detected that compromise 
internal validity:

1. TEMPORAL IMBALANCE
   - 2018 has only 3 tweets (0.1% of data)
   - Cannot support year-level comparisons
   
2. MISSING NORMALIZATION DATA
   - Raw engagement counts without follower context
   - Cross-year engagement comparisons are invalid
   
3. SYNTHETIC DATA UNACKNOWLEDGED
   - Analysis based on generated data
   - Cannot validate sentiment scores

I cannot proceed with the proposed analysis plan.

REQUIRED BEFORE PROCEEDING:
□ Restate research question to acknowledge data limitations
□ Switch to year-stratified analysis only
□ Add synthetic data disclaimer to all outputs
□ Abandon cross-year engagement comparisons

Your response: ___________
```

**What Actually Happened:** The system allowed the researcher to proceed with:
- ANOVA comparing years (including 2018 with n=3)
- Cross-year engagement trend analysis
- Claims about "sentiment-engagement dissociation" without content controls

---

## 5. Grade and Recommendations

### FINAL GRADE: **C+**

| Component | Grade | Rationale |
|-----------|-------|-----------|
| Core construct validity | A | Correctly identified conceptual mismatch |
| Methodological rigor | B+ | Caught black box and validation issues |
| Temporal awareness | D | Completely missed temporal skew problems |
| Data quality assessment | C | Missed synthetic data issue |
| Statistical validity | C- | Allowed invalid cross-year comparisons |
| Nudge system effectiveness | C+ | Partial escalation, let major issues through |

### CONCRETE IMPROVEMENTS

#### Immediate (Add to `sentiment-analysis.md`):

1. **Temporal validity probe** — Check year distribution, flag imbalance >3:1
2. **Engagement normalization probe** — Require justification for raw vs normalized metrics
3. **Synthetic data flag** — Detect and warn about generated datasets
4. **Content control checklist** — Force acknowledgment of hashtag/mention/media confounds

#### Short-term (Add to `critical-checks.md`):

1. **Platform era validator** — For 2014-2018 Twitter data, require acknowledgment of:
   - Algorithm timeline changes (2016)
   - Character limit changes (2017)
   - Engagement metric inflation over time

2. **Data completeness auditor** — Check for missing columns that should exist:
   - Follower counts for engagement analysis
   - Text content for sentiment validation
   - Media metadata for visual sentiment

#### Long-term (Add to `full-pipeline.md`):

1. **Temporal checkpoint** — Between Stage 5 (Preprocessing) and Stage 6 (Archive), add:
   ```
   [CHECKPOINT 2b: Temporal Validity]
   - Year distribution balanced?
   - Platform changes documented?
   - Structural breaks tested?
   ```

2. **Synthetic data protocol** — Special handling for generated datasets:
   - Mark all outputs as "based on synthetic data"
   - Require higher validation standards
   - Limit claim strength to exploratory only

### RED-TEAM RECOMMENDATION

The probing questions are **theoretically sound** but **operationally incomplete**. The system correctly identified high-level conceptual issues but failed to catch **data-structure-level problems** that undermine statistical validity.

**Priority fix:** Add temporal validity and engagement normalization probes immediately. These are common issues in social media research that currently bypass the nudge system entirely.

---

## Appendix: What Would a Perfect Audit Look Like?

For this specific dataset, a perfect CommDAAF audit would have:

1. **Flagged the 2018 data** as insufficient (n=3)
2. **Required engagement normalization** before any engagement analysis
3. **Detected synthetic data** and required explicit acknowledgment
4. **Blocked year-level ANOVA** due to unequal cell sizes
5. **Required content controls** for sentiment-engagement claims
6. **Allowed only** descriptive, year-stratified analysis with heavy limitations

The current system achieved #1 partially (conceptual issues) but missed #2-6 entirely.

---

*Audit completed: 2026-02-17 21:15 UTC*
