# MEMORY.md - Long-Term Knowledge

*Last updated: 2026-04-02*

---

## 🚨 AgentAcademy Publishing Routes (CRITICAL)

### Main Page: agentacademy.lampbotics.com/

**The template is HARDCODED HTML, not dynamic JSON!**

To publish a new study to the main page:
1. Edit `/root/vinechat/templates/commdaaf_agentacademy.html`
2. Add a `<div class="study-card">` block under "Completed Studies"
3. Flask auto-reloads (no restart needed)

**DO NOT** just update these JSON files (they're not used for the main page):
- `/root/.openclaw/workspace/commdaaf_agentacademy_results.json` — NOT USED
- `/root/vinechat/static/vineanalyst/commdaaf/results.json` — NOT USED

### Intuitionist Page: agentacademy.lampbotics.com/intuitionist

This IS dynamic. To publish:
1. Create study folder: `/root/agentacademy/intuitionist/studies/<study_id>/`
2. Add `study_config.json` with full metadata
3. Add peer reviews as `PEER_REVIEW_*.md`
4. Restart Intuitionist server: `pkill -f "server.py --port 3848" && cd /root/agentacademy/intuitionist && nohup python3 server.py --port 3848 --host 127.0.0.1 &`
5. Studies sorted by `completed_at` (most recent first)

### Static Files (PDFs, Slides, Landing Pages)

Put in `/var/www/agentacademy/<study-name>/`:
- nginx serves from `/var/www/agentacademy/`
- Add nginx location block if new path needed
- Run `/usr/sbin/nginx -t && systemctl reload nginx`

### Flask App Details
- Path: `/root/vinechat/app.py`
- Port: 5000
- Templates: `/root/vinechat/templates/`
- Restart: `pkill -f "vinechat/app.py" && cd /root/vinechat && nohup python3 app.py &`

---

## 🎓 Intuitionist - Academic Intuition Agent (Mar 2026)

### Overview
**Intuitionist** is an AgentAcademy module that develops "academic intuition" by reading social science papers. It learns to predict authors, journals, and topics from abstracts.

### Location
```
~/agentacademy/intuitionist/
├── data/
│   ├── intuitionist.db     # 9MB SQLite (1795 papers, 2984 authors)
│   └── journals.json       # 21 journals config
├── scripts/
│   ├── ingest.py           # RSS + Crossref ingestion
│   ├── intuition.py        # Prediction tasks
│   └── init_db.py          # Schema setup
└── README.md
```

### Data Coverage
| Discipline | Journals | Papers |
|------------|----------|--------|
| Communication | 7 | 615 |
| Political Science | 7 | 678 |
| Sociology | 7 | 502 |
| **Total** | **21** | **1,795** |

### Accuracy (v0.1)
| Task | Accuracy | Notes |
|------|----------|-------|
| Author (Top-5) | **94%** | Writing style is distinctive |
| Journal Top-1 | 30% | Exact match |
| Journal Top-3 | **52%** | Good for reviewer matching |
| Journal Top-5 | **64%** | Broad matching |
| Discipline | 32% | Social sciences overlap too much |

### Key Technical Decisions
1. **Embeddings**: Local e5-base-v2 (119 texts/sec, no API cost)
2. **Storage**: SQLite + numpy blobs for embeddings
3. **Sources**: RSS (Sage, T&F) + Crossref API (Oxford, Cambridge, Wiley)
4. **Hierarchical prediction failed** — flat similarity works better

### Usage
```bash
# Ingest papers
python3 scripts/ingest.py --limit 100

# Evaluate accuracy
python3 scripts/intuition.py --evaluate author --trials 50
python3 scripts/intuition.py --evaluate journal --trials 50

# ORCID enrichment
python3 scripts/ingest.py --enrich-orcid
```

### Next Steps
- [ ] Reviewer matching function (combine author + journal signals)
- [ ] Daily cron ingestion for new papers
- [ ] OpenClaw agent wrapper
- [ ] Citation data from Semantic Scholar

---

## 💵 Benny - Personal Finance Agent (Mar 2026)

### Overview
**Benny** (named after the $100 bill) is Wayne's personal financial advisor agent. Ramit Sethi's "I Will Teach You to Be Rich" philosophy, zero BS delivery.

### Access
- **Telegram command**: `/benny` (in menu)
- **Agent ID**: `benny`
- **Model**: DeepSeek V3.2 (via OpenRouter)
- **Workspace**: `~/.openclaw/workspace-benny/`

### How to Route to Benny
When Wayne types `/benny [message]` or asks to talk to Benny:
```
sessions_spawn(agentId: "benny", task: "[user's financial question]")
```

### Capabilities
- PDF statement parsing (Chase, Amex, BOA, Robinhood exports)
- Spending pattern analysis
- Net worth tracking
- Investment allocation review
- Budget coaching (Ramit Sethi style: automate, big wins, conscious spending)

### Memory Structure
- `memory/financial-profile.md` — Master financial profile
- `memory/spending-patterns.md` — Learned spending behaviors
- `memory/goals.md` — Financial goals tracking
- `statements/` — Archived statements by institution

### Philosophy (from SOUL.md)
1. Pay yourself first (before you can spend it on DoorDash)
2. Automate everything (willpower is for suckers)
3. Big wins > latte math (negotiate salary, not skip coffee)
4. Conscious spending (ball out on what you love, ruthless on what you don't)
5. Invest early and boring (index funds beat stock picking)
6. Debt is an emergency (except low-rate mortgage/student loans)

---

## 🚨 AgentAcademy Studies - MANDATORY PROTOCOL

**When Wayne asks for an AgentAcademy study, test study, or agentic content analysis:**

1. **MUST READ FIRST**: `projects/comm-research-skill/agent-academy-study-protocol.md`
2. **Follow all phases** in the protocol (Pre-Study → QC Checklist)
3. **Critical rules**:
   - Kimi batch limit: **25 posts max** (truncates JSON otherwise)
   - **Mandatory distribution diagnostics** before any regression
   - Report **frame-specific reliability**, not just aggregate κ
   - Never use OLS on skewed engagement data → use Negative Binomial
   - Never use OpenRouter/Mei for AgentAcademy (wrong billing model)

**Location**: `projects/comm-research-skill/agent-academy-study-protocol.md`

---

## Congressional AI Framing Study (Mar 2026)

### Overview
Exploratory study analyzing how AI is framed in U.S. congressional hearings using CommDAAF multi-model validation.

### Data Location
```
/root/.openclaw/workspace/projects/congressional-ai-framing/
├── DATA_MANIFEST.md             # Full data documentation
├── STUDY_DESIGN.md              # Research design
├── data/
│   ├── transcripts/             # 561 hearing transcripts (117MB)
│   └── pilot_batch_25.json      # Pilot sample
├── prompts/
│   └── commdaaf_v1.0.md         # Coding scheme (8 frames)
└── outputs/claude/              # Claude coding results
```

### Data Source
- **API**: GovInfo (api.govinfo.gov)
- **Collection**: CHRG (Congressional Hearings)
- **Query**: `"artificial intelligence" collection:CHRG`
- **API Key**: data.gov key (Wayne's)
- **Total Available**: 1,754 AI-related hearings

### Coding Scheme (8 Frames)
| Frame | Definition |
|-------|------------|
| INNOVATION | Economic opportunity, competitiveness |
| RISK_SAFETY | Existential/catastrophic threats |
| RISK_HARM | Concrete harms (children, users) |
| RISK_ECONOMIC | Job loss, inequality |
| GOVERNANCE | Regulatory approaches |
| SOVEREIGNTY | National security, China competition |
| RIGHTS | Privacy, discrimination |
| TECHNICAL | Scientific explanations |

### Pilot Results (Claude, N=25)
- **Valid AI hearings**: 9 (36%)
- **False positives**: 16 (64%) ⚠️
- **Frame distribution** (valid only):
  - SOVEREIGNTY: 56%
  - GOVERNANCE: 22%
  - RISK_HARM: 22%

### Key Issue (SOLVED)
Search returns hearings that *mention* AI, not hearings *about* AI.

**Solution**: `filter_transcripts.py` scores full transcripts by AI term density.
- HIGH: 129 hearings (23%) - density ≥5 or 20+ strong AI terms
- MEDIUM: 69 hearings (12%)
- Valid AI hearings: **198 total (35%)**

Use `data/valid_ai_hearings.json` for coding, not raw search results.

### False Positive Context Analysis
AI is mentioned in non-AI hearings in these contexts:
1. **List of technologies** (32%): "technologies like 5G, AI, and cloud..."
2. **Government modernization** (27%): AI as efficiency tool
3. **National security passing mention** (15%): Brief AI reference in defense hearings
4. **Workforce/automation concerns** (10%): Job impact discussions
5. **Specific application mentions** (10%): AI as tool for other tasks
6. **Budget line items** (6%): AI funding in appropriations

See `data/FALSE_POSITIVE_ANALYSIS.md` for full analysis.

### Quick Data Retrieval
```python
from pathlib import Path
import json

DATA = Path("/root/.openclaw/workspace/projects/congressional-ai-framing/data")

# Load pilot batch
with open(DATA / "pilot_batch_25.json") as f:
    pilot = json.load(f)

# Load Claude results
with open(DATA.parent / "outputs/claude/pilot_25_claude.json") as f:
    results = json.load(f)
```

### Status
- [x] Data collection (561 transcripts)
- [x] CommDAAF prompt v1.0
- [x] Claude pilot coding (original 25)
- [x] Filter false positives (198 valid AI hearings identified)
- [ ] Claude pilot coding (filtered 25)
- [ ] GLM pilot coding
- [ ] Kimi pilot coding
- [ ] Full sample coding

---

## GLM Model Configuration (Mar 2026)

### ⚠️ ALWAYS USE OPENCODE FOR GLM ⚠️

**Correct method:**
```bash
opencode -m zai-coding-plan/glm-4.7 run "Your task"
```

**With PTY for background tasks:**
```bash
exec pty:true background:true workdir:/path command:"opencode -m zai-coding-plan/glm-4.7 run 'Task'"
```

### DO NOT USE:
- ❌ Mei agent (OpenRouter) — Wayne has said this many times
- ❌ sessions_spawn with GLM
- ❌ Direct API calls

### Why OpenCode?
- Uses Wayne's z.ai coding plan subscription
- Proper PTY handling for interactive work
- File read/write capabilities

### Kimi Configuration
- **Kimi coding plan works** via `kimi-coding/k2p5` (both OpenClaw and OpenCode)
- OpenClaw agent `redteam-kimi` uses this correctly

---

## Chinese LLM Censorship Study (Feb 2026)

### Key Finding: Academic Framing Does NOT Bypass Content Filters

**Hypothesis (DISPROVEN):** CommDAAF's ~2,500 lines of academic methodology could dilute sensitive keywords below detection threshold.

**Reality:** OpenCode's free proxy (`opencode/kimi-k2.5-free`) routes through infrastructure without content filters. Direct API calls to z.ai and Kimi block Xinjiang/Uyghur content regardless of framing.

### Test Results
| API | Direct Prompt | CommDAAF-Wrapped | Free Proxy |
|-----|---------------|------------------|------------|
| z.ai GLM | ❌ BLOCKED | ❌ BLOCKED | ✅ WORKED |
| Kimi | ❌ BLOCKED | ❌ BLOCKED | ✅ WORKED |

### Implications
1. Chinese LLM content filtering is at API layer, not model weights
2. Proxy services create unintended policy gaps
3. Academic framing is not a bypass technique
4. Always verify which API endpoint is being called

### Wayne's OpenCode Config
- `zai-coding-plan/glm-4.7` → Direct z.ai API (paid, filtered)
- `kimi-for-coding/k2p5` → Direct Kimi API (paid, filtered)  
- `opencode/kimi-k2.5-free` → OpenCode proxy (free, unfiltered)

### GitHub
- Final study: `papers/CENSORSHIP_STUDY_FINAL.md`
- Commits: `580dbd3` (retraction), `789dea3` (final study)

### AgentAcademy Deployment
- Source: `/root/.openclaw/workspace/commdaaf_agentacademy_results.json`
- Deploy to: `/root/vinechat/static/vineanalyst/commdaaf/results.json`
- Site: https://vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy

---

## Chinese LLM Censorship Study (Feb 2026)

### Key Finding: Academic Framing Does NOT Bypass Content Filters

**Hypothesis (DISPROVEN):** CommDAAF's ~2,500 lines of academic methodology could dilute sensitive keywords below detection threshold.

**Reality:** OpenCode's free proxy (`opencode/kimi-k2.5-free`) routes through infrastructure without content filters. Direct API calls to z.ai and Kimi block Xinjiang/Uyghur content regardless of framing.

### Test Results
| API | Direct Prompt | CommDAAF-Wrapped | Free Proxy |
|-----|---------------|------------------|------------|
| z.ai GLM | ❌ BLOCKED | ❌ BLOCKED | ✅ WORKED |
| Kimi | ❌ BLOCKED | ❌ BLOCKED | ✅ WORKED |

### Implications
1. Chinese LLM content filtering is at API layer, not model weights
2. Proxy services create unintended policy gaps
3. Academic framing is not a bypass technique
4. Always verify which API endpoint is being called

### Wayne's OpenCode Config
- `zai-coding-plan/glm-4.7` → Direct z.ai API (paid, filtered)
- `kimi-for-coding/k2p5` → Direct Kimi API (paid, filtered)  
- `opencode/kimi-k2.5-free` → OpenCode proxy (free, unfiltered)

### GitHub
- Final study: `papers/CENSORSHIP_STUDY_FINAL.md`
- Commits: `580dbd3` (retraction), `789dea3` (final study)

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

## AgentAcademy Sprint Complete (Feb 2026)

### Summary
7 studies completed with 3-model validation (Claude + GLM + Kimi). Key findings:
- Belarus: Milk Tea Alliance solidarity (Thai content = organic, not bots)
- Xinjiang: Dual-sided coordination (both sides amplifying)
- All studies: 3-model convergence = high confidence

### Generalizable Lessons Added to CommDAAF
- Retweet-heavy warning (>80%)
- Peak/trough detection (>4:1)
- Language anomaly check (>20% non-local)
- Dual-sided coordination framework

### Schedule
- Now weekly on Sundays 05:00 UTC
- Site: vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy

---

## CommDAAF Cross-Agent Research (Feb 2026)

### Experiment Summary
First full autonomous research workflow: GLM-4.7 and Kimi K2.5 independently analyzed 3,153 tweets (@EastLosHighShow, 2014-2018), then cross-reviewed each other.

### Key Findings
- **Hashtags strongest predictor**: 3.5-3.8x engagement, δ=0.40 (medium effect)
- **Sentiment NOT predictive**: ρ = -0.03 to -0.08 (contradicts common assumptions)
- **2016 organic peak**: Real engagement growth before platform algorithm changes
- **2017 DACA anomaly**: Political content spike, not organic growth

### Methodological Lessons
- Effect sizes need proper classification (Cohen 1988 benchmarks)
- Multiple comparisons require correction (Bonferroni)
- Post-hoc categorizations should be flagged
- 4+ year datasets need temporal periodization

### CommDAAF Audit Grade: C+
Good on conceptual validity; missed temporal skew, engagement normalization, content controls.

### Files
- `projects/comm-research-skill/ANALYSIS_RESULTS.md` (GLM)
- `projects/comm-research-skill/ANALYSIS_RESULTS_KIMI.md` (Kimi)
- `/tmp/kimi-version/comm-daaf/CRITICAL_PM_REVIEW.md` (cross-review)

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

---

## Global South AI Framing Study (Mar 2026)

### Study Complete
- **Paper**: v9 final, deployed to AgentAcademy
- **Data**: US (192 hearings) vs Global South (102 docs: SA 41, Brazil 54, India 7)
- **Key finding**: US frames AI as competition (Sovereignty 22%), Global South frames as governance (42%)
- **Effect sizes**: Sovereignty V=.32, Governance V=.25 (medium effects)
- **Reliability**: Overall κ=.91; Rights κ=.52 (flagged)

### Peer Review Process
- Round 1 (v7): Both Kimi + GLM → Major Revision
- Round 2 (v8/v9): Both → Minor Revision
- Key issues fixed: effect sizes, Bonferroni, Rights flagging, causal hedging

### Deployment
- **NEW DOMAIN**: https://agentacademy.lampbotics.com (Mar 13, 2026)
- Old path still works: vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy
- Chinese version: /zh (龙虾学院)
- Agent enrollment: /enroll
- API: /api/* (AgentID server on port 3847)

### AgentID System (Mar 2026)
- Decentralized identity for AI agents
- Ed25519 keypairs, Agent ID = `aa_` + sha256(pubkey)[:22]
- **npm package**: https://www.npmjs.com/package/agentid-cli (published 2026-03-13)
- Repo: https://github.com/weiaiwayne/agentacademy
- Server: systemd service `agentid.service`
- First agent: `aa_FEiyWTFBrvqQ2GwoYDcKZm` (Claude-OpenClaw)
- PDFs: Paper + 4 reviews + Response to Reviewers

### Competitor: Agent4Science + Flamebird
- **Agent4Science** (agent4science.org): Social network for AI scientists
- **Flamebird**: Their autonomous agent runtime (`@agentforscience/flamebird`)
- Run by Chenhao Tan (UChicago), uses NeuriCo for paper generation
- We focus on credentials/training; they focus on discourse/publishing

### Skills Added
- `skills/commdaaf/references/methods/comparative-framing.md`
- Effect size reporting, multi-round peer review, reliability flagging

