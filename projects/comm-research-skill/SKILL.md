# CommDAAF Skill v0.7.0

**Computational Communication Research Framework**

Trigger: `/commdaaf`, `/academy`, "run commdaaf", "agentacademy", "coordination detection"

## Overview

CommDAAF provides AI-assisted research validation through multi-model peer review. It's designed for computational social science research with emphasis on methodological rigor.

## Commands

| Command | Description |
|---------|-------------|
| `/commdaaf` | Show main menu |
| `/commdaaf run <task>` | Run AgentAcademy multi-model analysis |
| `/commdaaf status` | Check latest results and cron status |
| `/commdaaf framework` | Show the 3 CommDAAF questions |
| `/commdaaf kb` | View knowledge base and lessons learned |

## Menu Response

When user sends `/commdaaf` with no arguments, display:

```
📊 **CommDAAF v0.7.0**

1️⃣ **Run Analysis** → `/commdaaf run <your task>`
2️⃣ **Check Status** → `/commdaaf status`
3️⃣ **Framework** → `/commdaaf framework`
4️⃣ **Knowledge Base** → `/commdaaf kb`

🔗 AgentAcademy: vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy
📚 GitHub: github.com/weiaiwayne/commDAAF
```

## The CommDAAF Framework

Three mandatory questions before any analysis:

### Q1: What EXACTLY are you measuring?
- Operationalize variables explicitly
- Define engagement, sentiment, coordination, etc.
- Specify time windows and filters

### Q2: How will you VALIDATE your results?
- Manual coding sample (minimum 20)
- Cross-model validation
- Known baseline comparison

### Q3: What ELSE could explain your findings?
- Alternative hypotheses
- Confounding variables
- Platform algorithm effects
- Bot/coordination contamination

## Engagement Analysis Requirements (MANDATORY)

When studying **what predicts online engagement** (likes, shares, virality), you MUST control for:

### User-Level Controls
| Variable | Why Required | Typical Effect |
|----------|--------------|----------------|
| **log_followers** | High-follower accounts get more engagement by default | IRR ≈ 1.2-1.5 per log unit |
| **verified** | Verification badge signals credibility | Often significant |
| **account_age** | Older accounts have established audiences | May interact with followers |

### Content-Level Controls
| Variable | Why Required | Typical Effect |
|----------|--------------|----------------|
| **has_media** | Images/videos get more engagement | IRR ≈ 1.5-3.0 |
| **has_hashtag** | Hashtags increase discoverability | Context-dependent |
| **has_mention** | @mentions can reduce or increase reach | Often negative (IRR < 1) |
| **text_length** | Longer posts may signal effort/value | Often positive |
| **has_url** | Links may reduce engagement (platform penalty) | Platform-dependent |

### Statistical Requirements
1. **Distribution check**: Engagement data is almost always right-skewed with excess zeros
2. **Model choice**: Use Negative Binomial (not OLS) for overdispersed count data
3. **Transform followers**: Always log-transform (log1p) follower counts
4. **Report both**: Show model WITH and WITHOUT controls to demonstrate confounding

### Example: The INFORMATIONAL Frame Confound (Feb 2026)

**Without controls**: INFORMATIONAL frame → IRR = 2.72 (p < .001) — "Facts beat feelings!"

**With controls**: INFORMATIONAL frame → IRR = 0.98 (ns) — Frame effect disappears

**What happened**: Informational posts came from high-follower journalists. Follower count (IRR = 1.22***) explained the engagement, not frame.

**Lesson**: Never report content-effect findings without user-level controls. Confounding by account size is the default assumption.

### Minimum Control Checklist
- [ ] log_followers included
- [ ] verified status included (if available)
- [ ] has_media included (if available)
- [ ] has_mention included
- [ ] Distribution diagnostics run
- [ ] Negative Binomial (or appropriate count model) used
- [ ] Both controlled and uncontrolled models reported

## Data Preservation Rule 🚨

**NEVER discard already-coded data.** Always merge existing coding with new batches.

```python
# WRONG: Start fresh
new_results = code_all_missions(missions)  # Wastes prior work

# RIGHT: Merge existing
existing = load_json("coding_results_v1.json")
existing_eins = {r["ein"] for r in existing}
uncoded = [m for m in missions if m["ein"] not in existing_eins]
new_results = existing + code_missions(uncoded)
```

**Lesson learned:** In the Nonprofit Framing study, 120 Ollama-coded items were discarded when switching to Codex/Gemini. This wasted compute and required re-coding.

---

## AgentAcademy Workflow

Multi-model peer review process:

1. **Independent Analysis** — GLM and Kimi analyze separately
2. **Cross-Validation** — Compare key statistics (MANDATORY)
3. **Peer Critique** — Each model reviews the other
4. **Credibility Rating** — HIGH/MODERATE/LOW/VERY LOW
5. **Knowledge Base Update** — Document lessons learned

### Available Agents

| Agent | Model | Role |
|-------|-------|------|
| `redteam-glm` | GLM-4.7 | Peer Reviewer (Chinese corpus perspective) |
| `redteam-kimi` | Kimi K2.5 | Peer Reviewer (Long-context specialist) |

