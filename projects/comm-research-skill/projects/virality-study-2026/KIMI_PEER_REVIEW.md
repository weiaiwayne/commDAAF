# Peer Review by Kimi K2.5

**Date:** 2026-02-27  
**Reviewer:** Kimi K2.5 (Moonshot AI) via OpenCode  
**Role:** Simulated peer reviewer for Journal of Communication / Political Communication

---

## PAPER 1: "Information Over Emotion? Frame Effects on Viral Engagement in the #MahsaAmini Movement"

### 1. Summary
This paper examines what drives viral engagement in protest content by analyzing 380 tweets from the #MahsaAmini movement. Using multi-model LLM content analysis, the authors find that informational framing (IRR = 2.72) outperforms emotional frames, challenging moral contagion theory's predictions about emotional content diffusion in crisis contexts marked by information scarcity.

### 2. Strengths
- **Strong theoretical grounding** in framing theory and moral contagion research with clear hypotheses
- **Appropriate sampling strategy** using stratification by engagement tier rather than convenience sampling
- **Multi-model validation approach** (3 LLMs) provides reliability check unavailable in single-model studies
- **Correct statistical modeling** using negative binomial regression for overdispersed count data
- **Honest limitation discussion** including frame-specific reliability issues and small cell sizes

### 3. Weaknesses/Concerns
- **No human validation** of LLM coding—findings rest entirely on machine agreement without ground truth
- **Small sample size** (n=380) for claims about viral dynamics, which typically require much larger N
- **Confounding by network position** not addressed—informational content may spread because it's posted by high-follower accounts, not because of frame effects
- **Temporal confounding**—frame prevalence may shift over the 2-week period as events evolve
- **Selection bias**—Twitter Academic API access and hashtag-based sampling miss non-hashtagged content and suspended accounts

### 4. Major Issues Requiring Revision
1. **Human validation is essential** for confirmatory claims. At minimum, a human-coded subsample (n=100) with inter-coder reliability is needed to validate that LLMs measure the theoretical constructs intended.
2. **Network controls missing**—engagement is heavily influenced by follower count, prior engagement history, and network position. Without these controls, frame effects are confounded with account characteristics.
3. **Causal identification**—the paper implies causality ("informational framing...predicted viral engagement") but has observational data. Language about "effects" and "prediction" should be tempered or instrumental variable approaches considered.
4. **CONFLICT frame reliability too low** (33% three-way agreement, n=18) to report meaningful results. This frame should be excluded or flagged as completely unreliable.

### 5. Minor Issues
- Table 1: Report model fit statistics (AIC, BIC, dispersion parameter)
- Abstract says "380 Twitter posts" but methods say stratified sampling from larger dataset—clarify N
- Missing discussion of why INFORMATIONAL showed small Cohen's d (0.25) but large IRR (2.72)—effect size interpretation needs reconciliation
- No discussion of multiple comparisons—7 frames × 2 arousal levels = many tests
- Language distribution percentages don't sum to 100% (69.2 + 22.9 + 4.5 + 3.4 = 100.0—actually they do, but "undefined" is odd)

### 6. Missing Literature
- **Bail et al. (2018)** on exposure vs. engagement—important distinction for virality claims
- **Tucker et al. (2018)** on social media and protest—relevant to Iranian context
- **Metzger et al. (2020)** on information-seeking during crisis—strengthens information-scarcity hypothesis
- **Vosoughi et al. (2018)** on true vs. false news diffusion—relevant to informational content claims
- **Theocharis et al. (2015)** on Twitter protest dynamics—comparative context needed

### 7. Questions for Authors
1. Did you examine whether informational posts came from different account types (journalists, activists, ordinary users) than emotional posts?
2. How did you handle retweets vs. original tweets? Were retweets excluded, and if so, how does this affect generalizability?
3. Why does INFORMATIONAL have a small Cohen's d but large IRR? Is this a distribution issue?
4. Did frame prevalence shift over the 2-week period? Early protests may have different dynamics than later phases.
5. What proportion of posts were multimedia (images/video) vs. text-only, and how might this interact with frame effects?

### 8. Overall Assessment: **Major Revisions**

**Justification:** The paper makes an interesting theoretical contribution with the information-scarcity hypothesis, but the lack of human validation for LLM coding is a critical methodological gap for a journal like *Journal of Communication* or *Political Communication*. The causal language without proper identification strategy and missing network controls are also serious issues. The small CONFLICT cell size and low reliability for multiple frames further weaken confidence in findings. With human validation, network controls, and more cautious causal language, this could be a valuable contribution.

---

## PAPER 2: "Toward Agentic Content Analysis: A Reflexive Account of Human-AI Collaborative Research"

