# Working with Existing Datasets

**Reality:** Most computational communication research in 2026 uses existing datasets, not fresh API collection. This is the new normal.

---

## Why Existing Datasets?

1. **API access is dead/expensive** — Twitter $5K/mo, Reddit restricted, Meta gated
2. **Faster research** — No collection delays
3. **Better documented** — Published datasets have methods documentation
4. **Peer-reviewed** — Collection methods already scrutinized
5. **Citeable** — DOIs enable proper attribution
6. **Comparable** — Others can use same data

---

## Finding Datasets

### General Repositories

| Repository | URL | Strengths | Search Tips |
|------------|-----|-----------|-------------|
| **Harvard Dataverse** | dataverse.harvard.edu | Social science, versioned | "social media" + topic |
| **ICPSR** | icpsr.umich.edu | Survey + social media | Requires membership |
| **Zenodo** | zenodo.org | Open, DOIs | CERN-hosted, broad |
| **OSF** | osf.io | Pre-reg + data | Search preprints |
| **Kaggle** | kaggle.com/datasets | ML-oriented | Good for large datasets |
| **IEEE DataPort** | ieee-dataport.org | Technical | CS-focused |
| **FigShare** | figshare.com | General | Many disciplines |

### Platform-Specific

#### Twitter/X Archives
| Dataset | Content | Access |
|---------|---------|--------|
| **DocNow Catalog** | Event-based tweet IDs | docnow.io (need API to hydrate) |
| **Internet Archive Twitter Stream** | Historical samples | archive.org |
| **ICWSM Datasets** | Conference-shared | Various |
| **Congressman Tweets** | Political elites | Harvard Dataverse |
| **Election2020** | US election discourse | Multiple sources |

#### Reddit Archives
| Dataset | Content | Access |
|---------|---------|--------|
| **Pushshift Archive** | Reddit through 2023 | Academic Torrents |
| **Subreddit-specific** | Various researchers | Zenodo, Dataverse |

#### Multi-Platform
| Dataset | Content | Access |
|---------|---------|--------|
| **FakeNewsNet** | Fake/real news + social | GitHub |
| **PHEME** | Rumor + verification | FigShare |
| **COVID-19 Datasets** | Pandemic content | Various |

### By Research Topic

```python
# Common topic-dataset mappings

TOPIC_DATASETS = {
    'elections': [
        'Harvard Election Study datasets',
        'DocNow election collections',
        'MIT Election Lab'
    ],
    'misinformation': [
        'FakeNewsNet',
        'LIAR dataset',
        'PHEME rumor dataset',
        'COVID-19 misinfo datasets'
    ],
    'political_communication': [
        'Congressman Twitter',
        'European Parliament data',
        'Campaign Ad Archive'
    ],
    'health_communication': [
        'COVID-19 social media datasets',
        'Vaccine discourse datasets',
        'Health misinformation datasets'
    ],
    'journalism': [
        'GDELT',
        'MediaCloud',
        'News datasets (various)'
    ],
    'hate_speech': [
        'HateXplain',
        'Civil Comments',
        'Twitter hate speech datasets'
    ]
}
```

---

## Evaluating Datasets

Before using, verify quality:

### Checklist

```markdown
## Dataset Evaluation Checklist

### Documentation
- [ ] Collection method documented?
- [ ] Sampling strategy explained?
- [ ] Time period specified?
- [ ] Platform/source clear?
- [ ] Variables/schema documented?

### Quality
- [ ] Sample size adequate for my RQ?
- [ ] Time period relevant?
- [ ] Population appropriate?
- [ ] Known biases documented?
- [ ] Data format usable?

### Provenance
- [ ] Creator credible (institution, publication)?
- [ ] Peer-reviewed or used in peer-reviewed work?
- [ ] Version numbered?
- [ ] DOI available?

### Legal/Ethical
- [ ] Terms of use clear?
- [ ] Can I use for my purpose?
- [ ] IRB/ethics documentation available?
- [ ] Redistribution rules clear?

### Technical
- [ ] File format(s)?
- [ ] Size manageable?
- [ ] Schema/codebook available?
- [ ] Missing data handling documented?
```

### Red Flags

```yaml
red_flags:
  - No documentation of collection method
  - "Scraped from API" without details
  - No version number (data may change)
  - Unclear sampling (convenience sample?)
  - Creator unreachable/anonymous
  - No license or unclear terms
  - Suspiciously complete (no missing data)
  - Time period doesn't match description
```

