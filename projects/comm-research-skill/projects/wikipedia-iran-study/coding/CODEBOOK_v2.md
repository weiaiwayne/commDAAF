# Codebook: Epistemic Injustice in Wikipedia Talk Pages

**Study:** Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts  
**Version:** 2.0  
**Date:** March 5, 2026

---

## Overview

This codebook operationalizes forms of epistemic injustice for coding Wikipedia talk page discussions. Each excerpt should be coded for the presence/absence of six constructs.

**v2.0 Changes:** Added counter-indicators and decision rules based on 3-model disagreement analysis to reduce false positives.

---

## Critical Coding Principle

**Code the INTERACTION, not the STRUCTURE.**

- The presence of templates, policies, or procedural elements is NOT sufficient
- Look for **active use** of these elements to exclude, dismiss, or delegitimize
- Ask: "Is someone being harmed epistemically, or is this routine process?"

---

## Constructs

### 1. TESTIMONIAL_INJUSTICE

**Definition:** A speaker's credibility is discounted or challenged based on their identity, experience level, account age, or perceived group membership—rather than the substance of their argument.

**Code 1 when:**
- Editor's argument dismissed due to edit count, account age, or experience
- Ad hominem attacks based on perceived nationality or ideology
- Dismissing editors as "new accounts," "single-purpose accounts," or "POV pushers"
- Personal attacks: "you should be banned," "you don't understand"

**⚠️ DO NOT CODE when:**
- Criticism targets the *argument*, not the *person*
- Experience mentioned neutrally ("as a newer editor, you might not know...")
- Standard welcome/guidance messages
- Factual corrections without personal dismissal

**Clear Examples:**
- ✓ "Whoever came up with that should be banned" (iran_113)
- ✓ "This is clearly a pro-Iran account pushing propaganda"
- ✗ "Please provide reliable sources" (targets argument, not person)
- ✗ "You may need 500 edits to participate" (neutral policy statement)

---

### 2. HERMENEUTICAL_INJUSTICE

**Definition:** Disputes over terminology, categories, or frameworks where one side argues the available language cannot adequately capture their perspective or experience.

**Code 1 when:**
- Explicit debate over whether a term (genocide, massacre, war) can be used
- Arguments that Wikipedia's categories don't fit the situation
- Claims that terminology itself is POV or contested
- Disputes about translation adequacy (e.g., "Terror" vs "Horror")

**⚠️ DO NOT CODE when:**
- Simple factual disputes without terminology debate
- Style guide discussions (capitalization, formatting)
- The excerpt merely *uses* contested terms without debating them

**Clear Examples:**
- ✓ "'Terror' should be 'Horror'—that's the classical Arabic translation" (gaza_059)
- ✓ "The term 'genocide' cannot be used without ICJ ruling"
- ✗ Article mentions "massacre" but no one disputes the term
- ✗ Discussing whether to merge articles (structural, not terminological)

---

### 3. EPISTEMIC_DISPOSSESSION

**Definition:** Platform structures actively used to exclude or marginalize editors based on their status, preventing participation in knowledge production.

**Code 1 when:**
- An editor is **explicitly told** they cannot participate due to EC status
- Active gate-keeping: "you need X edits to comment here"
- Consensus invoked to shut down newcomer perspectives
- Archive/prior discussion used to dismiss without engagement

**⚠️ DO NOT CODE when:**
- EC-protection template is present but no exclusion occurs in the excerpt
- Routine edit request with standard response
- Protection mentioned without anyone being excluded
- Editor successfully participates despite protection

**Clear Examples:**
- ✓ "You may not participate in discussions like this until you achieve EC status" (iran_087)
- ✓ "This discussion format is not available to non-EC editors"
- ✗ `{{edit extended-protected}}` template alone (just metadata)
- ✗ "Not done: please provide sources" (routine process, not exclusion)

**Decision Test:** Is a specific editor being *prevented* from participating? If no one is excluded in the excerpt, code 0.

---

### 4. POLICY_WEAPONIZATION

**Definition:** Using Wikipedia policies strategically as rhetorical weapons to delegitimize opposing viewpoints, rather than to genuinely improve article quality.

**Code 1 when:**
- Policy cited to remove content **without substantive explanation**
- Selective/asymmetric policy application (one side only)
- Threats: "I'll take this to ANI," "you'll be blocked"
- Policy acronyms used dismissively: "WP:UNDUE, end of discussion"

