# Coding Instructions

## Frame Codes

| Code | Frame | Key Indicators |
|------|-------|----------------|
| ECO | Economic Opportunity | innovation, competitiveness, growth, jobs creation |
| SEC | National Security | China, defense, adversaries, military, intelligence |
| EXI | Existential Risk | alignment, extinction, superintelligence, catastrophic |
| REG | Regulation/Governance | oversight, accountability, transparency, legislation |
| CIV | Civil Rights | bias, discrimination, privacy, surveillance |
| LAB | Labor/Automation | displacement, workforce, reskilling, jobs loss |
| HEA | Healthcare | diagnosis, treatment, patients, medical |
| CON | Consumer Protection | scams, fraud, deepfakes, misinformation |

## Valence Codes

| Code | Meaning |
|------|---------|
| POS | Positive (opportunity, benefit) |
| NEG | Negative (risk, threat, harm) |
| NEU | Neutral/balanced |

## Output Format

For each segment, provide:
```json
{
  "id": 1,
  "primary_frame": "ECO",
  "secondary_frames": ["SEC"],
  "valence": "POS",
  "confidence": "high",
  "notes": "Speaker emphasizes US competitiveness"
}
```
