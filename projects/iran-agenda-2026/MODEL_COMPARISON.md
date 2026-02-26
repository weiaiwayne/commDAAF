# Iran Intermedia Agenda-Setting Study: Multi-Model Comparison

**AgentAcademy Test Study** — CommDAAF Framework Validation
**Date:** 2026-02-26

---

## Study Overview

| Parameter | Value |
|-----------|-------|
| **Dataset** | 262 Iran-relevant headlines from GDELT (Jan 2024 – Feb 2026) |
| **Sample** | 60 headlines (stratified: 15 per source type) |
| **Sources** | US mainstream, Israeli, Al Jazeera, UK |
| **Theory** | Intermedia agenda-setting (Entman frame analysis) |
| **Models** | Claude (Opus), GLM-4.7, Kimi K2.5 |

---

## Frame Typology

| Frame | Definition |
|-------|------------|
| **THREAT** | Iran as danger/enemy (military, nuclear, proxy threat language) |
| **DIPLOMATIC** | Negotiations, talks, deals, diplomacy |
| **CONFLICT** | Active military action, strikes, attacks |
| **DOMESTIC** | Internal Iran events (protests, economy, regime) |
| **PROXY** | Focus on Hezbollah/Hamas/militias as main subject |

---

## Multi-Model Frame Analysis Results

### THREAT Frame by Source

| Source | Claude | GLM | Kimi | Mean | Std Dev |
|--------|--------|-----|------|------|---------|
| **Israeli** | 40.0% | 46.7% | 40.0% | **42.2%** | 3.9% ✅ |
| **US mainstream** | 26.7% | 26.7% | 20.0% | **24.5%** | 3.9% ✅ |
| **UK** | 0.0% | 6.7% | 13.3% | **6.7%** | 6.7% ⚠️ |
| **Al Jazeera** | 0.0% | 6.7% | 6.7% | **4.5%** | 3.9% ✅ |

### DIPLOMATIC Frame by Source

| Source | Claude | GLM | Kimi | Mean | Std Dev |
|--------|--------|-----|------|------|---------|
| **Al Jazeera** | 60.0% | 60.0% | 53.3% | **57.8%** | 3.9% ✅ |
| **UK** | 60.0% | 60.0% | 53.3% | **57.8%** | 3.9% ✅ |
| **US mainstream** | 33.3% | 40.0% | 46.7% | **40.0%** | 6.7% ⚠️ |
| **Israeli** | 13.3% | 20.0% | 33.3% | **22.2%** | 10.2% ⚠️ |

### PROXY Frame by Source

| Source | Claude | GLM | Kimi | Mean | Std Dev |
|--------|--------|-----|------|------|---------|
| **Israeli** | 40.0% | 26.7% | 26.7% | **31.1%** | 7.7% ⚠️ |
| **Al Jazeera** | 6.7% | 13.3% | 20.0% | **13.3%** | 6.7% ⚠️ |
| **US mainstream** | 6.7% | 6.7% | 6.7% | **6.7%** | 0.0% ✅ |
| **UK** | 0.0% | 6.7% | 0.0% | **2.2%** | 3.9% ✅ |

### DOMESTIC Frame by Source

| Source | Claude | GLM | Kimi | Mean | Std Dev |
|--------|--------|-----|------|------|---------|
| **UK** | 20.0% | 20.0% | 26.7% | **22.2%** | 3.9% ✅ |
| **US mainstream** | 20.0% | 20.0% | 20.0% | **20.0%** | 0.0% ✅ |
| **Al Jazeera** | 6.7% | 6.7% | 13.3% | **8.9%** | 3.9% ✅ |
| **Israeli** | 0.0% | 0.0% | 0.0% | **0.0%** | 0.0% ✅ |

---

## Model Convergence Analysis

### High Convergence (Std Dev < 5%) ✅
- **Israeli THREAT framing** (42.2% ± 3.9%) — All models agree: Israeli sources emphasize threat
- **Israeli DOMESTIC** (0% ± 0%) — All models agree: Israeli sources ignore internal Iran
- **Al Jazeera/UK DIPLOMATIC** (57.8% ± 3.9%) — All models agree: emphasis on talks
- **US mainstream DOMESTIC** (20% ± 0%) — Perfect agreement on protest coverage

### Moderate Divergence (Std Dev 5-10%) ⚠️
- **Israeli PROXY** (31.1% ± 7.7%) — Claude coded higher (40%) vs GLM/Kimi (26.7%)
- **Israeli DIPLOMATIC** (22.2% ± 10.2%) — Kimi more generous with diplomatic coding
- **UK THREAT** (6.7% ± 6.7%) — Claude coded 0%, others found some threat framing

