---
name: peer-review
description: Peer review documents using multiple LLM models via OpenRouter for epistemically diverse feedback. Use when reviewing research papers, methodologies, proposals, or any document that benefits from multiple critical perspectives. Triggers on requests for "peer review", "critique my paper", "review methodology", "get feedback from different models", or "multi-model analysis".
---

# Peer Review

Spawn parallel review agents powered by different foundation models to surface diverse critiques.

## Why Multi-Model?

| Approach | Limitation |
|----------|------------|
| Single model | Same blind spots |
| Single model + personas | Simulated diversity |
| **Multiple models** | Genuine diversity (different training = different biases) |

## Quick Start

1. **Ensure OpenRouter configured** — Key at `~/.openclaw/secrets/openrouter.key`
2. **Pick diverse models** from user's available list
3. **Run parallel reviews** using `sessions_spawn` with different models
4. **Synthesize** results into unified assessment

## Default 5-Agent Configuration

| Role | Model | Rationale |
|------|-------|-----------|
| **Methodologist** | `deepseek/deepseek-v3.2` | Strong reasoning, cost-effective |
| **Theorist** | `moonshotai/kimi-k2.5` | Long context, broad knowledge |
| **Empiricist** | `google/gemini-3-flash-preview` | Fast, good with data/facts |
| **Skeptic** | `x-ai/grok-4.1-fast` | Less filtered, adversarial |
| **Integrator** | `qwen/qwen3-vl-8b-thinking` | Reasoning mode, synthesis |

## Review Perspectives

See `references/prompts.md` for full prompts:

| Role | Focus |
|------|-------|
| **Methodologist** | Research design, validity, sampling, analysis |
| **Theorist** | Concepts, literature, argument structure, contribution |
| **Empiricist** | Data quality, statistics, replication, effect sizes |
| **Skeptic** | Assumptions, alternatives, objections, falsification |
| **Integrator** | Cross-perspective synthesis, gaps, overall coherence |

## Execution Pattern

```
For each of 5 reviewer perspectives:
  1. Load document into context
  2. Apply role-specific prompt from references/prompts.md
  3. Spawn sub-agent: sessions_spawn(task, model="openrouter/<model>")
  4. Collect structured critique

After all reviews complete:
  5. Synthesize using references/synthesis.md template
  6. Identify agreement (likely real issues) vs disagreement (ambiguous)
  7. Produce final assessment with confidence calibration
```

## Model Selection Principles

**Maximize diversity across:**
- Provider origin (US, China, Europe)
- Training approach (RLHF, constitutional, open)
- Size/speed tradeoffs
- Specialization (reasoning, long-context, multimodal)

## Output Format

Each review produces:
```markdown
## [PERSPECTIVE] Review

### Summary
[2-3 sentence overall assessment]

### Major Issues
1. [Issue with section/page citation]
2. ...

### Minor Issues
1. ...

### Strengths
1. ...

### Confidence: [0-100]%
[Brief justification]
```

Final synthesis follows `references/synthesis.md` template.

## Cost Estimation

Typical 5-model review of ~20K token document:
- Input: ~100K tokens total (~$0.05-0.10)
- Output: ~25K tokens total (~$0.05-0.15)
- **Total: ~$0.10-0.25 per review**

## Files

- `references/prompts.md` — Full review prompts by perspective
- `references/synthesis.md` — Synthesis template
- `scripts/review_runner.sh` — Reference CLI template
