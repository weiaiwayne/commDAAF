# Effect Size Interpreter Skill

Calculate, benchmark, and interpret effect sizes for communication research.

## When to Use

- After running statistical analyses
- Need to move beyond p-values to practical significance
- Comparing effects across studies
- Writing results sections that emphasize magnitude
- Preparing for peer review (effect sizes increasingly required)

## Capabilities

1. **Calculate Effect Sizes** - Cohen's d, η², IRR, odds ratios, r, R²
2. **Benchmark Against Norms** - Compare to field-specific conventions
3. **Interpret Practically** - Translate to meaningful statements
4. **Confidence Intervals** - Report uncertainty around estimates
5. **Multiple Comparison Correction** - Bonferroni, FDR, Holm

## Effect Size Types

| Measure | Use Case | Small | Medium | Large |
|---------|----------|-------|--------|-------|
| Cohen's d | Group differences | 0.2 | 0.5 | 0.8 |
| η² (eta-squared) | ANOVA | 0.01 | 0.06 | 0.14 |
| r (correlation) | Associations | 0.1 | 0.3 | 0.5 |
| R² | Variance explained | 0.02 | 0.13 | 0.26 |
| IRR (incidence rate ratio) | Count outcomes | 1.5 | 2.5 | 4.0 |
| Odds Ratio | Binary outcomes | 1.5 | 2.5 | 4.0 |

*Benchmarks from Cohen (1988) and field-specific literature*

## Usage

### Basic: Single Effect

```
Calculate and interpret Cohen's d for the difference between 
INFORMATIONAL frame (M=2.34, SD=2.31, n=34) and 
SOLIDARITY frame (M=1.73, SD=2.28, n=122)
```

### Advanced: Full Model Interpretation

```
Interpret these negative binomial regression results:
- INFORMATIONAL: IRR=2.72, 95% CI [1.52, 4.87], p<.001
- High arousal: IRR=1.58, 95% CI [1.03, 2.43], p=.038
- CONFLICT: IRR=1.89, 95% CI [0.84, 4.25], p=.124

Provide:
1. Effect size classification (small/medium/large)
2. Practical interpretation
3. Comparison to communication research norms
4. Confidence assessment
```

## Output Format

```json
{
  "effect": "INFORMATIONAL vs SOLIDARITY",
  "measure": "IRR",
  "value": 2.72,
  "ci_95": [1.52, 4.87],
  "p_value": 0.001,
  "classification": "large",
  "interpretation": "Posts with INFORMATIONAL framing received 2.72 times the engagement of SOLIDARITY posts",
  "practical_meaning": "Informational content substantially outperforms solidarity content in viral spread",
  "comparison_to_norms": "This effect exceeds typical frame effects in political communication (median IRR ~1.5)",
  "confidence": "high",
  "caveats": ["Small sample for INFORMATIONAL (n=34)", "Single study requires replication"]
}
```

## Communication Research Benchmarks

Based on meta-analyses and influential studies:

| Domain | Typical Effect | Source |
|--------|---------------|--------|
| Framing effects (attitudes) | d = 0.30 | Druckman 2001 |
| Emotional content → sharing | OR = 1.20 per moral word | Brady et al. 2017 |
| Source credibility | d = 0.40 | Pornpitakpan 2004 |
| Agenda-setting | r = 0.50 | McCombs & Shaw 1972 |
| Cultivation effects | r = 0.10 | Morgan & Shanahan 2010 |

## Integration with CommDAAF Pipeline

```python
from commdaaf import EffectSizeInterpreter

interpreter = EffectSizeInterpreter(field="communication")

# Single effect
result = interpreter.cohens_d(
    group1_mean=2.34, group1_sd=2.31, group1_n=34,
    group2_mean=1.73, group2_sd=2.28, group2_n=122
)

# From regression output
results = interpreter.from_regression(
    model_type="negative_binomial",
    coefficients={
        "INFORMATIONAL": {"irr": 2.72, "ci": [1.52, 4.87], "p": 0.001},
        "arousal_high": {"irr": 1.58, "ci": [1.03, 2.43], "p": 0.038}
    },
    reference="SOLIDARITY"
)

# Generate narrative interpretation
narrative = interpreter.to_narrative(results, style="apa")
```

## Multiple Comparison Correction

When testing multiple effects:

```python
interpreter.correct_multiple(
    p_values=[0.001, 0.038, 0.124, 0.259, 0.310],
    method="fdr"  # or "bonferroni", "holm"
)
```

## Practical Significance Translation

The interpreter can translate statistical effects to practical statements:

| IRR | Practical Meaning |
|-----|-------------------|
| 1.5 | 50% more engagement |
| 2.0 | Double the engagement |
| 2.72 | Nearly 3x the engagement |
| 4.0 | Quadruple the engagement |

## Limitations

- Benchmarks are approximate and context-dependent
- Small samples inflate effect sizes (use CI for uncertainty)
- Effect sizes don't establish causality
- Field norms vary by subdomain and method

## Best Practices

1. **Always report effect sizes** - Not just p-values
2. **Include confidence intervals** - Show uncertainty
3. **Use appropriate measures** - d for means, IRR for counts
4. **Benchmark in context** - What's "large" depends on domain
5. **Interpret practically** - What does this mean for real-world outcomes?

## References

- Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
- Lakens, D. (2013). Calculating and reporting effect sizes.
- Fritz, C. O., Morris, P. E., & Richler, J. J. (2012). Effect size estimates.
