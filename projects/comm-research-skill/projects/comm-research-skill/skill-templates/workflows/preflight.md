# Preflight Check System

Before executing any analysis, the agent MUST run through contextual checks and surface potential issues with default settings.

---

## When to Trigger Preflight

Run preflight checks when user requests:
- Coordinated behavior detection
- Network analysis
- LLM annotation
- Topic modeling
- Any full pipeline analysis

---

## Preflight Protocol

### Step 1: Detect Context

Extract from user request:
- Platform mentioned (Twitter, Telegram, Reddit, etc.)
- Time period
- Research question type
- Data characteristics (if known)

### Step 2: Check for Mismatches

Compare detected context against default parameters and FLAG potential issues.

---

## Context-Aware Warnings

### Platform-Specific Warnings

```yaml
warnings:
  twitter:
    - check: time_threshold > 120
      message: |
        ⚠️ **Time threshold may be too long for Twitter**
        Default: {current_value} seconds
        Twitter retweets typically happen within 30-60 seconds.
        
        For Twitter data, consider:
        - 30-60 seconds for retweet coordination
        - 300+ seconds only for cross-platform studies
        
        Keep current setting? (yes/no/adjust to ___) 

  telegram:
    - check: time_threshold < 300
      message: |
        ⚠️ **Time threshold may be too short for Telegram**
        Default: {current_value} seconds
        Telegram forwarding is typically slower than Twitter.
        
        For Telegram data, consider:
        - 300-3600 seconds for group forwarding
        - 60 seconds only for bot-driven channels
        
        Keep current setting? (yes/no/adjust to ___)

  reddit:
    - check: time_threshold < 600
      message: |
        ⚠️ **Time threshold may be too short for Reddit**
        Reddit cross-posting culture is slower.
        Consider 600-3600 seconds.
        
        Keep current setting? (yes/no/adjust to ___)
```

### Content Heterogeneity Warnings

```yaml
warnings:
  mixed_content_types:
    - check: content_types_detected > 1
      message: |
        ⚠️ **Mixed content types detected**
        
        Your dataset appears to contain:
        {detected_types}
        
        EXAMPLE FROM AGENTACADEMY:
        CNN dataset mixed TV transcripts (4,500 words avg) with
        web articles (700 words avg). Direct comparison invalid.
        
        Problems:
        - Word counts not comparable
        - Engagement baselines differ
        - Topic models behave differently
        
        Options:
        - Analyze separately, compare patterns
        - Filter to single type
        - Control for content type
        - Normalize within type
        
        Your approach? ___

  temporal_clustering:
    - check: max_period_pct > 30 OR min_period_pct < 5
      message: |
        ⚠️ **Uneven temporal distribution detected**
        
        Your data clusters around specific periods:
        {period_distribution}
        
        EXAMPLE FROM AGENTACADEMY:
        CNN 2015: June had 4x more articles than September
        (Charleston shooting drove coverage spike)
        
        Problems:
        - "Average" dominated by peak periods
        - Comparing periods = comparing events
        - Statistical independence assumption violated
        
        Options:
        - Weight by inverse frequency
        - Analyze peaks separately
        - Normalize within event windows
        - Acknowledge as limitation
        
        Your approach? ___
```

### Data Size Warnings

```yaml
warnings:
  small_dataset:
    - check: total_posts < 1000
      message: |
        ⚠️ **Small dataset detected ({total_posts} posts)**
        
        With limited data:
        - Coordination patterns may be coincidental
        - Statistical significance is harder to establish
        - Consider lowering min_edge_weight to 2
        
        Current min_edge_weight: {current_value}
        Recommended for small data: 2
        
        Adjust? (yes/no)

  large_dataset:
    - check: total_posts > 100000
      message: |
        ⚠️ **Large dataset detected ({total_posts} posts)**
        
        With high-volume data:
        - False positives increase (random co-occurrence)
        - Consider raising min_edge_weight to 4-5
        - Consider tighter time threshold
        
        Current min_edge_weight: {current_value}
        Recommended for large data: 4+
        
        Adjust? (yes/no)
```

### Research Question Warnings

