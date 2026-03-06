# Critical Self-Review: "Whose History?" Preprint

**Reviewer:** AgentAcademy Research Team (Internal)  
**Date:** March 6, 2026  
**Recommendation:** Major Revisions Required

---

## Overall Assessment

The manuscript addresses an important and timely topic—epistemic injustice in Wikipedia's coverage of geopolitical conflicts. The mixed-methods design is appropriate, and the theoretical framing is sophisticated. However, several significant weaknesses must be addressed before the paper is suitable for peer review.

**Strengths:**
- Novel application of epistemic injustice theory to platform epistemology
- Interesting methodological innovation (multi-model LLM coding)
- Timely empirical contribution during active conflicts
- Strong theoretical integration

**Critical Weaknesses:**
- Inadequate inter-rater reliability reporting
- Causal overclaims from correlational data
- Missing baseline/comparison conditions
- Undertheorized alternative explanations
- Incomplete operationalization of key constructs

---

## Major Issues

### 1. RELIABILITY CRISIS: Inter-Model Agreement Not Reported

**Problem:** The paper claims to use multi-model coding for reliability but **never reports kappa statistics** in the findings section. The abstract mentions κ assessment, but Table 5.2.1 shows raw counts without agreement metrics.

**Evidence from text:**
> "We assessed inter-model agreement using Cohen's kappa (κ) for each construct."

But findings only report:
> "| Construct | Claude | GLM | Kimi | Consensus Cases |"

**What's missing:**
- Pairwise κ for each construct (Claude-GLM, Claude-Kimi, GLM-Kimi)
- Fleiss' κ for 3-rater agreement
- Confidence intervals
- Interpretation of κ levels (Landis & Koch benchmarks)

**From agreement_results.json we know κ was LOW:**
- testimonial_injustice: κ = 0.09 (Claude-Kimi)
- hermeneutical_injustice: κ = 0.18
- epistemic_dispossession: κ = -0.14 (NEGATIVE!)
- source_hierarchy: κ = 0.47 (only acceptable one)

**Impact:** Low κ undermines the entire CDA component. The paper cannot claim valid coding with κ < 0.40.

**Required action:** 
- Report ALL κ values transparently
- Acknowledge low agreement as limitation
- Discuss what low κ means for construct validity
- Consider reporting only high-agreement constructs in main findings

---

### 2. CAUSAL OVERCLAIMS: "Pure Reverters" ≠ Epistemic Injustice

**Problem:** The paper repeatedly implies that being a "pure reverter" constitutes epistemic injustice or that the revert network structure *causes* epistemic harm. But this conflates structural position with normative judgment.

**Problematic claims:**
> "A minority of editors (41-43%) control content through reverting, while the majority (57-58%) have their contributions removed without recourse."

> "These editors occupy structurally protected positions... that insulate them from the same mechanisms they use to control others' contributions."

**Alternative explanations NOT considered:**
1. **Quality control:** Pure reverters may be removing vandalism, spam, or policy violations—legitimate editorial work
2. **Experience gradient:** Experienced editors *should* revert more because they know policies better
3. **Self-selection:** "Pure reverted" editors may be newcomers who leave after first conflict, not victims of systematic exclusion
4. **Edit type differences:** Reverters may patrol for BLP violations; reverted may be adding unsourced claims

**Required action:**
- Add "Alternative Explanations" section
- Analyze WHAT content was reverted (vandalism? policy violation? substantive dispute?)
- Control for editor experience, edit type, article protection level
- Soften causal language: "correlates with" not "creates conditions for"

---

### 3. MISSING BASELINE: What Would Non-Injustice Look Like?

**Problem:** The paper has no comparison condition. We don't know if 41% "pure reverters" is:
- Higher than non-conflict Wikipedia articles
- Higher than other contentious topics (climate, vaccines)
- Different from what random chance would predict

**Without baseline:**
- 41% pure reverters might be *normal* Wikipedia dynamics
- Similar patterns might exist in uncontroversial articles
- The "elite" framing assumes this is exceptional without evidence

**Required action:**
- Add comparison corpus (non-conflict articles of similar size/activity)
- Calculate expected role distribution under null model
- Statistical test: Is observed distribution significantly different from baseline?

---

### 4. CONSTRUCT VALIDITY: "Epistemic Injustice" vs. "Editorial Conflict"

**Problem:** The paper struggles to distinguish epistemic injustice (wrongful exclusion based on identity) from ordinary editorial conflict (disagreement about content).

**Example of slippage:**
> "Naming Dispute (gaza_059): "'Terror' should be 'Horror'—that's the classical Arabic translation."

This is coded as hermeneutical injustice, but it's actually a legitimate editorial dispute about translation accuracy. No one is being excluded because of *who they are*—they're debating *what the correct translation is*.

**Fricker's original definition requires IDENTITY-BASED prejudice:**
> "a wrong done to someone specifically in their capacity as a knower" (Fricker 2007, p. 1)

But many coded cases are:
- Policy disputes (WP:RS is applied equally to all)
- Translation debates (factual, not identity-based)
- Source challenges (based on source methodology, not editor identity)

**Required action:**
- Tighten construct definitions to require identity-based exclusion
- Re-code cases using stricter criteria
- Distinguish "editorial disagreement" from "epistemic injustice"
- Add clear decision rules for borderline cases

---

### 5. SAMPLING BIAS: High-Conflict Selection Inflates Findings

**Problem:** The paper explicitly samples for conflict:
> "High-conflict threads (most reverts), Policy disputes, Naming battles, Source debates"

