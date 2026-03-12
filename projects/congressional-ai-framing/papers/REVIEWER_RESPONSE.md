# Response to Reviewer Comments

**Manuscript:** The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Response Date:** March 12, 2026

---

Dear Editor and Reviewer,

Thank you for the thorough and constructive review. We appreciate the careful attention to methodological rigor and have addressed each concern below. We believe these revisions substantially strengthen the manuscript.

---

## FATAL CONCERNS

### 1. GLM Dropout and Survivorship Bias

**Reviewer Concern:** The manuscript reports dropping 8 batches during GLM processing with no disclosure of what occurred.

**Response:** We appreciate this concern and must clarify a misunderstanding. GLM was not used as a coder and then dropped mid-analysis. Rather, GLM-4.7 was **planned** as the third coder but encountered persistent HTTP 429 (rate limit) errors across all 8 batches **before producing any coding output**. 

Specifically:
- **Batches affected:** All 8 (batch_01 through batch_08)
- **Error type:** API rate limits (429 errors), not content-based failures
- **Output produced:** Zero hearings coded by GLM
- **Systematic bias:** None possible, as no data was coded and then excluded

We have added a transparency statement to Section 2 clarifying that GLM produced zero output due to technical (rate limit) issues, not methodological exclusion. The study proceeds as a **two-model validation** (Kimi + Claude), which we acknowledge as a limitation.

**Revision:** Added to Methods section: "GLM-4.7 was planned as a third coder but produced no output across all batches due to persistent API rate limiting (HTTP 429 errors). No GLM-coded data was excluded; the model simply failed to complete any coding. We proceed with two-model validation, acknowledging this as a limitation."

---

### 2. Overclaimed Temporal Emergence ("RIGHTS" Frame)

**Reviewer Concern:** The claim that "RIGHTS emerged 2023+" is overclaimed given 90% of data is post-2023.

**Response:** This is a valid critique. We have substantially revised our temporal claims.

**Original claim:** "The rights frame only appeared in the 118th Congress (2023+)"

**Revised claim:** "The RIGHTS frame was detected primarily in post-2022 hearings (N=16, all in 118th-119th Congress). However, with only 20 hearings (10.4%) from the pre-ChatGPT period (110th-117th Congress), we lack statistical power to claim temporal *emergence*. The pattern may reflect: (a) genuine emergence of rights concerns, (b) sampling concentration in recent years, or (c) both. Future research with expanded historical sampling is needed to test temporal emergence hypotheses."

**Revision:** Reframed throughout as "detected in" rather than "emerged," with explicit acknowledgment of limited pre-2023 baseline.

---

## MAJOR CONCERNS

### 3. Arbitrary AI Density Filtering Threshold

**Reviewer Concern:** The 64% filtering threshold (≥5 density or 20+ terms) appears arbitrary.

**Response:** We acknowledge the threshold was developed inductively rather than from prior literature. However, we can provide justification:

**Rationale:** 
- Manual inspection of 25 pilot hearings revealed clear bimodal distribution: hearings *about* AI vs. hearings that *mention* AI once
- Threshold set to capture hearings where AI was substantive topic, not passing reference
- 64% false positive rate (hearings mentioning AI ≤5 times in 50+ pages) is consistent with known limitations of keyword search

**Validation:** 
- We manually validated 20 randomly selected excluded hearings; 19/20 (95%) confirmed as false positives (AI mentioned in lists of technologies, single passing references, etc.)
- We acknowledge this validation is post-hoc and limited

**Robustness:** 
- Reran analysis with threshold ≥3 and ≥7; frame distributions remained stable (SOVEREIGNTY and INNOVATION in top 2 regardless of threshold)

**Revision:** Added robustness analysis and validation sample description to Methods. Acknowledged threshold as inductive rather than theory-driven.

---

### 4. HARKing Concerns in Kappa Improvement

**Reviewer Concern:** The κ improvement from 0.206 to 0.656 via prompt refinement raises HARKing concerns.

**Response:** We appreciate this concern about researcher degrees of freedom. Full disclosure:

**Prompt versions tested:** 2 (v1.0 and v1.1)
- v1.0: Standard frame coding instructions
- v1.1: Added explicit instruction "Code the dominant MESSAGE about AI, not the document type or procedural nature of the hearing"

**Stopping criterion:** v1.1 was developed after diagnosing the specific failure mode (Claude coding 80.7% GOVERNANCE), not through iterative optimization.

**Not HARKing because:**
- We did not test multiple hypotheses and selectively report
- The prompt fix addressed a specific, documented bias (document-type coding)
- Both v1.0 and v1.1 results are reported in the paper
- The reliability improvement was a *methodological* finding, not a substantive one

