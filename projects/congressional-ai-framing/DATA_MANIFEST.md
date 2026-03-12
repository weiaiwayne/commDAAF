# Congressional AI Framing Study - Data Manifest

**Last Updated**: 2026-03-12
**Study Location**: `/root/.openclaw/workspace/projects/congressional-ai-framing/`

---

## Directory Structure

```
projects/congressional-ai-framing/
├── STUDY_DESIGN.md              # Research design and methodology
├── DATA_MANIFEST.md             # This file - data locations
│
├── data/
│   ├── transcripts/             # Raw hearing transcripts (HTML/TXT)
│   │   └── CHRG-{congress}{chamber}hrg{number}.html
│   │
│   ├── metadata/                # Hearing metadata (JSON)
│   │   └── CHRG-*.json
│   │
│   ├── search_results.json      # API search results
│   ├── collection_summary.json  # Collection status per hearing
│   └── pilot_batch_25.json      # Pilot sample for coding
│
├── prompts/
│   └── commdaaf_v1.0.md         # Coding prompt (current version)
│
├── scripts/
│   ├── collect_hearings.py      # Data collection from GovInfo API
│   └── prepare_coding_batch.py  # Prepare excerpts for coding
│
└── outputs/                     # (To be created during coding)
    ├── claude/
    ├── glm/
    └── kimi/
```

---

## Data Sources

### GovInfo API
- **Endpoint**: `https://api.govinfo.gov/search`
- **Collection**: CHRG (Congressional Hearings)
- **API Key**: data.gov key (stored in environment or script)
- **Documentation**: https://api.govinfo.gov/docs

### Search Query
```
"artificial intelligence" collection:CHRG
```

---

## Data Files

### 1. Raw Transcripts
**Location**: `data/transcripts/`
**Format**: HTML (from GovInfo)
**Naming**: `CHRG-{congress}{chamber}hrg{jacket_number}.html`
- congress: 3-digit congress number (e.g., 119)
- chamber: `h` (House), `s` (Senate), `j` (Joint)
- jacket_number: GPO jacket number

**Example**: `CHRG-119hhrg61690.html`

**Count**: 561 transcripts (as of 2026-03-12)
**Size**: ~117MB total

### 2. Metadata
**Location**: `data/metadata/`
**Format**: JSON
**Content**: GovInfo package summary (committees, dates, witnesses)

### 3. Collection Summary
**Location**: `data/collection_summary.json`
**Format**: JSON array
**Content**:
```json
[
  {
    "packageId": "CHRG-119hhrg62435",
    "title": "...",
    "dateIssued": "2026-01-13",
    "hasTranscript": true,
    "hasMetadata": true
  }
]
```

### 4. Pilot Batch
**Location**: `data/pilot_batch_25.json`
**Format**: JSON array
**Content**: 25 hearing excerpts prepared for coding
```json
[
  {
    "id": "CHRG-119hhrg60318",
    "title": "...",
    "congress": 119,
    "chamber": "HOUSE",
    "committee": "...",
    "excerpt": "...",
    "excerpt_length": 1098
  }
]
```

---

## Coding Outputs (Future)

### Model Outputs
**Location**: `outputs/{model}/batch_{n}.json`
**Format**: JSON array per CommDAAF prompt specification
```json
[
  {
    "id": "CHRG-119hhrg61690",
    "primary_frame": "INNOVATION",
    "secondary_frame": "SOVEREIGNTY",
    "valence": "POSITIVE",
    "urgency": "MEDIUM",
    "policy_stance": "ANTI_REGULATION",
    "confidence": 0.85,
    "rationale": "..."
  }
]
```

### Merged Results
**Location**: `outputs/merged/all_models.json`
**Content**: Combined coding from all models with agreement metrics

---

## How to Retrieve Data

### Load Transcripts
```python
from pathlib import Path
import json

DATA_DIR = Path("/root/.openclaw/workspace/projects/congressional-ai-framing/data")

# List all transcripts
transcripts = list(DATA_DIR.glob("transcripts/CHRG-*.html"))
print(f"Found {len(transcripts)} transcripts")

# Load a specific transcript
with open(DATA_DIR / "transcripts/CHRG-119hhrg61690.html") as f:
    content = f.read()
```

### Load Pilot Batch
```python
with open(DATA_DIR / "pilot_batch_25.json") as f:
    pilot = json.load(f)
    
for hearing in pilot:
    print(f"{hearing['id']}: {hearing['title']}")
```

### Load Collection Summary
```python
with open(DATA_DIR / "collection_summary.json") as f:
    summary = json.load(f)
    
# Filter by date
recent = [h for h in summary if h['dateIssued'] >= '2025-01-01']
```

---

## Collection Statistics

| Metric | Value |
|--------|-------|
| Total Hearings | 561 |
| 119th Congress (2025-2026) | 165 |
| 118th Congress (2023-2024) | 376 |
| Earlier Congresses | 20 |
| Total Size | ~117MB |
| Avg Transcript Size | ~200KB |

---

## API Access

### GovInfo Search
```bash
curl -s -X POST "https://api.govinfo.gov/search" \
  -H "X-Api-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "\"artificial intelligence\" collection:CHRG", "pageSize": 100}'
```

### Fetch Transcript
```bash
curl -s "https://api.govinfo.gov/packages/CHRG-119hhrg61690/htm?api_key=YOUR_KEY"
```

### Fetch Metadata
```bash
curl -s "https://api.govinfo.gov/packages/CHRG-119hhrg61690/summary?api_key=YOUR_KEY"
```

---

## Version History

| Date | Action | Files Changed |
|------|--------|---------------|
| 2026-03-12 | Initial collection | 561 transcripts |
| 2026-03-12 | Created pilot batch | pilot_batch_25.json |
| 2026-03-12 | Created coding prompt | commdaaf_v1.0.md |
