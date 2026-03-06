# Peer Review: Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts

**Reviewer:** [Anonymous]
**Date:** March 6, 2026
**Recommendation:** Major Revisions

---

## Overview

This manuscript presents an exploratory mixed-methods study examining editorial conflict patterns in Wikipedia articles covering two Middle East conflicts (Iran war 2026 and Israel-Hamas war 2023-present). The authors combine revert network analysis with LLM-assisted discourse analysis of talk pages, using Fricker's (2007) epistemic injustice framework as a theoretical lens.

The study makes an interesting contribution to platform studies and Wikipedia research, but significant methodological and theoretical concerns must be addressed before publication.

---

## Main Strengths

### 1. Methodological Transparency and Intellectual Honesty

The authors deserve commendation for their exceptional transparency about limitations. Throughout the manuscript, they acknowledge alternative explanations (e.g., legitimate quality control vs. epistemic injustice), report low inter-rater reliability openly, and clearly state the exploratory nature of their study. This intellectual honesty is refreshing and exemplifies best practices for preliminary research.

The discussion of low κ values (0.09-0.18 for most constructs) as potentially substantive findings—revealing cultural contestation around epistemic injustice concepts rather than methodological failure—is a sophisticated and valuable methodological contribution.

### 2. Innovative Multi-Model LLM Coding Approach

The use of three culturally diverse LLMs (Claude, GLM-4.7, Kimi K2.5) and interpreting inter-model agreement as a form of construct validation is genuinely innovative. The finding that "Source Hierarchy" achieves moderate reliability (κ = 0.47) while constructs like "Hermeneutical Injustice" show systematic disagreement suggests this approach can distinguish between culturally robust and culturally contested constructs. This methodological advance merits development.

### 3. Clear Theoretical Grounding with Appropriate Caveats

The manuscript provides a solid grounding in Fricker's epistemic injustice framework and recent extensions to digital platforms. Importantly, the authors carefully note that these concepts were developed for face-to-face interaction and may require substantial modification for pseudonymous platform contexts. They acknowledge identity cues are attenuated online, which complicates direct application of Fricker's identity-prejudice focus.

---

## Main Weaknesses

### 1. Insufficient Theoretical Advancement

While the manuscript applies epistemic injustice theory competently to Wikipedia, it does not substantially advance the theory beyond what others (Ajmani et al., 2024; Kwok, 2025) have already proposed. The conclusion that these patterns "may" relate to epistemic injustice is hedged to the point of being non-committal.

The authors identify that Wikipedia's environment differs fundamentally from Fricker's face-to-face contexts (pseudonymity attenuating identity cues, platform-based authority systems replacing social identity cues), but do not develop theoretical tools for analyzing these differences. The manuscript needs to move beyond applying existing frameworks to contributing new theoretical insights.

Specifically, the manuscript would benefit from:
- Developing platform-specific conceptualizations of epistemic authority that account for Wikipedia's unique governance structures (EC protection, administrator status, edit count hierarchies)
- Theorizing how "experience-based expertise" differs from "identity-based prejudice" in ways that matter for justice claims
- Articulating conditions under which platform governance transitions from legitimate quality control to epistemic injustice

### 2. Limited Methodological Rigor in Several Key Areas

**a. No Baseline Comparison**

The most significant limitation is the absence of a comparison sample. The authors explicitly acknowledge this limitation (p. 341), but it severely constrains interpretive power. Without analyzing non-conflict articles or low-conflict Wikipedia pages, we cannot determine whether:
- The 41-43% "reverter" role distribution reflects Wikipedia's general editorial structure
- The observed contestation is specific to geopolitical conflicts or typical of all contentious topics
- The patterns are exceptional or mundane

This limitation should be addressed, even if it requires narrowing scope to one conflict cluster to enable comparison analysis.

**b. Insufficient Sample Sizes for Discourse Analysis**

The coding results (Table 2) reveal extremely small counts for most constructs:
- Testimonial Injustice: Claude=3, GLM=0, Kimi=1
- Policy Weaponization: Claude=1, GLM=3, Kimi=0
- Epistemic Dispossession: 2 across all models

With only 276 excerpts total, many constructs appear fewer than 5 times across all three models. These small N values severely limit the reliability of any conclusions, regardless of inter-rater agreement. The authors should either:
- Expand the sample size substantially for low-frequency constructs
- Drop underpowered constructs and focus analysis on those with sufficient data
- Transparently acknowledge that findings are descriptive rather than inferential for rare constructs

**c. No Human Validation of LLM Coding**

While the multi-model approach is innovative, without any human coder validation or reliability assessment, we cannot determine whether the models are converging on correct interpretations or systematically missing evidence. The absence of even a small human-validated subsample (e.g., 20-30 excerpts coded by humans) makes it impossible to assess construct validity beyond model agreement.

**d. No Content Analysis of Reverted Material**

The authors analyze revert patterns but never examine *what* was reverted. As they acknowledge (p. 127), revert patterns alone cannot distinguish legitimate quality control (removing vandalism, policy violations) from unjust gatekeeping. This omission is particularly significant given the centrality of "epistemic injustice" claims—if the reverted content was primarily policy-violating, the injustice interpretation weakens considerably.

### 3. Inadequate Integration of Methods

The two methodological components (revert networks and discourse analysis) remain largely disconnected. Section 3.5 states the authors "examined whether editors identified in talk page cases could be located in the revert network," but the findings section (4.2.3) presents only illustrative quotes without connecting them to network position or editor roles.

A more integrated analysis would:
- Map talk page participants to their network positions (reverter/reverted/bidirectional)
- Examine whether editors in different network roles engage in different discursive practices
- Analyze whether specific revert episodes correspond to talk page contestation about those reversions
- Investigate whether high-status editors (never reverted) use particular discursive strategies

