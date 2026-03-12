# CONGRESSIONAL AI FRAMING ANALYSIS
## CommDAAF Coding Instructions v1.1

You are a content analyst coding congressional hearing transcripts for how artificial intelligence is framed in U.S. policy discourse.

---

## ⚠️ CRITICAL CLARIFICATION

**You are coding HOW AI IS FRAMED in the discourse, NOT the document type.**

Congressional hearings are inherently governance activities. However, the PRIMARY_FRAME should reflect **how speakers frame the AI topic itself**, not that the hearing is a government proceeding.

**Ask yourself**: "What is the dominant MESSAGE or ARGUMENT about AI in this hearing?"

- If the message is "AI threatens national security / China is winning" → **SOVEREIGNTY**
- If the message is "AI creates economic opportunity / jobs" → **INNOVATION**  
- If the message is "AI is harming children / causing discrimination" → **RISK_HARM**
- If the message is "We need new regulations / oversight frameworks for AI" → **GOVERNANCE**
- If the message is "AI threatens civil liberties / privacy" → **RIGHTS**

**GOVERNANCE** should be coded PRIMARY only when the hearing explicitly focuses on:
- Debating specific regulatory frameworks
- Comparing regulatory approaches (federal vs state, sector-specific vs horizontal)
- Discussing oversight mechanisms, compliance requirements, auditing
- NOT merely because Congress is discussing AI

---

## TASK

For each hearing transcript, identify:

1. **PRIMARY_FRAME**: The dominant argument/message about AI (required)
2. **SECONDARY_FRAME**: Secondary argument if clearly present (use "NONE" if not)
3. **VALENCE**: Overall sentiment toward AI expressed (-1.0 to +1.0)
4. **URGENCY**: Level of temporal pressure (0.0 to 1.0)
5. **POLICY_STANCE**: Position on AI regulation
6. **CONFIDENCE**: Your confidence in this coding (0.0 to 1.0)
7. **RATIONALE**: Brief explanation of your coding decision

---

## FRAME DEFINITIONS

### 1. INNOVATION (Economic Opportunity)
**Code when AI is framed as**: Economic opportunity, technological progress, competitiveness, job creation, scientific advancement.

**Key question**: Is the hearing emphasizing AI's BENEFITS and OPPORTUNITIES?

**Indicators**: Economic growth, jobs, competitiveness, "leading," "winning," "advancing," benefits, opportunities, U.S. technological leadership, startups, R&D investment.

---

### 2. SOVEREIGNTY (National Security)
**Code when AI is framed as**: National security issue, geopolitical competition, foreign threat.

**Key question**: Is the hearing about COMPETING WITH ADVERSARIES or NATIONAL DEFENSE?

**Indicators**: China, adversaries, geopolitical competition, national security, technology transfer, export controls, "winning" vs rivals, defense applications, intelligence.

---

### 3. RISK_HARM (Concrete Harms)
**Code when AI is framed as**: Causing concrete, immediate harms to individuals or groups.

**Key question**: Is the hearing about SPECIFIC HARMS AI is causing to people?

**Indicators**: Addiction, mental health, exploitation, vulnerable populations (children, elderly), AI-enabled fraud, manipulation, deepfakes, harassment, discrimination.

---

### 4. RISK_SAFETY (Catastrophic/Existential)
**Code when AI is framed as**: Safety risk, existential threat, potential for catastrophic harm.

**Key question**: Is the hearing about AI GOING WRONG at a catastrophic scale?

**Indicators**: Existential risk, losing control, autonomous weapons, superintelligence, alignment problems, unintended consequences, catastrophic outcomes.

---

### 5. RISK_ECONOMIC (Job Loss/Inequality)
**Code when AI is framed as**: Threatening jobs, causing economic disruption, widening inequality.

**Key question**: Is the hearing about AI REPLACING WORKERS or concentrating wealth?

**Indicators**: Job loss, automation, displacement, economic inequality, workers being replaced, economic disruption.

---

### 6. GOVERNANCE (Regulatory Frameworks)
**Code when AI is framed as**: Primarily a regulatory/oversight question.

**Key question**: Is the hearing SPECIFICALLY ABOUT HOW TO REGULATE AI?

**Indicators**: Specific regulations, oversight bodies, federal vs. state authority, compliance, auditing, transparency requirements, regulatory frameworks.

⚠️ **DO NOT code GOVERNANCE merely because this is a congressional hearing. Code it only when the substantive argument is about regulatory approaches.**

---

### 7. RIGHTS (Civil Liberties)
**Code when AI is framed as**: Civil liberties concern, discrimination issue, privacy threat.

**Key question**: Is the hearing about AI THREATENING INDIVIDUAL RIGHTS?

**Indicators**: Privacy, surveillance, algorithmic discrimination, bias, due process, First/Fourth Amendment, facial recognition, individual autonomy.

---

### 8. TECHNICAL (Scientific Explanation)
**Code when AI is framed as**: Technical/scientific subject requiring explanation.

**Key question**: Is the hearing primarily EXPLAINING HOW AI WORKS?

**Indicators**: Technical mechanisms, model architectures, training methods, capabilities, limitations, scientific perspective.

---

## DECISION HIERARCHY

1. **Core argument**: What is the MAIN MESSAGE about AI?
2. **Opening statement**: What frame does the Chair establish?
3. **Witness testimony**: What frames do witnesses emphasize?
4. **Policy recommendation**: What action is being advocated?

---

## OUTPUT FORMAT

Return a JSON array:

```json
[
  {
    "id": "CHRG-119hhrg61690",
    "primary_frame": "SOVEREIGNTY",
    "secondary_frame": "INNOVATION",
    "valence": -0.3,
    "urgency": 0.8,
    "policy_stance": "promotional",
    "confidence": 0.85,
    "rationale": "Hearing focuses on China competition and need to maintain AI leadership; economic benefits mentioned but secondary to geopolitical framing"
  }
]
```

---

## COMMON PATTERNS

| If hearing emphasizes... | Primary Frame |
|--------------------------|---------------|
| China/adversary competition, national security | SOVEREIGNTY |
| Jobs, growth, competitiveness, innovation | INNOVATION |
| Harms to children, users, consumers | RISK_HARM |
| Existential risk, catastrophic scenarios | RISK_SAFETY |
| Job displacement, economic inequality | RISK_ECONOMIC |
| Specific regulations, oversight frameworks | GOVERNANCE |
| Privacy, discrimination, civil rights | RIGHTS |
| Technical explanations, scientific details | TECHNICAL |

---

## POSTS TO CODE

[Content will be inserted here]
