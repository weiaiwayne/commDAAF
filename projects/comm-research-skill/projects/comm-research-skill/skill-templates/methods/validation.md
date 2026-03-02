# Validation Methods Skill

Core validation methods to reduce false positives and handle uncertainty in computational social media research.

---

## Philosophy

> "All models are wrong, but some are useful." — George Box
> 
> The goal is not perfect classification. The goal is **knowing how wrong we are** and **being honest about it**.

---

## 1. Uncertainty Quantification

### For Every Classification, Report:

```python
def classify_with_uncertainty(text, classifier, n_samples=5):
    """
    Classify text with uncertainty quantification.
    
    Returns label + confidence + uncertainty signals.
    """
    # Multi-sample for variance estimate
    samples = [classifier(text) for _ in range(n_samples)]
    labels = [s['label'] for s in samples]
    scores = [s['score'] for s in samples]
    
    # Agreement as confidence proxy
    from collections import Counter
    label_counts = Counter(labels)
    majority_label = label_counts.most_common(1)[0][0]
    agreement = label_counts[majority_label] / n_samples
    
    # Score variance
    import numpy as np
    score_std = np.std(scores)
    
    # Detect potential issues
    issues = []
    
    # Check for sarcasm signals
    sarcasm_signals = detect_sarcasm_signals(text)
    if sarcasm_signals:
        issues.append(f"sarcasm_signals: {sarcasm_signals}")
    
    # Check for negation
    if contains_negation(text):
        issues.append("contains_negation")
    
    # Check for questions (often misclassified)
    if text.strip().endswith('?'):
        issues.append("is_question")
    
    # Check for quotes (reported speech)
    if '"' in text or "'" in text:
        issues.append("contains_quotes")
    
    return {
        'label': majority_label,
        'confidence': agreement,
        'score_mean': np.mean(scores),
        'score_std': score_std,
        'is_unanimous': agreement == 1.0,
        'needs_review': agreement < 0.8 or len(issues) > 0,
        'issues': issues,
        'all_labels': labels,
        'all_scores': scores
    }


def detect_sarcasm_signals(text):
    """Detect linguistic signals of potential sarcasm."""
    import re
    
    signals = []
    
    patterns = {
        'excessive_punctuation': r'[!?]{2,}|\.{3,}',
        'all_caps_words': r'\b[A-Z]{3,}\b',
        'air_quotes': r'["""][\w\s]+["""]',
        'yeah_right': r'\b(yeah|sure|right|oh)\s+(right|sure|okay)\b',
        'emoji_mismatch': r'(terrible|awful|worst|hate).*[😀🙂👍🎉]|(great|love|amazing).*[😒🙄😤💀]',
        'hashtag_sarcasm': r'#(sarcasm|not|yeah_right|sure)',
        'eye_roll': r'🙄',
    }
    
    text_lower = text.lower()
    
    for signal_name, pattern in patterns.items():
        if re.search(pattern, text if signal_name == 'all_caps_words' else text_lower):
            signals.append(signal_name)
    
    return signals


def contains_negation(text):
    """Check if text contains negation that might flip sentiment."""
    import re
    
    negation_patterns = [
        r"\b(not|no|never|neither|nobody|nothing|nowhere|none)\b",
        r"\b(isn't|aren't|wasn't|weren't|won't|wouldn't|couldn't|shouldn't|don't|doesn't|didn't|haven't|hasn't|hadn't)\b",
        r"\b(barely|hardly|scarcely|seldom|rarely)\b",
    ]
    
    text_lower = text.lower()
    return any(re.search(p, text_lower) for p in negation_patterns)
```

---

## 2. Human Validation Sample

### Required for Any Classification Task

