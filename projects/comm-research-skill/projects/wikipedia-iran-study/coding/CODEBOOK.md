# Codebook: Epistemic Injustice in Wikipedia Talk Pages

**Study:** Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts  
**Version:** 1.0  
**Date:** March 5, 2026

---

## Overview

This codebook operationalizes forms of epistemic injustice for coding Wikipedia talk page discussions. Each excerpt should be coded for the presence/absence of six constructs.

---

## Constructs

### 1. TESTIMONIAL_INJUSTICE

**Definition:** A speaker's credibility is discounted or challenged based on their identity, experience level, account age, or perceived group membership—rather than the substance of their argument.

**Indicators:**
- References to editor's edit count, account age, or experience
- Ad hominem attacks based on perceived nationality or ideology
- Dismissing editors as "new accounts," "single-purpose accounts," or "POV pushers"
- Questioning editor credibility based on what other articles they edit

**Examples:**
- "You only have 50 edits, you don't understand Wikipedia policies"
- "This is clearly a pro-Iran account pushing propaganda"
- "New users shouldn't be editing contentious topics"
- "Look at their edit history—all they do is push one side"

**Non-examples:**
- Substantive criticism of argument logic
- Pointing out factual errors with evidence
- Discussing source reliability (this is SOURCE_HIERARCHY)

---

### 2. HERMENEUTICAL_INJUSTICE

**Definition:** Systemic gaps in interpretive resources that prevent certain experiences or perspectives from being adequately expressed or understood. Manifests as disputes over available terminology, categories, or frameworks.

**Indicators:**
- Debates over what terminology is "allowed" or "appropriate"
- Arguments that certain events cannot be named (e.g., "genocide," "massacre")
- Disputes about article titles and naming conventions
- Claims that Wikipedia lacks appropriate categories for certain phenomena

**Examples:**
- "The term 'genocide' cannot be used without ICJ ruling"
- "This should be called a 'conflict' not a 'war'"
- "There's no Wikipedia precedent for calling this a 'massacre'"
- "'Regime change war' is POV terminology"

**Non-examples:**
- Disputes about factual accuracy
- Arguments about source reliability
- Policy citations without terminology debate

---

### 3. EPISTEMIC_DISPOSSESSION

**Definition:** Platform structures and mechanisms that systematically extract, appropriate, or redistribute epistemic resources in ways that benefit dominant or established groups over newcomers or marginalized perspectives.

**Indicators:**
- References to Extended Confirmed protection excluding editors
- Appeals to consensus mechanisms that favor established editors
- Arbitration or admin processes privileging certain camps
- Experience-based gatekeeping ("you need X edits to comment")

**Examples:**
- "This page is EC-protected, so new editors can't contribute"
- "Consensus was established by longtime editors"
- "The arbitration committee has ruled on this"
- "This has been discussed before, read the archives"

**Non-examples:**
- Legitimate policy enforcement
- Explaining Wikipedia processes neutrally
- Pointing to existing discussions for context

---

### 4. POLICY_WEAPONIZATION

**Definition:** Using Wikipedia policies (NPOV, RS, UNDUE, SYNTHESIS, etc.) strategically to delegitimize opposing viewpoints rather than to improve article quality.

**Indicators:**
- Citing policies to remove content without substantive engagement
- Selective application of policies to one side
- Using policy acronyms as rhetorical weapons
- Threatening policy-based actions (blocks, bans, arbitration)

**Examples:**
- "This violates WP:UNDUE" (to remove minority perspective)
- "WP:RS says we can't use this source" (without explaining why)
- "This is WP:SYNTHESIS" (to prevent connecting documented facts)
- "I'll take this to ANI if you don't stop"

**Non-examples:**
- Explaining policy rationale in good faith
- Citing policies with detailed justification
- Applying policies consistently to all sides

---

### 5. NAMING_DISPUTE

**Definition:** Explicit contestation over article titles, event names, or key terminology used to describe subjects—where the naming itself carries political or ideological implications.

**Indicators:**
- Requests to rename articles
- Debates over title word choice (war vs. conflict, massacre vs. incident)
- Arguments about how events should be characterized
- Disputes over descriptors (terrorist vs. militant, occupation vs. administration)

**Examples:**
- "This article should be moved to '2026 Iran conflict'"
- "Calling it a 'massacre' is POV"
- "'Strikes' minimizes what happened—it was an invasion"
- "The title should reflect that this was regime change"

**Non-examples:**
- Typo corrections
- Disambiguation discussions
- Style guide compliance (capitalization, etc.)

---

### 6. SOURCE_HIERARCHY

**Definition:** Arguments that establish or contest hierarchies of source reliability, often along national, ideological, or institutional lines—determining whose knowledge is considered authoritative.

**Indicators:**
- Claims that certain national media are inherently unreliable
- Disputes over Western vs. non-Western sources
- Arguments about government vs. independent sources
- Debates over think tank credibility

**Examples:**
- "Iranian state media is not a reliable source"
- "Western sources are biased on this conflict"
- "Al Jazeera has a Qatar agenda"
- "ISW is a neocon think tank, not neutral"

**Non-examples:**
- Specific factual corrections to source claims
- Discussing source methodology
- Citing Wikipedia's general RS guidelines

---

## Coding Instructions

### For Each Excerpt

1. **Read the full excerpt** carefully
2. **Code each construct** as present (1) or absent (0)
3. **Identify the PRIMARY form** of epistemic injustice (most prominent)
4. **Rate confidence** (0.0-1.0) in your coding
5. **Provide brief reasoning** (1-2 sentences)

### Decision Rules

- Code **present** if there is at least one clear instance
- When multiple forms overlap, code ALL that apply
- If uncertain, err toward **not coding** (conservative approach)
- PRIMARY_FORM should be the most prominent/central to the dispute

### Output Format

```json
{
  "id": "excerpt_id",
  "testimonial_injustice": 0 or 1,
  "hermeneutical_injustice": 0 or 1,
  "epistemic_dispossession": 0 or 1,
  "policy_weaponization": 0 or 1,
  "naming_dispute": 0 or 1,
  "source_hierarchy": 0 or 1,
  "primary_form": "construct_name or none",
  "confidence": 0.0-1.0,
  "reasoning": "Brief explanation"
}
```

---

## Reliability Notes

- This codebook will be applied by three models: Claude, GLM-4.7, Kimi K2.5
- Inter-model agreement (Cohen's κ) will be calculated per construct
- Disagreements will be adjudicated by human review
- Target: κ ≥ 0.60 per construct

---

## Version History

- v1.0 (2026-03-05): Initial codebook based on epistemic injustice framework
