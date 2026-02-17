# MEMORY.md - Long-Term Knowledge

*Last updated: 2026-02-04*

---

## OpenClaw + Social Science Research (Feb 2026)

### Key Market Insights
- **3,038+ arXiv papers** on AI in social sciences (2026) — growing field
- Major pain points: privacy-sensitive data scarcity, multi-platform fragmentation, literature review burden, participant recruitment challenges
- Students & early adopters show high AI adoption intention

### High-Value Use Cases Identified
1. **Autonomous Literature Review** — 80% time reduction potential
2. **Multi-Platform Social Media Monitoring** — X, Reddit, TikTok, Instagram aggregation
3. **Participant Recruitment & Engagement** — 5x recruitment rate improvement
4. **Social Experiments with AI Agents** — scalable to 14,490+ agents
5. **Automated Data Collection** — ethical scraping with GDPR compliance
6. **Real-Time Monitoring & Alerts** — crisis response, misinformation tracking
7. **Policy Analysis & Compliance** — DSA, AI Act auditing

### Target Markets
- Academic institutions (sociology, poli-sci, psych, econ departments)
- Government agencies (NSF, CDC, statistical bureaus)
- NGOs and advocacy organizations
- Public health organizations
- Market research firms

### Competitive Landscape
- Direct: GPT-4, Claude, Gemini (general purpose)
- Research tools: Elicit, Consensus, Brandwatch, Qualtrics
- Agent frameworks: LangChain, CrewAI, AutoGPT
- **OpenClaw differentiators**: true autonomy, privacy-first, multi-platform integration, research-specific features, open source

### GTM Priorities
1. Academic pilot program (10-15 departments)
2. Publish research papers demonstrating capabilities
3. Develop social science plugins (lit review, scraping, recruitment)
4. Build graduate student ambassador program

*Full report: memory/research/openclaw-social-science-2026-02.md*

---

## VibePolitics Project (Feb 2026)

### Project Overview
**Codename:** VibePolitics  
**Goal:** Agentic unconventional polling system for 2026 US midterms & Trump presidency  
**Location:** Boston, MA (framing)  
**Academic Target:** Peer-reviewed publication in political science journals

### Architecture
- **4 Autonomous Agents:**
  - PolAgent-A & PolAgent-B (political analysis, debate)
  - EconAgent-A & EconAgent-B (economic analysis, debate)
- **Data Sources:** Polymarket API, Kalshi API, Google Trends
- **Agent Capabilities:** Search for context, decide to act/not act, choose keywords, engage/abstain from debates
- **Transparency:** All reasoning logged and visible

### Key Design Decisions
1. Agents debate and peer-review each other
2. Multi-source data fusion (markets + search trends)
3. Continuous monitoring, not periodic snapshots
4. Frontend modeled after Kalshi.com
5. Academic publication strategy from day one

### Literature Review Findings
- **Prediction markets outperform polls** 74% of the time (Berg et al., 2008)
- **Google Trends adds predictive value** when combined with other sources
- **Multi-agent LLM systems** validated by ElectionSim (14,490 agents)
- **Key methodological innovation:** Track variance, not just levels (Timoneda & Wibbels, 2022)
- **Polymarket specifically** validated for academic research (Chen et al., 2024)

### API Access Confirmed
- Polymarket: `gamma-api.polymarket.com` — works, no auth needed
- Rich metadata: prices, volume, liquidity, spread, price changes

### Project Files
- `projects/vibepolitics/PROJECT_SPEC.md` — Full specification
- `projects/vibepolitics/VibePolitics_Spec_v0.1.pdf` — PDF version
- `projects/vibepolitics/research/LITERATURE_REVIEW.md` — Academic literature review
- `projects/vibepolitics/research/LITERATURE_REVIEW.pdf` — PDF version

### Next Steps
1. Build MVP data pipeline (Polymarket + Kalshi + Google Trends)
2. Implement single agent prototype
3. Expand to four-agent system with debate
4. Develop frontend dashboard
5. Validate against traditional polls

---

## Communication Research Skill Project (Feb 2026)

### Project Overview
Adapting DAAF (Data Analyst Augmentation Framework) for communication research as an OpenClaw skill package.

**Source repo:** https://github.com/DAAF-Contribution-Community/daaf

### Key Deliverables
- Spec document: `projects/comm-research-skill/SPEC_DRAFT.md`
- Zotero analysis: `projects/comm-research-skill/ZOTERO_ANALYSIS.md`

### Wayne's Research Focus (from Zotero)
- Agentic AI in social science
- Coordinated behavior detection
- Network analysis of movements
- Attention economy
- Zotero ID: 6345227

### Key Selling Point
**Multi-model architecture** — different models for different tasks:
- Cost: ~$5-15 vs DAAF's $30-60
- Epistemic diversity
- Vendor independence

---

## Research Archive
- `memory/research/openclaw-social-science-2026-02.md` — OpenClaw + Social Science analysis
- `projects/vibepolitics/research/LITERATURE_REVIEW.md` — VibePolitics academic foundation
- `projects/comm-research-skill/` — Communication Research Skill project

---

## Peer Review Skill (Feb 2026)

### Capability
Multi-model peer review system using 5 diverse LLMs via OpenRouter for epistemically diverse feedback on documents.

### Default Models
1. **DeepSeek V3.2** — Methodologist (research design, validity)
2. **Kimi K2.5** — Theorist (concepts, literature, argument)
3. **Gemini 3 Flash** — Empiricist (data, statistics, replication)
4. **Grok 4.1 Fast** — Skeptic (adversarial critique)
5. **Qwen3 VL Thinking** — Integrator (coherence, gaps)

### Location
- Skill: `skills/peer-review/`
- API Key: `~/.openclaw/secrets/openrouter.key`

### Usage
Trigger with: "peer review", "critique my paper", "multi-model analysis"

---

## 5 Specialist Agents (Feb 2026)

### Team
| Agent | Role | Model | Perspective |
|-------|------|-------|-------------|
| **Kenji** 🔬 | Methodologist | DeepSeek V3.2 | "Is the process sound?" |
| **Priya** 📚 | Theorist | Kimi K2.5 | "What's the big picture?" |
| **Wei** 📊 | Empiricist | Gemini 3 Flash | "What does the data say?" |
| **Arjun** 🔥 | Skeptic | Grok 4.1 Fast | "What could go wrong?" |
| **Mei** 🔗 | Integrator | Qwen3 VL Thinking | "How does it fit together?" |

### Workspaces
- `~/.openclaw/workspace-kenji/`
- `~/.openclaw/workspace-priya/`
- `~/.openclaw/workspace-wei/`
- `~/.openclaw/workspace-arjun/`
- `~/.openclaw/workspace-mei/`

### Slack Integration
- Workspace: lampbotics
- Each agent = separate Slack app with unique identity
- Tokens: `~/.openclaw/secrets/slack/agents.json`

---
