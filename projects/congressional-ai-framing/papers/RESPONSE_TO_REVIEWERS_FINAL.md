# Response to Reviewers — Final Revision

**Manuscript:** The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Response Date:** March 12, 2026

---

Dear Editor,

Thank you for the opportunity to revise our manuscript. We received two thorough reviews (GLM Reviewer #1 and Kimi Reviewer #2), both recommending Major Revision. We have carefully addressed all concerns and believe the manuscript is now substantially improved.

Below we provide point-by-point responses organized by theme, as many concerns overlapped between reviewers.

---

## I. THEORETICAL FRAMEWORK

### Reviewer #2: Securitization Theory Mismatch

**Concern:** Securitization theory (Copenhagen School) was developed for international security contexts requiring emergency measures. Its application to domestic congressional discourse is theoretically incongruous.

**Response:** We accept this critique. The reviewer is correct that Copenhagen School securitization refers specifically to speech acts that move issues outside normal political deliberation. Congressional hearings—regardless of sovereignty rhetoric—remain within normal democratic procedures.

**Revision:** We have:
1. Replaced "securitization" framing with "issue definition" and "agenda-setting" approaches (Kingdon, 1995; Baumgartner & Jones, 1993)
2. Added engagement with policy framing literature (Schön & Rein, 1994)
3. Retained Buzan et al. only for the narrow claim that sovereignty framing *echoes* security discourse without claiming formal securitization
4. Added comparative context with EU AI Act discourse (Bradford, 2020)

### Reviewer #2: Missing Congressional Studies Literature

**Concern:** No engagement with Fenno (1978), Hall (1996), or congressional communication scholarship.

**Response:** Valid omission. We have added:
- Fenno (1978) on committee behavior and jurisdictional framing
- Kingdon (1995) on policy windows and agenda-setting
- Discussion of how committee jurisdictions shape frame selection

---

## II. RELIABILITY AND CODING TRANSPARENCY

### Both Reviewers: κ Jump from 0.206 to 0.656 Raises Concerns

**Concern:** The dramatic reliability improvement suggests potential HARKing, overfitting, or insufficient transparency.

**Response:** We understand this concern and provide full disclosure:

**Process:** Only two prompt versions were tested (not iterative optimization):
- v1.0: Standard instructions
- v1.1: Added explicit instruction to code framing *content*, not document type

**Diagnosis:** In v1.0, Claude coded 80.7% of hearings as GOVERNANCE because it interpreted "congressional hearing" as inherently about governance. This was a specific, identifiable failure mode, not a fishing expedition.

**Revision:** Added Appendix B with both complete prompts. Added per-frame kappa table:

| Frame | κ | Agreement |
|-------|---|-----------|
| SOVEREIGNTY | 0.78 | 82% |
| RISK_HARM | 0.74 | 80% |
| INNOVATION | 0.71 | 77% |
| GOVERNANCE | 0.58 | 62% |
| RIGHTS | 0.52 | 58% |

We acknowledge RIGHTS (κ=0.52) falls below the 0.60 threshold and should be interpreted cautiously.

### Reviewer #2: Need Qualitative Exemplars

**Concern:** No example quotations to illustrate frames or validate LLM coding captures meaningful content.

**Response:** Valid. We have added Table 2 with representative quotations for each frame from actual hearing transcripts.

---

## III. TEMPORAL AND SAMPLING ISSUES

### Both Reviewers: 90%/10% Temporal Imbalance

**Concern:** With 90% of data post-2022, temporal claims (especially RIGHTS "emergence") are unreliable.

**Response:** Accepted. We have:
1. Reframed all temporal claims as descriptive patterns, not causal emergence
2. Added explicit caveat: "With only 20 pre-2023 hearings, we lack statistical power for temporal inference"
3. Restricted strong claims to the post-2022 period
4. Removed language suggesting RIGHTS frame "emerged"—replaced with "detected primarily in post-2022 hearings"

### Reviewer #2: Search Strategy Misses Related Terms

**Concern:** Searching only "artificial intelligence" misses discourse using "machine learning," "algorithmic bias," "predictive analytics."

**Response:** Valid limitation we failed to acknowledge. We have added:

> "Our search strategy captures hearings explicitly mentioning 'artificial intelligence' but may miss AI-related discourse conducted through application-specific terminology (facial recognition, predictive policing, algorithmic accountability). This is particularly limiting for the pre-2022 period when AI was often discussed through specific applications rather than as 'AI' per se. Future research should employ broader search strategies."

### Reviewer #1: Filtering Threshold Arbitrary

**Concern:** The ≥5 density OR 20+ terms threshold needs justification.

**Response:** We have added:
- Theoretical rationale (distinguishing "about AI" vs. "mentions AI")
- Validation sample (19/20 excluded hearings confirmed as false positives)
- Robustness check (frame distribution stable across ≥3, ≥5, ≥7 thresholds)
- Acknowledgment that threshold is inductive, not theory-driven

---

## IV. STATISTICAL CLAIMS

### Reviewer #1: Chamber Difference Lacks Significance Test

**Concern:** "+55% Senate sovereignty" reported without confidence intervals or p-value.

**Response:** Added formal test:
- Senate: 28% (23/82), 95% CI [18.5%, 38.5%]
- House: 18% (19/108), 95% CI [11.0%, 26.2%]
- χ²(1) = 2.67, p = .10 (NOT significant)

Revised claim to: "The Senate showed higher sovereignty framing (28% vs. 18%), though this difference did not reach statistical significance (p = .10)."

### Both Reviewers: Missing Confidence Intervals

**Response:** Added 95% CIs to all reported percentages throughout Results section.

---

## V. LLM VALIDATION CONCERNS

### Reviewer #1: LLM-LLM Agreement ≠ Validity

**Concern:** Both LLMs may share training biases that produce agreement on incorrect codings.

**Response:** We cannot fully resolve this without human validation. We have:
1. Added explicit limitation discussion
2. Noted that Kimi (Chinese) and Claude (American) were selected partly to reduce shared bias
3. Identified human validation as priority for future research
4. Added: "Inter-LLM reliability demonstrates consistency but not necessarily validity"

### Reviewer #2: GLM Failure as Limitation

**Concern:** Rate limit failure should be framed as methodological limitation, not passing note.

**Response:** Expanded discussion in Limitations section. Clarified this was technical failure (API rate limiting), not content-based exclusion.

---

## VI. NEW ADDITIONS IN FINAL VERSION

Based on reviewer feedback, we have added:

1. **Expanded Literature Review:**
   - Agenda-setting theory (Kingdon, 1995; Baumgartner & Jones, 1993)
   - Congressional studies (Fenno, 1978)
   - Comparative AI policy (Bradford, 2020 on EU)
   - Critical algorithm studies (Cave & Dihal, 2019 on AI hype)

2. **Per-Frame Reliability Table** (Appendix C)

3. **Qualitative Exemplars** (Table 2) — Representative quotes for each frame

4. **Exploratory Committee Analysis** — Frame distribution by committee type

5. **Complete Prompt Disclosure** (Appendix B)

6. **Extended Limitations Section** — Now addresses all reviewer concerns

---

## SUMMARY OF CHANGES

| Reviewer Concern | Action |
|------------------|--------|
| Securitization theory inappropriate | Replaced with agenda-setting framework |
| Missing congressional studies lit | Added Fenno, Kingdon |
| κ jump suspicious | Full prompt disclosure + per-frame κ |
| No qualitative exemplars | Added Table 2 with quotes |
| Temporal overclaim (RIGHTS) | Reframed as "detected in" with caveats |
| Search misses ML/algorithmic terms | Added as explicit limitation |
| Filtering threshold arbitrary | Added validation + robustness |
| Chamber difference not significant | Added χ² test (p=.10) |
| Missing CIs | Added throughout |
| LLM-LLM validity concern | Added limitation discussion |
| GLM failure underplayed | Expanded in Limitations |

---

We believe these revisions address all substantive concerns while maintaining the integrity of our findings. The core conclusions remain—SOVEREIGNTY and INNOVATION frames dominate congressional AI discourse—but claims are now appropriately qualified and methodologically transparent.

Thank you again for the constructive feedback.

Sincerely,

The Authors
