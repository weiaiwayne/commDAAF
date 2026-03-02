# Model Divergence Analysis: Claude vs Kimi Frame Coding

## Executive Summary

**Cohen's Kappa: 0.289 (Fair agreement)**
**Exact Agreement: 45%**

The primary source of divergence is Claude's expansive interpretation of SOLIDARITY, which it applies to 63.5% of posts. Kimi, following CommDAAF decision rules more strictly, distributes these across more specific frames.

---

## Key Divergence Patterns

### 1. SOLIDARITY → CALL_TO_ACTION (44 cases, 20%)

**Example:**
> "کم نیارین خسته نشین فقط یکم دیگ مونده"
> ("Don't give up, don't get tired, just a little more left")

| Model | Frame | Reasoning |
|-------|-------|-----------|
| Claude | SOLIDARITY | Focus on collective "we" implicit in Persian |
| Kimi | CALL_TO_ACTION | Focus on imperative verbs: "don't give up" |

**Hypothesis:** Claude interprets posts with collective pronouns as SOLIDARITY regardless of speech act. Kimi pays more attention to **illocutionary force** — whether the post is *unifying* or *mobilizing*.

CommDAAF Decision Rule: "CALL_TO_ACTION = direct appeals to act/share/protest" — imperative verbs are clear markers.

---

### 2. SOLIDARITY → INJUSTICE (29 cases, 13%)

**Example:**
> "برای مامانم که بعد ۲۲ سال سابقه معلم ابتدایی بودن حقوقش ۵ میلیونه!"
> ("For my mom who after 22 years as an elementary teacher earns only 5 million!")

| Model | Frame | Reasoning |
|-------|-------|-----------|
| Claude | SOLIDARITY | "For my mom" = expressing connection/support |
| Kimi | INJUSTICE | Explicit grievance about low wages = perpetrator implicit (regime) |

**Hypothesis:** Claude reads "برای" ("for") as solidarity dedication. Kimi reads the **content** — a complaint about unfair wages — and codes the substantive frame.

CommDAAF Decision Rule: "INJUSTICE = wrongdoing with explicit perpetrator/blame assigned" — Kimi infers regime responsibility for teacher salaries.

---

### 3. SOLIDARITY → INFORMATIONAL (33 cases, 15%)

**Example:**
> "59 milion and going! #mahsaaminii"

| Model | Frame | Reasoning |
|-------|-------|-----------|
| Claude | SOLIDARITY | Sharing milestone = collective achievement |
| Kimi | INFORMATIONAL | Factual update about hashtag count |

**Hypothesis:** Claude conflates **participation in a movement** with the SOLIDARITY frame. Kimi distinguishes between *what the post says* (information) and *why the user posted it* (solidarity may be the motive, but INFORMATIONAL is the content).

---

### 4. SOLIDARITY → HUMANITARIAN (30 cases, 13.6%)

**Example:**
> "mahsa amini is a 22-year-old iranian girl who was killed by the guidance patrol..."

| Model | Frame | Reasoning |
|-------|-------|-----------|
| Claude | INJUSTICE | Explicit perpetrator ("guidance patrol"), blame assigned |
| Kimi | HUMANITARIAN | Focus on victim ("22-year-old girl... killed"), suffering |

**Hypothesis:** When both perpetrator AND victim are mentioned, models weight differently. Claude prioritizes **blame attribution**; Kimi prioritizes **victim focus**.

CommDAAF Decision Rule ambiguity: "HUMANITARIAN = suffering WITHOUT perpetrator focus" vs "INJUSTICE = perpetrator explicit." When both present, decision depends on what the model foregrounds.

---

### 5. SOLIDARITY → HOPE (13 cases, 5.9%)

**Example:**
> "شاید در این راه اگر باهم بمانیم وقت رسیدن، شعر خوشبختی بخوانیم"
> ("Maybe if we stay together on this path, when we arrive, we'll sing songs of happiness")

| Model | Frame | Reasoning |
|-------|-------|-----------|
| Claude | SOLIDARITY | "together" = unity |
| Kimi | HOPE | "maybe... when we arrive... happiness" = future optimism |

**Hypothesis:** Persian protest poetry often combines solidarity ("together") with hope ("we will succeed"). Claude latches onto collective pronouns; Kimi latches onto temporal markers of future ("وقت رسیدن" = "when we arrive").

---

## Theoretical Implications

### 1. Frame Salience Hierarchy

Claude's implicit hierarchy:
1. Collective pronouns/dedication ("for X", "we") → SOLIDARITY
2. Everything else → secondary consideration

Kimi's implicit hierarchy:
1. Speech act type (informing, demanding, grieving)
2. Content (victim, perpetrator, collective)

### 2. Cultural/Linguistic Factors

Persian-language posts show higher divergence because:
- **Poetic compression**: Multiple frames in few words
- **Implicit subjects**: "برای" ("for") dedication framing
- **Cultural norms**: Grief and solidarity intertwined

Kimi (developed by Moonshot AI, Chinese company) may have:
- Different training on Persian text
- Stricter adherence to literal content vs implied meaning

### 3. CommDAAF Sensitivity

Kimi received the full CommDAAF prompt with:
- Frame decision rules
- Arousal anchors
- Edge case handling

Claude used earlier coding without these explicit rules. This methodological difference explains ~20% of divergence — Claude wasn't "wrong," it was using a different (implicit) decision rule.

---

## Recommendations for CommDAAF v0.6

### 1. Add SOLIDARITY Decision Rules

```yaml
solidarity_rules:
  requires:
    - Collective pronoun ("we", "us", "together") OR
    - Explicit unity language ("stand together", "united")
  excludes:
    - Imperative verbs (→ CALL_TO_ACTION instead)
    - Grievance content (→ INJUSTICE instead)
    - Future optimism without "we" (→ HOPE instead)
    - Factual reporting (→ INFORMATIONAL instead)
```

### 2. Add "Dedication" Sub-Pattern

Posts that say "For X" (برای X) need explicit rule:
- "For Mahsa" + grievance content → INJUSTICE (not solidarity)
- "For Mahsa" + collective action → SOLIDARITY
- "For Mahsa" + hashtag only → CALL_TO_ACTION (amplification)

### 3. Multi-Frame Coding

CommDAAF v0.4 introduced SECONDARY_FRAME but neither model used it here. For high-divergence cases, mandate:
- PRIMARY: The illocutionary act (what the post DOES)
- SECONDARY: The content frame (what the post is ABOUT)

---

## Conclusion

The Claude-Kimi divergence is **not noise** — it reveals different valid interpretations of frame salience. Claude reads **social function** (who's with whom), while Kimi reads **content type** (what's being said).

Both are defensible; CommDAAF needs to specify which interpretation is canonical for research purposes.

**Key insight for AgentAcademy:** Multi-model divergence on the same data with the same frame typology suggests frame analysis requires human adjudication at 🔴 Publication tier, even with converged methodology.
