**Peer Review Report**

**Manuscript:** The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Reviewer Recommendation:** Major Revision

---

Dear Editor and Authors,

Thank you for the opportunity to review this manuscript, which addresses an important and timely question: how artificial intelligence is framed in U.S. Congressional discourse. The authors present a multi-model content analysis of 192 hearings, employing both human and LLM-based coding to identify dominant frames. The research question is both theoretically and practically significant, particularly given AI's rapidly growing role in policy discourse.

I commend the authors for their transparency regarding methodological challenges and their ambitious sample size. The inter-rater reliability framework is well-structured, and the manuscript addresses a genuine gap in our understanding of AI's evolving framing in political contexts. However, several substantive concerns—particularly regarding data integrity, methodological arbitrariness, and statistical rigor—must be addressed before this work can be considered for publication.

Below, I outline my concerns organized by severity.

---

### FATAL CONCERNS

**1. GLM Dropout and Survivorship Bias**

The manuscript reports dropping 8 batches during GLM processing but provides no disclosure of what occurred or whether these deletions were systematic. This creates a substantial survivorship bias that fundamentally undermines the integrity of the findings. The authors must:

- Detail precisely which batches were dropped, when, and why
- Demonstrate that deletions were not systematic (e.g., not correlated with particular committees, time periods, or frame distributions)
- Consider sensitivity analyses or re-analysis with retained batches

Without full disclosure, readers cannot assess whether the patterns reported reflect genuine discourse trends or data culling artifacts.

**2. Overclaimed Temporal Emergence ("RIGHTS" Frame)**

The manuscript claims the "RIGHTS" frame emerged only after 2023, yet approximately 90% of the data is post-2023. This constitutes insufficient pre-2023 data to support such a strong temporal claim. The authors should:

- Report the exact proportion of data pre- versus post-2023
- Refine temporal claims to reflect data limitations
- Consider whether "emerged" is appropriate given the limited baseline
- If possible, expand pre-2023 coverage to enable robust temporal comparison

---

### MAJOR CONCERNS

**3. Arbitrary AI Density Filtering Threshold**

The AI density filtering process removed 64% of hearings using thresholds of ≥5 or 20+ AI-related terms. This threshold appears entirely arbitrary, with no justification, validation, or human reliability assessment. To address this:

- Provide theoretical or empirical justification for the chosen thresholds
- Report how results vary across alternative thresholds (robustness checks)
- Conduct human validation on a subsample of excluded hearings to confirm they are substantively AI-irrelevant
- Consider whether a graded inclusion scheme (rather than binary filtering) might be more appropriate

**4. HARKing Concerns in Kappa Improvement**

The manuscript reports kappa improving dramatically from 0.206 to 0.656 via "prompt refinement," with no disclosure of how many prompt versions were tested. This raises substantial HARKing (Hypothesizing After Results are Known) concerns. The authors must:

- Disclose the full sequence of prompt versions tested and their performance metrics
- Explain the criteria for stopping iteration
- Consider pre-registering or explicitly acknowledging this iterative exploration
- Distinguish between a priori design choices and post-hoc refinements

**5. Unsubstantiated Quantitative Claims**

The finding of "+55% Senate sovereignty" is reported without confidence intervals or significance tests, making it impossible to assess whether this represents a genuine effect or sampling variability. This is particularly problematic given:

- The sample size may not support such precise percentage estimates
- No standard errors are reported for any proportional claims
- Statistical significance is not addressed for key findings

All quantitative claims should be accompanied by appropriate uncertainty estimates and significance tests where applicable.

**6. LLM-LLM Agreement as Validation**

The manuscript uses agreement between different LLMs (GLM and GPT-4) as validation, but this may simply reflect shared training biases rather than true coding accuracy. LLMs trained on similar corpora may systematically encode the same misconceptions or framing assumptions. The authors should:

- Acknowledge this limitation explicitly
- Compare LLM coding to human coding on a validation subsample (not just reliability testing)
- Consider whether convergence between LLMs provides meaningful independent validation

**7. Signal-to-Noise Issues in Full Transcript Coding**

Coding full transcripts averaging 100+ pages introduces substantial signal-to-noise problems. Congressional hearings contain lengthy procedural content, constituent testimony, and irrelevant digressions that may dilute frame signals. The authors should:

- Justify why full transcripts are necessary versus, for example, prepared statements or question-and-answer periods
- Report the proportion of content that is procedurally or substantively irrelevant
- Consider whether coding focused sections would improve measurement precision

---

### MINOR CONCERNS

**8. Missing Confidence Intervals**

Confidence intervals are absent from all percentage-based results. Given the sample sizes involved, readers need to understand the precision of these estimates.

**9. Insufficient Frame Operationalization**

The manuscript does not specify how frames were operationalized for coding. What specific words, phrases, or semantic patterns indicate each frame? This is essential for reproducibility and theoretical clarity.

**10. Absence of Committee-Level Analysis**

No analysis is presented at the committee level, despite substantial theoretical reasons to expect frame variation across committees with different jurisdictions and constituencies.

**11. Alternative Explanations Not Considered**

The manuscript does not discuss the AI hype cycle as an alternative explanation for observed temporal patterns. Media and public attention to AI surged dramatically in 2022-2023, which could independently drive framing changes. This alternative explanation should be engaged.

---

### STRENGTHS

- The research question is both important and timely
- The sample size (N=192) is substantial and provides a strong foundation for analysis
- The inter-rater reliability framework is conceptually sound
- The authors display commendable transparency about methodological challenges and failures
- The multi-model approach (human + LLM coding) is innovative and worthy of further development

---

### RECOMMENDATION

**I recommend Major Revision.**

The manuscript addresses a significant research question with ambitious methodology and substantial data. However, the fatal concerns—particularly the undisclosed GLM batch deletions and the overclaimed temporal emergence—must be fully resolved before reconsideration. The major concerns require substantial clarification, revision, and in some cases re-analysis.

The following conditions should be met for reconsideration:

1. Complete disclosure of GLM batch deletions with systematicity assessment
2. Revision of temporal claims to reflect data limitations or pre-2023 data expansion
3. Justification and robustness testing of AI density filtering thresholds
4. Full disclosure of prompt iteration process to address HARKing concerns
5. Addition of confidence intervals and significance tests to all quantitative claims
6. Clarification of LLM validation strategy, ideally with human benchmarking
7. Justification for full-transcript coding approach or alternative methods

If the authors can address these concerns thoroughly, this manuscript has the potential to make a meaningful contribution to the literature on AI framing in political discourse. The methodological innovation, if rigorously validated, could serve as a model for future computational communication research.

Thank you again for the opportunity to review this work.

---

Sincerely,

[Reviewer Name]
[Institution]
[Date]
