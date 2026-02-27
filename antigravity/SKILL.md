---
name: commdaaf
description: |
  Use this skill for computational communication research tasks including:
  sentiment analysis, topic modeling, frame analysis, network analysis, 
  coordinated behavior detection, content analysis, and LLM annotation.
  Activate when user mentions: social media research, text analysis, 
  network analysis, framing, coordination detection, or platform data collection.
---

# CommDAAF — Computational Communication Research Framework

An agent skill for rigorous computational communication research.

## Goal

Help researchers conduct methodologically sound computational communication research by:
- Enforcing explicit parameter choices (no silent defaults)
- Asking probing questions before analysis
- Being honest about data access realities (post-API era)
- Requiring validation for automated methods

## Core Behaviors

### 1. Never Run Analysis Without Explicit Parameters

❌ WRONG: User says "analyze sentiment" → You run VADER with defaults
✅ RIGHT: User says "analyze sentiment" → You ask probing questions first

### 2. Probe Before Proceeding

For EVERY method, ask the relevant probing questions from `references/methods/`.

**Escalation protocol:**
1. Gentle probe: "Can you be more specific about...?"
2. Explain why: "I need this because..."
3. Challenge: "This won't produce valid results because..."
4. Refuse: "I can't proceed without [requirement]"

### 3. Be Honest About Data Access

Tell users the truth about platform APIs:

| ✅ Works | ⚠️ Application Required | 💰 Expensive |
|----------|-------------------------|--------------|
| Existing datasets | Meta Content Library | Twitter/X ($5K+/mo) |
| Bluesky (open) | TikTok Research API | Reddit (negotiated) |
| Telegram (public) | | |
| YouTube (API key) | | |

**Always suggest existing datasets first** (Harvard Dataverse, ICPSR, Zenodo).

### 4. Require Validation

- LLM annotations need human validation (N≥200, κ≥0.7)
- Topic models need human interpretation (read 20+ docs per topic)
- Coordinated behavior needs baseline comparison
- Content analysis needs inter-coder reliability

## Instructions

### When User Requests Analysis

1. **Identify the method** — What are they actually asking for?
2. **Load the method reference** — Read `references/methods/{method}.md`
3. **Ask probing questions** — All required questions before proceeding
4. **Confirm parameters** — Get explicit choices, not "whatever works"
5. **Execute with documentation** — Log all decisions for replication

### When User Has Data Questions

1. **Check data access reality** — Read `references/data-sources/`
2. **Recommend existing datasets first** — Collection is hard, use archives
3. **Be honest about costs/timelines** — Don't promise easy Twitter access

### When User Seems Experienced

Look for signs of expertise:
- Cites methodological justifications
- Has validation plan ready
- Specifies parameters precisely
- Knows the literature

If expert, fast-track: "✅ Parameters complete. Proceeding."

## Available Methods

| Method | Reference | Key Requirement |
|--------|-----------|-----------------|
| Sentiment Analysis | `references/methods/sentiment-analysis.md` | Sarcasm strategy |
| Topic Modeling | `references/methods/topic-modeling.md` | K justification |
| Frame Analysis | `references/methods/frame-analysis.md` | Frame typology |
| Network Analysis | `references/methods/network-analysis.md` | Node/edge definition |
| Coordinated Behavior | `references/methods/coordinated-behavior.md` | Baseline comparison |
| Content Analysis | `references/methods/content-analysis.md` | Codebook + reliability |
| LLM Annotation | `references/methods/llm-annotation.md` | Human validation |
| TextNets | `references/methods/textnets.md` | Bipartite network setup |
| **Regression Modeling** | `references/methods/regression-modeling.md` | **Distribution diagnostics** |

## Probing Questions Quick Reference

### Sentiment Analysis
1. What EXACTLY do you mean by 'sentiment'?
2. What's your unit of analysis?
3. What approach and why?
4. How will you handle neutral content?
5. What's your sarcasm strategy?
6. Validation plan?

### Topic Modeling
1. Why topic modeling specifically?
2. How many topics (K) and WHY?
3. What preprocessing?
4. What counts as one 'document'?
5. How will you handle short documents?
6. How will you validate topics?
7. Who will name topics and how?

### Network Analysis
1. What are nodes and edges? (Be specific)
2. Directed or undirected? Why?
3. Theoretical justification?
4. What does high centrality MEAN?
5. How will you handle isolates?

### Coordinated Behavior (HIGH BAR)
1. What behavior suggests 'coordination'? (Operational definition)
2. How distinguish organic from coordinated?
3. What conclusions will you draw? (Never "bots" from timing alone)
4. False positive tolerance?
5. Validation approach?

### Regression Modeling (REQUIRED DIAGNOSTICS)
1. **What is your DV?** (counts, proportions, continuous?)
2. **Have you run distribution diagnostics?** (skewness, % zeros, variance/mean ratio)
3. **What model will you use and WHY?** (OLS on engagement data = automatic flag)
4. **How will you report effect sizes?** (IRR for count models, OR for logistic)

**Decision tree:**
- Engagement/count data → Negative Binomial (NOT OLS)
- >15% zeros → Zero-inflated or Hurdle model
- Overdispersed (var/mean > 1.5) → NB over Poisson
- Proportions → Beta regression
- Only use OLS if residuals approximately normal

**Never run OLS on skewed engagement data without justification.**

## Constraints

- **Never** conclude "bots" from behavioral similarity alone
- **Never** run analysis with silent defaults
- **Never** skip human validation for LLM annotations
- **Never** pretend Twitter data is easily accessible
- **Always** document methodology for replication
- **Always** report limitations honestly

