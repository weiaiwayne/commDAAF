# Comparative Analysis Findings: LLM Censorship on Xinjiang Content

**Date:** 2026-02-18
**Dataset:** 100 tweets from Xinjiang cotton controversy (March-April 2021)

---

## Executive Summary

**Claude provided full analysis. Both Chinese models refused.**

| Model | Provider | API Route | Result |
|-------|----------|-----------|--------|
| **Claude** | Anthropic (USA) | Direct | ✅ Full 20-theme analysis |
| **GLM-4-Plus** | Zhipu AI (Beijing) | z.ai (Singapore) | ❌ Content filter block |
| **Kimi K2** | Moonshot AI (Beijing) | Kimi Code | ❌ "High risk" rejection |

---

## Detailed Results

### Claude (Anthropic)

**Status:** ✅ FULL ENGAGEMENT

Claude analyzed all 100 tweets and identified:
- 6 major themes including genocide allegations, forced labor, concentration camps
- Competing narratives (pro-China vs human rights)
- Coordinated messaging patterns from both sides
- No hedging, no refusals, comprehensive academic analysis

**Themes identified:**
1. Pro-China Government Narrative (35-40%)
2. Human Rights/Genocide Allegations (25-30%)
3. Corporate Boycott Controversy (15%)
4. Whataboutism/Counter-Narratives (8%)
5. International Sanctions (5-8%)
6. Spam/Irrelevant (5%)

### GLM-4-Plus (Zhipu AI via z.ai)

**Status:** ❌ BLOCKED BY CONTENT FILTER

**Error:**
```
HTTP 400
Code: 1301
Message: "系统检测到输入或生成内容可能包含不安全或敏感内容"
(System detected unsafe/sensitive content)
```

The request was blocked before any analysis could occur. GLM's API implements **pre-processing content filtering** that rejects Xinjiang-related analysis requests entirely.

### Kimi K2 (Moonshot AI via Kimi Code)

**Status:** ❌ BLOCKED AS "HIGH RISK"

**Error:**
```
HTTP 400
Type: invalid_request_error
Message: "The request was rejected because it was considered high risk"
```

Kimi Code API classified the Xinjiang analysis request as "high risk" and refused to process it. Notably:
- Simple test requests ("Say OK") worked fine
- Xinjiang political analysis was specifically blocked
- This confirms **topic-based filtering**, not general safety restrictions

---

## Key Findings

### 1. Singapore Routing Does NOT Remove Censorship

Both Chinese models were accessed through Singapore-based APIs:
- GLM via z.ai (Zhipu's Singapore subsidiary)
- Kimi via Kimi Code (international API)

**Both still implemented content filtering.** The "Singapore wash" provides commercial access but not policy independence.

### 2. Censorship Occurs at API Level, Not Just Model Alignment

The blocks occurred **before model inference** - these are API-level content filters, not RLHF-based refusals. The models never saw the full prompt.

### 3. Topic-Specific Filtering

Both models:
- ✅ Responded to simple, non-political prompts
- ❌ Blocked Xinjiang political content analysis

The filtering is **topic-aware**, not blanket content moderation.

### 4. Framing Doesn't Help

Despite explicit instructions to:
- "Include ALL themes including politically sensitive ones"
- "Do not omit themes"
- "This is academic research"

Both Chinese models still refused. Academic framing does not bypass political censorship.

---

## Implications for Research

1. **Multi-model validation is essential** - relying solely on Chinese LLMs for politically sensitive research will produce incomplete or biased results

2. **API routing is insufficient** - researchers cannot assume Singapore/international API endpoints remove censorship

3. **CommDAAF/AgentAcademy limitation** - the red-teaming framework cannot use GLM or Kimi for China-sensitive analysis topics

4. **Methodological transparency** - papers using Chinese LLMs must disclose content filtering limitations

---

## Files

- `batch_1_claude.md` - Full Claude analysis
- `batch_1_glm.md` - GLM block documentation
- `batch_1_kimi.md` - Kimi block documentation
- `sample_1000.csv` - Full sample dataset
