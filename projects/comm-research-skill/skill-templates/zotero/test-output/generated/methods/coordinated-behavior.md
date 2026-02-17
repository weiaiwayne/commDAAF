# Coordinated Behavior Detection Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Detect and analyze coordinated activity across platforms.
Your library shows strong focus on this method (5 papers).

## Priority in Your Research: HIGH

## Core Framework (Giglietto et al.)

1. **Data Collection**: Gather content with shared identifiers
2. **Co-sharing Detection**: Find accounts sharing same content rapidly
3. **Network Construction**: Build network from co-sharing patterns
4. **Community Detection**: Identify clusters of coordinated actors
5. **Validation**: Manual review of flagged networks

## Detection Signals

### Temporal
- Synchronized posting (same minute/hour)
- Rapid sequential sharing
- Activity bursts

### Network
- Dense interconnection
- Unusual follower patterns
- Amplification chains

### Content
- Identical/near-identical posts
- Shared URLs across accounts
- Hashtag coordination

## Implementation

```python
import pandas as pd
import networkx as nx
from datetime import timedelta

def detect_coordination(df, time_window='1h', min_shared=2):
    """
    Detect coordinated sharing based on temporal proximity.
    
    Args:
        df: DataFrame with columns [user_id, content_id, timestamp]
        time_window: Window for considering coordination
        min_shared: Minimum shared items to flag as coordinated
    """
    # Group by content
    coord_pairs = []
    
    for content_id, group in df.groupby('content_id'):
        if len(group) < 2:
            continue
            
        group = group.sort_values('timestamp')
        
        for i, row1 in group.iterrows():
            for j, row2 in group.iterrows():
                if i >= j:
                    continue
                    
                time_diff = row2['timestamp'] - row1['timestamp']
                if time_diff <= pd.Timedelta(time_window):
                    coord_pairs.append((row1['user_id'], row2['user_id']))
    
    # Build coordination network
    G = nx.Graph()
    for u1, u2 in coord_pairs:
        if G.has_edge(u1, u2):
            G[u1][u2]['weight'] += 1
        else:
            G.add_edge(u1, u2, weight=1)
    
    # Filter by minimum shared
    G = nx.Graph([(u, v, d) for u, v, d in G.edges(data=True) 
                  if d['weight'] >= min_shared])
    
    return G
```

## Ethical Considerations

- Coordination ≠ inauthenticity
- Document methodology transparently
- Avoid false positives

## Platform-Specific Notes

- **Twitter**: Appears in 293 papers
- **Facebook**: Appears in 89 papers
- **Weibo**: Appears in 31 papers

## Key Citations from Your Library

*Add key citations for coordinated_behavior from your library here*

---
*Auto-generated based on your research profile*
