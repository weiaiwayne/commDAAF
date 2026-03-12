# Congressional AI Framing Study

## Research Questions

**RQ1:** How is artificial intelligence framed in U.S. congressional hearings?

**RQ2:** How have AI frames evolved over time (pre-ChatGPT vs post-ChatGPT)?

**RQ3:** Do framing patterns differ between House and Senate hearings?

**RQ4:** Which frames predict greater media coverage and policy action?

---

## Corpus Summary

| Metric | Value |
|--------|-------|
| Total hearings | 61 |
| Date range | 2008-2025 |
| Chambers | House (36), Senate (24), Joint (1) |
| Total text | ~9 MB |

### Temporal Distribution
- **Pre-ChatGPT (2008-2022):** 22 hearings
- **Post-ChatGPT (2023-2025):** 39 hearings

---

## Frame Codebook v1.0

### Primary Frames

| Frame | Code | Definition | Indicators |
|-------|------|------------|------------|
| **ECONOMIC_OPPORTUNITY** | ECO | AI as driver of growth, competitiveness, jobs | innovation, leadership, competitiveness, economic growth, jobs creation, productivity, American companies |
| **NATIONAL_SECURITY** | SEC | AI as defense/intelligence asset or threat | China, adversaries, defense, military, intelligence, strategic competition, national security |
| **EXISTENTIAL_RISK** | EXI | AI as potential civilizational threat | alignment, extinction, superintelligence, control problem, existential, catastrophic |
| **REGULATION_GOVERNANCE** | REG | AI requiring oversight and rules | oversight, accountability, transparency, regulation, guardrails, legislation, standards |
| **CIVIL_RIGHTS** | CIV | AI and bias, privacy, discrimination | bias, discrimination, fairness, privacy, civil liberties, surveillance, consent |
| **LABOR_AUTOMATION** | LAB | AI impact on workforce | displacement, automation, workforce, reskilling, jobs loss, workers |
| **HEALTHCARE** | HEA | AI in medical applications | diagnosis, treatment, patients, healthcare, medical, clinical |
| **CONSUMER_PROTECTION** | CON | AI risks to consumers | scams, fraud, deepfakes, misinformation, consumer harm |

### Secondary Codes

| Code | Definition |
|------|------------|
| **VALENCE_POS** | Positive framing (opportunity, benefit) |
| **VALENCE_NEG** | Negative framing (risk, threat, harm) |
| **VALENCE_NEU** | Neutral/balanced framing |
| **ACTOR_GOV** | Government as primary actor |
| **ACTOR_IND** | Industry as primary actor |
| **ACTOR_ACAD** | Academia/researchers as primary actor |
| **URGENCY_HIGH** | Immediate action needed |
| **URGENCY_LOW** | More study/deliberation needed |

### Coding Rules

1. **Unit of analysis:** Individual speaker turn (testimony segment)
2. **Multiple frames allowed:** Code all applicable frames per turn
3. **Primary frame required:** Select ONE dominant frame
4. **Valence required:** Every coded segment needs valence
5. **Context window:** Consider 2 sentences before/after for context

### Decision Rules

- If ECONOMIC and SECURITY both present → code based on which is *justified by* (means vs. end)
- If EXISTENTIAL mentioned but in dismissive context → code as REGULATION + note
- If "jobs" mentioned → distinguish creation (ECO) vs. loss (LAB) by context
- If China mentioned → only code SEC if framed as *adversary/threat*, not mere comparison

---

## Sampling Strategy

### Stratified Sample (N=200 segments)

| Stratum | Criteria | Target N |
|---------|----------|----------|
| Pre-ChatGPT House | 2008-2022, House | 30 |
| Pre-ChatGPT Senate | 2008-2022, Senate | 30 |
| Post-ChatGPT House (2023) | 2023, House | 35 |
| Post-ChatGPT Senate (2023) | 2023, Senate | 35 |
| Post-ChatGPT House (2024-25) | 2024-2025, House | 35 |
| Post-ChatGPT Senate (2024-25) | 2024-2025, Senate | 35 |

### Segment Extraction

1. Parse transcripts into speaker turns
2. Filter to substantive testimony (>100 words, exclude procedural)
3. Random sample within each stratum
4. Ensure no more than 3 segments per hearing

---

## Validation Tier

**🟡 PILOT** (2-4 hours)
- Human validation: N ≥ 100
- Inter-coder reliability: κ ≥ 0.6
- Multi-model validation: 3 models

---

## AgentAcademy Protocol

### Phase 1: Data Preparation
- [x] Collect hearing transcripts (61 hearings)
- [ ] Parse into speaker segments
- [ ] Generate stratified sample (N=200)
- [ ] Export to coding format

### Phase 2: Independent Coding
- [ ] Claude codes full sample
- [ ] GLM-4.7 codes full sample  
- [ ] Kimi K2.5 codes full sample

### Phase 3: Agreement Analysis
- [ ] Calculate per-frame κ
- [ ] Identify systematic disagreements
- [ ] Flag low-agreement frames (<50%)

### Phase 4: Human Adjudication
- [ ] Review all 3-way disagreements
- [ ] Resolve with gold standard
- [ ] Document decision rationale

### Phase 5: Analysis
- [ ] Frame distribution by period
- [ ] Frame distribution by chamber
- [ ] Temporal trends visualization
- [ ] Chi-square tests for H1-H3

### Phase 6: Adversarial Review
- [ ] Each model writes "Reviewer 2" critique
- [ ] Address methodological concerns
- [ ] Revise findings if needed

---

## Hypotheses

**H1:** Post-ChatGPT hearings show increased EXISTENTIAL_RISK framing compared to pre-ChatGPT.

**H2:** Senate hearings emphasize REGULATION_GOVERNANCE more than House hearings.

**H3:** NATIONAL_SECURITY framing increases over time, driven by US-China competition.

**H4:** ECONOMIC_OPPORTUNITY framing is positively associated with industry witness testimony.

---

## Output Files

```
congressional-ai-framing/
├── STUDY_DESIGN.md          # This file
├── collect_hearings.py      # Data collection script
├── data/
│   ├── hearings_metadata.json
│   ├── corpus_summary.json
│   └── transcripts/         # 61 hearing transcripts
├── coding/
│   ├── sample_segments.json # Stratified sample
│   ├── claude_codes.json
│   ├── glm_codes.json
│   └── kimi_codes.json
└── analysis/
    ├── agreement_report.md
    ├── frame_distributions.png
    └── findings.md
```

---

## Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Data collection | 1 hour | ✅ Complete |
| Segment extraction | 30 min | Pending |
| 3-model coding | 2 hours | Pending |
| Agreement analysis | 30 min | Pending |
| Human adjudication | 1 hour | Pending |
| Analysis & writing | 2 hours | Pending |

**Total estimated time:** 6-7 hours

---

## References

- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm.
- Chong, D., & Druckman, J. N. (2007). Framing theory.
- Brossard, D. (2013). New media landscapes and the science information consumer.