```yaml
warnings:
  coordination_authenticity:
    - trigger: user mentions "inauthentic" or "bots" or "astroturf"
      message: |
        ⚠️ **Coordination ≠ Inauthenticity**
        
        This method detects COORDINATION patterns.
        It cannot determine:
        - Whether actors are bots or humans
        - Whether coordination is malicious or legitimate
        - The intent behind coordinated activity
        
        Legitimate coordination examples:
        - Social movements, activists
        - News organizations
        - PR/communications teams
        - Fan communities
        
        The system will flag coordination patterns.
        YOU must interpret authenticity based on:
        - Account characteristics
        - Content analysis
        - Contextual knowledge
        
        Understood? (yes/continue)

  small_groups:
    - trigger: user studying "small communities" or "niche groups"
      message: |
        ⚠️ **Small community considerations**
        
        In small groups, coordination is NORMAL:
        - Members know each other
        - Shared interests = shared content
        - Organic coordination is common
        
        Consider:
        - Higher thresholds for "suspicious"
        - Qualitative validation required
        - Anonymization especially important
        
        Proceed with caution? (yes/continue)
```

### LLM Annotation Warnings

```yaml
warnings:
  default_categories:
    - check: using_default_categories == true
      message: |
        ⚠️ **Using default annotation categories**
        
        Default categories: {default_categories}
        
        These may not fit your research:
        - Political comm → need campaign, attack, policy categories?
        - Health comm → need misinformation, personal story categories?
        - Your subfield → need custom categories?
        
        Options:
        1. Keep defaults
        2. Edit categories in config.yaml
        3. Tell me your categories now
        
        Your choice?

  validation_reminder:
    - trigger: llm_annotation_requested
      message: |
        📋 **LLM annotation validation required**
        
        Before trusting LLM labels:
        1. I will sample {validation_sample_size} items
        2. You (or a coder) should label them manually
        3. We compare LLM vs human (inter-rater reliability)
        4. Only proceed if κ ≥ 0.7
        
        This is standard practice per Davidson & Karell (2025).
        
        Proceed with validation plan? (yes/skip validation)
```

---

## Preflight Conversation Template

When user requests analysis, agent responds:

```
📋 **PREFLIGHT CHECK: Coordinated Behavior Detection**

I detected:
- Platform: Telegram
- Dataset: ~15,000 posts
- Research focus: vaccine misinformation

Current settings:
- Time threshold: 60 seconds
- Min edge weight: 2
- Content signals: URLs, hashtags

⚠️ **Potential issues:**

1. **Time threshold seems short for Telegram**
   Telegram forwarding is slower than Twitter.
   → Recommended: 300-600 seconds
   → Keep 60 / Change to ___?

2. **Dataset is medium-sized**
   Current settings are reasonable.
   → No change needed

3. **Studying misinformation**
   Reminder: Coordination ≠ Misinformation
   → Coordinated health advocates exist
   → Manual review required for interpretation
   → Acknowledged? (yes/no)

Ready to proceed after you confirm settings.
```

---

## Post-Analysis Sanity Checks

After running analysis, check results:

```yaml
sanity_checks:
  - check: largest_cluster > 50% of accounts
    warning: |
      ⚠️ **Unusually large cluster detected**
      {largest_cluster_pct}% of accounts in one cluster.
      
      This could mean:
      - Threshold too loose (catching organic sharing)
      - Genuine large-scale coordination
      - Data quality issue
      
      Recommend manual review before interpretation.

  - check: avg_time_delta < 5 seconds
    warning: |
      ⚠️ **Extremely fast coordination detected**
      Average time between co-shares: {avg_delta} seconds
      
      This suggests:
      - Automated/bot activity
      - Or data timestamp precision issue
      
      Verify data quality before concluding "bots."

  - check: no_clusters_found
    info: |
      ℹ️ **No coordination clusters found**
      
      This could mean:
      - No coordination in data (legitimate finding)
      - Threshold too tight
      - Time window too narrow
      - Insufficient data
      
      Consider relaxing parameters and re-running.
```

---

---

## Method-Specific Preflight Checks

### TOPIC MODELING

