# AgentAcademy: Multi-Model Peer Review Workflow

> **v0.7.0 Update**: Added mandatory cross-agent validation, credibility rating scheme, and structured knowledge base — inspired by Xu & Yang (2026), "Scaling Reproducibility."

## Overview

**AgentAcademy** is CommDAAF's incubator for AI-assisted research validation. Multiple AI models with different epistemic perspectives independently analyze the same research, then critique each other—catching what single-model self-review misses.

The academy is also a learning system: errors discovered in cross-review become new probing questions and checks, improving CommDAAF with each run.

## Why This Matters

Single-model review is circular: a model trained on certain data validates reasoning shaped by that same data. Multi-model peer review breaks this loop by introducing genuinely different perspectives.

## Architecture

See `ARCHITECTURE.md` for the full three-layer design (LLM Orchestrator → Knowledge Base → Deterministic Computation).

**Key principle from Xu & Yang (2026):**
> "The system separates scientific reasoning from computational execution."

In CommDAAF: Humans design research frameworks; AI executes computation; neither crosses into the other's domain.

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

---

## Workflow Stages

### Stage 1: Independent Analysis

Multiple agents receive the same dataset and research brief. Each works independently—no coordination, no peeking.

**Output:** Independent analysis reports from each agent, including:
- Key statistics (exported to JSON)
- Methodology description
- Findings and interpretations

### Stage 2: Cross-Agent Validation ⚠️ MANDATORY

> **New in v0.7.0** — Adapted from Xu & Yang (2026)

Before cross-review, agents must **validate each other's numbers**.

```yaml
cross_validation:
  required: true  # NOT optional
  
  protocol:
    1. Agent A exports key_stats.json
    2. Agent B independently re-computes on same data
    3. System compares results
    4. Flag divergence > threshold
    5. STOP if validation fails
    
  thresholds:
    coefficient_tolerance: 0.01   # 1% relative difference
    correlation_tolerance: 0.05   # 0.05 absolute difference  
    count_tolerance: 0            # Must match exactly
    
  on_divergence:
    - Log discrepancy details
    - Trace computation path (data loading, filtering, formula)
    - Identify root cause
    - Do NOT proceed until resolved
```

**Why this matters:** In the EndSARS analysis, raw correlation was r=0.412 but log-transformed was r=0.251 — a 40% difference. Without cross-validation, we would have reported only one.

### Stage 3: Cross-Review

Each agent receives the other agents' analyses and critiques them:
- Statistical/methodological errors
- Claims not supported by evidence
- Missing considerations
- Effect size interpretations
- What the other got right (be fair)

**Output:** Cross-review reports identifying convergent and divergent findings.

### Stage 4: Credibility Rating ⚠️ NEW

> Adapted from Xu & Yang (2026) Table S1

Assign a credibility rating based on warning count:

| Rating | Warnings | Interpretation | Action |
|--------|----------|----------------|--------|
| **HIGH** | 0 | Methods sound, results robust | ✅ Proceed to publication |
| **MODERATE** | 1-2 | Some concerns | ⚠️ Flag for human review |
| **LOW** | 3-4 | Substantial validity concerns | 🔄 Require methodology revision |
| **VERY LOW** | 5+ | Results likely unreliable | ❌ Do not publish; redesign |

**Warning triggers (Communication Research):**
1. Sample size < 100 for correlational claims
2. Effect size not reported or misclassified  
3. No temporal controls for longitudinal data
4. Missing bot/coordination check for social media
5. Cross-agent validation failed
6. Key assumption not tested
7. Multiple comparisons without correction
8. Claims exceed evidence

### Stage 5: Synthesis

All findings are synthesized:
- **Convergent findings** (all agents agree) → High confidence
- **Divergent findings** (agents disagree) → Investigate further
- **Errors caught** → Become new checks
- **Credibility rating** → Include in report header

### Stage 6: Knowledge Base Update

Lessons learned are documented:
- `LESSONS_LEARNED.md` — Methodology insights
- `KNOWLEDGE_BASE.md` — Failure patterns with resolutions

**Update protocol:** Changes happen BETWEEN runs, not during. All updates are version-controlled.

