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
