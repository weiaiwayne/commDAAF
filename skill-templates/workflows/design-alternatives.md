# Design Alternatives: From Blockers to Pivots

**Philosophy:** Every constraint is a design opportunity. CommDAAF doesn't just flag problems — it helps you pivot to what you CAN do.

---

## The Pattern

When a probing question identifies a problem:

```yaml
problem_detected:
  issue: "[What's wrong]"
  severity: "[blocker/major/minor]"
  why_it_matters: "[Impact on validity]"
  
  # THIS IS NEW - always include alternatives
  instead_try:
    option_1:
      approach: "[Alternative method]"
      tradeoff: "[What you give up]"
      works_because: "[Why this is valid]"
    option_2:
      approach: "[Another alternative]"
      tradeoff: "[What you give up]"
      works_because: "[Why this is valid]"
```

---

## Common Constraints → Alternatives

### Temporal Imbalance

**Problem:** Uneven year distribution (e.g., 2018 has n=3)

```yaml
temporal_imbalance:
  blocked: "Year-level ANOVA or cross-year comparisons"
  
  instead_try:
    1_collapse_periods:
      approach: "Collapse to meaningful periods (pre-finale, post-finale)"
      works_because: "Binary comparison needs less data per cell"
      example: "Compare engagement 30 days before vs 30 days after finale announcement"
    
    2_subset_analysis:
      approach: "Analyze only years with sufficient data (2015-2017)"
      works_because: "Internal validity preserved within subset"
      tradeoff: "Cannot generalize to full timeline"
    
    3_monthly_granularity:
      approach: "Use month as unit instead of year"
      works_because: "More observations per cell, finer temporal resolution"
      example: "24 months × ~130 tweets/month = viable comparison"
    
    4_continuous_time:
      approach: "Treat time as continuous predictor in regression"
      works_because: "No cell size requirements, captures trends"
      example: "engagement ~ days_since_launch + sentiment + controls"
```

### Missing Normalization Data

**Problem:** No follower counts to normalize engagement

```yaml
missing_normalization:
  blocked: "Cross-account or cross-time engagement comparisons"
  
  instead_try:
    1_within_period_percentiles:
      approach: "Convert to percentile rank within time windows"
      works_because: "Relative position doesn't need absolute baseline"
      example: "This tweet was in 90th percentile for its month"
    
    2_log_transform:
      approach: "Log-transform engagement to reduce scale effects"
      works_because: "Compresses range, makes distribution more normal"
      tradeoff: "Harder to interpret coefficients"
    
    3_binary_outcome:
      approach: "Convert to high/low engagement (above/below median)"
      works_because: "Removes magnitude issues entirely"
      example: "Logistic regression: P(viral) ~ sentiment + content_type"
    
    4_ratio_metrics:
      approach: "Use retweet-to-favorite ratio instead of counts"
      works_because: "Ratio is self-normalizing"
      example: "RT/fav ratio indicates amplification vs appreciation"
```

### Single Account Data

**Problem:** Only one brand account, can't generalize

```yaml
single_account:
  blocked: "Claims about 'entertainment brands' or 'TV shows' generally"
  
  instead_try:
    1_case_study_framing:
      approach: "Frame as exploratory case study, not generalizable finding"
      works_because: "Case studies generate hypotheses, not test them"
      example: "This case suggests entertainment brands MAY use..."
    
    2_within_account_variation:
      approach: "Focus on variation within the account over time/content"
      works_because: "Account is its own control"
      example: "How does THIS account's engagement vary by content type?"
    
    3_content_type_comparison:
      approach: "Compare content types (promo vs BTS vs fan engagement)"
      works_because: "Multiple conditions within single account"
      example: "N=500 promotional, N=300 behind-scenes, N=400 fan replies"
    
    4_hypothesis_generation:
      approach: "Explicitly position as hypothesis-generating for future multi-account study"
      works_because: "Sets up confirmatory research"
      example: "H1 for future test: Entertainment brands with higher positive sentiment..."
```

### Pre-computed Sentiment (Unknown Tool)

**Problem:** Polarity scores exist but provenance unknown

