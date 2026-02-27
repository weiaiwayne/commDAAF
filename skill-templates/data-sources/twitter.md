# Twitter/X Data Collection Skill

Collect and analyze Twitter/X data via available methods.

## ⚠️ Current API Landscape (2026)

Twitter/X API access has changed significantly:
- **Academic Research API**: Deprecated
- **Basic tier**: $100/month, limited access
- **Pro tier**: $5,000/month
- **Enterprise**: Custom pricing

**Alternatives covered in this skill:**
1. Official API (if budget allows)
2. Historical datasets (existing archives)
3. Third-party tools
4. Related platform migration (Bluesky, Mastodon)

## Official API Access

### Setup (If Using Official API)
```bash
pip install tweepy

# Bearer token from developer.twitter.com
export TWITTER_BEARER_TOKEN="your-token"
```

### Basic Search (v2 API)
```python
import tweepy
import os

def init_client():
    """Initialize Twitter API v2 client."""
    return tweepy.Client(
        bearer_token=os.environ['TWITTER_BEARER_TOKEN'],
        wait_on_rate_limit=True
    )

def search_tweets(query, max_results=100, start_time=None, end_time=None):
    """
    Search recent tweets (Basic tier: 7 days back).
    
    Args:
        query: Search query (operators: AND, OR, -exclude, from:, to:, etc.)
        max_results: Maximum tweets to return
        start_time: Start datetime (ISO format)
        end_time: End datetime (ISO format)
    """
    client = init_client()
    
    tweets = []
    
    for tweet in tweepy.Paginator(
        client.search_recent_tweets,
        query=query,
        tweet_fields=['created_at', 'public_metrics', 'author_id', 'conversation_id'],
        user_fields=['username', 'public_metrics', 'verified'],
        expansions=['author_id'],
        max_results=min(100, max_results),
        start_time=start_time,
        end_time=end_time
    ).flatten(limit=max_results):
        tweets.append(tweet)
    
    return tweets
```

### Get User Tweets
```python
def get_user_tweets(username, max_results=100):
    """Get recent tweets from a user."""
    client = init_client()
    
    # Get user ID
    user = client.get_user(username=username)
    if not user.data:
        return []
    
    tweets = []
    for tweet in tweepy.Paginator(
        client.get_users_tweets,
        id=user.data.id,
        tweet_fields=['created_at', 'public_metrics'],
        max_results=min(100, max_results)
    ).flatten(limit=max_results):
        tweets.append(tweet)
    
    return tweets
```

### Get Followers/Following
```python
def get_followers(username, max_results=1000):
    """Get user's followers."""
    client = init_client()
    
    user = client.get_user(username=username)
    if not user.data:
        return []
    
    followers = []
    for follower in tweepy.Paginator(
        client.get_users_followers,
        id=user.data.id,
        user_fields=['public_metrics', 'created_at', 'description'],
        max_results=min(1000, max_results)
    ).flatten(limit=max_results):
        followers.append(follower)
    
    return followers
```

## Historical Datasets

For research not requiring real-time data, use existing archives:

### DocNow Tweet ID Catalogs
```python
# DocNow maintains collections of tweet IDs for research events
# https://catalog.docnow.io/

# You can "hydrate" IDs if you have API access:
def hydrate_tweet_ids(tweet_ids, batch_size=100):
    """Hydrate tweet IDs to full tweet objects."""
    client = init_client()
    
    tweets = []
    for i in range(0, len(tweet_ids), batch_size):
        batch = tweet_ids[i:i+batch_size]
        response = client.get_tweets(
            ids=batch,
            tweet_fields=['created_at', 'public_metrics', 'author_id']
        )
        if response.data:
            tweets.extend(response.data)
    
    return tweets
```

### Internet Archive Twitter Collections
```python
# Archive.org has Twitter stream samples
# https://archive.org/details/twitterstream

import requests
from io import BytesIO
import gzip
import json

def load_archive_sample(url):
    """Load Twitter archive sample."""
    response = requests.get(url)
    
    tweets = []
    with gzip.open(BytesIO(response.content), 'rt') as f:
        for line in f:
            if line.strip():
                tweets.append(json.loads(line))
    
    return tweets
```

### Academic Datasets
- **Harvard Dataverse**: Various Twitter research datasets
- **ICPSR**: Social media research archives
- **Zenodo**: Researcher-shared datasets

## Third-Party Approaches

