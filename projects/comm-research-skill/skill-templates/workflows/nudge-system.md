# Conscious Research Design: Nudge System

> **"The default is the enemy of rigor."**

This system enforces **conscious decision-making** by making defaults dangerous, visible, and opt-in rather than opt-out.

---

## Core Principle

**No silent defaults.** Every parameter, threshold, and methodological choice must be:

1. **Visible** — Shown to the user, not hidden
2. **Questioned** — "Why this and not alternative X?"
3. **Justified** — Require explicit reasoning
4. **Owned** — User acknowledges "I chose this knowing the risks"

---

## Five Nudge Types

### 1️⃣ Default Danger Flags

When user accepts a default, **interrupt with risk assessment**.

**Example: Topic Modeling**
```
⚠️ DEFAULT ALERT

You're about to use BERTopic with DEFAULT parameters:
• min_topic_size = 10
• embedding_model = 'all-MiniLM-L6-v2'

🚨 DANGER: These defaults may be WRONG because:

1. min_topic_size=10 assumes ~500+ documents
   Your data: [X documents]
   Risk: Too many/few topics

2. 'all-MiniLM-L6-v2' is a GENERAL model
   Your domain: [political/health/etc.]
   Risk: Misaligned embeddings

⛔ Choose based on your data:

[ ] Accept defaults (NOT RECOMMENDED)
    → Justify why defaults fit your context: ___________

[ ] Calibrate for my data (RECOMMENDED)
    → System will guide parameter selection
```

---

### 2️⃣ Active Choice Requirement

**Force explicit decision** at every methodological fork. No "whatever works."

**Example: Network Edge Definition**
```
NETWORK EDGE DEFINITION REQUIRED

❌ "Standard network" is NOT an option.
❌ "Whatever works" is NOT acceptable.

You MUST choose based on your research question:

A. RETWEET NETWORK
   Captures: Information diffusion, amplification
   Misses: Original content, conversation
   Risk: Bots amplify, may not reflect genuine influence

B. MENTION NETWORK
   Captures: Conversation, attention
   Misses: Passive consumption
   Risk: @mention ≠ endorsement

C. SEMANTIC SIMILARITY NETWORK
   Captures: Thematic alignment
   Misses: Explicit interaction
   Risk: Similarity ≠ agreement (may be mockery)

Your research question: _________________________

Your choice: ___

Why this edge type: _________________________

Why NOT the alternatives: _________________________
```

---

### 3️⃣ Trade-Off Visualization

**Force explicit trade-off consideration** with visual matrix.

**Example: Sampling Strategy**
```
SAMPLING TRADE-OFF MATRIX

                    | Coverage | Depth | Speed | Bias Risk |
--------------------|----------|-------|-------|-----------|
Full archive        | ★★★★★    | ★★★★★ | ★☆☆☆☆ | LOW       |
Stratified sample   | ★★★★☆    | ★★★★☆ | ★★★☆☆ | MEDIUM    |
Random sample       | ★★★☆☆    | ★★★☆☆ | ★★★★☆ | MEDIUM    |
Keyword-filtered    | ★★☆☆☆    | ★★★★☆ | ★★★★★ | HIGH      |
Convenience sample  | ★☆☆☆☆    | ★★☆☆☆ | ★★★★★ | VERY HIGH |

⚠️ CONVENIENCE SAMPLING WARNING:
If you choose this, findings are NON-GENERALIZABLE.

Your choice: ___

Justification: _________________________

Alternatives considered and rejected: _________________________
```

---

### 4️⃣ Assumption Audit

**Surface hidden assumptions** before proceeding.

**Example: Pre-Analysis Audit**
```
ASSUMPTION AUDIT: Required Before Proceeding

Check all that apply and provide justification:

DATA ASSUMPTIONS
□ My sample represents the population I claim
  Justification: _________________________

□ Missing data is random (not systematic)
  Evidence: _________________________

□ Platform changes didn't affect behavior
  Verification: _________________________

METHOD ASSUMPTIONS
□ My operationalization captures the concept
  Validation: _________________________

□ Method's statistical assumptions are met
  Diagnostic tests: _________________________

INTERPRETATION ASSUMPTIONS
□ I understand correlation vs. causation
  My position: _________________________

□ Platform effects are acknowledged
  Handling: _________________________

⛔ If you CANNOT justify an assumption:
   → Collect evidence, OR
   → Acknowledge as limitation, OR
   → Change your method
```

---

### 5️⃣ Reflection Checkpoints

**Forced reflection** at key stages.

**Checkpoint: Post-Data Collection**
```
DATA COLLECTION COMPLETE — Reflect:

1. What surprised you about the data?
   _________________________

2. What was harder than expected?
   _________________________

3. How might collection choices shape the data?
   _________________________

⚠️ If you can't answer #3, you're not ready to analyze.
```

**Checkpoint: Post-Analysis**
```
INITIAL ANALYSIS COMPLETE — Reflect:

1. What patterns did you EXPECT?
   Expected: _________________________
   Found: _________________________

2. What was SURPRISING?
   _________________________

3. What ALTERNATIVE EXPLANATIONS exist?
   Alternative 1: _________________________
   Alternative 2: _________________________

4. What would DISPROVE your interpretation?
   _________________________

⛔ If you have no alternative explanations,
   you're not thinking critically.
```

**Checkpoint: Pre-Writing**
```
READY TO WRITE RESULTS?

For each key finding:

Finding: _________________________

Strength of evidence:
□ Strong (multiple converging lines)
□ Moderate (single strong line)
□ Weak (suggestive only)

Limitations: _________________________

Alternative interpretations to address: _________________________

□ I can defend this finding against skeptical reviewers
```

---

## Implementation

### In Every Method Skill

Add this section:

```markdown
## ⚠️ Conscious Choice Required

### Default Alert
[Why defaults are dangerous for this method]

### Your Options
[Present alternatives with trade-offs]

### Required Justification
I choose: ___
Reasoning: _________________________
Alternatives rejected: _________________________

### Assumption Audit
□ I understand what this choice assumes
□ I can justify or acknowledge each assumption
□ I know how to test if assumptions are violated
```

### Escalation Protocol

When user gives vague answers:

| Level | Trigger | Response |
|-------|---------|----------|
| 1 | Vague answer | Gentle probe: "Can you be more specific?" |
| 2 | Still vague | Explain stakes: "I need this because..." |
| 3 | Pushback | Challenge: "This won't produce valid results because..." |
| 4 | Insists | Refuse: "I can't proceed without [requirement]" |

---

## What This Produces

### Before Nudge System
- "Just run the analysis"
- Click, click, done
- Results appear magically
- Low confidence in methodology
- "The system said..."

### After Nudge System
- "I must design this analysis"
- Thoughtful choices at each stage
- Clear understanding of limitations
- High confidence in defensibility
- "I chose X because..."

---

## User Experience Goals

This should feel like:
- A rigorous methods course compressed
- A thoughtful collaborator pushing back
- Documentation that writes itself
- Insurance against Reviewer 2

This should NOT feel like:
- A bureaucratic checklist
- Punishment for wanting help
- Gatekeeping
- Busywork

---

## Success Metrics

A successful nudge produces:
- ✅ Explicit decision records for every key choice
- ✅ Written justifications (usable in methods section)
- ✅ Alternative consideration documented
- ✅ Assumptions surfaced and addressed
- ✅ Limitations acknowledged before claims

**The output should be defensible in a dissertation defense.**

---

*Conscious Research Design | CommDAAF v0.3*
