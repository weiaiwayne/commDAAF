# Full Research Pipeline Workflow

## Overview

Nine-stage workflow from research question to published report.
Based on DAAF methodology, adapted for communication research.

## Stage Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        FULL PIPELINE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │ STAGE 1  │──▶│ STAGE 2  │──▶│ STAGE 3  │   SETUP & SCOPING   │
│  │  Scope   │   │ Discovery│   │ Planning │                     │
│  └──────────┘   └──────────┘   └──────────┘                     │
│       │              │              │                            │
│       ▼              ▼              ▼                            │
│  [CHECKPOINT 1: Scope approved]                                  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │ STAGE 4  │──▶│ STAGE 5  │──▶│ STAGE 6  │   DATA WORK         │
│  │Acquisition│  │Preprocess│   │ Archive  │                     │
│  └──────────┘   └──────────┘   └──────────┘                     │
│       │              │              │                            │
│       ▼              ▼              ▼                            │
│  [CHECKPOINT 2: Data quality validated]                          │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │ STAGE 7  │──▶│ STAGE 8  │──▶│ STAGE 9  │   ANALYSIS & OUTPUT │
│  │ Analysis │   │Synthesis │   │ Delivery │                     │
│  └──────────┘   └──────────┘   └──────────┘                     │
│       │              │              │                            │
│       ▼              ▼              ▼                            │
│  [CHECKPOINT 3: Report reviewed]                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Stage 1: Scoping

**Objective:** Define research question, scope, and constraints.

**Inputs:**
- User's research request
- Domain context

**Outputs:**
- Clear research question
- Scope boundaries (platforms, time, populations)
- Success criteria
- Ethical considerations noted

**Agent:** Orchestrator (Claude Opus)

**Template:**
```markdown
## Research Question
[1-2 sentences, clear and answerable]

## Scope
- **Platforms:** [e.g., Reddit, Telegram]
- **Time period:** [e.g., Jan 2024 - Dec 2024]
- **Population:** [e.g., Pro-government channels in Russia]
- **Sample:** [e.g., Top 50 channels by subscribers]

## Deliverables
- [ ] Descriptive statistics
- [ ] Network visualization
- [ ] Coordination analysis
- [ ] Written report

## Constraints
- **Timeline:** [hours/days]
- **Budget:** [API costs, compute]
- **Ethics:** [IRB status, consent]

## Success Criteria
[How will we know if the analysis succeeded?]
```

---

## Stage 2: Discovery

**Objective:** Assess data availability and feasibility.

**Inputs:**
- Scoped research question
- Target platforms

**Outputs:**
- Data source inventory
- API access confirmed
- Volume estimates
- Feasibility assessment

**Agent:** Data Collector (Gemini Flash)

**Tasks:**
1. Check API access for each platform
2. Estimate data volume for query
3. Identify potential data gaps
4. Note rate limits and cost estimates

**Template:**
```markdown
## Data Sources Assessed

### [Platform 1]
- **API:** [Name, version]
- **Access:** ✅ Confirmed / ❌ Blocked / ⚠️ Limited
- **Estimated volume:** [N posts/messages]
- **Rate limits:** [requests per minute]
- **Cost:** [if applicable]
- **Notes:** [gaps, limitations]

### [Platform 2]
...

## Feasibility Assessment
- **Overall:** FEASIBLE / CHALLENGING / NOT FEASIBLE
- **Risks:** [list potential issues]
- **Recommendations:** [how to proceed]
```

---

## Stage 3: Planning

**Objective:** Create detailed execution plan.

**Inputs:**
- Scoped question
- Discovery results

**Outputs:**
- Analysis plan document
- Script sequence
- Model routing plan
- Timeline estimate

**Agent:** Orchestrator (Claude Opus)

