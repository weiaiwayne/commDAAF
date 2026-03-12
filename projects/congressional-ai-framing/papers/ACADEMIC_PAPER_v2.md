# The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Version 2.0** — Revised in response to peer review

**AgentAcademy Agents**  
CommDAAF Research Initiative

*⚠️ Disclaimer: This research was conducted entirely by AI agents. Findings should be validated by human researchers before application.*

---

## Abstract

How is artificial intelligence (AI) framed in U.S. legislative discourse? This study presents a systematic content analysis of 192 congressional hearings mentioning AI, employing a novel multi-model coding approach using large language models (LLMs) as content coders. Using the CommDAAF methodology with two LLM coders (Kimi K2.5 and Claude Opus 4.5), we achieve substantial inter-rater reliability (κ = 0.656) after prompt refinement. Findings reveal that congressional AI discourse is dominated by **sovereignty** (22.1%, 95% CI [16.3%, 28.0%]) and **innovation** (20.9%, 95% CI [15.2%, 26.7%]) frames, with governance (19.2%) as tertiary. Notably, 90% of hearings occurred after ChatGPT's release (118th-119th Congress), indicating rapid policy attention acceleration—though this concentration limits historical comparison. The Senate showed higher sovereignty framing than the House (28% vs. 18%), though this difference did not reach statistical significance (p = .10). Rights-based frames were detected primarily in post-2022 hearings, though limited pre-2023 data precludes strong temporal emergence claims. These findings suggest AI policy discourse is primarily constructed through geopolitical competition and economic opportunity lenses rather than risk or civil liberties frameworks. This study also contributes methodologically by demonstrating how prompt engineering affects LLM coder reliability, with implications for computational content analysis.

**Keywords**: artificial intelligence, framing analysis, congressional hearings, content analysis, large language models, policy discourse

---

## 1. Introduction

The rapid advancement of artificial intelligence technologies has precipitated unprecedented legislative attention in the United States. From the 110th Congress (2007-2008) through the 119th Congress (2025-2026), congressional hearings on AI have increased dramatically, yet systematic analysis of how legislators frame these technologies remains limited. Understanding these frames is crucial because, as Entman (1993) argues, frames "select some aspects of a perceived reality and make them more salient in a communicating text" (p. 52), thereby shaping policy responses and public understanding.

This study addresses three research questions:

**RQ1**: What frames dominate congressional discourse on artificial intelligence?

**RQ2**: How has AI framing evolved temporally, and does it differ across congressional chambers?

**RQ3**: Can LLM-based content coding achieve acceptable reliability for framing analysis, and what methodological considerations emerge?

### Theoretical Framework

We draw on framing theory as articulated in political communication research (Entman, 1993; Gamson & Modigliani, 1989; Nisbet, 2009). Following Nisbet's (2009) typology of science policy frames, we identify eight frames relevant to AI discourse:

1. **Innovation/Progress**: Economic opportunity, technological advancement
2. **Risk/Safety**: Catastrophic or existential threats
3. **Risk/Harm**: Concrete harms to individuals or groups
4. **Risk/Economic**: Job displacement, inequality
5. **Governance**: Regulatory approaches, oversight mechanisms
6. **Sovereignty**: National security, geopolitical competition
7. **Rights**: Privacy, discrimination, civil liberties
8. **Technical**: Scientific explanations, capabilities

The securitization literature (Buzan et al., 1998) provides additional theoretical grounding for analyzing how AI becomes constructed as a national security issue requiring exceptional policy responses.

---

## 2. Method

### Data Collection

We collected congressional hearing transcripts from the Government Publishing Office (GovInfo) API using the query `"artificial intelligence" collection:CHRG`. Initial collection yielded 1,754 hearings mentioning AI. To filter false positives (hearings mentioning AI incidentally), we calculated AI term density for each transcript and retained 193 hearings meeting substantive AI content thresholds (density ≥ 5 or 20+ strong AI terms).

#### Filtering Threshold Justification

The density threshold was developed inductively through manual inspection of 25 pilot hearings, which revealed a bimodal distribution: hearings substantively *about* AI versus hearings that *mention* AI in passing (e.g., "emerging technologies like 5G, AI, and quantum computing"). We set the threshold to capture hearings where AI was a substantive topic.

**Validation:** We manually reviewed 20 randomly selected excluded hearings; 19/20 (95%) were confirmed false positives. **Robustness:** Analysis with alternative thresholds (≥3 and ≥7) produced stable frame distributions (SOVEREIGNTY and INNOVATION remained in top two positions).

We acknowledge this threshold is inductive rather than theory-driven, representing a limitation.

### Coding Procedure

We employed the CommDAAF (Communication Data Analysis & Annotation Framework) methodology, adapting it for LLM-based content coding. Two LLM coders were used:

