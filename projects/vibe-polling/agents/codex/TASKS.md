# Codex Tasks — VibePoll-2026

**Agent:** Codex (OpenAI)  
**Study:** Vibe Polling  
**Framework:** CommDAAF v1.0  
**Role:** Data Recollection with Realistic Search Terms

---

## ⚠️ CRITICAL: READ BEFORE EXECUTING

**Study Context:**
- Original data collection used 76 search terms, but ~30% had 80-99% zeros (no signal)
- Peer review identified unrealistic academic phrasing as the root cause
- This task: Recollect Google Trends data with colloquial, realistic search terms

**Key Constraints:**
- Google Trends API rate limits apply
- PyTrends library required
- Output must match existing parquet schema for compatibility

---

## Task 0: CommDAAF Activation (MANDATORY)

```
FIRST, read and activate CommDAAF:

1. Read: /root/.openclaw/workspace/skills/commdaaf/SKILL.md
2. Read: /root/.openclaw/workspace/projects/comm-research-skill/agent-academy-study-protocol.md
3. Read: PLAN.md in the project root

Confirm activation by stating exactly:
"CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."
```

---

## Task 1: Review Search Term Critique

Read the peer review findings on search terms:

```
Read: /root/.openclaw/workspace/projects/vibe-polling/SEARCH_TERM_CRITIQUE.md
Read: /root/.openclaw/workspace/projects/vibe-polling/COMPREHENSIVE_PEER_REVIEW.md
```

**Key Issues Identified:**
| Original Term | Problem | Signal |
|---------------|---------|--------|
| `AI taking jobs` | Academic phrasing | 99.7% zeros |
| `US troops Iran` | Nobody searches this | ~0% signal |
| `grocery prices` | Too generic | Low signal |
| `inflation concerns` | Academic jargon | Low signal |

---

## Task 2: Define Realistic Search Terms

⚠️ **UPDATED 2026-03-19 per Reviewer Notes (see REVISION_NOTES_R2.md)**

Create a new term list based on how real people actually search. These terms were validated by the reviewer as HIGH PRIORITY:

### Priority 1: Economy (Colloquial) — HIGHEST SIGNAL EXPECTED
```
why is food so expensive     ← 10x volume vs "grocery prices"
cheap gas near me            ← localized economic behavior  
can't afford rent            ← housing crisis indicator
food bank near me            ← economic distress signal
how to save money 2026       ← anxiety + time-specific
side hustle                  ← gig economy, multiple jobs
apply for food stamps        ← direct assistance seeking
```

### Priority 2: War/Draft Anxiety — HIGH SIGNAL EXPECTED
```
am I going to be drafted     ← direct fear query
draft age 2026               ← specific concern, time-bound
are we going to war with Iran← plain language fear
will there be a draft        ← seeking reassurance
World War 3                  ← catastrophic framing
Iran attack                  ← news-driven
```

### Priority 3: AI/Jobs Anxiety — HIGH SIGNAL EXPECTED
```
will AI take my job          ← real phrasing
is my job safe from AI       ← question format
jobs AI can't replace        ← seeking safe careers
ChatGPT replacing workers    ← news-driven anxiety
AI proof careers             ← career planning
```

### Priority 4: Immigration (Localized) — MEDIUM-HIGH SIGNAL
```
ICE near me                  ← immediate local concern
deportation news             ← current events tracking
immigration lawyer near me   ← action-oriented
immigration news today       ← news-seeking
```

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

**Total new terms:** 23  
**Output:** Save to `data/reference/realistic_terms.json`

---

## Task 3: Collect Google Trends Data

Use PyTrends to collect data for all 13 states:

**States:**
```python
states = ['US-PA', 'US-MI', 'US-WI', 'US-AZ', 'US-GA', 'US-NV', 'US-NC',
          'US-CA', 'US-TX', 'US-OH', 'US-ME', 'US-NH', 'US-MN']
```

**Collection Script Template:**
```python
from pytrends.request import TrendReq
import pandas as pd
import time

pytrends = TrendReq(hl='en-US', tz=360)

# Read realistic terms
with open('data/reference/realistic_terms.json') as f:
    terms = json.load(f)

all_data = []

for state in states:
    for term in terms:
        try:
            pytrends.build_payload([term], geo=state, timeframe='2025-01-01 2026-03-19')
            df = pytrends.interest_over_time()
            if not df.empty:
                df['state'] = state
                df['term'] = term
                all_data.append(df)
            time.sleep(1)  # Rate limit
        except Exception as e:
            print(f"Error: {state}/{term}: {e}")

# Save
result = pd.concat(all_data)
result.to_parquet('data/processed/trends_realistic.parquet')
```

**Output:** `data/processed/trends_realistic.parquet`

---

## Task 4: Validate Data Quality

Run zero-signal check on new data:

```python
# Check for low-signal terms
df = pd.read_parquet('data/processed/trends_realistic.parquet')

zero_pct = df.groupby('term')['interest'].apply(lambda x: (x == 0).sum() / len(x))
print("Terms with >50% zeros (REMOVE):")
print(zero_pct[zero_pct > 0.50])

print("\nTerms with <20% zeros (HIGH SIGNAL):")
print(zero_pct[zero_pct < 0.20])
```

**Acceptance Criteria:**
- ✅ At least 70% of terms have <50% zeros
- ✅ At least 50% of terms have <20% zeros
- ✅ No term has >80% zeros

---

## Task 5: Generate Comparison Report

Compare original vs realistic term collections:

| Metric | Original (Claude Code) | Realistic (Codex) |
|--------|------------------------|-------------------|
| Total records | 75,894 | TBD |
| Unique terms | 76 | ~30 |
| Terms >50% zeros | ~30% | Target <30% |
| Mean signal/term | TBD | TBD |

**Output:** `COLLECTION_REPORT.md`

---

## Task 6: Handoff to Downstream Agents

Create handoff file for Kimi/Gemini to re-run analysis:

```json
{
  "agent": "codex",
  "task": "data_recollection",
  "status": "complete",
  "data_file": "data/processed/trends_realistic.parquet",
  "terms_file": "data/reference/realistic_terms.json",
  "records": TBD,
  "terms_retained": TBD,
  "quality_check": "passed/failed",
  "notes": "Realistic colloquial terms collected per peer review recommendations"
}
```

**Output:** `handoff.json`

---

## Deliverables Checklist

- [ ] `data/reference/realistic_terms.json` — New term list
- [ ] `data/processed/trends_realistic.parquet` — Collected data
- [ ] `scripts/collect_realistic_trends.py` — Collection script
- [ ] `scripts/validate_quality.py` — Quality check script
- [ ] `COLLECTION_REPORT.md` — Comparison report
- [ ] `handoff.json` — Handoff to downstream agents

---

## Directory Structure

```
agents/codex/
├── TASKS.md                    # This file
├── COLLECTION_REPORT.md        # Output: comparison report
├── handoff.json                # Output: handoff to Kimi/Gemini
├── scripts/
│   ├── collect_realistic_trends.py
│   └── validate_quality.py
└── data/
    └── reference/
        └── realistic_terms.json
```

---

*Task file created for Codex by OpenClaw*  
*Framework: CommDAAF v1.0*
