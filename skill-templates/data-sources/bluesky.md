# Bluesky Data Collection Skill

Collect and analyze Bluesky data via the AT Protocol.

## Overview

Bluesky is a decentralized social network built on the AT Protocol. Key features for researchers:
- Open protocol with public data
- No API costs or rate limits (currently)
- Growing platform for studying decentralized social media
- Migrating users from Twitter/X

## API Access

### No Authentication Required (Public Data)
```python
# Public API endpoints - no auth needed
BASE_URL = "https://public.api.bsky.app"
```

### With Authentication (For posting, follows, etc.)
```bash
# Install
pip install atproto

# Get app password from: bsky.app → Settings → App Passwords
```

## Data Collection Patterns

### 1. Search Posts
```python
import requests
from datetime import datetime, timedelta

def search_posts(query, limit=100, sort='latest'):
    """Search Bluesky posts."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"
    
    posts = []
    cursor = None
    
    while len(posts) < limit:
        params = {
            'q': query,
            'limit': min(100, limit - len(posts)),
            'sort': sort  # 'latest' or 'top'
        }
        if cursor:
            params['cursor'] = cursor
            
        response = requests.get(url, params=params)
        data = response.json()
        
        posts.extend(data.get('posts', []))
        cursor = data.get('cursor')
        
        if not cursor:
            break
    
    return posts
```

### 2. Get User Profile
```python
def get_profile(handle):
    """Get user profile by handle."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile"
    
    response = requests.get(url, params={'actor': handle})
    return response.json()
```

### 3. Get User Posts (Feed)
```python
def get_user_posts(handle, limit=100):
    """Get posts from a user's feed."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
    
    posts = []
    cursor = None
    
    while len(posts) < limit:
        params = {
            'actor': handle,
            'limit': min(100, limit - len(posts)),
            'filter': 'posts_no_replies'  # or 'posts_with_replies'
        }
        if cursor:
            params['cursor'] = cursor
            
        response = requests.get(url, params=params)
        data = response.json()
        
        posts.extend(data.get('feed', []))
        cursor = data.get('cursor')
        
        if not cursor:
            break
    
    return posts
```

### 4. Get Post Thread (with replies)
```python
def get_thread(post_uri):
    """Get full thread including replies."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread"
    
    response = requests.get(url, params={
        'uri': post_uri,
        'depth': 10,  # Depth of replies
        'parentHeight': 10  # Height of parent context
    })
    
    return response.json()
```

### 5. Get Followers/Following
```python
def get_followers(handle, limit=100):
    """Get user's followers."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.graph.getFollowers"
    
    followers = []
    cursor = None
    
    while len(followers) < limit:
        params = {
            'actor': handle,
            'limit': min(100, limit - len(followers))
        }
        if cursor:
            params['cursor'] = cursor
            
        response = requests.get(url, params=params)
        data = response.json()
        
        followers.extend(data.get('followers', []))
        cursor = data.get('cursor')
        
        if not cursor:
            break
    
    return followers

def get_following(handle, limit=100):
    """Get accounts user follows."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.graph.getFollows"
    
    following = []
    cursor = None
    
    while len(following) < limit:
        params = {
            'actor': handle,
            'limit': min(100, limit - len(following))
        }
        if cursor:
            params['cursor'] = cursor
            
        response = requests.get(url, params=params)
        data = response.json()
        
        following.extend(data.get('follows', []))
        cursor = data.get('cursor')
        
        if not cursor:
            break
    
    return following
```

### 6. Using atproto Library (Authenticated)
```python
from atproto import Client

def authenticated_client(handle, app_password):
    """Create authenticated client."""
    client = Client()
    client.login(handle, app_password)
    return client

def search_with_client(client, query, limit=100):
    """Search using authenticated client."""
    posts = []
    cursor = None
    
    while len(posts) < limit:
        response = client.app.bsky.feed.search_posts(
            params={
                'q': query,
                'limit': min(100, limit - len(posts)),
                'cursor': cursor
            }
        )
        posts.extend(response.posts)
        cursor = response.cursor
        
        if not cursor:
            break
    
    return posts
```

## Research Applications

### Platform Migration Studies
- Twitter → Bluesky migration patterns
- Community formation on new platform
- Network reconstruction

### Decentralization Research
- Federation dynamics
- Custom feed algorithms
- Moderation approaches

### Political Communication
- Political discourse in new spaces
- Influencer migration
- Echo chamber formation

### Comparative Platform Studies
- Cross-platform content analysis
- User behavior differences
- Algorithmic feed comparison

## Data Schema

### Post Object
```python
{
    'uri': str,  # at://did:plc:xxx/app.bsky.feed.post/xxx
    'cid': str,  # Content ID
    'author': {
        'did': str,  # Decentralized ID
        'handle': str,
        'displayName': str,
        'avatar': str
    },
    'record': {
        'text': str,
        'createdAt': datetime,
        'langs': List[str],
        'facets': List[dict],  # Mentions, links, tags
        'reply': Optional[dict],
        'embed': Optional[dict]
    },
    'replyCount': int,
    'repostCount': int,
    'likeCount': int,
    'indexedAt': datetime
}
```

### Profile Object
```python
{
    'did': str,
    'handle': str,
    'displayName': str,
    'description': str,
    'avatar': str,
    'banner': str,
    'followersCount': int,
    'followsCount': int,
    'postsCount': int,
    'indexedAt': datetime,
    'labels': List[dict]
}
```

## Unique Features

### Custom Feeds
Bluesky allows custom algorithmic feeds:
```python
def get_custom_feed(feed_uri, limit=50):
    """Get posts from a custom feed."""
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getFeed"
    
    response = requests.get(url, params={
        'feed': feed_uri,
        'limit': limit
    })
    
    return response.json()
```

### Labeling System
Posts and accounts can have labels (content warnings, etc.):
```python
def get_labels(subject_uri):
    """Get labels for a subject (post or account)."""
    url = "https://public.api.bsky.app/xrpc/com.atproto.label.queryLabels"
    
    response = requests.get(url, params={
        'uriPatterns': [subject_uri]
    })
    
    return response.json()
```

## Rate Limiting

Currently generous limits, but be respectful:
```python
import time

def rate_limited_fetch(urls, delay=0.1):
    """Fetch with small delay between requests."""
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.json())
        time.sleep(delay)
    return results
```

## Ethical Considerations

- Platform is still growing; be mindful of early adopter privacy
- Decentralized IDs are persistent across instances
- Custom feeds may have specific norms
- Consider impact on small communities
- Document that platform norms are still forming

## Workflow Integration

```yaml
# Spawn Bluesky collection agent
sessions_spawn:
  task: "Collect Bluesky posts about {topic} from past {days} days"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash
```

## Key Citations

- Gehl, R. W., & Zulli, D. (2023). The digital covenant: Non-centralised platform governance on Mastodon and the fediverse.
- (Bluesky-specific research is emerging)

---
*Part of Communication Research Skill for OpenClaw*
