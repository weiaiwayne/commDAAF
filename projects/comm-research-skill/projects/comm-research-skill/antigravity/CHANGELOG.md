
---

## v0.5.0 (2026-03-06)

### Study: Wikipedia Epistemic Authority

Analyzed 100 Wikipedia articles on 2026 Iran war and Israel-Hamas conflict (28,006 revisions, 276 talk page excerpts). Mixed-methods: revert network analysis + critical discourse analysis.

**Key Findings:**
- 41% reverter elite whose edits are never reverted
- Source hierarchy debates (κ=0.47) cross-culturally validated
- "Hermeneutical injustice" (κ=0.18) culturally contested—Western construct
- Credential-based authority ≠ identity-based prejudice

### New Methods Added

| Method | Description |
|--------|-------------|
| `multi-model-construct-validation.md` | Use culturally diverse LLMs to test if constructs are cross-culturally robust vs. contested |
| `platform-discourse-analysis.md` | Thick description of talk pages/forums with Foucault/Bourdieu framing |
| `revert-network-analysis.md` | Build networks from revert relationships to reveal power asymmetries |

### Key Learnings

1. **Multi-model κ as construct validation** — High κ across US+China models = cross-cultural robustness; Low κ = construct is culturally contested (finding, not failure)

2. **Source hierarchy as universal battleground** — Debates over "whose sources count" are recognizable across cultures; more philosophical constructs (epistemic injustice) are not

3. **Credential-based exclusion patterns** — Platform credentials (edit count, policy fluency) function as cultural capital; different from identity-based prejudice

4. **Structural isomorphism** — 40/60 reverter/reverted split appears constant across topics/timeframes (platform structure > topic dynamics)

5. **Policy alphabet soup as insider marker** — WP:RS, WP:NPOV, WP:BLP fluency signals legitimate participation; newcomers excluded by procedural discourse

### Files Added

- `references/methods/multi-model-construct-validation.md`
- `references/methods/platform-discourse-analysis.md`
- `references/methods/revert-network-analysis.md`

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

