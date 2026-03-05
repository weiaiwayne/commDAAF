# Wikipedia Epistemic Injustice Coding Task

You are coding Wikipedia talk page excerpts for forms of epistemic injustice. Code each excerpt for the presence (1) or absence (0) of six constructs:

## Constructs

1. **TESTIMONIAL_INJUSTICE**: Speaker's credibility discounted based on identity, experience, account age, or group membership (not argument substance)
   - Examples: "You only have 50 edits", "This is clearly a pro-X account", "New users shouldn't edit this"

2. **HERMENEUTICAL_INJUSTICE**: Disputes over available terminology, categories, or frameworks that prevent certain perspectives from being expressed
   - Examples: "The term 'genocide' cannot be used", "This should be called 'conflict' not 'war'"

3. **EPISTEMIC_DISPOSSESSION**: Platform structures systematically benefiting established groups over newcomers
   - Examples: "EC-protected so new editors can't contribute", "Consensus was established by longtime editors"

4. **POLICY_WEAPONIZATION**: Using Wikipedia policies strategically to delegitimize opposing viewpoints
   - Examples: "This violates WP:UNDUE" (without substantive engagement), "I'll take this to ANI"

5. **NAMING_DISPUTE**: Explicit contestation over article titles or event names with political implications
   - Examples: "This should be moved to 'conflict'", "Calling it a 'massacre' is POV"

6. **SOURCE_HIERARCHY**: Arguments establishing hierarchies of source reliability along national/ideological lines
   - Examples: "Iranian state media is not reliable", "Western sources are biased", "Al Jazeera has agenda"

## Decision Rules
- Code **1** if at least one clear instance present
- Code ALL applicable constructs (can overlap)
- If uncertain, err toward **0** (conservative)
- **primary_form**: most prominent construct, or "none"

## Output Format

Return a JSON array with one object per excerpt:

```json
[
  {
    "id": "iran_051",
    "testimonial_injustice": 0,
    "hermeneutical_injustice": 1,
    "epistemic_dispossession": 0,
    "policy_weaponization": 1,
    "naming_dispute": 0,
    "source_hierarchy": 0,
    "primary_form": "hermeneutical_injustice",
    "confidence": 0.85,
    "reasoning": "Dispute over whether 'massacre' terminology is allowed"
  }
]
```

Return ONLY the JSON array, no other text.
