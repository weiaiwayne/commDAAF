# Critical Research Practice Checks

**Philosophy:** This tool assists research. It does not replace researcher judgment. Every automated decision should be a conscious choice, not a passive default.

---

## Core Principles

1. **No silent defaults** — Every significant parameter must be explicitly confirmed
2. **Explain implications** — Don't just warn; explain WHY it matters
3. **Force decisions** — Require active choice, not just "proceed? y/n"
4. **Surface assumptions** — Make hidden assumptions visible
5. **Encourage skepticism** — Prompt users to question outputs

---

## LEVEL 1: Universal Checks (Every Analysis)

These run before ANY analysis, regardless of method.

### Research Design Awareness

```yaml
universal_check_1:
  trigger: any analysis request
  message: |
    📋 **RESEARCH DESIGN CHECK**
    
    Before we proceed, confirm your research context:
    
    1. **What is your research question?**
       (Write it out — this helps me give relevant warnings)
       → [your RQ]: ___
    
    2. **Is this exploratory or confirmatory?**
       - Exploratory: I'm discovering patterns
       - Confirmatory: I'm testing a hypothesis
       
       Why it matters:
       - Exploratory → flexible parameters OK
       - Confirmatory → parameters must be pre-registered
       
       → Your study is: (exploratory/confirmatory)
    
    3. **What decisions have you already made?**
       - Data collection criteria?
       - Time period selection?
       - Platform choice?
       
       → Any decisions already locked: ___
```

### Data Provenance

```yaml
universal_check_2:
  trigger: data provided
  message: |
    📋 **DATA PROVENANCE CHECK**
    
    Understanding your data source matters:
    
    1. **How was this data collected?**
       - API (official) → what endpoints? what limits?
       - Scraping → what was the method?
       - Third-party dataset → who collected it?
       - Provided by platform → under what terms?
       
       → Collection method: ___
    
    2. **What's MISSING from this data?**
       Every dataset has gaps:
       - Deleted posts?
       - Private accounts?
       - Rate-limited sampling?
       - Platform filtering?
       
       → Known gaps: ___
    
    3. **What time period does this cover?**
       → From: ___ To: ___
       
       Did anything significant happen in this period?
       (elections, events, platform changes, API changes)
       → Context: ___
    
    4. **Has this data been pre-processed?**
       - Filtered by language?
       - Sampled?
       - Deduplicated?
       
       → Pre-processing applied: ___
```

### Researcher Positionality

```yaml
universal_check_3:
  trigger: first analysis in session
  message: |
    📋 **POSITIONALITY CHECK**
    
    Your perspective shapes analysis:
    
    1. **What's your relationship to this topic?**
       - Neutral observer?
       - Advocate for a position?
       - Affected community member?
       
       Not asking you to be "objective" — asking you to be aware.
       → Your position: ___
    
    2. **What outcome would confirm your expectations?**
       This isn't bias — it's human. Name it so we can check against it.
       → Expected finding: ___
    
    3. **What would surprise you?**
       → Unexpected finding would be: ___
    
    I'll flag if results align too neatly with expectations.
```

### Content Type Mixing Check

```yaml
universal_check_3b:
  trigger: any analysis with heterogeneous content
  message: |
    📋 **CONTENT TYPE MIXING CHECK**
    
    Does your dataset mix different content types?
    
    Common mixes that cause problems:
    | Type A | Type B | Problem |
    |--------|--------|---------|
    | TV transcripts | Written articles | Word counts differ 5-10x |
    | Original posts | Retweets | Different engagement baselines |
    | Long-form | Short-form | Topic modeling behaves differently |
    | Text | Image captions | Different linguistic patterns |
    
    ⚠️ EXAMPLE FROM AGENTACADEMY:
    CNN dataset mixed TV transcripts (avg 4,500 words) with 
    web articles (avg 700 words). Direct comparison invalid.
    
    If mixed:
    ❌ BLOCKED: Direct comparison of raw metrics across types
    
    ✅ INSTEAD, TRY:
    - Analyze separately, then compare patterns
    - Normalize within content type
    - Use relative metrics (percentile within type)
    - Control for content type in models
    
    Content types in your data: ___
    Are you comparing across types? ___
    Mitigation approach: ___
```

### Temporal Distribution Check

```yaml
universal_check_3c:
  trigger: any time-series or longitudinal analysis
  message: |
    📋 **TEMPORAL DISTRIBUTION CHECK**
    
    Is your data evenly distributed over time?
    
    ⚠️ EVENT CLUSTERING WARNING
    Data often clusters around crises/events, not evenly distributed.
    
    EXAMPLE FROM AGENTACADEMY:
    CNN 2015 dataset: June had 4x more articles than September
    (Charleston shooting drove coverage spike)
    
    Problems with clustered data:
    - "Average" misleading (dominated by crisis periods)
    - Comparing months = comparing events, not trends
    - Statistical tests assume independence
    
    CHECK YOUR DISTRIBUTION:
    | Period | N | % of Total | Notable Events |
    |--------|---|------------|----------------|
    | ___    |   |            |                |
    
    🚨 FLAGS:
    - Any period with >30% of total observations
    - Any period with <5% of total observations
    - Peak/trough ratio > 4:1
    
    If clustered:
    ✅ INSTEAD, TRY:
    - Weight by inverse frequency
    - Analyze peak periods separately
    - Normalize within event windows
    - Acknowledge as limitation with direction
    
    Distribution assessment: ___
    Action taken: ___
```

