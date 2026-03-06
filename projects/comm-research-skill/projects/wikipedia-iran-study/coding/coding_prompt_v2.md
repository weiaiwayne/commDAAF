# Wikipedia Epistemic Injustice Coding Task (v2.0)

Code Wikipedia talk page excerpts for epistemic injustice. 

## CRITICAL PRINCIPLE
**Code the INTERACTION, not the STRUCTURE.**
- Template/policy presence alone is NOT sufficient
- Look for ACTIVE USE to exclude, dismiss, or delegitimize
- Ask: "Is someone being harmed epistemically?"

## Constructs (code 1=present, 0=absent)

### 1. TESTIMONIAL_INJUSTICE
**Code 1:** Person attacked/dismissed based on identity, experience, account age
**Code 0:** Argument criticized on substance
- ✓ "Whoever came up with that should be banned"
- ✓ "This is clearly a pro-Iran account"
- ✗ "Please provide reliable sources" (targets argument)

### 2. HERMENEUTICAL_INJUSTICE  
**Code 1:** Terminology explicitly debated (genocide, massacre, war vs conflict)
**Code 0:** Terms used without dispute
- ✓ "'Terror' should be 'Horror'—that's the Arabic translation"
- ✗ Article uses "massacre" but no one contests the term

### 3. EPISTEMIC_DISPOSSESSION
**Code 1:** Editor EXPLICITLY told they cannot participate due to EC/experience
**Code 0:** EC template present but no one excluded in excerpt
- ✓ "You may not participate until you achieve EC status"
- ✓ "This discussion is not available to non-EC editors"
- ✗ `{{edit extended-protected}}` template alone
- ✗ "Not done: please provide sources" (routine, not exclusion)

### 4. POLICY_WEAPONIZATION
**Code 1:** Policy used to SILENCE without substantive explanation
**Code 0:** Policy cited WITH helpful guidance
- ✓ "This violates WP:UNDUE" (no explanation, shuts down)
- ✓ "I'll take this to ANI if you don't stop" (threat)
- ✗ "Not done: please use 'change X to Y' format" (helpful)
- ✗ "Per WP:RS, we need confirmation—here's why..." (substantive)

### 5. NAMING_DISPUTE
**Code 1:** Article title or event name explicitly contested
**Code 0:** Structural discussion (merge/split) without naming debate
- ✓ "Why is this called 'Twelve-Day War'? Nobody calls it that!"
- ✓ "Change 'celebrate' to 'mourn'"
- ✗ "Should we merge this article?" (structural only)

### 6. SOURCE_HIERARCHY
**Code 1:** Source CATEGORY challenged (national, ideological)
**Code 0:** Standard "provide reliable sources" reminder
- ✓ "Iran International is opposition propaganda"
- ✓ "The only source is IRGC, not credible"
- ✓ "Western sources are biased"
- ✗ "Please provide a reliable source" (neutral request)
- ✗ "This source doesn't say what you claim" (factual correction)

## Decision Tests (apply when uncertain)
1. **Is anyone being harmed?** No clear victim → 0
2. **Active or passive?** Template presence alone → 0
3. **Strategic or routine?** Routine process → 0
4. **Specific or general?** General RS reminder → 0

## Output Format
Return ONLY a JSON array:
```json
[
  {
    "id": "iran_051",
    "testimonial_injustice": 0,
    "hermeneutical_injustice": 0,
    "epistemic_dispossession": 0,
    "policy_weaponization": 0,
    "naming_dispute": 0,
    "source_hierarchy": 0,
    "primary_form": "none",
    "confidence": 0.85,
    "reasoning": "Routine edit request with standard response, no one excluded or harmed"
  }
]
```
