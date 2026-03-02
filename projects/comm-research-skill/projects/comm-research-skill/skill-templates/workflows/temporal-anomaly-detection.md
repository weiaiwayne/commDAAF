# Temporal Anomaly Detection

**Purpose:** Automatically flag unusual patterns in time-series data that require explanation before interpretation.

---

## Philosophy

> "The 2017 spike" is not a finding. It's a question.

Unexplained anomalies in temporal data are methodological red flags, not results. CommDAAF requires explicit investigation of anomalies before proceeding to interpretation.

---

## When to Run

**Mandatory** for any analysis with temporal dimension:
- Engagement over time
- Sentiment trends
- Network growth
- Topic prevalence changes

---

## Anomaly Types

### 1. Sudden Spikes/Drops

```python
def detect_spikes(time_series, threshold_std=2.5):
    """
    Detect values that deviate significantly from local trend.
    
    Args:
        time_series: pandas Series with datetime index
        threshold_std: Number of standard deviations for anomaly
    
    Returns:
        List of anomalous periods requiring explanation
    """
    import pandas as pd
    import numpy as np
    
    # Calculate rolling statistics
    rolling_mean = time_series.rolling(window=7, center=True).mean()
    rolling_std = time_series.rolling(window=7, center=True).std()
    
    # Z-scores
    z_scores = (time_series - rolling_mean) / rolling_std
    
    # Flag anomalies
    anomalies = []
    for idx, z in z_scores.items():
        if abs(z) > threshold_std:
            anomalies.append({
                'date': idx,
                'value': time_series[idx],
                'expected': rolling_mean[idx],
                'z_score': z,
                'direction': 'spike' if z > 0 else 'drop',
                'magnitude': f"{abs(z):.1f} standard deviations",
                'explanation_required': True
            })
    
    return anomalies
```

### 2. Trend Breaks

```python
def detect_trend_breaks(time_series, min_segment=30):
    """
    Detect points where the trend changes significantly.
    
    Uses Bai-Perron structural break detection.
    """
    import numpy as np
    from scipy import stats
    
    # Simple approach: compare regression slopes before/after each point
    breaks = []
    values = time_series.values
    dates = time_series.index
    
    for i in range(min_segment, len(values) - min_segment):
        # Slope before
        x_before = np.arange(i)
        slope_before, _, _, _, _ = stats.linregress(x_before, values[:i])
        
        # Slope after
        x_after = np.arange(len(values) - i)
        slope_after, _, _, _, _ = stats.linregress(x_after, values[i:])
        
        # Significant change in slope?
        slope_change = abs(slope_after - slope_before)
        
        if slope_change > np.std(values) * 0.1:  # Threshold
            breaks.append({
                'date': dates[i],
                'slope_before': slope_before,
                'slope_after': slope_after,
                'change': slope_change,
                'interpretation': 'trend_reversal' if np.sign(slope_before) != np.sign(slope_after) else 'acceleration'
            })
    
    return breaks
```

### 3. Variance Changes

```python
def detect_variance_changes(time_series, window=30):
    """
    Detect periods where variance changes significantly.
    
    Important for: polarization studies, controversy detection
    """
    rolling_var = time_series.rolling(window=window).var()
    
    # Compare to overall variance
    overall_var = time_series.var()
    
    anomalies = []
    for idx, var in rolling_var.items():
        ratio = var / overall_var
        if ratio > 2.0 or ratio < 0.5:
            anomalies.append({
                'date': idx,
                'variance': var,
                'overall_variance': overall_var,
                'ratio': ratio,
                'interpretation': 'high_volatility' if ratio > 2 else 'low_volatility'
            })
    
    return anomalies
```

---

## Mandatory Explanation Framework

When an anomaly is detected, the researcher MUST provide:

```yaml
anomaly_explanation:
  required_fields:
    - anomaly_date: "When did this occur?"
    - observed_value: "What was the value?"
    - expected_value: "What would we expect based on trend?"
    - magnitude: "How large is the deviation?"
    
  explanation_options:
    external_event:
      description: "Something outside the data explains this"
      requires:
        - event_name: "What happened?"
        - event_date: "When?"
        - evidence: "How do you know this caused the anomaly?"
        - implication: "How does this affect interpretation?"
      
    data_artifact:
      description: "Collection or processing issue"
      requires:
        - artifact_type: "What went wrong?"
        - affected_period: "What data is affected?"
        - remediation: "How will you handle it?"
        - implication: "Does this invalidate findings?"
    
    methodological:
      description: "Your method caused this pattern"
      requires:
        - mechanism: "How did your method create this?"
        - robustness: "Does finding hold if you change method?"
        
    substantive:
      description: "This IS the finding"
      requires:
        - interpretation: "What does this mean?"
        - alternative_explanations: "What else could explain it?"
        - evidence_for_interpretation: "Why your explanation over alternatives?"
    
    unknown:
      description: "You don't know"
      requires:
        - investigation_done: "What did you check?"
        - implication: "How does uncertainty affect claims?"
```