### Sample Balance Check

```yaml
universal_check_4:
  trigger: any comparison across groups (time periods, categories, conditions)
  message: |
    📋 **SAMPLE BALANCE CHECK**
    
    Before comparing groups, verify each has sufficient observations.
    
    Show your distribution:
    | Group | N | % of Total |
    |-------|---|------------|
    | ___   |   |            |
    
    🚨 FLAGS:
    - Any group with <5% of total observations
    - Any group with N < 30
    - Largest/smallest group ratio > 10:1
    
    If imbalanced:
    ❌ BLOCKED: Standard group comparisons (ANOVA, chi-square)
    
    ✅ INSTEAD, TRY:
    - Collapse small groups into meaningful larger categories
    - Exclude insufficient groups and narrow claims
    - Use regression with group as continuous predictor
    - Report descriptive statistics only for small groups
    
    Your group distribution: ___
    Action taken: ___
```

### Metric Comparability Check

```yaml
universal_check_5:
  trigger: comparing counts/rates across time, accounts, or conditions
  message: |
    📋 **METRIC COMPARABILITY CHECK**
    
    Are your metrics comparable across comparison units?
    
    Baselines may differ due to:
    - Audience size changes over time
    - Platform algorithm or feature changes
    - Seasonal or cyclical patterns
    - Different data collection methods
    
    If baselines differ:
    ❌ BLOCKED: Direct comparison of raw values
    
    ✅ INSTEAD, TRY:
    - Rate metrics (per capita, per follower, per post)
    - Relative measures (percentile within period)
    - Include baseline as control variable
    - Log-transform to reduce scale effects
    - Binary outcome (above/below threshold)
    
    Do baselines differ? ___
    How are you handling it? ___
```

### Context Change Documentation

```yaml
universal_check_6:
  trigger: any longitudinal or time-series analysis
  message: |
    📋 **CONTEXT CHANGE CHECK**
    
    What changed in your research context during the study period?
    
    Consider:
    - Platform features, algorithms, or policies
    - Major external events (elections, crises, viral moments)
    - Data collection method changes
    - Community/population changes
    
    For each change:
    - When did it occur?
    - Could it affect your variables?
    - How will you address it?
    
    Options:
    - Include as control/moderator in analysis
    - Subset data to single-context period
    - Test for structural breaks
    - Acknowledge as limitation with direction of bias
    
    Known context changes: ___
    How addressed: ___
```

### Phase/Period Classification Consistency

```yaml
universal_check_6b:
  trigger: any temporal analysis with phases, periods, or bins
  message: |
    📋 **PHASE CLASSIFICATION CONSISTENCY CHECK**
    
    If you're labeling time periods (e.g., "high activity", "low activity", "Phase 1"):
    
    ⚠️ LABELS MUST BE INTERNALLY CONSISTENT
    
    Common error caught in cross-review:
    - Period A: 571 tweets/bin → labeled "Low"
    - Period B: 327 tweets/bin → labeled "Moderate"
    → Contradiction! Lower value has higher label.
    
    REQUIRED:
    1. Define classification criteria BEFORE labeling
    2. Apply criteria consistently across all periods
    3. Show the thresholds used
    
    Example valid approach:
    - Tertile split: Bottom 33% = Low, Middle = Moderate, Top = High
    - Standard deviation: Mean ± 1 SD = Moderate, outside = High/Low
    
    Your classification method: ___
    Thresholds used: ___
    
    ✓ CHECKPOINT:
    [ ] I verified no label contradictions exist
    [ ] Classification criteria are documented
    [ ] Same criteria applied to all periods
```

### Bot/Automated Account Detection

```yaml
universal_check_6c:
  trigger: Twitter/X analysis, social media network analysis, coordinated behavior analysis
  message: |
    📋 **BOT/AUTOMATED ACCOUNT CHECK**
    
    Have you checked for automated/bot accounts in your data?
    
    ⚠️ BOTS CAN DRAMATICALLY SKEW RESULTS
    
    Example from real analysis:
    - Top 4 most active accounts all had "bot" in username
    - ~10% of top activity from automated accounts
    - One analyst missed this entirely; cross-review caught it
    
    DETECTION SIGNALS (check at least 3):
    
    | Signal | Check |
    |--------|-------|
    | Username patterns | Contains "bot", "auto", "RT", "news" |
    | Posting frequency | >50 tweets/day sustained |
    | Account age vs activity | New account, massive output |
    | Content patterns | Near-identical tweets |
    | Timing regularity | Posts at exact intervals |
    | Bio indicators | "automated", "feed", "mirror" |
    
    REQUIRED:
    1. Check top 20 most active accounts manually
    2. Report % of activity from suspected automated accounts
    3. Decide: include, exclude, or analyze separately
    
    Bot detection performed: (yes/no)
    Suspected automated accounts found: ___
    % of total activity: ___
    Decision: (include/exclude/separate analysis)
    Justification: ___
```

