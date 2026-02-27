# CommDAAF Frame Coding Protocol

## Task
Code each post with PRIMARY_FRAME, VALENCE, and AROUSAL.

## Frame Definitions (v0.5)

| Frame | Definition | Key Signals |
|-------|------------|-------------|
| **SOLIDARITY** | Unity, collective identity, "we are together" | "We stand", "Together", collective pronouns |
| **INJUSTICE** | Wrongdoing with explicit perpetrator/blame | "They killed", "Police attacked", blame assigned |
| **CONFLICT** | Clash between active opposing parties | "Clashes", "vs", both sides active |
| **HUMANITARIAN** | Suffering/victimhood WITHOUT perpetrator focus | "Lives lost", "Suffering", victim focus |
| **HOPE** | Optimism, future vision, perseverance | "We will win", "Freedom coming", positive future |
| **INFORMATIONAL** | Neutral news/facts/updates | "Update:", "Report:", factual language |
| **CALL_TO_ACTION** | Direct appeals to act/share/protest | "Share this", "Rise up", imperatives |

## Decision Rules

### INJUSTICE vs CONFLICT vs HUMANITARIAN
- **INJUSTICE**: Perpetrator explicit AND blame assigned ("They killed us")
- **CONFLICT**: Both sides active participants ("Clashes between X and Y")  
- **HUMANITARIAN**: Victim focus WITHOUT perpetrator ("Lives lost", "Suffering")

### SOLIDARITY vs CALL_TO_ACTION
- **SOLIDARITY**: Emphasizes unity/togetherness ("We are one")
- **CALL_TO_ACTION**: Emphasizes mobilization/demands ("Share this!", "Join us!")

## Valence (Required)
- **positive**: Hopeful, supportive, celebrating resistance
- **negative**: Grief, anger, condemnation, suffering
- **neutral**: Factual, informational, neither positive nor negative

## Arousal Anchors
| Level | Examples | Markers |
|-------|----------|---------|
| **high** | "They are killing us!", "URGENT", death/violence | Exclamations, imperatives, threat language |
| **medium** | "We stand together", "Justice for Mahsa" | Emotional appeals, hashtag campaigns |
| **low** | "Update on situation", "Here's what happened" | Neutral reporting, factual |

## Special Cases
- **Hashtag-heavy posts** (>50% hashtags): Code from hashtag meaning, default arousal=medium
- **Persian/Farsi text**: Poetic metaphors may convey higher arousal than literal reading
- **Mixed frames**: Code the PRIMARY (dominant) frame

## Output Format
JSON array with ONLY these fields per post:
```json
{"id": "...", "frame": "SOLIDARITY", "valence": "positive", "arousal": "medium"}
```
