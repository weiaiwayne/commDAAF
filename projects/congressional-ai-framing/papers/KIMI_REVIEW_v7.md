# Peer Review: Governance or Competition? Divergent Frames in AI Policy Discourse Across the US and Global South

**Reviewer Letter for Communication Journal Submission**

---

## 1. Overall Assessment: **MAJOR REVISION REQUIRED**

This manuscript presents an ambitious comparative framing analysis of AI policy discourse across the US and three Global South nations. The study addresses a timely and important question about how AI governance is constructed differently across geopolitical contexts. However, significant theoretical, methodological, and empirical weaknesses prevent me from recommending acceptance at this time. The manuscript would benefit substantially from major revision to address concerns about conceptual coherence, methodological rigor, generalizability, and analytical depth.

---

## 2. Major Concerns

### 2.1 Theoretical and Conceptual Issues

**Weak Conceptualization of "Framing"**

The manuscript relies on Entman (1993) and Gamson & Modigliani (1989) but inadequately engages with more recent developments in framing theory. Notably absent:

- **Van Gorp (2007, 2010)** on the difference between "issue-specific" and "generic" frames, which would help clarify whether the frames identified are intrinsic to AI discourse or transferable across policy domains
- **Chong & Druckman (2007)** on framing effects and equivalence, which raises questions about whether the identified frames are truly competing constructions or simply emphasizing different aspects of a complex issue
- **Borah (2011)** on integrative framing analysis, which could help bridge the gap between the individual-level cognitive effects assumed by framing theory and the aggregate discourse patterns analyzed here

More critically, the manuscript does not adequately distinguish between **policy frames** (problem definitions), **news frames** (media narratives), and **individual-level framing effects** (how audiences process information). The authors shift between these levels without acknowledging the theoretical stakes of these distinctions.

**Problematic "Global South" Category**

The manuscript treats "Global South" as a coherent analytical category, but this masks substantial heterogeneity. The three cases selected—South Africa, Brazil, and India—vary along multiple dimensions that may confound the purported "Global South" framing pattern:

- **India is a major AI developer**, with significant indigenous AI industry (Infosys, TCS, numerous startups) and substantial research output. Treating India as simply an "AI adopter" is empirically problematic.
- **Brazil and South Africa** have very different colonial legacies, institutional capacities, and relationships to the US and China that may shape AI framing independently of "Global South" positioning.
- **Language and discourse traditions differ**: Portuguese and English parliamentary traditions differ substantially; comparing Brazilian legislative documents with US congressional hearings without addressing these genre differences is analytically suspect.

The manuscript needs to engage with **Comaroff & Comaroff (2012)** on "Theory from the South" and **Mehta (2011)** on postcolonial approaches to international relations to justify or problematize its category construction. Absent such engagement, the Global South framing appears more as a convenient aggregation than a theoretically grounded category.

**Missing Alternative Explanations**

The manuscript advances a competition-versus-governance explanation for framing divergence without adequately considering alternative explanations:

1. **Party politics and ideological differences**: The US data spans 2021-2026, a period of intense partisan polarization. Are sovereignty frames concentrated among Republicans while Democrats emphasize governance? The manuscript acknowledges temporal concentration (90% post-ChatGPT) but not partisan distribution.
2. **Institutional venue effects**: Congressional hearings versus committee reports and policy submissions are different genres with different rhetorical conventions. The manuscript acknowledges this limitation but does not adequately address whether observed differences reflect genre rather than national context.
3. **Issue salience effects**: AI may simply be lower-salience in Global South contexts, producing more technical/technocratic governance framing rather than mobilizing competition rhetoric.

### 2.2 Methodological Weaknesses

**Severe Sample Imbalance and Representativeness Concerns**

The US sample (192 documents) is nearly double the Global South sample (102), with India contributing only 7 documents. This imbalance creates several problems:

