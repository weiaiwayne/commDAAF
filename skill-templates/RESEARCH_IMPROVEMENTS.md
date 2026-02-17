# Research-Based Improvements to Skill Pack

Based on literature review of false positives and contextual understanding issues in computational social media research.

---

## Problem 1: False Positives in Social Media Research

### Key Finding: Rauchfleisch & Kaiser (2020) - "The False Positive Problem"

**Study:** Tested Botometer (most popular bot detection tool) on 4,134 verified accounts over 3 months.

**Findings:**
- Botometer scores are **highly unstable** over time
- Same account can be classified as bot one week, human the next
- **Language matters:** Accuracy drops significantly for non-English content
- **Threshold problem:** Researchers pick arbitrary thresholds (0.43 vs 0.76) → dramatically different results
- Many studies unknowingly count humans as bots and vice versa

**Implications for our skill pack:**
1. Any classification should report **confidence intervals**, not point estimates
2. Need **temporal stability checks** — run analysis at multiple time points
3. **Language-specific validation** required for non-English data
4. **No arbitrary thresholds** — require theoretical/empirical justification

---

## Problem 2: Lack of Contextual Understanding

### The Core Issue

Pre-AI computational methods (dictionaries, pattern matching, keyword counting) fail because they:
1. **Ignore context** — "not happy" → "happy" counted positive
2. **Miss sarcasm/irony** — "Great job, genius" → counted positive
3. **Can't handle domain shift** — "sick" negative in medicine, positive in slang
4. **Lose pragmatics** — "I could care less" vs "I couldn't care less"
5. **Flatten ambiguity** — Force binary classification on inherently ambiguous content

### Research on Sarcasm Detection

From Nature Scientific Reports (2024-2025):
- "Traditional sentiment analysis models are insufficient due to the complexity of sarcasm"
- "Sarcasm detection requires understanding of context, topic, and environment"
- Transformer models (BERT, RoBERTa) help but still struggle with cultural context

### LLMs as Partial Solution

Egami et al. (2024) "Using LLMs for Social Science":
- LLMs can understand context better than dictionaries
- BUT: LLM annotations are **not ground truth**
- Need **Design-based Supervised Learning (DSL)** framework
- Human validation sample + statistical correction for LLM bias

---

## Proposed Improvements

### Improvement 1: Multi-Layer Validation System

```
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: Automated Classification                               │
│   - Run method (sentiment, coordination, topic)                 │
│   - Output: Classification + confidence score                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 2: Uncertainty Detection                                  │
│   - Flag low-confidence classifications                         │
│   - Flag items with potential sarcasm/irony signals             │
│   - Flag items with domain-specific language                    │
│   - Flag items in non-primary language                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 3: Human Review Queue                                     │
│   - Uncertain items sent to human for review                    │
│   - Human labels used to correct/calibrate model                │
│   - Disagreements documented, not hidden                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 4: Statistical Correction                                 │
│   - Apply DSL correction for LLM annotation bias                │
│   - Report corrected estimates with confidence intervals        │
│   - Document sensitivity to threshold choices                   │
└─────────────────────────────────────────────────────────────────┘
```

### Improvement 2: Context Injection for LLM Analysis

**Before:**
```
Prompt: "Is this post positive or negative?"
Post: "Great, another update that breaks everything"
→ LLM might say "positive" (sees "Great")
```

**After:**
```
Prompt: "Analyze this post's sentiment. Consider:
- Is there sarcasm or irony?
- What is the actual intent?
- What context would help interpret this?

Post: 'Great, another update that breaks everything'

First, explain the likely meaning.
Then, classify as: positive / negative / sarcastic-negative / ambiguous"

→ LLM recognizes sarcasm, classifies as sarcastic-negative
```

### Improvement 3: Uncertainty Quantification

**Always report:**
1. Classification
2. Confidence score
3. Alternative interpretation
4. Factors that could change the interpretation

```python
def classify_with_uncertainty(text, model):
    """
    Returns classification with uncertainty measures.
    """
    # Get multiple samples (temperature > 0)
    samples = [model.classify(text) for _ in range(5)]
    
    # Calculate agreement
    classifications = [s['label'] for s in samples]
    agreement = max(Counter(classifications).values()) / len(samples)
    
    # Check for sarcasm signals
    sarcasm_signals = detect_sarcasm_signals(text)
    
    # Check for domain-specific terms
    domain_flags = detect_domain_terms(text)
    
    return {
        'classification': mode(classifications),
        'confidence': agreement,
        'is_unanimous': agreement == 1.0,
        'sarcasm_risk': len(sarcasm_signals) > 0,
        'sarcasm_signals': sarcasm_signals,
        'domain_flags': domain_flags,
        'needs_human_review': agreement < 0.8 or sarcasm_signals,
        'alternative_interpretations': list(set(classifications))
    }
```

### Improvement 4: Sarcasm/Irony Detection Layer

