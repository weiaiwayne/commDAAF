# Kimi Coding Task: Wikipedia Epistemic Injustice

Code Wikipedia talk page excerpts for epistemic injustice. Process batches 1-8 in sequence.

## Constructs (code 1=present, 0=absent)

1. **testimonial_injustice**: Credibility discounted based on identity/experience, not argument
2. **hermeneutical_injustice**: Disputes over terminology/categories preventing expression
3. **epistemic_dispossession**: Platform structures favoring established editors
4. **policy_weaponization**: Using WP policies strategically to delegitimize viewpoints
5. **naming_dispute**: Contestation over article titles/event names
6. **source_hierarchy**: Establishing reliability hierarchies along national/ideological lines

## Instructions

For each batch file (new_batch_1.json through new_batch_8.json):
1. Read the batch
2. Code each excerpt
3. Save results to kimi_new_batch_N.json

## Output Format (JSON array)

```json
[
  {
    "id": "iran_051",
    "testimonial_injustice": 0,
    "hermeneutical_injustice": 0,
    "epistemic_dispossession": 0,
    "policy_weaponization": 0,
    "naming_dispute": 0,
    "source_hierarchy": 0,
    "primary_form": "none",
    "confidence": 0.8,
    "reasoning": "Brief explanation"
  }
]
```

## Decision Rules
- Code 1 if at least one clear instance
- If uncertain, code 0 (conservative)
- primary_form = most prominent construct, or "none"

Work directory: /root/.openclaw/workspace/projects/comm-research-skill/projects/wikipedia-iran-study/coding/