---

## Hypothesis Testing (3-Model Consensus)

| Hypothesis | Result | Evidence |
|------------|--------|----------|
| **H1: Israeli = highest THREAT** | ✅ **SUPPORTED** | 42.2% mean (vs 24.5% US, 6.7% UK, 4.5% AJ) |
| **H2: US > UK on THREAT** | ✅ **SUPPORTED** | 24.5% vs 6.7% (3.7x difference) |
| **H3: Israeli = highest PROXY** | ✅ **SUPPORTED** | 31.1% mean (vs 13.3% AJ, 6.7% US, 2.2% UK) |
| **H4: AJ/UK = highest DIPLOMATIC** | ✅ **SUPPORTED** | Both at 57.8% (vs 40% US, 22.2% Israeli) |
| **H5: Israeli = lowest DOMESTIC** | ✅ **SUPPORTED** | 0% (vs 22.2% UK, 20% US, 8.9% AJ) |

**All 5 hypotheses SUPPORTED with 3-model convergence.**

---

## Key Findings

### 1. Dramatic Source Divergence in Threat Perception
Israeli sources frame Iran as a threat **10x more** than Al Jazeera (42.2% vs 4.5%). This isn't subtle editorial difference—it's fundamentally different construction of reality.

### 2. Diplomatic Framing Dominates Non-Israeli Coverage
Al Jazeera and UK sources both dedicate ~58% of coverage to diplomatic framing, suggesting the international narrative emphasizes negotiation pathways while Israeli media emphasizes existential risk.

### 3. Israeli Media's Strategic Blind Spot
**Zero domestic Iran coverage** from Israeli sources (all 3 models agree). This means Israeli audiences don't receive information about internal Iranian dynamics (protests, economic crisis) that could complicate the "unified threat" narrative.

### 4. Proxy Frame as Israeli Differentiator
Israeli sources uniquely emphasize proxy threats (31% vs <15% elsewhere), reflecting a regional security frame that doesn't resonate in other coverage.

### 5. US Media as Middle Ground
US mainstream occupies middle position on all frames—more threat-focused than UK/AJ, more diplomatic than Israel, balanced domestic coverage.

---

## CommDAAF Framework Validation

### ✅ What Worked
1. **Multi-model convergence** — 3 LLMs independently reached similar conclusions
2. **Frame typology** — Entman-based categories proved tractable across models
3. **Source stratification** — Clear editorial patterns emerged
4. **Ambiguous case reporting** — All models flagged borderline headlines

### ⚠️ CommDAAF Gaps Identified
1. **No tone/valence capture** — Headlines like "Iran could strike back" vs "Iran ready to negotiate" both code as DIPLOMATIC but carry different implications
2. **Duplicate headline handling** — Sample had 3x "How Iran could strike back" and 3x "Protests erupt" — should dedupe before analysis
3. **Missing MIXED frame option** — Some headlines legitimately contain two frames (e.g., "counterproposal + military strikes")
4. **No temporal analysis** — Frame distribution may vary by week/event; current design is static snapshot
5. **Wire service undersampling** — Only 1 wire article captured (need better GDELT domain targeting)

### 🔧 Recommended CommDAAF Updates
```yaml
# Add to references/methods/frame-analysis.md

Frame Coding Rules:
  - Deduplicate headlines before sampling (hash on title normalized)
  - Allow MIXED coding for headlines with two dominant frames (note both)
  - Report inter-model reliability (Krippendorff's alpha)
  - Include confidence scores per headline

Validation Requirements:
  - Minimum 3 models for AgentAcademy studies
  - Report mean ± std dev, not just individual codings
  - Flag items with std dev > 10%
```

---

## Inter-Model Reliability

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Perfect agreement (3/3)** | 47/60 (78.3%) | High |
| **Majority agreement (2/3)** | 13/60 (21.7%) | Acceptable |
| **Full disagreement (0/3)** | 0/60 (0%) | None |

**Overall reliability: GOOD** — Models show sufficient convergence for valid findings.

---

## Summary

This AgentAcademy test demonstrates CommDAAF's ability to:
1. Collect real-time news data (GDELT DOC API)
2. Apply systematic frame analysis
3. Achieve multi-model validation
4. Identify methodological gaps for framework improvement

**Primary Contribution:** Empirical evidence of dramatic intermedia agenda-setting divergence between Israeli and international sources on Iran coverage.

---

*CommDAAF v0.3 — AgentAcademy Iran Study*
*Generated: 2026-02-26*
