# Multi-Model Construct Validation

*Added from Wikipedia Epistemic Authority study (March 2026)*

## Overview

Use culturally diverse LLMs as independent coders to test whether constructs are **cross-culturally robust** or **culturally contested**. High agreement across models trained in different cultural contexts suggests a construct captures something recognizable beyond any single cultural framework.

## When to Use

- Testing whether academic constructs translate across cultures
- Validating codebooks before human coding
- Identifying ambiguous operational definitions
- Distinguishing universal patterns from culturally-specific ones

## The Logic

Traditional inter-coder reliability (human coders) validates **consistency** but not **cross-cultural robustness**. Two American grad students agreeing doesn't mean the construct works in China.

Using LLMs trained in different cultural contexts (e.g., Claude/US, GLM/China, Kimi/China) adds a dimension:
- **High agreement** → Construct is cross-culturally recognizable
- **Low agreement** → Construct is culturally contested OR poorly operationalized
- **Systematic disagreement** → Models interpret construct oppositely (investigate!)

## Recommended Model Ensemble

| Model | Origin | Perspective |
|-------|--------|-------------|
| Claude | US/Anthropic | Western, safety-focused |
| GPT-4 | US/OpenAI | Western, general |
| GLM-4 | China/Zhipu | Chinese tech ecosystem |
| Kimi | China/Moonshot | Chinese, consumer-focused |
| Gemini | US/Google | Western, multimodal |

**Minimum**: 3 models with at least 1 non-Western

## Interpreting Agreement (Fleiss' κ)

| κ Range | Interpretation | Action |
|---------|----------------|--------|
| **>0.60** | Strong cross-cultural validity | Use construct confidently |
| **0.40-0.60** | Moderate validity | Use with acknowledgment |
| **0.20-0.40** | Weak/partial | Revise operationalization |
| **<0.20** | Culturally contested | Report as exploratory finding |
| **Negative** | Systematic disagreement | Investigate divergence |

## Probing Questions

Before running multi-model validation:

1. **What constructs are you testing?** (list each with operational definition)
2. **What cultural assumptions might be embedded?** (e.g., Western emotion categories)
3. **Which models will you use?** (ensure cultural diversity)
4. **What's your threshold for "validated"?** (recommend κ>0.40)
5. **How will you report low-agreement constructs?** (not as failures, but as findings)

## Key Insight: Disagreement as Finding

**Don't treat low κ as failure.** When Western and Chinese models interpret a construct differently, that's substantive information about cultural specificity.

Example from Wikipedia study:
- "Source hierarchy" (κ=0.47): Cross-culturally recognized
- "Hermeneutical injustice" (κ=0.18): Western construct, not universal

The low κ for hermeneutical injustice revealed that the concept embeds Western assumptions about linguistic adequacy—a finding, not an error.

## Protocol

1. **Prepare excerpts**: Sample content for coding (N≥100 recommended)
2. **Write codebook**: Clear definitions, examples, counter-examples for each construct
3. **Code independently**: Each model codes all excerpts without seeing others' results
4. **Calculate κ**: Fleiss' kappa for 3+ models, Cohen's for pairwise
5. **Interpret**: High κ = validated; Low κ = investigate
6. **Report honestly**: Include ALL κ values, not just high ones

## Pitfalls

- ❌ Using only Western models and claiming "validation"
- ❌ Dropping low-κ constructs without reporting them
- ❌ Treating model disagreement as "noise" rather than signal
- ❌ Small sample sizes (need N≥100 for stable κ)
- ❌ Assuming high κ means "true" (agreement ≠ validity)

## Example Reporting

> "We validated constructs using three LLMs trained in different cultural contexts (Claude/US, GLM/China, Kimi/China). Source hierarchy debates achieved acceptable reliability (κ=0.47), indicating cross-cultural recognizability. Hermeneutical injustice showed low agreement (κ=0.18), suggesting the construct may embed Western-specific assumptions about linguistic adequacy. We report findings for both validated and contested constructs."

## References

- Wikipedia Epistemic Authority study (AgentAcademy, 2026)
- Fricker, M. (2007). Epistemic Injustice. Oxford.
- Fleiss, J.L. (1971). Measuring nominal scale agreement among many raters. Psychological Bulletin.
