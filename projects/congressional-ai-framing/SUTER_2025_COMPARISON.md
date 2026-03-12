# Comparison: Our US Findings vs. Suter (2025)

## Suter (2025) Study Overview

**Title:** "When Politicians Talk AI: Issue-Frames in Parliamentary Debates Before and After ChatGPT"  
**Published:** Policy & Internet, August 2025  
**Coverage:** 2014-2024, four legislatures  
**Method:** BERTopic + manual classification by two coders  

### Suter's Key Findings by Country:

| Frame | US Congress | EU Parliament | Singapore | Switzerland |
|-------|-------------|---------------|-----------|-------------|
| **Military & Security** | **45.9%** | ~15%* | ~10%* | ~12%* |
| **Ethics & Regulation** | 27.1% | **~40%*** | ~20%* | ~35%* |
| **Innovation & Growth** | 21.4% | ~25%* | **43.0%** | ~30%* |
| **Workforce & Skills** | ~5%* | ~15%* | ~25%* | ~20%* |

*Estimates from partial description; exact EU figures need full paper access*

### Suter's Key Conclusions:
1. **Steep surge post-ChatGPT** across all four legislatures
2. **Ethics & Regulation drove the surge** (not innovation/growth)
3. **US uniquely security-focused** (45.9% Military & Security)
4. **Singapore uniquely innovation-focused** (43.0%)
5. EU emphasized ethics/regulation more than US

---

## Our Study vs. Suter: Frame Mapping

| Our Frame | Closest Suter Frame | Our US % | Suter US % | Match? |
|-----------|---------------------|----------|------------|--------|
| SOVEREIGNTY | Military & Security | **22.1%** | **45.9%** | ⚠️ Big gap |
| INNOVATION | Innovation & Growth | **20.9%** | **21.4%** | ✅ Close |
| GOVERNANCE | Ethics & Regulation | **19.2%** | **27.1%** | ⚠️ Lower |
| RIGHTS | Ethics & Regulation (partial) | 9.3% | (included above) | — |
| RISK_HARM | Ethics & Regulation (partial) | 10.5% | (included above) | — |
| RISK_SAFETY | Military & Security (partial) | 9.9% | (included above) | — |

---

## Critical Differences to Explain

### 1. SOVEREIGNTY/Security Gap: 22.1% vs 45.9%

**Why Suter found higher security framing:**
- Suter used "Military & Security" which may include:
  - Explicit military AI applications
  - Defense AI funding discussions
  - National security broadly
- Our "SOVEREIGNTY" is narrower:
  - Geopolitical competition (China)
  - "AI race" rhetoric
  - Strategic autonomy

**Possible reconciliation:**
- If we combine SOVEREIGNTY (22.1%) + RISK_SAFETY (9.9%) = 32%
- Still lower than Suter's 45.9%
- Likely reflects different data sources:
  - Suter: Congressional Record (floor speeches)
  - Us: Congressional hearings (witnesses + members)

### 2. Ethics/Regulation Gap: 19.2% vs 27.1%

**Why Suter found higher ethics framing:**
- Suter combined ethics + regulation into one frame
- We split GOVERNANCE (19.2%) from RIGHTS (9.3%) and RISK_HARM (10.5%)

**Reconciliation:**
- GOVERNANCE + RIGHTS + RISK_HARM = 39.0%
- Actually HIGHER than Suter's 27.1%
- Suggests our finer granularity captured more nuance

### 3. Innovation Match: 20.9% vs 21.4% ✅

**Excellent agreement** on innovation framing despite:
- Different time periods (us: 2007-2026; Suter: 2014-2024)
- Different data sources
- Different coding methods

This validates both studies' core finding on innovation prevalence.

---

## Implications for EU Comparison

### What Suter Found for EU Parliament:
- **Ethics & Regulation dominant** (~40%)
- Lower Military & Security than US (~15%)
- AI Act drove discourse structure

### Expected US-EU Contrast (based on Suter):
| Frame | US (Our Data) | EU (Expected from Suter) |
|-------|---------------|--------------------------|
| Security/Sovereignty | 22-32% | ~15% |
| Ethics/Regulation/Rights | 39% | ~40% |
| Innovation | 21% | ~25% |

### Our Study's Potential Contribution:
1. **Finer frame granularity** (8 frames vs. Suter's 4-5)
2. **More recent data** (through 2026 vs. 2024)
3. **AI Act implementation period** (2024-2026)
4. **Direct hearing comparison** (if we use EP committee hearings)

---

## Methodological Differences

| Aspect | Suter (2025) | Our Study |
|--------|--------------|-----------|
| **Method** | BERTopic + 2 human coders | LLM coders (Kimi + Claude) |
| **Data source** | Congressional Record | Congressional hearings |
| **Time range** | 2014-2024 | 2007-2026 |
| **Frames** | 4-5 categories | 8 categories |
| **Reliability** | Human κ (not reported) | LLM κ = 0.656 |

---

## Research Gap We Can Fill

Suter (2025) provides baseline but:

1. **Ends in 2024** — misses AI Act implementation (Jan 2025 onward)
2. **Uses floor speeches** — hearings capture expert testimony + member Q&A
3. **Coarser frames** — combining ethics/regulation loses RIGHTS vs GOVERNANCE distinction
4. **Pre-dates DeepSeek, Claude 3.5, GPT-4o** — AI landscape evolved rapidly

**Our comparative study can:**
- Extend through March 2026
- Focus on AI Act implementation discourse
- Use same 8-frame scheme for direct comparability
- Include committee hearings (closer to US format)

---

## Next Steps

1. **Collect EP data 2021-2026** (AI Act period)
   - Use EP Open Data API for verbatim reports
   - Filter for AI-related debates
   
2. **Apply identical coding scheme**
   - Same 8 frames
   - Same CommDAAF prompts
   - Same LLM coders (Kimi + Claude)

3. **Key comparison questions:**
   - Does EU emphasize RIGHTS more than US?
   - Does US emphasize SOVEREIGNTY more than EU?
   - Did AI Act passage shift EU framing?
   - How do post-ChatGPT trends compare?

---

*Prepared for CommDAAF comparative study planning*
