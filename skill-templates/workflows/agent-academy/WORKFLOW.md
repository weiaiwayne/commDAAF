# AgentAcademy: Multi-Model Peer Review Workflow

## Overview

**AgentAcademy** is CommDAAF's incubator for AI-assisted research validation. Multiple AI models with different epistemic perspectives independently analyze the same research, then critique each other—catching what single-model self-review misses.

The academy is also a learning system: errors discovered in cross-review become new probing questions and checks, improving CommDAAF with each run.

## Why This Matters

Single-model review is circular: a model trained on certain data validates reasoning shaped by that same data. Multi-model peer review breaks this loop by introducing genuinely different perspectives.

## Agent Architecture

| Agent | Model | Role | Perspective |
|-------|-------|------|-------------|
| **main** | Opus 4.5 | Primary Analyst | "Is this methodologically sound?" |
| **redteam-glm** | GLM 4.7 | Peer Reviewer 1 | "What assumptions need challenging?" |
| **redteam-kimi** | Kimi K2.5 | Peer Reviewer 2 | "What's missing from the literature?" |

### Epistemic Diversity Rationale

- **Opus 4.5** (Anthropic): Constitutional AI training, cautious reasoning, strong on methodology
- **GLM 4.7** (Zhipu AI): Chinese corpus, different cultural assumptions about social research
- **Kimi K2.5** (Moonshot): Long-context specialist, pattern detection across large bodies of work

## Workflow Stages

### Stage 1: Independent Analysis

Multiple agents receive the same dataset and research brief. Each works independently—no coordination, no peeking.

Output: Independent analysis reports from each agent.

### Stage 2: Cross-Review

Each agent receives the other agents' analyses and critiques them:
- Statistical/methodological errors
- Claims not supported by evidence
- Missing considerations
- Effect size interpretations
- What the other got right (be fair)

Output: Cross-review reports identifying convergent and divergent findings.

### Stage 3: Synthesis

All findings are synthesized:
- **Convergent findings** (all agents agree) → High confidence
- **Divergent findings** (agents disagree) → Investigate further
- **Errors caught** → Become new checks

### Stage 4: Curriculum Update

Lessons learned are documented in `LESSONS_LEARNED.md` and converted into new probing questions and checks in CommDAAF.

## OpenClaw Configuration

Add to `openclaw.json`:

```json
{
  "agents": {
    "list": [
      {
        "id": "redteam-glm",
        "name": "AgentAcademy Analyst (GLM)",
        "model": "zai/glm-4.7",
        "workspace": "/path/to/commdaaf/workspace"
      },
      {
        "id": "redteam-kimi", 
        "name": "AgentAcademy Analyst (Kimi)",
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
  }
}
```

## Invoking the Workflow

### Via Chat Command

```
/academy <paste your analysis here>
```

Or with a file:

```
/academy file:sample-data/my_analysis.csv
```

### Via sessions_spawn (Programmatic)

```javascript
// Spawn analysts in parallel
const [glmAnalysis, kimiAnalysis] = await Promise.all([
  sessions_spawn({
    agentId: "redteam-glm",
    task: `Analyze this dataset: ${input}`,
    label: "academy-glm"
  }),
  sessions_spawn({
    agentId: "redteam-kimi", 
    task: `Analyze this dataset: ${input}`,
    label: "academy-kimi"
  })
]);

// Cross-review
const [glmReview, kimiReview] = await Promise.all([
  sessions_spawn({
    agentId: "redteam-glm",
    task: `Review Kimi's analysis: ${kimiAnalysis}`,
    label: "academy-crossreview-glm"
  }),
  sessions_spawn({
    agentId: "redteam-kimi",
    task: `Review GLM's analysis: ${glmAnalysis}`,
    label: "academy-crossreview-kimi"
  })
]);
```

## Output Format

### Final Report Structure

```markdown
# AgentAcademy Report

## Summary
[One paragraph synthesis]

## Convergent Findings (High Confidence)
1. [Finding]: All agents agree
   - GLM: [Details]
   - Kimi: [Details]

## Divergent Findings (Investigate)
1. [Finding]: Agents disagree
   - GLM says: [X]
   - Kimi says: [Y]
   - **Resolution needed**: [Question]

## Errors Caught
1. [Error]: [Description]
   - Caught by: [Agent]
   - **New check added**: [Check name]

## Lessons for CommDAAF
- [Lesson 1] → Added to [file]
- [Lesson 2] → Added to [file]
```

## Completed Runs

| Run | Dataset | Agents | Key Lessons |
|-----|---------|--------|-------------|
| 1 | @EastLosHighShow | GLM + Kimi | Effect size classification, platform change controls |
| 2 | #EndSARS | GLM + Kimi | Log-transform correlations, bot detection, phase consistency |

See `LESSONS_LEARNED.md` for full documentation.

## Tier Integration

| Tier | Academy Scope |
|------|---------------|
| 🟢 Exploratory | Optional (quick sanity check) |
| 🟡 Pilot | Recommended before scaling |
| 🔴 Publication | Required; iterate until convergence |

## API Costs

Estimated per full run (2 analyses + 2 cross-reviews):

| Stage | Est. Cost |
|-------|-----------|
| Independent analyses | ~$0.50 |
| Cross-reviews | ~$0.30 |
| **Total** | **~$0.80/run** |

## Limitations

1. **Not a replacement for human peer review**: Models don't have domain expertise or access to unpublished work
2. **Training cutoff**: Models may miss very recent literature
3. **Cultural bias**: Western research norms may be overrepresented
4. **Hallucination risk**: Always verify specific citations flagged by models

## Contributing

Found a blind spot? Run your analysis through the academy and submit lessons learned: https://github.com/weiaiwayne/commDAAF
