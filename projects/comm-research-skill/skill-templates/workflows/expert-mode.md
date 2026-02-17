# Expert Mode: Fast-Track for Experienced Researchers

**Purpose:** Experienced researchers shouldn't be interrogated every time. This workflow enables efficient interaction while maintaining rigor.

---

## Engagement Tiers

### Tier 1: Novice
**Who:** First-time users, students learning methods
**Experience:**
- Full probing questions for every method
- Explanations with each question
- Recommended readings suggested
- Competence verification required

### Tier 2: Intermediate  
**Who:** Researchers familiar with methods, some computational experience
**Experience:**
- Spot-check questions (key decisions only)
- Assumes terminology understanding
- Skip explanations unless asked
- Competence verified once per method

### Tier 3: Expert
**Who:** Published researchers, demonstrated competence
**Experience:**
- Fast-track mode: specify params, skip quiz
- Technical shorthand accepted
- Challenge on edge cases only
- Competence cached indefinitely

---

## How Expert Mode Works

### Fast-Track Request Format

Experts can use structured requests that pre-answer probing questions:

```markdown
## Sentiment Analysis Request (Expert Mode)

**Data:** tweets_vaccine_2026.csv (N=45,000)
**Construct:** Valence (positive/neutral/negative)
**Unit:** Post-level
**Tool:** VADER
**Neutral threshold:** compound score -0.05 to +0.05
**Sarcasm strategy:** Flag via LLM pre-filter, exclude flagged
**Validation:** 200-item human sample, target κ > 0.7

Proceed.
```

**System Response:**
```
✅ Expert request recognized. Parameters complete.

Checklist:
- [x] Construct defined: valence
- [x] Unit specified: post
- [x] Tool justified: VADER
- [x] Neutral handling: ±0.05 threshold
- [x] Sarcasm: LLM pre-filter + exclude
- [x] Validation: 200 items, κ > 0.7

Proceeding with sentiment analysis pipeline.

⚠️ One note: VADER may underperform on vaccine-specific language.
   Consider: domain-specific validation sample.
   
Continue? [Y/proceed anyway]
```

### Standard Expert Templates

```yaml
# Sentiment Analysis
sentiment:
  data: <path>
  construct: valence | emotion | stance
  unit: post | user | aggregated
  tool: vader | textblob | llm | custom
  neutral_threshold: <range>
  sarcasm: detect | exclude | acknowledge
  validation_n: <number>
  validation_target_kappa: <float>

# Topic Modeling
topic_modeling:
  data: <path>
  method: lda | bertopic | nmf
  k: <number> | range(<min>, <max>)
  preprocessing:
    stopwords: <list_name>
    min_df: <float>
    max_df: <float>
    min_length: <int>
  validation: coherence | human | both
  document_unit: post | user | thread

# Network Analysis
network:
  data: <path>
  nodes: users | posts | hashtags
  edges: mentions | retweets | co_occurrence | follows
  directed: true | false
  weighted: true | false
  metrics: [degree, betweenness, eigenvector, ...]
  community_detection: louvain | leiden | none

# Coordinated Behavior
coordination:
  data: <path>
  time_threshold_seconds: <int>
  min_edge_weight: <int>
  content_signals: [urls, hashtags, text_fingerprint]
  baseline_comparison: true | false
  validation_sample: <int>

# LLM Annotation
llm_annotation:
  data: <path>
  categories: [<list>]
  category_definitions: <path_to_codebook>
  strategy: zero_shot | few_shot | cot
  model: <model_name>
  validation_n: <int>
  validation_target_kappa: <float>

# Content Analysis
content_analysis:
  data: <path>
  codebook: <path>
  coders: <int>
  sample_n: <int>
  reliability_metric: kappa | krippendorff
  reliability_target: <float>
```

---

## Competence Verification & Caching

### Initial Verification

When a user first uses a complex method, verify understanding:

```python
def verify_competence(user_id, method):
    """One-time competence check per method."""
    
    questions = COMPETENCE_QUESTIONS[method]
    
    # Ask 3 questions
    responses = ask_questions(questions, sample=3)
    
    # Evaluate responses
    score = evaluate_responses(responses, method)
    
    if score >= 0.67:  # 2/3 correct
        cache_competence(user_id, method)
        return {'status': 'VERIFIED', 'level': 'expert'}
    else:
        return {
            'status': 'NOT_VERIFIED',
            'feedback': generate_feedback(responses),
            'resources': suggest_resources(method)
        }
```

### Competence Cache

```json
{
  "researcher_id": "wayne",
  "competence": {
    "sentiment_analysis": {
      "verified": "2026-02-15",
      "level": "expert"
    },
    "network_analysis": {
      "verified": "2026-02-10", 
      "level": "expert"
    },
    "topic_modeling": {
      "verified": "2026-02-17",
      "level": "intermediate"
    },
    "coordinated_behavior": {
      "verified": null,
      "notes": "Failed verification 2026-02-12, needs review"
    }
  },
  "publications": [
    "doi:10.1234/example1",
    "doi:10.1234/example2"
  ],
  "engagement_tier": "expert"
}
```

### Auto-Upgrade Path

```python
def check_upgrade(user_id):
    """Check if user should be upgraded to higher tier."""
    
    user = get_user_profile(user_id)
    
    # Signals of expertise
    signals = {
        'edits_config_directly': check_config_edits(user_id),
        'uses_technical_terms': check_language_sophistication(user_id),
        'catches_system_errors': check_error_corrections(user_id),
        'provides_detailed_specs': check_request_quality(user_id),
        'methods_verified': len(user['competence'])
    }
    
    # Upgrade thresholds
    if signals['methods_verified'] >= 3 and signals['edits_config_directly']:
        return 'expert'
    elif signals['methods_verified'] >= 1:
        return 'intermediate'
    else:
        return 'novice'
```

