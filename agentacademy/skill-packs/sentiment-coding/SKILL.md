# Sentiment Coding Skill Pack

**Version:** 0.1.0  
**Status:** Pending Validation  
**Maintainer:** UMass Computational Communication Lab

---

## Overview

Systematic coding of sentiment (valence and arousal) in text content.

## Capabilities

- Code valence: positive / negative / neutral / mixed
- Code arousal: low / medium / high
- Handle sarcasm and irony detection
- Multilingual sentiment with calibration

---

## Probing Questions (ALL REQUIRED)

```
Q1: What EXACTLY do you mean by 'sentiment'?
    ✓ Emotional valence (positive/negative)
    ✓ Attitude toward target
    ✓ Affective intensity
    ✗ "Sentiment" — TOO VAGUE

Q2: What's your unit of analysis?
    ✓ Document/post
    ✓ Sentence
    ✓ Entity-specific (sentiment toward X)
    ✗ "The text" — BE SPECIFIC

Q3: What approach and why?
    ✓ Dictionary-based (fast, interpretable)
    ✓ ML classifier (flexible, needs training data)
    ✓ LLM annotation (context-aware, expensive)
    ✗ "Whatever works" — JUSTIFY CHOICE

Q4: How will you handle neutral content?
    ✓ Explicit neutral category
    ✓ Forced choice (no neutral)
    ✓ Threshold-based (weak positive/negative → neutral)

Q5: What's your sarcasm strategy?
    ✓ Flag for human review
    ✓ Context-aware detection
    ✓ Exclude from analysis
    ✗ "Ignore it" — UNACCEPTABLE

Q6: Validation plan?
    ✓ Correlation with human judgment
    ✓ Comparison with established tools (VADER, etc.)
    ✓ Domain-specific benchmarking
```

---

## Valence Anchors

| Level | Indicators |
|-------|------------|
| **Positive** | Joy, hope, celebration, victory, gratitude, love, excitement |
| **Negative** | Anger, sadness, fear, disgust, grief, outrage, despair |
| **Neutral** | Factual, informational, no emotional loading |
| **Mixed** | Both positive and negative elements present |

---

## Arousal Anchors

| Level | Indicators |
|-------|------------|
| **High** | Urgency, intensity, exclamation, threat, crisis language |
| **Medium** | Engagement, concern, emphasis, appeals |
| **Low** | Calm, matter-of-fact, routine, detached |

---

## Output Schema

```json
{
  "id": "string",
  "valence": "positive | negative | neutral | mixed",
  "arousal": "low | medium | high",
  "confidence": "number (0.0-1.0)",
  "sarcasm_flag": "boolean",
  "target": "string | null (if entity-specific)"
}
```

---

## Known Limitations

1. **Sarcasm detection** — All models struggle
2. **Cultural calibration** — Arousal expression varies by culture
3. **Target ambiguity** — Positive toward X may be negative toward Y
4. **Emoji interpretation** — Context-dependent

---

## Validation Requirements

| Tier | Requirement |
|------|-------------|
| 🟢 Exploratory | Multi-model, correlation with VADER baseline |
| 🟡 Pilot | + Human validation (N≥100), r≥0.7 |
| 🔴 Publication | + Systematic validation (N≥200), κ≥0.8 |

---

## TODO

- [ ] Create benchmark dataset
- [ ] Add sarcasm detection protocol
- [ ] Add entity-specific sentiment guidance
- [ ] Peer validation

---

## References

- Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis.
- Mohammad, S. M., & Turney, P. D. (2013). Crowdsourcing a word-emotion association lexicon.