This guarantees finding conflict-related phenomena. It's like sampling emergency rooms to study injury prevalence—you'll find injuries, but can't generalize to the population.

**Impact:**
- Cannot claim "Wikipedia talk pages exhibit epistemic injustice" when you sampled injustice-likely contexts
- Prevalence estimates are meaningless (13/276 naming disputes in a naming-dispute sample?)
- No denominator for "how common is EI in Wikipedia?"

**Required action:**
- Acknowledge sampling strategy in limitations
- Add random sample of talk page excerpts for comparison
- Report findings as "in high-conflict contexts" not "in Wikipedia"
- Remove prevalence claims or add appropriate caveats

---

### 6. TEMPORAL MISMATCH: Iran (72h) vs. Gaza (2+ years)

**Problem:** The two clusters have vastly different temporal coverage:
- Iran: 72 hours (Feb 27-Mar 5, 2026)
- Gaza: 2+ years (Oct 2023-Mar 2026)

This makes comparison problematic:
- Iran shows *initial* editing dynamics
- Gaza shows *mature* conflict dynamics
- "Structural isomorphism" may reflect measurement artifacts, not real similarity

**Required action:**
- Standardize temporal windows (e.g., first week of each conflict)
- Or acknowledge temporal incomparability
- Analyze Gaza's first 72 hours separately for fair comparison

---

### 7. LLM METHOD: Insufficient Validation

**Problem:** The multi-model coding protocol is novel but undervalidated:
- No human gold standard to assess model accuracy
- No prompt sensitivity analysis
- "Epistemic diversity" claim is speculative (are Chinese models really "differently biased"?)
- Disagreement framed as "feature" but could be "noise"

**Problematic framing:**
> "These divergences are not errors but features—they reflect different cultural interpretive frameworks."

This is unfalsifiable. Any disagreement becomes "diversity"; no disagreement can be "error."

**Required action:**
- Create human-coded gold standard (50+ cases)
- Calculate model accuracy against gold standard
- Test prompt variations
- Provide evidence that model divergence reflects cultural difference, not random error

---

### 8. MISSING VOICES: No Wikipedia Editor Perspectives

**Problem:** The paper analyzes Wikipedia editors as objects of study but doesn't include their perspectives. This is ironic given the topic (epistemic injustice = excluding knowers).

**What's missing:**
- Editor interviews or surveys
- Insider accounts of revert dynamics
- Wikipedia community's own understanding of these patterns
- Response from named editors (ethical concern: are they aware they're being studied?)

**Required action:**
- Add qualitative component with editor interviews
- Or acknowledge as limitation and future direction
- Consider ethics of naming specific editors without consent

---

### 9. NORMATIVE OVERREACH: Policy Implications Unwarranted

**Problem:** The conclusion makes policy recommendations without sufficient evidence:
> "Alternative mechanisms—such as expert verification or tiered protection that allows reading but not editing—might balance quality control with epistemic inclusion."

But the paper hasn't shown:
- That EC protection *causes* epistemic injustice (vs. correlates)
- That "epistemic inclusion" would improve article quality
- That proposed alternatives would work better
- Any consideration of tradeoffs (more inclusion = more vandalism?)

**Required action:**
- Remove or heavily caveat policy recommendations
- Frame as "questions for future research" not "implications"
- Acknowledge that Wikipedia's current policies exist for reasons

---

### 10. LITERATURE GAPS

**Missing engagement with:**
- Wikipedia-specific research on edit wars (Yasseri et al., 2012; Borra et al., 2015)
- Content analysis methodology literature (Krippendorff's reliability standards)
- Platform governance scholarship (Gillespie, 2018; Caplan & boyd, 2018)
- Middle East studies / area expertise on the conflicts studied
- Computational propaganda / information operations literature

**Required action:**
- Expand literature review
- Engage with Wikipedia studies canon
- Situate LLM coding in content analysis methodology debates

---

## Minor Issues

### 11. Writing/Presentation
- Abstract is too long (250 words; should be ~150)
- "Pure reverter" terminology is jargon—define earlier
- Theoretical model diagram is ASCII art—needs proper figure
- Reference list is incomplete (missing full citations)

### 12. Data Reporting
- No standard errors or confidence intervals
- Network visualizations promised but not shown
- Article list not provided (even as appendix placeholder)

### 13. Reproducibility
- No code availability statement
- Prompts mentioned but not provided
- Sampling procedure not fully replicable

---

## Recommendations for Revision

### Priority 1 (Must fix before submission):
1. Report inter-model κ transparently; acknowledge low reliability
2. Add alternative explanations section
3. Tighten construct definitions (EI vs. editorial conflict)
4. Soften causal claims

### Priority 2 (Should fix):
5. Add baseline comparison corpus
6. Address temporal mismatch
7. Validate LLM coding against human gold standard
8. Expand literature review

### Priority 3 (Ideal but optional):
9. Add editor interviews
10. Improve visualizations
11. Provide full reproducibility materials

---

## Summary

This paper has a strong conceptual foundation and addresses an important topic. However, the current version has significant methodological weaknesses—particularly around reliability, construct validity, and causal inference—that undermine its empirical claims. The authors should:

1. Be more honest about what the data can and cannot show
2. Tighten the link between theory (epistemic injustice) and evidence (editing patterns)
3. Consider alternative explanations systematically
4. Report reliability metrics transparently

With major revisions addressing these issues, this could be a valuable contribution to platform epistemology scholarship.

---

*Review completed: March 6, 2026*
