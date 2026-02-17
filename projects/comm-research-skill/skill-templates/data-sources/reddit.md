# Reddit Data Source Skill

## Overview

Collect data from Reddit using the PRAW library (Python Reddit API Wrapper).
Rich source for studying public discourse, communities, and opinion dynamics.

## Access Requirements

| Requirement | Details |
|-------------|---------|
| **Client ID** | From reddit.com/prefs/apps |
| **Client Secret** | From app settings |
| **User Agent** | Custom string identifying your app |
| **Rate Limit** | 60 requests/minute (OAuth) |
| **Cost** | Free |

## Setup

```python
# Install
pip install praw

# Initialize client
import praw

reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='ResearchBot/1.0 by YourUsername'
)
```

## Data Schema

### Submission (Post) Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Unique submission ID |
| `title` | str | Post title |
| `selftext` | str | Post body (self posts) |
| `author` | str | Username |
| `subreddit` | str | Subreddit name |
| `score` | int | Upvotes - downvotes |
| `upvote_ratio` | float | Proportion upvotes |
| `num_comments` | int | Comment count |
| `created_utc` | float | Unix timestamp |
| `url` | str | Link URL (link posts) |
| `is_self` | bool | Self post vs link |
| `permalink` | str | Reddit URL path |

### Comment Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Unique comment ID |
| `body` | str | Comment text |
| `author` | str | Username |
| `parent_id` | str | Parent submission/comment |
| `score` | int | Upvotes - downvotes |
| `created_utc` | float | Unix timestamp |
| `is_submitter` | bool | Is OP |

## Collection Patterns

### Subreddit Posts

```python
def collect_subreddit_posts(reddit, subreddit_name, limit=1000, sort='new'):
    """
    Collect posts from a subreddit.
    
    sort: 'hot', 'new', 'top', 'rising'
    """
    subreddit = reddit.subreddit(subreddit_name)
    
    if sort == 'new':
        submissions = subreddit.new(limit=limit)
    elif sort == 'hot':
        submissions = subreddit.hot(limit=limit)
    elif sort == 'top':
        submissions = subreddit.top(limit=limit, time_filter='all')
    elif sort == 'rising':
        submissions = subreddit.rising(limit=limit)
    else:
        raise ValueError(f"Unknown sort: {sort}")
    
    posts = []
    for submission in submissions:
        posts.append({
            'id': submission.id,
            'title': submission.title,
            'selftext': submission.selftext,
            'author': str(submission.author),
            'subreddit': subreddit_name,
            'score': submission.score,
            'upvote_ratio': submission.upvote_ratio,
            'num_comments': submission.num_comments,
            'created_utc': submission.created_utc,
            'url': submission.url,
            'is_self': submission.is_self,
            'permalink': submission.permalink,
        })
    
    return posts
```

### Search Query

```python
def search_reddit(reddit, query, subreddit=None, limit=1000, sort='relevance', time_filter='all'):
    """
    Search Reddit for posts matching query.
    
    time_filter: 'all', 'day', 'hour', 'month', 'week', 'year'
    sort: 'relevance', 'hot', 'top', 'new', 'comments'
    """
    if subreddit:
        search_target = reddit.subreddit(subreddit)
    else:
        search_target = reddit.subreddit('all')
    
    results = search_target.search(query, sort=sort, time_filter=time_filter, limit=limit)
    
    posts = []
    for submission in results:
        posts.append(extract_submission(submission))
    
    return posts
```

### Comments Collection

```python
def collect_comments(reddit, submission_id, limit=None):
    """
    Collect all comments from a submission.
    
    Handles 'MoreComments' objects to get full tree.
    """
    submission = reddit.submission(id=submission_id)
    submission.comments.replace_more(limit=limit)  # Expand all comment trees
    
    comments = []
    for comment in submission.comments.list():
        comments.append({
            'id': comment.id,
            'body': comment.body,
            'author': str(comment.author),
            'parent_id': comment.parent_id,
            'score': comment.score,
            'created_utc': comment.created_utc,
            'is_submitter': comment.is_submitter,
            'submission_id': submission_id,
        })
    
    return comments
```

### User History

```python
def collect_user_history(reddit, username, limit=100):
    """
    Collect a user's post and comment history.
    
    Note: Respects user privacy settings.
    """
    try:
        user = reddit.redditor(username)
        
        posts = []
        for submission in user.submissions.new(limit=limit):
            posts.append(extract_submission(submission))
        
        comments = []
        for comment in user.comments.new(limit=limit):
            comments.append({
                'id': comment.id,
                'body': comment.body,
                'subreddit': str(comment.subreddit),
                'parent_id': comment.parent_id,
                'score': comment.score,
                'created_utc': comment.created_utc,
            })
        
        return {'posts': posts, 'comments': comments}
    
    except Exception as e:
        print(f"Error collecting {username}: {e}")
        return None
```

