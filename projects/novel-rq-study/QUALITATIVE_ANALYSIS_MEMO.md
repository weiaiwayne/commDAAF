# Qualitative Discourse Analysis: Model Disagreement Patterns

**Date:** 2026-03-04  
**Study:** Ukraine Cross-Context Analysis  
**Models Compared:** Claude (heuristic) vs Kimi (LLM)

---

## Executive Summary

Inter-model agreement is **55.2%** — below acceptable thresholds (κ≥0.7). Qualitative analysis of disagreement cases reveals systematic patterns that inform codebook revision.

---

## Quantitative Overview

| Metric | Value |
|--------|-------|
| Total posts compared | 339 |
| Agreements | 187 (55.2%) |
| Disagreements | 152 (44.8%) |

### Frame-Specific Agreement (Claude as reference)

| Frame | Agreement | Status |
|-------|-----------|--------|
| INFORMATIONAL | 72.9% | ✅ Acceptable |
| CONFLICT | 46.2% | ⚠️ Poor |
| INJUSTICE | 38.6% | ⚠️ Poor |
| CALL_TO_ACTION | 33.3% | ❌ Unacceptable |
| SOLIDARITY | 26.7% | ❌ Unacceptable |
| HOPE | 17.4% | ❌ Unacceptable |
| HUMANITARIAN | 16.7% | ❌ Unacceptable |

### Top Disagreement Flows

| Claude → | Kimi | Count |
|----------|------|-------|
| INFORMATIONAL | CONFLICT | 16 |
| SOLIDARITY | INFORMATIONAL | 13 |
| INJUSTICE | INFORMATIONAL | 12 |
| INFORMATIONAL | HOPE | 10 |
| HOPE | SOLIDARITY | 9 |

---

## Qualitative Patterns Identified

### Pattern 1: Form vs Content Coding

**Observation:** Claude's keyword heuristic reads STRUCTURAL features (news format, hashtags, links) and defaults to INFORMATIONAL. Kimi's LLM approach reads SEMANTIC content and codes by topic.

**Evidence:**

> Post: "ℹ️ The #BlackSeaFleet of the Russian Navy in full force left the ports and headed towards #Odessa..."
> - Claude: INFORMATIONAL (news format, ℹ️ emoji, hashtags)
> - Kimi: CONFLICT (military fleet heading to attack)

**Theoretical Implication:** The same message can be simultaneously informational (in form) and conflictual (in content). This reflects the inherent multi-layered nature of war discourse.

**Codebook Fix:** 
> **RULE 8.1:** Code PRIMARY CONTENT, not presentation format. If a news report describes military action, code as CONFLICT, not INFORMATIONAL. INFORMATIONAL is reserved for meta-level content (e.g., polling updates, procedural information).

---

### Pattern 2: SOLIDARITY vs HOPE Boundary Blur

**Observation:** Both frames involve positive affect about support/resilience. The distinction is conceptually unclear in operational terms.

**Evidence:**

> Post: "Today @ScaniaGroup opens a brand new facility near @Kyiv. Scania trucks will help #Ukraine rebuild what #Russia destroys. Nothing can break the resilience of Ukrainians."
> - Claude: HOPE (resilience, rebuilding, future-oriented)
> - Kimi: SOLIDARITY (international company standing with Ukraine)

**Theoretical Implication:** Hope and solidarity are intertwined in resistance discourse. Messages of international support simultaneously signal hope for the future and solidarity with victims.

**Codebook Fix:**
> **RULE 8.2:** HOPE = Future-oriented optimism (victory, rebuilding, "things will get better")
> **RULE 8.3:** SOLIDARITY = Actor-oriented unity (who is standing with whom, collective identity)
> If both apply, prioritize SOLIDARITY when an external actor is named; prioritize HOPE when the message emphasizes temporal trajectory.

---

### Pattern 3: Irony/Sarcasm Detection Failure

**Observation:** Claude's keyword heuristic misses evaluative framing conveyed through irony, sarcasm, or visual juxtaposition.

**Evidence:**

> Post: "📸Photo of the Day📸 🇷🇺🇮🇷 #Russia worships its true master."
> - Claude: INFORMATIONAL (photo post, neutral format)
> - Kimi: INJUSTICE (sarcastic criticism of Russia-Iran relationship)

**Theoretical Implication:** Political discourse frequently employs irony as a rhetorical strategy. Surface-level keyword analysis systematically misses these cases.

**Codebook Fix:**
> **RULE 8.4 (Irony Detection):** Flag posts with:
> - Quotation marks around evaluative terms
> - Emojis incongruent with literal content
> - Hyperbolic language ("true master", "brilliant strategy")
> - Visual juxtaposition (flag emojis indicating comparison)
> When irony detected, code based on INTENDED meaning, not literal surface.

