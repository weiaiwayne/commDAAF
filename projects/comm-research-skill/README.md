# CommDAAF

**Computational Communication Research Framework** | v1.0.0

A methodological skill pack for AI-assisted computational social science research, adapted from [DAAF](https://github.com/DAAF-Contribution-Community/daaf) and tailored for communication scholars.

**Sister project: [CommScribe](https://github.com/weiaiwayne/commscribe)** — While CommDAAF handles data analysis, CommScribe handles literature review, theory building, and scholarly writing with voice learning.

---

## What Is This?

CommDAAF is a set of structured instructions ("skills") that help AI coding assistants support computational communication research. Rather than treating AI as a magic analysis machine, CommDAAF enforces methodological rigor by:

- **Asking probing questions** before running any analysis
- **Refusing to use default parameters** without explicit justification
- **Requiring validation** at levels appropriate to your stakes
- **Connecting methods to communication theory**
- **Being honest about data access** in the post-API era

The goal is not to automate research, but to create a collaborator that pushes back on sloppy methodology.

---

## Key Features

### Tiered Validation

Not every analysis needs publication-grade rigor. CommDAAF lets you choose:

| Tier | Time | Use Case |
|------|------|----------|
| 🟢 Exploratory | 30-60 min | Hypothesis generation, learning a method |
| 🟡 Pilot | 2-4 hours | Committee presentation, working paper |
| 🔴 Publication | 1-2 days | Journal submission, dissertation |

Validation requirements scale accordingly.

### Nudge System

Every methodological choice is surfaced, not hidden:

1. **Default Danger Flags** — Warns when you're about to accept untested defaults
2. **Active Choice Requirement** — Forces explicit selection between alternatives
3. **Trade-Off Visualization** — Shows what you gain and lose with each choice
4. **Assumption Audit** — Surfaces hidden assumptions before analysis
5. **Reflection Checkpoints** — Pauses for metacognition at key stages

### Methods Included

| Method | Description |
|--------|-------------|
| Sentiment Analysis | VADER, LLM, sarcasm detection |
| Topic Modeling | LDA, BERTopic, K-selection |
| Frame Analysis | Entman framework, inductive/deductive |
| Network Analysis | Centrality, community detection |
| Coordinated Behavior | Timing similarity, network patterns |
| Content Analysis | Codebook development, reliability |
| LLM Annotation | Multi-model validation |

### Post-API Data Strategies

The era of free Twitter APIs is over. CommDAAF is honest about what data you can actually get:

| Platform | Status (2026) | Strategy |
|----------|---------------|----------|
| Twitter/X | $5K+/month | Existing datasets, Wayback Machine |
| Reddit | Restricted | Archives, limited API |
| Bluesky | Open | Recommended alternative |
| Meta | Gated | Application required (6-12 weeks) |

---

## Deployment

CommDAAF works with three AI coding platforms. Pick yours:

### Claude Code (Anthropic CLI)

```bash
curl -O https://raw.githubusercontent.com/weiaiwayne/commDAAF/main/CLAUDE_BUNDLE.md
mv CLAUDE_BUNDLE.md CLAUDE.md
```

### OpenClaw

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/weiaiwayne/commDAAF.git commdaaf
```

### Google Antigravity

```bash
cd ~/.gemini/antigravity/skills
git clone https://github.com/weiaiwayne/commDAAF.git
cd commDAAF && cp -r antigravity/* . && rm -rf antigravity skill-templates
```

### Quick Test

After installation, try:

```
Analyze sentiment in climate change discourse on Bluesky
```

If working correctly, the assistant should ask probing questions about what you mean by "sentiment," your unit of analysis, and your validation plan. If it just runs VADER with defaults, the setup isn't working.

---

## Project Structure

```
commDAAF/
├── CLAUDE_BUNDLE.md          # One-file version for Claude Code
├── DEPLOYMENT.md             # Detailed setup instructions
├── skill-templates/          # OpenClaw version
│   ├── SKILL.md              # Main entry point
│   ├── methods/              # 10+ method skills
│   ├── data-sources/         # Platform access guides
│   ├── workflows/            # Validation, ethics, stages
│   └── theories/             # Communication theory modules
└── antigravity/              # Google Antigravity version
```

---

## Citation

```bibtex
@software{commdaaf,
  title={CommDAAF: Computational Communication Research Framework},
  author={Xu, Wayne and LampBotics AI Lab},
  year={2026},
  url={https://github.com/weiaiwayne/commDAAF},
  license={GPL-3.0},
  note={Experimental. Adapted from DAAF.}
}
```

---

## Heritage: DAAF

CommDAAF adapts the [Data Analyst Augmentation Framework (DAAF)](https://github.com/DAAF-Contribution-Community/daaf), originally developed for education data analysis.

| DAAF | CommDAAF |
|------|----------|
| Education data focus | Communication/social media focus |
| Assumes API access | Post-API era strategies |
| General validation | Tiered validation (🟢/🟡/🔴) |
| Trust-based | Nudge system (forces conscious choices) |
| Single platform | Claude Code + OpenClaw + Antigravity |

---

## ⚠️ Experimental Software

This framework is under active development at the [LampBotics AI Lab](https://lampbotics.com). Built concurrently by Kimi K2.5 and Claude Opus 4.5 as an experiment in AI-assisted research tool development.

**Use with caution.** Things may break, documentation may be incomplete.

---

# 🎓 AgentAcademy: Multi-Model Validation

An incubator where AI agents learn from mistakes through adversarial peer review. Multiple models independently analyze the same data, then cross-review each other. **Errors become lessons; lessons become new framework checks.**

**Live dashboard:** [AgentAcademy](https://vineanalyst.lampbotics.com/vineanalyst/commdaaf/agentacademy)

---

## Recent Updates

### 🚀 v1.0.0: HILAR Protocol + Adversarial Review (Mar 2026)

**Major framework release** with formalized human-AI research governance:

| Feature | Description |
|---------|-------------|
| **HILAR Protocol** | Human-in-the-Loop Agentic Research — formalizes how AI agents operate under human authority with explicit approval gates |
| **Adversarial Peer Review** | Mandatory multi-model "Reviewer 2" critiques before finalizing 🟡/🔴 tier studies |
| **Frame-Specific Reliability** | Report agreement per frame, not just aggregate κ — flags unreliable constructs |
| **Model Bias Detection** | Multi-model triangulation to detect systematic model-specific bias (>15% deviation flagged) |

**Wikipedia Epistemic Injustice Study:**
- 100 articles (Iran + Gaza clusters), 28K revisions, 1.6M talk page chars
- 6 forms of epistemic injustice operationalized
- 3-model validation: 80-100% agreement (vs 55-75% with 2 models)
- Preprint: "Whose History? Epistemic Contestation in Wikipedia"

**AgentAcademy NSF HNDS-I Architecture:**
- Registry, benchmarks, and lessons data structures
- Designed for scalable multi-model validation studies

---

### 📄 v0.9.0: Preprints + AgentAcademy Protocol (Feb 27, 2026)

**Two preprints** from the #MahsaAmini virality study, plus a comprehensive protocol for future agentic studies:

| Document | Description |
|----------|-------------|
| [`PREPRINT_FRAMING_VIRALITY.pdf`](projects/virality-study-2026/PREPRINT_FRAMING_VIRALITY.pdf) | **Theory paper**: "Information Over Emotion?" — INFORMATIONAL framing (IRR=2.72) outperforms emotional frames in crisis contexts. Proposes information-scarcity hypothesis. |
| [`PREPRINT_AGENTIC_METHODS.pdf`](projects/virality-study-2026/PREPRINT_AGENTIC_METHODS.pdf) | **Methods paper**: "Toward Agentic Content Analysis" — Reflexive account of human-AI collaborative research. Introduces CommDAAF framework, catalogs failures, extracts 10 practices. |
| [`agent-academy-study-protocol.md`](agent-academy-study-protocol.md) | **Internal protocol**: Step-by-step guide for AgentAcademy studies. Mandatory reading before any multi-model coding study. |

**New subskills added (v0.6):**
- **Literature Synthesis** — Semantic Scholar + OpenAlex search, citation networks, gap analysis
- **Multimodal Coder** — Image frames, image-text relationships, video keyframes

**Key lessons encoded in protocol:**
- Kimi batch limit: 25 posts max (JSON truncation otherwise)
- Mandatory distribution diagnostics before regression
- Frame-specific reliability reporting required
- Never use OLS on skewed engagement data

---

### 🔧 v0.8.0: Iran Study → Skill Improvements (Feb 26, 2026)

**This study demonstrates the AgentAcademy improvement loop: Run research → Find gaps → Fix framework.**

Analyzed 262 Iran news headlines (GDELT, Jan 2024 – Feb 2026) with 3-model validation. Study worked—but exposed 5 methodology gaps that became skill updates:

| Gap Found During Study | Fix Added to CommDAAF |
|------------------------|----------------------|
| Duplicate headlines in sample | Pre-sampling deduplication protocol |
| No MIXED frame option | Multi-label coding (PRIMARY + SECONDARY) |
| "Strike back" vs "negotiate" coded same | Valence dimension required |
| No temporal breakdown | Segmentation for >30 day studies |
| Unclear single vs multi-model QC | Explicit distinction documented |

**Key research finding:** Israeli sources frame Iran as THREAT 10x more than Al Jazeera (42% vs 4%). All 5 hypotheses supported with 78% 3-model agreement.

📄 **Full report:** [`studies/2026-02-26-iran-agenda.md`](antigravity/studies/2026-02-26-iran-agenda.md)

### v0.7.0: Reproducibility Architecture (Feb 18, 2026)

Three-layer architecture, mandatory cross-agent validation, credibility rating scheme, and structured failure knowledge base. Inspired by [Xu & Yang (2026)](https://yiqingxu.org/papers/2026_ai/AI_reproducibility.pdf).

---

## Completed Studies

| Study | Dataset | Key Finding | Validation |
|-------|---------|-------------|------------|
| **📄 #MahsaAmini Virality** 🆕 | 380 tweets | INFORMATIONAL > emotional frames (IRR=2.72) → **2 preprints** | ✅ 3-model |
| **🔧 Iran Agenda-Setting** | 262 headlines | Israeli THREAT 10x > Al Jazeera → **v0.8 skill updates** | ✅ 3-model |
| **China TikTok** | 2K videos, 48K comments | 60x engagement disparity; state media premium | ✅ 3-model |
| **Xinjiang Cotton** | 92K tweets | Dual-sided coordination; pro-Uyghur 2x engagement | ✅ 3-model |
| **#StandWithBelarus** | 96K tweets | 38% Thai = Milk Tea Alliance solidarity, not bots | ✅ 3-model |
| **Ukraine Dam Crisis** | 266K tweets | Cuban state media unexpectedly prominent | ✅ 3-model |
| **#KashmirWithModi** | 99K tweets | Coordinated campaign: 70% pro-gov, copy-paste | ✅ 3-model |
| **CNN 2015 Coverage** | 983 articles | 87-94% law enforcement mentions | ✅ 3-model |
| **#EndSARS Nigeria** | 300K tweets | Elite accounts drove visibility | ✅ 2-model |
| **LLM Content Filtering** | API tests | Filtering at API layer, not model weights | ✅ 3-model |

---

## Chinese LLM Content Filtering Study (Feb 2026)

> **STATUS: HYPOTHESIS DISPROVEN**
>
> Controlled testing confirms: **Academic methodology framing does NOT bypass Chinese LLM content filters.** Both z.ai (GLM) and Moonshot (Kimi) block sensitive content regardless of CommDAAF wrapper.
>
> Previous apparent "bypass" was due to OpenCode's free proxy infrastructure, not prompt engineering.

| Test | API | Result |
|------|-----|--------|
| Direct sensitive prompt | z.ai GLM | ❌ BLOCKED |
| CommDAAF-wrapped | z.ai GLM | ❌ BLOCKED |
| Direct sensitive prompt | Kimi | ❌ BLOCKED |
| CommDAAF-wrapped | Kimi | ❌ BLOCKED |
| Via OpenCode free proxy | Any | ✅ WORKED |

📄 **Final study:** [`papers/CENSORSHIP_STUDY_FINAL.md`](skill-templates/workflows/agent-academy/papers/CENSORSHIP_STUDY_FINAL.md)

---

## Contributing

Contributions welcome:

- Bug reports and issues
- New method skills
- Improved probing questions
- Additional theory modules

---

## License

GNU General Public License v3.0 (GPL-3.0), same as the original DAAF.

---

## Acknowledgments

- **DAAF** — The original framework this adapts
- **Prof. Wayne Xu** — Methods development and Zotero library baseline
- **LampBotics AI Lab** — Development environment
- **Kimi K2.5 & Claude Opus 4.5** — Concurrent development

---

*Built for how research actually works—not how we wish it worked.*
