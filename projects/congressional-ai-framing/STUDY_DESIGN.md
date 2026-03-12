# Study Design: Congressional AI Framing Analysis

## Research Question

**Primary RQ:** How is artificial intelligence framed in U.S. congressional hearings, and how have these frames evolved over time?

**Secondary RQs:**
1. Which AI frames are associated with specific political parties or committees?
2. How do expert witness frames differ from legislator frames?
3. What frames predict legislative action (bills introduced, votes)?

## Validation Tier
🟢 EXPLORATORY — Multi-model validation, hypothesis-generating

## Data Source

### GovInfo API (Congressional Hearings)
- **Collection:** CHRG (Congressional Hearings)
- **API Key:** data.gov key (Wayne's)
- **Total AI-related hearings:** 1,754 (as of March 2026)
- **Full transcripts available:** Yes (HTML + PDF)
- **Time range available:** 1969-2026 (concentrated 2023-2026)

### Data Access Verification ✅
```bash
# Confirmed working:
curl -s -X POST "https://api.govinfo.gov/search" \
  -H "X-Api-Key: [KEY]" \
  -H "Content-Type: application/json" \
  -d '{"query": "\"artificial intelligence\" collection:CHRG", "pageSize": 20}'

# Full transcript access confirmed:
curl -s "https://api.govinfo.gov/packages/CHRG-119hhrg61690/htm?api_key=[KEY]"
```

### Temporal Distribution (Preliminary)
| Year | Hearings (sample) |
|------|-------------------|
| 2023 | 16 |
| 2024 | 19 |
| 2025 | 156+ |
| 2026 | 1+ (YTD) |

**Note:** Explosive growth in 2025 — likely ChatGPT/GenAI driven.

## Constructs

### Primary: AI Frames (adapted from technology policy literature)

| Frame | Definition | Theoretical Source |
|-------|------------|-------------------|
| **INNOVATION** | AI as economic opportunity, competitiveness, jobs | Entman 1993; Nisbet 2009 |
| **RISK/SAFETY** | AI as threat (existential, job loss, bias, misuse) | Jasanoff 2016 |
| **REGULATION** | AI as requiring governance, oversight, rules | Lessig 1999 |
| **SOVEREIGNTY** | AI as national security, China competition | Securitization theory |
| **RIGHTS** | AI as civil liberties issue (privacy, discrimination) | Zuboff 2019 |
| **TECHNICAL** | AI discussed in technical/scientific terms | Expert discourse |

### Secondary Dimensions

| Dimension | Values | Notes |
|-----------|--------|-------|
| **Valence** | positive / negative / neutral | Toward AI generally |
| **Urgency** | low / medium / high | Temporal pressure |
| **Specificity** | general AI / specific application | GenAI, autonomous vehicles, etc. |
| **Actor focus** | government / industry / academia / civil society | Who should act |

### Speaker Metadata
- **Party:** Republican / Democrat
- **Chamber:** House / Senate
- **Role:** Legislator / Witness / Agency official
- **Committee:** Judiciary, Commerce, Armed Services, etc.

## Sampling Strategy

### Phase 1: Pilot Sample (N=100)
- 25 hearings from each period:
  - Pre-ChatGPT (before Nov 2022)
  - Early ChatGPT (Nov 2022 - Dec 2023)
  - Peak AI discourse (2024)
  - Current (2025-2026)
- Stratified by chamber (House/Senate)

### Phase 2: Full Sample (N=400-600)
- Focus on 2023-2026 (high AI salience period)
- Stratified by:
  - Committee type (tech-focused vs. domain-specific)
  - Partisan control
  - Hearing type (oversight, legislative, investigative)

### Unit of Analysis Options
1. **Hearing-level:** Overall frame of entire hearing (coarser, faster)
2. **Statement-level:** Each speaker's statement (finer, richer)
3. **Paragraph-level:** Individual claims (finest, most labor-intensive)

**Recommendation:** Start with hearing-level, refine to statement-level for key findings.

## Data Collection Pipeline

```python
# Pseudocode for data collection

1. Search API for AI hearings
   → Get packageIds, titles, dates, committees

2. For each hearing:
   a. Fetch HTML transcript
   b. Parse into structured segments:
      - Opening statements
      - Witness testimony
      - Q&A exchanges
   c. Extract speaker metadata
   d. Save raw + processed versions

3. Create analysis batches:
   - 25 hearings per batch (Kimi limit)
   - Include metadata + transcript excerpts
```

## Planned Analyses

### Descriptive
- Frame distribution over time
- Frame distribution by party, chamber, committee
- Co-occurrence patterns (which frames appear together)

### Inferential
- **DV:** Frame presence (binary) or intensity (ordinal)
- **IVs:** Party, chamber, committee, time period, witness type
- **Model:** Logistic regression (binary) or ordinal logit
- **Controls:** Hearing length, number of witnesses, media attention

### Temporal
- Interrupted time series around ChatGPT release (Nov 2022)
- Frame evolution trajectories

## CommDAAF Coding Prompt (Draft v0.1)

```markdown
# CONGRESSIONAL AI FRAMING ANALYSIS

## TASK
For each congressional hearing excerpt, identify:
1. PRIMARY_FRAME: The dominant AI frame
2. SECONDARY_FRAMES: Other frames present (up to 2)
3. VALENCE: Overall sentiment toward AI
4. URGENCY: Temporal pressure expressed
5. ACTOR_FOCUS: Who is called to act

## FRAME DEFINITIONS
[To be developed with full decision rules, examples, counter-examples]

## OUTPUT FORMAT
JSON array with confidence scores
```

## Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Data collection | 1-2 days | Raw transcripts + metadata |
| Prompt development | 1 day | CommDAAF prompt v1.0 |
| Pilot coding (N=100) | 1 day | Reliability assessment |
| Prompt refinement | 0.5 day | CommDAAF prompt v2.0 |
| Full coding (N=400-600) | 2-3 days | Coded dataset |
| Analysis | 1-2 days | Statistical results |
| Writing | 2-3 days | Draft report |

**Total:** ~10 days for full exploratory study

## Files

See `DATA_MANIFEST.md` for complete data documentation.

```
projects/congressional-ai-framing/
├── STUDY_DESIGN.md              # This file
├── DATA_MANIFEST.md             # Data locations and retrieval
│
├── data/
│   ├── transcripts/             # 561 hearing transcripts (HTML)
│   ├── metadata/                # Per-hearing metadata (JSON)
│   ├── collection_summary.json  # Collection status
│   └── pilot_batch_25.json      # Pilot sample for coding
│
├── prompts/
│   └── commdaaf_v1.0.md         # Current coding prompt
│
├── scripts/
│   ├── collect_hearings.py      # GovInfo API collection
│   └── prepare_coding_batch.py  # Batch preparation
│
└── outputs/                     # Model coding outputs
    ├── claude/
    ├── glm/
    └── kimi/
```

## API Notes

### GovInfo Search API
- Endpoint: `POST https://api.govinfo.gov/search`
- Auth: `X-Api-Key` header or `api_key` query param
- Pagination: `offsetMark` (not `offset`)
- Collection filter: Include in query string (`collection:CHRG`)

### GovInfo Package API
- Transcript: `https://api.govinfo.gov/packages/{packageId}/htm?api_key=...`
- Metadata: `https://api.govinfo.gov/packages/{packageId}/summary?api_key=...`

### Rate Limits
- Unknown; implement exponential backoff
- Batch requests conservatively

---

*Created: 2026-03-12*
*Status: Ready for data collection*