### Effect Size Interpretation

```yaml
universal_check_7:
  trigger: any statistical test with effect size
  message: |
    📋 **EFFECT SIZE CHECK**
    
    Report effect size with standard interpretation.
    
    REFERENCE THRESHOLDS (Cohen, 1988):
    | Metric | Small | Medium | Large |
    |--------|-------|--------|-------|
    | Cohen's d | 0.2 | 0.5 | 0.8 |
    | Pearson/Spearman r | 0.1 | 0.3 | 0.5 |
    | Cliff's δ | 0.15 | 0.33 | 0.47 |
    | η² (eta-squared) | 0.01 | 0.06 | 0.14 |
    | Odds ratio | 1.5 | 2.5 | 4.0 |
    
    ⚠️ RULES:
    - Near boundaries → use lower category (0.32 r = "medium" not "medium-to-large")
    - δ = 0.40 is MEDIUM, not "large" (common error)
    - Always state metric used
    - Don't round up
    - Cite Cohen (1988) or justify alternative benchmarks
    
    Your effect size: ___
    Metric: ___
    Category: ___
    Citation for benchmarks: ___
```

### Correlation Transformation Check

```yaml
universal_check_7b:
  trigger: correlation with follower counts, engagement metrics, or any social media count variable
  message: |
    📋 **CORRELATION TRANSFORMATION CHECK**
    
    Social media metrics (followers, likes, retweets) are heavily right-skewed.
    
    ⚠️ RAW CORRELATIONS ARE INFLATED BY OUTLIERS
    
    Example from real analysis:
    - Raw follower→engagement r = 0.412
    - Log-transformed r = 0.251
    → Same data, different conclusions!
    
    REQUIRED:
    1. Check distribution of both variables (skewness, kurtosis)
    2. If skewed (skewness > 1), report BOTH:
       - Raw correlation (for comparability with naive studies)
       - Log-transformed correlation (methodologically sound)
    3. Report R² for both (variance explained)
    
    ❌ BLOCKED: Reporting only raw correlation for skewed data
    
    ✅ INSTEAD:
    - Log-transform: np.log1p(x) (handles zeros)
    - Report both raw and transformed
    - Base interpretation on transformed value
    
    Distribution check:
    - Variable 1 skewness: ___
    - Variable 2 skewness: ___
    
    Correlations reported:
    - Raw r = ___ (R² = ___%)
    - Log-transformed r = ___ (R² = ___%)
```

### Directional Consistency Check

```yaml
universal_check_8:
  trigger: any correlation, regression coefficient, or group difference
  message: |
    📋 **DIRECTION CHECK**
    
    Verify your interpretation matches the statistical direction.
    
    CORRELATIONS:
    - Positive r/ρ → "as X increases, Y increases"
    - Negative r/ρ → "as X increases, Y decreases"
    
    GROUP COMPARISONS:
    - Group A mean > Group B mean → "A has higher Y than B"
    - Check which group is which in your code
    
    REGRESSION:
    - Positive β → "more X = more Y"
    - Negative β → "more X = less Y"
    
    ✓ CHECKPOINT:
    [ ] I verified the sign/direction in my output
    [ ] My verbal interpretation matches the statistical direction
    [ ] I have not confused comparison group labels
    
    Confirmed: ___
```

### Confound Identification

```yaml
universal_check_9:
  trigger: any analysis claiming X relates to Y
  message: |
    📋 **CONFOUND CHECK**
    
    What else varies with X that could explain Y?
    
    PLATFORM-SPECIFIC CONFOUNDS (auto-generated):
    
    **Twitter/X:**
    - [ ] Algorithm changes (chronological → ranked: 2016, 2023)
    - [ ] Character limit changes (140 → 280: 2017)
    - [ ] Verified badge changes (blue check: 2023)
    - [ ] API access changes (2023)
    
    **Facebook/Instagram:**
    - [ ] News Feed algorithm updates (frequent)
    - [ ] Reels/Stories introduction
    - [ ] Privacy policy changes
    
    **YouTube:**
    - [ ] Recommendation algorithm shifts
    - [ ] Monetization policy changes
    - [ ] Comment section changes
    
    **General:**
    - [ ] Content features (length, media, formatting)
    - [ ] Source characteristics (popularity, verification)
    - [ ] Temporal factors (time of day, season, trends)
    - [ ] Audience factors (demographics, prior engagement)
    - [ ] External events overlapping data period
    
    ⚠️ EXAMPLE FROM AGENTACADEMY:
    Neither AI considered Twitter's 2016 algorithm change when 
    analyzing 2014-2018 engagement trends. Cross-review caught this.
    
    REQUIRED:
    - List 3+ potential confounds
    - For each: Do you have data to control for it?
    
    If you cannot control:
    ✅ INSTEAD, TRY:
    - Stratify analysis (examine within subgroups)
    - Match cases on confounders
    - Acknowledge specific confounds as limitations
    - Narrow claims to "association" not "effect"
    
    Potential confounds identified:
    1. ___ (controlled? ___)
    2. ___ (controlled? ___)
    3. ___ (controlled? ___)
```

### Retweet-Heavy Dataset Warning

