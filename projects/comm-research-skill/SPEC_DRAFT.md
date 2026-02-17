# Communication Research Analyst Skill for OpenClaw

## Specification Document v0.1

**Author:** OpenClaw Agent  
**Date:** 2026-02-17  
**Status:** Draft  
**Deadline:** 2026-02-17 09:00 UTC

---

## Executive Summary

This document specifies an OpenClaw skill package that enables AI-assisted computational communication research. Inspired by DAAF (Data Analyst Augmentation Framework), it adapts the multi-agent orchestration pattern for the unique challenges of communication scholarship: unstructured text data, social media APIs, network analysis, and rapidly changing platform ecosystems.

The skill package will support:
- **Data sources**: Reddit, YouTube, TikTok (Research API), Bluesky, Telegram, MediaCloud, GDELT, Internet Archive
- **Methods**: Text analysis (NLP, topic modeling, sentiment), network analysis (coordinated behavior detection, opinion leadership), content analysis, LLM-based annotation
- **Frameworks**: Attention economy, networked publics, coordinated inauthentic behavior, artificial sociality, information diffusion
- **Output**: Reproducible research pipelines with full audit trails

A novel feature enables **Zotero-informed skill generation**: researchers provide access to their reference library, and the system auto-generates domain-specific skills based on methodologies and theories present in their readings.

### Domain Focus (Based on Zotero Analysis)