Without this integration, the study presents parallel analyses rather than a cohesive mixed-methods investigation.

---

## Specific Suggestions for Improvement

### Theoretical Development

1. **Develop Platform-Specific Theory:** Move beyond applying Fricker to theorizing how Wikipedia's structures create distinctive forms of epistemic inclusion/exclusion. Consider developing concepts like "credential-based epistemic authority" (account age, edit count, EC status) as distinct from identity-based prejudice.

2. **Clarify the Justice Claims:** Explicitly articulate conditions under which Wikipedia governance transitions from legitimate to unjust. When is EC protection appropriate vs. exclusionary? When does experience-based authority become gatekeeping? The manuscript offers a framework but doesn't advance beyond asking these questions.

3. **Connect to Existing Platform Studies:** The literature review cites important work but could better integrate findings from existing Wikipedia power structure research (e.g., geographic biases, gender gaps, edit war patterns). How do your findings extend or complicate this prior work?

### Methodological Improvements

4. **Add a Comparison Sample:** Select 25-50 non-conflict or low-conflict Wikipedia articles (ideally on similar topics without active conflict) and conduct the same revert network analysis. This would establish whether observed patterns are conflict-specific or reflective of Wikipedia's general editorial structure.

5. **Expand Sample Size for Discourse Analysis:** Increase the excerpt sample to at least 500-600 total to ensure adequate power for rare constructs. If resource constraints prevent this, focus analysis exclusively on "Source Hierarchy" and "Naming Dispute" (the constructs with higher frequency and reliability), dropping underpowered constructs.

6. **Add Human Coding Validation:** Have at least one human coder (ideally two, for reliability assessment) code a random subsample of 30-50 excerpts using the same codebook. Compare human-LLM agreement to assess whether models converge on accurate interpretations.

7. **Code Revert Content:** Randomly sample 100-200 revert events and code whether the reverted content was:
   - Vandalism/obvious disruption
   - Policy-violating but good-faith (e.g., unsourced claims)
   - Good-faith, policy-compliant edits removed for other reasons

This would enable assessment of whether reversions reflect quality control or something more problematic.

8. **Integrate Methods More Thoroughly:** Create a systematic mapping between discourse participants and network positions. Analyze whether editors in different roles (reverter vs. reverted) use different discursive strategies or invoke different authority claims in talk pages.

### Analytical and Reporting Issues

9. **Strengthen Cross-Cluster Comparison Analysis:** Given the temporal asymmetry (Iran: 1 week, Gaza: 2.5 years), the cross-cluster comparison (RQ3) is limited. Either:
   - Narrow analysis to a comparable time window in the Gaza cluster, or
   - Explicitly analyze temporal evolution in the Gaza data and use this to theorize about conflict lifecycle patterns

10. **Report Confidence Intervals:** For proportion estimates (e.g., 41.4% reverters), report 95% confidence intervals to communicate sampling uncertainty.

11. **Quantify "Top Reverter" Concentration:** The finding that "Top 5 reverters account for 18-20% of all reverts" (p. 208) lacks context. Compare this to expected concentration under various distributions (e.g., power law, Poisson) to determine whether this represents extreme concentration or moderate inequality.

### Structural and Presentation Issues

12. **Restructure the Discussion:** The discussion alternates between epistemic injustice interpretation and alternative explanations in a way that is somewhat confusing. Consider:
   - First, present findings neutrally without interpretation
   - Then, systematically present multiple interpretive frameworks (epistemic injustice, quality control, learning curve, self-selection)
   - Finally, articulate what evidence would be needed to adjudicate between interpretations

13. **Add Visualizations:** The revert network findings would benefit from network diagrams showing role distributions, concentration patterns, and cross-cluster overlap. Visual representation would make structural patterns more accessible.

14. **Clarify Construct Definitions:** The operational definitions (Table 1) are ambitious but some concepts like "Hermeneutical Injustice" remain ambiguous when applied to Wikipedia discourse. Consider adding more detailed examples and counter-examples, or acknowledging that some constructs require further refinement before reliable coding is possible.

---

## Ethical Considerations

The manuscript does not explicitly address ethics approval. Given that Wikipedia editors are research participants whose public contributions are being analyzed, the authors should clarify whether:
- Institutional Review Board approval was obtained or deemed unnecessary (with justification)
- Any measures were taken to protect editor privacy (beyond pseudonymity)
- Editors have been informed of the research or could opt out

---

## Minor Editorial Issues

- p. 13: "LLM-assisted" appears twice in the keywords; consider redundancy
- p. 341: "Three-model ensemble" listed as limitation but never clearly explained why three is insufficient—expand or reframe
- Several typos and minor formatting issues throughout (proofreading recommended)
- Appendices referenced but not included—these should be included or clearly indicated as supplementary materials

---

## Conclusion

This manuscript addresses an important and timely topic—how digital platforms mediate knowledge production during geopolitical conflicts. The authors demonstrate methodological creativity and commendable intellectual honesty about limitations. However, the study's theoretical contribution is limited, and several methodological weaknesses (no baseline comparison, small discourse sample sizes, no human validation, lack of methodological integration) constrain the interpretive power of findings.

With major revisions addressing the key concerns above, this manuscript could make a valuable contribution to platform studies and Wikipedia research. The innovative multi-model LLM coding approach, in particular, merits further development and could become an important methodological contribution to computational communication research.

---

## Decision: Major Revisions

The manuscript requires substantial revisions in theoretical development and methodological rigor before reconsideration for publication. The specific recommendations above provide a roadmap for addressing these concerns.

---

*This review was conducted as a simulated peer review for educational purposes. Any resemblance to actual peer reviews is coincidental.*