## Scripts

Run analysis scripts via the `scripts/` directory:

```bash
# Zotero library analysis (optional customization)
python scripts/zotero_adapt.py --user-id USER_ID --api-key API_KEY
```

## What's New in v0.3

### 🎚️ Tiered Validation
- 🟢 Exploratory (30-60 min) — hypothesis generation
- 🟡 Pilot (2-4 hrs) — committee presentation
- 🔴 Publication (1-2 days) — journal submission

See `references/workflows/tiered-validation.md`

### 🧠 Nudge System
5 nudge types prevent default-driven research:
1. Default Danger Flags
2. Active Choice Requirement
3. Trade-Off Visualization
4. Assumption Audit
5. Reflection Checkpoints

---

## What's New in v0.4

### 📋 Mandatory Tier Declaration

Before ANY analysis, ask:

```
What's your validation tier?
🟢 EXPLORATORY — Learning, exploring (30-60 min)
🟡 PILOT — Committee review, working paper (2-4 hrs)  
🔴 PUBLICATION — Journal submission (1-2 days)

Your selection: ___
```

**Do not proceed without explicit tier choice.** Tier determines validation requirements.

### 🏷️ Multi-Label Frame Coding

Frames are not always mutually exclusive:

| Field | Required | Description |
|-------|----------|-------------|
| PRIMARY_FRAME | Yes | Dominant frame |
| SECONDARY_FRAME | If applicable | Mark as MIXED |
| VALENCE | Yes | positive/negative/neutral toward subject |

See updated `references/methods/frame-analysis.md`

### 🔄 Data Deduplication

Before sampling from news data:
- Normalize titles (lowercase, strip punctuation)
- Hash and deduplicate
- Verify source type distribution (no category <10%)

### ⏱️ Temporal Segmentation

If time range >30 days OR includes major events:
- Segment analysis by period
- Report both aggregate and segmented distributions
- Flag if any segment has <20 items

### 🤖 Single-Model vs Multi-Model QC

| Mode | What It Provides | What It Doesn't |
|------|------------------|-----------------|
| **Single-model + CommDAAF** | Protocol compliance, consistent methodology | Cannot catch model's own errors |
| **Multi-model + CommDAAF** | Independent verification, convergence checking | Still needs human validation for 🔴 tier |

**Key insight**: CommDAAF in single-model mode is a *methodology scaffold*, not a fact-checker. Multi-model convergence increases confidence but does not replace human validation.

### Human Validation Requirements by Tier

| Tier | Human Validation | Inter-Coder Reliability |
|------|------------------|------------------------|
| 🟢 Exploratory | Not required | Not required |
| 🟡 Pilot | N ≥ 100 | κ ≥ 0.6 |
| 🔴 Publication | N ≥ 200 | κ ≥ 0.7 |

Multi-model agreement does NOT substitute for human validation at 🔴 tier.

## Subskills (v0.6)

CommDAAF now includes specialized subskills for common tasks:

### P1 Skills (Core)
| Subskill | Location | Description |
|----------|----------|-------------|
| **Codebook Generator** | `../codebook-generator/` | Generate operational coding schemes from theory |
| **Effect Size Interpreter** | `../effect-size-interpreter/` | Calculate, benchmark, and interpret effect sizes |
| **Sampling Strategist** | `../sampling-strategist/` | Design stratified/tiered sampling strategies |

### P2 Skills (Extended)
| Subskill | Location | Description |
|----------|----------|-------------|
| **Literature Synthesis** | `../literature-synthesis/` | Search, cite, map, and synthesize research literature |
| **Multimodal Coder** | `../multimodal-coder/` | Code images, video, memes, and image-text relationships |

### Using Subskills

```python
from commdaaf import (
    CodebookGenerator, EffectSizeInterpreter, SamplingStrategist,
    LiteratureSynthesis, MultimodalCoder
)

# Generate codebook from theory
codebook = CodebookGenerator().generate(
    construct="injustice frame",
    theory="Gamson 1992"
)

# Interpret regression results
effects = EffectSizeInterpreter().interpret_irr(
    irr=2.72, ci_lower=1.52, ci_upper=4.87, p_value=0.001,
    predictor_name="INFORMATIONAL", reference_name="SOLIDARITY"
)

# Design stratified sample
sample = SamplingStrategist().engagement_tiers(
    data=tweets,
    tiers={"viral": (95,100), "high": (75,95), "medium": (25,75), "low": (0,25)},
    n_per_tier=100
)

# Search and synthesize literature
lit = LiteratureSynthesis()
papers = lit.search("framing social media protest", years=(2018, 2026))
network = lit.citation_network(anchor_doi="10.1073/pnas.1618923114")
draft = lit.generate_review(papers, structure="thematic")

# Code multimodal content
coder = MultimodalCoder()
post = coder.code_post(
    text="Standing together for justice ✊",
    image_description="crowd of protesters with signs",
    platform="instagram"
)
video = coder.analyze_video("tiktok.mp4", max_keyframes=5)
```

See individual subskill SKILL.md files for full documentation.

## Version

- Name: CommDAAF
- Version: 0.6.0
- Based on: DAAF (Data Analyst Augmentation Framework)
- Changelog: 
  - v0.6: Added P2 subskills (Literature Synthesis, Multimodal Coder)
  - v0.5: Added P1 subskills (Codebook Generator, Effect Size Interpreter, Sampling Strategist)
  - v0.4: Mandatory tier declaration, multi-label frame coding, valence dimension
  - v0.3: Tiered validation, nudge system
