# TikTok Data Collection Skill

Collect and analyze TikTok data via available methods.

## ⚠️ Current Status (2026)

TikTok is now the **dominant platform for political content** among under-35 audiences. Yet research access remains challenging:

| Method | Status | Access Level |
|--------|--------|--------------|
| **Research API** | Active, restricted | Approved researchers only |
| **Creative Center** | Public | Trends, limited data |
| **Existing Datasets** | Available | Historical, specific topics |
| **Third-party** | Risky | ToS violations, unreliable |

---

## Official Research API

### Eligibility
- Academic researchers at accredited institutions
- US, EU, and select other countries
- Approved research topics
- IRB/ethics approval required

### Application Process
1. Go to: `developers.tiktok.com/products/research-api`
2. Create developer account
3. Submit research proposal:
   - Research questions
   - Methodology
   - Data security plan
   - IRB documentation
4. Wait 4-8 weeks for review
5. If approved: sandbox access, then production

### API Capabilities
```python
# TikTok Research API provides query-based access
# No bulk download—must query through their interface

# Available endpoints:
# - Video search (by hashtag, keyword, date)
# - User info (public profiles)
# - Video metadata (views, likes, shares, comments count)
# - Comments (limited)

# NOT available:
# - Full video download
# - Private accounts
# - DMs
# - Algorithm/recommendation data
```

### Basic Usage
```python
import requests

class TikTokResearchAPI:
    def __init__(self, client_key, client_secret):
        self.base_url = "https://open.tiktokapis.com/v2"
        self.token = self._get_token(client_key, client_secret)
    
    def _get_token(self, key, secret):
        """Get OAuth token."""
        response = requests.post(
            "https://open.tiktokapis.com/v2/oauth/token/",
            data={
                "client_key": key,
                "client_secret": secret,
                "grant_type": "client_credentials"
            }
        )
        return response.json()["access_token"]
    
    def search_videos(self, query, start_date, end_date, max_count=100):
        """
        Search videos by query.
        
        Note: Research API has specific query syntax.
        """
        headers = {"Authorization": f"Bearer {self.token}"}
        
        payload = {
            "query": {
                "and": [
                    {"field": "keyword", "value": query}
                ]
            },
            "start_date": start_date,  # YYYYMMDD
            "end_date": end_date,
            "max_count": min(max_count, 100)
        }
        
        response = requests.post(
            f"{self.base_url}/research/video/query/",
            headers=headers,
            json=payload
        )
        
        return response.json()
    
    def get_video_comments(self, video_id, max_count=100):
        """Get comments on a video."""
        headers = {"Authorization": f"Bearer {self.token}"}
        
        response = requests.post(
            f"{self.base_url}/research/video/comment/list/",
            headers=headers,
            json={
                "video_id": video_id,
                "max_count": min(max_count, 100)
            }
        )
        
        return response.json()
```

### Query Syntax
```python
# Single keyword
query = {"field": "keyword", "value": "climate change"}

# Hashtag
query = {"field": "hashtag", "value": "fyp"}

# Multiple conditions (AND)
query = {
    "and": [
        {"field": "keyword", "value": "election"},
        {"field": "region", "value": "US"}
    ]
}

# OR conditions
query = {
    "or": [
        {"field": "hashtag", "value": "trump"},
        {"field": "hashtag", "value": "biden"}
    ]
}
```

### Rate Limits
- 1,000 requests per day
- 100 videos per request
- Maximum 1 year historical data

---

## TikTok Creative Center (Public)

### What's Available
The Creative Center provides trend data without API approval:
- Trending hashtags
- Trending songs
- Top videos by category
- Regional trends

### Access
```python
import requests
from bs4 import BeautifulSoup

def get_trending_hashtags(region='US'):
    """
    Scrape trending hashtags from Creative Center.
    Note: Web scraping—check ToS and be respectful.
    """
    url = f"https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en?region={region}"
    
    # This requires browser automation or careful request handling
    # Creative Center uses dynamic loading
    
    # Alternative: Use their public data exports if available
    pass
```

### Limitations
- No historical depth
- No post-level data
- Aggregated trends only
- Changes frequently

---

## Existing Datasets

