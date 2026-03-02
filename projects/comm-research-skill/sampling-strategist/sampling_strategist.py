#!/usr/bin/env python3
"""
CommDAAF Sampling Strategist

Design and implement sampling strategies for content analysis.
"""

import math
import random
from typing import Dict, List, Optional, Tuple, Any, Callable
from dataclasses import dataclass
from collections import Counter
import json

@dataclass
class SamplingPlan:
    """Container for sampling plan specification."""
    strategy: str
    population_n: int
    sample_n: int
    strata: List[Dict]
    constraints: List[str]
    power_analysis: Optional[Dict] = None
    random_seed: Optional[int] = None
    
    def to_dict(self):
        return {
            "strategy": self.strategy,
            "population_n": self.population_n,
            "sample_n": self.sample_n,
            "strata": self.strata,
            "constraints": self.constraints,
            "power_analysis": self.power_analysis,
            "random_seed": self.random_seed
        }
    
    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent)


@dataclass
class PowerResult:
    """Container for power analysis results."""
    n_required: int
    effect_size: float
    power: float
    alpha: float
    groups: int
    design: str
    notes: List[str]
    
    def to_dict(self):
        return {
            "n_required": self.n_required,
            "effect_size": self.effect_size,
            "power": self.power,
            "alpha": self.alpha,
            "groups": self.groups,
            "design": self.design,
            "notes": self.notes
        }


@dataclass
class SaturationResult:
    """Container for saturation analysis results."""
    is_saturated: bool
    n: int
    unique_codes: int
    last_new_code_at: int
    saturation_ratio: float
    recommendation: str


