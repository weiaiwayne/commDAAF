# Data Access Strategy for the Post-API Era

**Reality Check:** The "collect data via API" era is over for most platforms. This workflow helps you find realistic paths to data.

---

## The Current Landscape (2026)

| Platform | API Status | Cost | Realistic Access |
|----------|------------|------|------------------|
| **X/Twitter** | Pro tier required | $5,000/mo | Archives, partnerships only |
| **Reddit** | Restricted | $$$$ | Limited API, archives |
| **Meta (FB/IG)** | Content Library | Free but gated | Application, 6-12 week wait |
| **TikTok** | Research API | Free but gated | Application, restrictions |
| **YouTube** | Data API | Free | Works, quota limits |
| **Telegram** | Open | Free | Works well |
| **Bluesky** | Open | Free | Works well |
| **Mastodon** | Open | Free | Works well |

---

## Decision Tree: How to Get Your Data

```
START: I need data from [platform]

├─ Q1: Does a suitable dataset ALREADY EXIST?
│   │
│   ├─ YES → Use existing dataset (Section 1)
│   │        • Faster
│   │        • Peer-reviewed collection methods
│   │        • Citeable
│   │
│   └─ NO/UNSURE → Check archives first (Section 1)
│
├─ Q2: Is the platform OPEN PROTOCOL?
│   │
│   ├─ YES (Bluesky, Mastodon, Telegram) → Collect directly (Section 2)
│   │
│   └─ NO → Continue to Q3
│
├─ Q3: Does a RESEARCH API exist?
│   │
│   ├─ YES (Meta, TikTok) → Apply for access (Section 3)
│   │   • Meta Content Library: 6-12 weeks
│   │   • TikTok Research API: 4-8 weeks
│   │
│   └─ NO/TOO EXPENSIVE → Continue to Q4
│
├─ Q4: Can you use ALTERNATIVE DATA?
│   │
│   ├─ YES → Consider:
│   │   • Different platform with similar population
│   │   • Survey-embedded data collection
│   │   • Data donation from participants
│   │
│   └─ NO → You may need to:
│       • Revise research question
│       • Partner with platform
│       • Wait for regulatory access (DSA Art. 40)
```

---

## Section 1: Existing Datasets

### Where to Find Them

#### General Archives
| Repository | URL | Strengths |
|------------|-----|-----------|
| **Harvard Dataverse** | dataverse.harvard.edu | Social science, versioned |
| **ICPSR** | icpsr.umich.edu | Survey + social media |
| **Zenodo** | zenodo.org | Open, DOIs |
| **OSF** | osf.io | Pre-reg + data |
| **Kaggle** | kaggle.com/datasets | ML-oriented |

#### Platform-Specific
| Platform | Archive | Notes |
|----------|---------|-------|
| **Twitter/X** | DocNow Catalog | Tweet IDs (need API to hydrate) |
| | Internet Archive | Historical streams |
| | ICWSM datasets | Conference-shared |
| **Reddit** | Pushshift (archived) | Historical dumps to 2023 |
| | Academic Torrents | Large dumps |
| **YouTube** | YouTube-8M | Video features |
| **News** | MediaCloud | News coverage |
| | GDELT | Global events |

#### Event-Specific Collections
- **Elections:** Harvard/MIT Election Data + Science Lab
- **COVID-19:** COVIDLies, AYLIEN COVID News
- **Misinformation:** FakeNewsNet, LIAR dataset
- **Climate:** Climate Feedback datasets

### Evaluating Existing Datasets

Before using, verify:

```yaml
dataset_evaluation:
  questions:
    - Is the time period appropriate for my RQ?
    - Is the sampling method documented?
    - Are there known biases?
    - Is the collection method replicable?
    - Is there a DOI/citation?
    - What's the data format?
    - Are there usage restrictions?
    
  red_flags:
    - Collection method not documented
    - Unclear sampling
    - No versioning
    - "Scraped from API" without details
```

### Citing Datasets

Always cite data separately from papers about the data:

```bibtex
@dataset{chen2024twitterelection,
  author = {Chen, Emily and Ferrara, Emilio},
  title = {2024 US Election Twitter Dataset},
  year = {2024},
  publisher = {Harvard Dataverse},
  doi = {10.7910/DVN/XXXXX}
}
```

---

## Section 2: Open Protocol Platforms

### Bluesky (AT Protocol)

**Status:** Fully open, growing research community

```python
# No authentication needed for public data
import requests

def search_bluesky(query, limit=100):
    """Search Bluesky posts."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"
    params = {"q": query, "limit": min(limit, 100)}
    
    response = requests.get(url, params=params)
    return response.json()

def get_user_posts(handle, limit=100):
    """Get posts from a user."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
    params = {"actor": handle, "limit": min(limit, 100)}
    
    response = requests.get(url, params=params)
    return response.json()
```

**Advantages:**
- No API key required
- No rate limits (be respectful)
- Full data access
- Growing political discourse

**Limitations:**
- Smaller user base (but growing)
- Skews tech-savvy, political

### Mastodon/Fediverse

**Status:** Fully open, decentralized

```python
from mastodon import Mastodon

def search_mastodon(instance, query, limit=100):
    """Search posts on a Mastodon instance."""
    # No auth needed for public search
    api = Mastodon(api_base_url=f"https://{instance}")
    
    results = api.search_v2(query, result_type='statuses')
    return results['statuses'][:limit]
```

**Note:** Must query each instance separately or use relay.

### Telegram

**Status:** Open for public groups/channels

