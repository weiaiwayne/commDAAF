# Communication Research Analyst Skill

An OpenClaw skill package for computational communication research.

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

## Engagement Modes

### Discovery Mode
**Triggers:** "what data exists", "is it feasible", "can I study"

Check data availability, API access, estimate volume.

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
- `methods/validation.md` — Validation protocols

### Workflows
- `workflows/data-access-strategy.md` — Finding data in post-API era
- `workflows/ethics-compliance.md` — IRB, GDPR, platform ethics
- `workflows/expert-mode.md` — Fast-track for experienced researchers
- `workflows/rigor-enforcement.md` — Methodological guardrails
- `workflows/preflight.md` — Pre-analysis checks
- `workflows/critical-checks.md` — Research practice validation

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

- Skill version: 0.2.0
- Last updated: 2026-02-17
- Author: OpenClaw Community
