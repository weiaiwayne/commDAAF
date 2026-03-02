# LLM Annotation

## Probing Questions (ALL REQUIRED)

```
Q1: What are your categories?
    ✓ Exhaustive (covers all cases)
    ✓ Mutually exclusive (no overlap)
    ✓ Clearly defined with examples
    ✗ "Whatever the model finds" — YOU DEFINE CATEGORIES

Q2: Human validation plan?
    ✓ Minimum N ≥ 200
    ✓ Calculate inter-rater agreement (κ ≥ 0.7)
    ✓ Human vs LLM comparison
    ✗ "The model is validated" — NOT ON YOUR DATA

Q3: Prompt design?
    ✓ Clear definitions
    ✓ Examples for each category
    ✓ Edge case handling
    ✗ "Just ask it to classify" — INSUFFICIENT

Q4: Multi-model check?
    ✓ Run 2+ models
    ✓ Flag disagreement as uncertainty
    ✗ "One model is enough" — EPISTEMIC DIVERSITY MATTERS
```

## Validation Requirements

| Check | Minimum Threshold | Action if Failed |
|-------|-------------------|------------------|
| Human-LLM agreement | κ ≥ 0.7 | Revise prompt, retrain |
| Multi-model agreement | 80%+ | Flag disagreement |
| Edge case accuracy | Manual review | Add examples to prompt |

## Prompt Template

```
You are classifying [CONTENT TYPE] into the following categories:

1. **[CATEGORY A]**: [Definition]. Example: "[example]"
2. **[CATEGORY B]**: [Definition]. Example: "[example]"
3. **[CATEGORY C]**: [Definition]. Example: "[example]"

If unclear, classify as [DEFAULT/UNCLEAR].

Content to classify:
[CONTENT]

Respond with only the category name.
```

## Multi-Model Strategy

| Task | Model | Why |
|------|-------|-----|
| **Bulk annotation** | Gemini Flash / GPT-4o-mini | Cost |
| **Validation sample** | Claude Opus / GPT-4 | Quality |
| **Disagreement review** | Different model family | Independence |

**Key insight**: Model disagreement = uncertainty signal, not failure.

## Critical Checks

- [ ] Categories exhaustive and mutually exclusive
- [ ] Human validation planned (N≥200)
- [ ] Inter-rater reliability calculated
- [ ] Multi-model comparison done
- [ ] Prompt includes definitions + examples
