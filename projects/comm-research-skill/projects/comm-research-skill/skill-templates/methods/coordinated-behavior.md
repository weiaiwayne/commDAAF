# Coordinated Behavior Detection Method

## Overview

Detect coordinated activity across social media accounts/channels by analyzing
temporal co-sharing patterns, network structure, and content similarity.

**Key distinction:** Coordination ≠ Inauthenticity
- Activists coordinate legitimately (authentic)
- State actors coordinate deceptively (inauthentic)
- Method detects coordination; interpretation requires human judgment

## Theoretical Framework

### Coordinated Inauthentic Behavior (CIB)
Definition: Organized efforts to manipulate public discourse through coordinated 
action that obscures the true actors or their coordination.

### Coordinated Link Sharing Behavior (CLSB)
Definition: Multiple accounts sharing the same content within a short time window,
suggesting coordination rather than organic discovery.

Key papers:
- Giglietto et al. (2020) - CLSB methodology
- Kuznetsova (2025) - Telegram coordination detection

## Detection Signals

| Signal Type | Indicators | Weight |
|-------------|------------|--------|
| **Temporal** | Same content within seconds/minutes | High |
| **Network** | Dense interconnection, unusual patterns | Medium |
| **Content** | Identical text, shared URLs | High |
| **Behavioral** | Creation time, activity timing | Medium |
| **Linguistic** | Shared vocabulary, style | Low |

## Algorithm

### Step 1: Content Identification

Identify shared content markers:
- URLs (most reliable)
- Hashtags
- Text fingerprints (for near-duplicates)

```python
import hashlib

def content_signature(text, urls=None):
    """Create signature for content matching."""
    if urls:
        return tuple(sorted(urls))
    # Text fingerprint: first 100 chars, normalized
    normalized = ' '.join(text.lower().split())[:100]
    return hashlib.md5(normalized.encode()).hexdigest()
```

### Step 2: Co-Sharing Detection

Find accounts sharing same content within time threshold.

```python
from collections import defaultdict
from datetime import timedelta

def find_co_shares(posts, time_threshold_seconds=60):
    """
    Find posts sharing same content within time window.
    
    Returns list of (post1, post2, time_delta) tuples.
    """
    # Group by content
    content_groups = defaultdict(list)
    for post in posts:
        sig = content_signature(post['text'], post.get('urls'))
        content_groups[sig].append(post)
    
    co_shares = []
    for sig, group in content_groups.items():
        if len(group) < 2:
            continue
        
        # Sort by time
        group.sort(key=lambda x: x['timestamp'])
        
        # Find pairs within threshold
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                delta = (group[j]['timestamp'] - group[i]['timestamp']).total_seconds()
                if delta <= time_threshold_seconds:
                    co_shares.append({
                        'account_1': group[i]['account'],
                        'account_2': group[j]['account'],
                        'time_delta': delta,
                        'content_sig': sig,
                        'timestamp_1': group[i]['timestamp'],
                        'timestamp_2': group[j]['timestamp']
                    })
    
    return co_shares
```

### Step 3: Network Construction

Build coordination network from co-shares.

```python
import networkx as nx

def build_coordination_network(co_shares, min_weight=2):
    """
    Build network where edges = co-sharing relationships.
    
    Edge weight = number of co-shares between accounts.
    """
    G = nx.Graph()
    
    for cs in co_shares:
        a1, a2 = cs['account_1'], cs['account_2']
        
        if G.has_edge(a1, a2):
            G[a1][a2]['weight'] += 1
            G[a1][a2]['avg_delta'] = (
                G[a1][a2]['avg_delta'] + cs['time_delta']
            ) / 2
        else:
            G.add_edge(a1, a2, weight=1, avg_delta=cs['time_delta'])
    
    # Filter by minimum weight
    edges_to_remove = [
        (u, v) for u, v, d in G.edges(data=True) 
        if d['weight'] < min_weight
    ]
    G.remove_edges_from(edges_to_remove)
    
    # Remove isolated nodes
    G.remove_nodes_from(list(nx.isolates(G)))
    
    return G
```

### Step 4: Community Detection

Find clusters of coordinated accounts.

