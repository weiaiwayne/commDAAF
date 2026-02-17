# MediaCloud Data Collection Skill

Collect and analyze news media data via MediaCloud API.

## Overview

MediaCloud is a research platform for studying media ecosystems:
- 1.5M+ news sources worldwide
- Full-text search across archives
- Pre-built topic models
- Open-source and research-focused

## API Access

### Setup
1. Create account at [mediacloud.org](https://mediacloud.org)
2. Get API key from dashboard
3. Install client library

```bash
pip install mediacloud

# Set API key
export MEDIACLOUD_API_KEY="your-api-key"
```

## Data Collection Patterns

### 1. Search Stories
```python
import mediacloud.api
import os
from datetime import datetime, timedelta

def init_client():
    """Initialize MediaCloud client."""
    return mediacloud.api.MediaCloud(os.environ['MEDIACLOUD_API_KEY'])

def search_stories(query, start_date, end_date, collection_id=None, limit=1000):
    """
    Search for stories matching query.
    
    Args:
        query: Solr query string
        start_date: Start date (datetime or string YYYY-MM-DD)
        end_date: End date
        collection_id: Optional media collection ID
        limit: Maximum stories to return
    """
    mc = init_client()
    
    # Format dates
    if isinstance(start_date, datetime):
        start_date = start_date.strftime('%Y-%m-%d')
    if isinstance(end_date, datetime):
        end_date = end_date.strftime('%Y-%m-%d')
    
    # Build filter query
    fq = f"publish_day:[{start_date}T00:00:00Z TO {end_date}T23:59:59Z]"
    if collection_id:
        fq += f" AND tags_id_media:{collection_id}"
    
    stories = []
    last_id = 0
    
    while len(stories) < limit:
        batch = mc.storyList(
            query,
            fq,
            last_processed_stories_id=last_id,
            rows=min(1000, limit - len(stories))
        )
        
        if not batch:
            break
            
        stories.extend(batch)
        last_id = batch[-1]['processed_stories_id']
    
    return stories
```

### 2. Get Story Count Over Time
```python
def story_count_over_time(query, start_date, end_date, collection_id=None):
    """Get daily story counts for a query."""
    mc = init_client()
    
    if isinstance(start_date, datetime):
        start_date = start_date.strftime('%Y-%m-%d')
    if isinstance(end_date, datetime):
        end_date = end_date.strftime('%Y-%m-%d')
    
    fq = f"publish_day:[{start_date}T00:00:00Z TO {end_date}T23:59:59Z]"
    if collection_id:
        fq += f" AND tags_id_media:{collection_id}"
    
    counts = mc.storyCount(query, fq, split=True, split_period='day')
    
    return counts
```

### 3. Get Word Frequencies
```python
def word_frequencies(query, start_date, end_date, collection_id=None, num_words=100):
    """Get most frequent words in matching stories."""
    mc = init_client()
    
    if isinstance(start_date, datetime):
        start_date = start_date.strftime('%Y-%m-%d')
    if isinstance(end_date, datetime):
        end_date = end_date.strftime('%Y-%m-%d')
    
    fq = f"publish_day:[{start_date}T00:00:00Z TO {end_date}T23:59:59Z]"
    if collection_id:
        fq += f" AND tags_id_media:{collection_id}"
    
    words = mc.wordCount(query, fq, num_words=num_words)
    
    return words
```

### 4. Media Source Lookup
```python
def get_media_source(media_id):
    """Get details about a media source."""
    mc = init_client()
    return mc.media(media_id)

def search_media_sources(query, limit=100):
    """Search for media sources."""
    mc = init_client()
    return mc.mediaList(name_like=query, rows=limit)

def get_collection_sources(collection_id, limit=1000):
    """Get all sources in a collection."""
    mc = init_client()
    return mc.mediaList(tags_id=collection_id, rows=limit)
```

### 5. Pre-Built Collections
```python
# Useful collection IDs
COLLECTIONS = {
    'us_national': 34412234,      # Major US national sources
    'us_state': 38379429,         # US state/local sources
    'uk_national': 34412476,      # UK national sources
    'germany': 34412118,          # German sources
    'spain': 34412311,            # Spanish sources
    'france': 34412138,           # French sources
    'russia': 34412309,           # Russian sources (in Russian)
    'china': 34412021,            # Chinese sources (in Chinese)
}

def search_us_news(query, start_date, end_date):
    """Search US national news."""
    return search_stories(
        query, start_date, end_date, 
        collection_id=COLLECTIONS['us_national']
    )
```

## Research Applications

### Agenda Setting
- Track issue attention over time
- Compare coverage across outlets
- Intermedia agenda setting

### Framing Analysis
- Extract frames from coverage
- Compare framing across sources
- Track frame evolution

### Media Ecosystem Studies
- Source network analysis
- Coverage patterns
- Geographic distribution

### Misinformation Research
- Track narratives across sources
- Compare mainstream vs. fringe
- Story diffusion patterns

## Data Schema

### Story Object
```python
{
    'stories_id': int,
    'processed_stories_id': int,
    'title': str,
    'url': str,
    'publish_date': datetime,
    'media_id': int,
    'media_name': str,
    'media_url': str,
    'language': str,
    'ap_syndicated': bool,
    'word_count': int
}
```

### Word Count Object
```python
{
    'term': str,
    'stem': str,
    'count': int
}
```

## Advanced Queries

### Solr Query Syntax
```python
# Boolean operators
query = "(climate AND change) OR (global AND warming)"

# Phrase search
query = '"climate change"'

# Exclude terms
query = "climate -denial"

# Field-specific
query = "title:climate"

# Proximity search (words within N of each other)
query = '"climate crisis"~5'
```

### Complex Example
```python
def partisan_comparison(topic, start_date, end_date):
    """Compare coverage across partisan sources."""
    
    # Define partisan collections (example IDs)
    left_leaning = 123456  # hypothetical
    right_leaning = 789012  # hypothetical
    
    left_stories = search_stories(
        topic, start_date, end_date, 
        collection_id=left_leaning
    )
    
    right_stories = search_stories(
        topic, start_date, end_date,
        collection_id=right_leaning
    )
    
    return {
        'left': left_stories,
        'right': right_stories,
        'left_count': len(left_stories),
        'right_count': len(right_stories)
    }
```

## Rate Limiting

MediaCloud has generous limits for research:
```python
import time

def batch_search(queries, start_date, end_date, delay=1.0):
    """Run multiple searches with delay."""
    results = {}
    for query in queries:
        results[query] = search_stories(query, start_date, end_date)
        time.sleep(delay)
    return results
```

## Ethical Considerations

- MediaCloud is designed for research use
- Respect source copyright for full-text
- Document collection parameters for reproducibility
- Note that source coverage varies by region/language
- Some archives have gaps

## Workflow Integration

```yaml
# Spawn MediaCloud collection agent
sessions_spawn:
  task: "Collect news coverage of {topic} from {date_range} in {collection}"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash
```

## Key Citations

- Roberts, M., Stewart, B., & Nielsen, R. (2019). Adjusting for confounding with text matching.
- MediaCloud documentation: [mediacloud.org/support](https://mediacloud.org/support)

---
*Part of Communication Research Skill for OpenClaw*