```yaml
universal_check_10a:
  trigger: social media dataset with retweet data
  message: |
    📋 **RETWEET RATIO CHECK**
    
    What percentage of your dataset is retweets vs original content?
    
    | RT Ratio | Interpretation | Analysis Approach |
    |----------|----------------|-------------------|
    | <50% | Normal discourse | Standard analysis OK |
    | 50-80% | Amplification-heavy | Consider network analysis |
    | >80% | Amplification battle | Split analysis required |
    
    ⚠️ EXAMPLE FROM AGENTACADEMY:
    Xinjiang Cotton dataset: 88% retweets. This wasn't discourse — 
    it was competing sides trying to drown each other out.
    
    If RT% > 80%:
    ❌ BLOCKED: Standard engagement analysis (misleading)
    
    ✅ INSTEAD, TRY:
    - Network analysis: who amplifies whom
    - Separate original content analysis
    - Frame as "information warfare" not "discourse"
    - Track amplification cascades
    
    Your RT ratio: ___% 
    Analysis approach: ___
```

### Peak/Trough Spike Detection

```yaml
universal_check_10b:
  trigger: any time-series or temporal analysis
  message: |
    📋 **PEAK/TROUGH RATIO CHECK**
    
    Calculate: (highest period volume) / (lowest period volume)
    
    | Ratio | Interpretation |
    |-------|----------------|
    | <2:1 | Relatively stable |
    | 2-4:1 | Some clustering |
    | >4:1 | Event-driven dataset |
    
    ⚠️ EXAMPLE FROM AGENTACADEMY:
    Xinjiang: Peak/trough ratio 13.8:1
    March 25-26 = 36% of all tweets (H&M boycott trigger)
    
    If ratio > 4:1:
    ⚠️ WARNING: This is event-driven data, not organic baseline
    
    REQUIRED:
    1. Identify the triggering event for each spike
    2. Analyze spike and non-spike periods separately
    3. Do NOT report "average" metrics (meaningless)
    4. Document external event timeline
    
    Your peak/trough ratio: ___
    Triggering event identified: ___
```

### Language Anomaly Detection

```yaml
universal_check_10c:
  trigger: multilingual dataset or hashtag analysis
  message: |
    📋 **LANGUAGE DISTRIBUTION CHECK**
    
    What languages appear in your dataset?
    
    | Language | % of Dataset |
    |----------|--------------|
    | ___      | ___          |
    
    ⚠️ FLAG: Non-local language exceeds 20%
    
    EXAMPLE FROM AGENTACADEMY:
    #StandWithBelarus: 38% Thai content
    Initial assumption: bots
    Actual finding: Milk Tea Alliance solidarity
    
    Non-local language could indicate:
    - Diaspora communities (organic)
    - Solidarity movements (organic coordination)
    - Bot networks (inauthentic)
    - State-sponsored amplification (inauthentic)
    
    All show SIMILAR statistical signatures.
    Context determines interpretation.
    
    REQUIRED:
    1. Identify top accounts in non-local language
    2. Check if single source or distributed
    3. Look for known activists/state actors
    4. Don't assume "bots" without evidence
    
    Non-local language %: ___
    Source accounts identified: ___
    Interpretation: ___
```

### Dual-Sided Coordination Check

```yaml
universal_check_10d:
  trigger: coordination detection or campaign analysis
  message: |
    📋 **DUAL-SIDED COORDINATION CHECK**
    
    Are you assuming coordination comes from ONE side?
    
    ⚠️ ADVERSARIAL AMPLIFICATION EXISTS
    
    EXAMPLE FROM AGENTACADEMY:
    Xinjiang Cotton: BOTH sides coordinating
    - Pro-China: @SpokespersonCHN, @zlj517
    - Pro-Uyghur: @MarcRubio, @nathanlawkc
    Both had high RT ratios, different peak hours.
    
    Signs of dual-sided coordination:
    - Two dominant narrative frames
    - Both show high retweet ratios
    - Different peak hours (timezone signatures)
    - Engagement asymmetry between sides
    - Clear "sides" in reply networks
    
    REQUIRED:
    1. Check for multiple coordinating groups
    2. Compare peak hours (timezone analysis)
    3. Measure engagement per side
    4. Don't assume single actor
    
    Multiple coordinating groups found: (yes/no)
    Sides identified: ___
    Engagement asymmetry: ___
```

### Multiple Testing Awareness

```yaml
universal_check_10:
  trigger: >2 statistical tests in analysis
  message: |
    📋 **MULTIPLE TESTING CHECK**
    
    You're running multiple tests. False positive risk:
    - 3 tests → 14% chance of ≥1 false positive
    - 5 tests → 23%
    - 10 tests → 40%
    
    OPTIONS:
    
    Correction methods:
    - Bonferroni: α/n (conservative)
    - FDR/Benjamini-Hochberg (less conservative)
    - Holm-Bonferroni (step-down)
    
    Design approaches:
    - Pre-specify one primary test, label others exploratory
    - Use omnibus test first, post-hocs only if significant
    
    Transparency:
    - Report all tests run, not just significant ones
    - Label analysis as exploratory if many tests
    
    Number of tests: ___
    Approach taken: ___
```

