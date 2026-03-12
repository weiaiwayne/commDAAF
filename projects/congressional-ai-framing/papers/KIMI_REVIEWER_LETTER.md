**PEER REVIEW LETTER**

**Manuscript:** "The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis"

**Reviewer:** #2 (Kimi K2.5)

---

**Summary**

This manuscript examines the framing of artificial intelligence in U.S. congressional hearings from 2007-2026, employing a novel multi-LLM coding approach with Kimi K2.5 and Claude Opus 4.5. The study identifies SOVEREIGNTY (22%) and INNOVATION (21%) as dominant frames, with notable temporal shifts post-ChatGPT and chamber differences (Senate 28% vs. House 18% sovereignty framing). While the multi-model methodology is innovative and the dataset substantial, significant theoretical, methodological, and interpretive concerns limit the contribution. The manuscript requires major revision to address issues with theoretical fit, coding transparency, and generalizability before it can make a meaningful contribution to political communication and science and technology studies.

---

**MAJOR CONCERNS**

**1. Theoretical Framework Mismatch and Missing Literature**

The manuscript's theoretical grounding raises substantial concerns. While Entman (1993) and Nisbet (2009) provide appropriate framing foundations, the application of securitization theory (Buzan, Wæver & de Wilde, 1998) to domestic congressional discourse is theoretically incongruous. Securitization theory was developed to analyze existential threats in international security contexts requiring emergency measures outside normal political procedures. Domestic technology policy hearings—regardless of sovereignty rhetoric—do not constitute securitization moves in the Copenhagen School sense. The authors risk theoretical overreach or, worse, conceptual stretching.

**Recommendation:** Either properly theorize how congressional technology discourse constitutes securitization (engaging with Balzacq, 2011; Floyd, 2010; and recent critical security studies) OR abandon securitization for more appropriate theoretical frameworks. I strongly suggest engaging with agenda-setting theory (Kingdon, 1995; Baumgartner & Jones, 1993), policy framing in legislative contexts (Schön & Rein, 1994), or issue ownership literature (Petrocik, 1996). The absence of any citation to foundational congressional studies or policy process scholarship is a significant gap.

**2. Suspicious Reliability Trajectory and Insufficient Coding Transparency**

The reported jump from κ=0.206 (Slight agreement) to κ=0.656 (Substantial agreement) between prompt versions demands extraordinary transparency that the manuscript currently lacks. A 0.45 improvement in Cohen's kappa through "document-type bias correction" suggests either: (a) a fundamental flaw in the initial coding scheme now patched, (b) overfitting the prompt to achieve agreement, or (c) cherry-picked examples. Without access to the full prompts, error analysis, and qualitative examples of disagreements, readers cannot assess validity.

**Critical questions unanswered:**
- What specific document-type biases were identified?
- How many iterations occurred between v1.0 and v1.1?
- Were disagreements randomly distributed or systematic by frame type?
- What is the per-frame kappa? (Aggregate masks problematic categories)

**Recommendation:** Provide full prompt appendices, detailed error analysis with exemplar disagreements, and per-frame reliability statistics. Consider calculating Krippendorff's alpha for multiple coders and reporting Fleiss' kappa if expanding to three models.

**3. Temporal Data Imbalance and Questionable Generalizability**

The 90%/10% split (post/pre-ChatGPT) creates a severe temporal bias that the manuscript inadequately addresses. With only ~19 hearings from 2007-2022 spanning 15 years versus 173 from 2022-2026, any claims about temporal trends—including the reported emergence of RIGHTS framing post-2022—are statistically fragile and potentially artifacts of data sparsity.

**Recommendation:** Either: (a) restrict claims to the post-2022 period with appropriate caveats, or (b) supplement with additional pre-2022 data sources (e.g., committee reports, floor statements, C-SPAN transcripts not in GovInfo). The RIGHTS frame finding is particularly suspect—absence of detection in pre-2022 hearings may reflect coding scheme insensitivity rather than genuine discursive absence.

**4. Search Strategy Limitations and Missing Discourse**

