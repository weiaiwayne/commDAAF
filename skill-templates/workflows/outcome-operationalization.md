# Outcome Variable Operationalization

**Purpose:** Force explicit operationalization of dependent/outcome variables, not just independent variables.

---

## The Problem

Research often carefully operationalizes the IV (e.g., "sentiment") but treats DVs as self-evident:

> "We measured engagement" ← What does this mean?

Is engagement:
- Retweets? (endorsement, amplification)
- Likes/favorites? (low-effort acknowledgment)
- Replies? (conversation, controversy)
- Quote tweets? (commentary, often critical)
- Some combination? (how weighted?)

**Different operationalizations = different findings.**

---

## Common Outcome Variables in Comm Research

### Engagement

```yaml
engagement_operationalization:
  
  must_specify:
    - which_metrics: "Retweets? Likes? Replies? Shares?"
    - why_these_metrics: "What does each metric measure conceptually?"
    - aggregation: "Sum? Average? Weighted combination?"
    - normalization: "Raw counts? Per-follower? Log-transformed?"
    - exclusions: "Self-retweets? Bot engagement?"
  
  conceptual_distinctions:
    retweets:
      measures: "Amplification, endorsement, wanting followers to see"
      caveats: "Includes quote tweets by default; controversy gets RTs too"
      
    likes:
      measures: "Low-effort acknowledgment, 'I saw this'"
      caveats: "Meaning varies by platform; may be algorithmic signal"
      
    replies:
      measures: "Conversation, engagement depth"
      caveats: "Includes both positive and negative; harassment looks like engagement"
      
    quote_tweets:
      measures: "Commentary, often disagreement or context-adding"
      caveats: "Frequently negative or critical"
      
    shares:
      measures: "Wanting personal network to see"
      caveats: "Private shares invisible to researchers"
  
  red_flags:
    - combining_without_justification: "Engagement = RT + Likes + Replies is not self-evident"
    - ignoring_normalization: "Account with 1M followers getting 100 RTs ≠ account with 1K followers"
    - treating_as_quality: "High engagement ≠ good content (outrage gets engagement)"
```

### Virality/Reach

```yaml
virality_operationalization:
  
  must_specify:
    - definition: "What counts as 'viral'?"
    - threshold: "Above what number? Based on what?"
    - time_window: "Viral in an hour? A day? Ever?"
    - relative_to: "Relative to account size? Topic? Platform average?"
  
  common_operationalizations:
    absolute_threshold: "More than X retweets"
    percentile: "Top X% of posts in dataset"
    ratio_based: "Engagement / followers above threshold"
    cascade: "N levels of sharing"
  
  problems:
    - arbitrary_thresholds: "Why is 10,000 RTs viral but 9,999 is not?"
    - survivorship_bias: "We only study what went viral, not what didn't"
    - platform_dependence: "Viral on Twitter ≠ viral on TikTok"
```

### Influence

```yaml
influence_operationalization:

  must_specify:
    - influence_on_what: "Attitudes? Behaviors? Attention? Beliefs?"
    - influence_mechanism: "Information exposure? Persuasion? Social pressure?"
    - measurement_method: "Network centrality? Survey? Behavioral trace?"
  
  centrality_is_not_influence:
    warning: |
      High network centrality ≠ influence
      
      Centrality measures STRUCTURE:
      - Degree: connected to many
      - Betweenness: bridges communities
      - Eigenvector: connected to well-connected
      
      None of these measure IMPACT on beliefs or behaviors.
      
      To claim influence, you need:
      - Causal evidence of attitude/behavior change, OR
      - At minimum, acknowledge centrality ≠ influence
  
  follower_count_is_not_influence:
    warning: |
      Followers ≠ influence
      
      - Followers can be bought
      - Followers may not see content (algorithmic filtering)
      - Followers may ignore content
      - Follower count ≠ engagement
```

### Sentiment (as DV)

```yaml
sentiment_as_outcome:
  
  must_specify:
    - whose_sentiment: "Author? Audience? Quoted source?"
    - toward_what: "General? Toward specific entity? Toward topic?"
    - when_measured: "At posting? After engagement? Aggregated over time?"
  
  common_problems:
    - aggregate_sentiment_meaningless: "Mean sentiment = 0.2 could be consensus OR polarization"
    - direction_without_intensity: "Slightly positive ≠ extremely positive"
    - missing_distribution: "Always report distribution, not just mean"
```

---

## Operationalization Checklist

**For EVERY outcome variable, answer:**

```yaml
outcome_variable_checklist:
  
  1_conceptual:
    - "What concept are you trying to measure?"
    - "Why does this concept matter for your RQ?"
    - "What does existing literature use?"
  
  2_operational:
    - "What data will you use as a proxy for this concept?"
    - "Why is this proxy valid for this concept?"
    - "What does high/low values mean substantively?"
  
  3_measurement:
    - "What's the unit of analysis?"
    - "How will you aggregate if needed?"
    - "Will you normalize? How?"
    - "What transformations will you apply?"
  
  4_validity:
    - "Does this proxy actually capture the concept?"
    - "What does this proxy MISS about the concept?"
    - "Could something else affect the proxy besides your IV?"
  
  5_alternatives:
    - "What other operationalizations could you use?"
    - "Would you get the same results with different operationalization?"
    - "Robustness check: try multiple operationalizations"
```

