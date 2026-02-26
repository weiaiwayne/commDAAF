
---

## v0.4.0 (2026-02-26)

### Study: Iran Intermedia Agenda-Setting

Conducted AgentAcademy test study analyzing 262 Iran news headlines (Jan 2024 – Feb 2026) from GDELT. 60-headline stratified sample coded by Claude, GLM-4.7, and Kimi K2.5.

**Key Finding**: Israeli sources frame Iran as THREAT 10x more than Al Jazeera (42% vs 4%). All 5 hypotheses supported with 78% 3-model agreement.

### Gaps Identified → Skill Updates

| Gap Found | Fix Added |
|-----------|-----------|
| Duplicate headlines in sample | Pre-sampling deduplication protocol |
| No MIXED frame option | Multi-label coding (PRIMARY + SECONDARY) |
| "Strike back" vs "negotiate" coded same | Valence dimension required |
| No temporal breakdown | Segmentation required for >30 day studies |
| Unclear single vs multi-model QC | Explicit distinction documented |

### New Requirements

- **Mandatory tier declaration** before analysis (🟢/🟡/🔴)
- **Valence coding** alongside frame category
- **Human validation** still required for 🔴 Publication (N≥200, κ≥0.7)
- **Multi-model convergence ≠ human validation** — now explicitly stated

### Files Changed

- `SKILL.md` — v0.4 section, tier enforcement, QC distinction
- `references/methods/frame-analysis.md` — dedup, valence, temporal, multi-label
- `references/workflows/tiered-validation.md` — mandatory declaration, validation table