### Multi-Subreddit Collection

```python
def collect_multi_subreddit(reddit, subreddit_list, limit_per_sub=500):
    """
    Collect from multiple subreddits.
    """
    all_posts = []
    
    for sub_name in subreddit_list:
        try:
            posts = collect_subreddit_posts(reddit, sub_name, limit=limit_per_sub)
            all_posts.extend(posts)
            print(f"Collected {len(posts)} from r/{sub_name}")
        except Exception as e:
            print(f"Error on r/{sub_name}: {e}")
            continue
    
    return all_posts
```

## Pushshift (Historical Data)

PRAW only accesses recent data. For historical analysis, use Pushshift archives.

**Note:** Pushshift availability varies. Check current status.

```python
import requests

def pushshift_search(subreddit, query=None, after=None, before=None, size=500):
    """
    Search Pushshift for historical Reddit data.
    
    after/before: Unix timestamps
    """
    base_url = "https://api.pushshift.io/reddit/search/submission/"
    
    params = {
        'subreddit': subreddit,
        'size': size,
    }
    
    if query:
        params['q'] = query
    if after:
        params['after'] = after
    if before:
        params['before'] = before
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()['data']
    else:
        raise Exception(f"Pushshift error: {response.status_code}")
```

## Rate Limit Handling

```python
import time

def rate_limited_collect(reddit, subreddits, limit_per_sub=500):
    """
    Collection with rate limit awareness.
    
    PRAW handles most rate limiting automatically, but
    be cautious with high-volume collection.
    """
    all_posts = []
    
    for i, sub_name in enumerate(subreddits):
        posts = collect_subreddit_posts(reddit, sub_name, limit=limit_per_sub)
        all_posts.extend(posts)
        
        # Progress update
        print(f"[{i+1}/{len(subreddits)}] r/{sub_name}: {len(posts)} posts")
        
        # Small delay between subreddits (PRAW usually handles this)
        if (i + 1) % 10 == 0:
            time.sleep(2)
    
    return all_posts
```

## Network Construction

Build networks from Reddit interactions:

```python
def build_reply_network(comments):
    """
    Build network from comment reply structure.
    
    Edge: commenter → parent commenter
    """
    import networkx as nx
    
    # Map comment IDs to authors
    author_map = {c['id']: c['author'] for c in comments}
    
    G = nx.DiGraph()
    
    for comment in comments:
        child_author = comment['author']
        parent_id = comment['parent_id']
        
        # Check if parent is a comment (not submission)
        if parent_id.startswith('t1_'):
            parent_comment_id = parent_id[3:]  # Remove 't1_' prefix
            parent_author = author_map.get(parent_comment_id)
            
            if parent_author and parent_author != child_author:
                if G.has_edge(child_author, parent_author):
                    G[child_author][parent_author]['weight'] += 1
                else:
                    G.add_edge(child_author, parent_author, weight=1)
    
    return G
```

## Gotchas & Limitations

1. **Rate limits:** 60 requests/minute; PRAW handles most cases
2. **Historical data:** PRAW only gets recent posts; use Pushshift for archives
3. **Deleted content:** `[deleted]` or `[removed]` for author/content
4. **Private subreddits:** Require invitation to access
5. **Shadowbanned users:** Content may exist but author shows as None
6. **MoreComments:** Deep threads require explicit expansion

## Ethical Considerations

- Respect Reddit's robots.txt and API terms
- Don't collect from private/quarantined subreddits without permission
- Anonymize user data in publications
- Be aware of brigading if your research becomes public
- Consider whether scraping aligns with user expectations

## Output Format

Save as JSON Lines:

```python
import json
from datetime import datetime

def save_reddit_data(posts, output_path):
    """Save Reddit posts to JSON Lines format."""
    with open(output_path, 'w') as f:
        for post in posts:
            # Convert timestamps
            post['created_utc_iso'] = datetime.utcfromtimestamp(
                post['created_utc']
            ).isoformat()
            f.write(json.dumps(post) + '\n')
```

## Validation Checklist

- [ ] API credentials working
- [ ] Rate limits not exceeded
- [ ] Deleted content handled
- [ ] Timestamps in consistent format
- [ ] Author field checked for None/deleted
- [ ] MoreComments expanded if needed