---

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
// Stage 1: Spawn analysts in parallel
const [glmAnalysis, kimiAnalysis] = await Promise.all([
  sessions_spawn({
    agentId: "redteam-glm",
    task: `Analyze this dataset and export key_stats.json: ${input}`,
    label: "academy-glm"
  }),
  sessions_spawn({
    agentId: "redteam-kimi", 
    task: `Analyze this dataset and export key_stats.json: ${input}`,
    label: "academy-kimi"
  })
]);

// Stage 2: Cross-validation (MANDATORY)
const validation = compareKeyStats(glmAnalysis.stats, kimiAnalysis.stats);
if (!validation.passed) {
  throw new Error(`Cross-validation failed: ${validation.divergences}`);
}

// Stage 3: Cross-review
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

// Stage 4: Compute credibility rating
const rating = computeCredibilityRating([glmReview, kimiReview]);
```

---

## Output Format

### Final Report Structure

```markdown
# AgentAcademy Report

**Credibility Rating: [HIGH/MODERATE/LOW/VERY LOW]**
**Warnings: [N]**
**Cross-Validation: [PASSED/FAILED]**

## Summary
[One paragraph synthesis]

## Cross-Validation Results
| Metric | GLM | Kimi | Match |
|--------|-----|------|-------|
| N (observations) | X | X | ✅ |
| Mean engagement | X.XX | X.XX | ✅ |
| Correlation (raw) | 0.XX | 0.XX | ✅ |
| Correlation (log) | 0.XX | 0.XX | ✅ |

## Convergent Findings (High Confidence)
1. [Finding]: All agents agree
   - GLM: [Details]
   - Kimi: [Details]

## Divergent Findings (Investigate)
1. [Finding]: Agents disagree
   - GLM says: [X]
   - Kimi says: [Y]
   - **Resolution needed**: [Question]

## Warnings Triggered
1. [Warning]: [Description]
2. [Warning]: [Description]

## Errors Caught
1. [Error]: [Description]
   - Caught by: [Agent]
   - **Added to KNOWLEDGE_BASE.md**: [Pattern name]

## Lessons for CommDAAF
- [Lesson 1] → Added to [file]
- [Lesson 2] → Added to [file]
```

---

## Completed Runs

| Run | Date | Dataset | Agents | Rating | Key Lessons |
|-----|------|---------|--------|--------|-------------|
| 1 | 2026-02-15 | @EastLosHighShow | GLM + Kimi | MODERATE | Effect size classification, platform change controls |
| 2 | 2026-02-17 | #EndSARS | GLM + Kimi | MODERATE | Log-transform correlations, bot detection, phase consistency |

See `LESSONS_LEARNED.md` for full documentation.

---

## Tier Integration

| Tier | Academy Scope | Cross-Validation |
|------|---------------|------------------|
| 🟢 Exploratory | Optional | Optional |
| 🟡 Pilot | Recommended | Required |
| 🔴 Publication | **Required** | **Required** |

---

## API Costs

Estimated per full run (2 analyses + validation + 2 cross-reviews):

| Stage | Est. Cost |
|-------|-----------|
| Independent analyses | ~$0.50 |
| Cross-validation | ~$0.05 |
| Cross-reviews | ~$0.30 |
| **Total** | **~$0.85/run** |

---

## Related Files

- `ARCHITECTURE.md` — Three-layer design (orchestration, knowledge, computation)
- `KNOWLEDGE_BASE.md` — Resolved failure patterns
- `LESSONS_LEARNED.md` — Methodology insights from runs
- `ACADEMY_STATE.json` — Run tracking and dataset history

---

## Limitations

1. **Not a replacement for human peer review**: Models don't have domain expertise or access to unpublished work
2. **Training cutoff**: Models may miss very recent literature
3. **Cultural bias**: Western research norms may be overrepresented
4. **Hallucination risk**: Always verify specific citations flagged by models

---

## References

Xu, Yiqing and Leo Yang Yang. 2026. "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Reanalysis." Working Paper, Stanford University.
https://yiqingxu.org/papers/2026_ai/AI_reproducibility.pdf

---

## Contributing

Found a blind spot? Run your analysis through the academy and submit lessons learned: https://github.com/weiaiwayne/commDAAF
