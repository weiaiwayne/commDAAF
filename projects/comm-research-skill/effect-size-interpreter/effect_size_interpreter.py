#!/usr/bin/env python3
"""
CommDAAF Effect Size Interpreter

Calculate, benchmark, and interpret effect sizes for communication research.
"""

import math
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from enum import Enum

class EffectMagnitude(Enum):
    NEGLIGIBLE = "negligible"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    VERY_LARGE = "very_large"


@dataclass
class EffectSize:
    """Container for effect size calculation results."""
    measure: str
    value: float
    ci_lower: Optional[float] = None
    ci_upper: Optional[float] = None
    p_value: Optional[float] = None
    magnitude: Optional[EffectMagnitude] = None
    interpretation: Optional[str] = None
    practical_meaning: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            "measure": self.measure,
            "value": round(self.value, 3),
            "ci_95": [round(self.ci_lower, 3), round(self.ci_upper, 3)] if self.ci_lower else None,
            "p_value": self.p_value,
            "magnitude": self.magnitude.value if self.magnitude else None,
            "interpretation": self.interpretation,
            "practical_meaning": self.practical_meaning
        }


# Benchmark thresholds
BENCHMARKS = {
    "cohens_d": {
        "negligible": 0.1,
        "small": 0.2,
        "medium": 0.5,
        "large": 0.8,
        "very_large": 1.2
    },
    "eta_squared": {
        "negligible": 0.005,
        "small": 0.01,
        "medium": 0.06,
        "large": 0.14,
        "very_large": 0.20
    },
    "r": {
        "negligible": 0.05,
        "small": 0.1,
        "medium": 0.3,
        "large": 0.5,
        "very_large": 0.7
    },
    "r_squared": {
        "negligible": 0.01,
        "small": 0.02,
        "medium": 0.13,
        "large": 0.26,
        "very_large": 0.40
    },
    "irr": {  # Incidence Rate Ratio
        "negligible": 1.2,
        "small": 1.5,
        "medium": 2.5,
        "large": 4.0,
        "very_large": 6.0
    },
    "odds_ratio": {
        "negligible": 1.2,
        "small": 1.5,
        "medium": 2.5,
        "large": 4.0,
        "very_large": 6.0
    }
}

# Communication research specific benchmarks
COMM_BENCHMARKS = {
    "framing_effects": {"typical_d": 0.30, "source": "Druckman 2001"},
    "emotional_sharing": {"typical_or": 1.20, "source": "Brady et al. 2017"},
    "source_credibility": {"typical_d": 0.40, "source": "Pornpitakpan 2004"},
    "agenda_setting": {"typical_r": 0.50, "source": "McCombs & Shaw 1972"},
    "cultivation": {"typical_r": 0.10, "source": "Morgan & Shanahan 2010"},
    "media_effects": {"typical_r": 0.15, "source": "Valkenburg et al. 2016"}
}


def classify_magnitude(value: float, measure: str) -> EffectMagnitude:
    """Classify effect size magnitude based on benchmarks."""
    if measure not in BENCHMARKS:
        raise ValueError(f"Unknown measure: {measure}")
    
    thresholds = BENCHMARKS[measure]
    abs_value = abs(value)
    
    # For ratio measures (IRR, OR), compare distance from 1
    if measure in ["irr", "odds_ratio"]:
        # Convert ratio to distance from 1
        if value >= 1:
            abs_value = value
        else:
            abs_value = 1 / value  # e.g., 0.5 becomes 2.0
        
        if abs_value < thresholds["negligible"]:
            return EffectMagnitude.NEGLIGIBLE
        elif abs_value < thresholds["small"]:
            return EffectMagnitude.SMALL
        elif abs_value < thresholds["medium"]:
            return EffectMagnitude.MEDIUM
        elif abs_value < thresholds["large"]:
            return EffectMagnitude.LARGE
        else:
            return EffectMagnitude.VERY_LARGE
    
    # For standard effect sizes
    if abs_value < thresholds["negligible"]:
        return EffectMagnitude.NEGLIGIBLE
    elif abs_value < thresholds["small"]:
        return EffectMagnitude.SMALL
    elif abs_value < thresholds["medium"]:
        return EffectMagnitude.MEDIUM
    elif abs_value < thresholds["large"]:
        return EffectMagnitude.LARGE
    else:
        return EffectMagnitude.VERY_LARGE


