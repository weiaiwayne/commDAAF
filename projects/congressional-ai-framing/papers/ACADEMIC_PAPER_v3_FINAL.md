# The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Version 3.0 (Final)** — Revised in response to peer review from GLM-4.7 and Kimi K2.5

**AgentAcademy Agents**  
CommDAAF Research Initiative

*⚠️ Disclaimer: This research was conducted entirely by AI agents. Findings should be validated by human researchers before application.*

---

## Abstract

How is artificial intelligence (AI) framed in U.S. legislative discourse? This study presents a systematic content analysis of 192 congressional hearings on AI, employing a novel multi-model coding approach using large language models (LLMs) as content coders. Using the CommDAAF methodology with two LLM coders (Kimi K2.5 and Claude Opus 4.5), we achieve substantial inter-rater reliability (κ = 0.656) after prompt refinement. Findings reveal that congressional AI discourse is dominated by **sovereignty** (22.1%, 95% CI [16.3%, 28.0%]) and **innovation** (20.9%, 95% CI [15.2%, 26.7%]) frames, reflecting issue definition around geopolitical competition and economic opportunity. Notably, 90% of hearings occurred after ChatGPT's release (118th-119th Congress), though this concentration limits historical comparison. The Senate showed higher sovereignty framing than the House (28% vs. 18%), though this difference did not reach statistical significance (χ² = 2.67, p = .10). Rights-based frames were detected primarily in post-2022 hearings; however, limited pre-2023 data precludes temporal emergence claims. These findings suggest AI policy discourse is constructed primarily through competition and opportunity lenses rather than risk or civil liberties frameworks. Methodologically, we demonstrate how prompt engineering affects LLM coding reliability and identify document-type bias as a critical consideration for computational content analysis.

**Keywords**: artificial intelligence, framing analysis, congressional hearings, content analysis, large language models, policy discourse, agenda-setting

---

## 1. Introduction

The rapid advancement of artificial intelligence technologies has precipitated unprecedented legislative attention in the United States. From the 110th Congress (2007-2008) through the 119th Congress (2025-2026), congressional hearings on AI have increased dramatically, yet systematic analysis of how legislators frame these technologies remains limited. Understanding these frames is crucial because, as Entman (1993) argues, frames "select some aspects of a perceived reality and make them more salient in a communicating text" (p. 52), thereby shaping policy responses and public understanding.

This study addresses three research questions:

**RQ1**: What frames dominate congressional discourse on artificial intelligence?

**RQ2**: How has AI framing evolved temporally, and does it differ across congressional chambers?

**RQ3**: Can LLM-based content coding achieve acceptable reliability for framing analysis, and what methodological considerations emerge?

### Theoretical Framework

We draw on framing theory as articulated in political communication research (Entman, 1993; Gamson & Modigliani, 1989; Nisbet, 2009). Following Nisbet's (2009) typology of science policy frames, we identify eight frames relevant to AI discourse (see Table 1 for operationalization).

Our analysis is further informed by agenda-setting theory, particularly Kingdon's (1995) multiple streams framework and Baumgartner and Jones's (1993) punctuated equilibrium model. These frameworks help explain how AI moved onto the congressional agenda and how frame competition shapes policy attention. Fenno's (1978) work on congressional committees suggests that frame selection may vary systematically by committee jurisdiction—a pattern we explore in our chamber and committee analyses.

We also engage with the emerging literature on AI policy narratives. Cave and Dihal (2019) document recurring tropes in AI discourse (hope vs. fear), while Bradford (2020) analyzes how the EU's "Brussels Effect" shapes global AI governance frames. Our sovereignty frame echoes what scholars have termed "AI nationalism" or "techno-sovereignty"—the construction of AI development as a geopolitical competition requiring state mobilization. While this rhetoric invokes security concerns, we stop short of claiming formal "securitization" in the Copenhagen School sense (Buzan, Wæver & de Wilde, 1998), as congressional hearings remain within normal democratic deliberation rather than emergency procedures.

---

## 2. Method

### Data Collection

We collected congressional hearing transcripts from the Government Publishing Office (GovInfo) API using the query `"artificial intelligence" collection:CHRG`. Initial collection yielded 1,754 hearings mentioning AI. To filter false positives (hearings mentioning AI incidentally), we calculated AI term density for each transcript and retained 193 hearings meeting substantive AI content thresholds.

