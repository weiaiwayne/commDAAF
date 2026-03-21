# Claude Code Tasks — VibePoll-2026

**For:** Wayne (human operator running Claude Code)  
**Study:** Vibe Polling  
**Framework:** CommDAAF v1.0  

---

## Instructions for Wayne

Copy the prompts below into Claude Code. Each task is self-contained. Run them in order.

---

## Task 1: Setup & CommDAAF Activation

```
Read the file PLAN.md in this directory.

Then read and activate CommDAAF:
1. Read: /root/.openclaw/workspace/skills/commdaaf/SKILL.md
2. Read: /root/.openclaw/workspace/projects/comm-research-skill/agent-academy-study-protocol.md

Confirm activation by stating:
"CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."

Then create the full directory structure as specified in PLAN.md Section 14.
```

---

## Task 2: Search Term Validation (CRITICAL)

```
⚠️ CRITICAL TASK — READ CAREFULLY

Review the search terms in PLAN.md Section 6 and in:
/root/.openclaw/workspace/projects/vibe-polling/data/reference/term_categories.json

For each category, validate that terms are REALISTIC:
- Would a real person type this into Google at 11pm?
- NO academic jargon allowed

Spot-check 5-10 terms on Google Trends (manually or via pytrends) to verify:
1. The term has actual search volume
2. The term shows variation over time (not flat)

Create a validation report:
- List any terms you're removing (with reason)
- List any terms you're modifying (original → new)
- List any new terms you're adding (with justification)

Save to: agents/claude-code/search_term_validation.md
```

---

## Task 3: Implement Data Collection Scripts

```
Implement the data collection scripts from PLAN.md Section 7:

1. scripts/collect_trends.py
   - Use pytrends library
   - Collect for all states in data/reference/state_codes.json
   - Collect all terms in data/reference/term_categories.json
   - Handle rate limiting (2-5 second delays)
   - Save to data/raw/trends/trends_YYYY-MM-DD.parquet

2. scripts/collect_markets.py
   - Polymarket API: gamma-api.polymarket.com
   - Kalshi API (if accessible)
   - Save to data/raw/markets/markets_YYYY-MM-DD.json

3. scripts/collect_polls.py
   - Scrape RealClearPolitics generic ballot
   - Scrape 270toWin state ratings
   - Save to data/raw/polls/polls_YYYY-MM-DD.json

Test each script on a small sample before full run.
Log any issues to logs/collection_log.txt.
```

---

## Task 4: Run Data Collection

```
Execute the data collection scripts:

1. Run collect_trends.py for all states and terms
2. Run collect_markets.py
3. Run collect_polls.py

Verify data completeness:
- All 13 states collected?
- All term categories collected?
- No missing dates?

Generate initial summary:
- Total records per state
- Date range covered
- Any errors or gaps

Save summary to: agents/claude-code/collection_summary.md
```

---

## Task 5: Data Processing & Cleaning

```
Process the raw data:

1. Load all trends data from data/raw/trends/
2. Handle missing values (document decisions)
3. Normalize search volumes:
   - Z-score within each term across time
   - Z-score within each state across terms
4. Calculate engagement tiers if applicable

Document ALL transformations with rationale (CommDAAF transparency requirement).

Save processed data to:
- data/processed/trends_normalized.parquet
- data/processed/processing_log.md
```

---

## Task 6: Descriptive Analysis & Visualization

```
Generate descriptive analyses:

1. Heatmap: States × Issue Categories (average salience)
   - Save to outputs/figures/state_issue_heatmap.png

2. Time series: Top 5 terms over time
   - Annotate major events (Iran war start, Epstein release, etc.)
   - Save to outputs/figures/term_timeseries.png

3. State comparison: Battleground vs Control states
   - Save to outputs/figures/battleground_vs_control.png

4. Calculate Issue Salience Index per state per week
   - Use weights from PLAN.md Section 8.3
   - Save to data/processed/issue_salience.csv

5. Build Vibe Index per state
   - Weighted composite per PLAN.md Section 8.4
   - Save to data/processed/vibe_indices.csv

All figures must include:
- Clear titles and labels
- Legends
- Source notes
- Date of data collection
```

---

## Task 7: Prepare Handoff for Other Agents

```
Prepare data files for GLM and Kimi agents:

1. Copy processed data to shared location:
   - data/processed/trends_normalized.parquet
   - data/processed/vibe_indices.csv
   - data/raw/markets/*.json
   - data/raw/polls/*.json

2. Create handoff summary:
   - What data is available
   - What processing was done
   - Any data quality issues to note
   - Recommended next steps

Save to: agents/claude-code/handoff_summary.md

This completes Claude Code's primary tasks. 
GLM will handle correlation analysis.
Kimi will handle statistical modeling.
```

---

## Outputs Checklist

After completing all tasks, verify these files exist:

```
agents/claude-code/
├── search_term_validation.md
├── collection_summary.md
└── handoff_summary.md

data/
├── raw/
│   ├── trends/trends_*.parquet
│   ├── markets/markets_*.json
│   └── polls/polls_*.json
├── processed/
│   ├── trends_normalized.parquet
│   ├── issue_salience.csv
│   ├── vibe_indices.csv
│   └── processing_log.md

outputs/figures/
├── state_issue_heatmap.png
├── term_timeseries.png
└── battleground_vs_control.png

scripts/
├── collect_trends.py
├── collect_markets.py
└── collect_polls.py

logs/
└── collection_log.txt
```

---

## Notes for Wayne

- Run tasks sequentially (1 → 7)
- Task 2 (search term validation) is most critical — bad terms = invalid study
- If pytrends fails, manual CSV export from Google Trends is acceptable
- Polymarket API is free and doesn't require auth
- After Task 7, hand off to GLM and Kimi agents