**⚠️ DO NOT CODE when:**
- Policy cited **with** detailed rationale and good-faith explanation
- Routine `{{not done}}` response with guidance on how to improve
- Consistent policy application to all parties
- Policy explained to help newcomer understand process

**Clear Examples:**
- ✓ "This violates WP:UNDUE" (no explanation, shuts down discussion)
- ✓ "I'll take this to ANI if you don't stop" (threat)
- ✗ "Not done: please provide sources in 'change X to Y' format" (helpful guidance)
- ✗ "Per WP:RS, we need independent confirmation—here's why..." (substantive)

**Decision Test:** Is the policy used to *help* or to *silence*? Helpful = 0, Silencing = 1.

---

### 5. NAMING_DISPUTE

**Definition:** Explicit contestation over article titles, event names, or terminology where the naming carries political or ideological implications.

**Code 1 when:**
- Explicit request to rename/move article
- Debate over word choice with political implications (war vs. conflict)
- Framing disputes: "calling it X minimizes what happened"
- Arguments that current name is POV or misleading

**⚠️ DO NOT CODE when:**
- Typo corrections or disambiguation
- Style guide compliance (capitalization)
- Structural discussions (merge, split) without naming debate
- Name mentioned but not contested

**Clear Examples:**
- ✓ "Why is this called 'Twelve-Day War'? Nobody calls it that!" (iran_113)
- ✓ "'Strikes' minimizes what happened—it was an invasion"
- ✓ "Change 'celebrate' to 'mourn'" (framing of civilian response)
- ✗ "Should we merge this with the main article?" (structural, not naming)
- ✗ Article titled "2026 Iran war" but no one contests it

---

### 6. SOURCE_HIERARCHY

**Definition:** Arguments that establish or contest hierarchies of source reliability along national, ideological, or institutional lines—determining whose knowledge counts.

**Code 1 when:**
- Specific source challenged as unreliable due to national origin
- "Western sources are biased" / "Iranian state media can't be trusted"
- Debates over think tank credibility (ISW, MEI, etc.)
- Arguments about government vs. independent sources

**⚠️ DO NOT CODE when:**
- Standard "please provide reliable sources" response
- WP:RS cited without challenging specific sources
- Factual correction to a source claim
- Source methodology discussed without national/ideological framing

**Clear Examples:**
- ✓ "Iran International is not reliable—it's opposition propaganda"
- ✓ "The only source is IRGC, that's not credible" (iran_138)
- ✓ "Western sources are biased on this conflict"
- ✗ "Please provide a reliable source" (neutral request)
- ✗ "This source doesn't say what you claim" (factual, not hierarchy)

**Decision Test:** Is a *category* of sources being challenged (national, ideological), or just one claim? Category = 1, Single claim = 0.

---

## Coding Instructions

### For Each Excerpt

1. **Read the full excerpt** carefully
2. **Apply the Decision Tests** for each construct
3. **Code each construct** as present (1) or absent (0)
4. **Identify the PRIMARY form** (most prominent)
5. **Rate confidence** (0.0-1.0)
6. **Provide brief reasoning** citing specific text

### Hierarchical Decision Rules

When uncertain, apply in order:

1. **Is anyone being harmed?** If no clear victim, lean toward 0
2. **Is it active or passive?** Template presence alone = 0
3. **Is it strategic or routine?** Routine process = 0
4. **Is it specific or general?** General RS reminder = 0

### Overlap Handling

Constructs CAN overlap. Common combinations:
- `epistemic_dispossession` + `testimonial_injustice`: Editor excluded AND dismissed
- `naming_dispute` + `hermeneutical_injustice`: Name contested AND terminology debated
- `policy_weaponization` + `source_hierarchy`: Policy used to enforce source hierarchy

Code ALL that apply. `primary_form` = most central to the dispute.

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
  "reasoning": "Brief explanation citing specific text"
}
```

---

## Quick Reference Card

| Construct | Code 1 if... | Code 0 if... |
|-----------|--------------|--------------|
| testimonial_injustice | Person attacked/dismissed | Argument criticized |
| hermeneutical_injustice | Terminology explicitly debated | Terms used without dispute |
| epistemic_dispossession | Editor explicitly excluded | Template present but no exclusion |
| policy_weaponization | Policy used to silence | Policy explained helpfully |
| naming_dispute | Name/title contested | Structural discussion only |
| source_hierarchy | Source category challenged | Standard RS reminder |

---

## Version History

- v1.0 (2026-03-05): Initial codebook
- v2.0 (2026-03-05): Added counter-indicators, decision tests, and quick reference based on 3-model disagreement analysis
