# Sample Data for Red-Team Testing

Upload your research data here. The workflow can:
- **Use full dataset** — for smaller files or when you want comprehensive review
- **Sample automatically** — for large datasets (configurable sample size)

## Supported Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| CSV | `.csv` | Tabular data, auto-detects delimiter |
| JSON | `.json` | Nested structures supported |
| JSONL | `.jsonl` | One JSON object per line |
| Parquet | `.parquet` | Efficient for large datasets |
| Text | `.txt`, `.md` | Research notes, analysis writeups |
| PDF | `.pdf` | Research papers (text extracted) |

## Sampling Options

When invoking red-team review:

```
# Use full dataset
/redteam file:sample-data/my_analysis.csv

# Sample 100 rows
/redteam file:sample-data/my_analysis.csv sample:100

# Sample 10%
/redteam file:sample-data/my_analysis.csv sample:10%

# Random seed for reproducibility
/redteam file:sample-data/my_analysis.csv sample:100 seed:42
```

## What to Upload

Good candidates for red-teaming:
- **Analysis outputs** — topic models, network graphs, sentiment scores
- **Codebooks** — annotation schemes for content analysis
- **Draft methods sections** — before you finalize
- **Preliminary findings** — early results you want stress-tested

## Data Privacy

This folder is local to your OpenClaw workspace. Data is sent to AI models for analysis — don't upload anything you can't share with third-party APIs.

---

*Upload your data and let me know when ready to run the red-team.*