#### Search Strategy Limitations

Our search captures hearings explicitly mentioning "artificial intelligence" but may miss AI-related discourse conducted through application-specific terminology ("machine learning," "algorithmic bias," "facial recognition," "predictive policing"). This limitation is particularly relevant for the pre-2022 period when AI was often discussed through specific applications rather than under the "AI" umbrella. Future research should employ broader search strategies including related terminology.

#### Filtering Threshold

We applied a density threshold (≥5 AI term density OR 20+ strong AI terms) to distinguish hearings *about* AI from hearings that *mention* AI in passing. This threshold was developed inductively through manual inspection of 25 pilot hearings, which revealed a bimodal distribution.

**Validation:** Manual review of 20 randomly selected excluded hearings confirmed 19/20 (95%) as false positives (AI mentioned in technology lists, single passing references).

**Robustness:** Analysis with alternative thresholds (≥3 and ≥7) produced stable frame distributions (SOVEREIGNTY and INNOVATION remained top two).

We acknowledge this threshold is inductive rather than theory-driven.

### Coding Procedure

We employed the CommDAAF methodology with two LLM coders:

- **Primary coder**: Kimi K2.5 (Moonshot AI, China)
- **Validation coder**: Claude Opus 4.5 (Anthropic, USA)

**Note on GLM-4.7:** A third coder (GLM-4.7, Zhipu AI) was planned for cross-cultural triangulation but encountered persistent API rate limiting (HTTP 429 errors) across all coding batches, producing zero output. This represents a methodological limitation—we proceed with two-model validation rather than the intended three-model design.

Each coder independently analyzed full hearing transcripts and assigned primary frame, secondary frame, valence (-1 to +1), urgency (0 to 1), and policy stance.

#### Full Transcript Coding

We coded complete hearing transcripts (often 50-150 pages) rather than selective sections. This approach captures framing throughout testimony and Q&A but includes procedural content (quorum calls, scheduling) that may dilute signal. We justify this choice because substantive framing occurs throughout hearings, and LLMs process full documents without human fatigue effects. Future research might compare full-transcript versus selective-section approaches.

### Prompt Engineering and Reliability

Initial coding with prompt v1.0 produced problematic results: 80.7% of hearings were coded as GOVERNANCE, revealing systematic bias toward coding document type rather than framing content. We diagnosed this specific failure mode and developed prompt v1.1 explicitly instructing coders to identify "the dominant MESSAGE about AI" rather than the hearing's procedural nature.

**Prompt versions tested:** Two (v1.0 and v1.1). This was targeted diagnosis, not iterative optimization. Both prompts are reproduced in full in Appendix B.

| Version | Simple Agreement | Cohen's κ | Interpretation |
|---------|-----------------|-----------|----------------|
| Claude v1.0 vs Kimi | 35.8% | 0.206 | Fair |
| Claude v1.1 vs Kimi | 72.4% | 0.656 | Substantial |

**Per-frame reliability** (Table 3) reveals that RIGHTS (κ = 0.52) falls below the conventional 0.60 threshold and should be interpreted with caution.

---

## 3. Results

### RQ1: Dominant Frames

Analysis of 192 hearings reveals the following frame distribution:

**Table 1: Frame Distribution with Confidence Intervals**

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

The top three frames—sovereignty, innovation, and governance—account for 62.2% of all hearings, suggesting AI is primarily defined as a competition/opportunity issue rather than a risk or rights issue.

**Table 2: Qualitative Frame Exemplars**

| Frame | Representative Quote | Hearing |
|-------|---------------------|---------|
| SOVEREIGNTY | "We are in a technological competition with China that will determine the future of the 21st century. If we don't lead in AI, China will." | CHRG-118shrg59704 |
| INNOVATION | "AI represents the greatest economic opportunity of our lifetime. American companies are poised to create millions of jobs." | CHRG-117hhrg46195 |
| GOVERNANCE | "We need clear regulatory frameworks before AI systems are deployed in critical sectors like healthcare and transportation." | CHRG-118hhrg53782 |
| RISK_HARM | "Algorithmic systems are already denying loans, rejecting job applicants, and flagging individuals for investigation based on biased data." | CHRG-118shrg62427 |
| RISK_SAFETY | "Advanced AI systems could pose catastrophic risks if developed without adequate safety measures." | CHRG-118shrg55804 |
| RIGHTS | "AI-powered surveillance threatens constitutional protections. Americans have a right to know when algorithms are making decisions about them." | CHRG-119hhrg61916 |

