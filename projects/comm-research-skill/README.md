# CommDAAF

**Computational Communication Research Framework**

**Version 0.3.0** | Tiered Validation | Nudge System | Theory Integration

An AI-assisted research framework for computational communication science — built for the reality of 2026, not the assumptions of 2020.

*Adapted from [DAAF](https://github.com/DAAF-Contribution-Community/daaf) for communication scholars.*

---

## What's New in v0.3

| Feature | Description |
|---------|-------------|
| **🎚️ Tiered Validation** | 🟢 Exploratory (30 min) → 🟡 Pilot (4 hrs) → 🔴 Publication (2 days) |
| **🧠 Nudge System** | Conscious research design — no silent defaults |
| **📚 Theory Modules** | Gatekeeping, agenda-setting, networked publics, diffusion |
| **🔄 Guided Pipelines** | End-to-end workflows with time estimates |
| **🎯 Stage Detection** | Auto-detect Discovery → Development → Interpretation |

---

## What's Different About This?

### The Problem

Most AI research tools assume you can just "collect data from Twitter" or "scrape Reddit." That era is over:

| Platform | Reality (2026) |
|----------|---------------|
| Twitter/X | $5,000/month minimum |
| Reddit | API restricted, expensive |
| Meta | Gated (6-12 week wait) |
| TikTok | Application required |
| Instagram | Effectively inaccessible |

### Our Solution

This skill is designed for the **post-API era**:

1. **Existing datasets first** — Most research uses archived data, and that's fine
2. **Open platforms prioritized** — Bluesky, Mastodon, Telegram work great
3. **Realistic access guidance** — Honest about what you can/can't get
4. **Alternative pathways** — DSA Article 40, data donations, partnerships

---

## Key Features

### 🎯 Rigor Enforcement

We don't just run your analysis — we make sure you've thought it through:

- **Probing questions** for every method (sentiment, topics, networks, frames, etc.)
- **Competence verification** before complex methods
- **No silent defaults** — every parameter requires explicit choice
- **Escalation protocol** — gentle probe → explain → challenge → refuse

### ⚡ Expert Mode

Experienced researchers shouldn't be interrogated:

```
# Expert fast-track request
Sentiment: tweets_climate.csv, VADER, post-level, 
neutral ±0.05, LLM sarcasm prefilter, 200-item validation

# System response
✅ Parameters complete. Proceeding.
```

Set `engagement_tier: expert` in config or demonstrate competence once per method.

### 🔬 Multi-Model Validation

Different models catch different issues (epistemic diversity):

| Task | Model | Why |
|------|-------|-----|
| Orchestration | Claude Opus | Complex reasoning |
| Bulk annotation | Gemini Flash | Cost (100x cheaper) |
| Code review | GPT-4o | Different from generator |
| Synthesis | Claude Opus | Nuanced writing |

### 📚 Zotero Integration

Auto-customize skills based on your reading:

```bash
python adapt.py --user-id YOUR_ID --api-key YOUR_KEY
```

The adapter analyzes your library and prioritizes methods you actually use.

---

## Methods Supported

| Method | Probing Questions | Validation Required |
|--------|-------------------|---------------------|
| **Sentiment Analysis** | 6 questions | Human sample (N≥200) |
| **Topic Modeling** | 7 questions | Coherence + human interpretation |
| **Frame Analysis** | 5 questions | Inter-coder reliability (κ≥0.7) |
| **Network Analysis** | 5 questions | Theoretical justification |
| **Content Analysis** | 6 questions | 2+ coders, reliability |
| **Coordinated Behavior** | 5 questions (strict) | Baseline comparison |
| **LLM Annotation** | 4 questions | Human validation (κ≥0.7) |

---

## Data Sources

### ✅ Recommended (Actually Work)

| Source | Access | Notes |
|--------|--------|-------|
| **Existing Datasets** | Free | Start here — Harvard Dataverse, ICPSR, Zenodo |
| **Bluesky** | Open | No auth, no limits, growing community |
| **Telegram** | Open | Public channels, need account |
| **YouTube** | API key | Works, quota limits |
| **GDELT** | Open | Global news events |
| **MediaCloud** | API key | News coverage |

### ⚠️ Requires Application

| Source | Wait Time | Notes |
|--------|-----------|-------|
| **Meta Content Library** | 6-12 weeks | Facebook/Instagram public data |
| **TikTok Research API** | 4-8 weeks | Limited, US/EU researchers |

### 💰 Expensive

| Source | Cost | Notes |
|--------|------|-------|
| **Twitter/X** | $5K+/mo | Consider alternatives |
| **Reddit** | Negotiated | Limited unless paying |

---

## Quick Start

### 1. Install

```bash
cd skill-templates
./install.sh
```

### 2. Configure

Edit `config.yaml`:
- Set your `engagement_tier` (novice/intermediate/expert)
- Mark which platforms you actually have access to
- List methods you're already competent in

### 3. Use

```
User: Analyze framing of climate coverage in Bluesky posts

Agent: Before I proceed, I need to understand your approach...
       [Probing questions if novice/intermediate]
       
       [OR if expert with specs provided:]
       ✅ Parameters complete. Running frame analysis pipeline.
```

---

## Project Structure

```
comm-research-skill/
├── README.md                     # This file
├── CRITICAL_AUDIT.md            # Honest assessment of gaps
├── EXPANSION_IDEAS.md           # Future features
│
└── skill-templates/             # Skill package
    ├── SKILL.md                 # Main entry point
    ├── ONBOARDING.md            # How to customize
    ├── PROBING_QUESTIONS.md     # All required questions
    │
    ├── data-sources/
    │   ├── existing-datasets.md # START HERE
    │   ├── bluesky.md
    │   ├── tiktok.md
    │   ├── twitter.md           # (expensive, documented)
    │   └── ...
    │
    ├── methods/
    │   ├── sentiment-analysis.md
    │   ├── topic-modeling.md
    │   ├── frame-analysis.md
    │   ├── content-analysis.md
    │   ├── network-analysis.md
    │   ├── coordinated-behavior.md
    │   ├── llm-annotation.md
    │   └── validation.md
    │
    ├── workflows/
    │   ├── data-access-strategy.md  # Post-API guidance
    │   ├── ethics-compliance.md     # IRB/GDPR/DSA
    │   ├── expert-mode.md           # Fast-track
    │   └── rigor-enforcement.md     # Methodological guardrails
    │
    └── zotero/                  # Library adapter
        ├── adapt.py
        ├── extractor.py
        └── generator.py
```

---

## Why CommDAAF Over DAAF?

| Feature | DAAF | CommDAAF |
|---------|------|--------------|
| **Era** | API-centric | Post-API aware |
| **Data reality** | Assumes collection | Prioritizes existing datasets |
| **Rigor** | Trust user | Enforce methodology |
| **Expertise** | One-size-fits-all | Tiered engagement |
| **Models** | Single model | Multi-model (epistemic diversity) |
| **Cost** | ~$30-60/analysis | ~$5-15/analysis |
| **Domain** | General data | Communication research |
| **Ethics** | Basic | IRB/GDPR/DSA guidance |

---

## Philosophy

### This Tool Will:
- ✅ Push back on vague requests
- ✅ Ask probing questions
- ✅ Require explicit parameter choices
- ✅ Validate your understanding of methods
- ✅ Generate publication-ready documentation

### This Tool Won't:
- ❌ Run analysis with silent defaults
- ❌ Let you claim "bots" from coordination patterns
- ❌ Skip human validation for LLM annotations
- ❌ Pretend you can easily collect Twitter data
- ❌ Treat single-coder content analysis as valid

---

## For the Academic Community

This project is designed to be:

1. **Honest** — About data access realities
2. **Rigorous** — Methods standards enforced
3. **Teachable** — Usable in methods courses
4. **Affordable** — Multi-model cost optimization
5. **Ethical** — IRB/GDPR/DSA guidance built-in

---

## Contributing

Contributions welcome:
- New data source skills (especially for emerging platforms)
- New analysis methods
- Improved probing questions
- Translations of ethics/compliance for non-US contexts

---

## Citation

```bibtex
@software{commdaaf,
  title={CommDAAF: Computational Communication Research Framework},
  author={OpenClaw Community},
  version={0.2.0},
  year={2026},
  url={https://github.com/openclaw/commdaaf},
  note={Post-API era computational communication research framework, adapted from DAAF}
}
```

---

## License

MIT License — Use freely, cite if helpful.

---

*Built for how research actually works in 2026, not how we wish it worked.*