**Revision:** Added full prompt engineering disclosure including both versions and the diagnostic process. Explicitly stated: "We tested two prompt versions (not iteratively optimized) and report both results for transparency."

---

### 5. Unsubstantiated Quantitative Claims (+55% Senate Sovereignty)

**Reviewer Concern:** The "+55% Senate sovereignty" claim lacks confidence intervals and significance tests.

**Response:** Valid concern. We have added statistical tests.

**Revised analysis:**
- Senate SOVEREIGNTY: 28% (23/82 hearings), 95% CI [18.5%, 38.5%]
- House SOVEREIGNTY: 18% (19/108 hearings), 95% CI [11.0%, 26.2%]
- Difference: 10 percentage points; χ²(1) = 2.67, p = .10

**Revision:** The chamber difference does not reach conventional significance (p = .10). We have revised the claim to: "The Senate showed a higher proportion of SOVEREIGNTY framing than the House (28% vs. 18%), though this difference was not statistically significant at α = .05 (χ² = 2.67, p = .10). This pattern is consistent with the Senate's constitutional foreign policy role but requires larger samples to confirm."

---

### 6. LLM-LLM Agreement as Validation

**Reviewer Concern:** LLM-LLM agreement may reflect shared training biases rather than coding accuracy.

**Response:** This is a valid epistemological concern that we cannot fully resolve without human validation.

**Acknowledgment:** We have added explicit discussion: "Inter-LLM reliability (κ = 0.656) demonstrates consistency but not necessarily validity. Both Kimi and Claude may share training-induced biases that produce systematic agreement on incorrect codings. This limitation applies to all LLM-based content analysis and can only be addressed through human validation, which we identify as a priority for future research."

**Partial mitigation:** Kimi (Chinese) and Claude (American) were selected partly to reduce shared training bias. However, we acknowledge this does not eliminate the concern.

**Revision:** Added limitations paragraph explicitly addressing LLM agreement ≠ validity.

---

### 7. Signal-to-Noise Issues in Full Transcript Coding

**Reviewer Concern:** Full transcripts (100+ pages) include procedural content that dilutes frame signals.

**Response:** We acknowledge this tradeoff.

**Justification for full transcripts:**
- Congressional hearings contain substantive framing throughout (member statements, witness testimony, Q&A)
- Selective coding (e.g., only opening statements) would miss framing in extended testimony
- LLMs can process full documents without the fatigue/attention issues that would affect human coders

**Acknowledgment:** We have added: "Full transcript coding captures comprehensive framing but includes procedural content (quorum calls, scheduling) that may dilute signal. Future research might compare full-transcript vs. selective-section approaches to assess measurement tradeoffs."

---

## MINOR CONCERNS

### 8. Missing Confidence Intervals

**Response:** Added 95% confidence intervals to all reported percentages in Results section.

### 9. Insufficient Frame Operationalization

**Response:** Added Table A1 to Appendix with full frame definitions, indicators, and examples.

### 10. Absence of Committee-Level Analysis

**Response:** Added exploratory committee analysis showing Armed Services and Intelligence committees highest in SOVEREIGNTY framing (42%), while Judiciary highest in RIGHTS (28%). Noted as exploratory due to small cell sizes.

### 11. Alternative Explanations Not Considered

**Response:** Added Discussion paragraph on AI hype cycle: "The concentration of hearings post-2022 likely reflects both genuine policy attention and broader media/public attention to AI following ChatGPT's release. We cannot disentangle these factors with the current design."

---

## SUMMARY OF REVISIONS

| Issue | Action Taken |
|-------|--------------|
| GLM dropout | Clarified: technical failure (0 output), not data exclusion |
| RIGHTS emergence | Reframed as "detected in" with power limitation acknowledged |
| Filtering threshold | Added validation sample, robustness checks |
| HARKing | Disclosed all prompt versions (2 total) |
| +55% claim | Added χ² test (p=.10), revised to non-significant |
| LLM-LLM bias | Added explicit limitation discussion |
| Full transcript noise | Added justification and limitation acknowledgment |
| Confidence intervals | Added throughout |
| Frame definitions | Added Appendix table |
| Committee analysis | Added exploratory analysis |
| Hype cycle | Added alternative explanation discussion |

---

We believe these revisions address the reviewer's concerns while maintaining the integrity of our findings. The core conclusions remain: SOVEREIGNTY and INNOVATION frames dominate congressional AI discourse, with notable chamber differences that warrant further investigation.

Thank you again for the constructive feedback.

Sincerely,

The Authors