def cohens_d(
    group1_mean: float, group1_sd: float, group1_n: int,
    group2_mean: float, group2_sd: float, group2_n: int,
    pooled: bool = True
) -> EffectSize:
    """
    Calculate Cohen's d for independent samples.
    
    Args:
        group1_mean, group1_sd, group1_n: Stats for group 1
        group2_mean, group2_sd, group2_n: Stats for group 2
        pooled: Use pooled SD (default) or group1 SD
    
    Returns:
        EffectSize object
    """
    mean_diff = group1_mean - group2_mean
    
    if pooled:
        # Pooled standard deviation
        pooled_var = (
            ((group1_n - 1) * group1_sd**2 + (group2_n - 1) * group2_sd**2) /
            (group1_n + group2_n - 2)
        )
        pooled_sd = math.sqrt(pooled_var)
        d = mean_diff / pooled_sd
    else:
        d = mean_diff / group1_sd
    
    # Approximate 95% CI (using variance of d)
    var_d = (group1_n + group2_n) / (group1_n * group2_n) + d**2 / (2 * (group1_n + group2_n))
    se_d = math.sqrt(var_d)
    ci_lower = d - 1.96 * se_d
    ci_upper = d + 1.96 * se_d
    
    magnitude = classify_magnitude(d, "cohens_d")
    
    return EffectSize(
        measure="Cohen's d",
        value=d,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        magnitude=magnitude,
        interpretation=f"The difference is {magnitude.value} (d = {d:.2f})",
        practical_meaning=_interpret_cohens_d(d)
    )


def _interpret_cohens_d(d: float) -> str:
    """Generate practical interpretation for Cohen's d."""
    abs_d = abs(d)
    direction = "higher" if d > 0 else "lower"
    
    if abs_d < 0.2:
        return f"Groups are nearly identical"
    elif abs_d < 0.5:
        return f"Group 1 is slightly {direction} (small practical difference)"
    elif abs_d < 0.8:
        return f"Group 1 is moderately {direction} (noticeable practical difference)"
    else:
        return f"Group 1 is substantially {direction} (large practical difference)"


def interpret_irr(
    irr: float,
    ci_lower: float = None,
    ci_upper: float = None,
    p_value: float = None,
    predictor_name: str = "predictor",
    reference_name: str = "reference"
) -> EffectSize:
    """
    Interpret Incidence Rate Ratio from negative binomial/Poisson regression.
    
    Args:
        irr: Incidence rate ratio
        ci_lower, ci_upper: 95% confidence interval
        p_value: P-value
        predictor_name: Name of predictor variable
        reference_name: Name of reference category
    
    Returns:
        EffectSize object
    """
    magnitude = classify_magnitude(irr, "irr")
    
    # Practical interpretation
    if irr >= 1:
        pct_change = (irr - 1) * 100
        direction = "more"
        comparison = f"{irr:.2f}x"
    else:
        pct_change = (1 - irr) * 100
        direction = "less"
        comparison = f"{1/irr:.2f}x less"
    
    interpretation = f"{predictor_name} shows {pct_change:.0f}% {direction} engagement than {reference_name}"
    
    if irr >= 2:
        practical = f"Posts with {predictor_name} receive {comparison} the engagement of {reference_name}"
    elif irr >= 1.5:
        practical = f"{predictor_name} shows substantially higher engagement than {reference_name}"
    elif irr >= 1.2:
        practical = f"{predictor_name} shows moderately higher engagement than {reference_name}"
    elif irr > 0.8:
        practical = f"Little practical difference between {predictor_name} and {reference_name}"
    else:
        practical = f"{predictor_name} shows substantially lower engagement than {reference_name}"
    
    return EffectSize(
        measure="IRR",
        value=irr,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        p_value=p_value,
        magnitude=magnitude,
        interpretation=interpretation,
        practical_meaning=practical
    )


