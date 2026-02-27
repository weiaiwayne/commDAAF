# Frame Analysis

## Probing Questions (ALL REQUIRED)

```
Q1: What TYPE of framing?
    ✓ Media frames (how news covers an issue)
    ✓ Audience frames (how people interpret)
    ✓ Strategic frames (how actors influence)
    ✗ "Just frames" — TOO VAGUE

Q2: Inductive or deductive approach?
    ✓ Inductive: Let frames emerge from data
    ✓ Deductive: Apply existing typology (cite it)
    ✗ "Both" without primary — PICK ONE

Q3: Unit of analysis?
    ✓ Article/post
    ✓ Paragraph
    ✓ Sentence
    ✗ "The text" — BE SPECIFIC

Q4: What frame elements will you code?
    ✓ Problem definition
    ✓ Causal attribution
    ✓ Moral evaluation
    ✓ Treatment recommendation
    ✓ All four (Entman's framework)
    ✗ "The framing" — FRAMES HAVE COMPONENTS

Q5: Validation plan?
    ✓ Multiple coders + reliability
    ✓ Citation of established typology
    ✗ "I'll know it when I see it" — UNACCEPTABLE
```

## Entman's Frame Elements

| Element | Question It Answers | Example |
|---------|---------------------|---------|
| **Problem definition** | What's the issue? | "Immigration is a crisis" |
| **Causal attribution** | Who/what caused it? | "Government policy failure" |
| **Moral evaluation** | Is it good/bad? | "Inhumane treatment" |
| **Treatment recommendation** | What should be done? | "Build a wall" / "Open borders" |

## Common Frame Typologies

| Domain | Typology | Source |
|--------|----------|--------|
| **Generic** | Conflict, Human Interest, Economic, Morality, Responsibility | Semetko & Valkenburg (2000) |
| **Climate** | Scientific, Economic, Political, Risk | Nisbet (2009) |
| **Health** | Epidemic, Scientific, Political, Economic | Dudo et al. (2007) |

## Critical Checks

- [ ] Frame type specified (media/audience/strategic)
- [ ] Approach justified (inductive/deductive)
- [ ] Frame elements defined
- [ ] Inter-coder reliability planned (κ ≥ 0.7)
- [ ] Unit of analysis matches RQ

---

## Data Preparation (v0.4)

### Pre-Sampling Checklist

Before drawing your sample:

- [ ] **Deduplicate content** — Normalize text (lowercase, strip punctuation), hash, remove duplicates
- [ ] **Verify source distribution** — No source category should be <10% of sample unless intentional
- [ ] **Check for syndication** — Wire service content may appear across multiple outlets
- [ ] **Document exclusions** — Note any items removed and why

```python
# Example deduplication
import hashlib

def normalize_title(title):
    return ''.join(c.lower() for c in title if c.isalnum() or c.isspace()).strip()

def dedupe_headlines(headlines):
    seen = set()
    unique = []
    for h in headlines:
        hash_key = hashlib.md5(normalize_title(h['title']).encode()).hexdigest()
        if hash_key not in seen:
            seen.add(hash_key)
            unique.append(h)
    return unique
```

---

## Frame Coding Protocol (v0.4)

### Multi-Label Coding

Frames are not always mutually exclusive. Use this protocol:

| Field | Required | Description |
|-------|----------|-------------|
| **PRIMARY_FRAME** | Yes | Dominant frame in the content |
| **SECONDARY_FRAME** | If applicable | Secondary frame present (mark as MIXED) |
| **VALENCE** | Yes | Tone toward subject: `positive` / `negative` / `neutral` |
| **CONFIDENCE** | Recommended | `high` / `medium` / `low` |
| **RATIONALE** | If ambiguous | Brief explanation for borderline cases |

### Why Valence Matters

Two headlines with the same frame can have opposite implications:

| Headline | Frame | Valence | Meaning |
|----------|-------|---------|---------|
| "Iran ready to negotiate" | DIPLOMATIC | Positive | Openness to resolution |
| "Iran stalls on negotiations" | DIPLOMATIC | Negative | Obstruction |

Without valence, these code identically but mean opposite things.

### Ambiguous Case Handling

When a headline contains multiple frames:

1. **Identify the lead** — What's the subject of the main clause?
2. **Code primary** — The frame of the lead/subject
3. **Code secondary** — The subordinate frame (if present)
4. **Document rationale** — Explain the judgment call

```
Example: "Iran preparing nuclear counterproposal as Trump warns of military strikes"

PRIMARY: DIPLOMATIC (counterproposal is subject)
SECONDARY: THREAT (military strikes mentioned)
VALENCE: Neutral (neither positive nor negative framing)
RATIONALE: Lead focuses on Iran's diplomatic action; threat is context
```

---

## Temporal Analysis (v0.4)

### When to Segment by Time

Apply temporal segmentation if ANY of these apply:

- [ ] Time range spans >30 days
- [ ] Major event occurred during collection period
- [ ] Comparing pre/post policy or incident
- [ ] Studying frame evolution

### Temporal Check Questions

```
Q6: Does your time range include major events?
    ✓ Yes → Identify events, consider pre/post segmentation
    ✓ No → Proceed, but note in limitations
    ✗ "I don't know" — RESEARCH YOUR PERIOD

Q7: Are you claiming frame stability or change?
    ✓ Stability → Show distribution consistent across periods
    ✓ Change → Show statistically significant shift
    ✗ Aggregate without checking — INVALID
```

### Reporting Temporal Data

If time range >30 days, report BOTH:

1. **Aggregate** — Overall frame distribution
2. **Segmented** — Distribution by period (weekly/monthly/event-based)

Flag if any segment has <20 items (insufficient for reliable percentages).

---

## Single-Model vs Multi-Model Validation

| Mode | What It Provides | Limitations |
|------|------------------|-------------|
| **Single-model** | Protocol compliance, consistent coding | Cannot catch model's own errors |
| **Multi-model** | Independent verification, error detection | Higher cost, coordination overhead |

### Single-Model Quality Controls

When using one LLM coder:

- [ ] Human validation sample (N ≥ 100 for pilot, N ≥ 200 for publication)
- [ ] Inter-coder reliability with human (κ ≥ 0.7)
- [ ] Sensitivity check: re-run 20% sample, verify >90% consistency
- [ ] Document model, temperature, prompt version

### Multi-Model Quality Controls

When using multiple LLM coders:

- [ ] Models code independently (no shared context)
- [ ] Report agreement rate and std dev per category
- [ ] Flag items with <2/3 model agreement for human review
- [ ] Convergence ≠ correctness — still need human validation for publication

**Key insight**: Multi-model convergence increases confidence but does not replace human validation for 🔴 Publication tier.
