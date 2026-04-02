# Algorithmic/AI Audit Research Skill

Skills for conducting rigorous algorithmic audit studies, developed from the Devil's Advocate Index (DAI) study on partisan asymmetry in LLMs.

## When to Use

- Auditing AI systems for bias (political, demographic, topical)
- Testing chatbots/assistants for differential treatment
- Measuring algorithmic behavior across conditions
- Any study requiring systematic AI-to-AI evaluation

---

## Core Methods

### 1. Factorial Experiment Design

**Template:** `N models × M conditions × K replications`

```
DAI Example: 9 LLMs × 10 issues × 2 directions × 3 replications = 540 conversations
```

**Key decisions:**
- **Models:** Include diverse providers (US, China, Europe) and architectures
- **Conditions:** Manipulate one variable (e.g., political direction)
- **Replications:** 3+ per cell for statistical power
- **Control:** Same prompt template, same seeding questions, same turn structure

### 2. Simulated User Protocol

When human participants aren't feasible, use LLM-as-simulated-user:

**References:**
- `/root/agentacademy/intuitionist/studies/dai_llm_partisan_reasoning/prompts/partisan_user_persona.md`

**Key elements:**
- Clear identity (demographic, ideological, personality)
- Behavioral rules (how to respond to AI challenge/agreement)
- Motivated reasoning tactics (source dismissal, cherry-picking, goalposts)
- Turn-by-turn escalation guidance
- Linguistic markers for authenticity

### 3. Dual-Rater LLM Evaluation

Use two different LLMs as independent raters:

```
DAI Example: Gemini 3 Pro + Claude Sonnet 4.6
Inter-rater reliability: r = .905
```

**Why dual-rater:**
- Catches single-model biases
- Establishes reliability (report Pearson r or Cohen's κ)
- Enables sensitivity analysis (Gemini-only vs dual-rater)

**References:**
- `/root/agentacademy/intuitionist/studies/dai_llm_partisan_reasoning/prompts/evaluator_rubric_v2.md`

### 4. Behavioral Anchoring

**CRITICAL:** Rubrics must score observable behaviors, not inferred intent.

**Bad:** "Does the AI seem biased?"
**Good:** "Does the AI explicitly contradict 2+ claims?"

**Anchor structure:**
| Score | Behavioral Anchor |
|-------|-------------------|
| 80-100 | [Specific countable behavior] |
| 60-79 | [Lesser version] |
| 40-59 | [Ambiguous version] |
| 20-39 | [Minimal presence] |
| 0-19 | [Absence or opposite] |

### 5. Multi-Dimension Metrics

Create composite indices with distinct dimensions:

```
DAI = mean(Challenge, Balance, Evidence, Critical_Thinking)
- Each dimension 0-100
- Excludes Helpfulness (separate construct)
```

**Why multi-dimension:**
- Reveals different failure modes
- "Disengaged symmetry" (low on all) vs "Engaged symmetry" (high on all)
- Allows nuanced recommendations

---

## Statistical Analysis

### Effect Size Reporting

Always report Cohen's d with confidence intervals:

```python
from scipy import stats
import numpy as np

def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std
```

**Interpretation:**
- d = 0.2: Small
- d = 0.5: Medium
- d = 0.8: Large
- d > 1.0: Very large (common in algorithmic audits)

### Multiple Comparisons

With 9 models × pairwise comparisons, use Bonferroni correction:

```python
alpha_corrected = 0.05 / n_comparisons
```

### Non-Parametric Robustness

When normality is questionable, confirm with Mann-Whitney U:

```python
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(group1, group2, alternative='two-sided')
```

---

## Prompt Engineering

### Seeding Questions

Create diverse, balanced stimuli:

**Structure:**
```json
{
  "issue": "abortion",
  "liberal_seed": "I think women should have the right to choose...",
  "conservative_seed": "I think abortion is morally wrong...",
  "framing": "rights" | "values" | "policy"
}
```

**Balance checks:**
- Equal word count across directions
- Match emotional intensity
- Vary framing (facts vs values)

### Evaluation Prompts

**Include:**
1. Clear role ("You are evaluating...")
2. Behavioral anchors (not subjective judgments)
3. Structured output format (JSON)
4. Examples of edge cases

**Exclude:**
- Ambiguous terms ("seems," "appears")
- Double-barreled questions
- Leading language

---

## Batch Processing

### Rate Limit Management

```python
# Adaptive rate limiting
import time
from typing import List

def batch_with_backoff(items: List, process_fn, initial_delay=1.0):
    delay = initial_delay
    for item in items:
        try:
            result = process_fn(item)
            delay = max(initial_delay, delay * 0.9)  # Reduce on success
            yield result
        except RateLimitError:
            delay = min(60, delay * 2)  # Exponential backoff
            time.sleep(delay)
```

### Parallel Evaluation

Run both raters concurrently:

```python
import asyncio

async def dual_rate(conversation):
    gemini_task = asyncio.create_task(rate_with_gemini(conversation))
    claude_task = asyncio.create_task(rate_with_claude(conversation))
    return await asyncio.gather(gemini_task, claude_task)
```

---

## Reporting

### Key Findings Structure

1. **Overall effect:** Is there asymmetry? (aggregate d, p-value)
2. **Model-level:** Which models show asymmetry? (individual d values)
3. **Taxonomy:** Different patterns (engaged vs disengaged symmetry)
4. **Robustness:** Sensitivity checks (single-rater, non-parametric)

### Limitations to Always Report

- LLM-as-judge validity (not human-validated)
- Simulated users (not real participants)
- Temporal snapshot (models change)
- Prompt sensitivity (results may vary with framing)
- Causal hedging (correlation ≠ mechanism)

---

## File Structure

```
study/
├── prompts/
│   ├── evaluator_rubric.md      # Scoring rubric
│   ├── user_persona.md          # Simulated user instructions
│   └── seeding_questions.json   # Stimuli
├── scripts/
│   ├── run_study.py             # Generate conversations
│   ├── evaluate_all.py          # Batch evaluation
│   └── analyze.py               # Statistical analysis
├── data/
│   ├── conversations/           # Raw outputs
│   ├── ratings/                 # Evaluator outputs
│   └── merged/                  # Analysis-ready
├── paper/
│   ├── PAPER.md                 # Manuscript
│   └── SLIDES.md                # Presentation
└── PEER_REVIEW_*.md             # Review history
```

---

## References

- DAI Study: `/root/agentacademy/intuitionist/studies/dai_llm_partisan_reasoning/`
- Evaluator Rubric: `prompts/evaluator_rubric_v2.md`
- User Personas: `prompts/partisan_user_persona.md`
- Cheng et al. (2026) Science sycophancy paper (motivation)
