# Sampling Strategist Skill

Design and implement sampling strategies for content analysis.

## When to Use

- Dataset too large to code entirely
- Need representative sample from population
- Want to oversample rare cases (viral posts, specific events)
- Require coverage of engagement distribution (viral to zero)
- Planning statistical analyses with power requirements

## Capabilities

1. **Stratified Sampling** - Equal/proportional representation across strata
2. **Purposive Sampling** - Theoretically interesting cases
3. **Temporal Sampling** - Time-weighted, event-based
4. **Engagement-Stratified** - Viral/high/medium/low tiers
5. **Power Analysis** - Sample size for planned comparisons
6. **Saturation Detection** - When to stop sampling
7. **Outlier Identification** - Unusual cases for qualitative follow-up

## Sampling Strategies

| Strategy | Use Case | When to Use |
|----------|----------|-------------|
| **Simple Random** | Representative slice | Homogeneous population |
| **Stratified** | Ensure subgroup coverage | Known important subgroups |
| **Engagement-Tiered** | Study virality | Viral content research |
| **Temporal** | Event-based | Breaking news, protest waves |
| **Purposive** | Theoretical cases | Theory building |
| **Cluster** | Reduce costs | Geographic/organizational units |
| **Snowball** | Hard-to-reach | Network-based phenomena |

## Usage

### Basic: Stratified by Engagement

```
Create a stratified sample of 400 tweets from a dataset of 10,000:
- Viral tier (top 5%): n = 100
- High tier (75th-95th percentile): n = 100
- Medium tier (25th-75th percentile): n = 100
- Low tier (bottom 25%): n = 100

Include engagement variable for tier calculation.
```

### Advanced: Multi-Criteria Sampling

```
Design a sampling strategy for analyzing #MahsaAmini tweets:
- Total population: 50,000 tweets
- Target sample: n = 500
- Requirements:
  - Engagement-stratified (viral to zero)
  - Temporal coverage (each day of protest)
  - Language coverage (Persian 70%, English 25%, Arabic 5%)
  - Verified/unverified balance
  
Output: Sampling specification + executable code
```

## Output Format

```json
{
  "strategy": "multi-criteria stratified",
  "population_n": 50000,
  "sample_n": 500,
  "strata": [
    {
      "name": "engagement",
      "type": "quantile",
      "levels": ["viral_5pct", "high_75_95", "medium_25_75", "low_25"],
      "allocation": "equal"
    },
    {
      "name": "language",
      "type": "categorical", 
      "levels": ["fa", "en", "ar"],
      "allocation": "proportional"
    }
  ],
  "constraints": [
    "minimum 1 post per day",
    "verified accounts ≤ 30%"
  ],
  "expected_cells": 12,
  "posts_per_cell": 42,
  "power_analysis": {
    "effect_detectable": "d = 0.35",
    "power": 0.80,
    "alpha": 0.05
  }
}
```

## Engagement Tier Definitions

Standard engagement tiers for social media research:

| Tier | Percentile | Typical Content |
|------|------------|-----------------|
| **Viral** | Top 5% | Breakthrough content, influencer posts |
| **High** | 75th-95th | Successful posts, engaged audiences |
| **Medium** | 25th-75th | Typical engagement, baseline performance |
| **Low** | Bottom 25% | Low visibility, potential bot content |
| **Zero** | Engagement = 0 | No spread, baseline content |

## Power Analysis Guidelines

For frame/content analysis comparisons:

| Design | Minimum n/group | Detects |
|--------|-----------------|---------|
| 2 groups, d=0.5 | 64 | Medium effect |
| 2 groups, d=0.3 | 175 | Small effect |
| 7 frames, d=0.3 | 50/frame | Small effect |
| Regression, 5 predictors | 100 total | Medium R² |

## Integration with CommDAAF Pipeline

```python
from commdaaf import SamplingStrategist

strategist = SamplingStrategist()

# Simple stratified sample
sample = strategist.stratified_sample(
    data=tweets,
    strata_var="engagement_tier",
    n_per_stratum=100,
    random_seed=42
)

# Engagement-tiered sample
sample = strategist.engagement_tiers(
    data=tweets,
    engagement_var="composite_engagement",
    tiers={
        "viral": {"percentile": (95, 100), "n": 100},
        "high": {"percentile": (75, 95), "n": 100},
        "medium": {"percentile": (25, 75), "n": 100},
        "low": {"percentile": (0, 25), "n": 100}
    }
)

# Power analysis
power = strategist.power_analysis(
    effect_size="medium",  # or d=0.5
    groups=7,
    alpha=0.05,
    power=0.80
)

# Multi-criteria sampling
sample = strategist.multi_criteria(
    data=tweets,
    strata={
        "engagement_tier": {"allocation": "equal"},
        "language": {"allocation": "proportional"},
        "date": {"allocation": "coverage"}  # at least 1 per day
    },
    total_n=500,
    constraints={"verified": {"max_prop": 0.30}}
)
```

## Saturation Detection

For qualitative/exploratory sampling:

```python
# Check if additional sampling would add new patterns
saturation = strategist.check_saturation(
    coded_data=coded_tweets,
    code_var="frame",
    window=50,  # last 50 posts
    threshold=0.05  # <5% new codes = saturated
)

if saturation.is_saturated:
    print(f"Saturation reached at n={saturation.n}")
    print(f"Last new code at n={saturation.last_new_code}")
```

## Outlier Identification

For finding unusual cases:

```python
# Identify outliers for qualitative follow-up
outliers = strategist.identify_outliers(
    data=tweets,
    variables=["engagement", "sentiment"],
    method="iqr",  # or "zscore", "isolation_forest"
    n_outliers=20
)
```

## Best Practices

1. **Document your strategy** - Pre-register sampling plan before data collection
2. **Match strategy to question** - Virality studies need engagement-stratified samples
3. **Check coverage** - Verify sample covers intended population
4. **Report attrition** - Document any posts dropped (deleted, unavailable)
5. **Use random seed** - Enable reproducibility
6. **Power before sampling** - Calculate required n before committing

## Limitations

- Stratified sampling requires known strata
- Power analysis assumes effect size estimates (often uncertain)
- Temporal sampling may miss off-hours content
- Platform APIs may introduce systematic biases

## References

- Krippendorff, K. (2018). Content analysis: An introduction to its methodology.
- Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
- Guest, G., Bunce, A., & Johnson, L. (2006). How many interviews are enough?