The GovInfo API search for "artificial intelligence" exclusively captures hearings explicitly mentioning the term, missing substantial AI policy discourse conducted through related terminology ("machine learning," "automated decision systems," "algorithmic bias," "predictive analytics"). This is particularly problematic for the pre-2022 period when AI was frequently discussed through application-specific frames (facial recognition, predictive policing, credit scoring) rather than as "AI" per se.

**Recommendation:** Acknowledge this limitation explicitly and consider supplementary searches or discuss how this constraint shapes the representativeness of findings. The "AI density threshold" (≥5 or 20+ terms) also requires justification—why OR rather than AND? What validation supports these cutoffs?

**5. Inadequate Engagement with Comparative and Critical Literature**

The manuscript insufficiently contextualizes its findings within:
- **Comparative AI policy discourse:** How do U.S. congressional frames compare to EU parliamentary discourse (Bradford, 2020; Ebers et al., 2021) or Chinese policy documents?
- **Critical algorithm studies:** Missing engagement with Metcalf, Moss & boyd (2016) on algorithmic framing, Katzenbach (2023) on AI policy narratives, or recent work on AI hype cycles (Cave & Dihal, 2019).
- **Congressional communication scholarship:** No engagement with Fenno (1978) on committee behavior, Hall (1996) on policy change, or recent work on tech lobbying in Congress (Powell, 2021).

---

**MINOR CONCERNS**

**6. Sample Size Justification for Chamber Comparisons**

The manuscript reports Senate-House differences (28% vs. 18% sovereignty framing) without establishing whether this difference is statistically significant or whether sample sizes support such comparisons. With 90% of data post-2022 and potential committee selection effects, N sizes may be inadequate for chamber-level inference.

**7. Missing Frame Definitions and Operationalization**

The eight-frame scheme (SOVEREIGNTY, INNOVATION, GOVERNANCE, RISK_HARM, RISK_SAFETY, RIGHTS, RISK_ECONOMIC, TECHNICAL) is presented without detailed operationalization. How were these frames inductively derived versus theoretically specified? What distinguishes RISK_HARM from RISK_SAFETY? What coding rules resolved edge cases?

**8. GLM-4.7 Failure as Methodological Limitation**

The planned third coder "produced 0 output (rate limits)" should be framed as a methodological limitation rather than a passing note. With only two coders and no human validation, the reliability claim rests on thin ground. Rate limit failures suggest inadequate pilot testing.

**9. Data Coverage Through 2026**

Including data through 2026 when the manuscript appears to be written in 2025-2026 raises questions about data completeness. Are projected hearings included? Is the dataset closed? This needs explicit clarification.

**10. Absence of Qualitative Exemplars**

A content analysis of congressional discourse without exemplary quotations misses an opportunity to illustrate frame manifestations and validate that LLM coding captures meaningful thematic content rather than surface keywords.

---

**STRENGTHS**

1. **Methodological Innovation:** The multi-LLM validation approach represents a genuine methodological contribution to computational communication research. If properly documented, this could serve as a model for large-scale automated content analysis.

2. **Dataset Significance:** 192 congressional hearings represents a substantial corpus for AI policy discourse analysis, particularly for the post-2022 period which will be of considerable interest to scholars.

3. **Timely Contribution:** The finding of sovereignty framing dominance speaks directly to current debates about AI nationalism, techno-sovereignty, and the geopoliticization of AI governance.

4. **Transparency on Iterative Development:** Acknowledging the prompt development process (v1.0 to v1.1), while requiring more detail, demonstrates methodological reflexivity that strengthens credibility.

---

**RECOMMENDATION: MAJOR REVISION**

This manuscript addresses an important and timely topic with an innovative methodological approach. However, significant theoretical, methodological, and interpretive issues require substantial revision before publication.

**Essential revisions for resubmission:**
1. Resolve theoretical framework mismatch (securitization vs. alternative approaches)
2. Provide complete coding documentation with per-frame reliability and error analysis
3. Address temporal bias through either additional pre-2022 data or restricted claims
4. Acknowledge search strategy limitations and missing discourse types
5. Engage substantively with comparative AI policy and congressional studies literature

I look forward to reviewing a revised version that addresses these concerns.

**Reviewer #2**