---

## Working with Datasets

### Loading and Exploring

```python
import pandas as pd
import json

def load_and_assess(path):
    """Load dataset and generate assessment."""
    
    # Detect format
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith('.json') or path.endswith('.jsonl'):
        df = pd.read_json(path, lines=path.endswith('.jsonl'))
    elif path.endswith('.parquet'):
        df = pd.read_parquet(path)
    else:
        raise ValueError(f"Unknown format: {path}")
    
    assessment = {
        'rows': len(df),
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing': df.isnull().sum().to_dict(),
        'missing_pct': (df.isnull().sum() / len(df) * 100).to_dict(),
        'sample': df.head(3).to_dict()
    }
    
    # Date range if date column exists
    date_cols = [c for c in df.columns if 'date' in c.lower() or 'time' in c.lower()]
    if date_cols:
        for col in date_cols:
            try:
                df[col] = pd.to_datetime(df[col])
                assessment[f'{col}_range'] = {
                    'min': df[col].min().isoformat(),
                    'max': df[col].max().isoformat()
                }
            except:
                pass
    
    return df, assessment

# Usage
df, assessment = load_and_assess('data/tweets_election2024.csv')
print(json.dumps(assessment, indent=2, default=str))
```

### Validating Data Quality

```python
def validate_dataset(df, expected_schema):
    """
    Validate dataset against expected schema.
    """
    issues = []
    
    # Check required columns
    for col, spec in expected_schema.items():
        if col not in df.columns:
            issues.append(f"Missing required column: {col}")
            continue
        
        # Check dtype
        if 'dtype' in spec:
            if not df[col].dtype == spec['dtype']:
                issues.append(f"Column {col} has dtype {df[col].dtype}, expected {spec['dtype']}")
        
        # Check missing rate
        if 'max_missing' in spec:
            missing_rate = df[col].isnull().mean()
            if missing_rate > spec['max_missing']:
                issues.append(f"Column {col} has {missing_rate:.1%} missing, max allowed {spec['max_missing']:.1%}")
        
        # Check value range
        if 'min_value' in spec:
            if df[col].min() < spec['min_value']:
                issues.append(f"Column {col} has values below minimum {spec['min_value']}")
        
        if 'max_value' in spec:
            if df[col].max() > spec['max_value']:
                issues.append(f"Column {col} has values above maximum {spec['max_value']}")
    
    return issues

# Example schema
TWEET_SCHEMA = {
    'id': {'dtype': 'int64', 'max_missing': 0},
    'text': {'dtype': 'object', 'max_missing': 0.01},
    'created_at': {'dtype': 'datetime64[ns]', 'max_missing': 0.01},
    'user_id': {'dtype': 'int64', 'max_missing': 0.05},
    'retweet_count': {'dtype': 'int64', 'min_value': 0}
}
```

### Subsetting for Your RQ

```python
def create_study_sample(df, criteria):
    """
    Create study sample with documented filtering.
    """
    
    log = {
        'initial_n': len(df),
        'filters': [],
        'final_n': None
    }
    
    for name, condition in criteria.items():
        before = len(df)
        df = df[condition(df)]
        after = len(df)
        
        log['filters'].append({
            'filter': name,
            'removed': before - after,
            'remaining': after
        })
    
    log['final_n'] = len(df)
    
    return df, log

# Example
criteria = {
    'english_only': lambda df: df['lang'] == 'en',
    'has_text': lambda df: df['text'].notna() & (df['text'].str.len() > 0),
    'date_range': lambda df: (df['created_at'] >= '2024-01-01') & (df['created_at'] <= '2024-06-30'),
    'min_engagement': lambda df: df['retweet_count'] + df['like_count'] >= 1
}

study_df, filter_log = create_study_sample(raw_df, criteria)
```

---

## Combining Datasets

### Matching Across Sources

```python
def merge_datasets(df1, df2, match_col, how='inner'):
    """
    Merge datasets with documentation.
    """
    
    info = {
        'df1_rows': len(df1),
        'df2_rows': len(df2),
        'df1_unique_keys': df1[match_col].nunique(),
        'df2_unique_keys': df2[match_col].nunique(),
        'matched': None,
        'unmatched_df1': None,
        'unmatched_df2': None
    }
    
    merged = pd.merge(df1, df2, on=match_col, how=how, indicator=True)
    
    info['matched'] = len(merged[merged['_merge'] == 'both'])
    info['unmatched_df1'] = len(merged[merged['_merge'] == 'left_only'])
    info['unmatched_df2'] = len(merged[merged['_merge'] == 'right_only'])
    
    return merged, info
```

