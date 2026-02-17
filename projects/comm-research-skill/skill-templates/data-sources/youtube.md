# YouTube Data Collection Skill

Collect and analyze YouTube data via the Data API v3.

## Overview

YouTube provides rich data for communication research:
- Video metadata (titles, descriptions, tags, statistics)
- Comments and replies
- Channel information
- Captions/transcripts
- Trending and search results

## API Access

### Requirements
1. Google Cloud Project
2. YouTube Data API v3 enabled
3. API key (for public data) or OAuth (for private)

### Setup
```bash
# Install
pip install google-api-python-client

# Set API key
export YOUTUBE_API_KEY="your-api-key"
```

### Quotas
- 10,000 units/day default
- Search: 100 units/call
- Video details: 1 unit/call
- Comments: 1 unit/call
- Apply for higher quota if needed

## Data Collection Patterns

### 1. Search Videos
```python
from googleapiclient.discovery import build
import os

def search_videos(query, max_results=50):
    """Search YouTube for videos matching query."""
    youtube = build('youtube', 'v3', 
                   developerKey=os.environ['YOUTUBE_API_KEY'])
    
    results = []
    next_page = None
    
    while len(results) < max_results:
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=min(50, max_results - len(results)),
            pageToken=next_page,
            order='relevance'  # or 'date', 'viewCount'
        )
        response = request.execute()
        
        results.extend(response.get('items', []))
        next_page = response.get('nextPageToken')
        
        if not next_page:
            break
    
    return results
```

### 2. Get Video Details
```python
def get_video_details(video_ids):
    """Get detailed metadata for videos."""
    youtube = build('youtube', 'v3',
                   developerKey=os.environ['YOUTUBE_API_KEY'])
    
    # API accepts up to 50 IDs per call
    all_details = []
    
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=','.join(batch)
        )
        response = request.execute()
        all_details.extend(response.get('items', []))
    
    return all_details
```

### 3. Get Comments
```python
def get_video_comments(video_id, max_results=1000):
    """Get comments for a video."""
    youtube = build('youtube', 'v3',
                   developerKey=os.environ['YOUTUBE_API_KEY'])
    
    comments = []
    next_page = None
    
    while len(comments) < max_results:
        try:
            request = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                maxResults=100,
                pageToken=next_page,
                textFormat='plainText'
            )
            response = request.execute()
            
            for item in response.get('items', []):
                # Top-level comment
                top = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'id': item['id'],
                    'video_id': video_id,
                    'author': top['authorDisplayName'],
                    'author_channel': top.get('authorChannelId', {}).get('value'),
                    'text': top['textDisplay'],
                    'likes': top['likeCount'],
                    'published': top['publishedAt'],
                    'is_reply': False
                })
                
                # Replies
                for reply in item.get('replies', {}).get('comments', []):
                    r = reply['snippet']
                    comments.append({
                        'id': reply['id'],
                        'video_id': video_id,
                        'parent_id': item['id'],
                        'author': r['authorDisplayName'],
                        'author_channel': r.get('authorChannelId', {}).get('value'),
                        'text': r['textDisplay'],
                        'likes': r['likeCount'],
                        'published': r['publishedAt'],
                        'is_reply': True
                    })
            
            next_page = response.get('nextPageToken')
            if not next_page:
                break
                
        except Exception as e:
            if 'commentsDisabled' in str(e):
                break
            raise
    
    return comments
```

### 4. Get Channel Videos
```python
def get_channel_videos(channel_id, max_results=500):
    """Get all videos from a channel."""
    youtube = build('youtube', 'v3',
                   developerKey=os.environ['YOUTUBE_API_KEY'])
    
    # Get uploads playlist
    channel_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()
    
    uploads_playlist = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    # Get videos from playlist
    videos = []
    next_page = None
    
    while len(videos) < max_results:
        request = youtube.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=next_page
        )
        response = request.execute()
        
        videos.extend(response.get('items', []))
        next_page = response.get('nextPageToken')
        
        if not next_page:
            break
    
    return videos
```

### 5. Get Transcripts (Captions)
```python
# Use youtube-transcript-api for easier transcript access
# pip install youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, languages=['en']):
    """Get video transcript."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, 
            languages=languages
        )
        
        # Combine into full text
        full_text = ' '.join([entry['text'] for entry in transcript])
        
        return {
            'video_id': video_id,
            'segments': transcript,
            'full_text': full_text
        }
    except Exception as e:
        return {'video_id': video_id, 'error': str(e)}
```

## Research Applications

### Political Communication
- Campaign video analysis
- Political ad tracking
- Candidate channel comparison

### Health Communication
- Health misinformation in videos
- Public health messaging effectiveness
- COVID/vaccine discourse

### Media Studies
- News channel analysis
- Algorithmic recommendation effects
- Creator-audience dynamics

### Network Analysis
- Comment reply networks
- Cross-video citation networks
- Channel collaboration networks

## Data Schema

### Video Object
```python
{
    'video_id': str,
    'title': str,
    'description': str,
    'channel_id': str,
    'channel_title': str,
    'published_at': datetime,
    'tags': List[str],
    'category_id': str,
    'duration': str,  # ISO 8601
    'view_count': int,
    'like_count': int,
    'comment_count': int,
    'caption_available': bool
}
```

### Comment Object
```python
{
    'comment_id': str,
    'video_id': str,
    'parent_id': Optional[str],
    'author': str,
    'author_channel_id': str,
    'text': str,
    'like_count': int,
    'published_at': datetime,
    'is_reply': bool
}
```

## Rate Limiting

```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    """Decorator to rate limit API calls."""
    min_interval = 1.0 / calls_per_second
    last_call = [0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_call[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_call[0] = time.time()
            return result
        return wrapper
    return decorator
```

## Ethical Considerations

- Respect creator privacy for smaller channels
- Consider consent implications for comment analysis
- Note that statistics may change over time
- Document collection date for reproducibility
- Be aware of recommendation algorithm effects on search

## Workflow Integration

```yaml
# Spawn YouTube collection agent
sessions_spawn:
  task: "Collect YouTube videos about {topic} from {date_range}"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash  # Fast, cheap for collection
```

## Key Citations

- Rieder, B., Matamoros-Fernández, A., & Coromina, Ò. (2018). From ranking algorithms to 'ranking cultures'. *Convergence*.
- Lewis, R. (2018). Alternative influence: Broadcasting the reactionary right on YouTube. *Data & Society*.

---
*Part of Communication Research Skill for OpenClaw*