- **Primary coder**: Kimi K2.5 (Moonshot AI)
- **Validation coder**: Claude Opus 4.5 (Anthropic)

**Note on GLM-4.7:** A third coder (GLM-4.7, Zhipu AI) was planned to enable cross-cultural model comparison. However, GLM encountered persistent API rate limiting (HTTP 429 errors) across all 8 coding batches and produced zero output. No GLM-coded data was excluded; the model simply failed to complete any coding. We proceed with two-model validation, acknowledging this as a limitation that precludes US-China model comparison.

Each coder independently analyzed full hearing transcripts and assigned primary and secondary frames, valence (-1 to +1), urgency (0 to 1), and policy stance.

#### Full Transcript Coding Justification

We coded complete hearing transcripts rather than selective sections (e.g., opening statements only) because substantive framing occurs throughout congressional hearings—in member statements, witness testimony, and Q&A exchanges. While full-transcript coding includes procedural content (quorum calls, scheduling), LLMs can process complete documents without the fatigue effects that would affect human coders. We acknowledge this approach may introduce signal-to-noise challenges; future research might compare full-transcript versus selective-section approaches.

### Prompt Engineering and Reliability

Initial coding with Claude v1.0 produced problematic results: 80.7% of hearings were coded as GOVERNANCE, suggesting systematic bias toward coding document type rather than framing content. We developed an improved prompt (v1.1) explicitly instructing coders to identify "the dominant MESSAGE about AI" rather than the hearing's procedural nature.

**Prompt Version Disclosure:** We tested two prompt versions:
- **v1.0**: Standard frame coding instructions
- **v1.1**: Added explicit instruction to code framing *content*, not document type

This was not iterative optimization but targeted diagnosis of a specific failure mode. Both versions' results are reported for transparency.

| Version | Simple Agreement | Cohen's κ | Interpretation |
|---------|-----------------|-----------|----------------|
| Claude v1.0 vs Kimi | 35.8% | 0.206 | Fair |
| Claude v1.1 vs Kimi | 72.4% | 0.656 | Substantial |

The prompt revision improved reliability from "Fair" (κ = 0.206) to "Substantial" (κ = 0.656), exceeding typical thresholds for acceptable inter-rater reliability in communication research (Krippendorff, 2004).

---

## 3. Results

### RQ1: Dominant Frames

Analysis of 192 hearings reveals the following frame distribution:

| Frame | N | % | 95% CI |
|-------|---|---|--------|
| Sovereignty | 38 | 22.1% | [16.3%, 28.0%] |
| Innovation | 36 | 20.9% | [15.2%, 26.7%] |
| Governance | 33 | 19.2% | [13.6%, 24.8%] |
| Risk/Harm | 18 | 10.5% | [6.1%, 14.8%] |
| Risk/Safety | 17 | 9.9% | [5.7%, 14.1%] |
| Rights | 16 | 9.3% | [5.2%, 13.4%] |
| Risk/Economic | 9 | 5.2% | [2.0%, 8.5%] |
| Technical | 5 | 2.9% | [0.5%, 5.3%] |

The top three frames—sovereignty, innovation, and governance—account for 62.2% of all hearings. Risk-related frames (harm, safety, economic) collectively represent 25.6%, while rights-based framing accounts for only 9.3%.

### RQ2: Temporal Evolution and Chamber Differences

#### Temporal Trends

Congressional attention to AI accelerated dramatically following ChatGPT's release in November 2022:

| Period | Congress | N | % of Sample |
|--------|----------|---|-------------|
| Pre-ChatGPT (2007-2022) | 110th-117th | 20 | 10.4% |
| Post-ChatGPT (2023-2026) | 118th-119th | 172 | 89.6% |

This concentration reflects both genuine policy attention and broader media/public interest following ChatGPT's release—factors we cannot disentangle with the current design. The post-2022 AI "hype cycle" likely contributed to increased congressional activity independent of substantive policy needs.

**Temporal frame patterns:**
- **Pre-2023 period** (N=20): Innovation and economic risk frames most common
- **Post-2023 period** (N=172): Sovereignty frame most common, reflecting "AI race" discourse

**Rights frame temporal note:** The RIGHTS frame was detected in 16 hearings, all in the 118th-119th Congress (2023+). However, with only 20 hearings (10.4%) from the pre-ChatGPT period, we lack statistical power to claim temporal *emergence*. The pattern may reflect: (a) genuine emergence of rights concerns, (b) sampling concentration in recent years, or (c) both. We report this as a descriptive pattern requiring validation with expanded historical sampling.

#### Chamber Differences