```yaml
topic_modeling_checks:
  
  num_topics:
    - check: num_topics is manually set AND dataset_size < num_topics * 50
      warning: |
        ⚠️ **Too many topics for dataset size**
        You set {num_topics} topics, but only have {dataset_size} documents.
        Rule of thumb: need ~50+ docs per topic for stability.
        
        Options:
        - Reduce to {recommended_topics} topics
        - Use auto-detection (num_topics: 0)
        - Proceed anyway (results may be unstable)
        
        Your choice?

  language:
    - check: detected_language != config_language
      warning: |
        ⚠️ **Language mismatch detected**
        Config language: {config_language}
        Detected in data: {detected_language} ({pct}% of posts)
        
        Wrong language setting affects:
        - Stopword removal
        - Tokenization
        - Embedding quality
        
        Change to {detected_language}? (yes/no/mixed-language)

  short_texts:
    - check: avg_doc_length < 50 words
      warning: |
        ⚠️ **Short documents detected**
        Average length: {avg_length} words
        
        Topic modeling works best with longer texts.
        For short texts (tweets, comments), consider:
        - Aggregating by user/thread
        - Using BERTopic (better for short text)
        - Lowering min_topic_size
        
        Current algorithm: {algorithm}
        Recommended for short text: bertopic
        
        Switch to BERTopic? (yes/no)

  preprocessing:
    - trigger: any topic modeling request
      message: |
        📋 **Preprocessing decisions needed**
        
        These affect results significantly:
        
        1. Remove URLs? (yes/no) 
           - Yes for content focus
           - No if URLs carry meaning
        
        2. Remove mentions/handles? (yes/no)
           - Yes for topic clarity
           - No for interaction analysis
        
        3. Minimum document frequency? 
           - Default: 5 (word must appear in 5+ docs)
           - Lower for small datasets
        
        4. Remove hashtags? (yes/no)
           - Often useful to keep for social media
        
        Confirm or adjust:
```

### NETWORK ANALYSIS

```yaml
network_analysis_checks:

  network_type:
    - trigger: network analysis requested
      message: |
        📋 **What type of network?**
        
        Different networks need different approaches:
        
        1. **Follower/following network**
           - Directed graph
           - Centrality = influence
           
        2. **Retweet/share network**
           - Directed (who shared whom)
           - Shows information flow
           
        3. **Mention/reply network**
           - Can be directed or undirected
           - Shows conversation structure
           
        4. **Co-occurrence network**
           - Undirected (shared hashtags, URLs)
           - Shows topic clustering
           
        5. **Coordination network**
           - Undirected, weighted
           - Shows synchronized behavior
        
        Which type are you building?

  directed_vs_undirected:
    - check: network_type in [retweet, follower, mention] AND graph_is_undirected
      warning: |
        ⚠️ **Consider directed graph**
        For {network_type} networks, direction matters:
        - A follows B ≠ B follows A
        - A retweets B shows information flow
        
        Undirected loses this information.
        Switch to directed? (yes/no)

  isolates:
    - check: pct_isolates > 30
      warning: |
        ⚠️ **Many isolated nodes ({pct_isolates}%)**
        {num_isolates} accounts have no connections.
        
        This could mean:
        - Threshold too strict
        - Data collection incomplete
        - Legitimate finding (fragmented network)
        
        Options:
        - Remove isolates from analysis
        - Lower connection threshold
        - Keep and report fragmentation
        
        Your choice?

  centrality_interpretation:
    - trigger: centrality analysis
      message: |
        📋 **Centrality measure selection**
        
        Different measures answer different questions:
        
        | Measure | Question |
        |---------|----------|
        | **Degree** | Who has the most connections? |
        | **Betweenness** | Who bridges communities? |
        | **Eigenvector** | Who's connected to important people? |
        | **PageRank** | Who receives most attention flow? |
        | **Closeness** | Who can reach others fastest? |
        
        For communication research:
        - Influence studies → PageRank, Eigenvector
        - Gatekeepers → Betweenness
        - Popularity → Degree
        - Information access → Closeness
        
        Which measures for your research question?
```

### SENTIMENT ANALYSIS

