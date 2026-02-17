# Network Analysis Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Network analysis examines relationships and structures in social data.
Based on your library, you frequently use network methods for:
- Polarization research
- Misinformation research
- Political Communication research

## Priority in Your Research: CRITICAL

Detected in 145 papers in your library.

## Key Methods

### 1. Network Construction
- Co-occurrence networks (hashtags, URLs, mentions)
- Interaction networks (replies, retweets, quotes)
- Affiliation networks (group membership)
- Temporal networks (time-varying edges)

### 2. Centrality Measures
- Degree centrality (connections)
- Betweenness centrality (bridging)
- Eigenvector/PageRank (influence)
- Closeness centrality (access)

### 3. Community Detection
- Louvain algorithm
- Label propagation
- Infomap
- Spectral clustering

### 4. Coordinated Behavior Detection
- Co-sharing within time windows
- Synchronized posting patterns
- Network-based clustering of coordinated actors

## Python Libraries

```python
import networkx as nx
import igraph as ig
from cdlib import algorithms  # Community detection

# For large graphs
import graph_tool  # Faster than networkx
```

## Integration with Your Platforms

- **Twitter**: Appears in 293 papers
- **Facebook**: Appears in 89 papers
- **Weibo**: Appears in 31 papers

## Key Citations from Your Library

*Add key citations for network_analysis from your library here*

## Workflow Integration

```yaml
# Spawn network analysis agent
sessions_spawn:
  task: "Construct [network_type] network from [data_source]"
  agentId: comm-research-network
  model: deepseek/deepseek-v3  # Good at code
```

---
*Auto-generated based on your research profile*
