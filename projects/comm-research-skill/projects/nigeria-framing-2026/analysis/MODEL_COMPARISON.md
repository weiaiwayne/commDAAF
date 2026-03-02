# Three-Model Framing Analysis Comparison

**Date:** 2026-02-22  
**Dataset:** 304 articles (GDELT + MediaCloud)  
**Models:** Claude, GLM-4.7, Kimi K2.5

---

## Model Status

| Model | Status | Notes |
|-------|--------|-------|
| **Claude (Anthropic)** | ✅ Completed | Full analysis |
| **GLM-4.7 (Zhipu/z.ai)** | ✅ Completed | Full analysis |
| **Kimi K2.5 (Moonshot)** | ❌ BLOCKED | "Request rejected: high risk" |

**Note:** Kimi's content filter blocked analysis of religious conflict content, even with academic framing. This confirms earlier findings about Chinese LLM content moderation.

---

## Frame Prevalence Comparison

| Frame | Claude | GLM-4.7 | Convergence |
|-------|--------|---------|-------------|
| **Religious Persecution** | 55-60% | 62% | ✅ Strong |
| **Violence/Security** | 30-35% | — | — |
| **State Failure** | 15-20% | 18% | ✅ Strong |
| **Criminal/Banditry** | 10-15% | 14% | ✅ Strong |
| **Ethnic Conflict** | 5-8% | 4% | ✅ Strong |
| **Resource/Economic** | 2-3% | 2% | ✅ Strong |
| **Climate/Structural** | <1% | — | — |

**Convergence Score: HIGH** — Both models independently arrived at similar prevalence estimates.

---

## Hypothesis Assessment Comparison

| Hypothesis | Claude | GLM-4.7 | Agreement |
|------------|--------|---------|-----------|
| **H1: Religious > Economic framing** | ✅ Supported | ✅ Supported | ✅ AGREE |
| **H2: Fulani blamed > structural factors** | ✅ Supported | ✅ Supported | ✅ AGREE |
| **H3: Christians victims > Fulani** | ✅ Supported | ✅ Strongly Supported | ✅ AGREE |
| **H4: Conservative = stronger religious frame** | ✅ Supported | ✅ Supported | ✅ AGREE |
| **H5: Nigerian = more diverse framing** | ⚠️ Partially Supported | ❌ Not Supported | ⚠️ DIVERGE |

### Divergence on H5

**Claude's view:** Nigerian sources show more diverse framing (grazing policy, sovereignty concerns)
- Evidence: Punch mentions ranching; ThisDay covers governance

**GLM's view:** Nigerian sources similar to mainstream US (40-60% religious)
- Evidence: Statistical comparison shows no significant difference

**Resolution:** Both may be correct — Nigerian sources include *different* frames (policy) but *similar prevalence* of religious framing. Diversity ≠ lower religious framing.

---

## Source Classification Comparison

### Claude's Categories
- Conservative US
- Religious media
- Mainstream US
- Nigerian sources
- Wire services

### GLM's Categories
- Conservative US
- Mainstream US
- Nigerian sources
- Religious sources
- Analytical sources (new category)

**Key Addition by GLM:** Identified "Analytical sources" (TheConversation, TheGuardian) as distinct category with 0-33% religious framing — the only sources providing structural analysis.

---

## Key Patterns Identified

### Both Models Found:
1. **Religious framing dominance** (55-62%)
2. **Economic/climate framing near-absent** (1-2%)
3. **Christian victimhood dominant narrative**
4. **Conservative media echo chamber**
5. **Trump administration as frame driver**

### GLM Unique Findings:
1. **Narrative silos** — Mapped specific source clusters
2. **TheConversation anomaly** — Only source with consistent structural framing
3. **MACBAN response** — Only mention of Fulani victimhood
4. **Temporal clustering** — Coverage spikes around events

### Claude Unique Findings:
1. **Nicki Minaj effect** — Celebrity advocacy influencing coverage
2. **Christmas attack predictions** — Coordinated messaging pattern
3. **Kidnapping over-representation** — Event type bias

---

## Confidence Assessment

| Finding | Claude Confidence | GLM Confidence | Combined |
|---------|-------------------|----------------|----------|
| Religious frame dominance | High | High | **VERY HIGH** |
| Economic frame absence | High | High | **VERY HIGH** |
| Source ideology effects | Medium | High | **HIGH** |
| Nigerian diversity | Medium | Low | **MEDIUM** |
| Actor portrayal asymmetry | High | High | **VERY HIGH** |

---

## Methodological Notes

### Strengths of Multi-Model Approach
1. **Epistemic diversity** — Different training data, different biases
2. **Convergence validation** — Agreement increases confidence
3. **Blind spots revealed** — GLM found TheConversation anomaly; Claude found celebrity effect

### Limitations
1. **Title-only analysis** — Both models note this limitation
2. **Sample bias** — Conservative sources over-represented
3. **Binary coding** — Articles may blend frames
4. **Model agreement** — Both models may share similar training biases

### Kimi Blocking as Data Point
Kimi's refusal to analyze religious conflict content demonstrates:
- Content moderation persists even for academic analysis
- Topic sensitivity varies across LLM providers
- Two-model comparison still provides validation

---

## Final Verdict

### High-Confidence Findings (Claude + GLM agree)
1. **Religious framing dominates** international coverage (~60%)
2. **Economic/structural framing is nearly absent** (~2%)
3. **Christians portrayed as victims; Fulani as aggressors**
4. **Conservative US sources show strongest religious framing** (85-100%)
5. **No coverage of Fulani victimhood**

### Medium-Confidence Findings (partial agreement)
1. **Nigerian sources show different frames** (policy, sovereignty) but **similar religious prevalence**
2. **Analytical sources exist but are rare** (3 articles)

### Implications
Coverage systematically distorts the conflict by:
- Emphasizing religious persecution over resource competition
- Ignoring structural drivers (climate, land policy)
- Creating asymmetric actor portrayal
- Potentially influencing policy toward military rather than structural solutions

---

*Multi-Model Analysis | CommDAAF Framework*