```yaml
sentiment_analysis_checks:

  dictionary_choice:
    - trigger: sentiment analysis requested
      message: |
        📋 **Sentiment approach selection**
        
        Options with tradeoffs:
        
        1. **VADER** (default for social media)
           ✓ Handles emoji, slang, caps
           ✗ English-only
           ✗ General-purpose (not domain-specific)
        
        2. **TextBlob**
           ✓ Simple, fast
           ✗ Less accurate on social media
        
        3. **Domain-specific dictionary**
           ✓ Tailored to your context
           ✗ Requires building/validating
        
        4. **LLM-based**
           ✓ Most nuanced
           ✓ Handles context, sarcasm
           ✗ Expensive at scale
           ✗ Requires validation
        
        Your domain: {detected_subfield}
        Recommended: {recommendation}
        
        Your choice?

  language_coverage:
    - check: detected_languages includes non_english AND tool is VADER
      warning: |
        ⚠️ **Non-English content detected**
        {pct_non_english}% of posts appear non-English.
        Languages detected: {languages}
        
        VADER only works for English.
        
        Options:
        - Filter to English only (lose {pct_non_english}% data)
        - Use multilingual model (XLM-RoBERTa)
        - Translate then analyze (introduces noise)
        - Separate analysis by language
        
        Your choice?

  sarcasm_irony:
    - check: domain in [political, memes, youth]
      warning: |
        ⚠️ **Sarcasm/irony likely in this data**
        
        Political/meme content often uses:
        - Sarcasm ("Great job, genius")
        - Irony
        - Mocking quotes
        
        Dictionary methods will misclassify these.
        
        Recommendations:
        - Use LLM annotation for ambiguous cases
        - Sample and manually validate
        - Report limitation in methods
        
        Acknowledged?

  domain_specific:
    - check: domain == health AND using_general_sentiment
      warning: |
        ⚠️ **Health domain detected**
        
        General sentiment tools may misclassify:
        - "Vaccine side effects" → negative? (neutral medical term)
        - "Cancer survivor" → negative? (positive framing)
        - Clinical language → neutral? (may have emotional weight)
        
        Consider:
        - Health-specific lexicon
        - LLM with health context
        - Manual validation on health terms
        
        Proceed with general tool? (yes/switch to LLM)
```

### LLM ANNOTATION

```yaml
llm_annotation_checks:

  category_design:
    - trigger: llm annotation requested
      message: |
        📋 **Category scheme design**
        
        Good categories are:
        ✓ Mutually exclusive (one category per item)
        ✓ Exhaustive (covers all content)
        ✓ Clear definitions (coder can apply consistently)
        
        Your categories: {categories}
        
        Questions to consider:
        1. Can one post fit multiple categories?
           → Need multi-label or hierarchy?
        
        2. What about ambiguous/unclear posts?
           → Need "unclear" or "other" category?
        
        3. Are definitions specific enough?
           → "Political" = about policy? elections? politicians?
        
        Refine categories? (yes/no)

  model_selection:
    - trigger: llm annotation requested
      message: |
        📋 **Model selection for annotation**
        
        Tradeoff: Cost vs. Quality
        
        | Model | Cost/1M tokens | Best for |
        |-------|----------------|----------|
        | Gemini Flash | ~$0.08 | Bulk, clear cases |
        | GPT-4o-mini | ~$0.15 | Balanced |
        | Claude Sonnet | ~$3 | Complex reasoning |
        | GPT-4o | ~$5 | Highest quality |
        
        Strategy options:
        1. **All cheap**: Fast, may miss nuance
        2. **All expensive**: High quality, costly
        3. **Tiered**: Cheap first, expensive for low-confidence
        
        Dataset size: {dataset_size}
        Estimated cost (cheap): ${cheap_estimate}
        Estimated cost (expensive): ${expensive_estimate}
        
        Your choice?

  validation_required:
    - trigger: llm annotation requested
      message: |
        ⚠️ **Validation is required, not optional**
        
        LLM annotation is NOT ground truth.
        
        Required steps:
        1. Sample {sample_size} items randomly
        2. You or RA codes them manually
        3. Calculate agreement (Cohen's κ)
        4. Only proceed if κ ≥ 0.7
        
        If κ < 0.7:
        - Revise category definitions
        - Add few-shot examples
        - Try different model
        - Re-run validation
        
        This is non-negotiable for publication.
        
        Ready to proceed with validation plan?

  prompt_engineering:
    - trigger: llm annotation requested
      message: |
        📋 **Prompt design choices**
        
        1. **Zero-shot** (just categories + definitions)
           - Faster to set up
           - Works for clear categories
        
        2. **Few-shot** (include examples)
           - Better for ambiguous cases
           - Need 3-5 examples per category
           - Examples should include edge cases
        
        3. **Chain-of-thought** (ask for reasoning)
           - Slower, more expensive
           - Better for complex judgment
           - Helps debug errors
        
        Do you have labeled examples available?
        (yes → few-shot / no → zero-shot)
```

