# Codex Agent — VibePoll-2026

**Role:** Data Recollection with Realistic Search Terms  
**Framework:** CommDAAF v1.0  
**Status:** 🟡 Awaiting Execution

## Why Codex?

The peer review identified that ~30% of original search terms had near-zero signal due to unrealistic academic phrasing. Codex's task is to:

1. Define colloquial, realistic search terms
2. Recollect Google Trends data
3. Validate data quality
4. Hand off to Kimi/Gemini for re-analysis

## Quick Start

```bash
# Read tasks
cat agents/codex/TASKS.md

# Or run via Codex CLI (when available)
codex run "$(cat agents/codex/TASKS.md)"
```

## Key Files

| File | Purpose |
|------|---------|
| `TASKS.md` | Full task specification |
| `scripts/collect_realistic_trends.py` | Data collection script |
| `scripts/validate_quality.py` | Quality validation |
| `data/reference/realistic_terms.json` | New term list |
| `COLLECTION_REPORT.md` | Results summary |
| `handoff.json` | Downstream handoff |

## Context

### Original Terms (Problems)
- `AI taking jobs` → 99.7% zeros
- `US troops Iran` → ~0% signal
- `inflation concerns` → academic jargon

### Realistic Terms (Target)
- `why is food so expensive`
- `will AI take my job`
- `are we going to war`
- `gas prices near me`

## Dependencies

- Python 3.9+
- PyTrends (`pip install pytrends`)
- pandas, pyarrow

---

*Created by OpenClaw for VibePoll-2026 study*