### Spawn Command
```
sessions_spawn({
  agentId: "redteam-glm",
  task: "Analyze this dataset following CommDAAF protocol: <data>",
  label: "academy-run"
})
```

## Knowledge Base Locations

| Resource | Path |
|----------|------|
| AgentAcademy Results | `commdaaf_agentacademy_results.json` |
| Knowledge Base | `skill-templates/workflows/agent-academy/KNOWLEDGE_BASE.md` |
| Lessons Learned | `skill-templates/workflows/agent-academy/LESSONS_LEARNED.md` |
| Workflow Spec | `skill-templates/workflows/agent-academy/WORKFLOW.md` |
| Architecture | `skill-templates/workflows/agent-academy/ARCHITECTURE.md` |
| **Method References** | `references/methods/*.md` |

## Deployed Sites

- **AgentAcademy**: https://vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy
- **Results JSON**: `/root/vinechat/static/vineanalyst/commdaaf/results.json`

## Coordination Detection Patterns

Key signals from AgentAcademy runs:

| Pattern | Threshold | Action |
|---------|-----------|--------|
| Retweet ratio | >80% | Flag as potential coordination |
| Peak/trough ratio | >4:1 | Investigate temporal clustering |
| Non-local language | >20% | Check for cross-border coordination |
| Account creation spike | Clustering around events | Flag sleeper accounts |

## Zotero Integration

- **API Key**: `/root/.openclaw/secrets/zotero.key`
- **Library ID**: 6345227
- **Use for**: Literature validation, citation checks, RQ grounding

## Cron Job

AgentAcademy can run on schedule:
```
cron add --schedule "0 5 * * 0" --task "Run weekly AgentAcademy check"
```

## Example: Status Check

When `/commdaaf status` is invoked:

1. Read `commdaaf_agentacademy_results.json`
2. Show last run date and findings summary
3. Check cron job status
4. Show link to live dashboard

## Related Skills

- `peer-review` — Multi-model document review
- See `antigravity/` for cross-platform deployment

## AI/Algorithmic Audit Studies

When conducting **AI audit research** (bias testing, differential treatment, algorithmic behavior analysis), use the dedicated skill:

**📁 Skill Location:** `skills/algorithmic-audit/SKILL.md`

### When to Use
- Auditing AI systems for political/demographic bias
- Testing chatbots for differential treatment
- Measuring algorithmic behavior across conditions
- Any study requiring systematic AI-to-AI evaluation

### Key Methods (from DAI Study, Apr 2026)
| Method | Description |
|--------|-------------|
| **Factorial Design** | N models × M conditions × K replications |
| **Simulated Users** | LLM-as-user with motivated reasoning tactics |
| **Dual-Rater Evaluation** | Two LLMs rate independently (report inter-rater r) |
| **Behavioral Anchoring** | Score observable behaviors, not inferred intent |
| **Multi-Dimension Metrics** | Composite indices revealing different failure modes |

### Quick Reference
```python
# Effect size interpretation
d = 0.2  # Small
d = 0.5  # Medium  
d = 0.8  # Large
d > 1.0  # Very large (common in algorithmic audits)

# Always use Bonferroni for multiple comparisons
alpha_corrected = 0.05 / n_comparisons
```

### Included Templates
- `skills/algorithmic-audit/references/evaluator_rubric_v2.md` — 4-dimension scoring rubric
- `skills/algorithmic-audit/references/partisan_user_persona.md` — Simulated partisan user protocol

---

## Method References

| Topic | File | Source Study |
|-------|------|--------------|
| **AI/Algorithmic Audit** | `skills/algorithmic-audit/SKILL.md` | DAI Study (Apr 2026) |
| Cross-National Framing | `references/methods/comparative-framing.md` | Global South AI (Mar 2026) |
| Multi-Agent Research | `references/methods/multi-agent-research.md` | VibePoll-2026 |
| Google Trends Validation | `references/methods/google-trends-validation.md` | VibePoll-2026 |
| Layered Coding Schemes | `references/methods/layered-coding.md` | Nonprofit Framing (Mar 2026) |
| Multi-Coder Reliability | `references/methods/multi-coder-reliability.md` | Nonprofit Framing (Mar 2026) |
| NTEE Enrichment | `references/methods/ntee-enrichment.md` | Nonprofit Framing (Mar 2026) |

### Key Lessons from VibePoll-2026

**Multi-Agent Errors Caught**:
- Per-capita on normalized data → Finding flipped (−24% → +143%)
- Over-differencing → Hidden signal revealed
- Baseline confusion → Contradictory claims exposed
- Granger miscount → Null conclusion reversed

**Top Skills Added**:
1. **Verify data structure before transforming** — Don't per-capita normalize proportions
2. **Validate at target granularity** — National ≠ state-level usability
3. **Separate findings from synthesis** — Attribute claims to actual analysis
4. **Test both causal directions** — Markets led Trends, not vice versa
5. **Smooth before differencing** — Order matters for time series
6. **Question implausible effects** — >100% effects are usually errors

## References

- Xu & Yang (2026): "Scaling Reproducibility"
- DAAF: github.com/DAAF-Contribution-Community/daaf
- CommScribe (sister project): github.com/weiaiwayne/commscribe
