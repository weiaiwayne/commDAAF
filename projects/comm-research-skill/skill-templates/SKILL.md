# CommDAAF — Computational Communication Research Framework

**Version 0.3.0** — Now with tiered validation, nudge system, and theory integration.

An OpenClaw skill package for computational communication research, adapted from DAAF.

---

## What's New in v0.3

### 🎚️ Tiered Validation System
Match validation to your stakes:
| Tier | Time | Use Case |
|------|------|----------|
| 🟢 Exploratory | 30-60 min | Hypothesis generation |
| 🟡 Pilot | 2-4 hrs | Committee presentation |
| 🔴 Publication | 1-2 days | Journal submission |

See `workflows/tiered-validation.md`

### 🧠 Conscious Research Design (Nudge System)
Five nudge types prevent default-driven research:
1. Default Danger Flags
2. Active Choice Requirement
3. Trade-Off Visualization
4. Assumption Audit
5. Reflection Checkpoints

Try the demo: `python scripts/conscious_choice_demo.py`

See `workflows/nudge-system.md`

### 📚 Theory Modules
Communication theory integration:
- `theories/gatekeeping.md` — Network gatekeeping, algorithmic curation
- `theories/agenda-setting.md` — Network agenda-setting, intermedia dynamics
- `theories/networked-publics.md` — Publics, counterpublics, affordances
- `theories/information-diffusion.md` — Cascades, virality, echoing

### 🔄 Guided Pipelines
End-to-end workflows with time estimates:
- `pipelines/twitter-network-historical.md` — Post-API Twitter analysis

---

## Overview

This skill enables AI-assisted research on digital communication phenomena:
- Social media data collection and analysis
- Network analysis of online communities
- Text analysis (topics, sentiment, frames)
- Coordinated behavior detection
- Multi-platform studies

Built on multi-agent orchestration with per-task model routing for cost efficiency.

## Trigger Patterns

Activate this skill when user requests involve:
- "analyze [topic] on [platform]"
- "research [phenomenon] in social media"
- "detect coordinated behavior"
- "network analysis of [dataset]"
- "topic modeling / sentiment analysis"
- "collect data from [platform]"
- "explore this data"
- "review my code/analysis"
- "what do these results mean"

## Research Stages (Entry Points)

This skill is **stage-agnostic** — enter at any point in your research:

| Stage | You Have | You Want | Triggers |
|-------|----------|----------|----------|
| **🔍 Exploration** | Raw data | Understand what's there | "what's in this", "explore", "first look" |
| **📋 Validation** | Code/analysis | Check if it's sound | "review", "audit", "check my" |
| **📊 Interpretation** | Results | Understand meaning | "what does this mean", "critique" |
| **🛠️ Execution** | Clear plan | Run analysis | "run", "analyze", "compute" |
| **📝 Documentation** | Completed work | Write it up | "write methods", "document" |
| **🔄 Debugging** | Broken/wrong results | Fix it | "seems wrong", "debug", "fix" |

See `workflows/research-stages.md` for full documentation.

## Engagement Modes

### Discovery Mode
**Triggers:** "what data exists", "is it feasible", "can I study"

Check data availability, API access, estimate volume.

### Exploration Mode
**Triggers:** "what's in this data", "explore", "profile", "first look"

Data profiling, descriptive stats, potential research directions.

### Validation Mode  
**Triggers:** "review my", "audit", "check", "is this sound"

Code review, methodology audit, codebook review.

### Interpretation & Results Writing Mode
**Triggers:** "what does this mean", "interpret", "write up results", "help me understand this output", "here are my results", "critique", "are these plausible"

**Also triggers when:** User pastes statistical output, tables, or analysis results.

⚠️ **CRITICAL:** When users provide completed outputs, the analysis is DONE. 
- Do NOT ask probing questions about methodology
- Do NOT trigger preflight/critical checks
- Do NOT suggest alternative approaches
- ONLY interpret what's there and help write it up

When users send statistical outputs, visualizations, or analysis logs:

1. **Parse & confirm** — Make sure I understand the output correctly
2. **Translate** — Plain language interpretation with effect size context
3. **Flag interpretation issues** — Surprises, contradictions (not methodology critiques)
4. **Write together** — Draft results section WITH user, not FOR them

