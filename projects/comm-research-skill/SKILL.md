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

## References

- Xu & Yang (2026): "Scaling Reproducibility"
- DAAF: github.com/DAAF-Contribution-Community/daaf
- CommScribe (sister project): github.com/weiaiwayne/commscribe
