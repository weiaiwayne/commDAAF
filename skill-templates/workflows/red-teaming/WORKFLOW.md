# CommDAAF Multi-Model Red-Teaming Workflow

## Overview

Adversarial validation of computational communication research using epistemically diverse AI models. Three models with different training backgrounds critique the same analysis—catching what single-model self-review misses.

## Why This Matters

Single-model review is circular: a model trained on certain data validates reasoning shaped by that same data. Multi-model red-teaming breaks this loop by introducing genuinely different perspectives.

## Agent Architecture

| Agent | Model | Role | Perspective |
|-------|-------|------|-------------|
| **main** | Opus 4.5 | Primary Analyst | "Is this methodologically sound?" |
| **mei** | GLM 4.7 | Red-Teamer 1 | "What assumptions need challenging?" |
| **priya** | Kimi K2.5 | Red-Teamer 2 | "What's missing from the literature?" |

### Epistemic Diversity Rationale

- **Opus 4.5** (Anthropic): Constitutional AI training, cautious reasoning, strong on methodology
- **GLM 4.7** (Zhipu AI): Chinese corpus, different cultural assumptions about social research
- **Kimi K2.5** (Moonshot): Long-context specialist, pattern detection across large bodies of work

## Workflow Stages

### Stage 1: Primary Analysis (Opus 4.5)

The primary analyst reviews research output for:
- Methodological soundness
- Internal validity threats
- Statistical concerns
- Clarity of reasoning

Output: Structured assessment with flagged concerns.

### Stage 2: Adversarial Review (GLM 4.7 + Kimi K2.5)

Both red-teamers receive:
- Original research input
- Primary analyst's assessment

Each independently critiques:
- **GLM**: Challenge assumptions, find blind spots, attack statistical reasoning
- **Kimi**: Check literature coverage, identify edge cases, probe replication concerns

Output: Independent critique reports.

### Stage 3: Synthesis (Opus 4.5)

The primary analyst integrates all feedback:
- **Consensus issues** (all three flagged) → High confidence problems
- **Disagreements** (one model flagged) → Needs researcher judgment
- **Actionable report** with prioritized concerns

## OpenClaw Configuration

Add to `openclaw.json`:

```json
{
  "agents": {
    "list": [
      {
        "id": "redteam-glm",
        "name": "GLM Red-Teamer",
        "model": "zai/glm-4.7",
        "workspace": "/path/to/commdaaf/workspace"
      },
      {
        "id": "redteam-kimi", 
        "name": "Kimi Red-Teamer",
        "model": "kimi-coding/k2p5",
        "workspace": "/path/to/commdaaf/workspace"
      }
    ]
  },
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["main", "redteam-glm", "redteam-kimi"]
    }
  },
  "auth": {
    "profiles": {
      "zai:default": {
        "provider": "zai",
        "mode": "token"
      },
      "kimi-coding:default": {
        "provider": "kimi-coding",
        "mode": "token"
      }
    }
  }
}
```

Add tokens to `~/.openclaw/agents/main/agent/auth-profiles.json`:

```json
{
  "zai:default": {
    "type": "token",
    "provider": "zai",
    "token": "<your-z.ai-api-key>"
  },
  "kimi-coding:default": {
    "type": "token",
    "provider": "kimi-coding",
    "token": "<your-kimi-api-key>"
  }
}
```

## Invoking the Workflow

### Via Chat Command

```
/redteam <paste your analysis here>
```

### Via sessions_spawn (Programmatic)

```javascript
// Stage 1: Primary Analysis
const primaryAssessment = await runPrimaryAnalysis(input);

// Stage 2: Spawn red-teamers in parallel
const [glmCritique, kimiCritique] = await Promise.all([
  sessions_spawn({
    agentId: "redteam-glm",
    task: `${input}\n\n---\nPrimary Assessment:\n${primaryAssessment}`,
    cleanup: "delete"
  }),
  sessions_spawn({
    agentId: "redteam-kimi", 
    task: `${input}\n\n---\nPrimary Assessment:\n${primaryAssessment}`,
    cleanup: "delete"
  })
]);

// Stage 3: Synthesis
const finalReport = await synthesize(primaryAssessment, glmCritique, kimiCritique);
```

## Output Format

### Final Report Structure

```markdown
# Red-Team Analysis Report

## Summary
[One paragraph synthesis]

## High-Confidence Issues (All Models Agree)
1. [Issue]: [Description]
   - Primary: [Finding]
   - GLM: [Finding]
   - Kimi: [Finding]
   - **Recommendation**: [Action]

## Flagged Concerns (Single Model)
1. [Issue]: [Description]
   - Flagged by: [Model]
   - **Researcher Decision Needed**: [Question to consider]

## Strengths Identified
- [Strength 1]
- [Strength 2]

## Model Disagreements
| Topic | Opus 4.5 | GLM 4.7 | Kimi K2.5 |
|-------|----------|---------|-----------|
| [Topic] | [View] | [View] | [View] |
```

## Tier Integration

This workflow integrates with CommDAAF's tiered validation:

| Tier | Red-Team Scope |
|------|----------------|
| 🟢 Exploratory | Skip (too early) |
| 🟡 Pilot | Run once before scaling |
| 🔴 Publication | Required; iterate until consensus |

## API Costs

Estimated per run (varies by input length):

| Model | Input | Output | Est. Cost |
|-------|-------|--------|-----------|
| Opus 4.5 | ~8K tokens | ~2K tokens | ~$0.25 |
| GLM 4.7 | ~8K tokens | ~1K tokens | ~$0.03 |
| Kimi K2.5 | ~8K tokens | ~1K tokens | ~$0.02 |
| **Total** | | | **~$0.30/run** |

## Limitations

1. **Not a replacement for peer review**: Models don't have domain expertise or access to unpublished work
2. **Training cutoff**: Models may miss very recent literature
3. **Cultural bias**: Western research norms may be overrepresented
4. **Hallucination risk**: Always verify specific citations flagged by models

## Contributing

Found a blind spot? Open an issue at: https://github.com/weiaiwayne/commDAAF