### Academic Datasets

| Dataset | Content | Access |
|---------|---------|--------|
| **TikTok Videos Dataset (NUS)** | 10M+ video metadata | Academic request |
| **TikTok COVID-19 Dataset** | Pandemic content | Zenodo |
| **TikTok Misinformation Dataset** | Labeled misinfo | Paper authors |
| **TikHarm** | Harmful content detection | Academic request |

### Finding Datasets
```python
# Search academic repositories
repositories = [
    "https://dataverse.harvard.edu",
    "https://zenodo.org",
    "https://osf.io",
    "https://paperswithcode.com/datasets"
]

# Common search terms:
# "TikTok dataset"
# "short video social media dataset"
# "TikTok [topic]"  # e.g., "TikTok election"
```

### Using Existing Data
```python
import pandas as pd

def load_tiktok_dataset(path):
    """Load and validate TikTok dataset."""
    
    df = pd.read_csv(path)
    
    # Common TikTok data schema
    expected_cols = [
        'video_id',
        'author_id', 
        'create_time',
        'desc',  # video description/caption
        'music_id',
        'hashtags',
        'play_count',
        'like_count',
        'comment_count',
        'share_count'
    ]
    
    # Check what's available
    available = [c for c in expected_cols if c in df.columns]
    missing = [c for c in expected_cols if c not in df.columns]
    
    print(f"Available fields: {available}")
    print(f"Missing fields: {missing}")
    
    return df
```

---

## Third-Party Approaches (⚠️ Caution)

### Web Scraping Tools

**Warning:** These may violate ToS and break frequently.

```python
# Tools that exist (use at your own risk):
# - TikTok-Api (unofficial Python library)
# - tiktok-scraper (Node.js)
# - Various browser automation approaches

# Example (may not work/be ToS compliant):
# from TikTokApi import TikTokApi

# Generally NOT recommended for academic research:
# - Unreliable
# - ToS violation
# - IP blocking
# - Data quality issues
# - Ethical concerns
```

### Better Alternatives

Instead of scraping:
1. Apply for Research API (4-8 weeks)
2. Use existing datasets
3. Partner with researchers who have access
4. Survey-based: ask users about their experience
5. Content analysis of videos (downloaded with consent)

---

## Platform-Specific Considerations

### Content Characteristics
- **Short-form video:** 15-180 seconds (mostly <60s)
- **Heavy audio use:** Music, sounds, voiceovers
- **Visual-first:** Text often overlaid on video
- **Algorithm-driven:** "For You Page" is primary interface
- **Duets/Stitches:** Response videos are common

### Analysis Challenges

1. **Video Content**
   - Can't analyze video with text methods
   - Need: transcription, visual analysis, or metadata only
   
2. **Audio/Music**
   - Same audio = same "sound" (trending sounds)
   - Audio carries meaning (irony, context)
   
3. **Text is Minimal**
   - Captions are short
   - Hashtags dominate
   - Real content is in video

4. **Recommendation Algorithm**
   - Virality != organic popularity
   - Same video, different reach by user
   - Hard to measure "true" engagement

### Analysis Strategies

```python
def analyze_tiktok_metadata(df):
    """Metadata-based analysis (no video content needed)."""
    
    # Hashtag analysis
    hashtags = df['hashtags'].str.split(',').explode()
    hashtag_counts = hashtags.value_counts()
    
    # Engagement metrics
    df['engagement_rate'] = (
        df['like_count'] + df['comment_count'] + df['share_count']
    ) / df['play_count']
    
    # Temporal patterns
    df['hour'] = pd.to_datetime(df['create_time']).dt.hour
    df['day'] = pd.to_datetime(df['create_time']).dt.dayofweek
    
    # Sound/music analysis
    sound_counts = df['music_id'].value_counts()
    
    return {
        'top_hashtags': hashtag_counts.head(50),
        'avg_engagement': df['engagement_rate'].mean(),
        'top_sounds': sound_counts.head(20),
        'posting_patterns': df.groupby(['day', 'hour']).size()
    }

def analyze_tiktok_with_transcription(video_paths, model='whisper'):
    """Transcribe videos for text analysis."""
    import whisper
    
    model = whisper.load_model("base")
    
    transcripts = []
    for path in video_paths:
        result = model.transcribe(path)
        transcripts.append({
            'path': path,
            'text': result['text'],
            'language': result['language']
        })
    
    return transcripts
```