- **Statistical power**: Chi-square tests with highly unequal sample sizes and expected cell counts below 5 in multiple cells (e.g., "Safety" in Global South = 0) violate standard assumptions for chi-square testing.
- **India's near-exclusion**: With only 7 documents, claims about "Global South" patterns effectively rest on South Africa (41) and Brazil (54). The manuscript acknowledges this but continues to make aggregate "Global South" claims throughout.
- **Document type heterogeneity**: US congressional hearings follow predictable formats with structured testimony, Q&A, and partisan positioning. Brazilian "legislative documents" include committee reports, expert testimony, and "legislative analyses"—genres with different purposes and conventions. This is an apples-to-oranges comparison that undermines causal inference about "national framing."

**Unreliable Reliability Statistics**

The inter-coder reliability statistics are concerning:

- **US data**: Initial κ = .21 ("poor"), improved to κ = .66 ("substantial") only after targeted prompt revision. The admission that models were coding "document type" rather than "substantive framing" is troubling—it suggests the frames are not reliably distinguishable in the data.
- **Rights frame**: κ = .52 falls below the acceptable .60 threshold, yet the manuscript treats the 9% vs. 18% US/Global South difference as meaningful. This is methodologically unsound.
- **South Africa**: Initial κ = .45, improved to κ = 1.0 only after adjudication. The adjudication process resolved only 15 disagreements—was this a complete re-coding or selective resolution?

The manuscript notes that "findings for rights framing should be interpreted cautiously" but continues to interpret them throughout the Findings and Discussion sections without appropriate caveats.

**The "Adjudication" Problem**

Post-hoc adjudication by "two of the authors" raises serious questions about researcher degrees of freedom. The criteria provided (Annual Reports → Governance; 4IR opportunity → Innovation; copyright → Rights) appear arbitrary and raise concerns about confirmation bias. The jump from κ = .45 to κ = 1.0 after adjudication suggests the adjudicators may have simply imposed their theoretical expectations on ambiguous data.

**LLM-as-Coder Limitations**

While the manuscript acknowledges using LLMs for coding, it does not adequately address known limitations:

- **Training data contamination**: Kimi K2.5 (Chinese) and Claude Opus 4.5 (US) may have differential exposure to US vs. Global South AI discourse in their training data, potentially biasing frame recognition.
- **Prompt sensitivity**: The fact that a single prompt revision improved κ from .21 to .66 suggests frame coding is highly sensitive to prompting—a form of researcher influence that undermines claims of systematic, replicable analysis.
- **No human validation**: The manuscript reports no human-coded subset for validation, a standard practice in computational text analysis.

### 2.3 Empirical and Analytical Weaknesses

**Cherry-Picked Quotations**

The exemplary quotations in the Findings section are suspiciously perfect for the authors' argument. The manuscript does not report:
- How many documents were reviewed to select these quotations
- Whether quotations represent typical or extreme expressions
- Any contradictory quotations that might complicate the framing narrative

For example, the US sovereignty quotations are attributed to Armed Services and Intelligence committees—venues with explicit national security mandates. Were comparable security-focused frames absent in Global South military/defense contexts? The manuscript does not say.

**Circular Reasoning on "Adopter vs. Developer"**

