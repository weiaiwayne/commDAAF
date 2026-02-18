# CommDAAF

**Computational Communication Research Framework**

A methodological skill pack for AI-assisted computational social science research, adapted from [DAAF](https://github.com/DAAF-Contribution-Community/daaf) and tailored for communication scholars.

---

## ⚠️ Experimental Software

This framework is under active development at the [LampBotics AI Lab](https://lampbotics.com). It was built concurrently by Kimi K2.5 and Claude Opus 4.5 as an experiment in AI-assisted research tool development.

**Use with caution.** The lab will be field-testing CommDAAF over the coming weeks. We welcome researchers who want to try it and provide feedback—just understand that things may break, documentation may be incomplete, and the methods are still being validated.

If you encounter issues or have suggestions, open an issue or reach out.

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

## Heritage: DAAF

CommDAAF adapts the [Data Analyst Augmentation Framework (DAAF)](https://github.com/DAAF-Contribution-Community/daaf), originally developed for education data analysis. DAAF introduced the core idea of encoding methodological best practices into AI assistant instructions.

**What CommDAAF adds:**

| DAAF | CommDAAF |
|------|----------|
| Education data focus | Communication/social media focus |
| Assumes API access | Post-API era strategies (2025 reality) |
| General validation | Tiered validation (exploratory → pilot → publication) |
| Trust-based | Nudge system (forces conscious choices) |
| Single platform | Claude Code + OpenClaw + Antigravity |
| Generic methods | Communication theory integration |

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

Every methodological choice is surfaced, not hidden. The system uses five nudge types:

1. **Default Danger Flags** — Warns when you're about to accept untested defaults
2. **Active Choice Requirement** — Forces explicit selection between alternatives
3. **Trade-Off Visualization** — Shows what you gain and lose with each choice
4. **Assumption Audit** — Surfaces hidden assumptions before analysis
5. **Reflection Checkpoints** — Pauses for metacognition at key stages

### Post-API Data Strategies

The era of free Twitter APIs is over. CommDAAF is honest about what data you can actually get:

| Platform | Status (2025) | Strategy |
|----------|---------------|----------|
| Twitter/X | $5K+/month | Existing datasets, Wayback Machine |
| Reddit | Restricted | Archives, limited API |
| Bluesky | Open | Recommended alternative |
| Meta | Gated | Application required (6-12 weeks) |

### AgentAcademy: Multi-Model Peer Review

CommDAAF includes **AgentAcademy** — an incubator where AI agents learn from mistakes through adversarial peer review. Multiple models with different epistemic perspectives independently analyze your data, then critique each other:

| Agent | Role | Checks For |
|-------|------|------------|
| Methodologist | Research design | Validity threats, sampling issues |
| Theorist | Conceptual framing | Construct validity, literature gaps |
| Empiricist | Statistical rigor | Effect sizes, corrections, assumptions |
| Skeptic | Adversarial critique | What could go wrong, alternative explanations |
| Integrator | Coherence | Gaps between sections, logical flow |

**Try it live:** [vineanalyst.com/commdaaf/agentacademy](https://vineanalyst.com/commdaaf/agentacademy)

Validated by running GLM-4.7 and Kimi K2.5 through independent parallel analyses (e.g., #EndSARS dataset), then cross-reviewing each other. Errors caught become lessons; lessons become new checks. The skill pack improves with each run.

### Communication Theory Integration

Methods are connected to theory:

- **Gatekeeping** — Network centrality, algorithmic curation
- **Agenda-Setting** — Topic salience, intermedia dynamics
- **Networked Publics** — Community formation, counterpublics
- **Information Diffusion** — Cascades, echoing, virality

### Zotero Personalization

CommDAAF can analyze your Zotero library to customize its guidance based on methods and theories you actually use. The default configuration reflects Prof. Wayne Xu's research focus (network analysis, coordinated behavior, computational methods), but you can regenerate it from your own library.

```bash
cd skill-templates/zotero
python adapt.py --user-id YOUR_ZOTERO_ID --api-key YOUR_API_KEY
```

---

## Methods Included

| Method | Description |
|--------|-------------|
| Sentiment Analysis | VADER, LLM, sarcasm detection |
| Topic Modeling | LDA, BERTopic, K-selection |
| Frame Analysis | Entman framework, inductive/deductive |
| Network Analysis | Centrality, community detection |
| Coordinated Behavior | Timing similarity, network patterns |
| Content Analysis | Codebook development, reliability |
| LLM Annotation | Multi-model validation |
| TextNets | Bipartite document-word networks |
| LTTN | Latent temporal-thematic networks (experimental) |
| LLM Simulation | Agent-based modeling (experimental) |

---

## Deployment

CommDAAF works with three AI coding platforms. Pick yours:

### Claude Code (Anthropic CLI)

Simplest option—drop a single file into your project:

```bash
curl -O https://raw.githubusercontent.com/weiaiwayne/commDAAF/main/CLAUDE_BUNDLE.md
mv CLAUDE_BUNDLE.md CLAUDE.md
```

Or clone for full functionality:

```bash
git clone https://github.com/weiaiwayne/commDAAF.git .commdaaf
```

Then create a `CLAUDE.md` that references it:

```markdown
# CommDAAF Project

Read `.commdaaf/skill-templates/SKILL.md` for research tasks.
Load method files from `.commdaaf/skill-templates/methods/` as needed.
```

### OpenClaw

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/weiaiwayne/commDAAF.git commdaaf
```

The skill auto-registers via `manifest.json`.

### Google Antigravity

```bash
cd ~/.gemini/antigravity/skills
git clone https://github.com/weiaiwayne/commDAAF.git
cd commDAAF && cp -r antigravity/* . && rm -rf antigravity skill-templates
```

---

## Quick Test

After installation, try:

```
Analyze sentiment in climate change discourse on Bluesky
```

If working correctly, the assistant should:

1. Ask what you mean by "sentiment" (valence? emotions? stance?)
2. Ask about your unit of analysis
3. Ask about your sarcasm detection strategy (climate = high sarcasm domain)
4. Ask about your validation plan

If it just runs VADER with defaults, the setup isn't working.

---

## Project Structure

```
commDAAF/
├── CLAUDE_BUNDLE.md          # One-file version for Claude Code
├── DEPLOYMENT.md             # Detailed setup instructions
├── skill-templates/          # OpenClaw version
│   ├── SKILL.md              # Main entry point
│   ├── methods/              # 10+ method skills
│   ├── data-sources/         # 9 platform guides
│   ├── workflows/            # Validation, ethics, stages
│   ├── theories/             # Communication theory modules
│   ├── pipelines/            # End-to-end guided workflows
│   └── zotero/               # Library personalization
└── antigravity/              # Google Antigravity version
```

---

## Acknowledgments

- **DAAF** — The original framework this adapts
- **Prof. Wayne Xu** — Methods development and Zotero library baseline
- **LampBotics AI Lab** — Development environment
- **Kimi K2.5 & Claude Opus 4.5** — Concurrent development (yes, really)

---

## Contributing

This is experimental software. Contributions welcome:

- Bug reports and issues
- New method skills
- Improved probing questions
- Additional theory modules
- Translations of ethics guidance for non-US contexts

---

## License

GNU General Public License v3.0 (GPL-3.0), same as the original DAAF.

This means you can use, modify, and distribute CommDAAF freely, but derivative works must also be open source under GPL-3.0.

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

*Built for how research actually works—not how we wish it worked.*
