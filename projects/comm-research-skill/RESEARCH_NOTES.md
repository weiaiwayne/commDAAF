# Communication Research Skill - Research Notes

*Started: 2026-02-17 04:19 UTC*
*Deadline: 2026-02-17 09:00 UTC*

---

## Task Overview

Build an OpenClaw skill package for communication scholars doing computational social science research. Adapt DAAF's architecture for:
- Social media data (unstructured, messy)
- News/media data
- Network analysis + text-as-data methods
- Theories and concepts from communication research

### Key Deliverable
Detailed spec/design doc by 9am UTC

---

## Data Sources Inventory

### Social Media APIs (Currently Accessible)

| Source | Access | API Status | Notes |
|--------|--------|------------|-------|
| Reddit | Open | Active | PRAW library, decent rate limits |
| YouTube | Open | Active | YouTube Data API v3, quota system |
| TikTok | Research | Application required | TikTok Research API, academic access |
| X/Twitter | Paid | Expensive | Academic Research API deprecated, Basic tier $100/mo |
| Meta/Facebook | Restricted | SOMAR/ICPSR | Meta Content Library via application |
| Bluesky | Open | Active | AT Protocol, no auth required for public |
| Mastodon | Open | Active | ActivityPub, instance-specific |

### News/Media Data Sources

| Source | Access | Coverage | Notes |
|--------|--------|----------|-------|
| **MediaCloud** | Open | 60,000+ sources, 1B+ stories | Free API, global news |
| **GDELT** | Open | 100+ languages, since 1979 | Google BigQuery, 15-min updates |
| **Internet Archive** | Open | Historical web/news | Wayback Machine, TV News Archive |
| **Common Crawl** | Open | Web archives | Petabytes of web data |
| **News API** | Freemium | Current news | newsapi.org, limited free tier |
| **NewsData.io** | Freemium | Current news | Alternative to News API |
| **Webhose/Webz.io** | Paid | News, blogs, forums | Commercial |

### Pre-Built Datasets

| Source | Type | Notes |
|--------|------|-------|
| **SNAP Stanford** | Networks | Social networks, Reddit hyperlinks, Twitter |
| **Harvard Dataverse** | Various | Research datasets, social media |
| **SOMAR/ICPSR** | Social Media | Restricted access, application required |
| **DocNow Catalog** | Twitter IDs | Historical tweet collections |
| **Kaggle** | Various | 400k+ datasets |
| **data.world** | Various | Social media datasets |
| **HuggingFace** | NLP datasets | Text classification, sentiment |

### GDELT Specifics
- 300+ event categories
- Millions of themes, emotions
- Global Knowledge Graph (GKG)
- Visual GKG (image analysis)
- Historical: 1979-present
- Update frequency: 15 minutes
- Access: BigQuery (SQL), CSV downloads

### MediaCloud Specifics
- 60,000+ news sources globally
- 1 billion+ stories indexed
- Open-source tools
- API for search and analysis
- Directory of sources searchable

---

## Methods in Communication CSS

### Text Analysis
- Sentiment analysis
- Topic modeling (LDA, NMF, BERTopic)
- Named Entity Recognition (NER)
- Computational framing analysis
- Stance detection
- Bot/troll detection
- Claim/misinformation detection
- Narrative analysis
- Discourse analysis (computational)

### Network Analysis
- Social network analysis (SNA)
- Information diffusion
- Community detection
- Influence/centrality metrics
- Temporal network analysis
- Bipartite networks (users-content)
- Hyperlink networks

### Multi-Modal
- Image analysis (faces, objects, text)
- Video analysis (frames, captions)
- Audio transcription + analysis
- Cross-platform analysis

### Sampling & Collection
- Keyword/hashtag sampling
- Snowball sampling
- Stratified sampling
- Panel studies
- Longitudinal tracking

---

## Python Libraries for Comm Research

### Data Collection
- `praw` - Reddit API
- `google-api-python-client` - YouTube
- `tweepy` - Twitter (legacy)
- `snscrape` - Social media scraping (deprecated)
- `newspaper3k` - News article extraction
- `trafilatura` - Web content extraction
- `waybackpy` - Internet Archive
- `gdelt` - GDELT data access

