# Network Analysis Method Skill

## Overview

Construct and analyze social networks from communication data. Covers:
- Network construction from interactions
- Centrality and influence metrics
- Community detection
- Opinion leadership identification
- Temporal dynamics

Based on: Liang & Lee (2023), Gruzd et al. (2011), network science foundations.

## Network Types

### User-User Networks
Nodes = users, edges = interactions

**Edge sources:**
- Replies/mentions → directed
- Retweets/shares → directed
- Follows → directed
- Co-commenting → undirected

### User-Content Networks (Bipartite)
Two node types: users and content items

**Projections:**
- User projection: connect users who engaged with same content
- Content projection: connect content engaged by same users

### Content-Content Networks
Nodes = posts/articles, edges = similarity

**Edge sources:**
- Shared URLs
- Hashtag co-occurrence
- Semantic similarity (embeddings)

## Construction

```python
import networkx as nx
import pandas as pd

def build_reply_network(interactions_df):
    """
    Build directed network from reply interactions.
    
    interactions_df columns: ['source', 'target', 'timestamp', 'type']
    """
    G = nx.DiGraph()
    
    # Filter to replies
    replies = interactions_df[interactions_df['type'] == 'reply']
    
    for _, row in replies.iterrows():
        source, target = row['source'], row['target']
        
        if G.has_edge(source, target):
            G[source][target]['weight'] += 1
            G[source][target]['timestamps'].append(row['timestamp'])
        else:
            G.add_edge(source, target, weight=1, timestamps=[row['timestamp']])
    
    return G


def build_coengagement_network(posts_df, min_overlap=2):
    """
    Build undirected network connecting users who engaged with same content.
    
    posts_df columns: ['user', 'post_id', 'timestamp']
    """
    from itertools import combinations
    
    G = nx.Graph()
    
    # Group by post
    for post_id, group in posts_df.groupby('post_id'):
        users = group['user'].unique()
        if len(users) < 2:
            continue
        
        for u1, u2 in combinations(users, 2):
            if G.has_edge(u1, u2):
                G[u1][u2]['weight'] += 1
                G[u1][u2]['shared_posts'].append(post_id)
            else:
                G.add_edge(u1, u2, weight=1, shared_posts=[post_id])
    
    # Filter by minimum overlap
    edges_to_remove = [(u, v) for u, v, d in G.edges(data=True) if d['weight'] < min_overlap]
    G.remove_edges_from(edges_to_remove)
    
    return G
```

## Centrality Metrics

| Metric | Formula | Interpretation | Use Case |
|--------|---------|----------------|----------|
| **In-degree** | Count of incoming edges | Raw popularity | Who gets mentioned |
| **Out-degree** | Count of outgoing edges | Activity level | Who talks most |
| **Betweenness** | Fraction of shortest paths through node | Bridge role | Information brokers |
| **Eigenvector** | Centrality based on neighbor centrality | Elite status | Connected to elites |
| **PageRank** | Random walk probability | Influence flow | Overall influence |
| **Closeness** | Inverse avg distance to all nodes | Information access | Reach potential |

```python
def calculate_centrality_metrics(G):
    """Calculate multiple centrality measures."""
    metrics = pd.DataFrame(index=G.nodes())
    
    if G.is_directed():
        metrics['in_degree'] = pd.Series(dict(G.in_degree()))
        metrics['out_degree'] = pd.Series(dict(G.out_degree()))
    else:
        metrics['degree'] = pd.Series(dict(G.degree()))
    
    metrics['pagerank'] = pd.Series(nx.pagerank(G, weight='weight'))
    metrics['betweenness'] = pd.Series(nx.betweenness_centrality(G, weight='weight'))
    
    try:
        metrics['eigenvector'] = pd.Series(nx.eigenvector_centrality(G, weight='weight', max_iter=1000))
    except:
        metrics['eigenvector'] = 0  # May not converge for some networks
    
    return metrics
```