```python
def create_validation_sample(data, sample_size=200, stratify_by=None):
    """
    Create human validation sample with proper stratification.
    
    Args:
        data: Full dataset
        sample_size: Minimum 200 for reliable estimates
        stratify_by: Column(s) to stratify sample
    
    Returns:
        Sample dataframe with IDs for human coding
    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    
    if len(data) < sample_size:
        print(f"Warning: Dataset ({len(data)}) smaller than requested sample ({sample_size})")
        return data
    
    if stratify_by:
        # Stratified sample
        sample, _ = train_test_split(
            data,
            train_size=sample_size,
            stratify=data[stratify_by],
            random_state=42
        )
    else:
        # Random sample
        sample = data.sample(n=sample_size, random_state=42)
    
    # Add columns for human coding
    sample['human_label'] = None
    sample['human_coder'] = None
    sample['human_notes'] = None
    sample['coding_date'] = None
    
    return sample


def calculate_validation_metrics(human_labels, automated_labels, positive_class=1):
    """
    Calculate classification metrics from human validation.
    
    Returns precision, recall, F1, and error rates with confidence intervals.
    """
    from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
    import numpy as np
    
    # Basic metrics
    precision, recall, f1, _ = precision_recall_fscore_support(
        human_labels, 
        automated_labels,
        pos_label=positive_class,
        average='binary'
    )
    
    # Confusion matrix
    tn, fp, fn, tp = confusion_matrix(human_labels, automated_labels).ravel()
    
    # Error rates
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  # False Positive Rate
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0  # False Negative Rate
    
    # Bootstrap confidence intervals
    ci_precision = bootstrap_ci(human_labels, automated_labels, 'precision')
    ci_recall = bootstrap_ci(human_labels, automated_labels, 'recall')
    ci_fpr = bootstrap_ci(human_labels, automated_labels, 'fpr')
    
    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'false_positive_rate': fpr,
        'false_negative_rate': fnr,
        'true_positives': tp,
        'true_negatives': tn,
        'false_positives': fp,
        'false_negatives': fn,
        'sample_size': len(human_labels),
        'ci_precision_95': ci_precision,
        'ci_recall_95': ci_recall,
        'ci_fpr_95': ci_fpr,
    }


def bootstrap_ci(human, auto, metric, n_bootstrap=1000, ci=0.95):
    """Calculate bootstrap confidence interval for a metric."""
    import numpy as np
    from sklearn.metrics import precision_score, recall_score
    
    values = []
    n = len(human)
    
    for _ in range(n_bootstrap):
        # Resample with replacement
        indices = np.random.choice(n, size=n, replace=True)
        h_sample = [human[i] for i in indices]
        a_sample = [auto[i] for i in indices]
        
        # Calculate metric
        if metric == 'precision':
            try:
                values.append(precision_score(h_sample, a_sample, zero_division=0))
            except:
                continue
        elif metric == 'recall':
            try:
                values.append(recall_score(h_sample, a_sample, zero_division=0))
            except:
                continue
        elif metric == 'fpr':
            tn = sum(1 for h, a in zip(h_sample, a_sample) if h == 0 and a == 0)
            fp = sum(1 for h, a in zip(h_sample, a_sample) if h == 0 and a == 1)
            values.append(fp / (fp + tn) if (fp + tn) > 0 else 0)
    
    lower = np.percentile(values, (1 - ci) / 2 * 100)
    upper = np.percentile(values, (1 + ci) / 2 * 100)
    
    return (lower, upper)
```

---

## 3. Multi-Model Validation

### Use Model Disagreement as Uncertainty Signal

```python
async def multi_model_classify(text, task_prompt, models=None):
    """
    Classify using multiple models; disagreement = uncertainty.
    
    Args:
        text: Text to classify
        task_prompt: Classification task description
        models: List of models to use (default: diverse set)
    """
    if models is None:
        models = [
            'google/gemini-2.0-flash',    # Fast, Google
            'anthropic/claude-sonnet-4',   # Anthropic
            'openai/gpt-4o-mini',          # OpenAI
        ]
    
    results = {}
    
    for model in models:
        response = await call_model(model, task_prompt + f"\n\nText: {text}")
        results[model] = parse_classification(response)
    
    # Analyze agreement
    labels = [r['label'] for r in results.values()]
    unique_labels = set(labels)
    
    if len(unique_labels) == 1:
        # Full agreement
        return {
            'label': labels[0],
            'confidence': 'high',
            'unanimous': True,
            'model_results': results
        }
    else:
        # Disagreement - important signal!
        from collections import Counter
        label_counts = Counter(labels)
        majority = label_counts.most_common(1)[0]
        
        return {
            'label': 'AMBIGUOUS',
            'majority_label': majority[0],
            'majority_count': majority[1],
            'total_models': len(models),
            'unanimous': False,
            'needs_human_review': True,
            'model_results': results,
            'disagreement_note': f"Models disagree: {dict(label_counts)}"
        }
```

---

## 4. Sensitivity Analysis

### Test How Results Change with Different Parameters

```python
def sensitivity_analysis(data, classification_func, param_name, param_values):
    """
    Test how results change across parameter values.
    
    Stable results = robust finding.
    Unstable results = parameter-dependent, report with caution.
    """
    results = {}
    
    for value in param_values:
        # Run classification with this parameter value
        classifications = classification_func(data, **{param_name: value})
        
        # Summarize results
        from collections import Counter
        label_dist = Counter(classifications)
        
        results[value] = {
            'label_distribution': dict(label_dist),
            'pct_positive': label_dist.get(1, 0) / len(classifications) * 100
        }
    
    # Analyze stability
    pct_positives = [r['pct_positive'] for r in results.values()]
    import numpy as np
    
    stability = {
        'min_pct': min(pct_positives),
        'max_pct': max(pct_positives),
        'range': max(pct_positives) - min(pct_positives),
        'std': np.std(pct_positives),
        'is_stable': (max(pct_positives) - min(pct_positives)) < 10  # <10pp difference
    }
    
    return {
        'results_by_param': results,
        'stability': stability,
        'warning': None if stability['is_stable'] else 
            f"Results vary by {stability['range']:.1f} percentage points across {param_name} values"
    }


# Example: Sensitivity to threshold
def threshold_sensitivity(scores, thresholds=[0.3, 0.4, 0.5, 0.6, 0.7]):
    """
    Show how classification changes across threshold values.
    """
    results = {}
    
    for threshold in thresholds:
        classifications = [1 if s >= threshold else 0 for s in scores]
        n_positive = sum(classifications)
        pct_positive = n_positive / len(scores) * 100
        
        results[threshold] = {
            'n_positive': n_positive,
            'pct_positive': pct_positive
        }
    
    # Report
    print("Threshold Sensitivity Analysis")
    print("=" * 40)
    for t, r in results.items():
        print(f"Threshold {t}: {r['n_positive']:,} ({r['pct_positive']:.1f}%) classified positive")
    
    return results
```