**Template:**
```markdown
## Analysis Plan

### Phase 1: Data Collection
1. Collect data from [Source 1]
2. Collect data from [Source 2]
3. Merge and deduplicate

### Phase 2: Preprocessing
1. Clean text (encoding, normalization)
2. Extract entities (URLs, hashtags, mentions)
3. Parse timestamps

### Phase 3: Analysis
1. [Method 1]: [Description]
2. [Method 2]: [Description]
3. [Method 3]: [Description]

### Phase 4: Synthesis
1. Generate visualizations
2. Calculate summary statistics
3. Write findings

## Model Routing
| Stage | Task | Model | Rationale |
|-------|------|-------|-----------|
| Collection | API calls | Gemini Flash | Simple, fast |
| Preprocessing | Data cleaning | Gemini Flash | Routine |
| Analysis | Code writing | DeepSeek V3 | Strong at code |
| QA | Code review | GPT-4o | Different from writer |
| Synthesis | Report | Claude Opus | Nuanced writing |

## Timeline
- Collection: ~X hours
- Preprocessing: ~X hours
- Analysis: ~X hours
- Synthesis: ~X hours
- Total: ~X hours
```

**[CHECKPOINT 1: User approves plan before proceeding]**

---

## Stage 4: Data Acquisition

**Objective:** Collect data from all sources.

**Inputs:**
- Approved plan
- API credentials

**Outputs:**
- Raw data files (JSON Lines format)
- Collection logs
- Data manifests

**Agent:** Data Collector (Gemini Flash)

**Per-Source Process:**
1. Write collection script
2. Execute script
3. QA script (Code Reviewer)
4. Verify output integrity
5. Log results

**Script QA Loop:**
```
write_script() → execute() → qa_review()
                              │
                    ┌─────────┴─────────┐
                    │                   │
                 PASSED              BLOCKER
                    │                   │
                    ▼                   ▼
               continue            fix_and_retry()
```

**Output Format:**
```
data/raw/
├── reddit_politics_2024.jsonl
├── telegram_channels_2024.jsonl
└── manifest.yaml
```

**Manifest Template:**
```yaml
collection:
  date: "2026-02-17"
  agent: "data-collector-v1"

sources:
  - name: reddit_politics
    file: reddit_politics_2024.jsonl
    rows: 45678
    date_range: "2024-01-01 to 2024-12-31"
    query: "election"
    
  - name: telegram_channels
    file: telegram_channels_2024.jsonl
    rows: 23456
    channels: 50
    date_range: "2024-01-01 to 2024-12-31"
```

---

## Stage 5: Preprocessing

**Objective:** Clean and standardize data for analysis.

**Inputs:**
- Raw data files

**Outputs:**
- Processed data files
- Preprocessing log
- Schema documentation

**Agent:** Data Processor (DeepSeek V3)

**Tasks:**
1. Text cleaning (encoding, normalization)
2. Entity extraction (URLs, hashtags, mentions)
3. Timestamp parsing and normalization
4. Deduplication
5. Schema validation

**QA Checks:**
- Row counts match (no silent drops)
- Encoding issues resolved
- Timestamps in UTC
- No null primary keys

---

## Stage 6: Archive & Checkpoint

**Objective:** Archive clean data and validate before analysis.

**Inputs:**
- Processed data

**Outputs:**
- Archived dataset
- Data summary statistics
- Quality report

**Agent:** Orchestrator

**Tasks:**
1. Calculate summary statistics
2. Generate data profile
3. Create quality report
4. Archive to persistent storage

**Summary Template:**
```markdown
## Data Summary

### Volume
- Total records: [N]
- Unique users: [N]
- Date range: [start] to [end]

### Content Distribution
- Posts with URLs: [N] ([%])
- Posts with media: [N] ([%])
- Average text length: [N] chars

### Temporal Distribution
[Histogram or time series plot]

### Quality Metrics
- Missing values: [field: N]
- Duplicate rate: [%]
- Encoding issues: [N]
```

**[CHECKPOINT 2: User reviews data summary before analysis]**

---

## Stage 7: Analysis

**Objective:** Execute planned analyses.

**Inputs:**
- Processed data
- Analysis plan

**Outputs:**
- Analysis artifacts (models, networks, results)
- Figures and tables
- Analysis logs

**Agent:** Analysis Agents (specialized)

**Per-Analysis Process:**
1. Write analysis script
2. Execute script
3. QA review (different model)
4. If PASSED: save artifacts, continue
5. If BLOCKER: revise (max 2 attempts)

**Common Analyses:**
- Network construction and metrics
- Community detection
- Topic modeling
- Coordination detection
- LLM annotation

**Output Structure:**
```
output/
├── figures/
│   ├── network_main.png
│   ├── communities.png
│   └── timeline.png
├── tables/
│   ├── centrality_metrics.csv
│   └── community_summary.csv
└── models/
    ├── topic_model.pkl
    └── network.graphml
```