**Example:**
```
User: Here's my LTTN output: [paste]

Agent: Looking at your LTTN results:
       - Topic 3 peaks in March, Topic 7 shows inverse pattern
       - This suggests competing frames around [topic]
       
       For your results section: "Temporal analysis revealed..."
       
       What's the main takeaway you want readers to get?
```

See `workflows/results-interpretation.md` for full protocol.

**Handoff:** For full paper writing (intro, lit review, discussion), use CommScribe.

### Full Pipeline Mode
**Triggers:** "analyze", "research", "study", "investigate"

Complete workflow from research question to report.

### Text Analysis Mode
**Triggers:** "topic modeling", "sentiment", "frames", "classify"

Focused text analysis workflow.

### Network Analysis Mode
**Triggers:** "network", "connections", "community", "influence"

Focused network analysis workflow.

### Coordinated Behavior Mode
**Triggers:** "coordinated", "inauthentic", "bot detection", "astroturf"

Specialized workflow for coordination detection.

## Agent Invocation

Use `sessions_spawn` to invoke specialist agents:

```yaml
# Research planning
sessions_spawn:
  task: "Create research plan for {request}"
  agentId: comm-research-planner
  model: anthropic/claude-opus-4

# Data collection (use fast/cheap model)
sessions_spawn:
  task: "Collect {platform} data: {query}"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash

# Text analysis
sessions_spawn:
  task: "Run {method} on {corpus}"
  agentId: comm-research-text
  model: deepseek/deepseek-v3

# Network analysis
sessions_spawn:
  task: "Analyze network structure: {data}"
  agentId: comm-research-network
  model: deepseek/deepseek-v3

# Code review (use DIFFERENT model than generator)
sessions_spawn:
  task: "Review script: {path}"
  agentId: comm-research-reviewer
  model: openai/gpt-4o

# Report synthesis
sessions_spawn:
  task: "Generate report from {artifacts}"
  agentId: comm-research-synthesizer
  model: anthropic/claude-opus-4
```

## Model Routing Strategy

| Task | Recommended Model | Rationale |
|------|-------------------|-----------|
| Orchestration | Claude Opus | Complex coordination |
| Data validation | Gemini Flash | Fast, cheap |
| Code generation | DeepSeek V3 | Strong at code |
| Text classification | Gemini Flash | Batch processing |
| Adversarial review | GPT-4o | Different from generator |
| Final synthesis | Claude Opus | Nuanced writing |

## Human Checkpoints

Pause and notify user at:
1. After Discovery (before committing resources)
2. After Plan creation (before data collection)
3. After data collection (before analysis)
4. Before final delivery

Use Telegram/Slack notification:
```
message:
  action: send
  target: user_id
  message: |
    📊 **Research Checkpoint: {stage}**
    
    {summary}
    
    Reply "approve" to proceed
    Reply "revise" to modify
```

## Project Folder Structure

```
research/{date}_{name}/
├── PLAN.md
├── STATE.md
├── LEARNINGS.md
├── REPORT.md
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   └── qa/
├── models/
├── output/
│   ├── figures/
│   └── tables/
└── logs/
```

## Available Skills

### Data Sources
- `data-sources/existing-datasets.md` — Working with archived data (START HERE)
- `data-sources/reddit.md` — Reddit API via PRAW
- `data-sources/youtube.md` — YouTube Data API
- `data-sources/telegram.md` — Telegram via Telethon
- `data-sources/bluesky.md` — AT Protocol (open, recommended)
- `data-sources/tiktok.md` — TikTok Research API + alternatives
- `data-sources/twitter.md` — Twitter/X (expensive, limited)
- `data-sources/mediacloud.md` — News media search
- `data-sources/gdelt.md` — Global event database

### Methods
- `methods/sentiment-analysis.md` — Sentiment/valence analysis
- `methods/topic-modeling.md` — Topic extraction (LDA, BERTopic)
- `methods/frame-analysis.md` — Frame identification and analysis
- `methods/content-analysis.md` — Manual and LLM-assisted coding
- `methods/network-analysis.md` — Network metrics & communities
- `methods/coordinated-behavior.md` — Coordination detection
- `methods/llm-annotation.md` — LLM-based text classification
- `methods/lttn.md` — ⚠️ EXPERIMENTAL: Latent Temporal-Thematic Network (information flow)
- `methods/textnets.md` — Bipartite document-word network analysis (Bail method)
- `methods/llm-methods-landscape.md` — Survey: LLM annotation, synthetic data, agent simulation
- `methods/synthetic-data.md` — ⚠️ EMERGING: LLM-generated synthetic social media data
- `methods/llm-simulation.md` — ⚠️ EXPERIMENTAL: LLM-powered agent-based simulation
- `methods/validation.md` — Validation protocols