### Text Analysis
- `spacy` - NLP pipeline
- `transformers` - BERT, RoBERTa, etc.
- `sentence-transformers` - Embeddings
- `gensim` - Topic modeling
- `bertopic` - Neural topic modeling
- `textblob` - Simple sentiment
- `vaderSentiment` - Social media sentiment
- `stanza` - Stanford NLP

### Network Analysis
- `networkx` - General networks
- `igraph` - Fast network analysis
- `graph-tool` - High-performance
- `pyvis` - Network visualization
- `gephi` (external) - Visualization

### Visualization
- `plotnine` - ggplot2 for Python
- `matplotlib` - Base plotting
- `seaborn` - Statistical visualization
- `plotly` - Interactive plots
- `altair` - Declarative visualization

---

## Theoretical Frameworks in Communication

(To be populated from Zotero library analysis)

Common frameworks:
- Agenda Setting
- Framing Theory
- Spiral of Silence
- Two-Step Flow
- Uses and Gratifications
- Media Ecology
- Networked Public Sphere
- Filter Bubbles / Echo Chambers
- Platform Governance
- Algorithmic Amplification
- Mis/Disinformation Studies
- Political Communication
- Health Communication
- Crisis Communication
- Computational Propaganda

---

## DAAF Architecture Adaptation

### What Transfers Directly
- Multi-agent orchestration pattern
- Per-script QA loop
- Plan → Execute → Review → Report workflow
- File-first execution
- STATE.md session tracking
- LEARNINGS.md knowledge capture

### What Needs Adaptation
- Data source skills (education → media/social)
- Validation checkpoints (tabular → unstructured)
- Methodology skills (regression → NLP/network)
- Data quality metrics (missingness → API failures, rate limits)
- Reproducibility challenges (API access changes over time)

### New Components Needed
- API failure handling & retry logic
- Rate limit management
- Data archival strategies
- Ethics/IRB documentation
- Platform TOS compliance checking
- Multi-format data handling (JSON, text, images)

---

## Zotero Integration Design

### Concept
Read researcher's Zotero library to auto-generate domain-specific skills:
1. Extract methodologies mentioned in papers
2. Identify data sources used
3. Map theoretical frameworks
4. Build citation network of the field
5. Generate skill files from extracted knowledge

### API Access
- Zotero API: https://api.zotero.org
- Key provided: hdGQHncaNqZ48Bhe0rJGyCnb
- Need: User ID (numeric)

### Extraction Pipeline
1. Fetch all items from library
2. For each paper:
   - Extract title, abstract, full-text if available
   - Identify methodology section
   - Extract named methods, tools, datasets
   - Map to theoretical frameworks
3. Aggregate findings
4. Generate skill files

---

## Key Academic References Found

### Computational Framing Analysis
- "A Survey of Computational Framing Analysis Approaches" (EMNLP 2022)
- "Computational Identification of Media Frames" (Political Communication)
- "Three Gaps in Computational Text Analysis Methods" (2021)
- "Multi-Modal Framing Analysis of News" (2025) - 500k article dataset on HuggingFace

### Textbooks
- Van Atteveldt, Trilling, & Calderón (2022). "Computational Analysis of Communication" - Wiley
  - Open access at cssbook.net
  - Chapters: Text, Networks, Images, Scraping, ML

### Journals
- Computational Communication Research (CCR) - peer-reviewed, open access
- Communication Methods and Measures
- Political Communication

---

## Key Insights for Skill Design

1. **Framing analysis is complex** — no standard unsupervised method exists
2. **Supervised ML needed** for scale, but requires manual coding first
3. **Multi-modal analysis emerging** — text + images jointly
4. **Reproducibility is major concern** — methods papers often can't be replicated
5. **Theory-method gap** — computational methods often disconnected from communication theory

---

## TODO

- [x] Research data sources
- [x] Research methods (framing, topics, networks)
- [x] Draft initial spec document (43KB)
- [x] Set reminder for 06:00 UTC
- [x] Get Zotero user ID (6345227)
- [x] Fetch and analyze Zotero library
- [x] Save Zotero analysis to ZOTERO_ANALYSIS.md
- [x] Add Telegram data source skill
- [x] Add coordinated behavior detection skill
- [x] Add attention metrics skill
- [x] Add LLM-based annotation skill
- [ ] Add network analysis skill (opinion leadership)
- [ ] Finalize implementation roadmap
- [ ] Create example skill files
- [ ] Final review by 09:00 UTC

---