---

## Implementation

```python
def temporal_anomaly_report(data, time_column, value_column, context=None):
    """
    Generate full temporal anomaly report.
    
    Args:
        data: DataFrame with time series
        time_column: Column name for timestamps
        value_column: Column name for values
        context: Optional dict of known events {date: event_description}
    
    Returns:
        Report dict with anomalies and required explanations
    """
    import pandas as pd
    
    # Prepare time series
    ts = data.set_index(time_column)[value_column].sort_index()
    
    # Detect anomalies
    spikes = detect_spikes(ts)
    breaks = detect_trend_breaks(ts)
    variance_changes = detect_variance_changes(ts)
    
    all_anomalies = spikes + breaks + variance_changes
    
    if not all_anomalies:
        return {
            'status': 'clean',
            'message': 'No significant temporal anomalies detected',
            'anomalies': []
        }
    
    # Match with known events if provided
    if context:
        for anomaly in all_anomalies:
            anomaly_date = anomaly['date']
            # Check if known event within 3 days
            for event_date, event_desc in context.items():
                if abs((anomaly_date - event_date).days) <= 3:
                    anomaly['potential_explanation'] = event_desc
                    anomaly['explanation_status'] = 'candidate'
    
    # Generate report
    report = {
        'status': 'anomalies_detected',
        'n_anomalies': len(all_anomalies),
        'anomalies': all_anomalies,
        'action_required': True,
        'message': f"""
⚠️ TEMPORAL ANOMALIES DETECTED

{len(all_anomalies)} anomalies require explanation before proceeding.

For each anomaly, you must provide:
1. What happened at this time?
2. Is this an external event, data issue, or substantive finding?
3. How does this affect your interpretation?

Unexplained anomalies are methodological red flags.
Reviewers WILL ask about them.
"""
    }
    
    return report


def format_anomaly_table(anomalies):
    """Format anomalies as markdown table."""
    lines = ["| Date | Type | Magnitude | Explained? |",
             "|------|------|-----------|------------|"]
    
    for a in anomalies:
        explained = "✓" if a.get('explanation') else "❌ REQUIRED"
        lines.append(f"| {a['date']} | {a.get('direction', a.get('interpretation', 'unknown'))} | {a.get('magnitude', 'N/A')} | {explained} |")
    
    return "\n".join(lines)
```

---

## Integration with Critical Checks

```yaml
temporal_check:
  trigger: any_time_series_analysis
  
  steps:
    1. run_anomaly_detection
    2. present_anomalies_to_user
    3. require_explanations
    4. validate_explanations
    5. document_in_methods
  
  blocking: true  # Cannot proceed without explanations
  
  exceptions:
    - exploratory_tier: "Flag but don't block"
    - known_context: "Auto-fill if event matches"
```

---

## Reporting Template

```markdown
## Temporal Patterns

### Anomalies Detected

| Date | Observation | Expected | Deviation | Explanation |
|------|-------------|----------|-----------|-------------|
| 2017-03 | 118.8 avg RT | 32.9 avg RT | +261% | [REQUIRED] |

### Explanations

**March 2017 Engagement Spike:**
- **Type:** External event
- **Event:** [Season 4 premiere / Viral episode / Celebrity engagement]
- **Evidence:** [How do you know?]
- **Implication:** Engagement metric reflects show popularity, not sentiment strategy

### Unexplained Anomalies

[List any anomalies that remain unexplained and discuss implications for interpretation]
```

---

## Common Explanations Lookup

To help researchers, provide common explanations for social media data:

```yaml
common_explanations:
  twitter:
    2016-02: "Twitter algorithmic timeline introduced"
    2017-11: "Character limit expanded to 280"
    2020-06: "Fleets launched (temporary)"
    2023-07: "Rebrand to X, rate limits introduced"
    
  platform_general:
    - "Viral moment (check for quote tweets, news coverage)"
    - "Bot activity (check account age distribution)"
    - "Hashtag hijacking (check co-occurring hashtags)"
    - "External news event (check Google Trends)"
    - "API collection gap (check data completeness)"
    
  methodology:
    - "Keyword drift (meaning of search term changed)"
    - "Sample boundary effects (start/end of collection)"
    - "Rate limit artifacts (certain hours undersampled)"
```