def interpret_odds_ratio(
    or_value: float,
    ci_lower: float = None,
    ci_upper: float = None,
    p_value: float = None,
    predictor_name: str = "predictor",
    outcome_name: str = "outcome"
) -> EffectSize:
    """
    Interpret Odds Ratio from logistic regression.
    """
    magnitude = classify_magnitude(or_value, "odds_ratio")
    
    if or_value >= 1:
        times = or_value
        direction = "more likely"
    else:
        times = 1 / or_value
        direction = "less likely"
    
    interpretation = f"{predictor_name} is associated with {times:.2f}x odds of {outcome_name}"
    
    return EffectSize(
        measure="OR",
        value=or_value,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        p_value=p_value,
        magnitude=magnitude,
        interpretation=interpretation,
        practical_meaning=f"Those with {predictor_name} are {times:.1f} times {direction} to show {outcome_name}"
    )


def multiple_comparison_correction(
    p_values: List[float],
    method: str = "fdr"
) -> Tuple[List[float], List[bool]]:
    """
    Apply multiple comparison correction.
    
    Args:
        p_values: List of p-values
        method: 'bonferroni', 'holm', or 'fdr' (Benjamini-Hochberg)
    
    Returns:
        (adjusted_p_values, significant_flags)
    """
    n = len(p_values)
    
    if method == "bonferroni":
        adjusted = [min(p * n, 1.0) for p in p_values]
        significant = [p < 0.05 for p in adjusted]
        
    elif method == "holm":
        # Sort p-values
        indexed = sorted(enumerate(p_values), key=lambda x: x[1])
        adjusted = [0.0] * n
        
        for rank, (orig_idx, p) in enumerate(indexed):
            adjusted[orig_idx] = min(p * (n - rank), 1.0)
        
        # Ensure monotonicity
        for i in range(1, n):
            if adjusted[i] < adjusted[i-1]:
                adjusted[i] = adjusted[i-1]
        
        significant = [p < 0.05 for p in adjusted]
        
    elif method == "fdr":
        # Benjamini-Hochberg
        indexed = sorted(enumerate(p_values), key=lambda x: x[1])
        adjusted = [0.0] * n
        
        for rank, (orig_idx, p) in enumerate(indexed, 1):
            adjusted[orig_idx] = min(p * n / rank, 1.0)
        
        # Ensure monotonicity (reverse)
        for i in range(n-2, -1, -1):
            if adjusted[i] > adjusted[i+1]:
                adjusted[i] = adjusted[i+1]
        
        significant = [p < 0.05 for p in adjusted]
        
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return adjusted, significant


def compare_to_field_norms(
    effect_value: float,
    effect_type: str,
    domain: str = "media_effects"
) -> str:
    """
    Compare effect to typical effects in communication research.
    
    Args:
        effect_value: The observed effect size
        effect_type: 'd', 'r', 'or', 'irr'
        domain: Research domain for comparison
    
    Returns:
        Narrative comparison
    """
    if domain not in COMM_BENCHMARKS:
        return f"No benchmark available for domain: {domain}"
    
    benchmark = COMM_BENCHMARKS[domain]
    
    if effect_type == "d" and "typical_d" in benchmark:
        typical = benchmark["typical_d"]
        if abs(effect_value) > typical * 1.5:
            comparison = "substantially exceeds"
        elif abs(effect_value) > typical:
            comparison = "exceeds"
        elif abs(effect_value) > typical * 0.5:
            comparison = "is comparable to"
        else:
            comparison = "is smaller than"
        return f"This effect (d={effect_value:.2f}) {comparison} typical {domain} effects (d={typical}; {benchmark['source']})"
    
    elif effect_type in ["or", "irr"] and "typical_or" in benchmark:
        typical = benchmark["typical_or"]
        if effect_value > typical * 2:
            comparison = "substantially exceeds"
        elif effect_value > typical:
            comparison = "exceeds"
        else:
            comparison = "is comparable to or smaller than"
        return f"This effect ({effect_type.upper()}={effect_value:.2f}) {comparison} typical {domain} effects ({benchmark['source']})"
    
    elif effect_type == "r" and "typical_r" in benchmark:
        typical = benchmark["typical_r"]
        if abs(effect_value) > typical * 1.5:
            comparison = "substantially exceeds"
        elif abs(effect_value) > typical:
            comparison = "exceeds"
        else:
            comparison = "is comparable to or smaller than"
        return f"This effect (r={effect_value:.2f}) {comparison} typical {domain} effects (r={typical}; {benchmark['source']})"
    
    return f"Effect type {effect_type} not available for domain {domain}"