### Nitter Instances (Read-only scraping)
```python
# Note: Check ToS and legal considerations
# Nitter provides RSS feeds of public accounts

import feedparser

def get_nitter_feed(username, instance='nitter.net'):
    """Get tweets via Nitter RSS (public accounts only)."""
    url = f"https://{instance}/{username}/rss"
    feed = feedparser.parse(url)
    
    tweets = []
    for entry in feed.entries:
        tweets.append({
            'text': entry.summary,
            'published': entry.published,
            'link': entry.link
        })
    
    return tweets
```

### snscrape (Historical, may break)
```python
# pip install snscrape
# Note: May not work reliably, check status

import snscrape.modules.twitter as sntwitter

def scrape_tweets(query, limit=100):
    """Scrape tweets using snscrape."""
    tweets = []
    
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append({
            'id': tweet.id,
            'date': tweet.date,
            'content': tweet.rawContent,
            'user': tweet.user.username,
            'retweets': tweet.retweetCount,
            'likes': tweet.likeCount
        })
    
    return tweets
```

## Migration Tracking

Many Twitter users have migrated to alternative platforms:

### Track Migration to Bluesky
```python
# Cross-reference usernames
def find_bluesky_account(twitter_username):
    """Check if Twitter user has Bluesky account."""
    import requests
    
    # Try common patterns
    possible_handles = [
        f"{twitter_username}.bsky.social",
        twitter_username.replace('_', '')  + ".bsky.social"
    ]
    
    for handle in possible_handles:
        url = f"https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile"
        response = requests.get(url, params={'actor': handle})
        if response.status_code == 200:
            return response.json()
    
    return None
```

## Research Applications

### Political Communication (230 papers in your library)
- Election discourse analysis
- Political elite communication
- Campaign messaging

### Misinformation (100 papers)
- False claim propagation
- Correction effectiveness
- Bot/coordination detection

### Journalism (238 papers)
- News diffusion
- Source credibility
- Breaking news dynamics

### Network Analysis (145 papers)
- Retweet networks
- Mention networks
- Follower networks
- Information cascades

## Query Syntax

```python
# Boolean operators
query = "(climate OR warming) -hoax"

# User filters
query = "from:username"
query = "to:username"

# Engagement filters (may require higher tier)
query = "min_retweets:100"
query = "min_faves:500"

# Media filters
query = "has:images"
query = "has:videos"
query = "has:links"

# Conversation filter
query = "conversation_id:123456"
```

## Data Schema

### Tweet Object (v2 API)
```python
{
    'id': str,
    'text': str,
    'author_id': str,
    'created_at': datetime,
    'conversation_id': str,
    'in_reply_to_user_id': Optional[str],
    'public_metrics': {
        'retweet_count': int,
        'reply_count': int,
        'like_count': int,
        'quote_count': int
    },
    'entities': {
        'mentions': List[dict],
        'hashtags': List[dict],
        'urls': List[dict]
    }
}
```

## Cost-Benefit Analysis

| Approach | Cost | Data Access | Reliability |
|----------|------|-------------|-------------|
| Official API Basic | $100/mo | 7 days, limited | High |
| Official API Pro | $5,000/mo | 30 days, full | High |
| Historical datasets | Free | Past events | High |
| Nitter/scraping | Free | Current, limited | Low |
| Alternative platforms | Free | Current, growing | Medium |

## Recommendations

Given API costs, consider:

1. **Historical research** → Use existing archives (DocNow, Internet Archive)
2. **Real-time monitoring** → Consider Bluesky/Mastodon for new studies
3. **Specific events** → Budget for limited API access
4. **Network studies** → Combine historical data with alternative platforms

## Ethical Considerations

- Respect platform ToS changes
- Consider user consent expectations
- Deleted tweets may appear in archives
- Private accounts require explicit consent
- Document data collection methods precisely

## Workflow Integration

```yaml
# Spawn Twitter collection agent
sessions_spawn:
  task: "Search Twitter archives for [topic] in [date_range]"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash
```

## Key Citations (From Your Library)

*Twitter appears in 293 of your papers — add key citations here*

- Bruns, A., & Burgess, J. (2011). The use of Twitter hashtags in the formation of ad hoc publics.
- Bakshy, E., et al. (2015). Exposure to ideologically diverse news and opinion on Facebook.

---
*Part of Communication Research Skill for OpenClaw*
