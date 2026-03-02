# Study Design Warnings

**Purpose:** Automatically detect study design limitations and enforce appropriate claim scoping.

---

## Automatic Detection

CommDAAF infers study design from data characteristics and enforces corresponding claim limits.

---

## Design Detection Logic

```python
def detect_study_design(data_info):
    """
    Infer study design from data characteristics.
    
    Args:
        data_info: Dict with keys:
            - n_units: Number of unique accounts/entities
            - n_time_points: Number of distinct time periods
            - has_comparison: Whether there's a treatment/control
            - manipulation: Whether researcher manipulated anything
    
    Returns:
        Study design classification and claim limits
    """
    
    n_units = data_info.get('n_units', 1)
    n_time_points = data_info.get('n_time_points', 1)
    has_comparison = data_info.get('has_comparison', False)
    manipulation = data_info.get('manipulation', False)
    
    # Single case study
    if n_units == 1:
        return {
            'design': 'single_case_study',
            'generalizability': 'none',
            'causal_inference': 'none',
            'claim_scope': 'this_case_only',
            'warnings': [
                'SINGLE CASE: Findings cannot generalize to other accounts/brands',
                'No prescriptive claims allowed ("brands should...")',
                'Frame as: "In this case, we observed..."'
            ]
        }
    
    # Cross-sectional
    if n_time_points == 1 and n_units > 1:
        return {
            'design': 'cross_sectional',
            'generalizability': 'to_similar_populations',
            'causal_inference': 'none',
            'claim_scope': 'associations_only',
            'warnings': [
                'CROSS-SECTIONAL: Cannot make temporal claims',
                'Cannot say "X leads to Y" without time dimension',
                'Use: "X is associated with Y"'
            ]
        }
    
    # Longitudinal observational
    if n_time_points > 1 and not manipulation:
        return {
            'design': 'longitudinal_observational',
            'generalizability': 'temporal_within_context',
            'causal_inference': 'limited',
            'claim_scope': 'temporal_associations',
            'warnings': [
                'OBSERVATIONAL: Cannot rule out confounds',
                'Temporal precedence ≠ causation',
                'Use: "Changes in X precede changes in Y"'
            ]
        }
    
    # Experimental
    if manipulation:
        return {
            'design': 'experimental',
            'generalizability': 'to_similar_samples',
            'causal_inference': 'strong',
            'claim_scope': 'causal_within_sample',
            'warnings': [
                'Check: Was randomization successful?',
                'Check: Any attrition/compliance issues?',
                'External validity may be limited'
            ]
        }
    
    return {
        'design': 'unknown',
        'warnings': ['Could not determine study design. Manually specify.']
    }
```

---

## Design-Specific Warnings

### Single Case Study (N=1)

**Automatic triggers:**
- Only one account/entity in data
- Only one brand/organization
- Single event analysis

**Enforced restrictions:**

```yaml
single_case_restrictions:
  
  forbidden_language:
    - pattern: "brands should"
    - pattern: "platforms should"
    - pattern: "users should"
    - pattern: "this demonstrates that [general claim]"
    - pattern: "we recommend"
    - replacement: "In this case, we observed..."
  
  required_hedging:
    - "This case study of [specific entity]..."
    - "These findings are specific to [entity]..."
    - "Generalization requires additional research..."
  
  implication_warning: |
    ⚠️ SINGLE CASE STUDY DETECTED
    
    Your data contains only one [account/brand/entity].
    
    What you CAN say:
    - "This account showed X pattern"
    - "In this case, we observed Y"
    - "This example illustrates how [specific entity] approaches Z"
    
    What you CANNOT say:
    - "Brands should do X"
    - "This demonstrates that Y causes Z"
    - "These findings suggest that [general population] should..."
    
    Why? N=1 tells us about that one case. It cannot tell us about 
    other cases without evidence that this case is representative.
    
    To make general claims, you need:
    - Multiple cases
    - Evidence of representativeness
    - Replication
```

### Small-N Comparative

**Automatic triggers:**
- 2-10 accounts/entities
- Qualitative comparison design

**Enforced restrictions:**

```yaml
small_n_restrictions:
  
  warning: |
    ⚠️ SMALL-N STUDY (n={n})
    
    Your findings are based on {n} cases. This limits:
    
    1. Statistical power (may miss real effects)
    2. Generalizability (are these cases representative?)
    3. Quantitative claims (avoid precise percentages)
    
    Appropriate framing:
    - "Among the {n} [entities] examined..."
    - "This comparative analysis suggests..."
    - "These cases illustrate [pattern], though generalization is limited"
    
    Not appropriate:
    - "X% of [entities] do Y" (implies larger sample)
    - Strong causal claims
    - Population-level recommendations
```

### Cross-Sectional Snapshot

**Automatic triggers:**
- Single time point
- No temporal dimension

**Enforced restrictions:**