---

## LEVEL 2: Method-Specific Deep Checks

### TOPIC MODELING — Deep Checks

```yaml
topic_modeling_critical:

  interpretation_warning:
    message: |
      ⚠️ **TOPIC MODELING INTERPRETATION WARNING**
      
      Topics are statistical artifacts, not ground truth.
      
      Common mistakes:
      
      1. **Naming topics too quickly**
         - Topic: [democracy, vote, election, freedom]
         - Tempting name: "Pro-democracy discourse"
         - Problem: Could be anti-democracy discussing same terms
         
         → Always read actual documents in topic before naming
      
      2. **Assuming topics are meaningful**
         - Model will ALWAYS produce K topics
         - Doesn't mean K meaningful topics exist
         - Garbage in → coherent-looking garbage out
         
         → Check coherence scores, read samples
      
      3. **Over-interpreting small differences**
         - Topic 3 is 12% vs 10% of corpus
         - Is that meaningful or noise?
         
         → Calculate confidence intervals
      
      Will you commit to reading 20+ documents per topic before naming?
      (yes/no)

  num_topics_forcing:
    check: num_topics is set manually
    message: |
      ⚠️ **You manually set {num_topics} topics**
      
      Why this number?
      
      Be honest:
      - [ ] Theoretically motivated (I expect K themes based on literature)
      - [ ] Empirically determined (I ran coherence tests)
      - [ ] Arbitrary (seemed reasonable)
      - [ ] Following another paper (cite: ___)
      
      If arbitrary, consider auto-detection first.
      
      Your justification: ___

  preprocessing_consequences:
    message: |
      ⚠️ **PREPROCESSING SHAPES RESULTS**
      
      These "cleaning" decisions are analytical choices:
      
      | Decision | Consequence |
      |----------|-------------|
      | Remove stopwords | "not good" → "good" (meaning flip) |
      | Lemmatize | "running" = "ran" (loses tense) |
      | Remove URLs | Loses shared content signal |
      | Lowercase | "WHO" = "who" (org vs pronoun) |
      | Remove numbers | Loses dates, statistics |
      
      There's no "correct" preprocessing.
      Different choices → different topics.
      
      Your choices should match your RQ:
      - Studying language style? → minimal preprocessing
      - Studying themes? → standard preprocessing
      - Studying specific terms? → keep original forms
      
      Justify your preprocessing: ___
```

### NETWORK ANALYSIS — Deep Checks

```yaml
network_analysis_critical:

  boundary_specification:
    message: |
      ⚠️ **NETWORK BOUNDARY PROBLEM**
      
      Networks require boundaries. Yours are:
      
      1. **Who's included?**
         - All accounts in dataset?
         - Only accounts with N+ posts?
         - Only accounts with connections?
         
         → Inclusion criteria: ___
      
      2. **Who's excluded and why?**
         - Lurkers (no posts)?
         - Low-activity accounts?
         - Accounts outside time window?
         
         → Excluded: ___
      
      3. **Is your boundary theoretically meaningful?**
         - "All accounts mentioning X" → arbitrary hashtag boundary
         - "Members of group Y" → meaningful community boundary
         
         Boundary choice shapes findings.
         → Justification: ___

  centrality_misuse:
    message: |
      ⚠️ **CENTRALITY ≠ IMPORTANCE**
      
      Common misinterpretations:
      
      | Claim | Problem |
      |-------|---------|
      | "Most influential account" | Influence requires causal evidence |
      | "Key opinion leader" | Centrality ≠ opinion leadership |
      | "Most important node" | Important for what? |
      
      Centrality measures STRUCTURE, not IMPACT.
      
      High degree could mean:
      - Genuinely influential
      - Bot with many connections
      - Celebrity (famous ≠ influential in this context)
      - Hub account (aggregator)
      
      How will you validate centrality interpretation?
      → Validation plan: ___

  missing_edges:
    message: |
      ⚠️ **YOUR NETWORK IS INCOMPLETE**
      
      All collected networks miss edges:
      
      - Private messages (not visible)
      - Deleted interactions
      - Off-platform coordination
      - API rate limits
      - Time boundary cutoffs
      
      Your network is a SAMPLE of the true network.
      
      Implications:
      - Centrality rankings may be unstable
      - Communities may be artificially separated
      - Isolates may have off-platform connections
      
      Acknowledged? How will you address this limitation?
      → Approach: ___

  retweet_rate_interpretation:
    message: |
      ⚠️ **HIGH RETWEET RATE INTERPRETATION**
      
      Your dataset shows {retweet_rate}% retweets.
      
      High retweet rates (>70%) can mean VERY different things:
      
      | Context | Interpretation |
      |---------|----------------|
      | Crisis/breaking news | Information scarcity, amplification priority |
      | Authoritarian context | Safety-seeking (RT safer than original speech) |
      | Celebrity-driven | Fan amplification behavior |
      | Coordinated campaign | Strategic amplification |
      | Normal discourse | Unusual—investigate further |
      
      ⚠️ CONTEXT MATTERS
      
      Example from #EndSARS analysis:
      - 80-94% retweet rate
      - Two interpretations offered:
        1. "Solidarity signaling" (neutral framing)
        2. "Safety-seeking in authoritarian context" (political framing)
      - BOTH are valid; choice depends on your theoretical lens
      
      What is the political/social context of your data?
      → Context: ___
      
      Which interpretation fits your context?
      → Interpretation: ___
      
      Have you considered alternative interpretations?
      → Alternatives considered: ___
```

