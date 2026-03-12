# Congressional AI Framing Study - Key Findings

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Total Hearings Coded** | 192 (Kimi) |
| **Congress Range** | 110th - 119th (2007-2026) |
| **Peak Activity** | 118th Congress (121 hearings) |

---

## Finding 1: AI Discourse Exploded in 2023-2026

| Congress | Years | N Hearings | % of Sample |
|----------|-------|------------|-------------|
| 110-117 | 2007-2022 | 20 | 10% |
| 118 | 2023-2024 | **121** | **63%** |
| 119 | 2025-2026 | 51 | 27% |

**Interpretation**: Congressional attention to AI was minimal until ChatGPT's release (Nov 2022). The 118th Congress saw an explosion of AI hearings — more than all previous Congresses combined.

---

## Finding 2: Frame Distribution

### Overall Distribution (N=192)

| Frame | Count | % | Description |
|-------|-------|---|-------------|
| **SOVEREIGNTY** | 41 | 21.4% | China competition, national security |
| **INNOVATION** | 38 | 19.8% | Economic opportunity, jobs |
| **GOVERNANCE** | 34 | 17.7% | Regulatory frameworks |
| RISK_HARM | 19 | 9.9% | Concrete harms to people |
| RISK_SAFETY | 19 | 9.9% | Catastrophic/existential risks |
| RIGHTS | 17 | 8.9% | Privacy, discrimination |
| RISK_ECONOMIC | 9 | 4.7% | Job displacement |
| TECHNICAL | 5 | 2.6% | Scientific explanations |

**Key insight**: The top 3 frames (SOVEREIGNTY, INNOVATION, GOVERNANCE) account for 59% of hearings. AI is primarily framed as a **geopolitical and economic competition**, not as a risk or rights issue.

---

## Finding 3: Chamber Differences

| Frame | House (N=108) | Senate (N=82) |
|-------|---------------|---------------|
| SOVEREIGNTY | 18% | **28%** |
| INNOVATION | 23% | 15% |
| GOVERNANCE | 23% | 13% |
| RISK_HARM | 9% | **15%** |

**Interpretation**: 
- **Senate** emphasizes national security framing (SOVEREIGNTY) and concrete harms (RISK_HARM)
- **House** has more balanced distribution between INNOVATION and GOVERNANCE
- Both chambers treat AI primarily as opportunity/competition issue

---

## Finding 4: Temporal Evolution of Frames

### Early Period (110th-116th Congress, 2007-2020)
- **Dominant frames**: INNOVATION, RISK_ECONOMIC
- **Narrative**: AI as emerging technology with workforce implications
- **N = 15 hearings** (sparse attention)

### Middle Period (117th Congress, 2021-2022)
- **Rising frame**: SOVEREIGNTY
- **Narrative**: China competition emerging as concern
- **N = 5 hearings**

### Recent Period (118th-119th Congress, 2023-2026)
- **Dominant frames**: SOVEREIGNTY, INNOVATION, GOVERNANCE
- **New frame emergence**: RIGHTS (privacy, algorithmic bias)
- **N = 172 hearings** (90% of sample)

**Pattern**: RIGHTS frame only emerged in 118th Congress — suggests civil liberties concerns are recent addition to AI discourse.

---

## Finding 5: Valence and Urgency

### Valence Distribution
| Valence | % |
|---------|---|
| Positive | 31% |
| Negative | 30% |
| Neutral/Mixed | 39% |

**Interpretation**: Congressional AI discourse is relatively balanced — neither predominantly optimistic nor pessimistic.

### Urgency Distribution
| Urgency | % |
|---------|---|
| High | 44% |
| Medium | 50% |
| Low | 6% |

**Interpretation**: Strong sense of urgency across hearings — consistent with "AI race" framing.

---

## Methodological Notes

### Inter-Rater Reliability
| Version | Agreement | Cohen's κ | Interpretation |
|---------|-----------|-----------|----------------|
| Claude v1 vs Kimi | 35.8% | 0.206 | Fair |
| **Claude v2 vs Kimi** | **72.4%** | **0.656** | **Substantial** |

The improved prompt (v1.1) fixed Claude's tendency to over-code GOVERNANCE, raising reliability from "Fair" to "Substantial" agreement.

### Limitations
1. GLM dropped from study (rate limits, no output)
2. 16 hearings coded by Claude only (Kimi token limit)
3. AI density threshold (≥5) may exclude brief AI discussions
4. Frame coding based on transcript text, not video/witness identity

---

## Research Implications

1. **Securitization of AI**: SOVEREIGNTY frame dominance suggests AI policy is increasingly viewed through national security lens

2. **Economic optimism**: INNOVATION remains strong, especially in House — suggests bipartisan support for AI development

3. **Rights frame emerging**: Recent appearance of RIGHTS frame suggests privacy/bias concerns gaining traction

4. **Regulatory uncertainty**: GOVERNANCE frame presence but not dominance suggests policy approaches still being debated

---

*Analysis date: 2026-03-12*
*Coder: Kimi K2.5 via CommDAAF v1.1*