```yaml
cross_sectional_restrictions:
  
  forbidden_language:
    - pattern: "leads to"
    - pattern: "results in"
    - pattern: "over time"
    - pattern: "increasingly"
    - pattern: "trend"
    
  required_framing:
    - "At this time point..."
    - "In this snapshot..."
    - "Cross-sectional association..."
    
  warning: |
    ⚠️ CROSS-SECTIONAL DATA
    
    Your data is from a single time point. You cannot make temporal claims.
    
    Cannot say:
    - "X leads to Y" (no temporal precedence)
    - "Increasing X results in..." (no trend data)
    - "Over time..." (only one time point)
    
    Can say:
    - "X is associated with Y"
    - "At this time point, accounts with X tend to have Y"
    - "We observe a correlation between X and Y"
```

---

## Implementation

```python
def enforce_design_limits(report_text, study_design):
    """
    Scan report for claims that exceed study design limits.
    
    Args:
        report_text: Draft report text
        study_design: Dict from detect_study_design()
    
    Returns:
        List of violations and suggested revisions
    """
    import re
    
    violations = []
    
    # Design-specific patterns
    patterns_by_design = {
        'single_case_study': [
            (r'\b(brands?|users?|accounts?)\s+should\b', 
             'Prescriptive claim from single case',
             'In this case, [entity] [observed behavior]'),
            (r'this\s+(demonstrates?|proves?|shows?)\s+that',
             'Generalizing from single case',
             'This case illustrates how [entity]...'),
            (r'(we\s+)?recommend',
             'Recommendation from single case',
             'This case suggests [entity] approached X by...'),
        ],
        'cross_sectional': [
            (r'\b(leads?\s+to|results?\s+in)\b',
             'Causal/temporal language with cross-sectional data',
             'is associated with'),
            (r'\b(over\s+time|increasingly|trend)\b',
             'Temporal claim without temporal data',
             'at this time point'),
        ],
        'longitudinal_observational': [
            (r'\bcauses?\b',
             'Causal claim without experimental design',
             'is associated with / precedes'),
            (r'\beffect\s+of\b',
             'Effect language suggests causation',
             'association between / relationship between'),
        ],
    }
    
    design_type = study_design.get('design', 'unknown')
    
    if design_type in patterns_by_design:
        for pattern, problem, suggestion in patterns_by_design[design_type]:
            matches = re.finditer(pattern, report_text, re.IGNORECASE)
            for match in matches:
                # Get surrounding context
                start = max(0, match.start() - 50)
                end = min(len(report_text), match.end() + 50)
                context = report_text[start:end]
                
                violations.append({
                    'match': match.group(),
                    'context': context,
                    'problem': problem,
                    'suggestion': suggestion,
                    'design': design_type
                })
    
    return violations


def design_warning_banner(study_design):
    """
    Generate prominent warning banner for report header.
    """
    
    banners = {
        'single_case_study': """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  SINGLE CASE STUDY                                        ║
║                                                              ║
║  This analysis examines ONE entity.                          ║
║  Findings are specific to this case.                         ║
║  Generalization requires additional research.                ║
╚══════════════════════════════════════════════════════════════╝
""",
        'cross_sectional': """
╔══════════════════════════════════════════════════════════════╗
║  📸 CROSS-SECTIONAL SNAPSHOT                                  ║
║                                                              ║
║  Data from single time point.                                ║
║  Cannot make temporal or causal claims.                      ║
╚══════════════════════════════════════════════════════════════╝
""",
        'longitudinal_observational': """
╔══════════════════════════════════════════════════════════════╗
║  📊 OBSERVATIONAL LONGITUDINAL STUDY                          ║
║                                                              ║
║  Temporal data without manipulation.                         ║
║  Can establish temporal precedence.                          ║
║  Cannot establish causation without ruling out confounds.    ║
╚══════════════════════════════════════════════════════════════╝
"""
    }
    
    design_type = study_design.get('design', 'unknown')
    return banners.get(design_type, "⚠️ Study design: " + design_type)
```

---

## Pre-Analysis Warning

Before any analysis begins:

```yaml
pre_analysis_design_check:
  
  trigger: analysis_start
  
  actions:
    1. detect_study_design
    2. display_design_banner
    3. show_claim_limits
    4. require_acknowledgment
  
  acknowledgment_required: |
    I understand that this {design_type} limits my claims to:
    {claim_limits}
    
    I will not:
    {forbidden_claims}
    
    [ ] I acknowledge these limitations
```

---

## Integration with Tiered Validation

| Tier | Design Enforcement |
|------|-------------------|
| 🟢 Exploratory | Warn but don't block |
| 🟡 Pilot | Require acknowledgment |
| 🔴 Publication | Block claims exceeding evidence |

---

## Reporting Integration

Automatically add to methods section:

```markdown
## Study Design and Limitations

**Design:** {design_type}

**Scope:** This analysis examines {n_units} {unit_type} over {time_period}.

**Generalizability:** {generalizability_statement}

**Claim Limits:** 
- ✓ {allowed_claim_type_1}
- ✓ {allowed_claim_type_2}
- ✗ {forbidden_claim_type_1}
- ✗ {forbidden_claim_type_2}

**Acknowledgment:** The claims in this report have been scoped to match the evidence strength permitted by this study design.
```