### Workflows
- `workflows/data-access-strategy.md` — Finding data in post-API era
- `workflows/ethics-compliance.md` — IRB, GDPR, platform ethics
- `workflows/expert-mode.md` — Fast-track for experienced researchers
- `workflows/rigor-enforcement.md` — Methodological guardrails
- `workflows/preflight.md` — Pre-analysis checks
- `workflows/critical-checks.md` — Research practice validation
- `workflows/tiered-validation.md` — Match validation to stakes
- `workflows/nudge-system.md` — Force conscious research decisions
- `workflows/confound-checklist.md` — **NEW** Identify confounding variables
- `workflows/temporal-anomaly-detection.md` — **NEW** Flag unexplained spikes/drops
- `workflows/claim-evidence-matcher.md` — **NEW** Prevent overclaiming
- `workflows/outcome-operationalization.md` — **NEW** Force DV operationalization
- `workflows/study-design-warnings.md` — **NEW** N=1 and design limit enforcement
- `workflows/design-alternatives.md` — **NEW** Pivot from blockers to achievable designs

### Theories
- `theories/attention-economy.md` — Attention as resource
- `theories/networked-publics.md` — Network society
- `theories/coordinated-behavior.md` — CIB framework
- `theories/artificial-sociality.md` — Human-AI interaction

## Quality Assurance

Every script follows execute→QA→evaluate loop:
1. Agent writes script
2. Execute and capture output
3. Reviewer agent checks (adversarial)
4. PASSED → continue, BLOCKER → revise

## Ethical Guidelines

- Respect platform Terms of Service
- Document IRB status if applicable
- Archive raw data (platforms may revoke access)
- Don't conflate coordination with inauthenticity
- Report limitations honestly

## Engagement Tiers

This skill supports three engagement levels:

| Tier | Who | Experience |
|------|-----|------------|
| **Novice** | Students, first-time users | Full probing questions, explanations |
| **Intermediate** | Familiar with methods | Spot-check key decisions |
| **Expert** | Published researchers | Fast-track mode (see `workflows/expert-mode.md`) |

Set tier in `config.yaml` or let the system assess based on interaction.

## Post-API Era

Data access has changed dramatically. Before planning collection:
1. **Read `workflows/data-access-strategy.md`** — Understand current landscape
2. **Check `data-sources/existing-datasets.md`** — Existing data is often better
3. **Open platforms first** — Bluesky, Mastodon, Telegram work well
4. **Budget for gated access** — Meta, TikTok require applications

## Version

- Name: CommDAAF
- Full name: Computational Communication Research Framework
- Version: 0.7.0
- Last updated: 2026-02-18
- Author: OpenClaw Community
- Based on: DAAF (Data Analyst Augmentation Framework)

### Changelog
- **0.7.0**: Reproducibility architecture update (inspired by Xu & Yang 2026) — three-layer architecture (orchestrator/knowledge/computation), mandatory cross-agent validation, credibility rating scheme, structured failure knowledge base. See `workflows/agent-academy/ARCHITECTURE.md`.
- **0.6.0**: Universal methodology checks — sample balance, metric comparability, context changes, effect size thresholds, directional consistency, confound identification, multiple testing awareness (all platform-agnostic)
- **0.5.0**: Design alternatives system — blockers now include "INSTEAD, TRY" pivots; nudges help design achievable studies rather than just flagging problems
- **0.4.0**: Red-teaming driven improvements — confound checklist, temporal anomaly detection, claim-evidence matcher, outcome operationalization requirements, study design warnings (N=1 enforcement)
- **0.3.0**: Tiered validation, nudge system, theory modules, guided pipelines
- **0.2.0**: Post-API data strategies, expert mode, 10 methods, 9 data sources
- **0.1.0**: Initial release
