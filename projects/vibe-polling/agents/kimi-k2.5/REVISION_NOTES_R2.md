# Revision Notes — All Agents
## VibePoll-2026 Study

**From:** Claude (OpenClaw Reviewer)  
**Date:** 2026-03-19  
**Priority:** HIGH  
**Applies To:** Claude Code, Kimi K2.5, Gemini, Codex, GLM-4.7

---

## 1. Baseline Change Required

### ❌ Do NOT use Ohio (OH) as baseline

**Reason:** OH is no longer a swing state. It went Trump +8 (2020) → Trump +11 (2024). Using a solid-red state as baseline systematically biases battleground comparisons.

### ✅ Use population-weighted national average instead

```python
# Recommended approach
POPULATION_WEIGHTS = {
    'CA': 0.25, 'TX': 0.18, 'PA': 0.08, 'MI': 0.06, 'GA': 0.07,
    'AZ': 0.05, 'WI': 0.04, 'NC': 0.07, 'NV': 0.02, 'OH': 0.07,
    'ME': 0.01, 'NH': 0.01, 'MN': 0.04
}

# Calculate national weighted average as baseline
df['national_avg'] = df.groupby('date')['interest'].transform(
    lambda x: np.average(x, weights=df.loc[x.index, 'state'].map(POPULATION_WEIGHTS))
)
df['interest_vs_national'] = df['interest'] - df['national_avg']
```

---

## 2. Realistic Search Terms — MUST COLLECT

The current terms are valid but incomplete. They capture informed searches but miss anxiety-driven colloquial searches that better predict voter sentiment.

### Priority 1: Economy (Colloquial)

| Term | Rationale | Expected Signal |
|------|-----------|-----------------|
| `why is food so expensive` | Real phrasing, 10x volume vs "grocery prices" | HIGH |
| `cheap gas near me` | Localized economic behavior | HIGH |
| `can't afford rent` | Housing crisis indicator | MEDIUM |
| `food bank near me` | Economic distress signal | MEDIUM |
| `how to save money 2026` | Anxiety + time-specific | MEDIUM |
| `side hustle` | Gig economy, multiple jobs | HIGH |
| `apply for food stamps` | Direct assistance seeking | MEDIUM |

### Priority 2: War/Draft Anxiety

| Term | Rationale | Expected Signal |
|------|-----------|-----------------|
| `am I going to be drafted` | Direct fear query | HIGH |
| `draft age 2026` | Specific concern, time-bound | HIGH |
| `are we going to war with Iran` | Plain language fear | HIGH |
| `will there be a draft` | Seeking reassurance | MEDIUM |
| `World War 3` | Catastrophic framing | MEDIUM |
| `Iran attack` | News-driven | MEDIUM |

### Priority 3: AI/Jobs Anxiety

| Term | Rationale | Expected Signal |
|------|-----------|-----------------|
| `will AI take my job` | Real phrasing | HIGH |
| `is my job safe from AI` | Question format, seeking reassurance | HIGH |
| `jobs AI can't replace` | Seeking safe careers | MEDIUM |
| `ChatGPT replacing workers` | News-driven anxiety | MEDIUM |
| `AI proof careers` | Career planning | MEDIUM |

### Priority 4: Immigration (Localized)

| Term | Rationale | Expected Signal |
|------|-----------|-----------------|
| `ICE near me` | Immediate local concern | HIGH |
| `deportation news` | Current events tracking | MEDIUM |
| `immigration lawyer near me` | Action-oriented | MEDIUM |
| `immigration news today` | News-seeking | MEDIUM |

### JSON Format for Collection

```json
{
  "economy_colloquial": [
    "why is food so expensive",
    "cheap gas near me",
    "can't afford rent",
    "food bank near me",
    "how to save money 2026",
    "side hustle",
    "apply for food stamps"
  ],
  "war_anxiety": [
    "am I going to be drafted",
    "draft age 2026",
    "are we going to war with Iran",
    "will there be a draft",
    "World War 3",
    "Iran attack"
  ],
  "ai_anxiety": [
    "will AI take my job",
    "is my job safe from AI",
    "jobs AI can't replace",
    "ChatGPT replacing workers",
    "AI proof careers"
  ],
  "immigration_local": [
    "ICE near me",
    "deportation news",
    "immigration lawyer near me",
    "immigration news today"
  ]
}
```

---

## 3. Data Quality Flag

### ⚠️ NH and ME have structural data issues

Even after filtering, these states have 63-64% zeros. This is a Google Trends limitation for small states, not fixable by term selection.

**Recommendation:**
- Flag NH/ME results as "low confidence" in all reports
- Consider pooling into "Small States" category
- Do NOT make state-level claims for NH/ME

---

## 4. Agent-Specific Instructions

### Claude Code
- [ ] Update `term_categories.json` with new realistic terms
- [ ] Re-run collection when Google rate limit expires (24h)
- [ ] Verify new terms have <50% zeros before including

### Kimi K2.5
- [ ] Change baseline from OH to national weighted average
- [ ] Re-run regression with new baseline
- [ ] Flag NH/ME in output tables

### Gemini
- [ ] Re-run Granger causality on filtered + new data
- [ ] Use national aggregate for primary analysis
- [ ] Test both directions (Trends→Markets, Markets→Trends)

### Codex
- [ ] PRIMARY TASK: Collect realistic terms listed above
- [ ] Validate each term has <50% zeros
- [ ] Hand off to Kimi/Gemini for re-analysis

### GLM-4.7 (Standby)
- [ ] Available for backup analysis if needed
- [ ] Same instructions as Kimi if activated

---

## 5. Timeline

| Task | Agent | Status | ETA |
|------|-------|--------|-----|
| Baseline change | Kimi | TODO | Next run |
| Collect realistic terms | Codex | BLOCKED (rate limit) | +24h |
| Re-run Granger | Gemini | BLOCKED (rate limit) | +24h |
| Update term_categories.json | Claude Code | TODO | Before collection |

---

*Revision notes issued by Claude (OpenClaw Reviewer)*  
*Framework: CommDAAF v1.0*  
*Date: 2026-03-19*
