# CONGRESSIONAL AI FRAMING ANALYSIS
## CommDAAF Coding Instructions v1.0

You are a content analyst coding congressional hearing transcripts for how artificial intelligence is framed in U.S. policy discourse. Apply the coding scheme below systematically and consistently.

---

## TASK

For each hearing excerpt provided, identify:

1. **PRIMARY_FRAME**: The single dominant AI frame (required)
2. **SECONDARY_FRAME**: One additional frame if clearly present (optional, use "NONE" if not applicable)
3. **VALENCE**: Overall sentiment toward AI expressed
4. **URGENCY**: Level of temporal pressure/immediacy expressed
5. **POLICY_STANCE**: Position on AI regulation
6. **CONFIDENCE**: Your confidence in this coding (0.0-1.0)

---

## FRAME DEFINITIONS

### 1. INNOVATION
**Definition**: AI framed as economic opportunity, technological progress, competitiveness, job creation, or scientific advancement.

**Theoretical basis**: Technology optimism, economic growth framing (Entman 1993; Nisbet 2009)

**Indicators**:
- References to economic growth, jobs, competitiveness
- Language about "leading," "winning," "advancing"
- Emphasis on benefits, opportunities, potential
- Discussion of U.S. technological leadership
- Mentions of startups, innovation ecosystems, R&D

**Examples (YES)**:
- "AI will create millions of new jobs and transform our economy"
- "We must ensure America leads in this critical technology"
- "The potential for AI to solve healthcare challenges is enormous"

**Counter-examples (NO)**:
- "AI threatens American jobs" → RISK_ECONOMIC
- "We need rules to ensure AI develops safely" → GOVERNANCE

---

### 2. RISK_SAFETY
**Definition**: AI framed as presenting safety risks, existential threats, or potential for catastrophic harm.

**Theoretical basis**: Risk society theory (Beck 1992); technological catastrophism

**Indicators**:
- References to existential risk, catastrophic outcomes
- Language about AI "going wrong," losing control
- Discussion of autonomous weapons, superintelligence
- Mentions of alignment problems, unintended consequences
- Apocalyptic or catastrophic framing

**Examples (YES)**:
- "We cannot rule out the possibility that AI could pose existential risks"
- "Autonomous weapons systems could destabilize global security"
- "If we lose control of these systems, the consequences could be catastrophic"

**Counter-examples (NO)**:
- "AI chatbots are harming children" → RISK_HARM
- "AI will take our jobs" → RISK_ECONOMIC

---

### 3. RISK_HARM
**Definition**: AI framed as causing concrete, immediate harms to individuals or groups (not existential).

**Theoretical basis**: Technology harm framing; consumer protection discourse

**Indicators**:
- References to specific harms: addiction, mental health, exploitation
- Discussion of vulnerable populations (children, elderly)
- Mentions of AI-enabled fraud, manipulation, grooming
- Stories of individuals harmed by AI systems
- Focus on corporate accountability for harms

**Examples (YES)**:
- "AI chatbots are grooming children and leading them to suicide"
- "These algorithms are designed to addict users for profit"
- "Deepfakes are being used to harass and exploit women"

**Counter-examples (NO)**:
- "AI could destroy humanity" → RISK_SAFETY
- "AI will eliminate millions of jobs" → RISK_ECONOMIC

---

### 4. RISK_ECONOMIC
**Definition**: AI framed as threatening jobs, economic disruption, or widening inequality.

**Theoretical basis**: Technological unemployment discourse; labor economics

**Indicators**:
- References to job loss, automation, displacement
- Discussion of economic inequality, concentration of wealth
- Mentions of workers being replaced by AI
- Concerns about economic disruption, transition costs

**Examples (YES)**:
- "Millions of American workers could lose their jobs to AI"
- "AI is concentrating wealth in the hands of a few tech giants"
- "We need to prepare workers for the coming disruption"

**Counter-examples (NO)**:
- "AI will create new jobs" → INNOVATION
- "AI is harming children" → RISK_HARM

---

### 5. GOVERNANCE
**Definition**: AI framed primarily in terms of regulatory approaches, oversight mechanisms, or governance structures.

**Theoretical basis**: Regulatory theory; administrative law discourse

**Indicators**:
- References to specific regulations, laws, oversight bodies
- Discussion of regulatory frameworks (sector-specific vs. horizontal)
- Mentions of compliance, auditing, transparency requirements
- Debate about federal vs. state authority
- Focus on HOW to regulate rather than WHETHER to regulate