## Opinion Leadership Detection

Per Liang & Lee (2023):

```python
def identify_opinion_leaders(G, posts_df=None, top_n=50):
    """
    Identify opinion leaders using multiple signals.
    
    Signals:
    - Network centrality (in-degree, PageRank)
    - Content generation (thread initiation)
    - Engagement received
    """
    metrics = calculate_centrality_metrics(G)
    
    # Add content-based metrics if available
    if posts_df is not None:
        # Thread initiation rate
        thread_starts = posts_df[posts_df['is_thread_start']].groupby('user').size()
        metrics['thread_starts'] = thread_starts.reindex(metrics.index, fill_value=0)
        
        # Total engagement received
        engagement = posts_df.groupby('user')['engagement'].sum()
        metrics['total_engagement'] = engagement.reindex(metrics.index, fill_value=0)
    
    # Composite leadership score
    for col in metrics.columns:
        metrics[f'{col}_rank'] = metrics[col].rank(pct=True)
    
    rank_cols = [c for c in metrics.columns if c.endswith('_rank')]
    metrics['leadership_score'] = metrics[rank_cols].mean(axis=1)
    
    # Top leaders
    leaders = metrics.nlargest(top_n, 'leadership_score')
    
    return leaders


def analyze_leadership_stability(G_snapshots, top_n=50):
    """
    Track stability of opinion leadership across time periods.
    
    G_snapshots: list of (timestamp, Graph) tuples
    """
    from scipy.stats import spearmanr
    
    leadership_over_time = []
    
    for ts, G in G_snapshots:
        leaders = identify_opinion_leaders(G, top_n=top_n)
        leaders['timestamp'] = ts
        leadership_over_time.append(leaders)
    
    # Calculate rank correlations between periods
    stability_scores = []
    
    for i in range(len(leadership_over_time) - 1):
        df1 = leadership_over_time[i]
        df2 = leadership_over_time[i + 1]
        
        common_users = set(df1.index) & set(df2.index)
        
        if len(common_users) >= 10:
            r, p = spearmanr(
                df1.loc[list(common_users), 'leadership_score'],
                df2.loc[list(common_users), 'leadership_score']
            )
            stability_scores.append({
                'period': i,
                'timestamp_1': G_snapshots[i][0],
                'timestamp_2': G_snapshots[i+1][0],
                'rank_correlation': r,
                'p_value': p,
                'common_users': len(common_users)
            })
    
    return pd.DataFrame(stability_scores)
```

## Community Detection

| Algorithm | Complexity | Quality | Use Case |
|-----------|------------|---------|----------|
| **Louvain** | O(n log n) | High | Default choice |
| **Leiden** | O(n log n) | Higher | When guaranteed connectivity needed |
| **Label Propagation** | O(n) | Medium | Very large networks |
| **Infomap** | O(n log n) | High | When flow dynamics matter |

```python
from community import community_louvain

def detect_communities(G, method='louvain', resolution=1.0):
    """
    Detect communities in network.
    
    Returns partition dict: {node: community_id}
    """
    # Convert to undirected if needed
    G_undirected = G.to_undirected() if G.is_directed() else G
    
    if method == 'louvain':
        partition = community_louvain.best_partition(
            G_undirected, 
            weight='weight',
            resolution=resolution
        )
    elif method == 'label_propagation':
        communities = nx.community.label_propagation_communities(G_undirected)
        partition = {}
        for i, comm in enumerate(communities):
            for node in comm:
                partition[node] = i
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return partition


def analyze_communities(G, partition):
    """Analyze detected community structure."""
    from collections import defaultdict
    
    # Group nodes by community
    communities = defaultdict(list)
    for node, comm_id in partition.items():
        communities[comm_id].append(node)
    
    results = []
    for comm_id, members in communities.items():
        subgraph = G.subgraph(members)
        
        # Find most central node
        if len(members) > 0:
            pageranks = nx.pagerank(subgraph)
            central_node = max(pageranks, key=pageranks.get)
        else:
            central_node = None
        
        results.append({
            'community_id': comm_id,
            'size': len(members),
            'density': nx.density(subgraph),
            'internal_edges': subgraph.number_of_edges(),
            'central_node': central_node,
            'members': members
        })
    
    return pd.DataFrame(results).sort_values('size', ascending=False)
```