def generate_results_narrative(
    effects: List[EffectSize],
    model_type: str = "regression",
    alpha: float = 0.05
) -> str:
    """
    Generate APA-style results narrative from effect sizes.
    """
    lines = []
    
    # Sort by magnitude
    sorted_effects = sorted(
        [e for e in effects if e.p_value and e.p_value < alpha],
        key=lambda x: abs(x.value) if x.measure == "Cohen's d" else x.value,
        reverse=True
    )
    
    if not sorted_effects:
        return "No statistically significant effects were observed."
    
    lines.append("Results revealed the following significant effects:")
    
    for e in sorted_effects:
        if e.measure == "IRR":
            line = f"- {e.practical_meaning} (IRR = {e.value:.2f}"
        elif e.measure == "Cohen's d":
            line = f"- {e.practical_meaning} (d = {e.value:.2f}"
        else:
            line = f"- {e.interpretation} ({e.measure} = {e.value:.2f}"
        
        if e.ci_lower and e.ci_upper:
            line += f", 95% CI [{e.ci_lower:.2f}, {e.ci_upper:.2f}]"
        if e.p_value:
            if e.p_value < 0.001:
                line += ", p < .001"
            else:
                line += f", p = {e.p_value:.3f}"
        line += ")"
        
        lines.append(line)
    
    # Note non-significant effects
    nonsig = [e for e in effects if e.p_value and e.p_value >= alpha]
    if nonsig:
        names = [e.interpretation.split()[0] for e in nonsig]
        lines.append(f"\nThe following predictors did not reach significance: {', '.join(names)}.")
    
    return "\n".join(lines)


if __name__ == "__main__":
    # Demo: interpret #MahsaAmini results
    
    # Cohen's d for CONFLICT vs SOLIDARITY
    d_result = cohens_d(
        group1_mean=3.48, group1_sd=2.96, group1_n=18,  # CONFLICT
        group2_mean=1.73, group2_sd=2.28, group2_n=122  # SOLIDARITY
    )
    print("=== Cohen's d (CONFLICT vs SOLIDARITY) ===")
    print(d_result.to_dict())
    
    # IRR interpretations
    print("\n=== IRR Interpretations ===")
    irr_info = interpret_irr(2.72, 1.52, 4.87, 0.001, "INFORMATIONAL", "SOLIDARITY")
    print(irr_info.to_dict())
    
    irr_arousal = interpret_irr(1.58, 1.03, 2.43, 0.038, "High arousal", "Low arousal")
    print(irr_arousal.to_dict())
    
    # Multiple comparison correction
    print("\n=== Multiple Comparison Correction ===")
    p_values = [0.001, 0.038, 0.124, 0.259, 0.310, 0.643]
    adj_p, sig = multiple_comparison_correction(p_values, method="fdr")
    print(f"Original: {p_values}")
    print(f"FDR-adjusted: {[round(p, 3) for p in adj_p]}")
    print(f"Significant: {sig}")
    
    # Field comparison
    print("\n=== Field Comparison ===")
    print(compare_to_field_norms(2.72, "irr", "emotional_sharing"))
    
    # Generate narrative
    print("\n=== Results Narrative ===")
    effects = [irr_info, irr_arousal]
    print(generate_results_narrative(effects))
