# Communication Research Analyst Skill for OpenClaw

An AI-assisted research framework for computational communication science.

## What is This?

This is an OpenClaw skill package that enables autonomous research workflows for communication scholars doing computational social science. Inspired by [DAAF](https://github.com/DAAF-Contribution-Community/daaf), but adapted for:

- **Social media data** (Reddit, YouTube, Telegram, Bluesky)
- **News media data** (MediaCloud, GDELT, Internet Archive)
- **Communication-specific methods** (coordinated behavior detection, network analysis, topic modeling)
- **Multi-model architecture** (cost-effective, epistemically diverse)

## Why This Over DAAF?

| Feature | DAAF | This Package |
|---------|------|--------------|
| Platform | Claude Code CLI | OpenClaw |
| Model | Claude only | Any model (OpenRouter) |
| Cost | ~$30-60/analysis | ~$5-15/analysis |
| Data focus | Education (Urban Institute) | Communication/media |
| Notification | Terminal | Telegram/Slack |
| Extensibility | Manual | Zotero-informed |

### Key Selling Point: Multi-Model Architecture

Route different tasks to different models:

- **Complex reasoning** → Claude Opus
- **Data validation** → Gemini Flash (100x cheaper)
- **Code generation** → DeepSeek V3
- **Adversarial review** → Different model than generator (epistemic diversity)

This isn't just cheaper—it's methodologically better. Different models catch different issues.

## Quick Start

### Option 1: Standard Install
```bash
cd skill-templates
./install.sh
```

### Option 2: Zotero-Customized Install
```bash
# 1. Install base skill
cd skill-templates
./install.sh

# 2. Customize for your research domain
cd zotero
python adapt.py --user-id YOUR_ZOTERO_ID --api-key YOUR_API_KEY

# 3. Copy customized skills
cp -r generated/* ~/.openclaw/workspace/skills/comm-research/
```

### Configure API Keys
Add to OpenClaw config or environment:
- Reddit: PRAW credentials
- YouTube: Google API key  
- Telegram: API ID/Hash from my.telegram.org
- OpenRouter: API key for model routing

### Start Researching
```
User: Analyze coordinated messaging on Telegram pro-government channels during [event]

Agent: [Invokes discovery → planning → collection → analysis → report workflow]
```

## Project Structure

```
comm-research-skill/
├── README.md                    # This file
├── SPEC_DRAFT.md               # Full specification (~9000 words)
├── ZOTERO_ANALYSIS.md          # Example library analysis
├── RESEARCH_NOTES.md           # Development notes
│
└── skill-templates/            # Actual skill files
    ├── SKILL.md                # Main entry point
    ├── agents/
    │   ├── orchestrator.md     # Workflow coordinator
    │   └── code-reviewer.md    # Adversarial QA
    ├── data-sources/
    │   └── telegram.md         # Telegram collection
    └── methods/
        └── coordinated-behavior.md  # Coordination detection
```

## Supported Workflows

### Full Pipeline
Research question → Data collection → Analysis → Report

### Discovery Mode
"What data exists for studying X?"

### Text Analysis
Topic modeling, sentiment, LLM annotation

### Network Analysis
Opinion leadership, community detection, diffusion

### Coordinated Behavior
Detect and analyze coordinated activity across platforms

## Data Sources

| Source | API | Status |
|--------|-----|--------|
| Reddit | PRAW | ✅ Open |
| YouTube | Data API v3 | ✅ Open |
| Telegram | Telethon | ✅ Open |
| Bluesky | AT Protocol | ✅ Open |
| MediaCloud | REST API | ✅ Open |
| GDELT | BigQuery | ✅ Open |
| TikTok | Research API | ⚠️ Application required |
| Twitter/X | - | ❌ Expensive |

## Methods

- **Coordinated Behavior Detection** — Per Giglietto et al., Kuznetsova
- **Network Analysis** — Opinion leadership, communities, diffusion
- **LLM-Based Annotation** — Zero/few-shot classification with validation
- **Topic Modeling** — LDA, BERTopic
- **Attention Metrics** — Engagement, virality, distribution

## Novel Feature: Zotero Adapter

Connect your Zotero library, and the system **auto-generates domain-specific skills** based on your readings.

### How It Works

```bash
cd skill-templates/zotero
python adapt.py --user-id YOUR_ID --api-key YOUR_KEY --output-dir ./my-skills/
```

The adapter:
1. **Fetches** your library via Zotero API
2. **Analyzes** titles, abstracts, and tags
3. **Detects** methods, theories, platforms, and topics
4. **Generates** customized skill files prioritized for YOUR research

### What It Detects

| Category | Examples |
|----------|----------|
| **Methods** | Network analysis, topic modeling, LLM annotation, coordinated behavior |
| **Theories** | Attention economy, networked publics, framing, artificial sociality |
| **Platforms** | Twitter, Reddit, Telegram, YouTube, TikTok, Bluesky |
| **Topics** | Misinformation, polarization, health communication, political communication |

### Output

```
my-skills/
├── README.md           # Your research profile
├── config.json         # Customized priorities
├── methods/
│   ├── network-analysis.md      # Customized for your use cases
│   ├── coordinated-behavior.md
│   └── llm-annotation.md
└── theories/
    ├── attention-economy.md
    └── artificial-sociality.md
```

### Why This Matters

- **No manual configuration** — skills auto-adapt to your domain
- **Prioritized workflows** — focus on what you actually research
- **Consistent with your literature** — citations and concepts from your library
- **Publishable methodology** — can document "skill was customized based on researcher's N papers"

## Documentation

- **Full Specification**: [SPEC_DRAFT.md](./SPEC_DRAFT.md)
- **Zotero Analysis Example**: [ZOTERO_ANALYSIS.md](./ZOTERO_ANALYSIS.md)
- **Skill Templates**: [skill-templates/](./skill-templates/)

## Theoretical Foundations

This skill integrates communication theory:

- **Attention Economy** (Simon) — Attention as scarce resource
- **Networked Publics** (Castells, boyd) — Network-mediated public spheres
- **Coordinated Behavior** (Giglietto) — Detecting coordination patterns
- **Artificial Sociality** — Human-AI interaction dynamics

## For the Academic Community

This project is designed to be:

1. **Publishable** — Clear methodology, reproducible
2. **Teachable** — Usable in methods courses
3. **Extensible** — Add your own skills
4. **Affordable** — Multi-model cost optimization

## Contributing

This is an open framework. Contributions welcome:

- New data source skills
- New analysis methods
- Theory integrations
- Bug fixes and improvements

## License

MIT License — Use freely, cite if helpful.

## Citation

```bibtex
@software{comm_research_skill,
  title={Communication Research Analyst Skill for OpenClaw},
  author={OpenClaw Community},
  year={2026},
  url={https://github.com/...}
}
```

---

*Built with OpenClaw. Inspired by DAAF. Made for communication scholars.*