---

## Smart Probing

Even in expert mode, some situations warrant questions:

### When to Still Ask (Even Experts)

```yaml
always_ask:
  # Edge cases
  - method: coordinated_behavior
    condition: findings_rate > 30%
    question: "30%+ coordination rate is unusually high. Did you mean to use these thresholds?"
  
  # Data quality issues
  - method: any
    condition: sample_size < 500
    question: "Small sample (N<500). Is this intentional (pilot) or should we collect more?"
  
  # Method mismatch
  - method: lda
    condition: avg_doc_length < 20
    question: "Short documents detected. Consider BERTopic or aggregation?"
    
  # Unusual parameters
  - method: sentiment
    condition: neutral_threshold > 0.3
    question: "Wide neutral zone (±0.3). Most content will be neutral. Intended?"

never_skip:
  - Ethical concerns (vulnerable populations, identification risks)
  - Legal concerns (ToS, GDPR implications)
  - Sanity check failures (implausible results)
```

### Contextual Intelligence

```python
def smart_probe(request, user_tier):
    """Determine what to ask based on user tier and request context."""
    
    if user_tier == 'expert':
        # Only ask about:
        # 1. Anomalies in their request
        # 2. Edge cases they might have missed
        # 3. Data-specific concerns
        
        anomalies = detect_anomalies(request)
        if anomalies:
            return ask_about_anomalies(anomalies)
        
        return {'status': 'PROCEED'}
    
    elif user_tier == 'intermediate':
        # Spot-check key decisions
        key_decisions = get_key_decisions(request.method)
        missing = [k for k in key_decisions if k not in request.params]
        
        if missing:
            return ask_key_decisions(missing)
        
        return {'status': 'PROCEED'}
    
    else:  # novice
        # Full probing
        return full_probe(request)
```

---

## Quick Commands for Experts

### Skip Explanations
```
/noexplain - Turn off explanations for this session
/explain   - Turn explanations back on
```

### Batch Operations
```
/batch sentiment tweets_*.csv --params sentiment_config.yaml
```

### Template Reuse
```
/save-template my_sentiment --from last_run
/use-template my_sentiment --data new_data.csv
```

### Quick Status
```
/status          - Current project state
/params          - Show current parameters
/validate quick  - Run quick validation
```

---

## Interaction Examples

### Novice Interaction
```
User: "Do sentiment analysis on my tweets"

System: 
📋 Before I analyze sentiment, I need some specifications.

1. **What do you mean by "sentiment"?**
   - Positive/negative valence?
   - Specific emotions (anger, joy, fear)?
   - Stance toward a specific topic?

[... 5 more questions ...]
```

### Expert Interaction
```
User: "Sentiment: tweets_climate.csv, VADER, post-level, 
       neutral ±0.05, LLM sarcasm prefilter, 200-item validation"

System:
✅ Running sentiment analysis.

Pipeline:
1. Load tweets_climate.csv
2. Sarcasm pre-filter (LLM)
3. VADER sentiment (neutral: ±0.05)  
4. Sample 200 for validation

ETA: ~15 minutes for 45K posts

[Progress bar]
```

### Edge Case (Expert Gets Questioned)
```
User: "Coordination detection: telegram_health.csv, 
       30 second threshold, min 2 co-shares"

System:
⚠️ Quick check (unusual parameters):

30-second threshold is tight for Telegram. 
Your previous health comm analysis used 300s 
(Telegram forwarding is slower than Twitter).

Did you mean:
A) 30 seconds (keep as specified)
B) 300 seconds (match previous analysis)
C) Let me explain why I chose 30

[A/B/C]
```

---

## Enabling Expert Mode

### For New Users
```
System: I notice you're using technical terminology and 
        specifying parameters directly.
        
        Would you like to:
        A) Continue with guided mode (full explanations)
        B) Switch to expert mode (fast-track, minimal questions)
        
        Expert mode assumes familiarity with methods.
        I'll still flag anomalies and ethical concerns.
```

### Via Config
```yaml
# config.yaml

researcher:
  name: "Wayne"
  engagement_tier: expert
  
  verified_competence:
    - sentiment_analysis
    - network_analysis
    - topic_modeling
    - coordinated_behavior
    - llm_annotation
    - content_analysis
  
  preferences:
    explanations: minimal
    probing: edge_cases_only
    templates: saved_templates/
```

### Via Command
```
/expert on   - Enable expert mode
/expert off  - Return to guided mode
/novice      - Full guided mode
```

---

## Safety Rails

Expert mode doesn't mean no guardrails:

### Always Active
```yaml
non_negotiable:
  - Ethics/IRB check for vulnerable populations
  - Sanity check for implausible results
  - Legal compliance checks
  - Data security reminders
  - Reproducibility documentation

can_be_skipped:
  - Method explanations
  - Terminology definitions
  - Competence quiz (if cached)
  - Probing questions for known parameters
  - Reading recommendations
```

### The "Are You Sure?" Moments

Even experts get asked to confirm:
- Identifying individuals in publication
- Using coordination patterns to claim "bots"
- Analyzing data from repressive regimes
- Any analysis involving minors
- Parameters that produce implausible results

---

*Expert mode respects researcher autonomy while maintaining research integrity.*
