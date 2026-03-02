# Claim-Evidence Matcher

**Purpose:** Prevent overclaiming by matching claim strength to evidence type.

---

## The Problem

Research often makes claims that exceed the evidence:

| Evidence Type | Common Overclaim |
|---------------|------------------|
| Correlation | "X causes Y" |
| Single case | "Entertainment brands should..." |
| Cross-sectional | "X leads to Y over time" |
| Observational | "The effect of X on Y" |

CommDAAF enforces alignment between claim language and evidence strength.

---

## Claim Taxonomy

### Level 1: Descriptive Claims

**What you can say:** "We observed X"

**Evidence required:** Data showing X

**Language:**
- ✓ "We found that..."
- ✓ "The data show..."
- ✓ "In this sample..."
- ✗ "This demonstrates that..."
- ✗ "This proves..."

### Level 2: Associational Claims

**What you can say:** "X is associated with Y"

**Evidence required:** Correlation/co-occurrence analysis

**Language:**
- ✓ "X is associated with Y"
- ✓ "X and Y are correlated"
- ✓ "X tends to co-occur with Y"
- ✗ "X affects Y"
- ✗ "X drives Y"
- ✗ "X influences Y"

### Level 3: Conditional Claims

**What you can say:** "When X, then Y (in this context)"

**Evidence required:** Association + temporal precedence OR controlled comparison

**Language:**
- ✓ "Posts with X tend to receive more Y"
- ✓ "In this dataset, X precedes Y"
- ✓ "Conditional on X, Y is more likely"
- ✗ "X causes Y"
- ✗ "X results in Y"

### Level 4: Causal Claims

**What you can say:** "X causes Y"

**Evidence required:** Experimental manipulation OR quasi-experiment with strong design OR natural experiment

**Language:**
- ✓ "X causes Y" (only with experimental evidence)
- ✓ "We find causal evidence that X affects Y"

**NOT sufficient:**
- Correlation (even strong)
- Temporal precedence alone
- Theory suggesting causation
- "It makes sense that X causes Y"

### Level 5: Generalizable Claims

**What you can say:** "This applies to population P"

**Evidence required:** Representative sample OR replication across contexts

**Language:**
- ✓ "Entertainment brands [in this study] use positive sentiment"
- ✗ "Entertainment brands should maintain positive sentiment" (from N=1)

---

## Claim Checker Implementation

```python
def check_claim_evidence_alignment(claim_text, evidence_type):
    """
    Check if claim language matches evidence strength.
    
    Args:
        claim_text: The claim being made
        evidence_type: One of ['descriptive', 'correlational', 'quasi-experimental', 'experimental']
    
    Returns:
        Assessment of claim appropriateness
    """
    
    # Causal language patterns
    causal_patterns = [
        r'\b(causes?|caused|causing)\b',
        r'\b(affects?|affected|affecting)\b',
        r'\b(influences?|influenced|influencing)\b',
        r'\b(drives?|drove|driving)\b',
        r'\b(leads?\s+to|led\s+to)\b',
        r'\b(results?\s+in|resulted\s+in)\b',
        r'\b(produces?|produced|producing)\b',
        r'\b(determines?|determined)\b',
        r'\beffect\s+of\b',
        r'\bimpact\s+of\b',
    ]
    
    # Prescriptive language patterns
    prescriptive_patterns = [
        r'\bshould\b',
        r'\bmust\b',
        r'\bneed\s+to\b',
        r'\bought\s+to\b',
        r'\brecommend\b',
        r'\badvise\b',
        r'\bbest\s+practice\b',
    ]
    
    # Generalizing language patterns
    generalizing_patterns = [
        r'\ball\s+\w+\s+(should|do|are)\b',
        r'\b(brands|users|people|accounts)\s+(should|always|never)\b',
        r'\bin\s+general\b',
        r'\btypically\b',
        r'\busually\b',
    ]
    
    import re
    
    issues = []
    
    # Check for causal language with non-causal evidence
    if evidence_type in ['descriptive', 'correlational']:
        for pattern in causal_patterns:
            if re.search(pattern, claim_text, re.IGNORECASE):
                issues.append({
                    'type': 'causal_overclaim',
                    'pattern': pattern,
                    'problem': 'Causal language used with correlational/descriptive evidence',
                    'suggestion': 'Replace with associational language: "is associated with", "correlates with", "tends to co-occur"'
                })
    
    # Check for prescriptive claims
    for pattern in prescriptive_patterns:
        if re.search(pattern, claim_text, re.IGNORECASE):
            issues.append({
                'type': 'prescriptive_claim',
                'pattern': pattern,
                'problem': 'Prescriptive claim requires causal evidence + generalizability',
                'suggestion': 'Describe what was observed, not what should be done'
            })
    
    # Check for generalizing from limited evidence
    for pattern in generalizing_patterns:
        if re.search(pattern, claim_text, re.IGNORECASE):
            issues.append({
                'type': 'overgeneralization',
                'pattern': pattern,
                'problem': 'Generalizing language may exceed evidence scope',
                'suggestion': 'Scope to your sample: "In this study...", "Among accounts in our sample..."'
            })
    
    return {
        'claim': claim_text,
        'evidence_type': evidence_type,
        'issues': issues,
        'acceptable': len(issues) == 0,
        'revision_needed': len(issues) > 0
    }


def suggest_claim_revision(claim_text, evidence_type):
    """
    Suggest revised claim language appropriate for evidence.
    """
    
    revisions = {
        'correlational': {
            'causes': 'is associated with',
            'affects': 'correlates with',
            'influences': 'co-occurs with',
            'drives': 'is related to',
            'leads to': 'is associated with',
            'results in': 'tends to co-occur with',
            'effect of': 'association between',
            'impact of': 'relationship between',
        },
        'descriptive': {
            'should': 'in this case,',
            'always': 'in this sample,',
            'never': 'in this dataset,',
        }
    }
    
    revised = claim_text
    
    if evidence_type in revisions:
        for original, replacement in revisions[evidence_type].items():
            import re
            revised = re.sub(
                rf'\b{original}\b',
                replacement,
                revised,
                flags=re.IGNORECASE
            )
    
    return revised
```