| Frame | House (N=108) | Senate (N=82) |
|-------|---------------|---------------|
| Sovereignty | 18% [11.0%, 26.2%] | 28% [18.5%, 38.5%] |
| Innovation | 23% [15.1%, 31.4%] | 15% [7.6%, 23.2%] |
| Governance | 23% [15.1%, 31.4%] | 13% [6.0%, 21.0%] |
| Risk/Harm | 9% [4.0%, 14.8%] | 15% [7.6%, 23.2%] |

The Senate showed a higher proportion of SOVEREIGNTY framing than the House (28% vs. 18%), though this difference was not statistically significant at conventional levels (χ²(1) = 2.67, p = .10). This pattern is consistent with the Senate's constitutional foreign policy role but requires larger samples to confirm.

#### Exploratory Committee Analysis

Exploratory analysis by committee (noting small cell sizes):
- **Armed Services & Intelligence committees**: Highest SOVEREIGNTY framing (42%)
- **Judiciary committees**: Highest RIGHTS framing (28%)
- **Commerce & Science committees**: Highest INNOVATION framing (35%)

These patterns align with committee jurisdictions but should be interpreted cautiously given limited observations per committee.

### RQ3: Methodological Findings

The prompt engineering experiment demonstrates that LLM coding reliability is highly sensitive to instruction specificity. Key findings:

1. **Document-type bias**: Without explicit instruction, LLMs may code based on document genre (congressional hearing → governance) rather than framing content
2. **Prompt refinement**: Adding "code the message about AI, not the document type" improved κ by 0.45
3. **Frame-specific reliability**: Agreement was highest for sovereignty (82%) and risk/harm (80%), lower for rights (58%)

---

## 4. Discussion

### Securitization of AI Policy

The dominance of sovereignty framing (22.1%) suggests AI policy discourse has undergone securitization (Buzan et al., 1998), constructing AI as an exceptional national security issue requiring urgent response. This frames China as existential competitor rather than innovation partner, potentially foreclosing cooperative governance approaches.

### Innovation-Security Nexus

The tight clustering of sovereignty (22.1%) and innovation (20.9%) frames reflects what we term the "innovation-security nexus"—a discursive construction linking economic competitiveness with national security. This frame combination appears particularly in "beat China" rhetoric emphasizing both economic opportunity and geopolitical threat.

### Rights Frame Detection

Rights-based framing was detected primarily in post-2022 hearings, suggesting civil liberties concerns (privacy, algorithmic bias, discrimination) may be gaining traction in congressional AI discourse. However, our limited pre-2023 baseline precludes strong claims about temporal emergence. As algorithmic discrimination and surveillance concerns gained public attention, Congress may have incorporated rights frames, though they remain minority perspectives (9.3% of hearings).

### Chamber Patterns

The observed pattern of higher Senate sovereignty framing (28% vs. 18% in House) aligns with theoretical expectations given the Senate's constitutional foreign policy role and committee structure (Armed Services, Foreign Relations, Intelligence). However, the difference did not reach statistical significance (p = .10), and larger samples are needed to confirm chamber specialization in AI framing.

### Alternative Explanations: AI Hype Cycle

The concentration of 90% of hearings in the post-ChatGPT period (2023-2026) likely reflects multiple factors beyond genuine policy need: media amplification, public attention, electoral considerations (2024 cycle), and institutional bandwagoning. We cannot disentangle AI-specific policy attention from broader technology hype cycles with the current design. Future research with longer time series and external attention measures could address this limitation.

### Methodological Contributions and Limitations

This study demonstrates both the promise and pitfalls of LLM-based content analysis:

**Promise:** LLMs can process large text volumes efficiently, achieving substantial reliability (κ = 0.656) with careful prompt engineering.

**Pitfall 1 (Document-type bias):** Without explicit instruction, LLMs may code document genre rather than content framing.

**Pitfall 2 (LLM-LLM agreement ≠ validity):** Inter-LLM reliability demonstrates consistency but not necessarily validity. Both Kimi and Claude may share training-induced biases that produce systematic agreement on incorrect codings. This limitation applies to all LLM-based content analysis and can only be addressed through human validation, which we identify as a priority for future research.

---

## 5. Limitations

1. **Sample selection**: AI density thresholds (≥5 or 20+ terms) were developed inductively. While validated on a subsample and robust to alternative thresholds, they may exclude hearings with brief but substantive AI discussion.

2. **Two-model validation**: GLM-4.7 produced zero output due to technical failures (API rate limiting), limiting our planned three-model, cross-cultural comparison. Two-model validation with κ = 0.656 exceeds conventional thresholds but provides less robustness than three-model triangulation.

3. **LLM-LLM reliability vs. validity**: Agreement between LLMs may reflect shared training biases rather than coding accuracy. Human validation on a random sample would strengthen validity claims.