The Discussion section explains the divergence through "adopter versus developer positioning," but this explanation is circular:
- The US is identified as a "developer" because it has major AI companies
- The US frames AI as competition (presumably because it's a developer)
- Global South nations are identified as "adopters" 
- They frame AI as governance (presumably because they're adopters)

This is post-hoc reasoning that doesn't explain why India—with substantial AI industry—is grouped with "adopters" rather than "developers," or why Europe (also a "developer" region via companies like Mistral, Aleph Alpha, and DeepMind) frames AI through "trustworthy AI" governance rather than competition.

**Missing Comparison Cases**

The manuscript excludes China for reasonable data-access reasons, but this creates a significant gap. If the competition frame reflects "developer" positioning, we would expect China—undeniably a developer—to show strong sovereignty/competition framing. Without this comparison, the developer/adopter hypothesis remains untested.

Similarly, **Europe** is discussed in passing but not empirically analyzed. The EU's "trustworthy AI" framing would provide an important test case: European AI developers exist, yet framing emphasizes governance. This case directly contradicts the developer→competition framing hypothesis advanced in the Discussion.

**Overstated Claims of "Disciplinary Power"**

The Discussion section claims competition framing has "disciplinary power" that subordinates rights concerns in US discourse. The evidence for this is a single quotation where a legislator acknowledges privacy concerns but prioritizes competition. This is thin evidence for a strong claim about discursive discipline. No systematic analysis of how rights frames are positioned relative to competition frames is provided.

### 2.4 Statistical Issues

**Multiple Comparisons Problem**

Table 1 reports chi-square tests for 8 frame categories without adjustment for multiple comparisons. At α = .05, with 8 tests, we expect 0.4 false positives by chance alone. The two "significant" findings marked with ** (p < .01) survive Bonferroni correction, but the single * (p < .05) finding (Rights: +8.7%) does not.

**Zero-Cell Problem**

The Global South sample shows 0% for "Safety" and "Technical" frames. Chi-square tests with zero expected frequencies are problematic and may inflate Type I error rates. The manuscript does not address this issue.

**Effect Sizes Not Reported**

For significant chi-square tests, the manuscript does not report Cramér's V or other effect size measures. Are the observed differences substantively meaningful or merely statistically significant due to large N?

---

## 3. Minor Concerns

### 3.1 Literature Gaps

Several relevant literatures receive inadequate attention:

- **International Relations theory**: Constructivist approaches (Wendt, 1999; Finnemore & Sikkink, 1998) on how norms diffuse and vary across contexts would strengthen the theoretical framing.
- **Postcolonial technology studies**: Could engage with **Philip et al. (2012)** on postcolonial computing and **Dourish & Mainwaring (2012)** on transnational technology cultures.
- **Science and Technology Studies (STS)**: The framing analysis would benefit from engagement with **Jasanoff (2005)** on "sociotechnical imaginaries"—nationally-specific visions of technology-society relationships that closely parallel the "framing" concept used here.
- **Comparative policy analysis**: **Howlett (2019)** on policy tools and instruments could help operationalize the claim that frames "shape which solutions appear viable."
- **Digital sovereignty literature**: Recent work by **Couture & Toupin (2019)** and **Milan & Treré (2020)** on data and digital sovereignty from Global South perspectives is directly relevant but absent.

### 3.2 Writing and Presentation Issues

**Duplicated "Limitations" Section**

The manuscript contains two nearly identical "Limitations" subsections—one in the Discussion (page 19) and one immediately following it (page 20). This appears to be an editing error.

**Inconsistent Referencing**

- The AI Now Institute (2025) is cited for South Africa's National AI Policy Framework, but this source appears to be a forward-dated citation (current year is presumably 2024 or earlier given data collection through 2025).
- "AgentAcademy Research Team" is listed as the author but the manuscript is clearly written by researchers with affiliations and institutional backing. Anonymization for review is standard, but the byline should indicate this is an anonymous submission for peer review.

**Vague Temporal References**

The manuscript mentions "the current administration's 'small yard, high fence' approach" without specifying which administration. Given data through 2025, this presumably refers to a hypothetical or future administration, creating confusion.

### 3.3 Analytical Missed Opportunities

- **Frame combinations**: The analysis treats frames as mutually exclusive categories, but real policy discourse typically combines multiple frames. Analysis of frame co-occurrence (e.g., sovereignty + innovation = "competition frame" as defined in the Discussion) could be more systematically developed.
- **Temporal dynamics**: With 90% of US data post-ChatGPT, the manuscript could analyze whether framing changed after this "event." The Discussion speculates about this but provides no systematic analysis.
- **Committee-level analysis**: Different congressional committees have different jurisdictions and constituencies. Armed Services framing might differ from Energy & Commerce framing in ways that illuminate the competition/governance divergence.

---

## 4. Specific Line-by-Line Suggestions

| Line/Location | Issue | Suggestion |
|---------------|-------|------------|
| Abstract, "Sovereignty framing...virtually absent" (1%) | Statistical reliability | Add caveat about small Global South sample and potential floor effects |
| Introduction, "first systematic comparison" | Scope claim | Substantiate or soften—Jobin et al. (2019) and Ulnicane et al. (2021) include some Global South cases |
| Literature Review, "systematic comparison...remains limited" | Missing citations | Cite **Cihon (2019)** on AI policy diffusion and **Roberts et al. (2021)** on African AI strategies |
| Method, "102 policy documents from South Africa, Brazil, and India" | Clarity | Clarify the exact document types for each country; currently ambiguous |
| Method, "7 parliamentary documents" for India | Justification | Explain why such a small sample is included despite representativeness concerns |
| Method, "eight-frame typology" | Theoretical grounding | Explain why these eight frames were selected; were others considered and excluded? |
| Method, "revised prompt substantially improved reliability" | Transparency | Provide both original and revised prompts in appendix for replicability |
| Findings, Table 1 | Statistics | Add Cramér's V for effect sizes; footnote on zero-cell issue for Safety/Technical |
| Findings, "the single most common frame" | Precision | At 22% vs. 21% for Innovation, this is essentially tied—revise language |
| Discussion, "adopter versus developer positioning" | Conceptualization | Add table mapping countries to developer/adopter status with empirical criteria |
| Discussion, EU comparison | Expansion | Systematically analyze EU documents using same methodology for valid comparison |
| Conclusion, "path dependencies that shape policy for decades" | Causal claim | Cite evidence for path dependency claim; currently unsupported assertion |

---

## 5. Suggestions for Revision

### Essential Revisions

1. **Restructure the "Global South" analysis**: Either drop India as insufficiently represented, or obtain more Indian documents. Consider analyzing Brazil and South Africa as separate cases rather than aggregating them.

2. **Address reliability concerns**: Either exclude the Rights frame from primary analysis given κ = .52, or provide detailed adjudication records showing how disagreements were resolved. Report all reliability statistics prominently, not buried in Method.

3. **Test alternative explanations**: Add analysis of partisan differences in US data (Republican vs. Democratic committee control) and institutional venue (security vs. domestic committees).

4. **Include Europe**: Add European AI policy documents coded with same methodology to test the developer/adopter hypothesis. If Europe shows governance framing despite developer status, the current explanation fails.

5. **Fix statistical reporting**: Add effect sizes, address zero-cell issues, and apply Bonferroni correction for multiple comparisons.

### Desirable Revisions

6. **Human validation**: Have human coders code a subset (n=50) to validate LLM coding decisions. Report human-LLM agreement statistics.

7. **Expand theoretical engagement**: Add sections on sociotechnical imaginaries (Jasanoff), postcolonial computing (Philip et al.), and digital sovereignty (Milan & Treré).

8. **Analyze frame combinations**: Move beyond single-frame dominance to analyze how frames combine (e.g., sovereignty + innovation = competition frame; governance + rights = protective governance).

9. **Longitudinal analysis**: With temporal concentration post-ChatGPT, analyze whether framing shifted after November 2022.

10. **Qualitative depth**: Add more exemplary quotations and indicate selection criteria. Include contradictory or ambiguous cases that complicate the neat competition/governance dichotomy.

---

## 6. Conclusion

This manuscript tackles an important question and assembles an impressive dataset. However, major theoretical, methodological, and analytical weaknesses undermine its contributions. The aggregation of heterogeneous "Global South" cases, unreliable coding for key frames, problematic statistical testing, and post-hoc circular reasoning about developer/adopter positioning prevent me from recommending acceptance.

If the authors can address the essential revisions—particularly the sample representativeness, reliability concerns, and alternative explanation testing—I would welcome resubmission. The topic deserves rigorous treatment, and with substantial revision, this manuscript could make a genuine contribution to our understanding of AI policy discourse across national contexts.

---

**Reviewer Recommendations for Action:**
- [ ] Major Revision Required (as indicated)
- [ ] Reject and Resubmit
- [ ] Minor Revision (only if essential revisions are addressed)
- [ ] Accept (not recommended in current form)

---

*Review completed by: Anonymous Reviewer*
*Date: March 2026*