## Temporal Network Analysis

```python
def create_temporal_snapshots(interactions_df, window='7D'):
    """
    Create network snapshots over time windows.
    
    Returns list of (timestamp, Graph) tuples.
    """
    interactions_df['timestamp'] = pd.to_datetime(interactions_df['timestamp'])
    
    snapshots = []
    for period, group in interactions_df.groupby(pd.Grouper(key='timestamp', freq=window)):
        if len(group) > 0:
            G = build_reply_network(group)
            if G.number_of_nodes() > 0:
                snapshots.append((period, G))
    
    return snapshots


def track_network_evolution(snapshots):
    """Track network statistics over time."""
    stats = []
    
    for ts, G in snapshots:
        stats.append({
            'timestamp': ts,
            'nodes': G.number_of_nodes(),
            'edges': G.number_of_edges(),
            'density': nx.density(G),
            'avg_clustering': nx.average_clustering(G.to_undirected()),
            'components': nx.number_weakly_connected_components(G) if G.is_directed() else nx.number_connected_components(G)
        })
    
    return pd.DataFrame(stats)
```

## Visualization

```python
import matplotlib.pyplot as plt

def visualize_network(G, partition=None, output_path='network.png', 
                      node_size_attr=None, figsize=(12, 12)):
    """
    Create network visualization.
    """
    plt.figure(figsize=figsize)
    
    # Layout
    pos = nx.spring_layout(G, weight='weight', k=2, iterations=50, seed=42)
    
    # Node sizes
    if node_size_attr:
        sizes = [G.nodes[n].get(node_size_attr, 100) for n in G.nodes()]
    else:
        sizes = [100 + G.degree(n) * 10 for n in G.nodes()]
    
    # Node colors (by community if provided)
    if partition:
        colors = [partition.get(n, 0) for n in G.nodes()]
        cmap = plt.cm.tab20
    else:
        colors = 'lightblue'
        cmap = None
    
    # Edge weights
    edge_weights = [G[u][v].get('weight', 1) for u, v in G.edges()]
    max_weight = max(edge_weights) if edge_weights else 1
    edge_widths = [0.5 + (w / max_weight) * 2 for w in edge_weights]
    
    # Draw
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=edge_widths)
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=colors, 
                           cmap=cmap, alpha=0.8)
    
    # Labels for high-degree nodes only
    high_degree_nodes = [n for n in G.nodes() if G.degree(n) > 10]
    labels = {n: n for n in high_degree_nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    return output_path
```

## Output Format

```yaml
# network_analysis_results.yaml

metadata:
  network_type: "reply_network"
  nodes: 1234
  edges: 5678
  density: 0.0037
  analysis_date: "2026-02-17"

global_metrics:
  avg_clustering: 0.23
  avg_path_length: 4.2
  diameter: 12
  components: 3

centrality_summary:
  top_pagerank:
    - user: "@user_a"
      score: 0.045
    - user: "@user_b"
      score: 0.032

communities:
  count: 5
  modularity: 0.67
  largest:
    - size: 234
      density: 0.12
      central_user: "@user_x"

opinion_leaders:
  - user: "@user_a"
    leadership_score: 0.89
    in_degree_rank: 0.98
    pagerank_rank: 0.95
```

## Validation Checklist

- [ ] Network construction matches interaction semantics
- [ ] Self-loops handled appropriately
- [ ] Edge weights normalized if needed
- [ ] Disconnected components analyzed separately if needed
- [ ] Temporal snapshots have sufficient data per period
- [ ] Community detection resolution parameter justified