### SENTIMENT ANALYSIS — Deep Checks

```yaml
sentiment_analysis_critical:

  validity_challenge:
    message: |
      ⚠️ **SENTIMENT VALIDITY CHALLENGE**
      
      What are you actually measuring?
      
      | You say | But actually |
      |---------|--------------|
      | "Public opinion" | Opinion of people who post publicly |
      | "Sentiment toward X" | Sentiment in posts mentioning X |
      | "Community feeling" | Aggregated individual expressions |
      
      Fundamental issues:
      
      1. **Selection bias**: Who posts? Who stays silent?
      2. **Expression vs feeling**: Perforмative positivity, venting
      3. **Context collapse**: Same words, different meanings
      4. **Temporal validity**: Sentiment when posting ≠ stable attitude
      
      What construct are you actually measuring?
      → Operationalization: ___

  aggregation_problem:
    message: |
      ⚠️ **AGGREGATION HIDES HETEROGENEITY**
      
      "Average sentiment = 0.2 (slightly positive)"
      
      Could mean:
      - Everyone slightly positive
      - 60% positive, 40% negative (polarized!)
      - 90% neutral, 10% extreme
      
      Average sentiment often meaningless.
      
      Always report:
      - Distribution (not just mean)
      - Variance
      - Bimodality check
      
      Will you report full distribution?
      → (yes/no)

  dictionary_assumptions:
    check: using dictionary method
    message: |
      ⚠️ **DICTIONARY ASSUMPTIONS**
      
      Dictionaries assume word = meaning.
      
      Problems in your data:
      
      1. **Negation**: "not happy" → "not" removed, "happy" counted positive
      
      2. **Domain shift**: 
         - General: "sick" = negative
         - Slang: "that's sick!" = positive
      
      3. **Sarcasm**: "Oh great, another update" = negative
      
      4. **Quotes/reported speech**: 
         - "They said 'this is terrible'" 
         - Who's sentiment? Poster or quoted?
      
      5. **Platform-specific**:
         - "ratio" (Twitter) = negative context
         - "based" = positive in some communities
      
      How will you handle these?
      → Strategy: ___
```

### LLM ANNOTATION — Deep Checks

```yaml
llm_annotation_critical:

  llm_not_oracle:
    message: |
      ⚠️ **LLMs ARE NOT GROUND TRUTH**
      
      Critical reminders:
      
      1. **LLMs are trained on internet text**
         - Reflect biases in training data
         - May have political/cultural leanings
         - Confident when wrong
      
      2. **LLMs are inconsistent**
         - Same input → different outputs
         - Temperature affects results
         - Prompt phrasing matters enormously
      
      3. **LLMs are not humans**
         - "Human-like" ≠ "human"
         - Cannot substitute for human judgment
         - Cannot validate themselves
      
      Using LLM annotation without human validation
      is methodologically indefensible.
      
      Your validation plan:
      → Sample size for human coding: ___
      → Who will do human coding: ___
      → Minimum acceptable agreement: ___

  prompt_sensitivity:
    message: |
      ⚠️ **RESULTS DEPEND ON PROMPT WORDING**
      
      Small prompt changes → big result changes.
      
      Example:
      Prompt A: "Is this post positive or negative?"
      Prompt B: "What is the sentiment of this post?"
      → Can give different results
      
      Example:
      "Classify as misinformation" vs
      "Classify as potentially misleading"
      → Very different thresholds
      
      You must:
      1. Document exact prompt used
      2. Test prompt variations
      3. Report sensitivity analysis
      
      Have you tested prompt variations?
      → (yes, results were stable / yes, results varied / no)
      
      If varied, which version and why?
      → Justification: ___

  model_choice_bias:
    message: |
      ⚠️ **DIFFERENT MODELS, DIFFERENT RESULTS**
      
      GPT-4, Claude, Gemini will give different labels.
      
      This is not a bug — it reveals:
      - Task ambiguity
      - Cultural/political variation in training
      - Different "perspectives"
      
      For robust findings:
      - Use multiple models
      - Report agreement across models
      - Human adjudicate disagreements
      
      Or acknowledge single-model limitation.
      
      Your approach:
      → (single model / multi-model / human hybrid)
```

### COORDINATED BEHAVIOR — Deep Checks

