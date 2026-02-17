# Telegram Data Source Skill

## Overview

Collect data from public Telegram channels using the Telethon library.
Particularly useful for studying coordinated messaging, political communication,
and information operations.

## Access Requirements

| Requirement | Details |
|-------------|---------|
| **API ID** | From my.telegram.org |
| **API Hash** | From my.telegram.org |
| **Phone Number** | For authentication |
| **Rate Limit** | Flood wait applies (~30 req/30s) |
| **Cost** | Free |

## Setup

```python
# Install
pip install telethon

# Create session
from telethon import TelegramClient

api_id = 'YOUR_API_ID'       # From my.telegram.org
api_hash = 'YOUR_API_HASH'   # From my.telegram.org

client = TelegramClient('research_session', api_id, api_hash)
```

## Data Schema

### Message Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Message ID (unique per channel) |
| `message` | str | Text content |
| `date` | datetime | Posted timestamp |
| `views` | int | View count |
| `forwards` | int | Forward count |
| `from_id` | int | Sender ID (if available) |
| `peer_id` | int | Channel/chat ID |
| `fwd_from` | object | Forward source info |
| `media` | object | Attached media |
| `entities` | list | Links, mentions, hashtags |
| `replies` | object | Reply info |

### Forward Metadata (Critical for Coordination Research)

```python
if msg.fwd_from:
    fwd_from.channel_id  # Original channel
    fwd_from.date        # Original post date
    fwd_from.post_id     # Original message ID
```

## Collection Patterns

### Basic Channel History

```python
async def collect_channel_history(client, channel_username, limit=1000):
    """Collect recent messages from a channel."""
    channel = await client.get_entity(channel_username)
    
    messages = []
    async for msg in client.iter_messages(channel, limit=limit):
        messages.append({
            'id': msg.id,
            'text': msg.text,
            'date': msg.date.isoformat(),
            'views': msg.views,
            'forwards': msg.forwards,
            'fwd_channel': msg.fwd_from.channel_id if msg.fwd_from else None,
            'fwd_date': msg.fwd_from.date.isoformat() if msg.fwd_from else None,
        })
    
    return messages
```

### Date-Bounded Collection

```python
from datetime import datetime

async def collect_date_range(client, channel, start_date, end_date):
    """Collect messages within date range."""
    messages = []
    
    async for msg in client.iter_messages(
        channel,
        offset_date=end_date,
        reverse=False
    ):
        if msg.date < start_date:
            break
        messages.append(extract_message(msg))
    
    return messages
```

### Multi-Channel Collection (for Coordination Analysis)

```python
async def collect_multi_channel(client, channel_list):
    """Collect from multiple channels for coordination detection."""
    all_messages = []
    
    for channel_name in channel_list:
        try:
            channel = await client.get_entity(channel_name)
            async for msg in client.iter_messages(channel, limit=500):
                all_messages.append({
                    'channel': channel_name,
                    'channel_id': channel.id,
                    **extract_message(msg)
                })
        except Exception as e:
            print(f"Error collecting {channel_name}: {e}")
            continue
    
    return all_messages
```

### Forward Network Extraction

```python
def build_forward_network(messages):
    """
    Build network of forwarding relationships.
    Used for coordination detection (Kuznetsova 2025).
    """
    import networkx as nx
    
    G = nx.DiGraph()
    
    for msg in messages:
        if msg.get('fwd_channel'):
            source = msg['fwd_channel']
            target = msg['channel_id']
            
            if G.has_edge(source, target):
                G[source][target]['weight'] += 1
            else:
                G.add_edge(source, target, weight=1)
    
    return G
```

## Coordination Detection

Per Giglietto et al. (2020) and Kuznetsova (2025):

```python
def detect_rapid_sharing(messages, time_threshold_seconds=60):
    """
    Identify messages shared across channels within short time window.
    High coordination signal.
    """
    from collections import defaultdict
    
    # Group by content (use URL or text hash)
    content_groups = defaultdict(list)
    for msg in messages:
        content_key = msg.get('url') or hash(msg.get('text', '')[:100])
        content_groups[content_key].append(msg)
    
    coordinated_pairs = []
    
    for content_key, group in content_groups.items():
        if len(group) < 2:
            continue
        
        # Sort by time
        group.sort(key=lambda x: x['date'])
        
        # Check time deltas
        for i in range(len(group) - 1):
            delta = (group[i+1]['date'] - group[i]['date']).total_seconds()
            if delta <= time_threshold_seconds:
                coordinated_pairs.append({
                    'channel_1': group[i]['channel'],
                    'channel_2': group[i+1]['channel'],
                    'time_delta': delta,
                    'content_key': content_key
                })
    
    return coordinated_pairs
```

## Rate Limit Handling

```python
from telethon.errors import FloodWaitError
import asyncio

async def safe_collect(client, channel, limit):
    """Collection with flood wait handling."""
    messages = []
    
    try:
        async for msg in client.iter_messages(channel, limit=limit):
            messages.append(extract_message(msg))
    except FloodWaitError as e:
        print(f"Flood wait: {e.seconds} seconds")
        await asyncio.sleep(e.seconds + 10)
        # Retry
        return await safe_collect(client, channel, limit)
    
    return messages
```

## Gotchas & Limitations

1. **Must join channels to access history**
   - Some channels are private/invite-only
   - Joining too many channels may trigger restrictions

2. **Account restrictions**
   - New accounts have stricter limits
   - Use established accounts for research
   - Avoid bot-like behavior patterns

3. **Data availability**
   - Deleted messages not accessible
   - Some metadata may be missing for old messages
   - Media requires separate download

4. **Forward metadata**
   - Only available if original post still exists
   - Anonymous forwards lose source info
   - Critical for coordination analysis

## Ethical Considerations

- Public channels are generally fair game
- Private channels/groups require IRB consideration
- Don't identify individuals without consent
- Archive data responsibly (platforms may revoke access)
- Coordination ≠ inauthenticity (activists coordinate too)

## Output Format

Save collected data as JSON Lines:

```python
import json

def save_messages(messages, output_path):
    with open(output_path, 'w') as f:
        for msg in messages:
            f.write(json.dumps(msg) + '\n')
```

## Validation Checklist

- [ ] API credentials working
- [ ] Target channels accessible
- [ ] Rate limits respected
- [ ] Forward metadata captured
- [ ] Timestamps in consistent timezone
- [ ] Data archived before processing