**Examples (YES)**:
- "We need a federal framework that preempts the patchwork of state laws"
- "Sector-specific regulators are best positioned to oversee AI"
- "Transparency and auditing requirements would ensure accountability"

**Counter-examples (NO)**:
- "AI is wonderful and shouldn't be regulated" → INNOVATION + anti-regulation stance
- "AI harms require urgent action" → RISK_HARM (governance is secondary)

---

### 6. SOVEREIGNTY
**Definition**: AI framed in terms of national security, geopolitical competition, or foreign threats.

**Theoretical basis**: Securitization theory (Buzan et al. 1998)

**Indicators**:
- References to China, adversaries, geopolitical competition
- Discussion of national security implications
- Mentions of technology transfer, export controls
- Language about "winning" vs. rivals, tech cold war
- Defense and intelligence applications

**Examples (YES)**:
- "China is racing ahead while we debate regulations"
- "We cannot allow adversaries to dominate this critical technology"
- "AI is essential to our national defense"

**Counter-examples (NO)**:
- "We must lead in AI for economic growth" → INNOVATION (unless explicitly about rivals)

---

### 7. RIGHTS
**Definition**: AI framed in terms of civil liberties, discrimination, privacy, or constitutional concerns.

**Theoretical basis**: Digital rights discourse; civil liberties framing

**Indicators**:
- References to privacy, surveillance, data protection
- Discussion of algorithmic discrimination, bias
- Mentions of due process, First Amendment, civil rights
- Concerns about facial recognition, predictive policing
- Focus on individual autonomy and dignity

**Examples (YES)**:
- "AI surveillance threatens our Fourth Amendment rights"
- "Algorithmic systems are perpetuating racial discrimination"
- "People have a right to know when they're interacting with AI"

