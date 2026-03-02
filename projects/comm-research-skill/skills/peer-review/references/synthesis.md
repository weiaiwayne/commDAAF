# Review Synthesis Template

After collecting all reviews, synthesize using this structure:

---

## Synthesis Prompt

```
You have received reviews from 5 AI models, each applying a different analytical lens:

[METHODOLOGIST REVIEW - DeepSeek V3.2]
{methodologist_review}

[THEORIST REVIEW - Kimi K2.5]
{theorist_review}

[EMPIRICIST REVIEW - Gemini 3 Flash]
{empiricist_review}

[SKEPTIC REVIEW - Grok 4.1]
{skeptic_review}

[INTEGRATOR REVIEW - Qwen3 VL Thinking]
{integrator_review}

Synthesize these reviews into a unified assessment:

## 1. AREAS OF AGREEMENT
What concerns do multiple reviewers share? These are likely genuine issues.
- List each shared concern
- Note which reviewers flagged it
- Assess severity (critical / major / minor)

## 2. AREAS OF DISAGREEMENT  
Where do reviewers diverge? What might explain the divergence?
- List each point of disagreement
- Explain the different perspectives
- Assess whether disagreement reflects genuine ambiguity

## 3. UNIQUE INSIGHTS
What did only one reviewer catch?
- List single-reviewer concerns
- Assess whether these are valid concerns or noise
- Note which model found it (may indicate model-specific strength)

## 4. OVERALL ASSESSMENT

### Critical Issues (must address before publication)
1. ...

### Major Issues (should address)
1. ...

### Minor Issues (consider addressing)
1. ...

### Strengths to Preserve
1. ...

## 5. CONFIDENCE CALIBRATION

Overall confidence in this assessment: [0-100]%

Factors increasing confidence:
- ...

Factors decreasing confidence:
- ...

Perspectives still missing:
- [e.g., domain expert, end-user, ethics reviewer]
```

---

## Interpreting Results

### High-Signal Findings

| Signal | Interpretation |
|--------|----------------|
| Multi-model agreement | Likely genuine issue |
| Specific citations | More credible than vague |
| Matches methodology standards | Credible concern |
| Skeptic + other agrees | Probably real problem |

### Low-Signal Findings

| Signal | Interpretation |
|--------|----------------|
| Single model, others silent | May be noise OR unique insight |
| Vague/generic critique | Often model hedging |
| Contradictory assessments | Genuine ambiguity |
| Skeptic-only concern | Check if overly adversarial |

### What Multi-Model Review Cannot Catch

- Errors in domain knowledge none of the models have
- Normative/political implications models avoid
- What the field actually cares about (trends, politics)
- Novel contributions (models trained on past)
- Ethical concerns requiring human judgment
- Very recent developments (after training cutoff)

---

## Confidence Calibration Guide

| Confidence | When to Use |
|------------|-------------|
| 80-100% | Strong multi-model agreement, specific issues, clear citations |
| 60-80% | Majority agreement, some specificity, minor divergence |
| 40-60% | Mixed signals, some disagreement, moderate specificity |
| 20-40% | Significant disagreement, vague concerns, uncertain |
| 0-20% | Strong disagreement, document outside model expertise |

---

## Output Checklist

Before delivering synthesis, verify:

- [ ] All four reviews incorporated
- [ ] Agreement vs disagreement clearly distinguished
- [ ] Specific citations preserved from reviews
- [ ] Severity levels assigned (critical/major/minor)
- [ ] Confidence calibrated with justification
- [ ] Missing perspectives acknowledged
- [ ] Actionable recommendations provided