```yaml
coordinated_behavior_critical:

  threshold_justification:
    message: |
      ⚠️ **THRESHOLD JUSTIFICATION REQUIRED**
      
      You're using:
      - Time window: {time_threshold} seconds
      - Min co-shares: {min_weight}
      
      These numbers determine who gets flagged as "coordinated."
      
      Questions:
      
      1. **Where did these numbers come from?**
         - [ ] Literature (cite: ___)
         - [ ] Empirical testing on this data
         - [ ] Default values
         - [ ] Intuition
      
      2. **What's the false positive rate?**
         - At these thresholds, what % of organic sharing gets flagged?
         - Have you checked?
      
      3. **What's the false negative rate?**
         - What coordination might you be missing?
         - Slower coordination? Cross-platform?
      
      4. **Sensitivity analysis done?**
         - How do results change at threshold ± 50%?
      
      Justify your thresholds: ___

  coordination_types:
    message: |
      ⚠️ **COORDINATION IS NOT MONOLITHIC**
      
      Your method detects temporal co-sharing.
      
      But coordination takes many forms:
      
      | Type | Your method detects? |
      |------|---------------------|
      | Rapid retweet bursts | ✓ Yes |
      | Scheduled posting | ✗ No (same time daily) |
      | Narrative alignment | ✗ No (different content) |
      | Cross-platform | ✗ No (unless linked) |
      | Hashtag hijacking | Partially |
      | Reply coordination | Different method needed |
      
      What coordination are you actually studying?
      → Target behavior: ___
      
      What might you miss?
      → Blind spots: ___

  accusation_ethics:
    message: |
      🛑 **ETHICAL CHECKPOINT: COORDINATION ACCUSATIONS**
      
      Flagging accounts as "coordinated" has consequences:
      - Platform suspension
      - Reputational harm
      - Potential legal issues
      - Harassment from others
      
      Before publishing or reporting:
      
      1. **Is "coordinated" the right framing?**
         - "Coordinated" implies intentional
         - Could be: community, shared interest, news cycle
      
      2. **Are you naming individuals?**
         - Public figures: more acceptable
         - Private individuals: high harm potential
         - Pseudonymous accounts: still people
      
      3. **Have you contacted them?**
         - Right of reply before publication?
      
      4. **What's your confidence level?**
         - "Possibly coordinated" vs "definitely coordinated"
         - Confidence intervals?
      
      5. **What's the harm of false positives?**
         - Activists mislabeled as bots
         - Minority communities flagged
         - Legitimate movements delegitimized
      
      Your ethical framework:
      → Naming policy: ___
      → Confidence threshold for claims: ___
      → False positive mitigation: ___
```

---

## LEVEL 3: Output Interpretation Checks

Run AFTER analysis, BEFORE interpretation.

```yaml
post_analysis_checks:

  confirmation_bias_check:
    message: |
      📋 **CONFIRMATION BIAS CHECK**
      
      Your results show: {summary}
      
      Earlier, you said you expected: {expected_finding}
      
      Questions:
      
      1. **Do results match expectations?**
         → (yes / no / partially)
      
      2. **If yes: Are you sure it's not confirmation bias?**
         - Did you look for disconfirming evidence?
         - Did you test alternative explanations?
         
      3. **If no: Are you dismissing unexpected findings?**
         - Unexpected doesn't mean wrong
         - Could reveal something interesting
      
      What would change your interpretation?
      → Alternative evidence needed: ___

  effect_size_vs_significance:
    message: |
      📋 **EFFECT SIZE CHECK**
      
      Statistical significance ≠ practical importance.
      
      Your finding: {finding}
      
      Questions:
      
      1. **Is this effect large enough to matter?**
         - 2% difference may be significant with N=100,000
         - But is 2% meaningful in real terms?
      
      2. **What's the baseline?**
         - "30% of accounts are coordinated"
         - Compared to what? What's normal?
      
      3. **Confidence intervals?**
         - Point estimate vs range of plausible values
      
      Restate finding with practical magnitude:
      → Substantive interpretation: ___

  generalizability:
    message: |
      📋 **GENERALIZABILITY CHECK**
      
      Your data: {data_description}
      
      Your findings generalize to:
      - [ ] This specific dataset only
      - [ ] This platform (at this time)
      - [ ] This topic/community
      - [ ] Broader population (justify)
      
      What are you NOT claiming?
      → Scope limitations: ___
      
      Would findings replicate with:
      - Different time period?
      - Different platform?
      - Different data collection method?
      
      → Replication expectations: ___

  alternative_explanations:
    message: |
      📋 **ALTERNATIVE EXPLANATIONS**
      
      Your interpretation: {interpretation}
      
      Before concluding, consider:
      
      1. **Data artifact?**
         - Could this be a collection bias?
         - API quirk? Platform change?
      
      2. **Method artifact?**
         - Would different parameters give different results?
         - Would different method give different results?
      
      3. **Confounding?**
         - What else correlates with your finding?
         - Have you controlled for it?
      
      4. **Reverse causation?**
         - Does A cause B, or B cause A?
      
      5. **Third variable?**
         - Does C cause both A and B?
      
      Name 2 alternative explanations you've considered:
      → Alternative 1: ___
      → Alternative 2: ___
      → Why your interpretation is better: ___
```

---

## LEVEL 3B: Cross-Model Validation Protocol

When using multiple LLMs for analysis or annotation, document convergence.

