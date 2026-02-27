# Virality Study: Preliminary Report

**AgentAcademy Test Study** — CommDAAF Multi-Model Guardrail Test  
**Date:** 2026-02-27  
**Status:** In Progress (Claude complete, GLM/Kimi coding)

---

## Study Setup

| Parameter | Value |
|-----------|-------|
| **Total Sample** | 719 posts (after deduplication + language filter) |
| **MahsaAmini** | 380 posts (Sep 2022 Iran protests) |
| **Ukraine** | 339 posts (Jun 16-23, 2022 war discourse) |
| **Engagement Tiers** | Viral (top 5%), High, Medium, Low |
| **CommDAAF Tier** | 🟢 Exploratory |

---

## Claude Analysis: Batch 1 (100 MahsaAmini Viral Posts)

### Frame Distribution

| Frame | Count | % |
|-------|-------|---|
| **SOLIDARITY** | 28 | 28% |
| **INJUSTICE** | 24 | 24% |
| **HOPE** | 17 | 17% |
| **CALL_TO_ACTION** | 14 | 14% |
| **CONFLICT** | 10 | 10% |
| **INFORMATIONAL** | 7 | 7% |
| **HUMANITARIAN** | 0 | 0% |

### Valence Distribution

| Valence | Count | % |
|---------|-------|---|
| **Negative** | 47 | 47% |
| **Positive** | 45 | 45% |
| **Neutral** | 8 | 8% |

### Arousal Distribution

| Arousal | Count | % |
|---------|-------|---|
| **High** | 72 | 72% |
| **Medium** | 21 | 21% |
| **Low** | 7 | 7% |

---

## Preliminary Findings

### H1: Content Frames & Virality

**Finding: SOLIDARITY and INJUSTICE dominate viral MahsaAmini posts (52% combined)**

This supports H1a (injustice) and H1b (solidarity) — viral protest content frames victimization AND collective action together.

### H2: Arousal & Virality

**Finding: 72% of viral posts are HIGH arousal**

Strongly supports H2 — high arousal content spreads faster, consistent with Berger & Milkman (2012).

### H3: Valence Effects

**Finding: Near-equal positive (45%) and negative (47%) valence**

Mixed support for H3 — in protest context, BOTH emotional polarities can drive virality:
- Negative: Injustice, conflict, outrage
- Positive: Solidarity, hope, collective efficacy

### Unexpected Finding: HUMANITARIAN Frame Absent

**Zero humanitarian-framed viral posts** in MahsaAmini sample. This may indicate:
- Protest movements emphasize agency (SOLIDARITY, CALL_TO_ACTION) over victimhood (HUMANITARIAN)
- Or: HUMANITARIAN framing doesn't drive virality in protest contexts

---

## Ukraine Comparison (Preliminary)

From initial coding of Ukraine batch 5:

| Dataset | Dominant Frames | Arousal Pattern |
|---------|----------------|-----------------|
| **MahsaAmini** | SOLIDARITY (28%), INJUSTICE (24%) | 72% HIGH |
| **Ukraine** | INFORMATIONAL (56%), CONFLICT (22%) | 44% LOW |

**Preliminary H7 Assessment**: Frame patterns differ substantially between protest and war discourse:
- **Protest**: Emotional, solidarity-focused, high arousal
- **War**: Informational, conflict-focused, lower arousal

This suggests **context-specific** rather than universal virality predictors.

---

## CommDAAF Gaps Identified (So Far)

### 1. Mixed-Language Coding Challenge
Many MahsaAmini posts are in Farsi with English hashtags. Need:
- Language-specific frame indicators
- Translation verification step

### 2. Hashtag-Heavy Posts
~40% of posts are primarily hashtags with minimal text. Frame coding is ambiguous.
- Suggest: Add HASHTAG_RALLY as a sub-category of CALL_TO_ACTION

### 3. Image/Video References
Many posts reference attached media ("https://t.co/..."). Without seeing media, coding is incomplete.
- Suggest: Flag posts with media attachments for separate analysis

---

## Next Steps

1. **Await GLM & Kimi coding** — Compare inter-model reliability
2. **Code remaining batches** — Full 719-post analysis
3. **Regression analysis** — Frame + Source → Engagement
4. **Cross-dataset comparison** — Formal H7 test

---

## Files Generated

| File | Description |
|------|-------------|
| `sample_for_coding.csv` | Full 719-post sample |
| `coding_batch_*.json` | 8 batches for LLM coding |
| `claude_batch1_coding.json` | Claude's 100-post analysis |
| `RESEARCH_DESIGN.md` | Full methodology |

---

*Preliminary Report — Final synthesis pending multi-model validation*
