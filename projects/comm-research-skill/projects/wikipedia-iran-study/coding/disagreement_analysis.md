# Model Disagreement Analysis

## Summary

| Model  | Tendency | Root Cause |
|--------|----------|------------|
| Claude | Over-codes epistemic_dispossession | Triggers on EC-protection templates, even without active exclusion |
| Kimi   | Over-codes policy_weaponization | Triggers on {{not done}} responses, treating routine denials as weaponization |
| GLM    | Over-codes source_hierarchy | Triggers on "reliable source" mentions, even in routine requests |

INTERPRETATION DIFFERENCES:

1. THRESHOLD PROBLEM
   - Claude: LOW threshold for epistemic_dispossession (template = dispossession)
   - Kimi: LOW threshold for policy_weaponization (denial = weaponization)
   - GLM: LOW threshold for source_hierarchy (mention = hierarchy)

2. CONTEXT SENSITIVITY
   - Claude distinguishes active exclusion from passive protection: WEAK
   - Kimi distinguishes weaponization from routine process: WEAK
   - GLM distinguishes hierarchy disputes from RS reminders: WEAK

3. CODEBOOK INTERPRETATION
   - Codebook says "code 1 if at least one clear instance"
   - Models interpret "clear instance" differently
   - Need clearer decision rules for edge cases

RECOMMENDATION:
   Add "counter-indicators" to codebook:
   - epistemic_dispossession: NOT if just template, need active gate-keeping
   - policy_weaponization: NOT if routine process, need strategic use
   - source_hierarchy: NOT if just RS reminder, need hierarchy claims