---

## Implementation

```python
def outcome_operationalization_check(outcome_name, operationalization):
    """
    Validate that outcome variable is properly operationalized.
    
    Args:
        outcome_name: Name of the outcome variable (e.g., "engagement")
        operationalization: Dict describing how it's measured
    
    Returns:
        Validation result with warnings/requirements
    """
    
    required_fields = [
        'concept',        # What are you trying to measure?
        'proxy_variables', # What data variables represent this?
        'aggregation',    # How are multiple measures combined?
        'justification',  # Why is this a valid operationalization?
    ]
    
    warnings = []
    missing = []
    
    # Check required fields
    for field in required_fields:
        if field not in operationalization:
            missing.append(field)
    
    # Check for common issues
    if 'engagement' in outcome_name.lower():
        if operationalization.get('proxy_variables'):
            proxies = operationalization['proxy_variables']
            
            # Mixing different engagement types without justification
            if len(proxies) > 1 and not operationalization.get('combination_justification'):
                warnings.append({
                    'type': 'missing_combination_justification',
                    'message': f"You're combining {proxies}. These measure different things. Justify why combining them is valid.",
                })
            
            # No normalization for follower count
            if not operationalization.get('normalization'):
                warnings.append({
                    'type': 'no_normalization',
                    'message': "Engagement without normalization favors large accounts. Consider per-follower rates.",
                })
    
    if 'influence' in outcome_name.lower():
        if 'centrality' in str(operationalization.get('proxy_variables', [])).lower():
            warnings.append({
                'type': 'centrality_as_influence',
                'message': "Centrality measures structure, not influence. You need causal evidence to claim influence.",
            })
    
    # Check for treating proxy as ground truth
    if not operationalization.get('limitations'):
        warnings.append({
            'type': 'no_limitations',
            'message': "Every operationalization has limitations. Document what your proxy misses.",
        })
    
    return {
        'outcome': outcome_name,
        'valid': len(missing) == 0,
        'missing_fields': missing,
        'warnings': warnings,
        'pass': len(missing) == 0 and len(warnings) == 0
    }


def generate_operationalization_template(outcome_type):
    """
    Generate template for common outcome types.
    """
    
    templates = {
        'engagement': """
## Outcome Variable: Engagement

### Concept
What I mean by "engagement": ___

### Operationalization
- **Metric(s) used**: [retweets / likes / replies / combination]
- **Why these metrics**: ___
- **Unit of analysis**: [post / user / time period]
- **Aggregation method**: [sum / mean / median]
- **Normalization**: [none / per-follower / log-transform / percentile]

### Combination Justification (if using multiple metrics)
Why combining these metrics is valid: ___
Weights/formula: ___

### Limitations
This operationalization misses: ___
This could be affected by: ___

### Robustness
Alternative operationalizations to test: ___
""",
        
        'sentiment': """
## Outcome Variable: Sentiment

### Concept
What I mean by "sentiment": [valence / emotion / stance]
Sentiment of whom: [author / audience / about target]
Toward what: [general / specific entity / topic]

### Operationalization
- **Method**: [dictionary / ML / LLM]
- **Tool**: [specific tool/model]
- **Scale**: [binary / ternary / continuous]
- **Aggregation**: [post-level / user-level / time-aggregated]

### Handling of Edge Cases
- Neutral content: ___
- Sarcasm: ___
- Mixed sentiment: ___

### Limitations
This operationalization misses: ___

### Validation
Human validation sample: N = ___
Agreement metric: κ = ___
""",
        
        'influence': """
## Outcome Variable: Influence

### Concept
Influence on what: [attitudes / behaviors / attention / beliefs]
Through what mechanism: [exposure / persuasion / social pressure]

### Operationalization
- **Proxy used**: [centrality / followers / engagement / survey]
- **Why this proxy**: ___

### Critical Acknowledgment
⚠️ Centrality/followers measure POSITION, not IMPACT.
How I address this: ___

### Limitations
This operationalization misses: ___
Cannot rule out: ___
"""
    }
    
    return templates.get(outcome_type, "No template for this outcome type. Document: concept, proxy, justification, limitations.")
```

---

## Integration with Methods Skills

Add to any method that involves outcomes:

```yaml
method_outcome_integration:
  
  before_analysis:
    - check: outcome_operationalized
    - require: operationalization_documentation
    - warn_if: common_issues_detected
  
  in_report:
    - section: "Outcome Operationalization"
    - content: full_operationalization_template
    - required: true
```

---

## Reporting Template

```markdown
## Variable Operationalization

### Independent Variable: [Name]
[How IV is operationalized - already required]

### Dependent Variable: [Name]
- **Concept**: What this represents
- **Proxy**: Data used as measure
- **Measurement**: Units, scale, aggregation
- **Justification**: Why this is a valid proxy
- **Limitations**: What this misses or conflates

### Operationalization Robustness
Alternative operationalizations tested: [yes/no]
Results consistent across operationalizations: [yes/no/partially]
```