```python
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

async def collect_channel(client, channel_username, limit=1000):
    """Collect messages from public channel."""
    channel = await client.get_entity(channel_username)
    
    messages = []
    async for message in client.iter_messages(channel, limit=limit):
        messages.append({
            'id': message.id,
            'date': message.date,
            'text': message.text,
            'views': message.views,
            'forwards': message.forwards
        })
    
    return messages
```

**Note:** Requires Telegram account. Private groups need invitation.

---

## Section 3: Research API Applications

### Meta Content Library

**What it provides:**
- Facebook public pages, groups
- Instagram public posts
- Historical data back to 2019

**Application process:**
1. Go to: `developers.facebook.com/docs/content-library`
2. Verify academic affiliation
3. Submit research proposal
4. Wait 6-12 weeks
5. Access via Meta's research environment (no data export)

**Template: Meta Research Application**
```
Research Title: [Title]

Principal Investigator: [Name, Institution]

Research Questions:
1. [RQ1]
2. [RQ2]

Data Needed:
- Platform(s): Facebook / Instagram / Both
- Content type: Posts / Comments / Both
- Time period: [Start] to [End]
- Geographic scope: [Countries]
- Keywords/pages: [Specifics]

Methodology:
[Brief description]

IRB Status: [Approved / Exempt / Pending]

Data Security:
[How you'll protect data]

Publication Plan:
[Where you intend to publish]
```

### TikTok Research API

**What it provides:**
- Public video metadata
- Limited content access
- User statistics

**Application:**
1. Go to: `developers.tiktok.com/research`
2. Academic verification required
3. Submit proposal
4. Wait 4-8 weeks

**Restrictions:**
- US/EU researchers only (currently)
- Approved topics only
- No bulk download
- Must use their query interface

---

## Section 4: Alternative Approaches

### Survey-Embedded Collection

When you can't access platform data, have participants share:

```
Study Design:
1. Recruit participants (e.g., Prolific)
2. Ask permission to access their data
3. They export their data (GDPR right!)
4. They upload to your study

Advantages:
- Legally clean
- Consent is explicit
- Can get private data with permission

Disadvantages:
- Small samples
- Self-selection bias
- Labor-intensive
```

### Data Donation

Participants voluntarily share their data:

```python
# Example: Browser extension approach

# 1. User installs extension
# 2. Extension captures their feed/timeline
# 3. Data sent to research server with consent

# Projects doing this:
# - Algorithm Watch (platform auditing)
# - Mozilla Rally
# - NYU Ad Observatory
```

### DSA Article 40 (EU)

The Digital Services Act requires platforms to provide researcher access:

**Status (2026):** Implementation ongoing

**How to request:**
1. Be EU-based or EU-affiliated researcher
2. Submit vetted researcher application
3. Request specific data through platform's DSA portal
4. Access within regulatory framework

**Reality:** Platforms are slow-walking this. Works better for large institutions.

---

## Section 5: When You Can't Get the Data

### Revise the Research Question

Sometimes the honest answer is: **you can't study this with available data.**

```
Original RQ: "How does Instagram's algorithm affect body image?"

Problem: No Instagram research access

Options:
1. Study Bluesky/Mastodon instead (different population)
2. Study historical Instagram data (old datasets)
3. Survey-based: ask people about their experience
4. Lab study: show people curated feeds
5. Different RQ: "Body image discourse on open platforms"
```

### Document the Access Attempt

For publications, document what you tried:

```markdown
## Data Access

We attempted to collect Instagram data through Meta's Content Library 
(application submitted March 2026) but had not received access by the 
study deadline. We therefore used [alternative] which may limit 
generalizability to Instagram specifically.
```

### Consider Platform Partnership

For large projects:
- Industry-academic partnerships
- Platform research programs
- Data-sharing MOUs

These take 6-12 months to establish but provide better access.

---

## Quick Reference: What's Actually Accessible (2026)

### ✅ Just Works
- Bluesky (fully open)
- Mastodon (fully open)
- Telegram (public channels)
- YouTube (with quotas)
- GDELT (news events)
- MediaCloud (news)

### ⏳ Requires Application
- Meta Content Library (6-12 weeks)
- TikTok Research API (4-8 weeks)

### 💰 Expensive
- X/Twitter ($5K/mo minimum)
- Reddit (negotiated pricing)

### 🚫 Effectively Inaccessible
- Instagram (without Meta Content Library)
- WhatsApp (encrypted)
- Snapchat (no research access)
- Private Facebook groups

---

## Workflow Integration

Before any data collection task, the system should:

```python
def precheck_data_access(platform, research_question):
    """Check data access feasibility before planning."""
    
    if platform in OPEN_PLATFORMS:
        return {
            'status': 'PROCEED',
            'method': 'direct_collection',
            'notes': f'{platform} is openly accessible'
        }
    
    if platform in GATED_PLATFORMS:
        return {
            'status': 'CHECK_ACCESS',
            'questions': [
                f'Do you have {platform} research API access?',
                f'Have you applied? When?',
                f'Would existing datasets work instead?'
            ]
        }
    
    if platform in EXPENSIVE_PLATFORMS:
        return {
            'status': 'COST_WARNING',
            'message': f'{platform} requires paid API access (${COSTS[platform]}/mo)',
            'alternatives': suggest_alternatives(platform)
        }
    
    return {
        'status': 'NOT_ACCESSIBLE',
        'message': f'{platform} is not accessible for research',
        'alternatives': suggest_alternatives(platform)
    }
```

---

*This document reflects the data access landscape as of February 2026. Platform policies change frequently—verify current status before planning studies.*