def calculate_percentiles(values: List[float], percentiles: List[float]) -> Dict[float, float]:
    """Calculate percentile values from a list."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    result = {}
    for p in percentiles:
        idx = int(p / 100 * (n - 1))
        result[p] = sorted_vals[idx]
    return result


def simple_random_sample(
    data: List[Dict],
    n: int,
    random_seed: Optional[int] = None
) -> List[Dict]:
    """
    Simple random sample from data.
    
    Args:
        data: List of records (dicts)
        n: Sample size
        random_seed: For reproducibility
    
    Returns:
        Sampled records
    """
    if random_seed:
        random.seed(random_seed)
    
    if n >= len(data):
        return data.copy()
    
    return random.sample(data, n)


def stratified_sample(
    data: List[Dict],
    strata_var: str,
    n_per_stratum: Optional[int] = None,
    total_n: Optional[int] = None,
    allocation: str = "equal",
    random_seed: Optional[int] = None
) -> Tuple[List[Dict], Dict[str, int]]:
    """
    Stratified sample from data.
    
    Args:
        data: List of records (dicts)
        strata_var: Variable to stratify by
        n_per_stratum: Fixed n per stratum (for equal allocation)
        total_n: Total sample size (for proportional allocation)
        allocation: 'equal' or 'proportional'
        random_seed: For reproducibility
    
    Returns:
        (sampled_records, stratum_counts)
    """
    if random_seed:
        random.seed(random_seed)
    
    # Group by stratum
    strata = {}
    for record in data:
        stratum = record.get(strata_var)
        if stratum not in strata:
            strata[stratum] = []
        strata[stratum].append(record)
    
    # Calculate n per stratum
    if allocation == "equal":
        if n_per_stratum is None:
            raise ValueError("n_per_stratum required for equal allocation")
        stratum_n = {s: n_per_stratum for s in strata}
    elif allocation == "proportional":
        if total_n is None:
            raise ValueError("total_n required for proportional allocation")
        total = len(data)
        stratum_n = {s: int(len(records) / total * total_n) 
                     for s, records in strata.items()}
    else:
        raise ValueError(f"Unknown allocation: {allocation}")
    
    # Sample from each stratum
    sampled = []
    counts = {}
    for stratum, records in strata.items():
        n = min(stratum_n.get(stratum, 0), len(records))
        sampled.extend(random.sample(records, n))
        counts[stratum] = n
    
    return sampled, counts


def engagement_tiered_sample(
    data: List[Dict],
    engagement_var: str,
    tiers: Dict[str, Dict],
    random_seed: Optional[int] = None
) -> Tuple[List[Dict], Dict[str, int]]:
    """
    Sample stratified by engagement tiers.
    
    Args:
        data: List of records
        engagement_var: Name of engagement variable
        tiers: Dict of tier specs, e.g.:
            {
                "viral": {"percentile": (95, 100), "n": 100},
                "high": {"percentile": (75, 95), "n": 100},
                ...
            }
        random_seed: For reproducibility
    
    Returns:
        (sampled_records, tier_counts)
    """
    if random_seed:
        random.seed(random_seed)
    
    # Calculate percentile cutoffs
    engagement_values = [r[engagement_var] for r in data]
    all_percentiles = set()
    for tier_spec in tiers.values():
        all_percentiles.update(tier_spec["percentile"])
    cutoffs = calculate_percentiles(engagement_values, list(all_percentiles))
    
    # Assign records to tiers
    tier_records = {tier: [] for tier in tiers}
    for record in data:
        eng = record[engagement_var]
        for tier_name, tier_spec in tiers.items():
            pct_low, pct_high = tier_spec["percentile"]
            low_val = cutoffs.get(pct_low, float('-inf'))
            high_val = cutoffs.get(pct_high, float('inf'))
            if low_val <= eng < high_val or (pct_high == 100 and eng >= low_val):
                tier_records[tier_name].append(record)
                break
    
    # Sample from each tier
    sampled = []
    counts = {}
    for tier_name, records in tier_records.items():
        n = min(tiers[tier_name]["n"], len(records))
        sampled.extend(random.sample(records, n) if n < len(records) else records)
        counts[tier_name] = n
    
    # Add tier label to records
    for record in sampled:
        eng = record[engagement_var]
        for tier_name, tier_spec in tiers.items():
            pct_low, pct_high = tier_spec["percentile"]
            low_val = cutoffs.get(pct_low, float('-inf'))
            high_val = cutoffs.get(pct_high, float('inf'))
            if low_val <= eng < high_val or (pct_high == 100 and eng >= low_val):
                record["tier"] = tier_name
                break
    
    return sampled, counts


def power_analysis(
    effect_size: float = 0.5,
    groups: int = 2,
    alpha: float = 0.05,
    power: float = 0.80
) -> PowerResult:
    """
    Calculate required sample size for given effect size and power.
    
    Uses approximation formulas for t-test (2 groups) and ANOVA (>2 groups).
    
    Args:
        effect_size: Cohen's d (or f for ANOVA)
        groups: Number of groups
        alpha: Significance level
        power: Desired power
    
    Returns:
        PowerResult with required n per group
    """
    # Z-scores for alpha and power
    z_alpha = 1.96 if alpha == 0.05 else 2.576 if alpha == 0.01 else 1.645
    z_power = 0.84 if power == 0.80 else 1.28 if power == 0.90 else 0.52
    
    if groups == 2:
        # Two-sample t-test
        n_per_group = int(2 * ((z_alpha + z_power) / effect_size) ** 2) + 1
        design = "independent samples t-test"
    else:
        # One-way ANOVA approximation
        # Convert d to f (f ≈ d/2 for comparing extreme groups)
        f = effect_size / 2
        # Approximate n per group
        n_per_group = int(((z_alpha + z_power) ** 2) / (f ** 2 * groups)) + 1
        design = f"one-way ANOVA ({groups} groups)"
    
    notes = [
        f"Assumes {effect_size:.2f} effect size (Cohen's d)",
        f"Power = {power:.0%} to detect effect",
        f"Two-tailed test at α = {alpha}",
        "Add 10-20% for attrition"
    ]
    
    if n_per_group < 30:
        notes.append("WARNING: n < 30 per group may violate normality assumptions")
    
    return PowerResult(
        n_required=n_per_group,
        effect_size=effect_size,
        power=power,
        alpha=alpha,
        groups=groups,
        design=design,
        notes=notes
    )


def check_saturation(
    coded_data: List[Dict],
    code_var: str,
    window: int = 50,
    threshold: float = 0.05
) -> SaturationResult:
    """
    Check if coding has reached saturation (no new codes emerging).
    
    Args:
        coded_data: List of coded records
        code_var: Variable containing codes
        window: Number of recent records to check
        threshold: Proportion of new codes below which = saturated
    
    Returns:
        SaturationResult
    """
    if len(coded_data) < window:
        return SaturationResult(
            is_saturated=False,
            n=len(coded_data),
            unique_codes=len(set(r[code_var] for r in coded_data)),
            last_new_code_at=len(coded_data),
            saturation_ratio=1.0,
            recommendation="Continue sampling; insufficient data for saturation check"
        )
    
    # Track when each code first appeared
    seen_codes = set()
    last_new_code_at = 0
    for i, record in enumerate(coded_data):
        code = record[code_var]
        if code not in seen_codes:
            seen_codes.add(code)
            last_new_code_at = i + 1
    
    # Check proportion of new codes in window
    recent_codes = [r[code_var] for r in coded_data[-window:]]
    codes_before_window = set(r[code_var] for r in coded_data[:-window])
    new_in_window = len([c for c in recent_codes if c not in codes_before_window])
    saturation_ratio = new_in_window / window
    
    is_saturated = saturation_ratio < threshold
    
    if is_saturated:
        recommendation = f"Saturation reached. Last new code at n={last_new_code_at}. Consider stopping."
    else:
        recommendation = f"Not saturated ({saturation_ratio:.1%} new codes in last {window}). Continue sampling."
    
    return SaturationResult(
        is_saturated=is_saturated,
        n=len(coded_data),
        unique_codes=len(seen_codes),
        last_new_code_at=last_new_code_at,
        saturation_ratio=saturation_ratio,
        recommendation=recommendation
    )


def identify_outliers(
    data: List[Dict],
    variable: str,
    method: str = "iqr",
    n_outliers: int = 20
) -> List[Dict]:
    """
    Identify outlier records for qualitative follow-up.
    
    Args:
        data: List of records
        variable: Numeric variable to check
        method: 'iqr', 'zscore', or 'extreme'
        n_outliers: Max outliers to return
    
    Returns:
        List of outlier records
    """
    values = [r[variable] for r in data]
    
    if method == "iqr":
        sorted_vals = sorted(values)
        q1 = sorted_vals[int(len(sorted_vals) * 0.25)]
        q3 = sorted_vals[int(len(sorted_vals) * 0.75)]
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        
        outliers = [r for r in data 
                   if r[variable] < lower or r[variable] > upper]
    
    elif method == "zscore":
        mean = sum(values) / len(values)
        std = math.sqrt(sum((v - mean)**2 for v in values) / len(values))
        
        outliers = []
        for r in data:
            z = (r[variable] - mean) / std if std > 0 else 0
            if abs(z) > 2.5:
                r["_zscore"] = z
                outliers.append(r)
    
    elif method == "extreme":
        # Just get top and bottom extremes
        sorted_data = sorted(data, key=lambda r: r[variable])
        n_each = n_outliers // 2
        outliers = sorted_data[:n_each] + sorted_data[-n_each:]
    
    else:
        raise ValueError(f"Unknown method: {method}")
    
    # Sort by extremity and limit
    outliers = sorted(outliers, key=lambda r: abs(r[variable]), reverse=True)
    return outliers[:n_outliers]


def create_sampling_plan(
    population_n: int,
    sample_n: int,
    strata_specs: Dict[str, Dict],
    constraints: List[str] = None,
    random_seed: int = None
) -> SamplingPlan:
    """
    Create a formal sampling plan.
    
    Args:
        population_n: Size of population
        sample_n: Target sample size
        strata_specs: Dict of stratum specifications
        constraints: List of constraint descriptions
        random_seed: For reproducibility
    
    Returns:
        SamplingPlan object
    """
    strata = []
    for name, spec in strata_specs.items():
        stratum = {
            "name": name,
            "type": spec.get("type", "categorical"),
            "levels": spec.get("levels", []),
            "allocation": spec.get("allocation", "equal")
        }
        strata.append(stratum)
    
    # Calculate power for default effect size
    n_per_group = sample_n // len(strata_specs) if strata_specs else sample_n
    power = power_analysis(effect_size=0.5, groups=len(strata_specs) or 2)
    
    return SamplingPlan(
        strategy="multi-criteria stratified",
        population_n=population_n,
        sample_n=sample_n,
        strata=strata,
        constraints=constraints or [],
        power_analysis=power.to_dict(),
        random_seed=random_seed
    )


# Standard engagement tier configurations
STANDARD_ENGAGEMENT_TIERS = {
    "4_tier_equal": {
        "viral": {"percentile": (95, 100), "n": None},  # Set n dynamically
        "high": {"percentile": (75, 95), "n": None},
        "medium": {"percentile": (25, 75), "n": None},
        "low": {"percentile": (0, 25), "n": None}
    },
    "5_tier_with_zero": {
        "viral": {"percentile": (95, 100), "n": None},
        "high": {"percentile": (75, 95), "n": None},
        "medium": {"percentile": (25, 75), "n": None},
        "low": {"percentile": (5, 25), "n": None},
        "zero": {"percentile": (0, 5), "n": None}  # Near-zero engagement
    }
}


def get_standard_tiers(
    template: str,
    n_per_tier: int
) -> Dict[str, Dict]:
    """Get standard tier configuration with specified n."""
    if template not in STANDARD_ENGAGEMENT_TIERS:
        raise ValueError(f"Unknown template: {template}")
    
    tiers = {}
    for name, spec in STANDARD_ENGAGEMENT_TIERS[template].items():
        tiers[name] = {
            "percentile": spec["percentile"],
            "n": n_per_tier
        }
    return tiers


if __name__ == "__main__":
    # Demo with synthetic data
    import random
    
    # Create synthetic tweet data
    random.seed(42)
    tweets = []
    for i in range(1000):
        engagement = random.expovariate(0.5)  # Exponential distribution
        tweets.append({
            "id": f"tweet_{i}",
            "engagement": engagement,
            "language": random.choices(["fa", "en", "ar"], weights=[70, 25, 5])[0],
            "verified": random.random() < 0.1
        })
    
    print("=== Power Analysis ===")
    power = power_analysis(effect_size=0.5, groups=7, power=0.80)
    print(json.dumps(power.to_dict(), indent=2))
    
    print("\n=== Engagement-Tiered Sampling ===")
    tiers = get_standard_tiers("4_tier_equal", n_per_tier=50)
    sample, counts = engagement_tiered_sample(
        tweets, 
        engagement_var="engagement",
        tiers=tiers,
        random_seed=42
    )
    print(f"Sample size: {len(sample)}")
    print(f"Tier counts: {counts}")
    
    print("\n=== Sampling Plan ===")
    plan = create_sampling_plan(
        population_n=1000,
        sample_n=200,
        strata_specs={
            "engagement": {"type": "quantile", "allocation": "equal"},
            "language": {"type": "categorical", "allocation": "proportional"}
        },
        constraints=["minimum 1 post per language", "verified ≤ 30%"],
        random_seed=42
    )
    print(plan.to_json())