---

## Study Design → Claim Limits

```yaml
study_design_limits:
  
  single_case_study:
    description: "One account/brand/event analyzed"
    allowed_claims:
      - "This account shows pattern X"
      - "In this case, we observed Y"
    forbidden_claims:
      - "Brands should do X"
      - "This demonstrates that Y causes Z"
    generalizability: "None - case-specific only"
  
  cross_sectional_survey:
    description: "Snapshot of multiple units at one time"
    allowed_claims:
      - "X is associated with Y"
      - "Units with X tend to have higher Y"
    forbidden_claims:
      - "X leads to Y over time"
      - "Increasing X will increase Y"
    generalizability: "To similar populations, not over time"
  
  longitudinal_observational:
    description: "Multiple time points, no manipulation"
    allowed_claims:
      - "X precedes Y temporally"
      - "Changes in X are associated with subsequent changes in Y"
    forbidden_claims:
      - "X causes Y" (without ruling out confounds)
    generalizability: "Temporal, within similar contexts"
  
  natural_experiment:
    description: "External shock creates comparison groups"
    allowed_claims:
      - "The [shock] was associated with changes in Y"
      - "Stronger causal language if design is robust"
    requirements:
      - "Clear treatment/control distinction"
      - "Parallel trends pre-treatment"
      - "No selection into treatment"
    generalizability: "To similar shocks"
  
  randomized_experiment:
    description: "Random assignment to conditions"
    allowed_claims:
      - "X causes Y"
      - "The effect of X on Y is Z"
    generalizability: "To populations similar to sample"
```

---

## Pre-Publication Claim Audit

Before any claims leave CommDAAF:

```yaml
claim_audit:
  trigger: generate_report
  
  steps:
    1. extract_all_claims:
        - scan conclusions section
        - scan implications section
        - scan abstract
    
    2. classify_each_claim:
        - descriptive
        - associational
        - causal
        - prescriptive
        - generalizing
    
    3. match_to_evidence:
        - what evidence supports this?
        - what study design was used?
        - is claim language appropriate?
    
    4. flag_mismatches:
        - causal language + correlational evidence
        - prescriptive claims + observational data
        - generalizations + single case
    
    5. require_revision:
        - provide suggested revisions
        - block export until resolved
```

---

## Example Transformations

### Before (Overclaimed)

> "This study demonstrates that entertainment brands should maintain positive sentiment, as positive content drives higher engagement."

### After (Appropriate)

> "In this case study of one entertainment brand's Twitter account (2014-2018), we observed predominantly positive sentiment (44.8% positive, 6.7% negative). However, sentiment polarity showed negligible correlation with engagement metrics (r = -0.01 for retweets). These descriptive findings suggest that for this account, sentiment valence alone did not predict engagement, though other factors not captured in our data may mediate this relationship."

### Key Changes

| Original | Revised | Reason |
|----------|---------|--------|
| "demonstrates" | "we observed" | Descriptive, not demonstrative |
| "brands should" | "for this account" | Scoped to sample |
| "drives" | "showed negligible correlation" | Correlational language |
| Implied causation | "other factors may mediate" | Acknowledges limitations |

---

## Integration

Add to reporting workflow:

```python
def audit_claims_before_export(report_text, study_design):
    """
    Scan report for claim-evidence mismatches before export.
    """
    # Extract potential claims (sentences with claim keywords)
    import re
    
    claim_patterns = [
        r'[^.]*\b(shows?|demonstrates?|proves?|indicates?)\b[^.]*\.',
        r'[^.]*\b(should|must|recommends?)\b[^.]*\.',
        r'[^.]*\b(causes?|affects?|influences?|drives?)\b[^.]*\.',
        r'[^.]*\b(all|always|never|typically)\b[^.]*\.',
    ]
    
    potential_claims = []
    for pattern in claim_patterns:
        matches = re.findall(pattern, report_text, re.IGNORECASE)
        potential_claims.extend(matches)
    
    # Check each claim
    issues = []
    for claim in potential_claims:
        result = check_claim_evidence_alignment(claim, study_design)
        if not result['acceptable']:
            issues.append(result)
    
    if issues:
        print("⚠️ CLAIM-EVIDENCE MISMATCHES DETECTED")
        print("=" * 50)
        for issue in issues:
            print(f"\nClaim: {issue['claim'][:100]}...")
            for problem in issue['issues']:
                print(f"  Problem: {problem['problem']}")
                print(f"  Suggestion: {problem['suggestion']}")
        
        return False, issues
    
    return True, []
```
