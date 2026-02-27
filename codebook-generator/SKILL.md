# Codebook Generator Skill

Generate operational coding schemes from theoretical constructs.

## When to Use

- Starting a content analysis project
- Translating theory into measurable codes
- Need consistent definitions across coders/models
- Working with multilingual data
- Building CommDAAF-compliant prompts

## Capabilities

1. **Construct Definition** - Transform theoretical concept into operational definition
2. **Decision Rules** - Generate hierarchical rules for ambiguous cases
3. **Anchor Generation** - Create prototypical examples and counter-examples
4. **Multilingual Anchors** - Produce culturally appropriate examples in multiple languages
5. **CommDAAF Prompt Assembly** - Combine into ready-to-use coding prompt

## Usage

### Basic: Single Construct

```
Generate a codebook entry for the construct "injustice frame" 
based on Gamson (1992) for coding social media posts.
```

### Advanced: Full Codebook

```
Generate a CommDAAF-compliant codebook for analyzing protest tweets with:
- Constructs: [frame (7 types), valence, arousal]
- Theory sources: Entman 1993, Gamson 1992, Snow & Benford 1988
- Languages: English, Persian, Arabic
- Output: JSON schema + decision rules + anchors
```

## Output Format

```json
{
  "construct": "INJUSTICE",
  "definition": "Content that identifies wrongdoing and explicitly assigns blame to a perpetrator",
  "theoretical_source": "Gamson 1992; diagnostic framing",
  "decision_rules": [
    "Must name or clearly imply a responsible actor",
    "Prioritize over HUMANITARIAN when perpetrator is explicit",
    "Distinguish from CONFLICT: INJUSTICE = one-sided blame, CONFLICT = two-sided clash"
  ],
  "anchors": {
    "prototypical": [
      "The regime killed her for wearing hijab wrong",
      "Police brutality must end - they are murderers"
    ],
    "counter_examples": [
      "She died in custody (no perpetrator = HUMANITARIAN)",
      "Protesters clashed with police (two-sided = CONFLICT)"
    ]
  },
  "multilingual_anchors": {
    "fa": ["رژیم او را کشت", "پلیس قاتل است"],
    "ar": ["النظام قتلها", "الشرطة قتلة"]
  },
  "reliability_notes": "Moderate difficulty; perpetrator identification can be implicit",
  "common_confusions": ["HUMANITARIAN (victim-focused)", "CONFLICT (both sides active)"]
}
```

## Best Practices

1. **Start with theory** - Don't invent constructs; ground them in literature
2. **Define boundaries** - Explicitly state what does NOT qualify
3. **Anticipate overlaps** - Create decision rules before coding, not after disagreements
4. **Test anchors** - Verify examples with domain experts or pilot coding
5. **Version your codebook** - Track changes as you refine

## Integration with CommDAAF Pipeline

```python
from commdaaf import CodebookGenerator

generator = CodebookGenerator()

# Generate single construct
injustice = generator.generate(
    construct="injustice frame",
    theory="Gamson 1992",
    context="social media protest"
)

# Generate full codebook
codebook = generator.generate_full(
    constructs=["solidarity", "injustice", "conflict", "humanitarian", "hope", "informational", "call_to_action"],
    theory_sources={"framing": "Entman 1993", "movements": "Snow & Benford 1988"},
    languages=["en", "fa", "ar"],
    output_format="commdaaf_prompt"
)
```

## Example: 7-Frame Protest Codebook

See `examples/protest_frames_codebook.json` for the complete codebook used in the #MahsaAmini study.

## Limitations

- Cannot validate theoretical appropriateness (human judgment required)
- Multilingual anchors need native speaker verification
- Decision rules may not cover all edge cases
- Generated examples may not perfectly match your data domain

## References

- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm.
- Gamson, W. A. (1992). Talking politics.
- Krippendorff, K. (2018). Content analysis: An introduction to its methodology.
- Snow, D. A., & Benford, R. D. (1988). Ideology, frame resonance, and participant mobilization.
