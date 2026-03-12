# Three-Model Comparison: Pilot Filtered 5 Hearings

**Date:** 2026-03-12
**Models:** Claude (Opus 4.5), GLM-4.7, Kimi K2.5

## Primary Frame Agreement

| Hearing ID | Claude | GLM | Kimi | Agreement |
|------------|--------|-----|------|-----------|
| CHRG-118shrg59704 | RISK_SAFETY | RISK_SAFETY | RISK_SAFETY | ✓✓✓ |
| CHRG-115shrg37295 | INNOVATION | INNOVATION | INNOVATION | ✓✓✓ |
| CHRG-118shrg62427 | RISK_HARM | RISK_HARM | RISK_HARM | ✓✓✓ |
| CHRG-118hhrg53782 | GOVERNANCE | GOVERNANCE | GOVERNANCE | ✓✓✓ |
| CHRG-118hhrg54392 | GOVERNANCE | SOVEREIGNTY | GOVERNANCE | 2/3 |

**Unanimous Agreement:** 4/5 (80%)

## Secondary Frame Agreement

| Hearing ID | Claude | GLM | Kimi | Agreement |
|------------|--------|-----|------|-----------|
| CHRG-118shrg59704 | GOVERNANCE | GOVERNANCE | GOVERNANCE | ✓✓✓ |
| CHRG-115shrg37295 | GOVERNANCE | GOVERNANCE | RISK_ECONOMIC | 2/3 |
| CHRG-118shrg62427 | RIGHTS | GOVERNANCE | RIGHTS | 2/3 |
| CHRG-118hhrg53782 | TECHNICAL | TECHNICAL | TECHNICAL | ✓✓✓ |
| CHRG-118hhrg54392 | SOVEREIGNTY | INNOVATION | SOVEREIGNTY | 2/3 |

**Unanimous Agreement:** 2/5 (40%)

## Inter-Model Reliability (Primary Frame)

| Pair | Cohen's κ | Interpretation |
|------|-----------|----------------|
| Claude-GLM | 0.750 | Substantial |
| Claude-Kimi | 1.000 | Perfect |
| GLM-Kimi | 0.750 | Substantial |
| **Average** | **0.833** | **Almost Perfect** |

## Key Findings

1. **Strong primary frame convergence**: 80% unanimous, κ = 0.833 exceeds standard threshold (0.70) for acceptable reliability

2. **One substantive disagreement**: CHRG-118hhrg54392 ("White House Policy on AI")
   - GLM coded SOVEREIGNTY (emphasized China competition framing)
   - Claude & Kimi coded GOVERNANCE (emphasized EO implementation focus)
   - Both interpretations defensible; hearing has dual framing

3. **Secondary frames more variable**: Expected for inherently subjective secondary coding
   - RIGHTS vs GOVERNANCE (healthcare bias hearing)
   - RISK_ECONOMIC vs GOVERNANCE (2017 innovation hearing)
   - All disagreements involve closely related frames

## Implications for Full Coding

- Primary frame coding shows sufficient reliability for 198-hearing sample
- Consider adjudication protocol for split decisions (2/3 agreement = majority rule)
- May simplify secondary frame to single alternative or drop from analysis

## Next Steps

1. [ ] Majority voting for remaining disagreements
2. [ ] Scale to full 198 valid AI hearings
3. [ ] Frame distribution analysis
4. [ ] Temporal trends (2017-2024)