```python
from community import community_louvain

def detect_coordinated_clusters(G):
    """
    Detect communities in coordination network.
    Each community = potential coordinated group.
    """
    if len(G.nodes()) == 0:
        return {}
    
    partition = community_louvain.best_partition(G, weight='weight')
    
    # Calculate cluster statistics
    clusters = defaultdict(list)
    for node, cluster_id in partition.items():
        clusters[cluster_id].append(node)
    
    cluster_stats = []
    for cluster_id, members in clusters.items():
        subgraph = G.subgraph(members)
        cluster_stats.append({
            'cluster_id': cluster_id,
            'size': len(members),
            'members': members,
            'density': nx.density(subgraph),
            'avg_weight': sum(d['weight'] for _, _, d in subgraph.edges(data=True)) / max(subgraph.number_of_edges(), 1),
            'total_co_shares': sum(d['weight'] for _, _, d in subgraph.edges(data=True))
        })
    
    return sorted(cluster_stats, key=lambda x: x['total_co_shares'], reverse=True)
```

### Step 5: Scoring & Ranking

Score accounts by coordination intensity.

```python
def calculate_coordination_scores(G, clusters):
    """
    Score accounts by coordination intensity.
    """
    scores = {}
    
    for node in G.nodes():
        # Weighted degree
        weighted_degree = sum(d['weight'] for _, _, d in G.edges(node, data=True))
        
        # Average time delta (lower = more suspicious)
        avg_delta = sum(d['avg_delta'] for _, _, d in G.edges(node, data=True)) / max(G.degree(node), 1)
        
        # Cluster density contribution
        for cluster in clusters:
            if node in cluster['members']:
                cluster_density = cluster['density']
                break
        else:
            cluster_density = 0
        
        scores[node] = {
            'weighted_degree': weighted_degree,
            'avg_time_delta': avg_delta,
            'cluster_density': cluster_density,
            'coordination_score': weighted_degree * cluster_density / max(avg_delta, 1)
        }
    
    return scores
```

## Validation

### Ground Truth Comparison
If known coordinated campaigns exist:
- Calculate precision/recall against known actors
- Check false positive rate

### Manual Review
For top-scoring clusters:
- Review account profiles
- Check content patterns
- Verify coordination interpretation

### Sanity Checks
- Are time deltas realistic for organic sharing?
- Is coordination density higher than baseline?
- Do clusters align with known groups?

## Visualization

```python
import matplotlib.pyplot as plt

def visualize_coordination_network(G, clusters, output_path):
    """Create visualization of coordination network."""
    
    # Color nodes by cluster
    partition = {}
    for cluster in clusters:
        for member in cluster['members']:
            partition[member] = cluster['cluster_id']
    
    pos = nx.spring_layout(G, weight='weight', k=2, iterations=50)
    
    plt.figure(figsize=(12, 12))
    
    # Draw edges
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=[w/max(edge_weights)*3 for w in edge_weights])
    
    # Draw nodes colored by cluster
    colors = [partition.get(node, -1) for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=colors, cmap=plt.cm.tab20, node_size=100)
    
    plt.title('Coordination Network')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

## Output Format

```yaml
# coordination_analysis.yaml

metadata:
  analysis_date: "2026-02-17"
  time_threshold_seconds: 60
  min_weight: 2
  total_posts_analyzed: 50000
  total_accounts: 1234

summary:
  co_shares_detected: 456
  accounts_in_network: 89
  clusters_found: 5

clusters:
  - cluster_id: 0
    size: 15
    density: 0.73
    total_co_shares: 234
    members: [account1, account2, ...]
    interpretation: "Likely coordinated - pro-government messaging"
    
  - cluster_id: 1
    size: 8
    density: 0.65
    total_co_shares: 89
    members: [...]
    interpretation: "Possibly organic - activist coalition"

high_coordination_accounts:
  - account: account_x
    coordination_score: 45.2
    weighted_degree: 23
    avg_time_delta: 12.5
```

## Ethical Guidelines

1. **Coordination ≠ Inauthenticity**
   - Social movements coordinate
   - News organizations coordinate
   - Only behavior is detected, not intent

2. **Avoid False Accusations**
   - High threshold for "inauthentic" label
   - Manual review before naming actors
   - Document methodology transparently

3. **Platform Considerations**
   - Some platforms facilitate coordination (share buttons)
   - Context matters for interpretation

4. **Reporting**
   - Report coordination patterns, not individuals (unless public figures)
   - Focus on behavior, not identity
   - Allow for alternative explanations
