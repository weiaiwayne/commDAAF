# Coordination Detection Skill Pack

**Version:** 0.1.0  
**Status:** Pending Validation  
**Maintainer:** UMass Computational Communication Lab

---

## Overview

Detection of coordinated inauthentic behavior (CIB) and coordinated campaigns in social media data.

**⚠️ HIGH-STAKES SKILL: False positives can harm legitimate activists.**

---

## Capabilities

- Identify temporal coordination patterns
- Detect content similarity clusters
- Distinguish organic from coordinated behavior
- Baseline comparison methodology

---

## Probing Questions (ALL REQUIRED — HIGH BAR)

```
Q1: What behavior suggests 'coordination'?
    ✓ Simultaneous posting (within N seconds)
    ✓ Identical/near-identical content
    ✓ Network structure anomalies
    ✗ "Suspicious activity" — OPERATIONAL DEFINITION REQUIRED

Q2: How will you distinguish organic from coordinated?
    ✓ Baseline comparison (organic movement benchmark)
    ✓ Statistical threshold (p < 0.01 vs null model)
    ✓ Manual validation sample
    ✗ "It looks coordinated" — UNACCEPTABLE

Q3: What conclusions will you draw?
    ✓ "Statistically unusual temporal patterns"
    ✓ "Content similarity above baseline"
    ✗ "Bots" — NEVER CONCLUDE FROM BEHAVIOR ALONE
    ✗ "State actors" — ATTRIBUTION REQUIRES ADDITIONAL EVIDENCE

Q4: What's your false positive tolerance?
    ✓ Explicit threshold (e.g., FPR < 0.05)
    ✓ Human review for all flagged cases
    ✗ "We'll review significant cases" — DEFINE SIGNIFICANT

Q5: How will you validate?
    ✓ Known coordinated campaign (ground truth)
    ✓ Known organic movement (baseline)
    ✓ Human review of flagged accounts
    ✗ "The patterns speak for themselves" — CIRCULAR REASONING
```

---

## What You CAN Conclude

| Evidence | Valid Conclusion |
|----------|------------------|
| Unusual temporal clustering | "Posting times deviate from baseline" |
| High content similarity | "Content repetition above organic baseline" |
| Network structure anomalies | "Account relationships differ from organic pattern" |
| Combined indicators | "Pattern consistent with coordination" |

## What You CANNOT Conclude

| Invalid Conclusion | Why |
|--------------------|-----|
| "Bots" | Timing alone cannot distinguish human from automated |
| "State actors" | Attribution requires additional evidence |
| "Inauthentic" | Coordinated ≠ inauthentic (activists coordinate too) |
| "Malicious" | Intent cannot be inferred from behavior |

---

## Methodology

### 1. Establish Baseline

Before claiming coordination, establish what "normal" looks like:

```python
# Calculate baseline posting distribution
baseline_data = load_organic_movement()  # Known organic
baseline_inter_post_times = calculate_inter_post_times(baseline_data)
baseline_content_similarity = calculate_similarity_distribution(baseline_data)

# Your target data
target_inter_post_times = calculate_inter_post_times(target_data)
target_content_similarity = calculate_similarity_distribution(target_data)

# Statistical comparison
timing_ks_stat, timing_p = ks_2samp(baseline_inter_post_times, target_inter_post_times)
similarity_ks_stat, similarity_p = ks_2samp(baseline_content_similarity, target_content_similarity)
```

### 2. Temporal Analysis

```python
def detect_temporal_bursts(posts, window_seconds=60, threshold_multiplier=3):
    """Flag unusually synchronized posting."""
    timestamps = sorted([p['timestamp'] for p in posts])
    
    # Calculate expected rate
    total_time = timestamps[-1] - timestamps[0]
    expected_rate = len(timestamps) / total_time
    
    # Sliding window burst detection
    bursts = []
    for i, t in enumerate(timestamps):
        window_end = t + window_seconds
        posts_in_window = sum(1 for ts in timestamps if t <= ts < window_end)
        expected_in_window = expected_rate * window_seconds
        
        if posts_in_window > threshold_multiplier * expected_in_window:
            bursts.append({
                'start': t,
                'count': posts_in_window,
                'expected': expected_in_window,
                'ratio': posts_in_window / expected_in_window
            })
    
    return bursts
```