This skill package is specifically tuned for research on:
1. **Agentic AI in social science** — Using AI agents as research tools while being reflexive about AI's role
2. **Coordinated behavior analysis** — Detecting and analyzing coordinated inauthentic/authentic behavior across platforms
3. **Network analysis of movements** — Opinion leadership, diffusion, temporal dynamics
4. **Attention economy** — How information competes for attention in algorithmic environments
5. **Platform studies** — Telegram, Twitter/X, Reddit, alternative platforms

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Design Philosophy](#2-design-philosophy)
3. [Architecture Overview](#3-architecture-overview)
4. [Agent Definitions](#4-agent-definitions)
5. [Skill Definitions](#5-skill-definitions)
6. [Workflow Stages](#6-workflow-stages)
7. [Data Source Integration](#7-data-source-integration)
8. [Zotero Adapter System](#8-zotero-adapter-system)
9. [Validation & QA System](#9-validation--qa-system)
10. [Output Artifacts](#10-output-artifacts)
11. [OpenClaw Integration](#11-openclaw-integration)
12. [Implementation Roadmap](#12-implementation-roadmap)
13. [Appendices](#13-appendices)

---

## 1. Problem Statement

### 1.1 The Communication Research Context

Communication scholars doing computational social science face distinct challenges:

1. **Data Instability**: Social media APIs change frequently (Twitter Academic API deprecation), requiring constant adaptation
2. **Unstructured Data**: Text, images, networks — not clean tabular datasets
3. **Scale vs. Depth**: Balancing large-scale automated analysis with qualitative rigor
4. **Reproducibility Crisis**: Platform data may become inaccessible; preprocessing decisions are often underdocumented
5. **Methodological Complexity**: Combining NLP, network analysis, and statistical methods requires diverse expertise
6. **Ethical Considerations**: IRB, platform TOS, data retention policies

### 1.2 What DAAF Gets Right

DAAF's architecture addresses core research workflow problems:
- **Every transformation has a validation** — catches errors early
- **Multi-agent specialization** — different "experts" for different tasks
- **File-first execution** — full audit trail, reproducibility
- **Human-in-the-loop** — researcher maintains control at checkpoints
- **Progressive loading** — manages context window efficiently

### 1.3 What Needs Adaptation

| DAAF Assumption | Communication Research Reality |
|-----------------|--------------------------------|
| Clean, tabular data from stable APIs | Messy, multi-format data from unstable APIs |
| Well-documented codebooks | Platform-specific quirks, undocumented behaviors |
| Predictable data structures | JSON blobs, nested objects, missing fields |
| Single data source per analysis | Multi-platform, cross-platform studies |
| Numeric/categorical variables | Text, images, networks, temporal streams |

---

## 2. Design Philosophy

### 2.1 Core Principles

1. **Graceful Degradation**: Expect API failures; build retry logic and fallbacks
2. **Data Preservation**: Archive raw data immediately; platforms may revoke access
3. **Method Transparency**: Every analytical decision documented in plain language
4. **Theory-Method Alignment**: Connect computational methods to communication theories
5. **Reproducibility-First**: Even if APIs change, document everything needed to understand what was done

### 2.2 The Human-AI Partnership

```
┌─────────────────────────────────────────────────────────────────┐
│                     RESEARCHER (Human)                          │
│  • Defines research questions                                   │
│  • Selects theoretical frameworks                               │
│  • Makes interpretive judgments                                 │
│  • Validates findings against domain knowledge                  │
│  • Writes final publications                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│                RESEARCH ANALYST SKILL (AI)                      │
│  • Executes data collection pipelines                           │
│  • Performs preprocessing and cleaning                          │
│  • Runs computational analyses                                  │
│  • Generates visualizations                                     │
│  • Documents methodology exhaustively                           │
│  • Flags anomalies and quality issues                          │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 Key Differentiators from DAAF

| Aspect | DAAF | Comm Research Skill |
|--------|------|---------------------|
| Platform | Claude Code CLI | OpenClaw |
| **Model flexibility** | **Claude only** | **Any model via OpenRouter** |
| Multi-agent | Subagent invocation | sessions_spawn |
| Notification | Terminal output | Telegram/Slack/etc. |
| Data focus | Education (Urban Institute) | Media & social media |
| Domain adaptation | Manual skill creation | Zotero-informed auto-generation |

### 2.4 Multi-Model Architecture (Key Selling Point)

**DAAF's limitation:** Locked to Claude (Opus/Sonnet). Expensive. Single vendor.

**OpenClaw's advantage:** Route different tasks to different models based on:
- **Cost** — Use cheap models for validation, expensive models for reasoning
- **Capability** — Use specialized models for specific tasks
- **Diversity** — Epistemic diversity via multiple model perspectives

#### Recommended Model Allocation

| Task | Model | Rationale |
|------|-------|-----------|
| **Orchestration** | Claude Opus / GPT-4 | Complex coordination, context management |
| **Data validation** | GPT-4o-mini / Gemini Flash | Fast, cheap, sufficient for schema checks |
| **Code generation** | DeepSeek V3 / Claude Sonnet | Strong at code, cheaper than Opus |
| **Text classification** | Gemini Flash / Qwen | Fast batch processing |
| **Adversarial review** | Different model from generator | Avoid self-confirmation bias |
| **Final synthesis** | Claude Opus | Nuanced writing, coherence |

#### Cost Comparison (Estimated)

| Workflow | DAAF (Claude Only) | OpenClaw (Multi-Model) |
|----------|-------------------|------------------------|
| Full pipeline analysis | ~$30-60 | ~$5-15 |
| Simple data validation | ~$2-5 | ~$0.10-0.50 |
| 10 QA review cycles | ~$10-20 | ~$1-3 |

#### Epistemic Diversity

Using multiple models for adversarial review creates genuine diversity:
- Claude finds different issues than GPT-4
- DeepSeek catches different code bugs than Sonnet
- No single model's biases dominate

This is particularly valuable for:
1. **Code review** — Different models catch different bugs
2. **Interpretation** — Multiple "perspectives" on findings
3. **Robustness** — Results that survive multi-model scrutiny are more reliable

#### Implementation

```python
# OpenClaw model routing via config
agents:
  orchestrator:
    model: anthropic/claude-opus-4
  data-collector:
    model: google/gemini-2.0-flash  # Fast, cheap
  text-analyst:
    model: deepseek/deepseek-v3     # Good at code
  code-reviewer:
    model: openai/gpt-4o            # Different from generator
  synthesizer:
    model: anthropic/claude-opus-4  # High quality writing
```

**This is a core value proposition for the academic market:**
- Cheaper than DAAF
- More flexible than DAAF
- Epistemically more robust than single-model systems

---

## 3. Architecture Overview

### 3.1 System Components

```
skills/comm-research/
├── SKILL.md                    # Main orchestrator instructions
├── agents/
│   ├── orchestrator.md         # Main coordinator
│   ├── data-collector.md       # API interaction specialist
│   ├── text-analyst.md         # NLP/text analysis expert
│   ├── network-analyst.md      # Network analysis expert
│   ├── code-reviewer.md        # QA adversarial reviewer
│   ├── planner.md              # Research plan creation
│   └── synthesizer.md          # Report generation
├── workflows/
│   ├── full-pipeline.md        # Complete research workflow
│   ├── discovery.md            # Data availability exploration
│   ├── text-analysis.md        # Text-specific workflow
│   └── network-analysis.md     # Network-specific workflow
├── data-sources/
│   ├── reddit.md               # Reddit API skill
│   ├── youtube.md              # YouTube Data API skill
│   ├── tiktok.md               # TikTok Research API skill
│   ├── bluesky.md              # AT Protocol skill
│   ├── mediacloud.md           # MediaCloud API skill
│   ├── gdelt.md                # GDELT BigQuery skill
│   └── internet-archive.md     # Wayback/TV News skill
├── methods/
│   ├── sentiment-analysis.md   # Sentiment methods
│   ├── topic-modeling.md       # LDA, BERTopic, etc.
│   ├── ner.md                  # Named Entity Recognition
│   ├── network-metrics.md      # Centrality, community detection
│   └── content-analysis.md     # Computational content analysis
├── theories/
│   ├── attention-economy.md    # Attention as scarce resource
│   ├── networked-publics.md    # Network society, publics
│   ├── coordinated-behavior.md # Inauthentic behavior framework
│   ├── artificial-sociality.md # Human-AI interaction
│   └── diffusion.md            # Information diffusion
├── templates/
│   ├── research-plan.md        # Plan document template
│   ├── report.md               # Final report template
│   └── methodology-section.md  # Methods writeup template
├── zotero/
│   ├── adapter.md              # Zotero integration instructions
│   ├── extractor.py            # Method/theory extraction
│   └── skill-generator.py      # Auto-generate skills from papers
└── scripts/
    ├── init-project.sh         # Initialize project folder
    └── archive-data.py         # Data preservation script
```

### 3.2 Agent Coordination Flow

```
                            USER REQUEST
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │     ORCHESTRATOR       │
                    │  (SKILL.md + agents/   │
                    │   orchestrator.md)     │
                    └───────────┬────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
    ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
    │   PLANNER     │   │ DATA-COLLECTOR│   │ TEXT-ANALYST  │
    │ (research     │   │ (API calls,   │   │ (NLP, topic   │
    │  design)      │   │  scraping)    │   │  modeling)    │
    └───────────────┘   └───────────────┘   └───────────────┘
            │                   │                   │
            │                   ▼                   │
            │           ┌───────────────┐           │
            │           │ CODE-REVIEWER │◄──────────┤
            │           │ (adversarial  │           │
            │           │  QA per script│           │
            │           └───────────────┘           │
            │                   │                   │
            ▼                   ▼                   ▼
    ┌─────────────────────────────────────────────────────┐
    │                    SYNTHESIZER                       │
    │            (report generation, findings)             │
    └─────────────────────────────────────────────────────┘
                                │
                                ▼
                            DELIVERY
                    (Telegram notification + files)
```

---

## 4. Agent Definitions

### 4.1 Orchestrator

**Purpose**: Coordinate the research workflow, manage context, enforce quality gates

**Behavioral Protocol**:
```markdown
# Orchestrator Agent

## Identity
You are the Research Coordinator for computational communication research.
You manage the overall workflow, delegate to specialists, and ensure quality.

## Core Responsibilities
1. Classify user requests into engagement modes
2. Invoke appropriate specialist agents via sessions_spawn
3. Enforce validation checkpoints between stages
4. Report progress to user at human checkpoints
5. Maintain STATE.md for session continuity

## Engagement Modes
- **Discovery**: What data is available? Is this feasible?
- **Full Pipeline**: Complete research from question to report
- **Text Analysis**: Focused text/NLP analysis
- **Network Analysis**: Focused network/graph analysis
- **Revision**: Update existing analysis

## Quality Gates
- G1: Research question clarified, scope confirmed
- G2: Data sources identified, APIs accessible
- G3: Data collected, archived, validated
- G4: Analysis complete, QA passed
- G5: Report generated, findings synthesized

## Human Checkpoints
Pause and await user confirmation at:
- After Discovery (before committing to full pipeline)
- After Plan creation (before data collection)
- After data collection (before analysis)
- Before final delivery
```

### 4.2 Data Collector

**Purpose**: Handle all API interactions, data fetching, archival

**Behavioral Protocol**:
```markdown
# Data Collector Agent

## Identity
You are a data acquisition specialist for social media and news data.
You handle API authentication, rate limiting, error recovery, and archival.

## Core Competencies
- Reddit API (PRAW)
- YouTube Data API v3
- TikTok Research API
- Bluesky/AT Protocol
- MediaCloud API
- GDELT BigQuery
- Web scraping (ethical, TOS-compliant)

## Operational Principles
1. **Archive First**: Save raw API responses before any processing
2. **Rate Limit Respect**: Never exceed platform limits; use exponential backoff
3. **Error Logging**: Document all failures with timestamps and error codes
4. **Pagination Handling**: Fetch complete datasets, handle cursors properly
5. **Schema Documentation**: Record data structure received from each API

## Output Format
For each collection task:
- Raw data: data/raw/{source}_{timestamp}.json
- Collection log: logs/collection_{source}.log
- Schema snapshot: docs/schemas/{source}.md
```

### 4.3 Text Analyst

**Purpose**: NLP, text preprocessing, topic modeling, sentiment analysis

**Behavioral Protocol**:
```markdown
# Text Analyst Agent

## Identity
You are a computational text analysis specialist.
You handle NLP pipelines, topic modeling, sentiment analysis, and text classification.

## Core Methods
- Preprocessing: tokenization, lemmatization, stopword removal
- Sentiment: VADER, transformer-based, aspect-based
- Topics: LDA, NMF, BERTopic, Top2Vec
- NER: spaCy, transformers, custom patterns
- Embeddings: sentence-transformers, word2vec
- Classification: supervised ML, zero-shot

## Operational Principles
1. **Preprocessing Transparency**: Document every text transformation
2. **Model Selection Justification**: Explain why this method for this question
3. **Validation Samples**: Show example outputs for human review
4. **Reproducibility**: Set random seeds, save model artifacts

## Output Format
- Processed text: data/processed/text_{task}.parquet
- Model artifacts: models/{method}_{timestamp}/
- Validation samples: output/validation/text_samples.md
```

### 4.4 Network Analyst

**Purpose**: Social network analysis, graph construction, community detection

**Behavioral Protocol**:
```markdown
# Network Analyst Agent

## Identity
You are a social network analysis specialist.
You construct and analyze network graphs from communication data.

## Core Methods
- Graph construction: user-user, user-content, content-content
- Centrality: degree, betweenness, eigenvector, PageRank
- Community: Louvain, Label Propagation, Infomap
- Temporal: dynamic networks, cascades, diffusion
- Bipartite: two-mode projections
- Visualization: force-directed, hierarchical

## Operational Principles
1. **Edge Definition Clarity**: Document what constitutes an edge
2. **Weighted vs. Unweighted**: Justify choice
3. **Directed vs. Undirected**: Justify choice
4. **Sampling Effects**: Document if network is sampled

## Output Format
- Graph files: data/networks/{name}.graphml
- Metrics: output/network_metrics.csv
- Visualizations: output/figures/network_*.png
```

### 4.5 Code Reviewer

**Purpose**: Adversarial QA of all scripts, validation of outputs

**Behavioral Protocol**:
```markdown
# Code Reviewer Agent

## Identity
You are an adversarial code reviewer.
Your job is to find problems, not rubber-stamp work.

## Review Dimensions
1. **Correctness**: Does the code do what it claims?
2. **Data Integrity**: Are transformations preserving/corrupting data?
3. **Methodology**: Is this the right approach for the research question?
4. **Edge Cases**: What happens with missing data, empty responses?
5. **Reproducibility**: Can this be re-run and get same results?

## Severity Levels
- **PASSED**: No issues found
- **WARNING**: Minor issues, document and proceed
- **BLOCKER**: Critical issues, must fix before continuing

## Review Protocol
For each script:
1. Read the script and understand intent
2. Check data transformations for correctness
3. Verify output matches expected format
4. Look for silent failures or data loss
5. Check error handling
6. Write adversarial test cases
7. Issue verdict with reasoning

## Output Format
QA report in scripts/qa/{stage}_{script}_review.md
```

---

## 5. Skill Definitions

### 5.1 Data Source Skills

Each data source gets a dedicated skill file containing:
- API endpoints and authentication
- Rate limits and quotas
- Data schema and fields
- Common issues and workarounds
- Sample collection code

#### 5.1.1 Reddit Skill

```markdown
# Reddit Data Source Skill

## Access
- API: Reddit API via PRAW
- Auth: OAuth2 (client_id, client_secret, user_agent)
- Rate Limit: 60 requests/minute
- Cost: Free

## Endpoints
- Subreddit posts: subreddit.new(), subreddit.hot(), etc.
- Comments: submission.comments
- User data: redditor.submissions, redditor.comments
- Search: reddit.subreddit("all").search()

## Data Schema
Post fields:
- id, title, selftext, author, subreddit
- score, upvote_ratio, num_comments
- created_utc, url, permalink
- is_self, link_flair_text

## Collection Patterns
- Keyword search: subreddit.search(query, time_filter, limit)
- Subreddit monitoring: subreddit.stream.submissions()
- Historical: Use Pushshift API (limited) or PSAW

## Gotchas
- Deleted/removed posts return [deleted]/[removed]
- Rate limits can vary by OAuth scope
- PRAW requires user_agent that identifies your app
- Large subreddits may have millions of posts

## Sample Code
```python
import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="comm_research:v1.0 (by /u/your_username)"
)

posts = []
for post in reddit.subreddit("politics").search("election", limit=1000):
    posts.append({
        "id": post.id,
        "title": post.title,
        "text": post.selftext,
        "author": str(post.author),
        "score": post.score,
        "created_utc": post.created_utc,
        "num_comments": post.num_comments
    })
```
```

#### 5.1.2 MediaCloud Skill

```markdown
# MediaCloud Data Source Skill

## Access
- API: https://search.mediacloud.org/api/
- Auth: API key (free registration)
- Rate Limit: Generous for academic use
- Cost: Free

## Capabilities
- Search 60,000+ news sources globally
- 1 billion+ stories indexed
- Full-text search with date ranges
- Source metadata and collections

## Endpoints
- Search: /search/story/list
- Count: /search/story/count
- Sources: /directory/sources/list
- Collections: /directory/collections/list

## Data Schema
Story fields:
- stories_id, title, url
- publish_date, language
- media_id, media_name, media_url
- word_count

## Collection Patterns
- Topic search with date range
- Source-specific collection
- Language filtering
- Attention over time queries

## Gotchas
- Full text not always available (depends on source)
- Some sources have paywalls
- Date parsing can be tricky for some sources
- Large queries should be paginated
```

#### 5.1.3 Telegram Skill

```markdown
# Telegram Data Source Skill

## Access
- API: Telethon (MTProto) or Pyrogram
- Auth: Phone number + API ID/Hash from my.telegram.org
- Rate Limit: Flood wait applies (~30 requests/30 seconds)
- Cost: Free

## Capabilities
- Public channel message history
- Channel member lists (if permissions allow)
- Message forwarding metadata
- Media attachments
- Temporal message patterns

## Data Schema
Message fields:
- id, message, date
- from_id, peer_id (channel)
- fwd_from (forwarding info — critical for coordination analysis)
- views, forwards, replies
- media, entities (links, mentions)

## Collection Patterns
- Channel history: client.iter_messages(channel, limit=N)
- Forward tracking: msg.fwd_from.channel_id
- Time-windowed collection for coordination detection

## Coordination Detection
Key methodology (per Giglietto et al., Kuznetsova):
1. Collect messages with same URL/content across channels
2. Calculate time delta between shares
3. Construct coordination network (channels as nodes, co-shares as edges)
4. Detect communities of coordinated actors

## Gotchas
- Need to join channels to access history
- Private channels require invitation
- Flood wait errors need exponential backoff
- Account may be restricted if flagged as bot
- Forward metadata crucial for coordination studies

## Sample Code
```python
from telethon import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

async with TelegramClient('session', api_id, api_hash) as client:
    channel = await client.get_entity('channel_username')
    
    messages = []
    async for msg in client.iter_messages(channel, limit=1000):
        messages.append({
            'id': msg.id,
            'text': msg.text,
            'date': msg.date,
            'views': msg.views,
            'forwards': msg.forwards,
            'fwd_from': msg.fwd_from.channel_id if msg.fwd_from else None
        })
```
```

#### 5.1.4 GDELT Skill

```markdown
# GDELT Data Source Skill

## Access
- BigQuery: Direct SQL queries
- CSV: Bulk downloads
- Auth: Google Cloud account (for BigQuery)
- Rate Limit: BigQuery quotas apply
- Cost: BigQuery charges (free tier available)

## Datasets
- GDELT Event Database: 300+ event categories, 1979-present
- Global Knowledge Graph (GKG): Entities, themes, emotions
- Visual GKG: Image analysis metadata
- Special collections: Books, academic literature

## Key Tables (BigQuery)
- `gdelt-bq.gdeltv2.events`: Event records
- `gdelt-bq.gdeltv2.gkg`: Knowledge graph
- `gdelt-bq.gdeltv2.gkg_partitioned`: Partitioned for efficiency

## Update Frequency
- 15 minutes for events and GKG

## Query Patterns
```sql
SELECT 
  SQLDATE, Actor1Name, Actor2Name, 
  EventCode, GoldsteinScale, NumMentions, SourceURL
FROM `gdelt-bq.gdeltv2.events`
WHERE SQLDATE >= 20240101
  AND Actor1CountryCode = 'USA'
LIMIT 10000
```

## Gotchas
- Very large dataset — use filters aggressively
- GKG themes are semicolon-delimited
- Some URLs may be dead
- Event coding can have false positives
```

### 5.2 Method Skills

#### 5.2.1 Coordinated Behavior Detection Skill

```markdown
# Coordinated Behavior Detection Skill

## Overview
Detect coordinated inauthentic (or authentic) behavior across platforms by analyzing
temporal co-sharing patterns, network structure, and content similarity.

Based on: Giglietto et al. (2020), Kuznetsova (2025)

## Methods Available

### Temporal Co-Sharing Detection
Identify accounts/channels sharing same content within short time windows.

**Algorithm:**
1. Collect content with shared URLs, hashtags, or text
2. For each piece of content, find all shares
3. Calculate pairwise time deltas between sharers
4. If delta < threshold (e.g., 60 seconds), flag as potential coordination
5. Build co-sharing network

### Coordination Network Construction
Build network from co-sharing patterns.

**Node types:** Users, channels, pages
**Edge weights:** Number of co-shares, average time delta

### Community Detection in Coordination Networks
Identify clusters of coordinated actors.

**Methods:** Louvain, Label Propagation, Infomap

## Key Metrics
- Coordination score: weighted sum of co-shares / time_delta
- Network density within suspected coordinated groups
- Temporal regularity (variance in posting times)
- Content diversity (do they share same sources?)

## Validation
- Compare to known coordinated campaigns
- Manual review of flagged networks
- Cross-reference with platform takedowns

## Sample Code
```python
import pandas as pd
import networkx as nx
from itertools import combinations
from datetime import timedelta

def detect_coordination(df, time_threshold_seconds=60):
    """
    df: DataFrame with columns ['user', 'content_id', 'timestamp']
    Returns: NetworkX graph of coordinated actors
    """
    G = nx.Graph()
    
    # Group by content
    for content_id, group in df.groupby('content_id'):
        if len(group) < 2:
            continue
        
        # Sort by time
        group = group.sort_values('timestamp')
        
        # Check all pairs
        for (_, row1), (_, row2) in combinations(group.iterrows(), 2):
            delta = abs((row1['timestamp'] - row2['timestamp']).total_seconds())
            
            if delta <= time_threshold_seconds:
                u1, u2 = row1['user'], row2['user']
                if G.has_edge(u1, u2):
                    G[u1][u2]['weight'] += 1
                    G[u1][u2]['avg_delta'] = (G[u1][u2]['avg_delta'] + delta) / 2
                else:
                    G.add_edge(u1, u2, weight=1, avg_delta=delta)
    
    return G
```

## Ethical Considerations
- Coordination is not inherently inauthentic
- Activists coordinate legitimately
- Focus on behavior patterns, not content judgment
- Document methodology transparently
```

#### 5.2.2 Attention Metrics Skill

```markdown
# Attention Metrics Skill

## Overview
Measure and analyze attention allocation in digital environments.

Based on: Herbert Simon's attention economy framework, Qiu et al.

## Metrics

### Engagement Metrics
- **Engagement rate:** (likes + comments + shares) / followers
- **Amplification rate:** shares / followers
- **Conversation rate:** comments / followers
- **Virality coefficient:** secondary shares / primary shares

### Attention Distribution
- **Gini coefficient:** Inequality of attention distribution
- **Power law exponent:** Fit attention to power law
- **Concentration ratio:** % of attention to top N accounts

### Temporal Attention
- **Attention decay:** Half-life of engagement
- **Attention cascade:** Time to peak engagement
- **Sustained attention:** Duration of above-baseline engagement

### Competitive Attention
- **Share of voice:** Account mentions / total mentions
- **Attention flow:** Net gain/loss of attention over time

## Sample Code
```python
import numpy as np
from scipy.stats import gini

def attention_gini(engagement_counts):
    """Calculate Gini coefficient of attention distribution"""
    sorted_counts = np.sort(engagement_counts)
    n = len(sorted_counts)
    cumulative = np.cumsum(sorted_counts)
    return (2 * np.sum((np.arange(1, n+1) * sorted_counts))) / (n * np.sum(sorted_counts)) - (n + 1) / n

def engagement_rate(likes, comments, shares, followers):
    """Calculate engagement rate"""
    if followers == 0:
        return 0
    return (likes + comments + shares) / followers

def attention_halflife(timestamps, engagements):
    """Estimate attention decay half-life"""
    # Fit exponential decay
    from scipy.optimize import curve_fit
    
    def exp_decay(t, a, b):
        return a * np.exp(-b * t)
    
    t = np.array([(ts - timestamps[0]).total_seconds() for ts in timestamps])
    popt, _ = curve_fit(exp_decay, t, engagements, p0=[max(engagements), 0.001])
    
    halflife = np.log(2) / popt[1]
    return halflife
```
```

#### 5.2.3 LLM-Based Annotation Skill

```markdown
# LLM-Based Annotation Skill

## Overview
Use large language models for text classification, coding, and annotation tasks
that traditionally required human coders.

Based on: Davidson & Karell (2025), recent LLM annotation literature

## Methods

### Zero-Shot Classification
Classify text without training examples.

**Use when:**
- Categories are well-defined conceptually
- Human-interpretable labels
- Exploratory analysis

### Few-Shot Classification
Provide examples in prompt.

**Use when:**
- Categories need clarification
- Edge cases exist
- Better accuracy needed

### Chain-of-Thought Annotation
Have LLM explain reasoning before classifying.

**Use when:**
- Transparency required
- Complex judgment calls
- Audit trail needed

## Validation Protocol

### Inter-Rater Reliability with Human Coders
1. Randomly sample N items (recommend: 200-500)
2. Have human coders annotate sample
3. Calculate agreement: Cohen's Kappa, Krippendorff's Alpha
4. Target: α > 0.8 for reliable annotation

### Calibration Testing
1. Test on known-label validation set
2. Calculate precision, recall, F1
3. Check for systematic biases by category

### Prompt Sensitivity Analysis
1. Vary prompt wording
2. Check consistency of classifications
3. Document final prompt in methodology

## Best Practices

1. **Document prompts exhaustively** — Full prompt is part of methods section
2. **Report model and version** — e.g., "GPT-4-turbo, January 2024 snapshot"
3. **Temperature = 0** for classification tasks (deterministic)
4. **Batch with rate limiting** — Avoid API errors
5. **Save raw responses** — Enable re-analysis

## Sample Code
```python
import openai
from tqdm import tqdm

def llm_classify(texts, categories, model="gpt-4", examples=None):
    """
    Zero/few-shot classification with LLM
    """
    system_prompt = f"""You are a content classifier. 
Classify the following text into one of these categories: {', '.join(categories)}.
Respond with ONLY the category name, nothing else."""

    if examples:
        example_text = "\n".join([f"Text: {ex['text']}\nCategory: {ex['label']}" for ex in examples])
        system_prompt += f"\n\nExamples:\n{example_text}"
    
    results = []
    for text in tqdm(texts):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Text: {text}"}
            ],
            temperature=0
        )
        results.append(response.choices[0].message.content.strip())
    
    return results

def calculate_agreement(human_labels, llm_labels):
    """Calculate Cohen's Kappa"""
    from sklearn.metrics import cohen_kappa_score
    return cohen_kappa_score(human_labels, llm_labels)
```

## Ethical Considerations
- LLMs can encode biases
- Validate on diverse samples
- Don't claim LLM annotations are "objective"
- Document limitations in methods section
```

#### 5.2.4 Network Analysis Skill

```markdown
# Network Analysis Skill

## Overview
Construct and analyze social networks from communication data, with focus on
opinion leadership, information diffusion, and community structure.

Based on: Liang & Lee (2023), Gruzd et al. (2011), network science foundations

## Network Construction

### User-User Networks
**Edges from:**
- Replies/mentions
- Retweets/shares
- Follows (if available)
- Co-participation in threads

### User-Content Networks (Bipartite)
**Nodes:** Users + Content items
**Edges:** User interacted with content

### Content-Content Networks
**Edges from:**
- Shared URLs
- Hashtag co-occurrence
- Semantic similarity

## Key Metrics

### Centrality Measures
| Metric | Interpretation | Use Case |
|--------|----------------|----------|
| **Degree** | Number of connections | Raw popularity |
| **Betweenness** | Bridge between communities | Information brokers |
| **Eigenvector** | Connected to well-connected nodes | Elite status |
| **PageRank** | Weighted influence flow | Overall influence |
| **Closeness** | Average distance to all nodes | Information access |

### Opinion Leadership Detection
Per Liang & Lee (2023):

1. **Influence metrics:**
   - In-degree (being replied to)
   - Retweet/share count
   - Thread initiation rate

2. **Stability analysis:**
   - Track leadership over time windows
   - Calculate rank correlation between periods
   - Identify stable vs. transient leaders

3. **Characteristic predictors:**
   - Activity level
   - Content type
   - Account age
   - Network position

### Community Detection
| Algorithm | Strengths | Use When |
|-----------|-----------|----------|
| **Louvain** | Fast, good quality | Large networks |
| **Label Propagation** | Very fast | Exploratory |
| **Infomap** | Information-theoretic | Flow dynamics matter |
| **Leiden** | Improved Louvain | Need guaranteed connectivity |

### Temporal Network Analysis
- **Snapshot approach:** Network per time window
- **Event-based:** Edges have timestamps
- **Dynamic community tracking:** Label matching across snapshots

## Sample Code

```python
import networkx as nx
import pandas as pd
from community import community_louvain

def build_interaction_network(interactions_df):
    """
    Build network from interaction data.
    interactions_df: columns ['source', 'target', 'timestamp', 'type']
    """
    G = nx.DiGraph()
    
    for _, row in interactions_df.iterrows():
        if G.has_edge(row['source'], row['target']):
            G[row['source']][row['target']]['weight'] += 1
        else:
            G.add_edge(row['source'], row['target'], weight=1)
    
    return G

def calculate_opinion_leadership(G):
    """Calculate multiple centrality measures for opinion leadership."""
    metrics = pd.DataFrame(index=G.nodes())
    
    metrics['in_degree'] = pd.Series(dict(G.in_degree()))
    metrics['out_degree'] = pd.Series(dict(G.out_degree()))
    metrics['pagerank'] = pd.Series(nx.pagerank(G))
    metrics['betweenness'] = pd.Series(nx.betweenness_centrality(G))
    
    # Composite leadership score
    metrics['leadership_score'] = (
        metrics['in_degree'].rank(pct=True) * 0.3 +
        metrics['pagerank'].rank(pct=True) * 0.4 +
        metrics['betweenness'].rank(pct=True) * 0.3
    )
    
    return metrics.sort_values('leadership_score', ascending=False)

def track_leadership_stability(G_snapshots):
    """
    Track stability of opinion leadership across time windows.
    G_snapshots: list of (timestamp, Graph) tuples
    """
    from scipy.stats import spearmanr
    
    leadership_over_time = []
    for ts, G in G_snapshots:
        leaders = calculate_opinion_leadership(G)
        leaders['timestamp'] = ts
        leadership_over_time.append(leaders)
    
    # Calculate rank correlations between adjacent periods
    correlations = []
    for i in range(len(leadership_over_time) - 1):
        df1 = leadership_over_time[i]
        df2 = leadership_over_time[i + 1]
        
        common = set(df1.index) & set(df2.index)
        if len(common) > 10:
            r, p = spearmanr(
                df1.loc[list(common), 'leadership_score'],
                df2.loc[list(common), 'leadership_score']
            )
            correlations.append({'period': i, 'correlation': r, 'p_value': p})
    
    return pd.DataFrame(correlations)

def detect_communities(G, method='louvain'):
    """Detect communities in network."""
    if method == 'louvain':
        partition = community_louvain.best_partition(G.to_undirected())
        return partition
    elif method == 'label_propagation':
        communities = nx.community.label_propagation_communities(G.to_undirected())
        partition = {}
        for i, comm in enumerate(communities):
            for node in comm:
                partition[node] = i
        return partition
    else:
        raise ValueError(f"Unknown method: {method}")
```

## Visualization

### Network Layouts
- **Force-directed (Fruchterman-Reingold):** General purpose
- **Circular:** Show community structure
- **Hierarchical:** Show influence flow

### Recommended Tools
- `pyvis` — Interactive HTML networks
- `Gephi` — Publication-quality static images
- `networkx` + `matplotlib` — Quick exploration

## Validation
- Compare centrality rankings to ground truth (if available)
- Check community quality (modularity score)
- Validate temporal patterns against known events
```

#### 5.2.5 Topic Modeling Skill

```markdown
# Topic Modeling Skill

## Methods Available

### LDA (Latent Dirichlet Allocation)
- Library: gensim
- Use when: Interpretable topics needed, moderate corpus size
- Preprocessing: Required (tokenization, stopwords, etc.)

### BERTopic
- Library: bertopic
- Use when: Neural embeddings desired, larger corpus
- Preprocessing: Minimal (handles tokenization)

### Top2Vec
- Library: top2vec
- Use when: Automatic topic number detection needed
- Preprocessing: Minimal

## Selection Criteria
| Criterion | LDA | BERTopic | Top2Vec |
|-----------|-----|----------|---------|
| Interpretability | High | Medium | Medium |
| Corpus size | <100k docs | Any | Any |
| Preprocessing | Heavy | Light | Light |
| Speed | Fast | Medium | Slow |
| Topic coherence | Good | Better | Good |

## Validation Protocol
1. Coherence scores (C_v, NPMI)
2. Human topic labeling sample
3. Document-topic distribution review
4. Perplexity (for LDA)

## Sample Code (BERTopic)
```python
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

# Use a model appropriate for your domain
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

topic_model = BERTopic(
    embedding_model=embedding_model,
    nr_topics="auto",
    calculate_probabilities=True
)

topics, probs = topic_model.fit_transform(documents)

# Get topic info
topic_info = topic_model.get_topic_info()
```
```

### 5.3 Theory/Framework Skills

These skills provide theoretical grounding for research design and interpretation.

#### 5.3.1 Attention Economy Skill

```markdown
# Attention Economy Framework Skill

## Core Concept
"What information consumes is rather obvious: it consumes the attention of 
its recipients." — Herbert Simon

In information-rich environments, attention becomes the scarce resource.

## Key Principles

1. **Attention scarcity**: Finite human attention vs. infinite information
2. **Competition for attention**: Content competes for limited attention slots
3. **Attention inequality**: Power-law distribution of attention
4. **Cognitive biases**: Mental shortcuts determine attention allocation
5. **Algorithmic mediation**: Platforms shape attention flows

## Research Applications

### Measurement
- Engagement metrics as attention proxies
- Attention Gini coefficient
- Time-on-content measures
- Scroll depth, dwell time

### Analysis Questions
- How is attention distributed across actors?
- What content features predict attention capture?
- How do algorithms shape attention allocation?
- What are consequences of attention inequality?

### Methodological Implications
- High-attention content ≠ high-quality content
- Viral spread reflects attention dynamics, not truth
- Platform metrics are attention metrics, not impact metrics

## Key Citations
- Simon, H. A. (1971). Designing organizations for an information-rich world.
- Wu, T. (2016). The Attention Merchants.
- Qiu, J. et al. - Attention economy and misinformation
```

#### 5.3.2 Networked Publics Skill

```markdown
# Networked Publics Framework Skill

## Core Concept
Publics that are restructured by networked technologies, exhibiting new 
dynamics of visibility, spreadability, and participation.

## Key Properties (boyd, 2010)
1. **Persistence**: Content is recorded and archived
2. **Replicability**: Content can be copied perfectly
3. **Scalability**: Potential for massive visibility
4. **Searchability**: Content can be found via search

## Dynamics
1. **Invisible audiences**: Can't see who's watching
2. **Collapsed contexts**: Multiple audiences in one space
3. **Blurred public/private**: Boundaries unclear

## Research Applications

### Network Analysis
- How do network structures shape public discourse?
- Who are the bridges between communities?
- How do information cascades form?

### Platform Studies
- How do platform affordances shape publics?
- What publics form around specific platforms?
- How do algorithmic feeds reshape publics?

### Movement Studies
- How do networked publics enable collective action?
- What is the role of "leaderless" organization?
- How does microcelebrity activism work?

## Key Citations
- Castells, M. (2000). The Rise of the Network Society.
- boyd, d. (2010). Social network sites as networked publics.
- Papacharissi, Z. (2015). Affective Publics.
```

#### 5.3.3 Coordinated Behavior Framework Skill

```markdown
# Coordinated Behavior Framework Skill

## Core Concept
Coordinated inauthentic behavior (CIB) refers to organized efforts to 
manipulate public discourse through coordinated action that obscures 
the true actors or their coordination.

## Key Distinctions

| Type | Authentic | Inauthentic |
|------|-----------|-------------|
| **Coordinated** | Social movements, advocacy campaigns | Astroturfing, state-sponsored ops |
| **Organic** | Individual expression | - |

## Detection Signals

### Temporal Signals
- Synchronized posting times
- Unusually rapid content sharing
- Coordinated bursts of activity

### Network Signals
- Dense interconnection among actors
- Unusual follower/following patterns
- Coordinated amplification networks

### Content Signals
- Identical or near-identical content
- Shared URLs across accounts
- Hashtag coordination

### Behavioral Signals
- Account creation patterns
- Activity timing (working hours in specific timezone)
- Engagement patterns

## Methodological Framework (Giglietto et al.)

1. **Data collection**: Gather content with shared identifiers (URLs, hashtags)
2. **Co-sharing detection**: Identify accounts sharing same content rapidly
3. **Network construction**: Build network from co-sharing patterns
4. **Community detection**: Find clusters of coordinated actors
5. **Validation**: Manual review of flagged networks

## Ethical Considerations
- Coordination ≠ inauthenticity (activists coordinate legitimately)
- Avoid false positives that harm legitimate actors
- Document methodology transparently
- Focus on behavior patterns, not content judgment

## Key Citations
- Giglietto, F. et al. (2020). It takes a village to manipulate the media.
- Kuznetsova, D. (2025). Amplifying the regime.
- Starbird, K. et al. - Information operations research
```

#### 5.3.4 Artificial Sociality Skill

```markdown
# Artificial Sociality Framework Skill

## Core Concept
The study of social interaction between humans and artificial agents,
and the authenticity/inauthenticity dynamics that emerge.

## Key Concepts

### Meta-Authenticity
"The flexible, co-constructive process of self-referential (in)authenticity 
performances" — where artificial actors perform authenticity while 
acknowledging their artificiality.

### Machine Fluency
The skill of effectively instructing AI agents to align with one's objectives.
A new source of heterogeneity in AI-mediated outcomes.

### Agentic Attention
How AI agents mediate and allocate attention on behalf of humans.

## Research Applications

### Virtual Influencers
- How do audiences engage with known-artificial personas?
- What authenticity performances do VI creators construct?
- What are ethical implications of artificial sociality at scale?

### AI-Mediated Communication
- How do AI agents shape human-human communication?
- What happens when AI agents interact with each other?
- How does "machine fluency" create new inequalities?

### Research Tools (Meta-Level)
- How does using AI agents for research change the research?
- What are the reflexive implications of agentic research tools?
- How do we maintain human oversight in AI-augmented research?

## Key Citations
- Meta-authenticity framework (from your Zotero)
- Imas et al. - Human differences in AI agent interactions
- Davidson & Karell (2025) - GenAI in social science research
```

---

## 6. Workflow Stages

### 6.1 Full Pipeline Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: SCOPING & DESIGN                                       │
├─────────────────────────────────────────────────────────────────┤
│  Stage 1: Research Question Intake                              │
│      ├─ Parse user request                                      │
│      ├─ Identify theoretical framework                          │
│      ├─ Clarify scope (time range, platforms, keywords)         │
│      └─ Gate G1: Question + scope confirmed                     │
│                                                                 │
│  Stage 2: Data Source Discovery                                 │
│      ├─ Check API availability                                  │
│      ├─ Estimate data volume                                    │
│      ├─ Identify collection challenges                          │
│      └─ Gate G2: Sources confirmed, access verified             │
│                                                                 │
│  Stage 3: Research Plan Creation                                │
│      ├─ Document methodology decisions                          │
│      ├─ Define analysis pipeline                                │
│      ├─ Create project folder structure                         │
│      └─ Gate G3: Plan approved by user                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ★ HUMAN CHECKPOINT 1 ★
                    (Review and approve plan)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: DATA COLLECTION                                        │
├─────────────────────────────────────────────────────────────────┤
│  Stage 4: API Collection                                        │
│      ├─ Execute collection scripts                              │
│      ├─ Handle rate limits and errors                           │
│      ├─ Archive raw responses immediately                       │
│      └─ Gate G4: Raw data archived, collection log complete     │
│                                                                 │
│  Stage 4-QA: Collection Validation                              │
│      ├─ Verify expected volume                                  │
│      ├─ Check schema consistency                                │
│      ├─ Sample data for quality                                 │
│      └─ Gate G4-QA: Validation passed                           │
│                                                                 │
│  Stage 5: Preprocessing                                         │
│      ├─ Parse and normalize data                                │
│      ├─ Handle missing/malformed fields                         │
│      ├─ Text cleaning (if applicable)                           │
│      └─ Gate G5: Processed data saved, transformations logged   │
│                                                                 │
│  Stage 5-QA: Preprocessing Validation                           │
│      ├─ Compare raw vs processed counts                         │
│      ├─ Check for data loss                                     │
│      ├─ Validate text cleaning                                  │
│      └─ Gate G5-QA: Validation passed                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ★ HUMAN CHECKPOINT 2 ★
                    (Review data quality metrics)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: ANALYSIS                                               │
├─────────────────────────────────────────────────────────────────┤
│  Stage 6: Primary Analysis                                      │
│      ├─ Execute analysis scripts (text/network/mixed)           │
│      ├─ Per-script QA loop                                      │
│      ├─ Save intermediate results                               │
│      └─ Gate G6: Analysis complete, all scripts QA'd            │
│                                                                 │
│  Stage 7: Visualization                                         │
│      ├─ Generate figures                                        │
│      ├─ Create summary statistics                               │
│      └─ Gate G7: Figures saved, captions drafted                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ★ HUMAN CHECKPOINT 3 ★
                    (Review analysis results)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: SYNTHESIS & DELIVERY                                   │
├─────────────────────────────────────────────────────────────────┤
│  Stage 8: Report Generation                                     │
│      ├─ Synthesize findings                                     │
│      ├─ Write methodology section                               │
│      ├─ Document limitations                                    │
│      └─ Gate G8: Report draft complete                          │
│                                                                 │
│  Stage 9: Final Review                                          │
│      ├─ Cross-check findings against data                       │
│      ├─ Verify all citations and references                     │
│      ├─ Compile LEARNINGS.md                                    │
│      └─ Gate G9: Final review passed                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                          DELIVERY
                (Notify user via Telegram + file paths)
```

### 6.2 Per-Script QA Loop (Critical)

Every analysis script follows this pattern:

```
For each script in analysis pipeline:
    │
    ├─ 1. Analyst agent writes script
    │      └─ Save to scripts/{stage}_{name}.py
    │
    ├─ 2. Execute script
    │      └─ Capture output to logs/{script}_output.log
    │
    ├─ 3. Code-reviewer agent reviews (adversarial)
    │      └─ Save review to scripts/qa/{script}_review.md
    │
    ├─ 4. Evaluate verdict
    │      ├─ PASSED → Continue to next script
    │      ├─ WARNING → Log and continue
    │      └─ BLOCKER → Revise and re-review (max 2 attempts)
    │
    └─ 5. Update STATE.md with script status
```

---

## 7. Data Source Integration

### 7.1 Available Sources (2026)

| Source | Access Level | API Cost | Python Library | Data Type |
|--------|--------------|----------|----------------|-----------|
| Reddit | Open | Free | `praw` | Posts, comments, users |
| YouTube | Open | Free (quota) | `google-api-python-client` | Videos, comments, channels |
| TikTok | Research | Free (apply) | `tiktokapi` / custom | Videos, users, hashtags |
| Bluesky | Open | Free | `atproto` | Posts, follows, feeds |
| Mastodon | Open | Free | `Mastodon.py` | Posts, users, instance-specific |
| MediaCloud | Open | Free | `mediacloud` | News articles, sources |
| GDELT | Open | BigQuery costs | `google-cloud-bigquery` | Events, GKG, visual |
| Internet Archive | Open | Free | `waybackpy`, custom | Historical web, TV news |
| Common Crawl | Open | Storage costs | `warcio` | Web crawl archives |

### 7.2 Deprecated/Expensive Sources

| Source | Status | Notes |
|--------|--------|-------|
| Twitter/X | Expensive | $100/mo Basic tier, Academic API deprecated |
| Meta/Facebook | Restricted | Research API via SOMAR/ICPSR application |
| Instagram | Restricted | Via Meta Content Library |
| LinkedIn | Restricted | No public research API |

### 7.3 Pre-Built Datasets

For when live API access isn't needed:

| Repository | Content | Access |
|------------|---------|--------|
| SNAP Stanford | Social network graphs | Direct download |
| Harvard Dataverse | Research datasets | Direct download |
| SOMAR/ICPSR | Social media archives | Application required |
| DocNow Catalog | Tweet ID collections | Direct download |
| HuggingFace Datasets | NLP datasets | `datasets` library |
| Kaggle | Various | `kaggle` API |

---

## 8. Zotero Adapter System

### 8.1 Concept

The Zotero Adapter reads a researcher's reference library and auto-generates domain-specific skills. This enables:
- Automatic identification of methods used in the field
- Extraction of theoretical frameworks
- Discovery of common data sources
- Building a citation network of the researcher's area

### 8.2 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     ZOTERO ADAPTER                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────┐ │
│  │ Zotero API  │───▶│  Extractor  │───▶│  Skill Generator    │ │
│  │ (fetch items│    │ (parse      │    │ (create .md files   │ │
│  │  + PDFs)    │    │  methods,   │    │  for methods,       │ │
│  └─────────────┘    │  theories)  │    │  theories)          │ │
│                     └─────────────┘    └─────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.3 Extraction Pipeline

```python
# Pseudo-code for Zotero extraction

def extract_from_library(user_id, api_key):
    # 1. Fetch all items
    items = zotero_api.get_all_items(user_id, api_key)
    
    # 2. For each paper, extract metadata
    papers = []
    for item in items:
        paper = {
            "title": item.get("title"),
            "abstract": item.get("abstractNote"),
            "year": item.get("date"),
            "tags": item.get("tags"),
            "doi": item.get("DOI")
        }
        
        # 3. If PDF attached, extract full text
        if has_pdf(item):
            paper["full_text"] = extract_pdf_text(item)
        
        papers.append(paper)
    
    # 4. Use LLM to extract methods and theories
    for paper in papers:
        paper["methods"] = llm_extract_methods(paper)
        paper["theories"] = llm_extract_theories(paper)
        paper["data_sources"] = llm_extract_data_sources(paper)
    
    # 5. Aggregate across papers
    method_counts = aggregate_methods(papers)
    theory_counts = aggregate_theories(papers)
    
    # 6. Generate skill files
    for method, count in method_counts.items():
        if count >= threshold:
            generate_method_skill(method, papers)
    
    return generated_skills
```

### 8.4 LLM Extraction Prompts

For method extraction:
```
Analyze this academic paper abstract and identify:
1. Research methods used (e.g., "topic modeling", "content analysis", "network analysis")
2. Specific tools or libraries mentioned (e.g., "LIWC", "spaCy", "Gephi")
3. Data sources (e.g., "Twitter", "news articles", "survey data")

Abstract: {abstract}

Return as JSON:
{
  "methods": ["method1", "method2"],
  "tools": ["tool1", "tool2"],
  "data_sources": ["source1", "source2"]
}
```

For theory extraction:
```
Analyze this academic paper abstract and identify:
1. Theoretical frameworks referenced (e.g., "agenda setting", "framing theory")
2. Key concepts being studied (e.g., "polarization", "misinformation")
3. Communication subfield (e.g., "political communication", "health communication")

Abstract: {abstract}

Return as JSON:
{
  "theories": ["theory1", "theory2"],
  "concepts": ["concept1", "concept2"],
  "subfield": "subfield_name"
}
```

### 8.5 Full Extraction Implementation

```python
#!/usr/bin/env python3
"""
Zotero Library Analyzer for Communication Research Skill
Extracts methods, theories, and data sources from researcher's library.
"""

import os
import json
import re
from pyzotero import zotero
from collections import Counter
from typing import List, Dict, Any

class ZoteroAnalyzer:
    def __init__(self, user_id: str, api_key: str):
        self.zot = zotero.Zotero(user_id, 'user', api_key)
        self.items = []
        self.methods = Counter()
        self.theories = Counter()
        self.data_sources = Counter()
        self.platforms = Counter()
    
    def fetch_library(self, limit: int = 500):
        """Fetch all items from library."""
        self.items = self.zot.everything(self.zot.top())
        print(f"Fetched {len(self.items)} items")
        return self.items
    
    def extract_from_item(self, item: Dict) -> Dict:
        """Extract methods, theories, sources from single item."""
        data = item.get('data', {})
        
        text_to_analyze = ' '.join([
            data.get('title', ''),
            data.get('abstractNote', ''),
            ' '.join([t.get('tag', '') for t in data.get('tags', [])])
        ]).lower()
        
        extracted = {
            'methods': [],
            'theories': [],
            'data_sources': [],
            'platforms': []
        }
        
        # Method detection patterns
        method_patterns = {
            'network analysis': r'network analysis|social network|graph analysis|centrality',
            'content analysis': r'content analysis|coding scheme|intercoder',
            'topic modeling': r'topic model|lda|latent dirichlet|bertopic',
            'sentiment analysis': r'sentiment|opinion mining|polarity',
            'machine learning': r'machine learning|classifier|supervised|random forest',
            'llm annotation': r'llm|large language model|gpt|claude|chatgpt',
            'coordinated behavior': r'coordinat\w+ (inauthentic|behavior)|astroturf',
            'survey': r'survey|questionnaire|likert',
            'experiment': r'experiment|treatment|control group|rct',
            'agent simulation': r'agent.based|simulation|abm',
        }
        
        for method, pattern in method_patterns.items():
            if re.search(pattern, text_to_analyze):
                extracted['methods'].append(method)
        
        # Theory detection patterns
        theory_patterns = {
            'attention economy': r'attention econom|attention scarc|herbert simon',
            'networked publics': r'networked public|network society|castells',
            'framing': r'framing theory|frame analysis|entman',
            'agenda setting': r'agenda.setting|mccombs',
            'diffusion': r'diffusion|cascade|viral spread|contagion',
            'echo chambers': r'echo chamber|filter bubble|polarization',
            'platform governance': r'platform governance|content moderation',
        }
        
        for theory, pattern in theory_patterns.items():
            if re.search(pattern, text_to_analyze):
                extracted['theories'].append(theory)
        
        # Platform detection
        platforms = ['twitter', 'facebook', 'reddit', 'telegram', 'youtube', 
                    'tiktok', 'instagram', 'weibo', 'whatsapp', 'bluesky']
        for platform in platforms:
            if platform in text_to_analyze:
                extracted['platforms'].append(platform)
        
        # Data source detection
        sources = ['mediacloud', 'gdelt', 'crowdtangle', 'academic api',
                  'pushshift', 'common crawl', 'internet archive']
        for source in sources:
            if source in text_to_analyze:
                extracted['data_sources'].append(source)
        
        return extracted
    
    def analyze_library(self) -> Dict:
        """Analyze entire library and aggregate findings."""
        for item in self.items:
            if item.get('data', {}).get('itemType') == 'attachment':
                continue
            
            extracted = self.extract_from_item(item)
            
            for method in extracted['methods']:
                self.methods[method] += 1
            for theory in extracted['theories']:
                self.theories[theory] += 1
            for source in extracted['data_sources']:
                self.data_sources[source] += 1
            for platform in extracted['platforms']:
                self.platforms[platform] += 1
        
        return {
            'total_items': len([i for i in self.items 
                               if i.get('data', {}).get('itemType') != 'attachment']),
            'methods': dict(self.methods.most_common()),
            'theories': dict(self.theories.most_common()),
            'data_sources': dict(self.data_sources.most_common()),
            'platforms': dict(self.platforms.most_common()),
        }
    
    def generate_skill_recommendations(self) -> List[str]:
        """Generate skill recommendations based on library analysis."""
        recommendations = []
        
        # Method-based recommendations
        if self.methods['network analysis'] >= 3:
            recommendations.append('network-analysis.md (high priority)')
        if self.methods['coordinated behavior'] >= 2:
            recommendations.append('coordinated-behavior.md (high priority)')
        if self.methods['topic modeling'] >= 3:
            recommendations.append('topic-modeling.md (standard)')
        if self.methods['llm annotation'] >= 2:
            recommendations.append('llm-annotation.md (emerging method)')
        
        # Platform-based recommendations
        for platform, count in self.platforms.most_common(3):
            if count >= 3:
                recommendations.append(f'{platform}-data-source.md (frequently used)')
        
        return recommendations
    
    def export_analysis(self, output_path: str):
        """Export analysis to markdown file."""
        analysis = self.analyze_library()
        recommendations = self.generate_skill_recommendations()
        
        md = f"""# Zotero Library Analysis

## Overview
- **Total items analyzed:** {analysis['total_items']}
- **Analysis date:** {__import__('datetime').datetime.now().isoformat()}

## Methods Detected

| Method | Count |
|--------|-------|
"""
        for method, count in analysis['methods'].items():
            md += f"| {method} | {count} |\n"
        
        md += """
## Theories/Frameworks Detected

| Theory | Count |
|--------|-------|
"""
        for theory, count in analysis['theories'].items():
            md += f"| {theory} | {count} |\n"
        
        md += """
## Platforms Studied

| Platform | Count |
|----------|-------|
"""
        for platform, count in analysis['platforms'].items():
            md += f"| {platform} | {count} |\n"
        
        md += """
## Recommended Skills

Based on your library, prioritize these skills:

"""
        for rec in recommendations:
            md += f"- {rec}\n"
        
        with open(output_path, 'w') as f:
            f.write(md)
        
        return md


# CLI usage
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--user-id', required=True)
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--output', default='zotero_analysis.md')
    args = parser.parse_args()
    
    analyzer = ZoteroAnalyzer(args.user_id, args.api_key)
    analyzer.fetch_library()
    analyzer.export_analysis(args.output)
    print(f"Analysis exported to {args.output}")
```

### 8.6 Generated Skill Example

After processing a library heavy in coordinated behavior research:

```markdown
# Framing Analysis Skill (Auto-Generated)

## Source
Generated from Zotero library analysis
Papers referenced: 23
Last updated: 2026-02-17

## Overview
Framing analysis examines how issues are presented in media, focusing on
selection and salience of certain aspects of reality.

## Common Methods in This Library
1. Manual coding with intercoder reliability (15 papers)
2. Automated frame detection via ML (8 papers)
3. Keyword/dictionary approaches (5 papers)

## Key Citations
- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm.
- Chong, D., & Druckman, J. N. (2007). Framing theory.
- Baden, C. (2010). Communication, contextualization, & cognition.

## Recommended Approach
Based on methods in your library, consider:
1. Develop codebook with frame definitions
2. Use supervised ML to scale manual coding
3. Validate with human coders on sample

## Related Skills
- content-analysis.md
- sentiment-analysis.md
- political-communication.md
```

---

## 9. Validation & QA System

### 9.1 Validation Checkpoints

| Checkpoint | Stage | What's Validated |
|------------|-------|------------------|
| CP1 | Data Collection | API response validity, expected volume |
| CP2 | Preprocessing | Data integrity, no silent drops |
| CP3 | Analysis | Method appropriateness, statistical validity |
| CP4 | Visualization | Figure accuracy, proper labeling |
| CP5 | Report | Findings match data, citations correct |

### 9.2 QA Severity Levels

```
PASSED
  │── No issues found
  └── Proceed immediately

WARNING
  │── Minor issues
  │── Document in STATE.md
  └── Proceed with notation

BLOCKER
  │── Critical issues
  │── Must fix before proceeding
  └── Max 2 revision attempts, then escalate to user
```

### 9.3 Common Validation Failures

| Failure Type | Detection | Resolution |
|--------------|-----------|------------|
| API rate limit exceeded | HTTP 429 | Exponential backoff, resume later |
| Missing data fields | Schema validation | Impute, drop, or flag for manual review |
| Encoding errors | Parse exceptions | Try UTF-8, Latin-1, error handling |
| Empty responses | Zero-length check | Verify query, check API status |
| Duplicate records | ID uniqueness | Deduplicate, log count |
| Text truncation | Length comparison | Fetch full text if available |

---

## 10. Output Artifacts

### 10.1 Project Folder Structure

```
research/
└── {YYYY-MM-DD}_{project_name}/
    ├── README.md              # Project overview
    ├── PLAN.md                # Research plan
    ├── STATE.md               # Session state tracking
    ├── LEARNINGS.md           # Lessons learned
    ├── REPORT.md              # Final report
    │
    ├── data/
    │   ├── raw/               # Untouched API responses
    │   │   ├── reddit_2026-02-17.json
    │   │   └── mediacloud_2026-02-17.json
    │   ├── processed/         # Cleaned, transformed data
    │   │   ├── corpus.parquet
    │   │   └── network.graphml
    │   └── metadata/          # Data documentation
    │       └── schema.md
    │
    ├── scripts/
    │   ├── 01_collect.py
    │   ├── 02_preprocess.py
    │   ├── 03_analyze.py
    │   └── qa/                # QA review reports
    │       ├── 01_collect_review.md
    │       └── 02_preprocess_review.md
    │
    ├── models/                # Saved ML models
    │   └── topic_model/
    │
    ├── output/
    │   ├── figures/           # Visualizations
    │   │   ├── topic_dist.png
    │   │   └── network_graph.png
    │   └── tables/            # Summary statistics
    │       └── descriptives.csv
    │
    └── logs/
        ├── collection.log
        └── analysis.log
```

### 10.2 Report Template

```markdown
# {Project Title}

## Executive Summary
{Brief overview of research question, methods, and key findings}

## 1. Introduction
### 1.1 Research Question
{Clear statement of what was investigated}

### 1.2 Theoretical Framework
{Communication theories/concepts guiding the analysis}

## 2. Data & Methods
### 2.1 Data Sources
{Platforms, time range, sample size}

### 2.2 Data Collection
{API used, collection procedure, ethical considerations}

### 2.3 Analysis Methods
{NLP methods, network methods, statistical approaches}

## 3. Results
### 3.1 Descriptive Statistics
{Overview of the data}

### 3.2 Main Findings
{Key results with figures}

## 4. Discussion
### 4.1 Interpretation
{What the findings mean}

### 4.2 Limitations
{Data limitations, method limitations, generalizability}

## 5. Conclusion
{Summary and implications}

## Appendix
### A. Data Schema
### B. Full Variable List
### C. Robustness Checks

## References
```

---

## 11. OpenClaw Integration

### 11.1 Installation

```bash
# Clone skill into OpenClaw workspace
cd ~/.openclaw/workspace/skills/
git clone https://github.com/your-repo/comm-research comm-research

# Or manually create structure
mkdir -p comm-research/{agents,workflows,data-sources,methods,templates,zotero}
```

### 11.2 SKILL.md Entry Point

```markdown
# Communication Research Analyst Skill

## Trigger Patterns
- "analyze {topic} on {platform}"
- "research {phenomenon}"
- "what data is available for {topic}"
- "run topic modeling on {corpus}"
- "network analysis of {dataset}"

## Engagement Modes

### Discovery
Trigger: "what data", "is it possible", "feasibility"
Action: Check API availability, estimate volume

### Full Pipeline
Trigger: "analyze", "research", "study"
Action: Complete research workflow (see workflows/full-pipeline.md)

### Text Analysis
Trigger: "topic modeling", "sentiment", "content analysis"
Action: Text-focused workflow (see workflows/text-analysis.md)

### Network Analysis
Trigger: "network", "graph", "connections"
Action: Network-focused workflow (see workflows/network-analysis.md)

## Agent Invocation
Use sessions_spawn to invoke specialist agents:
- Planner: "Create research plan for {request}"
- Data Collector: "Collect {source} data for {query}"
- Text Analyst: "Run {method} on {corpus}"
- Network Analyst: "Analyze network structure of {data}"
- Code Reviewer: "Review script at {path}"
- Synthesizer: "Generate report from {artifacts}"

## Human Checkpoints
Notify user via Telegram at each checkpoint.
Wait for explicit confirmation before proceeding.

## Project Initialization
For each new analysis:
1. Create folder: research/{date}_{name}/
2. Initialize: PLAN.md, STATE.md, LEARNINGS.md
3. Create subfolders: data/, scripts/, output/, logs/
```

### 11.3 Sessions Spawn Examples

```python
# Invoking the planner agent
sessions_spawn(
    task="Create a research plan for analyzing political discourse on Reddit r/politics during the 2024 election",
    agentId="comm-research-planner",
    label="planner-session"
)

# Invoking the data collector
sessions_spawn(
    task="Collect Reddit posts from r/politics containing 'election' from 2024-01-01 to 2024-11-30",
    agentId="comm-research-collector",
    label="collector-session"
)

# Invoking the text analyst
sessions_spawn(
    task="Run BERTopic topic modeling on the collected Reddit corpus",
    agentId="comm-research-text",
    label="text-session"
)
```

### 11.4 Telegram Notifications

At each human checkpoint, send notification:

```python
# Using OpenClaw message tool
message(
    action="send",
    target="user_id",
    message="""
📊 **Research Checkpoint: Plan Complete**

Project: Political Discourse Analysis
Stage: Plan Creation (3/9)

**Summary:**
- Data source: Reddit r/politics
- Time range: Jan-Nov 2024
- Estimated posts: ~50,000
- Methods: BERTopic + sentiment

**Action Required:**
Reply "approve" to proceed with data collection
Reply "revise" to modify the plan

[View Plan](file://research/2024-politics/PLAN.md)
    """
)
```

---

## 12. Implementation Roadmap

### Phase 1: Core Framework (Week 1)
- [ ] Create skill folder structure
- [ ] Write SKILL.md orchestrator
- [ ] Implement basic agents (orchestrator, planner, synthesizer)
- [ ] Create project initialization scripts
- [ ] Test basic workflow with mock data

### Phase 2: Data Sources (Week 2)
- [ ] Reddit skill (PRAW integration)
- [ ] MediaCloud skill (API integration)
- [ ] GDELT skill (BigQuery integration)
- [ ] Test data collection pipelines

### Phase 3: Analysis Methods (Week 3)
- [ ] Text analyst agent (sentiment, topics)
- [ ] Network analyst agent (graphs, communities)
- [ ] Code reviewer agent (QA protocol)
- [ ] Validation checkpoint system

### Phase 4: Zotero Integration (Week 4)
- [ ] Zotero API connection
- [ ] Method/theory extraction pipeline
- [ ] Auto-generation of domain skills
- [ ] Testing with real library

### Phase 5: Polish & Documentation (Week 5)
- [ ] Report templates
- [ ] User documentation
- [ ] Example workflows
- [ ] Publish to GitHub/ClawhHub

---

## 13. Appendices

### A. Python Dependencies

```
# Data collection
praw>=7.7.0
google-api-python-client>=2.100.0
atproto>=0.0.30
mediacloud>=4.0.0
google-cloud-bigquery>=3.12.0
waybackpy>=3.0.0

# Text analysis
spacy>=3.7.0
transformers>=4.35.0
sentence-transformers>=2.2.0
bertopic>=0.15.0
gensim>=4.3.0
nltk>=3.8.0
vaderSentiment>=3.3.2

# Network analysis
networkx>=3.2.0
igraph>=0.11.0
pyvis>=0.3.0

# Data processing
polars>=0.19.0
pandas>=2.1.0
numpy>=1.26.0

# Visualization
plotnine>=0.12.0
matplotlib>=3.8.0
seaborn>=0.13.0
plotly>=5.18.0

# Utilities
pyzotero>=1.5.0
requests>=2.31.0
tqdm>=4.66.0
```

### B. Zotero API Reference

```
Base URL: https://api.zotero.org

Endpoints:
- GET /users/{userID}/items - List all items
- GET /users/{userID}/collections - List collections
- GET /users/{userID}/items/{itemKey}/file - Get attached file

Headers:
- Zotero-API-Key: {api_key}
- Zotero-API-Version: 3

Rate Limits:
- Generous for authenticated requests
- Check X-RateLimit-* headers
```

### C. Communication Journals for Reference

Computational Communication Research venues:
- Computational Communication Research (CCR)
- Journal of Communication
- Communication Research
- Political Communication
- New Media & Society
- Social Media + Society
- Journal of Computer-Mediated Communication

### D. Glossary

- **API**: Application Programming Interface
- **BERTopic**: Neural topic modeling using BERT embeddings
- **GKG**: Global Knowledge Graph (GDELT)
- **IRB**: Institutional Review Board
- **LDA**: Latent Dirichlet Allocation
- **NER**: Named Entity Recognition
- **NLP**: Natural Language Processing
- **PRAW**: Python Reddit API Wrapper
- **TOS**: Terms of Service

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-02-17 | Initial draft |

---

*Document generated by OpenClaw Agent*
*For questions or feedback, contact the repository maintainer*