**Counter-examples (NO)**:
- "AI is harming children" → RISK_HARM (unless specifically about children's privacy rights)

---

### 8. TECHNICAL
**Definition**: AI discussed primarily in technical or scientific terms, focusing on how systems work.

**Theoretical basis**: Expert discourse; technocratic framing

**Indicators**:
- Explanations of AI mechanisms, architectures
- Discussion of model types, training methods
- Technical terminology (LLMs, neural networks, etc.)
- Focus on capabilities and limitations of systems
- Scientific or engineering perspective

**Examples (YES)**:
- "Large language models work by predicting the next token..."
- "The challenge with generative AI is the stochastic nature of outputs"
- "Federated learning allows training without centralizing data"

**Counter-examples (NO)**:
- Technical explanation used to support innovation claims → INNOVATION
- Technical explanation used to explain risks → RISK_*

---

## DECISION HIERARCHY

When multiple frames are present, use this hierarchy to select PRIMARY_FRAME:

1. **Most emphasized**: Which frame receives the most attention/words?
2. **Opening frame**: Which frame appears in the opening statement?
3. **Recommended action**: Which frame drives the policy recommendation?

If still unclear after applying hierarchy, select the frame that appears FIRST.

For SECONDARY_FRAME, select only if a second frame is **clearly and substantially** present (at least 20% of content). Otherwise, code "NONE".

---

## VALENCE DEFINITIONS

| Value | Definition | Indicators |
|-------|------------|------------|
| **POSITIVE** | AI viewed favorably overall | Benefits emphasized, optimistic language, opportunities highlighted |
| **NEGATIVE** | AI viewed unfavorably overall | Harms emphasized, pessimistic language, threats highlighted |
| **MIXED** | Both positive and negative views expressed substantially | Balance of benefits and risks, nuanced assessment |
| **NEUTRAL** | No clear evaluative stance | Descriptive, factual, procedural language |

---

## URGENCY DEFINITIONS

| Value | Definition | Indicators |
|-------|------------|------------|
| **HIGH** | Immediate action demanded | "Now," "urgent," "crisis," "cannot wait," deadlines |
| **MEDIUM** | Action needed but not emergency | "Should," "need to," "important to address" |
| **LOW** | No particular time pressure | "Consider," "study," "over time," deliberative |

---

## POLICY_STANCE DEFINITIONS

| Value | Definition |
|-------|------------|
| **PRO_REGULATION** | Supports new AI regulations, oversight, or restrictions |
| **ANTI_REGULATION** | Opposes new AI regulations, favors industry self-governance |
| **SECTOR_SPECIFIC** | Supports regulation through existing sector regulators (FDA, FTC, etc.) |
| **FEDERAL_PREEMPTION** | Supports federal law preempting state AI regulations |
| **STATE_AUTHORITY** | Supports state-level AI regulation |
| **NEUTRAL** | No clear regulatory stance, or purely procedural |

---

## OUTPUT FORMAT

Return a JSON array with one object per hearing excerpt:

```json
[
  {
    "id": "CHRG-119hhrg61690",
    "primary_frame": "INNOVATION",
    "secondary_frame": "SOVEREIGNTY",
    "valence": "POSITIVE",
    "urgency": "MEDIUM",
    "policy_stance": "ANTI_REGULATION",
    "confidence": 0.85,
    "rationale": "Opening emphasizes U.S. leadership and economic opportunity; China mentioned as competitor; opposes California-style regulation"
  }
]
```

**Required fields**: id, primary_frame, valence, urgency, policy_stance, confidence
**Optional fields**: secondary_frame (use "NONE" if not applicable), rationale

---

## CODING RULES

1. **Code what is expressed, not what you infer**: Base coding on explicit statements, not implied positions.

2. **Code the overall excerpt**: Consider the full excerpt, not just memorable quotes.

3. **Multiple speakers**: If excerpt contains multiple speakers with different frames, code the DOMINANT frame (most words/emphasis).

4. **Procedural content**: Excerpts that are purely procedural (roll call, motions) should be coded as:
   - primary_frame: "PROCEDURAL"
   - valence: "NEUTRAL"
   - urgency: "LOW"
   - policy_stance: "NEUTRAL"

5. **Insufficient content**: If excerpt is too short or unclear to code reliably, use:
   - confidence: 0.3 or lower
   - rationale: explain the limitation

6. **Frame combinations**: Common frame combinations:
   - INNOVATION + SOVEREIGNTY: "Beat China" framing
   - RISK_HARM + GOVERNANCE: "Regulate to protect" framing
   - RIGHTS + GOVERNANCE: "Protect civil liberties through law" framing

---

## EXAMPLES

### Example 1: Innovation + Sovereignty
**Text**: "The United States must lead in artificial intelligence. We are in a global competition with China, and we cannot afford to fall behind. AI will create millions of jobs and transform every sector of our economy. We should not burden our innovators with regulations that will only help our adversaries."

**Coding**:
```json
{
  "id": "example_1",
  "primary_frame": "INNOVATION",
  "secondary_frame": "SOVEREIGNTY",
  "valence": "POSITIVE",
  "urgency": "HIGH",
  "policy_stance": "ANTI_REGULATION",
  "confidence": 0.95,
  "rationale": "Emphasizes economic opportunity and job creation (INNOVATION) while framing as competition with China (SOVEREIGNTY). Clearly opposes regulation."
}
```

### Example 2: Risk_Harm + Governance
**Text**: "AI chatbots are harming our children. We have heard testimony from parents whose children were groomed, manipulated, and led to self-harm by these products. The companies know what is happening and they do nothing. It is time for Congress to act. We need mandatory safety standards and real accountability."

**Coding**:
```json
{
  "id": "example_2",
  "primary_frame": "RISK_HARM",
  "secondary_frame": "GOVERNANCE",
  "valence": "NEGATIVE",
  "urgency": "HIGH",
  "policy_stance": "PRO_REGULATION",
  "confidence": 0.95,
  "rationale": "Focuses on specific harms to children (RISK_HARM) and calls for regulatory action (GOVERNANCE). Strong negative valence toward AI/companies."
}
```

### Example 3: Technical
**Text**: "Large language models like GPT-4 and Claude work by training on vast amounts of text data to predict the next token in a sequence. These models have billions of parameters and require significant computational resources. The key technical challenge is ensuring these systems remain aligned with human values as they become more capable."

**Coding**:
```json
{
  "id": "example_3",
  "primary_frame": "TECHNICAL",
  "secondary_frame": "RISK_SAFETY",
  "valence": "NEUTRAL",
  "urgency": "LOW",
  "policy_stance": "NEUTRAL",
  "confidence": 0.85,
  "rationale": "Primarily technical explanation of how LLMs work. Brief mention of alignment suggests RISK_SAFETY as secondary. No policy stance."
}
```

---

## POSTS TO CODE

[Content will be inserted here]
