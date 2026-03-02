# CommDAAF Knowledge Base: Resolved Failure Patterns

> **Attribution**: This structured knowledge base approach is adapted from Xu & Yang (2026), "Scaling Reproducibility." They accumulated 64 documented failure patterns across 92 studies. We adopt their format for communication research.
>
> Paper: https://yiqingxu.org/papers/2026_ai/AI_reproducibility.pdf

## Purpose

This file documents **resolved failure patterns** encountered during AgentAcademy runs. Each entry includes:
- **Context**: When/where the failure occurs
- **Problem**: What goes wrong
- **Root Cause**: Why it happens
- **Fix**: Generalized resolution rule
- **Impact**: Which datasets/analyses are affected

Entries are version-controlled and updated **between runs only**.

---

## Entry Format

```markdown
### [DATE] Short Description
- **Context**: [Stage, data type, trigger condition]
- **Problem**: [What fails or produces wrong results]
- **Root Cause**: [Why this happens]
- **Fix**: [Generalized resolution rule]
- **Impact**: [Scope: specific dataset, all Twitter data, etc.]
- **Caught by**: [Agent or validation step]
- **Version added**: [CommDAAF version]
```

---

## Data Loading Patterns

### [2026-02-17] Missing timestamp column variants
- **Context**: Loading Twitter/social media CSV data
- **Problem**: Script fails with "column not found: created_at"
- **Root Cause**: Different datasets use different column names (timestamp, time, date, created_at, posted_at)
- **Fix**: Check for column variants in order: ['created_at', 'timestamp', 'time', 'date', 'posted_at', 'datetime']; use first match
- **Impact**: All social media datasets
- **Caught by**: Data loading stage
- **Version added**: 0.5.0

### [2026-02-17] Engagement metrics named inconsistently
- **Context**: Computing engagement statistics
- **Problem**: Engagement column not found
- **Root Cause**: Platforms use different names (likes, favorites, like_count, favourites_count)
- **Fix**: Normalize to standard names during preprocessing: {like_count, retweet_count, reply_count, quote_count}
- **Impact**: All engagement analyses
- **Caught by**: Metric computation stage
- **Version added**: 0.5.0

### [2026-02-18] Pickle file version mismatch
- **Context**: Loading .pkl files from different Python versions
- **Problem**: UnpicklingError or protocol mismatch
- **Root Cause**: Pickle protocol varies by Python version
- **Fix**: Try loading with encoding='latin1'; if fail, convert to CSV first
- **Impact**: Archived datasets in .pkl format
- **Caught by**: Data loading stage
- **Version added**: 0.6.0

---

## Statistical Computation Patterns

