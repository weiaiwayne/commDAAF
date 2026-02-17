# Confound Checklist

**Purpose:** Force explicit identification of confounding variables before analysis.

---

## When to Use

Run this BEFORE any analysis that will make comparative or causal claims.

---

## The Checklist

Every analysis must document potential confounds. This isn't optional — reviewers will ask.

### 1. Temporal Confounds

```yaml
temporal_confounds:
  questions:
    - "What external events occurred during your study period?"
    - "Did the platform change its algorithm during this time?"
    - "Were there API changes that affected data collection?"
    - "Did follower/audience size change significantly?"
    
  common_issues:
    - news_cycle: "Breaking news drives engagement regardless of content"
    - platform_changes: "Algorithm updates (Twitter 2016, etc.) affect visibility"
    - seasonal_effects: "Holidays, elections, academic calendars"
    - growth_effects: "Larger accounts get more engagement mechanically"
  
  document:
    - time_period: "___"
    - known_events: "___"
    - platform_changes: "___"
    - how_addressed: "controlled for / acknowledged as limitation / N/A"
```

### 2. Content Confounds

```yaml
content_confounds:
  questions:
    - "Does content TYPE vary with your independent variable?"
    - "Do media attachments (images, video) correlate with your IV?"
    - "Does post length correlate with your IV?"
    - "Do hashtags/mentions correlate with your IV?"
  
  common_issues:
    - media_richness: "Posts with images get 2-3x engagement"
    - post_length: "Longer posts may signal effort/quality"
    - hashtag_use: "Hashtags increase discoverability"
    - mention_networks: "Mentions to large accounts get amplified"
  
  document:
    - content_types_present: "___"
    - media_distribution: "___"
    - correlation_with_iv: "___"
    - how_addressed: "controlled for / stratified / acknowledged"
```

### 3. Account-Level Confounds

```yaml
account_confounds:
  questions:
    - "Does account size (followers) correlate with your IV?"
    - "Does account age correlate with your IV?"
    - "Does account type (verified, org, individual) correlate?"
    - "Does posting frequency correlate with your IV?"
  
  common_issues:
    - follower_count: "More followers = more baseline engagement"
    - verification: "Verified accounts get algorithmic boost"
    - account_age: "Older accounts have established audiences"
    - activity_level: "Active accounts have more engaged followers"
  
  document:
    - follower_distribution: "___"
    - account_types: "___"
    - correlation_with_iv: "___"
    - how_addressed: "normalized / controlled / acknowledged"
```

### 4. Selection Confounds

```yaml
selection_confounds:
  questions:
    - "Why are these accounts/posts in your sample?"
    - "What's MISSING from your sample?"
    - "Could the selection criteria correlate with your DV?"
    - "Is there survivorship bias? (deleted accounts/posts)"
  
  common_issues:
    - keyword_selection: "Keyword choice determines who's included"
    - api_limits: "Rate limits may bias toward certain accounts"
    - deletion_bias: "Controversial content more likely deleted"
    - platform_filtering: "Platforms may hide certain content"
  
  document:
    - selection_criteria: "___"
    - known_gaps: "___"
    - survivorship_risk: "___"
    - how_addressed: "___"
```

---

## Confound Documentation Template

```markdown
## Confounding Variables

### Identified Confounds

| Confound | Correlation with IV | Correlation with DV | Strategy |
|----------|---------------------|---------------------|----------|
| Follower count | [yes/no/unknown] | [yes/no/unknown] | [control/acknowledge] |
| Media attachments | [yes/no/unknown] | [yes/no/unknown] | [control/acknowledge] |
| Time of posting | [yes/no/unknown] | [yes/no/unknown] | [control/acknowledge] |
| Account type | [yes/no/unknown] | [yes/no/unknown] | [control/acknowledge] |
| [Add more] | | | |

### Uncontrolled Confounds (Limitations)

These confounds were identified but could not be controlled:

1. **[Confound]**: [Why it couldn't be controlled, impact on interpretation]
2. **[Confound]**: [Why it couldn't be controlled, impact on interpretation]

### Confounds Checked and Ruled Out

These were checked and found not to correlate:

1. **[Variable]**: [Evidence it doesn't confound]
```

---

## Implementation

```python
def confound_checklist(data, iv_column, dv_column):
    """
    Automated confound detection.
    
    Checks correlation between common confounds and IV/DV.
    """
    import pandas as pd
    from scipy import stats
    
    potential_confounds = []
    
    # Check if these columns exist
    confound_columns = {
        'follower_count': 'Account size',
        'retweet_count': 'Prior engagement',
        'media_present': 'Media attachments',
        'text_length': 'Post length',
        'hour_posted': 'Time of day',
        'is_verified': 'Verification status',
        'account_age_days': 'Account age'
    }
    
    for col, name in confound_columns.items():
        if col in data.columns:
            # Correlation with IV
            if data[iv_column].dtype in ['int64', 'float64']:
                iv_corr, iv_p = stats.pearsonr(data[col], data[iv_column])
            else:
                # Categorical IV - use point-biserial or chi-square
                iv_corr, iv_p = None, None
            
            # Correlation with DV
            dv_corr, dv_p = stats.pearsonr(data[col], data[dv_column])
            
            if iv_corr and abs(iv_corr) > 0.1 and dv_p < 0.05:
                potential_confounds.append({
                    'variable': name,
                    'column': col,
                    'iv_correlation': iv_corr,
                    'dv_correlation': dv_corr,
                    'risk': 'HIGH' if abs(iv_corr) > 0.3 and abs(dv_corr) > 0.3 else 'MEDIUM'
                })
    
    if potential_confounds:
        print("⚠️ POTENTIAL CONFOUNDS DETECTED")
        print("=" * 50)
        for c in potential_confounds:
            print(f"\n{c['risk']} RISK: {c['variable']}")
            print(f"  Correlation with IV: r = {c['iv_correlation']:.3f}")
            print(f"  Correlation with DV: r = {c['dv_correlation']:.3f}")
            print(f"  → Must control for this or acknowledge as limitation")
    else:
        print("✓ No obvious confounds detected in available columns")
        print("  (Check manually for confounds not in data)")
    
    return potential_confounds
```

---

## Integration with Tiered Validation

| Tier | Confound Requirements |
|------|----------------------|
| 🟢 Exploratory | List potential confounds (no control required) |
| 🟡 Pilot | Check correlations, document uncontrolled |
| 🔴 Publication | Control statistically OR exclude from causal claims |