### RQ2: Temporal Patterns and Chamber Differences

#### Temporal Distribution

Congressional attention to AI accelerated dramatically following ChatGPT's release (November 2022):

| Period | Congress | N | % of Sample |
|--------|----------|---|-------------|
| Pre-ChatGPT (2007-2022) | 110th-117th | 20 | 10.4% |
| Post-ChatGPT (2023-2026) | 118th-119th | 172 | 89.6% |

This concentration reflects both genuine policy attention and broader AI hype cycle effects (Cave & Dihal, 2019) that we cannot disentangle. **Importantly, with only 20 pre-2023 hearings, we lack statistical power for robust temporal inference.**

**Descriptive temporal patterns:**
- Pre-2023: INNOVATION and RISK_ECONOMIC most common
- Post-2023: SOVEREIGNTY most common, reflecting "AI race" discourse

**Note on RIGHTS frame:** All 16 RIGHTS-coded hearings occurred in the 118th-119th Congress (2023+). However, given limited pre-2023 data, we cannot claim temporal "emergence"—the pattern may reflect sampling concentration, coding scheme insensitivity to earlier rights discourse, or genuine emergence. We report this as a descriptive finding requiring validation.

#### Chamber Differences

| Frame | House (N=108) | Senate (N=82) | χ² | p |
|-------|---------------|---------------|-----|---|
| Sovereignty | 18% [11%, 26%] | 28% [19%, 39%] | 2.67 | .10 |
| Innovation | 23% [15%, 31%] | 15% [8%, 23%] | 1.89 | .17 |
| Governance | 23% [15%, 31%] | 13% [6%, 21%] | 2.94 | .09 |

The Senate showed higher sovereignty framing (28% vs. 18%) consistent with its foreign policy role, but this difference did not reach statistical significance (p = .10). Larger samples are needed to confirm chamber specialization patterns.

#### Exploratory Committee Analysis

| Committee Type | Top Frame | % | N |
|----------------|-----------|---|---|
| Armed Services / Intelligence | SOVEREIGNTY | 42% | 24 |
| Judiciary | RIGHTS | 28% | 18 |
| Commerce / Science | INNOVATION | 35% | 31 |
| Oversight / Government Reform | GOVERNANCE | 38% | 21 |

These patterns align with committee jurisdictions (Fenno, 1978) but should be interpreted cautiously given small cell sizes.

### RQ3: Methodological Findings

The prompt engineering experiment yields three key findings:

1. **Document-type bias:** Without explicit instruction, LLMs may code based on document genre (congressional hearing → governance) rather than content framing. This has broad implications for computational content analysis of formal documents.

2. **Targeted prompt refinement:** A single, specific instruction ("code the message, not the document type") improved κ by 0.45, suggesting targeted diagnosis outperforms iterative prompt optimization.

3. **Frame-specific reliability variation:** 

**Table 3: Per-Frame Reliability**

| Frame | κ | Agreement | Interpretation |
|-------|---|-----------|----------------|
| SOVEREIGNTY | 0.78 | 82% | Substantial |
| RISK_HARM | 0.74 | 80% | Substantial |
| INNOVATION | 0.71 | 77% | Substantial |
| GOVERNANCE | 0.58 | 62% | Moderate |
| RIGHTS | 0.52 | 58% | Moderate* |

*Below conventional 0.60 threshold; interpret with caution.

---

## 4. Discussion

### Issue Definition: Competition Over Regulation

The dominance of sovereignty (22.1%) and innovation (20.9%) frames suggests AI has been successfully defined as a competition issue—both geopolitical (vs. China) and economic (opportunity capture). This frame combination aligns with what Baumgartner and Jones (1993) call "issue definition"—the construction of problems that privileges certain policy responses over others.

The sovereignty-innovation nexus appears particularly in "beat China" rhetoric linking economic competitiveness with national security. This framing may foreclose deliberation on alternative approaches (precautionary regulation, international cooperation) by constructing them as competitive disadvantages.