---

## Research Applications

### Political Communication
- Election misinformation spread
- Candidate messaging strategies
- Youth political engagement
- Political influencer networks

### Health Communication  
- Health misinformation (vaccines, treatments)
- Health advice quality
- Crisis communication
- Mental health content

### Media Studies
- Creator economy dynamics
- Algorithmic amplification
- Cross-platform content flow
- Trend lifecycle

### Coordinated Behavior
- Hashtag hijacking
- Coordinated commenting
- Sound-based coordination
- Cross-platform campaigns

---

## Network Construction for TikTok

Unlike Twitter (retweets) or Facebook (shares), TikTok networks are built differently:

```python
def build_tiktok_network(df, network_type='sound'):
    """
    Build network from TikTok data.
    
    Network types:
    - 'sound': Users connected if they use same sound
    - 'hashtag': Users connected if they use same hashtag
    - 'duet': Users connected by duet/stitch relationships
    - 'mention': Users connected by @mentions in captions
    """
    import networkx as nx
    
    G = nx.Graph()
    
    if network_type == 'sound':
        # Users sharing same sound
        for sound_id, group in df.groupby('music_id'):
            users = group['author_id'].unique()
            for i, u1 in enumerate(users):
                for u2 in users[i+1:]:
                    if G.has_edge(u1, u2):
                        G[u1][u2]['weight'] += 1
                    else:
                        G.add_edge(u1, u2, weight=1)
    
    elif network_type == 'hashtag':
        # Users sharing same hashtags
        for hashtag, group in df.explode('hashtags').groupby('hashtags'):
            users = group['author_id'].unique()
            for i, u1 in enumerate(users):
                for u2 in users[i+1:]:
                    if G.has_edge(u1, u2):
                        G[u1][u2]['weight'] += 1
                    else:
                        G.add_edge(u1, u2, weight=1)
    
    return G
```

---

## Cost-Benefit Analysis

| Approach | Cost | Data Access | Reliability | Ethics |
|----------|------|-------------|-------------|--------|
| Research API | Free (time) | Query-based | High | Clean |
| Creative Center | Free | Trends only | Medium | Clean |
| Existing datasets | Free | Fixed scope | High | Clean |
| Scraping | Free | Varies | Low | Risky |
| Survey-based | $$ | User-reported | Medium | Clean |

---

## Recommendations by Research Type

### For Trend Analysis
→ Creative Center + existing datasets

### For Content Analysis
→ Research API (if approved) + transcription

### For Network Analysis
→ Research API hashtag/sound queries

### For Longitudinal Studies
→ Existing datasets (limited) or start collection now

### For Comparative (TikTok vs other platforms)
→ Combine TikTok datasets with Twitter/Bluesky collection

---

## Ethical Considerations

1. **User Expectations**
   - TikTok users expect public posts to be seen
   - But not necessarily scraped/analyzed at scale
   - Young user base: extra sensitivity

2. **Content Sensitivity**
   - Much personal/vulnerable content
   - Body image, mental health, identity
   - Be careful with examples in papers

3. **Creator Attribution**
   - Creators are often identifiable
   - Quoting = potentially identifying
   - Consider: aggregate vs individual analysis

4. **Algorithm Influence**
   - "Viral" ≠ "popular"
   - Algorithmic amplification affects metrics
   - Report this limitation

---

## Key Citations

- Zulli, D., & Zulli, D. J. (2022). Extending the Internet meme: Conceptualizing technological mimesis and imitation publics on the TikTok platform. *New Media & Society*.

- Guinaudeau, B., Votta, F., & Munger, K. (2022). Fifteen seconds of fame: TikTok and the supply side of social video. *Computational Communication Research*.

- Zeng, J., & Abidin, C. (2021). '#OkBoomer, time to meet the Zoomers': studying the memefication of intergenerational politics on TikTok. *Information, Communication & Society*.

---

*Part of Communication Research Skill for OpenClaw*
