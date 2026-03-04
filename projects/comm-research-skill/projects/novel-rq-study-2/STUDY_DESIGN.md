# Novel RQ Study: Linguistic Style and Attention Capture

**Date:** 2026-03-04  
**Validation Tier:** 🟢 EXPLORATORY  
**Status:** In Progress

---

## Phase 1: RQ Generation (Zotero-Informed)

### Wayne's Research Interests (from Zotero)
- Agentic AI (15 papers)
- AI methodology (33 papers)
- Coordination detection (2+ papers)
- Network analysis (6 papers)
- Attention economy (1+ papers)
- Public sphere / networked publics (6+ papers)

### Gap Analysis
| Approach | Prior Studies | Status |
|----------|---------------|--------|
| Frame analysis | #MahsaAmini, Ukraine, Belarus, etc. | ✅ Done extensively |
| Hashtag network | Overnight study (crashed) | ⚠️ Attempted |
| Linguistic features | None | ❌ **UNTESTED** |
| Temporal patterns | None | ❌ Untested |
| User-level structure | None | ❌ Untested |

### Selected Novel Direction: **Linguistic Style**

**Rationale:**
1. Connects to attention economy (what grabs attention?)
2. Language-agnostic (works across Persian + English)
3. Testable with LLM annotation (CommDAAF compatible)
4. Theoretically grounded in persuasion research

---

## Phase 2: Research Questions

### RQ1: Rhetorical Style
**What rhetorical styles characterize high-engagement crisis content?**

We code 4 styles (mutually exclusive primary assignment):
| Style | Definition | Example |
|-------|------------|---------|
| **NARRATIVE** | Story-telling, personal account, first-person experience | "I was there when the police attacked..." |
| **ANALYTICAL** | Facts, statistics, cause-effect reasoning | "Since February, 3,000 civilians have been killed..." |
| **APPEAL** | Direct call to action, mobilization, requests | "Share this! Call your representatives!" |
| **EXPRESSIVE** | Emotional expression, solidarity, identity affirmation | "We stand with Ukraine 🇺🇦💔" |

### RQ2: Cross-Context Differences
**Does the engagement-style relationship differ between war and protest discourse?**

- H2a: NARRATIVE will predict engagement in protest (personal stories of victims)
- H2b: ANALYTICAL will predict engagement in war (information-seeking context)

### RQ3: Arousal-Style Interaction
**Does high arousal amplify the effect of rhetorical style on engagement?**

- H3: The style-engagement relationship is moderated by arousal (high arousal + APPEAL > low arousal + APPEAL)

---

## Phase 3: Methodology

### 3.1 Data

**Ukraine (war discourse):**
- Source: `ukraine_june2022_sample.json`
- N: 300 posts
- Fields: text, engagement, followers, language

**MahsaAmini (protest discourse):**
- Source: `coding_batch_*.json` (multiple batches)
- Target N: 300 posts (matched)
- Fields: text, engagement, tier

### 3.2 Coding Scheme

Each post coded for:
| Variable | Values | Coding |
|----------|--------|--------|
| PRIMARY_STYLE | NARRATIVE / ANALYTICAL / APPEAL / EXPRESSIVE | Single choice |
| AROUSAL | low / medium / high | Single choice |
| CONFIDENCE | 0.0-1.0 | Model confidence |

### 3.3 Coding Prompt (CommDAAF)

```markdown
# RHETORICAL STYLE CODING

## TASK
For each text, assign:
1. PRIMARY_STYLE: The dominant rhetorical approach
2. AROUSAL: Emotional intensity level

## STYLE DEFINITIONS

### NARRATIVE
- First-person account or story
- Temporal sequence ("then...", "when...")
- Specific events, people, places
- Experiential focus

**Examples:**
- "I watched the soldiers enter my neighborhood at 3am..."
- "My sister was arrested yesterday. She was just walking home."

**NOT narrative:** General statements, statistics, calls to action

### ANALYTICAL
- Facts, figures, statistics
- Cause-effect reasoning
- Explanations, context-setting
- Third-person, objective tone

**Examples:**
- "Since the invasion began, 4.3 million refugees have fled."
- "The protests started after Mahsa Amini died in police custody on September 16."

**NOT analytical:** Personal stories, emotional appeals, calls to action

### APPEAL
- Direct call to action
- Imperatives ("Share!", "Donate!", "Vote!")
- Requests for help, attention, or action
- Mobilization language

**Examples:**
- "RT this! The world needs to see what's happening!"
- "Call your senator NOW. Demand sanctions."

**NOT appeal:** Informational content, personal stories, emotional expression without action request

### EXPRESSIVE
- Emotional expression (grief, anger, hope, solidarity)
- Identity affirmation
- Symbolic language, emojis
- No story, no facts, no call to action — just feeling

**Examples:**
- "💔🇺🇦 Slava Ukraini"
- "We are all Mahsa. #WomanLifeFreedom"
- "This breaks my heart. No words."

**NOT expressive:** Stories (narrative), facts (analytical), action requests (appeal)

## DECISION HIERARCHY
When multiple styles present:
1. If there's a CALL TO ACTION → APPEAL (dominant)
2. If telling a PERSONAL STORY → NARRATIVE
3. If providing FACTS/STATISTICS → ANALYTICAL
4. If pure EMOTIONAL EXPRESSION → EXPRESSIVE

## AROUSAL LEVELS
- **low**: Calm, matter-of-fact, subdued
- **medium**: Engaged, emphatic, concerned
- **high**: Urgent, intense, alarming, desperate, enraged

## OUTPUT FORMAT
Return JSON array:
[{"id": "...", "style": "...", "arousal": "...", "confidence": 0.0-1.0}]
```

### 3.4 Analysis Plan

1. **Distribution check:** Style × Context crosstab
2. **Diagnostics:** Engagement distribution (expect right-skew → NegBin)
3. **Model 1:** Engagement ~ Style + Context + Style×Context
4. **Model 2:** Add arousal interaction
5. **Effect sizes:** Report IRR with 95% CI

### 3.5 Multi-Model Validation

| Model | Role | Access |
|-------|------|--------|
| Claude | Primary coder | Direct |
| GLM-4.7 | Independent replication | OpenCode `zai-coding-plan/glm-4.7` |
| Kimi K2.5 | Cross-review | OpenCode `kimi-coding/k2p5` |

**Batch sizes:**
- Claude: 50 posts/batch
- GLM: 50 posts/batch
- Kimi: **25 posts/batch** (strict limit)

---

## Phase 4: Execution Plan

- [ ] 4.1 Extract Ukraine sample (n=200)
- [ ] 4.2 Extract MahsaAmini sample (n=200, new posts)
- [ ] 4.3 Create coding batches (25-post Kimi-compatible)
- [ ] 4.4 Claude coding (all batches)
- [ ] 4.5 GLM coding (all batches)
- [ ] 4.6 Kimi coding (all batches)
- [ ] 4.7 Merge and calculate reliability
- [ ] 4.8 Distribution diagnostics
- [ ] 4.9 Regression analysis
- [ ] 4.10 Adversarial peer review
- [ ] 4.11 Final write-up

---

## Phase 5: Expected Contributions

### Theoretical
- Attention economy: What linguistic features capture attention in crisis?
- Context-dependency: War vs protest may reward different styles
- Arousal amplification: Does emotional intensity moderate style effects?

### Methodological
- Rhetorical style coding via LLM (novel for crisis communication)
- 3-model CommDAAF validation applied to linguistic features

### Empirical
- First systematic comparison of rhetorical style and engagement across crisis types
- Actionable insights for crisis communicators

---

*Design complete. Beginning Phase 4 execution.*