Add explicit sarcasm detection before sentiment/stance analysis:

```python
SARCASM_SIGNALS = {
    'punctuation': r'[!?]{2,}|\.{3,}',
    'caps_emphasis': r'\b[A-Z]{2,}\b',
    'quotation_marks': r'[""\'"](?:sure|right|great|wonderful|fantastic)[""\'"]',
    'emoji_mismatch': r'(terrible|awful|worst).*[😀🙂👍]|(great|amazing|love).*[😒🙄😤]',
    'intensifiers': r'\b(so+|very+|really+|totally)\b',
    'rhetorical': r'\b(oh|wow|gee|sure|right)\b.*[!?]',
    'contrast_markers': r'\b(but|yet|however|although)\b',
}

def detect_sarcasm_signals(text):
    """Detect potential sarcasm signals in text."""
    signals = []
    for signal_type, pattern in SARCASM_SIGNALS.items():
        if re.search(pattern, text, re.IGNORECASE):
            signals.append(signal_type)
    return signals
```

### Improvement 5: Temporal Stability Checks

```python
def check_temporal_stability(classification_func, data, time_column, n_windows=3):
    """
    Check if classifications are stable across time windows.
    
    Unstable classifications suggest method sensitivity issues.
    """
    # Split data into time windows
    windows = split_by_time(data, time_column, n_windows)
    
    # Run classification on each window
    results = []
    for window in windows:
        classifications = classification_func(window)
        results.append(classifications)
    
    # Calculate stability metrics
    stability = {}
    for item_id in data['id'].unique():
        item_classifications = [r[item_id] for r in results if item_id in r]
        stability[item_id] = {
            'classifications': item_classifications,
            'stable': len(set(item_classifications)) == 1,
            'majority': mode(item_classifications),
        }
    
    unstable_pct = sum(1 for v in stability.values() if not v['stable']) / len(stability)
    
    return {
        'stability_by_item': stability,
        'pct_unstable': unstable_pct,
        'warning': unstable_pct > 0.1  # More than 10% unstable is concerning
    }
```

### Improvement 6: False Positive Estimation

```python
def estimate_false_positive_rate(human_sample, automated_results):
    """
    Estimate false positive rate using human-coded sample.
    
    Args:
        human_sample: Dict of {item_id: human_label}
        automated_results: Dict of {item_id: automated_label}
    
    Returns:
        False positive rate, false negative rate, confidence intervals
    """
    matched_ids = set(human_sample.keys()) & set(automated_results.keys())
    
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    
    for item_id in matched_ids:
        human = human_sample[item_id]
        auto = automated_results[item_id]
        
        if human == 1 and auto == 1:
            true_positives += 1
        elif human == 0 and auto == 1:
            false_positives += 1
        elif human == 0 and auto == 0:
            true_negatives += 1
        elif human == 1 and auto == 0:
            false_negatives += 1
    
    fpr = false_positives / (false_positives + true_negatives) if (false_positives + true_negatives) > 0 else 0
    fnr = false_negatives / (false_negatives + true_positives) if (false_negatives + true_positives) > 0 else 0
    
    # Bootstrap confidence intervals
    ci_fpr = bootstrap_ci(human_sample, automated_results, 'fpr')
    ci_fnr = bootstrap_ci(human_sample, automated_results, 'fnr')
    
    return {
        'false_positive_rate': fpr,
        'false_negative_rate': fnr,
        'fpr_95_ci': ci_fpr,
        'fnr_95_ci': ci_fnr,
        'sample_size': len(matched_ids),
        'adequate_sample': len(matched_ids) >= 200  # Minimum for reliable estimates
    }
```

### Improvement 7: Multi-Model Disagreement as Signal

Use model disagreement to identify ambiguous cases:

```python
def multi_model_classification(text, models=['gpt-4o', 'claude-sonnet', 'gemini-flash']):
    """
    Classify using multiple models; use disagreement as uncertainty signal.
    """
    results = {}
    for model in models:
        results[model] = classify_with_model(text, model)
    
    # Check agreement
    labels = [r['label'] for r in results.values()]
    agreement = len(set(labels)) == 1
    
    if not agreement:
        # Disagreement is informative!
        return {
            'classification': 'AMBIGUOUS',
            'model_labels': results,
            'needs_human_review': True,
            'note': 'Models disagree — likely ambiguous or context-dependent'
        }
    else:
        return {
            'classification': labels[0],
            'model_labels': results,
            'unanimous': True,
            'confidence': 'high'
        }
```

---

## Implementation Priority

### HIGH PRIORITY (Implement Now)

1. **Uncertainty quantification** for all classifications
2. **Sarcasm signal detection** before sentiment analysis
3. **Multi-model validation** option
4. **Human review queue** for low-confidence items
5. **False positive estimation** with human sample

### MEDIUM PRIORITY (Implement Soon)