---

## 5. Temporal Stability Check

### Same Data, Different Time Points

```python
def temporal_stability_check(classifier_func, account_ids, check_dates, threshold=0.1):
    """
    Check if classifications are stable over time.
    
    Based on Rauchfleisch & Kaiser (2020): Botometer scores 
    fluctuate significantly, causing false positives/negatives.
    """
    results = {}
    
    for account_id in account_ids:
        classifications = []
        
        for date in check_dates:
            # Get classification at this date
            result = classifier_func(account_id, as_of=date)
            classifications.append({
                'date': date,
                'label': result['label'],
                'score': result['score']
            })
        
        # Check stability
        labels = [c['label'] for c in classifications]
        scores = [c['score'] for c in classifications]
        
        import numpy as np
        
        results[account_id] = {
            'classifications': classifications,
            'labels_stable': len(set(labels)) == 1,
            'score_std': np.std(scores),
            'score_range': max(scores) - min(scores),
            'majority_label': max(set(labels), key=labels.count)
        }
    
    # Summary
    n_unstable = sum(1 for r in results.values() if not r['labels_stable'])
    pct_unstable = n_unstable / len(results) * 100
    
    return {
        'by_account': results,
        'n_unstable': n_unstable,
        'pct_unstable': pct_unstable,
        'warning': pct_unstable > threshold * 100,
        'warning_message': f"{pct_unstable:.1f}% of accounts have unstable classifications across time"
            if pct_unstable > threshold * 100 else None
    }
```

---

## 6. Context-Aware Classification

### Add Context to LLM Prompts

```python
def context_aware_classify(text, category_definitions, include_context=True):
    """
    Classify with explicit context reasoning.
    
    Forces model to consider sarcasm, irony, and domain context.
    """
    if include_context:
        prompt = f"""
Classify the following text. Before classifying, analyze:

1. **Literal vs intended meaning**: Is the text sarcastic or ironic?
2. **Context clues**: Emojis, punctuation, quoted text
3. **Domain context**: Platform-specific language, slang

Categories:
{category_definitions}

Text to classify:
"{text}"

Respond in this format:
ANALYSIS:
- Literal meaning: [what the words literally say]
- Likely intent: [what the author probably means]
- Sarcasm signals: [any indicators of sarcasm/irony, or "none"]
- Confidence: [high/medium/low]

CLASSIFICATION: [category]
REASONING: [one sentence explaining why]
"""
    else:
        prompt = f"""
Classify the following text.

Categories:
{category_definitions}

Text: "{text}"

CLASSIFICATION:
"""
    
    response = call_llm(prompt)
    return parse_context_aware_response(response)
```

---

## 7. Reporting Template

### Every Analysis Should Report:

```markdown
## Classification Validation Report

### Sample Characteristics
- Total items: {n_total}
- Human-validated sample: {n_validated}
- Sampling method: {method}

### Performance Metrics
| Metric | Value | 95% CI |
|--------|-------|--------|
| Precision | {precision} | [{ci_low}, {ci_high}] |
| Recall | {recall} | [{ci_low}, {ci_high}] |
| F1 Score | {f1} | - |
| False Positive Rate | {fpr} | [{ci_low}, {ci_high}] |
| False Negative Rate | {fnr} | [{ci_low}, {ci_high}] |

### Uncertainty Distribution
- High confidence (>0.8): {pct_high}%
- Medium confidence (0.5-0.8): {pct_med}%
- Low confidence (<0.5): {pct_low}%
- Flagged for review: {pct_flagged}%

### Sensitivity Analysis
- Parameter varied: {param}
- Range tested: {range}
- Result stability: {stable/unstable}
- Note: {sensitivity_note}

### Known Limitations
1. {limitation_1}
2. {limitation_2}
3. {limitation_3}

### Sarcasm/Context Issues
- Items with sarcasm signals: {n_sarcasm}
- Items with negation: {n_negation}
- Items manually reviewed for context: {n_reviewed}
```

---

## Integration

Add to any classification method:

```python
# Before classification
validation_sample = create_validation_sample(data, sample_size=200)
print(f"Send {len(validation_sample)} items for human coding before proceeding")

# During classification
results = [classify_with_uncertainty(text, classifier) for text in data['text']]

# Flag uncertain items
uncertain = [r for r in results if r['needs_review']]
print(f"{len(uncertain)} items flagged for human review ({len(uncertain)/len(results)*100:.1f}%)")

# After human coding
metrics = calculate_validation_metrics(human_labels, auto_labels)
print(f"False Positive Rate: {metrics['false_positive_rate']:.2%}")

# Sensitivity check
sensitivity = threshold_sensitivity(scores)

# Generate report
generate_validation_report(results, metrics, sensitivity)
```
