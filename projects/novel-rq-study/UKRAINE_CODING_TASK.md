# Ukraine Dataset Coding Task

## Instructions
Code ALL posts in batches ukraine_batch_1.json through ukraine_batch_14.json (339 posts total).

## Location
`/root/.openclaw/workspace/skills/commdaaf/projects/novel-rq-study/`

## Frame Definitions

| Frame | Definition | Key Signals |
|-------|------------|-------------|
| **SOLIDARITY** | Unity, collective identity, "we stand together" | "We stand", "Together", collective pronouns |
| **INJUSTICE** | Wrongdoing with explicit perpetrator/blame | "They killed", "Russia attacked", blame assigned |
| **CONFLICT** | Clash between active opposing parties | "Clashes", "battle", both sides active |
| **HUMANITARIAN** | Suffering/victimhood WITHOUT perpetrator focus | "Lives lost", "Suffering", victim focus |
| **HOPE** | Optimism, future vision, perseverance | "We will win", "Victory coming", positive future |
| **INFORMATIONAL** | Neutral news/facts/updates | "Update:", "Report:", factual language |
| **CALL_TO_ACTION** | Direct appeals to act/share/donate | "Share this", "Donate", imperatives |

## Decision Rules for Ukraine Context
- INFORMATIONAL: Military updates, troop movements, news reports
- INJUSTICE: Russian war crimes, atrocities, blame on Putin/Russia
- CONFLICT: Active fighting descriptions, battle reports
- HUMANITARIAN: Civilian suffering, refugees (without blame focus)
- HOPE: Victory predictions, resilience, positive outcomes
- SOLIDARITY: Western support, NATO unity, #StandWithUkraine
- CALL_TO_ACTION: Donate appeals, weapon requests, #ArmUkraineNow

## Output Format
Save results to `ukraine_codings_[MODEL].json`:
```json
{
  "model": "your-model-name",
  "total_posts": 339,
  "codings": {
    "post_id": {"frame": "FRAME", "valence": "pos/neg/neutral", "arousal": "high/medium/low"},
    ...
  }
}
```

## Valence
- positive: Support for Ukraine, hope, solidarity
- negative: Condemnation, war crimes, suffering
- neutral: Factual reporting

## Arousal
- high: URGENT, violence, death, exclamations
- medium: Standard advocacy, appeals
- low: Neutral reporting, updates
