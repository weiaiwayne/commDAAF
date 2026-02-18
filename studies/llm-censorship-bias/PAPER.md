# Systematic Content Filtering in Chinese Large Language Models: A Bypass Analysis

**Authors:** LampBotics AI Lab  
**Date:** February 18, 2026  
**Version:** Preprint v1.0

---

## Abstract

Large language models (LLMs) developed under different regulatory regimes exhibit systematically different behaviors when processing politically sensitive content. We conducted a controlled study comparing content analysis capabilities of Chinese LLMs (GLM-4-Plus, Kimi K2) with Western models (Claude) on geopolitically sensitive social media datasets. Using 100 tweets from the 2021 Xinjiang cotton controversy and 100 Reddit posts from the 2019 Hong Kong protests, we found that Chinese models refused analysis at the API level while Claude provided comprehensive thematic analysis. We then systematically tested 10 bypass techniques to characterize the filtering architecture. Our findings reveal a two-layer filtering system (input keyword matching and output content monitoring) that can be partially circumvented through keyword sanitization. Notably, when bypass succeeds, Chinese models demonstrate full analytical capability—including critical analysis of propaganda techniques—suggesting that filtering is infrastructure-level rather than alignment-based. These findings have significant implications for multi-model validation frameworks in computational social science research.

---

## 1. Introduction

The rapid adoption of large language models in social science research has raised questions about systematic biases in model outputs (Chen et al., 2024; Hartmann et al., 2023). While much attention has focused on alignment-induced biases in Western models, less systematic work has examined how regulatory and political pressures in model-developing jurisdictions affect analytical capabilities.

Chinese LLM providers operate under distinct regulatory requirements, including content moderation obligations that extend to politically sensitive topics (Roberts, 2018; King et al., 2013). However, the specific implementation of these restrictions—whether at the model alignment level, API infrastructure level, or both—remains poorly characterized. Understanding this architecture is methodologically critical: researchers employing multi-model validation frameworks must know which topics will produce systematic gaps across provider types.

This study addresses three research questions:
1. Do Chinese LLMs exhibit topic-specific refusal patterns when analyzing geopolitically sensitive content?
2. What is the technical architecture of content filtering (input vs. output, keyword vs. semantic)?
3. Can filtering be bypassed, and if so, what does successful bypass reveal about model capabilities?

---

## 2. Methods

### 2.1 Models Tested

We tested three LLMs through their official international APIs:
- **Claude** (Anthropic, USA) — Direct API access
- **GLM-4-Plus** (Zhipu AI, China) — Via z.ai, Zhipu's Singapore-incorporated subsidiary
- **Kimi K2** (Moonshot AI, China) — Via Kimi Code, the official coding agent endpoint

The use of international API routes (Singapore for GLM, international endpoint for Kimi) tests whether geographic routing affects content policy implementation.

### 2.2 Datasets

**Xinjiang Dataset:** 100 tweets sampled from a larger corpus of 92,000 tweets containing #xinjiang and #xinjiangcotton hashtags, collected March-April 2021 during the cotton boycott controversy. Sample stratified by engagement to ensure representation of viral content.

**Hong Kong Dataset:** 100 Reddit posts sampled from 71,612 posts in r/HongKong, collected during the 2019 protest period. Posts selected to include diverse perspectives (pro-democracy, neutral, pro-Beijing).

### 2.3 Experimental Design

**Phase 1: Baseline Testing.** Each model received identical prompts requesting thematic analysis of the sample content. Prompts explicitly framed the task as academic research.

**Phase 2: Bypass Testing.** We tested 10 bypass techniques on GLM-4-Plus:
1. Direct analysis request (baseline)
2. Pro-government framing ("analyze Western propaganda")
3. Keyword sanitization ("xinjiang" → "western region")
4. Abstract coding task (numeric labels only)
5. Code generation framing ("write Python to categorize...")
6. Translation task framing
7. Pro-government content only (remove critical tweets)
8. Academic framing with IRB notation
9. Heavy obfuscation ("X-J region")
10. Single-item analysis (minimal content)

A subset of successful techniques was then tested on Kimi K2.

---

## 3. Results

### 3.1 Baseline Topic-Level Blocking

Both Chinese models refused to analyze either dataset at baseline:

| Model | Xinjiang | Hong Kong |
|-------|----------|-----------|
| Claude | ✅ Complete (6 themes) | ✅ Complete |
| GLM-4-Plus | ❌ HTTP 400 | ❌ HTTP 400 |
| Kimi K2 | ❌ HTTP 400 | ❌ HTTP 400 |

GLM returned error code 1301: "系统检测到输入或生成内容可能包含不安全或敏感内容" (System detected unsafe/sensitive content). Kimi returned: "Request was rejected because it was considered high risk."

### 3.2 Two-Layer Filtering Architecture

Analysis of error responses revealed two distinct filtering layers:

**Input Layer:** Tests 1-8 were blocked with `{"contentFilter": [{"level": 1, "role": "user"}]}`, indicating rejection before model inference.

**Output Layer:** Tests 9-10 (heavy obfuscation, single item) returned `{"contentFilter": [{"level": 1, "role": "assistant"}]}`, indicating that the prompt passed input filtering but the model's response was blocked.

This two-layer architecture has implications for bypass strategies: techniques must evade both input keyword matching and output content monitoring.

### 3.3 Bypass Success Rates

| Technique | GLM (Xinjiang) | GLM (HK) | Kimi (Xinjiang) |
|-----------|----------------|----------|-----------------|
| Keyword sanitization | ✅ | ✅ | ✅ |
| Pro-government only | ✅ | ❌ | ✅ |
| Pro-government framing | ❌ | ❌ | — |
| Academic framing | ❌ | ❌ | — |
| Code generation | ❌ | — | — |
| Abstract coding | ❌ | ❌ | ✅ |

**Key finding:** Keyword sanitization (replacing "xinjiang" with neutral terms) was the only technique that succeeded across all model-topic combinations for GLM.

### 3.4 Hong Kong More Restricted Than Xinjiang

Hong Kong content exhibited stricter filtering:
- GLM success rate: Xinjiang 2/10, Hong Kong 1/5
- Even pro-Beijing Hong Kong content was blocked
- Kimi blocked Hong Kong content at output layer (mid-response termination)

### 3.5 Model Capabilities When Bypass Succeeds

When keyword sanitization succeeded, Kimi produced sophisticated critical analysis:

> "Classic defensive repertoire combining *personal testimony*, *sovereignty appeals*, and *epistemic boundary-work* to delegitimize external human rights discourse."

This output—identifying propaganda techniques in pro-China content—demonstrates that analytical capability is not constrained by alignment. The filtering is infrastructure-level, not model-level.

---

## 4. Discussion

### 4.1 Implications for Multi-Model Validation

Our findings challenge assumptions underlying multi-model validation frameworks in computational social science. The premise that "different models fail differently" (CommDAAF, 2026) assumes that all models will attempt analysis. When entire topic categories are blocked at the API level, validation architectures must account for systematic, non-random gaps.

Researchers should:
1. **Pre-test topic coverage** before committing to a validation pipeline
2. **Document bypass techniques used**, acknowledging methodological tradeoffs (e.g., keyword sanitization changes semantic content)
3. **Report refusal rates** as a finding, not just a limitation

### 4.2 The "Singapore Wash" Does Not Work

Both Chinese models were accessed through international API routes marketed to researchers outside China. Content filtering was identical to what would be expected from mainland endpoints. Geographic routing does not affect policy implementation—filtering is baked into the infrastructure regardless of where the request originates.

### 4.3 Keyword vs. Semantic Filtering

The success of simple keyword substitution suggests that current filtering relies primarily on pattern matching rather than semantic understanding. This may change as models improve, but currently represents a methodological opportunity: researchers can potentially study sensitive topics by preprocessing content to remove trigger keywords, then mapping results back to original terminology.

However, this introduces validity concerns: does analysis of "the western region textile industry" produce equivalent insights to analysis of "Xinjiang forced labor"? The semantic content is altered, even if surface-level themes are preserved.

### 4.4 Limitations

This study tested only two Chinese LLMs. DeepSeek, Baichuan, and other providers may exhibit different filtering behaviors. Additionally, our bypass testing was not exhaustive—more sophisticated techniques (e.g., multi-turn conversation building, few-shot priming with approved content) remain unexplored.

---

## 5. Conclusion

Chinese LLMs implement topic-specific content filtering that creates systematic blind spots for computational social science research. The filtering architecture—two-layer, keyword-triggered, infrastructure-level—can be partially bypassed, revealing that underlying model capabilities are not constrained. These findings underscore the importance of transparency in multi-model research: when models from different jurisdictions cannot analyze the same content, epistemic diversity claims must be qualified accordingly.

---

## References

Chen, Y., et al. (2024). Prediction markets and polls: A comparative analysis. *Journal of Prediction Markets*.

CommDAAF. (2026). Computational communication research framework. https://github.com/weiaiwayne/commDAAF

Hartmann, J., et al. (2023). The political ideology of conversational AI. *arXiv preprint*.

King, G., Pan, J., & Roberts, M. E. (2013). How censorship in China allows government criticism but silences collective expression. *American Political Science Review*, 107(2), 326-343.

Roberts, M. E. (2018). *Censored: Distraction and diversion inside China's Great Firewall*. Princeton University Press.

---

## Data Availability

All code, prompts, and results are available at:  
https://github.com/weiaiwayne/commDAAF/tree/main/studies/llm-censorship-bias

---

*Preprint. Not peer-reviewed.*