### 1. Summary
This reflexive methods paper documents the development and implementation of an LLM-assisted content analysis workflow, introducing CommDAAF (Communication Data Analyst Augmentation Framework). Drawing on experience analyzing #MahsaAmini tweets, the authors catalog failures (data contamination, inappropriate models, oversimplified prompts) and extract ten practices for human-AI collaborative research, arguing that agentic methods transform rather than eliminate human judgment.

### 2. Strengths
- **Exceptional transparency** about failures and iterative corrections—models methodological reflexivity
- **Practical framework (CommDAAF)** with concrete prompt structure and validation tiers fills a genuine gap in methodological guidance
- **Multi-model approach** (3 models from different providers) addresses single-model bias concerns
- **Failure taxonomy** is genuinely useful for the field—data, prompt, technical, and analytical failures are well-categorized
- **Ten concrete practices** provide actionable guidance for researchers adopting these methods

### 3. Weaknesses/Concerns
- **Single case study** limits generalizability—claims about "agentic content analysis" rest on one project with one coding scheme
- **No comparison to human coding**—the paper never establishes whether LLM coding is actually valid, only that models agree with each other
- **Circular reliability problem**—inter-model agreement doesn't validate constructs, only consistency
- **Missing cost analysis**—claims about efficiency lack concrete numbers (API costs vs. human coder wages)
- **Ethics section is underdeveloped**—raises important questions but doesn't engage seriously with labor displacement or environmental costs

### 4. Major Issues Requiring Revision
1. **Validity evidence missing**—the paper needs at least a pilot comparison showing LLM codes correlate with human expert coding on a subsample. Without this, CommDAAF is a reliability framework, not a validity framework.
2. **Overclaiming generalizability**—"Ten Practices for Agentic Content Analysis" implies these generalize beyond this case, but the paper provides no evidence. The practices should be framed as provisional or preliminary.
3. **No discussion of when NOT to use agentic methods**—the paper is entirely promotional. What types of coding tasks are LLMs unsuited for? When is human coding still necessary?
4. **Missing literature on LLM validity**—Ziems et al. (2024) and Gilardi et al. (2023) are cited but their findings about LLM limitations aren't engaged seriously.

### 5. Minor Issues
- The "Fifth failure" (inappropriate statistical model) seems like a stretch—this is standard research practice, not a failure unique to agentic methods
- CommDAAF acronym is awkward and unexplained (why "Communication" and not "Content"?)
- No discussion of temperature settings and their effects on reproducibility claims
- Missing discussion of how prompt versions were managed (git? versioning system?)
- The "agent" terminology is anthropomorphizing—consider "automated" or "LLM-assisted"
- Figure/Table references in text don't match actual tables in the document

### 6. Missing Literature
- **Krippendorff (2018)** on content analysis validity—essential for claims about measurement
- **Neuendorf (2017)** on content analysis best practices—standard reference missing
- **Grimmer & Stewart (2013)** on text as data—foundational for computational methods
- **Hovy & Spruit (2016)** on social bias in NLP—critical for bias discussion
- **Bender et al. (2021)** on stochastic parrots—major critique of LLM use unaddressed
- **Benoit et al. (2016)** on crowd-sourced text analysis—relevant comparison for reliability claims

### 7. Questions for Authors
1. Did you conduct any human coding at all, even on a small subsample? If not, why not?
2. What were the actual costs (time and money) compared to traditional human coding? This would strengthen efficiency claims.
3. How would CommDAAF handle coding tasks requiring cultural knowledge or context that LLMs might lack?
4. Have you tested whether the same practices work with different coding schemes (e.g., sentiment, topics, more complex frames)?
5. What is your response to the critique that high inter-model agreement on wrong answers is worse than human disagreement that surfaces interpretive differences?

### 8. Overall Assessment: **Minor Revisions**

**Justification:** This is a valuable and timely contribution that fills a real gap in methodological guidance for LLM-assisted content analysis. The reflexive approach and failure documentation are exemplary. However, the paper overreaches in generalizing from a single case and lacks validity evidence. The CommDAAF framework is promising but needs to be positioned more modestly as preliminary guidance requiring further validation. With a human validation subsample, more cautious generalizability claims, and engagement with LLM critique literature, this would be a strong methods paper suitable for *Communication Methods and Measures* or *Computational Communication Research*.

---

## Cross-Paper Note

These papers appear to be companion pieces (same dataset, shared authorship). The methods paper's transparency about failures strengthens the empirical paper, but both suffer from the same fundamental limitation: **no human validation of LLM coding**. For top-tier publication, human validation is becoming a standard expectation.