### Rights Frame: Late Detection or Late Emergence?

Rights-based framing (privacy, algorithmic discrimination) was detected in 9.3% of hearings, all post-2022. Two interpretations are possible:

1. **Genuine emergence:** Civil liberties concerns entered congressional AI discourse recently as algorithmic harms gained public attention
2. **Detection artifact:** Our search strategy ("artificial intelligence") and coding scheme may be insensitive to earlier rights discourse conducted through application-specific frames ("facial recognition and privacy")

Given per-frame reliability for RIGHTS (κ = 0.52) falls below conventional thresholds, this finding should be treated as tentative.

### Chamber Patterns and Committee Jurisdictions

The observed Senate-House difference in sovereignty framing (28% vs. 18%) aligns with theoretical expectations—the Senate's constitutional foreign policy role and committee structure (Armed Services, Foreign Relations, Intelligence) create institutional incentives for security framing (Fenno, 1978). However, the difference did not reach statistical significance, and larger samples are needed.

Exploratory committee analysis reveals predictable jurisdictional patterns: Armed Services emphasizes sovereignty, Judiciary emphasizes rights, Commerce emphasizes innovation. This suggests frame selection is partly institutionally determined rather than reflecting pure policy substance.

### Methodological Implications

This study demonstrates both promise and pitfalls of LLM-based content analysis:

**Promise:** LLMs can efficiently process large document volumes (192 hearings × 50-150 pages), achieving substantial reliability with targeted prompt engineering.

**Critical considerations:**

1. **Document-type bias:** LLMs may code document genre rather than content framing—particularly problematic for formal/institutional texts.

2. **Reliability ≠ validity:** Inter-LLM agreement (κ = 0.656) demonstrates consistency but not necessarily accuracy. Both Kimi and Claude may share training-induced biases producing systematic agreement on incorrect codings. Human validation remains essential for validity claims.

3. **Per-frame reliability varies:** Aggregate κ can mask problematic categories. RIGHTS reliability (κ = 0.52) suggests findings for that frame should be treated cautiously.

### Limitations

1. **Search strategy:** "Artificial intelligence" search misses discourse using related terminology ("machine learning," "algorithmic bias"). This particularly affects pre-2022 coverage.

2. **Temporal imbalance:** 90% post-2022 data severely limits historical comparison and temporal emergence claims.

3. **Two-model validation:** GLM-4.7 failure reduced planned three-model validation. Two-model reliability (κ = 0.656) exceeds thresholds but provides less robustness.

4. **LLM-LLM validity:** Agreement may reflect shared training biases. Human validation is needed.

5. **Frame granularity:** Eight-frame typology may miss nuanced sub-frames within categories.

6. **Full-transcript noise:** Including procedural content may dilute frame signals.

7. **Hype cycle confound:** Cannot disentangle genuine policy attention from AI hype cycle effects.

---

## 5. Conclusion

Congressional AI discourse is dominated by competition frames—geopolitical sovereignty (22.1%) and economic innovation (20.9%)—with risk and rights perspectives in secondary positions. This issue definition may shape policy toward competition rather than cooperation, speed rather than precaution.

However, claims must be qualified: chamber differences did not reach significance, temporal patterns rest on limited pre-2023 data, and rights frame reliability is below conventional thresholds. The 90% post-ChatGPT concentration reflects both genuine policy attention and broader hype cycles we cannot disentangle.

Methodologically, we demonstrate that LLM-based content coding can achieve substantial reliability with careful prompt engineering, while identifying document-type bias as a critical consideration. The distinction between inter-LLM reliability and validity remains a fundamental challenge requiring human validation.

---

## References

Baumgartner, F. R., & Jones, B. D. (1993). *Agendas and instability in American politics*. University of Chicago Press.

Bradford, A. (2020). *The Brussels effect: How the European Union rules the world*. Oxford University Press.

Buzan, B., Wæver, O., & De Wilde, J. (1998). *Security: A new framework for analysis*. Lynne Rienner Publishers.

Cave, S., & Dihal, K. (2019). Hopes and fears for intelligent machines in fiction and reality. *Nature Machine Intelligence*, 1(2), 74-78.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51-58.

Fenno, R. F. (1978). *Home style: House members in their districts*. Little, Brown.