### [2026-02-17] Raw vs log-transformed correlations diverge significantly
- **Context**: Computing correlations on engagement data
- **Problem**: Raw Pearson r = 0.412, but log-transformed r = 0.251 — 40% difference
- **Root Cause**: Social media engagement is heavily right-skewed; raw correlations inflated by outliers
- **Fix**: **Always report BOTH** raw and log-transformed correlations for skewed data; flag if difference > 20%
- **Impact**: All engagement correlation analyses
- **Caught by**: Cross-agent validation (Kimi caught GLM's raw-only report)
- **Version added**: 0.6.0

### [2026-02-17] Effect size classification inconsistent
- **Context**: Interpreting correlation coefficients
- **Problem**: Agent classified r=0.15 as "moderate" in one section, "small" in another
- **Root Cause**: No explicit reference to Cohen (1988) benchmarks
- **Fix**: Enforce Cohen benchmarks with explicit citation: small (0.1), medium (0.3), large (0.5)
- **Impact**: All effect size interpretations
- **Caught by**: Cross-review (GLM caught Kimi inconsistency)
- **Version added**: 0.6.0

### [2026-02-18] Multiple comparisons without correction
- **Context**: Running correlations across many variable pairs
- **Problem**: 5 of 20 correlations "significant" at p<0.05, but expected 1 by chance
- **Root Cause**: No Bonferroni or FDR correction applied
- **Fix**: Flag when >3 comparisons; require correction or explicit acknowledgment
- **Impact**: All multi-variable correlation analyses
- **Caught by**: Methodology audit
- **Version added**: 0.6.0

---

## Cross-Agent Validation Patterns

### [2026-02-17] Coefficient sign reversal between agents
- **Context**: GLM reports positive correlation, Kimi reports negative
- **Problem**: Results contradict each other
- **Root Cause**: Different handling of missing values (GLM dropped, Kimi imputed)
- **Fix**: Require explicit missing value handling statement; both agents must use same method
- **Impact**: All analyses with missing data
- **Caught by**: Cross-validation comparison
- **Version added**: 0.6.0

### [2026-02-17] Count mismatch after filtering
- **Context**: Applying sample filters (date range, user type)
- **Problem**: GLM N=3,153, Kimi N=3,147 after "same" filter
- **Root Cause**: Different timezone handling for date filters
- **Fix**: Require explicit timezone specification; normalize to UTC before filtering
- **Impact**: All temporal filtering operations
- **Caught by**: Cross-validation comparison
- **Version added**: 0.6.0

---

## Bot/Coordination Detection Patterns

### [2026-02-17] Top accounts not checked for automation
- **Context**: Analyzing hashtag campaign
- **Problem**: Top 3 accounts responsible for 40% of tweets, but no bot check
- **Root Cause**: Analysis focused on content, ignored account behavior
- **Fix**: **Mandatory**: Check top 20 accounts for automation signals before interpreting aggregate patterns
- **Impact**: All hashtag/campaign analyses
- **Caught by**: Cross-review (Kimi flagged missing check)
- **Version added**: 0.6.0

### [2026-02-17] Coordination inferred from timing alone
- **Context**: Detecting coordinated behavior
- **Problem**: Claimed coordination based on posts within 60-second windows
- **Root Cause**: Didn't account for organic response to breaking news
- **Fix**: Require multiple signals: timing AND (content similarity OR network connection OR account age)
- **Impact**: All coordination detection analyses
- **Caught by**: Methodology audit
- **Version added**: 0.6.0

---

## Temporal Analysis Patterns

### [2026-02-17] Phase classification inconsistent
- **Context**: Dividing timeline into phases (early, peak, decline)
- **Problem**: Phase boundaries defined differently in methods vs results sections
- **Root Cause**: Post-hoc phase identification based on observed patterns
- **Fix**: Require explicit phase criteria BEFORE analysis; document any post-hoc adjustments
- **Impact**: All longitudinal/phase analyses
- **Caught by**: Cross-review (GLM caught Kimi inconsistency)
- **Version added**: 0.6.0

### [2026-02-17] Platform algorithm change not controlled
- **Context**: Analyzing engagement trends 2014-2018
- **Problem**: Engagement spike in 2016 attributed to content quality
- **Root Cause**: Twitter algorithm change in Feb 2016 (timeline ranking)
- **Fix**: **Mandatory**: Check for known platform changes in study period; add to confound checklist
- **Impact**: All multi-year platform analyses
- **Caught by**: Cross-review (Kimi identified missing control)
- **Version added**: 0.6.0

---

## Reporting Patterns

### [2026-02-17] Claims exceed statistical evidence
- **Context**: Interpreting non-significant results
- **Problem**: "Suggests a relationship" used for p=0.23
- **Root Cause**: Desire to report positive findings
- **Fix**: Enforce claim-evidence matcher; non-significant = "no evidence for relationship"
- **Impact**: All interpretive text
- **Caught by**: Claim-evidence matcher workflow
- **Version added**: 0.5.0

### [2026-02-18] Sample size buried in footnotes
- **Context**: Reporting results
- **Problem**: Main text doesn't mention N; found only in table footnote
- **Root Cause**: Standard practice in some fields
- **Fix**: Require N in main text for every statistical claim
- **Impact**: All reports
- **Caught by**: Report template validation
- **Version added**: 0.7.0

---

## Silent Failure Patterns

> These produce no error message but wrong results.

### [2026-02-18] UTF-8 encoding produces garbled hashtags
- **Context**: Loading CSV with non-ASCII characters
- **Problem**: #BlackLivesMatter becomes #BlackLivesMaïer
- **Root Cause**: File saved as Latin-1, loaded as UTF-8
- **Fix**: Detect encoding with chardet before loading; warn if confidence < 0.9
- **Impact**: Multilingual datasets
- **Caught by**: Manual inspection of sample data
- **Version added**: 0.7.0

### [2026-02-18] Duplicate rows inflating statistics
- **Context**: Computing engagement totals
- **Problem**: Total engagement 2x higher than expected
- **Root Cause**: Data export included duplicates (retweets as separate rows)
- **Fix**: Check for duplicates on (tweet_id) or (user_id, timestamp, text); report duplicate rate
- **Impact**: All aggregate statistics
- **Caught by**: Cross-validation (count mismatch)
- **Version added**: 0.7.0

---

## Knowledge Base Statistics

| Category | Patterns Documented |
|----------|---------------------|
| Data Loading | 3 |
| Statistical Computation | 3 |
| Cross-Agent Validation | 2 |
| Bot/Coordination Detection | 2 |
| Temporal Analysis | 2 |
| Reporting | 2 |
| Silent Failures | 2 |
| **Total** | **16** |

**Last Updated**: 2026-02-18
**CommDAAF Version**: 0.7.0

---

## Contributing

When you encounter a new failure pattern:

1. Document it in this format
2. Implement a generalized fix (not paper-specific)
3. Add to appropriate category
4. Update statistics
5. Commit with message: `kb: add [category] pattern - [short description]`

Patterns should be **generalizable** — if it only affects one specific dataset, it's not a pattern.
