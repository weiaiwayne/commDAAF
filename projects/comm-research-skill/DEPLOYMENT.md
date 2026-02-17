# CommDAAF — Deployment Guide

**Computational Communication Research Framework**

Three platforms, same rigor. Pick yours.

---

## 🔀 Quick Decision

| Platform | Install Time | Best For |
|----------|--------------|----------|
| [**Claude Code**](#-claude-code) | 1 min | Anthropic CLI users |
| [**OpenClaw**](#-openclaw) | 2 min | Agentic gateway users |
| [**Antigravity**](#-google-antigravity) | 2 min | Google IDE users |

---

## 🤖 Claude Code

Claude Code reads `CLAUDE.md` in your project root.

### Option A: One-File Bundle (Fastest)

```bash
curl -O https://raw.githubusercontent.com/openclaw/commdaaf/main/CLAUDE_BUNDLE.md
mv CLAUDE_BUNDLE.md CLAUDE.md
```

Done. Full skill embedded in one file.

### Option B: Full Install (Recommended)

```bash
# Clone CommDAAF
git clone https://github.com/openclaw/commdaaf.git .commdaaf

# Create CLAUDE.md that references it
cat > CLAUDE.md << 'EOF'
# CommDAAF Research Project

Read and follow `.commdaaf/skill-templates/SKILL.md` for all research tasks.
Load method files from `.commdaaf/skill-templates/methods/` when relevant.

## My Research
**Topic:** [Your topic]
**Methods:** [Your methods]
**Experience:** [novice/intermediate/expert]
EOF
```

### Option C: Minimal Instructions

```bash
cat > CLAUDE.md << 'EOF'
# Research Assistant Rules

1. Ask probing questions before any analysis
2. Never use default parameters without confirmation
3. Be honest: Twitter=$5K/mo, Reddit=restricted, use existing datasets
4. LLM annotations need human validation (N≥200)
5. Never conclude "bots" from behavioral similarity alone
EOF
```

---

## 🐙 OpenClaw

OpenClaw has a skills system that auto-loads based on task.

### Standard Install

```bash
curl -sSL https://raw.githubusercontent.com/openclaw/commdaaf/main/install.sh | bash
```

Or manually:

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/openclaw/commdaaf.git
```

### With Zotero Customization

```bash
cd ~/.openclaw/workspace/skills/commdaaf/zotero
pip install pyzotero
python adapt.py --user-id YOUR_ZOTERO_ID --api-key YOUR_API_KEY
```

### Verify Installation

```bash
cat ~/.openclaw/workspace/skills/commdaaf/manifest.json | grep name
# Should show: "name": "commdaaf"
```

---

## 🚀 Google Antigravity

Antigravity uses directory-based skills with YAML frontmatter.

### Global Install (All Projects)

```bash
cd ~/.gemini/antigravity/skills
git clone https://github.com/openclaw/commdaaf.git
cd commdaaf && cp -r antigravity/* . && rm -rf antigravity skill-templates
```

### Project Install (Single Project)

```bash
mkdir -p .agent/skills
cd .agent/skills
git clone https://github.com/openclaw/commdaaf.git
cd commdaaf && cp -r antigravity/* . && rm -rf antigravity skill-templates
```

### Verify Installation

Ask Antigravity:
```
Run topic modeling on my dataset
```

If working, it should ask probing questions about K, preprocessing, validation.

---

## 📁 What's Included

### Methods (10)

| Method | File | Key Requirement |
|--------|------|-----------------|
| Sentiment Analysis | `sentiment-analysis.md` | Sarcasm strategy |
| Topic Modeling | `topic-modeling.md` | K justification |
| Frame Analysis | `frame-analysis.md` | Frame typology |
| Network Analysis | `network-analysis.md` | Node/edge definition |
| Coordinated Behavior | `coordinated-behavior.md` | Baseline comparison |
| Content Analysis | `content-analysis.md` | Codebook + reliability |
| LLM Annotation | `llm-annotation.md` | Human validation |
| TextNets | `textnets.md` | Bipartite setup |
| Validation | `validation.md` | Protocols |
| LTTN | `lttn.md` | ⚠️ Experimental |

### Data Sources (9)

| Source | Status | Notes |
|--------|--------|-------|
| **Existing Datasets** | ⭐ Recommended | Harvard Dataverse, ICPSR, Zenodo |
| **Bluesky** | ✅ Open | No auth, no limits |
| **Telegram** | ✅ Works | Public channels |
| **YouTube** | ✅ Works | API key, quotas |
| **GDELT** | ✅ Open | News/events |
| **MediaCloud** | ✅ Works | News coverage |
| **TikTok** | ⚠️ Application | 4-8 weeks |
| **Meta** | ⚠️ Application | 6-12 weeks |
| **Twitter/X** | 💰 $5K+/mo | Usually unavailable |

---

## ⚡ Quick Test

After any installation, try:

```
Analyze sentiment in climate change posts
```

**Expected behavior:**

✅ Asks about construct (valence? emotions? stance?)  
✅ Asks about unit of analysis  
✅ Asks about sarcasm strategy (climate = high sarcasm)  
✅ Asks about validation plan  

❌ If it just runs VADER with defaults → setup not working

---

## 🎚️ Experience Levels

Set your level to adjust how much the system probes:

| Level | Experience |
|-------|-----------|
| **Novice** | Full probing questions, explanations |
| **Intermediate** | Spot-check key decisions |
| **Expert** | Fast-track if specs complete |

**Expert fast-track example:**
```
Sentiment: climate_tweets.csv, VADER + LLM sarcasm prefilter, 
post-level, neutral ±0.05, 200-item validation planned
```

Response: `✅ Parameters complete. Proceeding.`

---

## 🔄 Updates

### Claude Code
```bash
cd .commdaaf && git pull
```

### OpenClaw
```bash
cd ~/.openclaw/workspace/skills/commdaaf && git pull
```

### Antigravity
```bash
cd ~/.gemini/antigravity/skills/commdaaf && git pull
# OR for project-level:
cd .agent/skills/commdaaf && git pull
```

---

## 📖 More Info

- [Full README](README.md) — Feature details, philosophy
- [CRITICAL_AUDIT.md](CRITICAL_AUDIT.md) — Honest assessment of gaps
- [EXPANSION_IDEAS.md](EXPANSION_IDEAS.md) — Future roadmap

---

*Built for how research actually works in 2026.*
