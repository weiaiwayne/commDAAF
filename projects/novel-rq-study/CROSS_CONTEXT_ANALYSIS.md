# Cross-Context Frame Analysis: War vs Protest Discourse

**Date:** 2026-03-04  
**Validation Tier:** 🟢 EXPLORATORY  
**Contexts Compared:**
- Ukraine War (N=339, June 2022)
- #MahsaAmini Protest (N=380, Sept-Oct 2022)

---

## Executive Summary

War and protest movements produce **fundamentally different discourse patterns**:

| Dimension | War (Ukraine) | Protest (#MahsaAmini) |
|-----------|---------------|----------------------|
| **Dominant Frame** | INFORMATIONAL (57%) | SOLIDARITY (34%) |
| **Primary Valence** | Neutral (54%) | Positive (47%) |
| **Arousal Level** | Medium (83%) | High (45%) |
| **Function** | Information distribution | Identity mobilization |

---

## Frame Distribution Comparison

| Frame | Ukraine | % | MahsaAmini | % | Δ |
|-------|---------|---|------------|---|---|
| **SOLIDARITY** | 30 | 8.8% | 130 | **34.2%** | +25.4% |
| **INJUSTICE** | 44 | 13.0% | 42 | 11.1% | -1.9% |
| **CONFLICT** | 26 | 7.7% | 24 | 6.3% | -1.4% |
| **HUMANITARIAN** | 12 | 3.5% | 32 | 8.4% | +4.9% |
| **HOPE** | 23 | 6.8% | 48 | 12.6% | +5.8% |
| **INFORMATIONAL** | 192 | **56.6%** | 32 | 8.4% | -48.2% |
| **CALL_TO_ACTION** | 12 | 3.5% | 72 | 18.9% | +15.4% |

### Visualization (ASCII)

```
SOLIDARITY      ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ 8.8%  (Ukraine)
                ████████████████████████████████████ 34.2% (MahsaAmini)

INFORMATIONAL   ████████████████████████████████████ 56.6% (Ukraine)
                █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 8.4%  (MahsaAmini)

CALL_TO_ACTION  ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 3.5%  (Ukraine)
                ████████████████████░░░░░░░░░░░░░░░ 18.9% (MahsaAmini)

HOPE            █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 6.8%  (Ukraine)
                ████████████░░░░░░░░░░░░░░░░░░░░░░░ 12.6% (MahsaAmini)
```

---

## Valence Distribution

| Valence | Ukraine | % | MahsaAmini | % |
|---------|---------|---|------------|---|
| Positive | 67 | 19.8% | 178 | **46.8%** |
| Negative | 88 | 26.0% | 134 | 35.3% |
| Neutral | 184 | **54.3%** | 68 | 17.9% |

**Interpretation:** Protest discourse is more emotionally polarized (positive OR negative), while war discourse maintains journalistic neutrality.

---

## Arousal Distribution

| Arousal | Ukraine | % | MahsaAmini | % |
|---------|---------|---|------------|---|
| High | 44 | 13.0% | 169 | **44.5%** |
| Medium | 281 | **82.9%** | 171 | 45.0% |
| Low | 14 | 4.1% | 40 | 10.5% |

**Interpretation:** Protest discourse requires high emotional engagement for mobilization. War discourse maintains steady-state medium arousal (ongoing crisis, not peak mobilization).

---

## Theoretical Interpretation

### 1. Discourse Function Hypothesis

**Protest movements need identity construction** → SOLIDARITY dominates
- "We are one"
- "The world is watching"
- Collective identity formation

**War coverage prioritizes information** → INFORMATIONAL dominates
- "Breaking: Russian forces..."
- "OSINT update..."
- Situational awareness

### 2. Mobilization Strategy Hypothesis

**Protest = peak mobilization phase** → High arousal, CALL_TO_ACTION
- Need to recruit participants
- Emotional urgency required
- "Act now" framing

**War = sustained conflict** → Medium arousal, INFORMATIONAL
- Long-term engagement needed
- Fatigue management
- Information-as-action (sharing = contributing)

### 3. INJUSTICE Convergence

Both contexts have similar INJUSTICE framing (~11-13%):
- Universal: Moral outrage is foundation of both movements
- Necessary but not sufficient for mobilization
- Requires pairing with SOLIDARITY (protest) or INFORMATIONAL (war)

### 4. Absent Frames

**Ukraine lacks:**
- SOLIDARITY (8.8%) — Why? Collective identity less salient than tactical info?
- CALL_TO_ACTION (3.5%) — Mobilization happens in other channels?

**MahsaAmini lacks:**
- INFORMATIONAL (8.4%) — Protest doesn't need "news"; it IS the news
- Low neutral valence — No room for detachment in revolt

---

## Qualitative Implications

### For RQ1 (Enemy Construction)
- **Hypothesis:** Ukraine constructs Russia as strategic threat; MahsaAmini constructs regime as moral abomination
- **Test:** Compare INJUSTICE exemplars across contexts

### For RQ2 (Solidarity Performance)
- **Hypothesis:** Diaspora solidarity differs by context — Ukraine = material support; MahsaAmini = identity solidarity
- **Test:** Compare SOLIDARITY exemplars, especially English-language

### For RQ3 (Frame Hybridization)
- **Hypothesis:** War discourse hybridizes INFORMATIONAL + CONFLICT; Protest hybridizes SOLIDARITY + HOPE
- **Test:** Analyze multi-frame posts in each context

### For RQ4 (Silence & Absence)
- **Confirmed:** SOLIDARITY absent in war; INFORMATIONAL absent in protest
- **Question:** Is this functional (appropriate to context) or a missed opportunity?

---

## Methodological Notes

### Sample Comparability
- Both datasets: Twitter/X
- Both periods: 2022
- Both samples: Engagement-stratified
- N similar: 339 vs 380

### Reliability Caveats
- Ukraine: Claude-Kimi consensus (55.2% agreement); GLM excluded due to INFORMATIONAL bias
- MahsaAmini: Claude single-model coding (prior study)
- **Limitation:** Different coding approaches may inflate apparent differences

### Next Steps for Publication Quality
1. Code MahsaAmini with 3 models for reliability parity
2. Statistical test for frame distribution differences (χ²)
3. Regression: Does context predict frame, controlling for language/engagement?

---

## Key Takeaway

> **The same frames exist in both contexts, but their prevalence tells the story:**
> - War = "Here's what's happening" (INFORMATIONAL)
> - Protest = "We are together" (SOLIDARITY)
> 
> Frame dominance reflects movement function, not just content differences.

---

*Analysis conducted: 2026-03-04*  
*Analyst: Claude (main session)*  
*Source data: ukraine_codings_claude.json, ukraine_codings_kimi.json, claude_mahsa_commdaaf_final.json*