6. **Temporal stability checks**
7. **DSL statistical correction** for LLM bias
8. **Language-specific warnings**
9. **Domain shift detection**

### LOWER PRIORITY (Future Enhancement)

10. **Active learning** to improve model with human feedback
11. **Platform-specific models** (Twitter vs Telegram vs Reddit)
12. **Cultural context adaptation**

---

## New Preflight Checks Based on Research

Add these to `critical-checks.md`:

### Data Quality Checks

```yaml
data_quality_checks:
  
  sample_representativeness:
    message: |
      ⚠️ **SAMPLE REPRESENTATIVENESS CHECK**
      
      Your data may not represent the population:
      
      1. **API sampling bias**
         - Did you get all data or a sample?
         - How was it sampled? (time? keyword? random?)
      
      2. **Platform visibility bias**
         - You only see public posts
         - Who posts publicly? Who doesn't?
      
      3. **Temporal bias**
         - Is this time period typical?
         - Events during collection period?
      
      4. **Deletion bias**
         - Deleted posts are invisible
         - Controversial content more likely deleted
      
      What are the known biases in your sample?
      → Biases: ___

  language_context:
    check: detected_language != 'english' OR multilingual
    message: |
      ⚠️ **NON-ENGLISH/MULTILINGUAL DATA DETECTED**
      
      Most NLP tools are trained primarily on English.
      
      Issues:
      - Sentiment dictionaries may not translate
      - Sarcasm cues differ by language/culture
      - Named entity recognition less accurate
      - Slang/colloquialisms missed
      
      Languages detected: {languages}
      
      Options:
      - Use language-specific models
      - Separate analysis by language
      - Acknowledge limitation
      
      Your approach: ___
```

### Analysis Quality Checks

```yaml
analysis_quality_checks:

  uncertainty_acknowledgment:
    trigger: any classification task
    message: |
      📋 **UNCERTAINTY HANDLING**
      
      How will you handle uncertain classifications?
      
      Options:
      1. **Flag for human review** (recommended)
         - Route low-confidence items to human
         - Use to estimate error rates
      
      2. **Exclude from analysis**
         - Removes uncertain cases
         - May bias results
      
      3. **Include with caveat**
         - Report uncertainty distribution
         - Sensitivity analysis
      
      Your approach: ___
      Confidence threshold for "uncertain": ___

  sarcasm_handling:
    trigger: sentiment OR stance analysis
    message: |
      ⚠️ **SARCASM/IRONY STRATEGY**
      
      Sarcasm flips sentiment polarity.
      "Great job breaking everything" = NEGATIVE, not positive.
      
      Your domain ({domain}) likely contains sarcasm if:
      - Political content ✓
      - Complaints/criticism ✓
      - Informal/social media ✓
      - Youth audiences ✓
      
      Sarcasm handling options:
      
      1. **Detect and flag**
         - Run sarcasm detection first
         - Review flagged items manually
      
      2. **Include sarcasm category**
         - "positive / negative / sarcastic"
         - Requires category definition
      
      3. **Use LLM with context**
         - Prompt for sarcasm awareness
         - More expensive, more accurate
      
      4. **Acknowledge limitation**
         - Document that sarcasm may be misclassified
         - Estimate prevalence in sample
      
      Your choice: ___

  false_positive_mitigation:
    trigger: any classification task
    message: |
      📋 **FALSE POSITIVE MITIGATION PLAN**
      
      All classifiers produce false positives.
      
      Required:
      1. **Human validation sample**
         - Minimum 200 items coded by human
         - Calculate precision, recall, F1
         - Report in methods section
      
      2. **Threshold justification**
         - Why this threshold?
         - What's the FPR at this threshold?
      
      3. **Sensitivity analysis**
         - How do results change at threshold ± 0.1?
         - If results are threshold-sensitive, report it
      
      Your sample size: ___
      How will you select validation sample: ___
```

---

## Key Citations

1. Rauchfleisch, A., & Kaiser, J. (2020). The False positive problem of automatic bot detection in social science research. PLOS ONE.

2. Egami, N., Hinck, M., Stewart, B., & Wei, H. (2024). Using Large Language Model Annotations for the Social Sciences: A General Framework of Using Predicted Variables in Statistical Analyses.

3. Abdurahman, S., et al. (2025). A Primer for Evaluating Large Language Models in Social-Science Research. Advances in Methods and Practices in Psychological Science.

4. Various (2024-2025). Sarcasm detection research in Nature Scientific Reports.

---

## Summary

**The core insight:** Computational methods are tools, not oracles. The messiness of social media data requires:

1. **Always quantify uncertainty** — confidence scores, not just labels
2. **Always validate with humans** — estimate FPR/FNR empirically
3. **Always check for context issues** — sarcasm, irony, domain shift
4. **Never trust arbitrary thresholds** — justify or test sensitivity
5. **Embrace ambiguity** — "uncertain" is a valid classification