### Harmonizing Variables

```python
def harmonize_text_column(df, source_col, target_col='text'):
    """
    Harmonize text column from different dataset formats.
    """
    
    # Common mappings
    MAPPINGS = {
        'full_text': lambda x: x['full_text'],
        'body': lambda x: x['body'],
        'content': lambda x: x['content'],
        'message': lambda x: x['message'],
        'tweet': lambda x: x['tweet'],
        'post_text': lambda x: x['post_text']
    }
    
    if source_col in MAPPINGS:
        df[target_col] = MAPPINGS[source_col](df)
    else:
        df[target_col] = df[source_col]
    
    return df
```

---

## Citing Datasets

### Proper Citation Format

```bibtex
@dataset{author2024datasetname,
  author = {Author, First and Author, Second},
  title = {Dataset Name},
  year = {2024},
  publisher = {Repository Name},
  version = {1.0},
  doi = {10.7910/DVN/XXXXX},
  url = {https://doi.org/10.7910/DVN/XXXXX}
}
```

### In-Text Citation

> We used the Twitter Election Dataset (Author & Author, 2024) comprising 2.5 million tweets from January to November 2024.

### Data Availability Statement

```markdown
## Data Availability

The data used in this study are available from [Repository Name] 
at [DOI/URL]. The dataset is available under [license] for 
[purposes]. Our analysis code is available at [GitHub URL].

Note: Raw tweets require Twitter API access to hydrate from 
provided tweet IDs.
```

---

## Creating New Datasets for Sharing

If you collect new data, make it reusable:

### Documentation Requirements

```markdown
# Dataset Documentation Template

## Overview
- Name:
- Version:
- DOI:
- Last updated:
- Maintainer:

## Description
[What is this dataset? What does it contain?]

## Collection Method
[How was data collected? What tools/APIs?]

## Time Period
[Start date] to [End date]

## Sampling
[How was the sample constructed? Random? Keyword? Complete?]

## Variables
| Variable | Type | Description | Missing Rate |
|----------|------|-------------|--------------|
| id | int | Unique identifier | 0% |
| text | str | Post content | 0.5% |
| ... | ... | ... | ... |

## Known Limitations
- [Limitation 1]
- [Limitation 2]

## Ethics
[IRB status, consent, anonymization]

## Citation
[How to cite this dataset]

## License
[Usage terms]

## Version History
- v1.0 (2024-01-01): Initial release
- v1.1 (2024-06-01): Added [fields]
```

### Sharing Checklist

```yaml
before_sharing:
  - Remove PII (emails, phone numbers, names if needed)
  - Check platform ToS (some prohibit redistribution)
  - Choose appropriate license (CC-BY, CC0, etc.)
  - Create documentation
  - Version the dataset
  - Generate DOI
  - Test: can someone else load this?
```

---

## Workflow: Using Existing Data

```python
def existing_data_workflow():
    """Standard workflow for using existing datasets."""
    
    return {
        1: {
            'step': 'Find candidate datasets',
            'actions': [
                'Search repositories',
                'Check recent papers for data sources',
                'Contact authors if needed'
            ]
        },
        2: {
            'step': 'Evaluate datasets',
            'actions': [
                'Check documentation quality',
                'Verify fitness for RQ',
                'Assess data quality'
            ]
        },
        3: {
            'step': 'Document selection',
            'actions': [
                'Record why you chose this dataset',
                'Note any limitations for your purpose',
                'Plan for handling issues'
            ]
        },
        4: {
            'step': 'Load and validate',
            'actions': [
                'Load data',
                'Run validation checks',
                'Explore distributions'
            ]
        },
        5: {
            'step': 'Subset and process',
            'actions': [
                'Apply inclusion/exclusion criteria',
                'Document all filtering',
                'Create study sample'
            ]
        },
        6: {
            'step': 'Analyze',
            'actions': [
                'Run planned analyses',
                'Document any deviations from plan'
            ]
        },
        7: {
            'step': 'Report',
            'actions': [
                'Cite dataset properly',
                'Describe any processing',
                'Note limitations specific to dataset'
            ]
        }
    }
```

---

*In the post-API era, working with existing datasets isn't a limitation—it's a skill.*
