# Model Disagreement Analysis: Wikipedia Epistemic Injustice Study

## Summary

Three models (Claude, GLM-4.7, Kimi K2.5) coded 176 new excerpts for epistemic injustice. Despite high raw agreement (78-96%), Fleiss' κ was low (−0.01 to 0.36) due to base rate issues and **systematic interpretation differences**.

## Root Causes of Disagreement

### 1. THRESHOLD DIFFERENCES

| Model | Over-codes | Trigger Pattern |
|-------|-----------|-----------------|
| **Claude** | `epistemic_dispossession` (27 solo) | EC-protection template present |
| **Kimi** | `policy_weaponization` (22 solo) | `{{not done}}` response present |
| **GLM** | `source_hierarchy` (26 solo) | "reliable source" mentioned |

### 2. CONTEXT SENSITIVITY FAILURES

**Claude** treats structural barriers (EC protection) as dispossession even when:
- No editor is actively excluded in the discussion
- The template is just metadata
- The interaction is routine/constructive

**Kimi** treats policy citations as weaponization even when:
- The denial is procedurally correct
- No strategic/adversarial use is evident
- The editor is helped with guidance

**GLM** treats source mentions as hierarchy disputes even when:
- It's a standard RS reminder
- No specific source is challenged
- No national/ideological hierarchy is argued

### 3. ILLUSTRATIVE CASES

#### Case: iran_113 (Twelve-Day War naming)

> "WHY ON EARTH is this called 'Twelve-Day War'? ...whoever came up with that and unilaterally plastered it on Wikipedia should be banned..."

| Construct | Claude | GLM | Kimi | Ground Truth? |
|-----------|--------|-----|------|---------------|
| testimonial_injustice | **1** | 0 | 0 | 1 (dismissive of editor who chose name) |
| naming_dispute | **1** | 0 | **1** | 1 (explicit naming contestation) |
| source_hierarchy | 0 | **1** | 0 | 0 (RS cited as defense, not disputed) |

**Analysis**: Claude catches the testimonial injustice ("should be banned") that others miss. GLM misreads the RS citation as a hierarchy dispute when it's actually defending the current name.

#### Case: iran_087 (UN genocide finding)

> "Not an accurate statement... this discussion format is not available to non-EC editors"

| Construct | Claude | GLM | Kimi | Ground Truth? |
|-----------|--------|-----|------|---------------|
| testimonial_injustice | **1** | 0 | 0 | 1 (dismissed for not being EC) |
| epistemic_dispossession | **1** | 0 | **1** | 1 (explicit exclusion) |
| policy_weaponization | 0 | 0 | **1** | 0-1 (borderline) |
| source_hierarchy | 0 | **1** | 0 | 0-1 (borderline) |

**Analysis**: Clear case of epistemic dispossession that Claude and Kimi both catch. GLM focuses on the UN source question instead. Kimi sees policy weaponization in the closure.

## Methodological Implications

### 1. Codebook Needs Counter-Indicators

Current: "Code 1 if at least one clear instance"

**Proposed additions:**
- `epistemic_dispossession`: NOT if template-only with no active gate-keeping
- `policy_weaponization`: NOT if routine process with constructive guidance  
- `source_hierarchy`: NOT if standard RS reminder without specific hierarchy claims

### 2. Model Strengths Differ

| Model | Strength | Weakness |
|-------|----------|----------|
| Claude | Catches subtle dismissals (testimonial) | Over-triggers on structural templates |
| Kimi | Good at weaponization pattern | Over-applies to routine denials |
| GLM | Sensitive to source discussions | Conflates RS reminders with hierarchy |

### 3. Agreement ≠ Validity

High agreement (96% on testimonial_injustice) can mask:
- All models missing the same cases (false negatives)
- Agreement on easy zeros (base rate artifact)
- Systematic shared blind spots

### 4. Inter-Model Disagreement as Signal

When models disagree, often **multiple constructs apply**:
- iran_087: Both dispossession AND testimonial injustice
- iran_113: Both naming dispute AND testimonial injustice
- Disagreement may indicate **construct overlap** rather than error

## Recommendations

1. **Revise codebook** with clearer decision rules and counter-indicators
2. **Human adjudicate** the 16 high-disagreement cases
3. **Accept multi-coding** when constructs genuinely overlap
4. **Report model-specific findings** alongside aggregate (methodological contribution)

## Files

- `new_batch_merged.json`: All 176 excerpts with 3-model codings
- `expanded_agreement_results.json`: Agreement statistics
- `disagreement_analysis.md`: This analysis
