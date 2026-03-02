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