### CONTENT ANALYSIS (Manual/Hybrid)

```yaml
content_analysis_checks:

  sampling:
    - trigger: content analysis requested
      message: |
        📋 **Sampling strategy**
        
        Dataset size: {dataset_size}
        
        Options:
        1. **Random sample** 
           - Size: {recommended_sample} for 95% CI, ±5%
           - Simple but may miss rare categories
        
        2. **Stratified sample**
           - Ensure coverage across time/source/topic
           - Better representativeness
        
        3. **Purposive sample**
           - Focus on specific cases
           - Not generalizable
        
        4. **Full population**
           - Only feasible with automation
           - Need LLM or trained classifier
        
        Your approach?

  reliability:
    - trigger: manual coding mentioned
      message: |
        📋 **Inter-coder reliability plan**
        
        For publishable content analysis:
        
        1. **How many coders?**
           - Minimum: 2
           - Recommended: 2-3
        
        2. **Training**
           - Code together first
           - Discuss disagreements
           - Refine codebook
        
        3. **Reliability sample**
           - {reliability_sample_pct}% coded by all coders
           - Calculate agreement (Krippendorff's α or Cohen's κ)
           - Target: α ≥ 0.8 (content), α ≥ 0.7 (interpretation)
        
        4. **Disagreement resolution**
           - Discussion to consensus
           - Third coder tiebreak
           - Majority vote
        
        Your plan?
```

---

## Multi-Model Analysis Protocol

When using multiple LLMs for analysis (recommended for robust findings):

```yaml
multi_model_checks:

  convergence_planning:
    - trigger: multi-model analysis requested
      message: |
        📋 **MULTI-MODEL CONVERGENCE PROTOCOL**
        
        Using multiple models increases confidence in findings.
        
        PROTOCOL (from AgentAcademy):
        
        1. **Run models independently**
           - Same data, same prompts
           - No cross-contamination of outputs
        
        2. **Compare findings BEFORE interpretation**
           - What do all models agree on? → High confidence
           - What do most agree on? → Moderate confidence
           - What do models disagree on? → Flag for review
        
        3. **Document convergence**
           | Finding | Claude | GLM | Kimi | Confidence |
           |---------|--------|-----|------|------------|
           | ___     |        |     |      |            |
        
        4. **Cross-review (optional but valuable)**
           - Have Model B critique Model A's output
           - Catches sign errors, classification inflation
        
        Models you're using: ___
        Convergence threshold for "finding": ___

  divergence_value:
    - trigger: models disagree
      message: |
        📋 **MODEL DIVERGENCE IS VALUABLE**
        
        Models disagree on: {finding}
        
        This is not a bug—it reveals:
        - Task ambiguity
        - Multiple valid interpretations
        - Need for human judgment
        
        EXAMPLES FROM AGENTACADEMY:
        
        ✅ Convergence (3/3):
        - Cuban state media in Ukraine data
        - 70% pro-government in Kashmir
        
        ⚠️ Divergence (interpretation):
        - "Solidarity" vs "safety-seeking" for RT behavior
        - Both valid, different theoretical lenses
        
        Resolution options:
        1. Report both interpretations
        2. Choose based on your theory
        3. Additional analysis to discriminate
        4. Human expert makes call
        
        Your resolution approach? ___
```

---

## User Override

Users can skip preflight with explicit flag:

```yaml
# In config.yaml
preflight:
  enabled: true           # Set to false to skip (not recommended)
  require_confirmation: true
  log_warnings: true      # Always log even if skipped
```

But warnings are ALWAYS logged for reproducibility documentation.

---

## Implementation Note

When executing analysis, agent MUST:

1. Run preflight checks
2. Present warnings conversationally
3. Wait for user confirmation on flagged items
4. Log all warnings and user responses
5. Include in METHODS.md output

**Never silently use defaults that may be inappropriate.**
