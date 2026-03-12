# Congressional AI Framing Study - Preliminary Results

**Date:** 2026-03-12
**Status:** Exploratory (pending full validation)

## Data
- **Source:** GovInfo API, CHRG collection
- **Query:** "artificial intelligence" in congressional hearings
- **Total collected:** 561 transcripts
- **Valid AI hearings:** 193 (filtered by AI density score)
- **Coded:** 192 hearings

## Inter-Model Reliability

### Pilot (5 hearings, 3 models)
| Pair | Cohen's κ |
|------|-----------|
| Claude-GLM | 0.750 |
| Claude-Kimi | 1.000 |
| GLM-Kimi | 0.750 |
| **Average** | **0.833** |

### Full Sample (High-Density Batches, 2 models)
- N = 49 hearings
- Claude-Kimi κ = 0.528 (Moderate agreement)

**Note:** Lower κ on full sample due to:
1. Faster coding methodology (title + opening only)
2. Legitimate interpretive disagreements
3. Multi-frame hearings difficult to code

## Frame Distribution (Claude, High Confidence N=59)

| Frame | Count | % |
|-------|-------|---|
| GOVERNANCE | 22 | 37.3% |
| INNOVATION | 14 | 23.7% |
| SOVEREIGNTY | 9 | 15.3% |
| RISK_HARM | 8 | 13.6% |
| RISK_SAFETY | 3 | 5.1% |
| RISK_ECONOMIC | 2 | 3.4% |
| RIGHTS | 1 | 1.7% |

## Temporal Trends

| Congress | Years | N | Dominant Frame |
|----------|-------|---|----------------|
| 114-115th | 2015-2018 | 7 | INNOVATION |
| 118th | 2023-2024 | 34 | GOVERNANCE |
| 119th | 2025+ | 11 | INNOVATION |

**Key Finding:** Shift from innovation framing (2015-2018) to governance/regulatory framing (2023-2024), with potential return to innovation framing in 119th Congress.

## Limitations
1. Rate limiting prevented GLM 3-model validation
2. Low-density batches (5-8) coded with defaults
3. Kimi batches 3, 4, 6 failed to save output
4. Single-coder confidence affects reliability

## Next Steps
1. Re-run failed Kimi batches
2. Retry GLM with sequential (not parallel) calls
3. Adjudicate disagreements between Claude and Kimi
4. Full temporal regression analysis