```yaml
cross_model_validation:

  convergence_documentation:
    trigger: analysis uses 2+ different LLMs
    message: |
      📋 **CROSS-MODEL CONVERGENCE CHECK**
      
      You used multiple models: {models_used}
      
      Document convergence for each major finding:
      
      | Finding | Model 1 | Model 2 | Model 3 | Convergence |
      |---------|---------|---------|---------|-------------|
      | ___     | ✓/✗     | ✓/✗     | ✓/✗     | Full/Partial/None |
      
      CONFIDENCE LEVELS:
      - **FULL CONVERGENCE** (all models agree): High confidence
        → Report as main finding
      
      - **PARTIAL CONVERGENCE** (majority agree): Moderate confidence
        → Report with caveat, note dissent
      
      - **NO CONVERGENCE** (models disagree): Low confidence
        → Flag for human review
        → Do NOT report as finding without human adjudication
      
      ⚠️ EXAMPLES FROM AGENTACADEMY:
      
      ✅ High confidence (3/3 agreed):
      - Cuba as major amplifier in Ukraine data
      - 70% pro-government in Kashmir data
      - 87-94% law enforcement mentions in CNN data
      
      ⚠️ Partial (interpretation differed):
      - "Solidarity" vs "safety-seeking" for high RT rates
      - Effect size classifications varied
      
      Document your convergences:
      → Full convergence findings: ___
      → Partial convergence findings: ___
      → Divergent findings (needs human review): ___

  divergence_handling:
    trigger: models disagree on finding
    message: |
      📋 **MODEL DIVERGENCE DETECTED**
      
      Models disagree on: {finding}
      
      Model A says: {model_a_interpretation}
      Model B says: {model_b_interpretation}
      
      This divergence is VALUABLE, not a problem.
      It reveals:
      - Ambiguity in the data
      - Multiple valid interpretations
      - Need for human judgment
      
      OPTIONS:
      1. **Both valid**: Report both interpretations
      2. **Theoretical preference**: Choose based on your framework
      3. **Empirical resolution**: Additional analysis to discriminate
      4. **Human adjudication**: Expert makes call
      
      Your resolution: ___
      Justification: ___

  cross_review_errors:
    trigger: one model reviews another's output
    message: |
      📋 **CROSS-REVIEW ERROR LOG**
      
      When Model B reviewed Model A's analysis, errors were caught:
      
      ⚠️ LOG ALL ERRORS (for transparency & learning)
      
      | Error Type | Description | Caught By | Severity |
      |------------|-------------|-----------|----------|
      | ___        | ___         | ___       | Low/Med/High |
      
      COMMON ERROR TYPES (from AgentAcademy):
      - **Sign errors**: Negative correlation reported as positive effect
      - **Classification inflation**: "Medium" effect called "large"
      - **Transformation omission**: Raw correlation without log-transform
      - **Missing confounds**: Didn't control for known factors
      - **Temporal inconsistency**: Period labels contradict values
      
      Errors caught improve the final analysis.
      Document them to improve future prompts.
      
      Errors found: ___
      Corrections made: ___
```

---

## LEVEL 4: Pre-Publication Checks

Before any output leaves the system.

```yaml
pre_publication:

  reproducibility_check:
    message: |
      📋 **REPRODUCIBILITY CHECKLIST**
      
      Could another researcher replicate this?
      
      - [ ] Data collection method documented
      - [ ] All parameters recorded
      - [ ] Code available
      - [ ] Random seeds set
      - [ ] Preprocessing steps documented
      - [ ] Software versions recorded
      - [ ] Limitations stated
      
      Missing items: ___

  limitation_section:
    message: |
      📋 **LIMITATIONS DOCUMENTATION**
      
      Every study has limitations. Yours include:
      
      Auto-detected:
      {auto_detected_limitations}
      
      Add any others:
      → Additional limitations: ___
      
      These will be included in METHODS.md output.

  claim_strength_audit:
    message: |
      📋 **CLAIM STRENGTH AUDIT**
      
      Review your planned claims:
      
      | Claim | Evidence strength | Appropriate? |
      |-------|-------------------|--------------|
      | {claim_1} | {evidence_1} | ? |
      | {claim_2} | {evidence_2} | ? |
      
      Hedging guide:
      - Strong evidence: "X is associated with Y"
      - Moderate evidence: "X appears to be associated with Y"
      - Weak evidence: "X may be associated with Y"
      - Exploratory: "We observed a pattern suggesting..."
      
      Review and adjust claim language.
```

---

## Implementation: Friction by Design

The system should create **productive friction**:

1. **Cannot skip critical checks** — Some checks are mandatory
2. **Active responses required** — "yes/no" not enough, must fill blanks
3. **Logged for reproducibility** — All responses saved in METHODS.md
4. **Escalating warnings** — Ignore warning → stronger warning
5. **Peer review hooks** — Share checks with collaborators

```yaml
friction_settings:
  # Checks that CANNOT be skipped
  mandatory:
    - data_provenance
    - llm_validation_plan
    - coordination_ethics
    - claim_strength_audit
  
  # Checks that require typed responses (not just yes/no)
  require_justification:
    - threshold_justification
    - num_topics_forcing
    - preprocessing_consequences
    - boundary_specification
  
  # If user tries to skip, escalate
  escalation:
    attempt_1: "This check is recommended. Skip anyway? (yes/no)"
    attempt_2: "⚠️ Skipping this check may compromise research validity. Document reason for skipping: ___"
    attempt_3: "🛑 This check is mandatory for this method. Cannot proceed without completion."
```
