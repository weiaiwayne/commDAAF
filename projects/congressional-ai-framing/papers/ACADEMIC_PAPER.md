# The Framing of Artificial Intelligence in U.S. Congressional Discourse: A Multi-Model Content Analysis

**Wayne Xu**  
Department of Communication  
University of Massachusetts Amherst

---

## Abstract

How is artificial intelligence (AI) framed in U.S. legislative discourse? This study presents a systematic content analysis of 192 congressional hearings mentioning AI, employing a novel multi-model coding approach using large language models (LLMs) as content coders. Using the CommDAAF methodology with two LLM coders (Kimi K2.5 and Claude Opus 4.5), we achieve substantial inter-rater reliability (κ = 0.656) after prompt refinement. Findings reveal that congressional AI discourse is dominated by **sovereignty** (22.1%) and **innovation** (20.9%) frames, with governance (19.2%) as tertiary. Notably, 90% of hearings occurred after ChatGPT's release (118th-119th Congress), indicating rapid policy attention acceleration. The Senate emphasizes national security framing significantly more than the House (28% vs 18%), while rights-based frames only emerged in the 118th Congress (2023+). These findings suggest AI policy discourse is primarily constructed through geopolitical competition and economic opportunity lenses rather than risk or civil liberties frameworks. This study also contributes methodologically by demonstrating how prompt engineering affects LLM coder reliability, with implications for computational content analysis.

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

### Coding Procedure

We employed the CommDAAF (Communication Data Analysis & Annotation Framework) methodology, adapting it for LLM-based content coding. Two LLM coders were used:

- **Primary coder**: Kimi K2.5 (Moonshot AI)
- **Validation coder**: Claude Opus 4.5 (Anthropic)

Each coder independently analyzed full hearing transcripts and assigned primary and secondary frames, valence (-1 to +1), urgency (0 to 1), and policy stance.

### Prompt Engineering and Reliability

Initial coding with Claude v1 produced problematic results: 80.7% of hearings were coded as GOVERNANCE, suggesting systematic bias toward coding document type rather than framing content. We developed an improved prompt (v1.1) explicitly instructing coders to identify "the dominant MESSAGE about AI" rather than the hearing's procedural nature.

| Version | Simple Agreement | Cohen's κ | Interpretation |
|---------|-----------------|-----------|----------------|
| Claude v1 vs Kimi | 35.8% | 0.206 | Fair |
| Claude v2 vs Kimi | 72.4% | 0.656 | Substantial |

The prompt revision improved reliability from "Fair" (κ = 0.206) to "Substantial" (κ = 0.656), exceeding typical thresholds for acceptable inter-rater reliability in communication research (Krippendorff, 2004).

---

## 3. Results

### RQ1: Dominant Frames

Analysis of 192 hearings reveals the following frame distribution:

| Frame | N | % |
|-------|---|---|
| Sovereignty | 38 | 22.1% |
| Innovation | 36 | 20.9% |
| Governance | 33 | 19.2% |
| Risk/Harm | 18 | 10.5% |
| Risk/Safety | 17 | 9.9% |
| Rights | 16 | 9.3% |
| Risk/Economic | 9 | 5.2% |
| Technical | 5 | 2.9% |

**[INSERT FIGURE 2: Frame Distribution Donut Chart]**

The top three frames—sovereignty, innovation, and governance—account for 62.2% of all hearings. Risk-related frames (harm, safety, economic) collectively represent 25.6%, while rights-based framing accounts for only 9.3%.

### RQ2: Temporal Evolution and Chamber Differences

#### Temporal Trends

Congressional attention to AI accelerated dramatically following ChatGPT's release in November 2022:

| Period | Congress | N | % of Sample |
|--------|----------|---|-------------|
| Early (2007-2022) | 110th-117th | 20 | 10.4% |
| Post-ChatGPT | 118th-119th | 172 | 89.6% |

**[INSERT FIGURE 1: Temporal Trend Bar Chart]**

Frame evolution shows notable patterns:
- **Early period**: Innovation and economic risk frames dominated
- **Recent period**: Sovereignty frame emerged as dominant, reflecting "AI race" discourse

The rights frame only appeared in the 118th Congress (2023+), suggesting civil liberties concerns are recent additions to congressional AI discourse.

**[INSERT FIGURE 4: Frame Evolution Stacked Area Chart]**

#### Chamber Differences

Significant differences emerge between chambers:

| Frame | House | Senate |
|-------|-------|--------|
| Sovereignty | 18% | **28%** |
| Innovation | 23% | 15% |
| Governance | 23% | 13% |
| Risk/Harm | 9% | **15%** |

**[INSERT FIGURE 3: Chamber Comparison Bar Chart]**

The Senate emphasizes sovereignty framing significantly more than the House (χ² = 4.82, p < .05), consistent with its constitutional role in foreign policy and national security. The House shows more balanced distribution between innovation and governance frames.

### RQ3: Methodological Findings

The prompt engineering experiment demonstrates that LLM coding reliability is highly sensitive to instruction specificity. Key findings:

1. **Document-type bias**: Without explicit instruction, LLMs may code based on document genre (congressional hearing → governance) rather than framing content
2. **Prompt refinement**: Adding "code the message about AI, not the document type" improved κ by 0.45
3. **Frame-specific reliability**: Agreement was highest for sovereignty (82%) and risk/harm (80%), lower for rights (58%)

**[INSERT FIGURE 5: Reliability Improvement Bar Chart]**

---

## 4. Discussion

### Securitization of AI Policy

The dominance of sovereignty framing (22.1%) suggests AI policy discourse has undergone securitization (Buzan et al., 1998), constructing AI as an exceptional national security issue requiring urgent response. This frames China as existential competitor rather than innovation partner, potentially foreclosing cooperative governance approaches.

### Innovation-Security Nexus

The tight clustering of sovereignty (22.1%) and innovation (20.9%) frames reflects what we term the "innovation-security nexus"—a discursive construction linking economic competitiveness with national security. This frame combination appears particularly in "beat China" rhetoric emphasizing both economic opportunity and geopolitical threat.

### Rights Frame Emergence

The late emergence of rights-based framing (only in 118th Congress) suggests civil liberties concerns have been systematically marginalized in AI policy discourse. As algorithmic discrimination and surveillance concerns gained public attention, Congress began incorporating rights frames, though they remain minority perspectives.

### Chamber Specialization

Senate emphasis on sovereignty reflects its constitutional foreign policy role and committee structure (Armed Services, Foreign Relations, Intelligence). House emphasis on governance may reflect its closer connection to constituent concerns and regulatory implementation.

### Methodological Contributions

This study demonstrates both the promise and pitfalls of LLM-based content analysis. While LLMs can process large text volumes efficiently, reliability depends critically on prompt engineering. Our finding that document-type bias affects LLM coding has implications for computational communication research broadly.

---

## 5. Limitations

1. **Sample selection**: AI density thresholds may exclude hearings with brief but substantive AI discussion
2. **Two-model validation**: GLM-4.7 was dropped due to rate limits, limiting cross-cultural model comparison
3. **Frame granularity**: Eight-frame typology may miss nuanced sub-frames
4. **Temporal concentration**: 90% of sample from 2023-2026 limits historical trend analysis

---

## 6. Conclusion

Congressional AI discourse is dominated by geopolitical competition and economic opportunity frames, with risk and rights perspectives occupying secondary positions. The dramatic acceleration of attention post-ChatGPT, combined with sovereignty frame dominance, suggests AI policy is being constructed primarily as a national security issue. This framing may shape policy responses toward competition rather than cooperation, innovation incentives rather than precautionary regulation.

Methodologically, this study demonstrates that LLM-based content coding can achieve substantial reliability with careful prompt engineering, offering a scalable approach for large-scale framing analysis while highlighting the importance of addressing document-type bias.

---

## References

Buzan, B., Wæver, O., & De Wilde, J. (1998). *Security: A new framework for analysis*. Lynne Rienner Publishers.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51-58.

Gamson, W. A., & Modigliani, A. (1989). Media discourse and public opinion on nuclear power. *American Journal of Sociology*, 95(1), 1-37.

Krippendorff, K. (2004). *Content analysis: An introduction to its methodology*. Sage.

Nisbet, M. C. (2009). Communicating climate change: Why frames matter for public engagement. *Environment: Science and Policy for Sustainable Development*, 51(2), 12-23.

---

## Appendix

### A. Coding Scheme (CommDAAF v1.1)

[Full coding scheme available in supplementary materials]

### B. Frame Definitions

[Detailed operationalization of each frame]

### C. Hearing List

[Complete list of 192 coded hearings with IDs and primary frames]

---

*Corresponding author: Wayne Xu, Department of Communication, University of Massachusetts Amherst*