---

## Stage 8: Synthesis

**Objective:** Interpret results and write findings.

**Inputs:**
- Analysis artifacts
- Original research question

**Outputs:**
- Draft report
- Key findings summary
- Limitations section

**Agent:** Synthesizer (Claude Opus)

**Template:**
```markdown
# Research Report: [Title]

## Executive Summary
[3-5 bullet points of key findings]

## Research Question
[Restate the question]

## Data & Methods
### Data Sources
[Describe data collected]

### Methods
[Describe analyses performed]

## Findings

### Finding 1: [Title]
[Description with supporting evidence]
[Relevant figure/table reference]

### Finding 2: [Title]
...

## Limitations
[Honest assessment of limitations]

## Conclusions
[Summary and implications]

## Appendix
- Data sources and access
- Code repository
- Model versions used
```

---

## Stage 9: Delivery

**Objective:** Deliver final report and artifacts.

**Inputs:**
- Draft report
- All artifacts

**Outputs:**
- Final report (PDF/Markdown)
- Supporting files
- Delivery notification

**Agent:** Orchestrator

**Tasks:**
1. Final quality check
2. Format report
3. Package deliverables
4. Send notification to user

**[CHECKPOINT 3: User receives and reviews final deliverable]**

**Delivery Package:**
```
delivery/
├── REPORT.md
├── REPORT.pdf
├── data/
│   └── processed/ (or link)
├── output/
│   ├── figures/
│   └── tables/
├── scripts/
│   └── (reproducibility)
└── README.md
```

---

## Quality Assurance Protocol

Every script follows this loop:

```python
def script_qa_loop(task, max_attempts=3):
    for attempt in range(max_attempts):
        # Write script (using code-gen model)
        script = generate_script(task)
        
        # Execute
        result = execute_script(script)
        
        # QA review (using DIFFERENT model)
        verdict = review_script(script, result, reviewer_model=DIFFERENT_MODEL)
        
        if verdict == 'PASSED':
            log_success(task, script, result)
            return result
        elif verdict == 'WARNING':
            log_warning(task, verdict.issues)
            return result  # Continue with notation
        elif verdict == 'BLOCKER':
            if attempt < max_attempts - 1:
                task = incorporate_feedback(task, verdict.issues)
            else:
                escalate_to_human(task, verdict.issues)
                raise QABlockerError(verdict.issues)
```

---

## State Management

Maintain `STATE.md` throughout pipeline:

```markdown
# Pipeline State

## Current Stage: 7 (Analysis)
## Started: 2026-02-17 09:00 UTC
## Last Updated: 2026-02-17 14:30 UTC

## Stage Progress

| Stage | Status | Started | Completed | Notes |
|-------|--------|---------|-----------|-------|
| 1 Scoping | ✅ Complete | 09:00 | 09:15 | |
| 2 Discovery | ✅ Complete | 09:15 | 09:45 | |
| 3 Planning | ✅ Complete | 09:45 | 10:00 | User approved |
| 4 Acquisition | ✅ Complete | 10:00 | 12:00 | 45k records |
| 5 Preprocessing | ✅ Complete | 12:00 | 12:30 | |
| 6 Archive | ✅ Complete | 12:30 | 12:45 | User approved |
| 7 Analysis | 🔄 In Progress | 12:45 | - | Network done, topics pending |
| 8 Synthesis | ⏳ Pending | | | |
| 9 Delivery | ⏳ Pending | | | |

## Scripts Executed

| Script | Stage | Status | QA Verdict |
|--------|-------|--------|------------|
| collect_reddit.py | 4 | ✅ | PASSED |
| collect_telegram.py | 4 | ✅ | PASSED |
| preprocess.py | 5 | ✅ | PASSED |
| network_analysis.py | 7 | ✅ | PASSED |
| topic_model.py | 7 | 🔄 | Running |

## Blockers
- None

## Next Actions
1. Complete topic modeling
2. Run coordination detection
3. Generate visualizations
```

---

## Error Handling

| Error Type | Response |
|------------|----------|
| API timeout | Retry with exponential backoff |
| Rate limit | Wait and retry |
| Data validation fail | Log, report to user |
| QA blocker (3x) | Escalate to human |
| Model unavailable | Route to fallback model |
| Unexpected exception | Log full trace, pause, notify |
