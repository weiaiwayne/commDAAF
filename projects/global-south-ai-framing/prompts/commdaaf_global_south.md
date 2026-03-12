# CommDAAF Coding Prompt: Global South AI Governance Framing

## Task
You are a content analyst coding legislative documents for how they **frame** artificial intelligence. For each document, identify the PRIMARY frame (most dominant) and any SECONDARY frames present.

## Coding Scheme (8 Frames)

| Frame | Code | Definition | Example Keywords |
|-------|------|------------|------------------|
| **Innovation** | INNOVATION | AI as economic opportunity, competitiveness, growth, development | innovation, competitiveness, growth, jobs, economy, startup, investment |
| **Safety Risk** | RISK_SAFETY | Existential/catastrophic AI threats, loss of control | existential, catastrophic, superintelligence, control problem, alignment |
| **Harm Risk** | RISK_HARM | Concrete harms to individuals/groups (children, users, vulnerable populations) | harm, abuse, manipulation, misinformation, deepfake, children, vulnerable |
| **Economic Risk** | RISK_ECONOMIC | Job displacement, inequality, economic disruption | unemployment, job loss, workers, inequality, displacement, automation |
| **Governance** | GOVERNANCE | Regulatory approaches, oversight mechanisms, compliance | regulation, oversight, compliance, audit, standards, accountability |
| **Sovereignty** | SOVEREIGNTY | National security, geopolitical competition, strategic autonomy | security, defense, China, sovereignty, strategic, national interest |
| **Rights** | RIGHTS | Privacy, discrimination, civil liberties, algorithmic bias | privacy, discrimination, bias, rights, dignity, consent, fairness |
| **Technical** | TECHNICAL | Scientific explanations, technical standards, capabilities | algorithm, model, training, data, neural network, parameters |

## Country-Specific Context

### South Africa
- **4IR (Fourth Industrial Revolution)** is a dominant discourse frame
- High unemployment context shapes RISK_ECONOMIC framing
- Digital inclusion and rural access concerns
- Post-apartheid equality lens on RIGHTS

### Brazil
- **Marco Civil da Internet** precedent for digital governance
- LGPD (data protection) alignment concerns
- Small business (SIMPLES) considerations
- Social media regulation debates

### India
- World's largest democracy - scale considerations
- **Digital India** initiative framing
- Data localization debates
- Balance between innovation and regulation

## Output Format

For each document, provide:

```json
{
  "id": "<document_id>",
  "title": "<title>",
  "country": "<country_code>",
  "primary_frame": "<FRAME_CODE>",
  "secondary_frames": ["<FRAME_CODE>", ...],
  "confidence": <0.0-1.0>,
  "evidence": "<1-2 sentence justification with key quote>",
  "frame_distribution": {
    "INNOVATION": <0.0-1.0>,
    "RISK_SAFETY": <0.0-1.0>,
    "RISK_HARM": <0.0-1.0>,
    "RISK_ECONOMIC": <0.0-1.0>,
    "GOVERNANCE": <0.0-1.0>,
    "SOVEREIGNTY": <0.0-1.0>,
    "RIGHTS": <0.0-1.0>,
    "TECHNICAL": <0.0-1.0>
  }
}
```

## Rules
1. **Primary frame** = the dominant framing (>40% of content focus)
2. **Secondary frames** = frames with >15% presence
3. **Confidence** = your certainty in the coding (0.7+ for clear cases)
4. **Evidence** = specific quote or paraphrase supporting your coding
5. **Frame distribution** = normalized scores summing to 1.0

## Batch Instructions
You will receive a JSON array of documents. Return a JSON array of codings, one per document. Maintain the same order as input.

Do NOT include any text outside the JSON output.
