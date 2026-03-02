# Data Module

Format detection, conversion, and public dataset references for communication research.

---

## Architecture

```
data/
├── README.md           # This file
├── formats.py          # Format detection & conversion
├── loaders.py          # Platform-specific loaders
├── validators.py       # Data quality checks
├── synthetic.py        # Generate test data
└── datasets.md         # Public dataset references
```

---

## Quick Start

```python
from data.formats import load_social_media_data

# Auto-detect format and load
data = load_social_media_data("my_data.json")
# or
data = load_social_media_data("my_data.csv")
# or  
data = load_social_media_data("my_folder/")

# Returns standardized DataFrame with:
# - id, text, timestamp, author, platform
# - Plus platform-specific fields
```

---

## Supported Formats

| Platform | Formats | Auto-Detect |
|----------|---------|-------------|
| Twitter/X | API JSON (v1, v2), CSV export | ✅ |
| Reddit | PRAW JSON, Pushshift, CSV | ✅ |
| Telegram | JSON export, HTML export | ✅ |
| YouTube | API JSON, CSV | ✅ |
| Bluesky | AT Protocol JSON | ✅ |
| Generic | CSV, JSON, JSONL | ✅ |

---

## Public Datasets for Testing & Benchmarking

See `datasets.md` for full list with download links.
