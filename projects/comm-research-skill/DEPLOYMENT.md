# Communication Research Skill — Deployment Guide

**Two paths, same skill.** Pick your environment.

---

## 🔀 Quick Decision

| You're using... | Go to... |
|-----------------|----------|
| **Claude Code** (Anthropic's CLI) | [Claude Code Setup](#-claude-code-setup) |
| **OpenClaw** (agentic gateway) | [OpenClaw Setup](#-openclaw-setup) |
| **Not sure** | You probably want Claude Code |

---

## 🤖 Claude Code Setup

**Time: ~2 minutes**

Claude Code reads a `CLAUDE.md` file in your project root. We just need to point it to the right files.

### Option A: Minimal (Copy One File)

If you want the simplest possible setup:

```bash
# In your research project folder
curl -O https://raw.githubusercontent.com/openclaw/skills-comm-research/main/CLAUDE_BUNDLE.md
mv CLAUDE_BUNDLE.md CLAUDE.md
```

Done. Claude Code now has the full skill embedded.

### Option B: Full Install (Recommended)

Better for ongoing use — keeps methods as separate files you can browse:

```bash
# 1. Clone the skill into your project
git clone https://github.com/openclaw/skills-comm-research.git .comm-research

# 2. Create CLAUDE.md that references it
cat > CLAUDE.md << 'EOF'
# Communication Research Project

## Research Assistant Instructions

You are a communication research assistant. Before answering research questions, 
read and follow the relevant files in `.comm-research/skill-templates/`.

### Core Files (Read First)
- `.comm-research/skill-templates/SKILL.md` — Main instructions
- `.comm-research/skill-templates/PROBING_QUESTIONS.md` — Required questions

### Methods (Read When Relevant)
- `.comm-research/skill-templates/methods/` — Analysis methods
- `.comm-research/skill-templates/data-sources/` — Platform access guides
- `.comm-research/skill-templates/workflows/` — Process guidance

### My Research Context
<!-- Add your specific context here -->

**Topic:** [Your research topic]
**Data:** [What data you have/need]
**Methods:** [Methods you plan to use]
**Experience level:** [novice/intermediate/expert]
EOF
```

### Option C: Just the Instructions (Ultra-Minimal)

For a quick test without full features:

```bash
cat > CLAUDE.md << 'EOF'
# Research Assistant Mode

When helping with communication research:

1. **Ask before analyzing** — Don't run methods with default parameters
2. **Probe methodology** — Ask about unit of analysis, validation plans, ground truth
3. **Be honest about data** — Twitter costs $5K/mo, Reddit is restricted, recommend existing datasets
4. **Require validation** — Any LLM annotation needs human validation (N≥200)
5. **Multi-model** — Use different models for annotation vs synthesis

## Data Access Reality (2026)

| ✅ Accessible | ⚠️ Application Required | 💰 Expensive |
|---------------|------------------------|--------------|
| Existing datasets | Meta Content Library | Twitter/X ($5K+/mo) |
| Bluesky (open) | TikTok Research API | Reddit (negotiated) |
| Telegram (public) | | |
| YouTube (API key) | | |
| GDELT/MediaCloud | | |

Always suggest existing datasets first.
EOF
```

---

## 🐙 OpenClaw Setup

**Time: ~3 minutes**

OpenClaw has a skills system that auto-loads instructions based on task context.

### Standard Install

```bash
# One-liner install to OpenClaw workspace
curl -sSL https://raw.githubusercontent.com/openclaw/skills-comm-research/main/install.sh | bash
```

Or manually:

```bash
# Clone to skills directory
cd ~/.openclaw/workspace/skills
git clone https://github.com/openclaw/skills-comm-research.git comm-research

# Skill auto-registers via manifest.json
```

### With Zotero Customization

Personalize the skill based on your reading:

```bash
cd ~/.openclaw/workspace/skills/comm-research/zotero

# Get your Zotero user ID from: https://www.zotero.org/settings/keys
# Create API key at: https://www.zotero.org/settings/keys/new

python adapt.py --user-id YOUR_USER_ID --api-key YOUR_API_KEY
```

This analyzes your library and:
- Prioritizes methods you actually use
- Adds theories from papers you've saved
- Customizes examples to your research area

---

## 📁 What's Included

```
skill-templates/
├── SKILL.md                 # 🎯 Main entry (read this first)
├── PROBING_QUESTIONS.md     # ❓ Questions before each method
├── config.yaml              # ⚙️ Your settings
│
├── methods/                 # 🔬 Analysis techniques
│   ├── sentiment-analysis.md
│   ├── topic-modeling.md
│   ├── frame-analysis.md
│   ├── content-analysis.md
│   ├── network-analysis.md
│   ├── coordinated-behavior.md
│   ├── llm-annotation.md
│   ├── textnets.md
│   ├── validation.md
│   └── lttn.md (experimental)
│
├── data-sources/            # 📊 Platform guides
│   ├── existing-datasets.md # ⭐ Start here
│   ├── bluesky.md
│   ├── telegram.md
│   ├── youtube.md
│   └── ...
│
├── workflows/               # 🔄 Process guides
│   ├── data-access-strategy.md
│   ├── ethics-compliance.md
│   ├── expert-mode.md
│   └── research-stages.md
│
└── zotero/                  # 📚 Library integration
    └── adapt.py
```

---

## ⚡ Quick Test

After setup, try:

```
Analyze sentiment in climate change discourse on Bluesky
```

**Expected behavior:**

If configured correctly, your assistant should:
1. Ask probing questions (not just run analysis)
2. Ask about unit of analysis (post? thread? user?)
3. Ask how you'll validate (human sample?)
4. Mention sarcasm detection for climate content

If it just runs sentiment analysis with defaults → setup isn't working.

---

## 🎚️ Configuration

### Set Your Experience Level

In Claude Code (`CLAUDE.md`):
```markdown
**Experience level:** expert
**Methods I'm competent in:** sentiment-analysis, topic-modeling
```

In OpenClaw (`config.yaml`):
```yaml
engagement_tier: expert  # novice | intermediate | expert
verified_competencies:
  - sentiment-analysis
  - topic-modeling
```

**What this changes:**
- **Novice**: Full probing questions, explanations, guardrails
- **Intermediate**: Spot-check questions, trust explicit parameters
- **Expert**: Fast-track, minimal interruption if specs complete

---

## 🔑 API Keys (Optional)

Only needed if collecting new data (not using existing datasets):

```bash
# .env file in your project
YOUTUBE_API_KEY=...
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
TELEGRAM_API_ID=...
TELEGRAM_API_HASH=...
MEDIACLOUD_API_KEY=...
```

---

## 🆘 Troubleshooting

### "Claude isn't asking probing questions"

- Check `CLAUDE.md` exists in your project root
- Verify the file references are correct (Option B)
- Try restarting Claude Code: `/clear` then re-ask

### "OpenClaw doesn't see the skill"

```bash
# Check skill is registered
cat ~/.openclaw/workspace/skills/comm-research/manifest.json

# Should show:
# "name": "comm-research"
# "description": "..."
```

### "Methods feel too basic"

You might be in expert mode. To get full guidance:
- Remove yourself from `verified_competencies`
- Set `engagement_tier: novice`

---

## 🔄 Updates

### Claude Code
```bash
cd .comm-research && git pull
```

### OpenClaw
```bash
cd ~/.openclaw/workspace/skills/comm-research && git pull
```

---

## 📖 Next Steps

1. **Browse methods** — Read the ones relevant to your research
2. **Check data-sources** — Understand what's actually accessible
3. **Run a test** — Try one analysis and see how it guides you
4. **Customize** — Edit `config.yaml` or `CLAUDE.md` for your needs

---

*Questions? Open an issue or check the main [README.md](README.md)*
