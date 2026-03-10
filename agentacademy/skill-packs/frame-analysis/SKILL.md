# Frame Analysis Skill Pack

**Version:** 1.0.0  
**Status:** Validated  
**Maintainer:** UMass Computational Communication Lab

---

## Overview

Systematic coding of message frames in text content, following Entman (1993) and subsequent framing research.

## Capabilities

This skill pack enables an agent to:
- Identify primary and secondary frames in text
- Code valence (positive/negative/neutral toward subject)
- Code arousal level (low/medium/high)
- Handle multilingual content (with appropriate anchors)
- Distinguish between overlapping frame types

## Prerequisites

- Access to LLM capable of structured JSON output
- Understanding of framing theory (Entman 1993, Gamson 1992)
- Language-specific anchors for non-English content

---

## Probing Questions (ALL REQUIRED)

Before running frame analysis, answer:

```
Q1: What TYPE of framing?
    ✓ Media frames (how news covers an issue)
    ✓ Audience frames (how people interpret)
    ✓ Strategic frames (how actors influence)
    ✗ "Just frames" — TOO VAGUE

Q2: Inductive or deductive approach?
    ✓ Inductive: Let frames emerge from data
    ✓ Deductive: Apply existing typology (cite it)
    ✗ "Both" without primary — PICK ONE

Q3: Unit of analysis?
    ✓ Article/post
    ✓ Paragraph
    ✓ Sentence
    ✗ "The text" — BE SPECIFIC

Q4: What frame elements will you code?
    ✓ Problem definition
    ✓ Causal attribution
    ✓ Moral evaluation
    ✓ Treatment recommendation
    ✓ All four (Entman's framework)
    ✗ "The framing" — FRAMES HAVE COMPONENTS

Q5: Validation plan?
    ✓ Multiple coders + reliability
    ✓ Citation of established typology
    ✗ "I'll know it when I see it" — UNACCEPTABLE
```

---

## Entman's Frame Elements

| Element | Question It Answers | Example |
|---------|---------------------|---------|
| **Problem definition** | What's the issue? | "Immigration is a crisis" |
| **Causal attribution** | Who/what caused it? | "Government policy failure" |
| **Moral evaluation** | Is it good/bad? | "Inhumane treatment" |
| **Treatment recommendation** | What should be done? | "Build a wall" / "Open borders" |

---

## Common Frame Typologies

| Domain | Typology | Source |
|--------|----------|--------|
| **Generic** | Conflict, Human Interest, Economic, Morality, Responsibility | Semetko & Valkenburg (2000) |
| **Climate** | Scientific, Economic, Political, Risk | Nisbet (2009) |
| **Health** | Epidemic, Scientific, Political, Economic | Dudo et al. (2007) |
| **Protest** | Injustice, Solidarity, Call-to-Action, Humanitarian, Conflict | Gamson (1992), adapted |

---

## Coding Protocol

### Output Schema

```json
{
  "id": "string (post/article identifier)",
  "primary_frame": "string (from typology)",
  "secondary_frame": "string | null",
  "valence": "positive | negative | neutral",
  "arousal": "low | medium | high",
  "confidence": "number (0.0-1.0)",
  "rationale": "string (if ambiguous)"
}
```

### Multi-Label Coding

Frames are not always mutually exclusive:

| Field | Required | Description |
|-------|----------|-------------|
| **PRIMARY_FRAME** | Yes | Dominant frame in the content |
| **SECONDARY_FRAME** | If applicable | Secondary frame (mark as MIXED) |
| **VALENCE** | Yes | Tone toward subject |
| **CONFIDENCE** | Recommended | Coder certainty |

### Why Valence Matters

Two headlines with the same frame can have opposite implications:

| Headline | Frame | Valence | Meaning |
|----------|-------|---------|---------|
| "Iran ready to negotiate" | DIPLOMATIC | Positive | Openness |
| "Iran stalls on negotiations" | DIPLOMATIC | Negative | Obstruction |

---

## Decision Rules

### INJUSTICE vs CONFLICT vs HUMANITARIAN

```
IF post describes wrongdoing/harm:
  IF perpetrator is explicit AND blame is assigned:
    → INJUSTICE
  IF suffering/victimhood focus WITHOUT perpetrator:
    → HUMANITARIAN
  
IF post describes clash/opposition between actors:
  IF both sides are active participants:
    → CONFLICT
  IF one side is passive victim:
    → INJUSTICE
```

| Signal | Indicates |
|--------|-----------|
| "They killed", "Police attacked" | INJUSTICE |
| "Clashes between protesters and police" | CONFLICT |
| "Lives lost", "Suffering continues" | HUMANITARIAN |
| "Regime murdered innocent civilians" | INJUSTICE |

