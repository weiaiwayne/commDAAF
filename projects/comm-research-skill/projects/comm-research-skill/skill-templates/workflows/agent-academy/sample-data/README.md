# AgentAcademy: Sample Data

Upload your research data here for multi-agent analysis and peer review.

## How AgentAcademy Works

1. **Upload your data** — analysis outputs, draft methods, preliminary findings
2. **Multiple AI agents** independently analyze the same material
3. **Cross-review** — agents critique each other's work
4. **Synthesis** — convergent findings = high confidence; divergent = investigate further
5. **Lessons learned** — errors become new checks in CommDAAF

## Supported Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| CSV | `.csv` | Tabular data, auto-detects delimiter |
| Excel | `.xlsx` | Spreadsheet data |
| JSON | `.json` | Nested structures supported |
| JSONL | `.jsonl` | One JSON object per line |
| Parquet | `.parquet` | Efficient for large datasets |
| Text | `.txt`, `.md` | Research notes, analysis writeups |
| PDF | `.pdf` | Research papers (text extracted) |

## Sampling Options

For large datasets, the academy can sample:

```
# Use full dataset
/academy file:sample-data/my_analysis.csv

# Sample 100 rows
/academy file:sample-data/my_analysis.csv sample:100

# Sample 10%
/academy file:sample-data/my_analysis.csv sample:10%

# Random seed for reproducibility
/academy file:sample-data/my_analysis.csv sample:100 seed:42
```

## What to Upload

Good candidates for AgentAcademy review:
- **Analysis outputs** — topic models, network graphs, sentiment scores
- **Codebooks** — annotation schemes for content analysis
- **Draft methods sections** — before you finalize
- **Preliminary findings** — early results you want stress-tested
- **Raw datasets** — let agents discover research questions

## Completed Runs

| Dataset | Agents | Key Finding |
|---------|--------|-------------|
| @EastLosHighShow tweets | GLM + Kimi | Hashtags boost engagement; sentiment doesn't matter |
| #EndSARS protest | GLM + Kimi | Hybrid decentralized participation + centralized amplification |

See `LESSONS_LEARNED.md` for full documentation of errors caught and lessons extracted.

## Data Privacy

This folder is local to your OpenClaw workspace. Data is sent to AI models for analysis — don't upload anything you can't share with third-party APIs.

---

*Upload your data and let me know when ready to run the academy.*