```yaml
unknown_sentiment_tool:
  blocked: "Trusting scores without validation"
  
  instead_try:
    1_validate_sample:
      approach: "Manually code 50-100 tweets, correlate with pre-computed"
      works_because: "Establishes empirical validity for YOUR data"
      threshold: "r > 0.7 = acceptable, r < 0.5 = recompute"
    
    2_use_as_proxy:
      approach: "Treat as 'text positivity proxy' not 'true sentiment'"
      works_because: "Honest about construct limitations"
      example: "We use pre-computed polarity as a proxy for text valence..."
    
    3_recompute_transparent:
      approach: "Recompute with VADER/TextBlob and document fully"
      works_because: "Full reproducibility"
      tradeoff: "Extra computation, may differ from original"
    
    4_categorical_only:
      approach: "Use only for positive/neutral/negative categories, not continuous"
      works_because: "Directional classification more robust than exact scores"
      example: "Classify as positive (>0.1), neutral (-0.1 to 0.1), negative (<-0.1)"
```

### Content Confounds

**Problem:** Hashtags/media/mentions affect engagement but aren't controlled

```yaml
content_confounds:
  blocked: "Attributing engagement differences to sentiment alone"
  
  instead_try:
    1_stratified_analysis:
      approach: "Analyze sentiment-engagement within content type strata"
      works_because: "Controls for content type"
      example: "Among tweets WITH images, sentiment-engagement correlation is..."
    
    2_include_controls:
      approach: "Add content features as control variables in regression"
      works_because: "Statistical control for confounds"
      example: "engagement ~ sentiment + has_media + hashtag_count + mention_count"
    
    3_matched_comparison:
      approach: "Match high/low sentiment tweets on content features"
      works_because: "Pseudo-experimental design"
      example: "Compare positive vs negative tweets with same hashtag count"
    
    4_subset_to_homogeneous:
      approach: "Analyze only text-only tweets (no media, no hashtags)"
      works_because: "Eliminates confounds by exclusion"
      tradeoff: "Reduced sample size, may not generalize to full corpus"
```

---

## Integration with Probing Questions

Update each method skill's probing questions to include:

```yaml
# Example: sentiment-analysis.md Q3 update

q3_tool:
  question: "What approach will you use and why?"
  
  if_problem_black_box:
    issue: "Pre-computed scores with unknown provenance"
    severity: "major"
    
    instead_try:
      - "Validate against 50-tweet human-coded sample (recommended)"
      - "Recompute with documented tool (VADER/TextBlob)"
      - "Use as categorical proxy only (pos/neu/neg)"
      - "Report as 'text valence proxy' with explicit limitations"
    
    minimum_requirement: "Choose one alternative and document"
```

---

## User Experience

### Before (Blocker Mode)
```
⚠️ PROBLEM: Your data has severe temporal imbalance.
2018 has only 3 tweets.
Year-level ANOVA is invalid.

Cannot proceed until resolved.
```

### After (Pivot Mode)
```
⚠️ PROBLEM: Your data has temporal imbalance.
2018 has only 3 tweets — year-level ANOVA won't work.

📐 INSTEAD, TRY:

1. COLLAPSE TO PERIODS
   → Pre-finale vs post-finale (binary comparison)
   → Needs: ~50+ tweets per period ✓

2. SUBSET TO 2015-2017
   → Drop 2018 entirely, analyze balanced years
   → Needs: Acknowledge limitation in scope

3. MONTHLY GRANULARITY  
   → 24 months with ~130 tweets each
   → Needs: Enough variation within months

4. CONTINUOUS TIME MODEL
   → Regression with days_since_launch predictor
   → Needs: No cell size requirements

Which approach fits your RQ? ___
```

---

## Implementation Checklist

For each constraint type in CommDAAF:

- [ ] Identify what's blocked
- [ ] List 3-4 realistic alternatives
- [ ] Specify tradeoffs for each
- [ ] Explain why alternative is valid
- [ ] Set minimum requirement (must pick one)
- [ ] Update probing question to include options

---

## Success Criteria

A good "instead, try" suggestion:
- ✅ Is actually achievable with the available data
- ✅ Preserves as much research value as possible
- ✅ Makes tradeoffs explicit
- ✅ Explains WHY the alternative works
- ✅ Can be defended in peer review

A bad suggestion:
- ❌ "Just collect more data" (not helpful)
- ❌ Requires resources the researcher doesn't have
- ❌ Hides the limitation instead of addressing it
- ❌ Is methodologically weaker than the original problem

---

*Design Alternatives | CommDAAF v0.4*
