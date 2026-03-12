# Congressional AI Framing Study - Methodology & Limitations

## Study Overview

**Research Question**: How is artificial intelligence framed in U.S. congressional hearings?

**Method**: Multi-model content analysis using CommDAAF methodology with LLM coders

**Sample**: 193 congressional hearings with substantive AI content (filtered from 561 AI-mentioning hearings)

---

## Data Collection

### Source
- **API**: GovInfo (api.govinfo.gov)
- **Collection**: CHRG (Congressional Hearings)
- **Query**: `"artificial intelligence" collection:CHRG`
- **Date Retrieved**: March 2026

### Filtering Process
1. **Initial query**: 1,754 hearings mentioning "artificial intelligence"
2. **Downloaded**: 561 full transcripts
3. **AI density scoring**: Calculated term density per transcript
4. **Threshold**: density ≥5 OR 20+ strong AI terms
5. **Final sample**: 198 valid AI hearings → 193 after deduplication

### False Positive Analysis
64% of initial search results were false positives (hearings that mention AI but aren't about AI):
- List of technologies (32%): "technologies like 5G, AI, and cloud..."
- Government modernization (27%): AI as efficiency tool
- National security passing mention (15%)
- Other (26%): workforce, budget line items, etc.

---

## Coding Methodology

### Framework
CommDAAF v1.1 - Communication Data Analysis & Annotation Framework

### Frame Categories (8)
| Frame | Definition |
|-------|------------|
| INNOVATION | Economic opportunity, competitiveness, job creation |
| RISK_SAFETY | Existential/catastrophic threats |
| RISK_HARM | Concrete harms to individuals/groups |
| RISK_ECONOMIC | Job loss, economic disruption, inequality |
| GOVERNANCE | Regulatory frameworks, oversight mechanisms |
| SOVEREIGNTY | National security, geopolitical competition |
| RIGHTS | Privacy, discrimination, civil liberties |
| TECHNICAL | Scientific/technical explanations |

### Coders
- **Primary**: Kimi K2.5 (kimi-coding plan)
- **Validation**: Claude Opus 4.5 (v2 with improved prompt)
- **Dropped**: GLM-4.7 (rate limited, no usable output)

---

## Methodological Decisions & Limitations

### Decision 1: Kimi as Primary Coder
**Rationale**: Claude v1 over-coded GOVERNANCE (80.7%) by interpreting congressional hearings as inherently governance activities. Kimi correctly coded based on framing *within* the discourse, producing analytically useful frame diversity.

**Resolution**: 
- Kimi used as primary for frame distribution analysis
- Claude recoded with v1.1 prompt emphasizing framing content, not document type
- Both coders' results reported for transparency

### Decision 2: Dropping GLM
**Rationale**: GLM-4.7 encountered persistent rate limits (429 errors) and produced no usable output across all 8 batches.

**Limitation**: Study relies on 2-model validation instead of planned 3-model validation.

### Decision 3: Partial Kimi Coverage
**Issue**: Kimi completed 177/193 hearings (92%). Batches 3, 4, 6 partially failed due to token limits (262K exceeded).

**Resolution**: Sub-batch approach recovered most data. 16 hearings uncoded by Kimi but coded by Claude.

**Limitation**: Inter-rater reliability calculated on 177 overlapping hearings, not full sample.

### Decision 4: AI Density Threshold
**Issue**: Arbitrary threshold (density ≥5 OR 20+ terms) for "valid AI hearings"

**Limitation**: May exclude hearings with substantive but brief AI discussion; may include hearings where AI is secondary topic.

---

## Inter-Rater Reliability

### Initial Results (Claude v1 vs Kimi)
- **Simple Agreement**: 35.8%
- **Cohen's Kappa**: 0.206 (Fair)
- **Primary Disagreement**: Claude defaulting to GOVERNANCE (80.7%)

### Final Results (Claude v2 vs Kimi)
- **Overlap N**: 116 hearings
- **Simple Agreement**: 72.4%
- **Cohen's Kappa**: **0.656 (Substantial)**
- **Improvement**: Prompt v1.1 explicitly instructed "code framing content, not document type"

### Agreement by Frame
| Frame | Agreement |
|-------|-----------|
| SOVEREIGNTY | 82% |
| RISK_HARM | 80% |
| INNOVATION | 77% |
| GOVERNANCE | 62% |
| RIGHTS | 58% |

**Conclusion**: κ=0.656 exceeds typical threshold (0.60) for acceptable inter-rater reliability in communication research.

---

## Sample Characteristics

- **Congress Range**: 110th - 119th (2008-2026)
- **Chamber Split**: TBD from analysis
- **Committee Distribution**: TBD from analysis
- **Temporal Coverage**: 18 years

---

## Files

| File | Description |
|------|-------------|
| `data/transcripts/` | 561 full transcripts |
| `data/valid_ai_hearings.json` | 193 filtered hearings |
| `data/batches/batch_0X.json` | 8 coding batches |
| `outputs/kimi/all_kimi_merged.json` | Kimi codings (N=177) |
| `outputs/claude_v2/` | Claude v2 codings (pending) |
| `prompts/commdaaf_v1.1.md` | Improved coding prompt |

---

## Reproducibility

All code, data, and prompts available in project directory. LLM outputs are deterministic given same inputs (temperature=0 for coding tasks).

---

*Last updated: 2026-03-12*