### SOLIDARITY vs CALL_TO_ACTION

```
IF post emphasizes unity/togetherness:
  → SOLIDARITY ("We are one", "Standing together")

IF post emphasizes mobilization/demands:
  → CALL_TO_ACTION ("Share this", "Rise up")

IF BOTH present:
  → Code PRIMARY as dominant, note SECONDARY
```

---

## Arousal Anchors

| Level | Examples | Markers |
|-------|----------|---------|
| **HIGH** | "They are killing us", "URGENT" | Exclamations, imperatives, threat |
| **MEDIUM** | "We stand together", "Justice for X" | Collective pronouns, appeals |
| **LOW** | "Update on situation", "Report:" | Neutral, factual, links |

---

## Multilingual Handling

### Persian-Specific

- "زن زندگی آزادی" (Woman Life Freedom) = SOLIDARITY/HOPE
- "مرگ بر دیکتاتور" (Death to dictator) = INJUSTICE (high arousal)
- Hashtags: #مهسا_امینی, #زن_زندگی_آزادی

### Arabic-Specific

- "المرأة الحياة الحرية" = SOLIDARITY/HOPE
- Mixed Arabic-Persian: code dominant language sentiment

### Cross-Cultural Notes

- Persian uses poetic metaphors — may seem "medium" literally but convey "high" arousal
- Chinese models may under-rate arousal vs Western models
- Always note model used for calibration

---

## Validation Requirements

| Tier | Requirement |
|------|-------------|
| 🟢 Exploratory | Multi-model coding, flag disagreements |
| 🟡 Pilot | + Human spot-check (N≥100), κ≥0.6 |
| 🔴 Publication | + Systematic human validation (N≥200), κ≥0.7 |

### Frame-Specific Reliability

**CRITICAL: Report reliability BY FRAME, not just aggregate.**

| Frame | Typical Reliability | Notes |
|-------|---------------------|-------|
| INFORMATIONAL | High (>70%) | Clear factual markers |
| CONFLICT | Medium (50-70%) | Depends on explicitness |
| SOLIDARITY | Low-Medium (30-50%) | Overlaps with HOPE |
| HUMANITARIAN | Low-Medium (30-50%) | Overlaps with INJUSTICE |

Flag frames with <40% three-way agreement.

---

## Prompt Template

```markdown
# FRAME ANALYSIS CODING INSTRUCTIONS

## TASK
For each text, assign codes for:
1. PRIMARY_FRAME: [list from typology]
2. SECONDARY_FRAME: [if applicable, else null]
3. VALENCE: positive / negative / neutral
4. AROUSAL: low / medium / high
5. CONFIDENCE: 0.0-1.0

## OUTPUT FORMAT
Return JSON array:
[{"id": "...", "primary_frame": "...", "secondary_frame": null, 
  "valence": "...", "arousal": "...", "confidence": 0.8}]

## DECISION HIERARCHY
When multiple frames apply:
1. INJUSTICE (if perpetrator explicit)
2. CONFLICT (if both sides active)
3. HUMANITARIAN (if victim focus)
4. SOLIDARITY (if unity emphasis)
5. CALL_TO_ACTION (if mobilization)
6. INFORMATIONAL (if factual only)

## FRAME DEFINITIONS
[Include full definitions from typology]

## VALENCE ANCHORS
- Positive: hope, victory, celebration
- Negative: grief, anger, injustice
- Neutral: factual, no emotional valence

## AROUSAL ANCHORS
[Include level-specific examples]

## LANGUAGE-SPECIFIC GUIDANCE
[Include anchors for relevant languages]
```

---

## Benchmark

See `benchmarks/frame-analysis-gold-v1.json` for validation dataset.

**Benchmark specs:**
- N = 200 posts
- Languages: English, Persian, Arabic
- Human-coded by 3 coders
- Fleiss' κ = 0.74

**Passing criteria:**
- Accuracy vs gold ≥ 0.75
- Pairwise κ with gold ≥ 0.7

---

## Known Limitations

1. **SOLIDARITY/HOPE overlap** — Low inter-model agreement
2. **Persian arousal** — Western models may under-code
3. **Hashtag-heavy posts** — Limited text for frame inference
4. **Sarcasm** — All models struggle; flag for human review

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-10 | Initial release |

---

## References

- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm.
- Gamson, W. A. (1992). Talking politics.
- Semetko, H. A., & Valkenburg, P. M. (2000). Framing European politics.