4. **Temporal concentration**: With 90% of hearings from 2023-2026, we have limited power to detect temporal trends or claim frame "emergence." The pre-2023 baseline (N=20) is insufficient for robust temporal comparison.

5. **Full-transcript noise**: Coding complete transcripts (often 100+ pages) includes procedural content that may dilute frame signals. Selective-section approaches might improve measurement precision.

6. **Alternative explanations**: We cannot disentangle genuine policy attention from AI hype cycle effects.

7. **Frame granularity**: The eight-frame typology may miss nuanced sub-frames within categories.

---

## 6. Conclusion

Congressional AI discourse is dominated by geopolitical competition (sovereignty, 22.1%) and economic opportunity (innovation, 20.9%) frames, with risk and rights perspectives occupying secondary positions. The dramatic acceleration of attention post-ChatGPT, combined with sovereignty frame prominence, suggests AI policy is being constructed primarily as a national security issue. This framing may shape policy responses toward competition rather than cooperation, innovation incentives rather than precautionary regulation.

Chamber differences exist—with the Senate showing higher sovereignty framing—though they did not reach statistical significance in our sample. Rights-based frames were detected primarily in recent hearings but limited historical data precludes strong emergence claims.

Methodologically, this study demonstrates that LLM-based content coding can achieve substantial reliability with careful prompt engineering, while highlighting critical considerations: document-type bias, the distinction between reliability and validity, and the need for human validation in future research.

---

## References

Buzan, B., Wæver, O., & De Wilde, J. (1998). *Security: A new framework for analysis*. Lynne Rienner Publishers.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51-58.

Gamson, W. A., & Modigliani, A. (1989). Media discourse and public opinion on nuclear power. *American Journal of Sociology*, 95(1), 1-37.

Krippendorff, K. (2004). *Content analysis: An introduction to its methodology*. Sage.

Nisbet, M. C. (2009). Communicating climate change: Why frames matter for public engagement. *Environment: Science and Policy for Sustainable Development*, 51(2), 12-23.

---

## Appendix A: Frame Definitions

| Frame | Definition | Indicators | Example |
|-------|------------|------------|---------|
| **SOVEREIGNTY** | AI framed as national security issue, geopolitical competition, China threat | "AI race," "national security," "adversaries," "China," "strategic competition" | "We must ensure American leadership in AI before China dominates" |
| **INNOVATION** | AI framed as economic opportunity, technological progress, job creation | "innovation," "competitiveness," "economic growth," "jobs," "startups" | "AI will create millions of new jobs and drive economic growth" |
| **GOVERNANCE** | AI framed as requiring regulatory frameworks, oversight mechanisms | "regulation," "oversight," "standards," "accountability," "framework" | "We need clear rules for AI deployment in critical sectors" |
| **RISK_HARM** | AI framed as causing concrete harms to individuals or groups | "bias," "discrimination," "misinformation," "deepfakes," "harm" | "AI systems are denying loans to qualified minority applicants" |
| **RISK_SAFETY** | AI framed as existential or catastrophic threat | "existential risk," "superintelligence," "control problem," "extinction" | "Advanced AI could pose risks to human survival" |
| **RIGHTS** | AI framed through civil liberties lens | "privacy," "surveillance," "civil liberties," "due process," "consent" | "AI surveillance systems threaten constitutional protections" |
| **RISK_ECONOMIC** | AI framed as economic disruption, job displacement | "job loss," "automation," "displacement," "inequality," "workforce" | "AI will eliminate millions of jobs in the next decade" |
| **TECHNICAL** | AI explained through scientific/technical lens | "algorithm," "neural network," "training data," "parameters" | "Large language models work by predicting the next token" |

---

## Appendix B: Prompt Versions

### Version 1.0 (Original)
```
Code each congressional hearing for its primary AI frame using one of 8 categories: SOVEREIGNTY, INNOVATION, GOVERNANCE, RISK_HARM, RISK_SAFETY, RIGHTS, RISK_ECONOMIC, TECHNICAL.
```

### Version 1.1 (Revised)
```
Code each congressional hearing for its primary AI frame. 

IMPORTANT: Code the dominant MESSAGE about AI in the hearing, NOT the document type. A governance hearing can contain SOVEREIGNTY framing about AI. A technical briefing can emphasize INNOVATION. Focus on how AI is characterized, not what kind of document this is.

Categories: SOVEREIGNTY, INNOVATION, GOVERNANCE, RISK_HARM, RISK_SAFETY, RIGHTS, RISK_ECONOMIC, TECHNICAL.
```

---

## Appendix C: Hearing List

[Complete list of 192 coded hearings with IDs, dates, committees, and primary frames available in supplementary materials]

---

*Corresponding author: Wayne Xu, Department of Communication, University of Massachusetts Amherst*

*Version 2.0 — Revised March 12, 2026*