---

### Pattern 4: News-About-X Problem

**Observation:** A news report ABOUT a call to action is itself functioning as a call to action (by amplifying the message). Similarly, news about conflict IS conflict content.

**Evidence:**

> Post: "Zelenskyy urged Ukraine's allies to accelerate the shipment of heavy weapons to match Russia on the battlefield. #ArmUkraineNow"
> - Claude: CONFLICT (battlefield context)
> - Kimi: CALL_TO_ACTION (Zelenskyy's urging + activist hashtag)

**Theoretical Implication:** In social media, reporting on directives often functions as endorsement/amplification. The hashtag #ArmUkraineNow suggests the poster is joining the call, not neutrally reporting it.

**Codebook Fix:**
> **RULE 8.5:** If the PRIMARY message is directive (do X, donate, share, act now), code as CALL_TO_ACTION regardless of who issues the directive. Reporting on a call to action with endorsing hashtags = CALL_TO_ACTION.

---

### Pattern 5: Humanitarian Impact as Frame Boundary

**Observation:** HUMANITARIAN is poorly distinguished from INFORMATIONAL and INJUSTICE. Economic impacts, civilian suffering, and factual reports about casualties all blur together.

**Evidence:**

> Post: "Annual harvest has declined by almost half according to some estimates"
> - Claude: INFORMATIONAL (factual report)
> - Kimi: HUMANITARIAN (economic/food security impact)

**Theoretical Implication:** The HUMANITARIAN frame requires explicit victim focus. Economic statistics alone may not activate the humanitarian frame unless human suffering is foregrounded.

**Codebook Fix:**
> **RULE 8.6:** HUMANITARIAN requires explicit reference to civilian victims, refugees, or direct human suffering. Economic/infrastructure reports without victim focus = INFORMATIONAL.

---

## Proposed Qualitative Research Questions

Based on the disagreement analysis, the following qualitative RQs emerge:

### RQ1: Rhetorical Construction of Enemy
*How do users linguistically construct "the enemy" in war discourse (Russia) vs protest discourse (Iranian regime)?*
- Method: Critical Discourse Analysis (CDA)
- Focus: Dehumanization, moral framing, us/them boundaries, naming practices

### RQ2: Solidarity Performance
*What discursive strategies do diaspora users employ to perform solidarity with victims they cannot physically help?*
- Method: Thematic analysis of SOLIDARITY-coded posts
- Focus: Witnessing, amplification, identity claims, emotional labor

### RQ3: Frame Hybridization
*How do users blend frames (e.g., INJUSTICE + HOPE) and what does this reveal about emotional regulation in crisis discourse?*
- Method: Sequential analysis of multi-frame posts
- Focus: Emotional arcs, coping strategies, narrative structure

### RQ4: Silence & Absence
*What is NOT said? What frames are conspicuously absent in each context?*
- Method: Negative case analysis
- Compare: Low HOPE in Ukraine (realistic pessimism?) vs low CONFLICT in #MahsaAmini (civilian protest framing?)

### RQ5: Irony as Resistance
*How does ironic/sarcastic framing function in political resistance discourse across cultural contexts?*
- Method: Discourse analysis of irony-flagged posts
- Focus: Target of irony, in-group signaling, emotional distancing

---

## Codebook Revision Summary

| Rule | Description |
|------|-------------|
| 8.1 | Code primary CONTENT, not presentation format |
| 8.2 | HOPE = future-oriented optimism |
| 8.3 | SOLIDARITY = actor-oriented unity |
| 8.4 | Irony detection: quote marks, incongruent emojis, hyperbole |
| 8.5 | Directive message + endorsing hashtag = CALL_TO_ACTION |
| 8.6 | HUMANITARIAN requires explicit victim reference |

---

## Implications for CommDAAF

1. **Multi-method coding** — Single-method (keyword OR LLM) produces systematic bias. Hybrid approaches needed.

2. **Disagreement-as-data** — Model disagreements aren't failures; they're signals of genuine frame ambiguity worth qualitative investigation.

3. **Context-specific calibration** — Frame definitions developed for protest discourse may not transfer cleanly to war discourse. Cross-context studies require codebook adaptation.

4. **Mandatory qualitative phase** — Before publication, pull disagreement cases and do discourse analysis. This catches systematic biases that aggregate reliability metrics miss.

---

*Analysis conducted: 2026-03-04*
*Analyst: Claude (main session)*
*Source files: ukraine_codings_claude.json, ukraine_codings_kimi.json, DISAGREEMENT_SAMPLE.json*