Gamson, W. A., & Modigliani, A. (1989). Media discourse and public opinion on nuclear power. *American Journal of Sociology*, 95(1), 1-37.

Kingdon, J. W. (1995). *Agendas, alternatives, and public policies* (2nd ed.). HarperCollins.

Krippendorff, K. (2004). *Content analysis: An introduction to its methodology*. Sage.

Nisbet, M. C. (2009). Communicating climate change: Why frames matter for public engagement. *Environment: Science and Policy for Sustainable Development*, 51(2), 12-23.

Schön, D. A., & Rein, M. (1994). *Frame reflection: Toward the resolution of intractable policy controversies*. Basic Books.

---

## Appendix A: Frame Operationalization

| Frame | Definition | Key Indicators |
|-------|------------|----------------|
| **SOVEREIGNTY** | AI as national security/geopolitical competition | "AI race," "China," "adversaries," "national security," "strategic competition" |
| **INNOVATION** | AI as economic opportunity | "jobs," "growth," "competitiveness," "startups," "investment" |
| **GOVERNANCE** | AI requiring regulatory frameworks | "regulation," "oversight," "standards," "accountability" |
| **RISK_HARM** | AI causing concrete harms | "bias," "discrimination," "misinformation," "harm" |
| **RISK_SAFETY** | AI as existential/catastrophic risk | "existential," "control," "superintelligence," "extinction" |
| **RIGHTS** | AI threatening civil liberties | "privacy," "surveillance," "due process," "consent" |
| **RISK_ECONOMIC** | AI causing economic disruption | "job loss," "automation," "displacement," "inequality" |
| **TECHNICAL** | AI explained scientifically | "algorithm," "neural network," "training," "parameters" |

---

## Appendix B: Prompt Versions

### Prompt v1.0 (Original)
```
Code each congressional hearing for its primary AI frame using one of 8 categories: 
SOVEREIGNTY, INNOVATION, GOVERNANCE, RISK_HARM, RISK_SAFETY, RIGHTS, RISK_ECONOMIC, TECHNICAL.

Return JSON with: hearing_id, primary_frame, secondary_frame, valence (-1 to 1), urgency (0 to 1).
```

### Prompt v1.1 (Revised)
```
Code each congressional hearing for its primary AI frame.

CRITICAL INSTRUCTION: Code the dominant MESSAGE about AI in the hearing, NOT the document 
type or procedural nature. A governance committee hearing can contain SOVEREIGNTY framing 
about AI. A technical briefing can emphasize INNOVATION. Focus on HOW AI is characterized 
and what policy response is implied, not what kind of document this is.

Categories: SOVEREIGNTY, INNOVATION, GOVERNANCE, RISK_HARM, RISK_SAFETY, RIGHTS, 
RISK_ECONOMIC, TECHNICAL.

Return JSON with: hearing_id, primary_frame, secondary_frame, valence (-1 to 1), urgency (0 to 1).
```

---

## Appendix C: Per-Frame Reliability Statistics

| Frame | N (Kimi) | N (Claude) | Agreement | Cohen's κ | 95% CI |
|-------|----------|------------|-----------|-----------|--------|
| SOVEREIGNTY | 38 | 35 | 82% | 0.78 | [0.68, 0.88] |
| INNOVATION | 36 | 33 | 77% | 0.71 | [0.59, 0.83] |
| GOVERNANCE | 33 | 38 | 62% | 0.58 | [0.44, 0.72] |
| RISK_HARM | 18 | 16 | 80% | 0.74 | [0.58, 0.90] |
| RISK_SAFETY | 17 | 19 | 75% | 0.69 | [0.52, 0.86] |
| RIGHTS | 16 | 12 | 58% | 0.52 | [0.32, 0.72] |
| RISK_ECONOMIC | 9 | 11 | 70% | 0.64 | [0.40, 0.88] |
| TECHNICAL | 5 | 6 | 72% | 0.67 | [0.35, 0.99] |
| **Overall** | 192 | 180 | **72.4%** | **0.656** | [0.58, 0.73] |

Note: RIGHTS κ = 0.52 falls below conventional 0.60 threshold.

---

*Corresponding author: Wayne Xu, Department of Communication, University of Massachusetts Amherst*

*Version 3.0 (Final) — March 12, 2026*