### 3. Content Similarity Analysis

```python
def detect_content_clusters(posts, similarity_threshold=0.8):
    """Identify near-duplicate content clusters."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([p['text'] for p in posts])
    
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    # Find clusters above threshold
    clusters = []
    seen = set()
    for i in range(len(posts)):
        if i in seen:
            continue
        cluster = [i]
        for j in range(i+1, len(posts)):
            if similarity_matrix[i,j] > similarity_threshold:
                cluster.append(j)
                seen.add(j)
        if len(cluster) > 1:
            clusters.append(cluster)
    
    return clusters
```

### 4. Combined Scoring

```python
def coordination_score(posts, baseline):
    """Calculate overall coordination likelihood."""
    
    # Temporal component
    timing_deviation = calculate_timing_deviation(posts, baseline)
    
    # Content component
    similarity_deviation = calculate_similarity_deviation(posts, baseline)
    
    # Network component (if available)
    network_anomaly = calculate_network_anomaly(posts, baseline)
    
    # Combined score (weighted)
    score = (
        0.4 * timing_deviation +
        0.4 * similarity_deviation +
        0.2 * network_anomaly
    )
    
    return {
        'score': score,
        'timing': timing_deviation,
        'content': similarity_deviation,
        'network': network_anomaly,
        'interpretation': interpret_score(score)
    }

def interpret_score(score):
    if score > 0.8:
        return "Strong indicators of coordination (requires validation)"
    elif score > 0.6:
        return "Moderate indicators (investigate further)"
    elif score > 0.4:
        return "Weak indicators (likely organic with some patterns)"
    else:
        return "Consistent with organic activity"
```

---

## Dual-Sided Coordination

**Important:** Coordination can occur on BOTH sides of a contentious issue.

```
IF analyzing controversial topic:
  1. Analyze pro-X content separately
  2. Analyze anti-X content separately
  3. Compare both to organic baselines
  4. Report findings for BOTH sides

DO NOT assume one side is organic and the other coordinated.
```

---

## Output Schema

```json
{
  "study_id": "string",
  "target_data": {
    "n_posts": "number",
    "n_accounts": "number",
    "time_range": "string"
  },
  "baseline": {
    "source": "string (what organic baseline used)",
    "n_posts": "number"
  },
  "findings": {
    "temporal": {
      "deviation_from_baseline": "number",
      "p_value": "number",
      "interpretation": "string"
    },
    "content": {
      "similarity_deviation": "number",
      "p_value": "number",
      "interpretation": "string"
    },
    "overall": {
      "coordination_score": "number (0-1)",
      "interpretation": "string"
    }
  },
  "flagged_clusters": [
    {
      "cluster_id": "string",
      "n_accounts": "number",
      "indicators": ["timing", "content"]
    }
  ],
  "limitations": ["string"],
  "validation_status": "human_reviewed | pending_review | automated_only"
}
```

---

## Validation Requirements

| Tier | Requirement |
|------|-------------|
| 🟢 Exploratory | Baseline comparison, statistical thresholds |
| 🟡 Pilot | + Human review of top 10% flagged cases |
| 🔴 Publication | + Systematic validation (known campaign), F1 ≥ 0.6 |

---

## Known Limitations

1. **Organic activists coordinate** — Coordination ≠ inauthenticity
2. **Platform algorithms amplify** — May look like coordination
3. **Breaking news clusters organically** — Time-based patterns expected
4. **Attribution impossible** — Cannot identify actors from behavior

---

## TODO

- [ ] Create benchmark with known coordinated + organic campaigns
- [ ] Add network analysis module
- [ ] Add account-level behavioral analysis
- [ ] Peer validation

---

## References

- Keller, F. B., et al. (2020). Political astroturfing on Twitter.
- Pacheco, D., et al. (2021). Uncovering coordinated networks on social media.
- Nizzoli, L., et al. (2021). Coordinated behavior on social media in 2019 UK general election.
