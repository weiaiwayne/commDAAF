# CommDAAF Skill

Trigger: `/commdaaf`, `/academy`, "run commdaaf", "agentacademy"

## Overview

CommDAAF (Computational Communication Research Framework) provides AI-assisted research validation through multi-model peer review.

## Commands

### `/commdaaf` — Show Menu
Display options:
1. **Run AgentAcademy** — Multi-model analysis with peer critique
2. **Check Status** — Latest AgentAcademy results and cron status
3. **Show Framework** — The 3 CommDAAF questions
4. **Knowledge Base** — View lessons learned

### `/commdaaf run <task>` — Run Analysis
Spawn GLM and Kimi agents to analyze data with cross-validation.

### `/commdaaf status` — Check Status
- Show latest AgentAcademy results
- Check cron job status
- Link to live site

### `/commdaaf framework` — Show Framework
Display the three CommDAAF questions:
1. What EXACTLY are you measuring?
2. How will you VALIDATE your results?
3. What ELSE could explain your findings?

## Knowledge Base Locations

| Resource | Path |
|----------|------|
| Results JSON | `/root/.openclaw/workspace/projects/comm-research-skill/commdaaf_agentacademy_results.json` |
| Knowledge Base | `projects/comm-research-skill/skill-templates/workflows/agent-academy/KNOWLEDGE_BASE.md` |
| Lessons Learned | `projects/comm-research-skill/skill-templates/workflows/agent-academy/LESSONS_LEARNED.md` |
| Workflow | `projects/comm-research-skill/skill-templates/workflows/agent-academy/WORKFLOW.md` |

## Live Site
https://vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy

## Agent Configuration

Available agents for AgentAcademy runs:
- `redteam-glm` — GLM-4.7 (Zhipu AI)
- `redteam-kimi` — Kimi K2.5 (Moonshot)

## Zotero Integration
- API Key: `/root/.openclaw/secrets/zotero.key`
- Library ID: 6345227
- Use for literature validation and citation checks

## Menu Response

When user sends `/commdaaf` with no arguments, respond with:

```
📊 **CommDAAF Menu**

1️⃣ `/commdaaf run` — Run AgentAcademy analysis
2️⃣ `/commdaaf status` — Check latest results  
3️⃣ `/commdaaf framework` — Show 3 questions
4️⃣ `/commdaaf kb` — View knowledge base

🔗 Live: vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy
```
