# Guided Pipeline: Twitter Network Analysis (Historical Data)

> End-to-end workflow for post-API era Twitter research

---

## Overview

| Aspect | Details |
|--------|---------|
| **Goal** | Analyze information diffusion, gatekeeping, or influence |
| **Data** | Historical Twitter (post-API strategies) |
| **Time** | 🟢 4-6 hrs \| 🟡 2-3 days \| 🔴 1-2 weeks |
| **Theory** | Gatekeeping, agenda-setting, networked publics |

---

## Phase 1: Data Acquisition (Post-API)

### Step 1.1: Assess Availability

**Reality check** — What can you actually get?

| Strategy | Coverage | Cost | Effort |
|----------|----------|------|--------|
| **Wayback Machine** | 10-30% (popular content) | Free | Medium |
| **Existing datasets** | Varies | Free | Low |
| **Purchased data** | High | $$$$ | Low |
| **Bluesky alternative** | Growing | Free | Low |

**⚠️ CONSCIOUS CHOICE REQUIRED**

```
Your time period: _______________
Your phenomenon: _______________

Which strategy fits?
[ ] Wayback Machine — My topic was high-profile
[ ] Existing dataset — Check Harvard Dataverse, ICPSR
[ ] Purchase data — I have budget
[ ] Bluesky — Acceptable alternative platform

Justification: _______________
```

### Step 1.2: Data Collection

**For Wayback Machine:**
```python
# Example: Retrieve archived Twitter pages
import wayback

# Define targets
handles = ['@account1', '@account2']
date_range = ('2019-09-01', '2019-09-30')

# Collect snapshots
for handle in handles:
    snapshots = wayback.search(f'twitter.com/{handle}', date_range)
    # Parse HTML to extract tweets
```

**For Existing Datasets:**
Search: `[topic] twitter dataset site:dataverse.harvard.edu`

### Step 1.3: Document Provenance

```markdown
## Data Provenance

- **Source**: [Wayback/Dataset name/etc.]
- **Collection date**: [When you collected]
- **Time period**: [Start] to [End]
- **Coverage**: [Estimated %]
- **Known gaps**: [What's missing]
- **Limitations**: [Acknowledge]
```

---

## Phase 2: Data Preparation

### Step 2.1: Load and Profile

```python
import pandas as pd

# Load data
tweets = pd.read_json('data/tweets.json', lines=True)

# Profile
print(f"Total tweets: {len(tweets):,}")
print(f"Unique users: {tweets['user_id'].nunique():,}")
print(f"Date range: {tweets['created_at'].min()} to {tweets['created_at'].max()}")
print(f"Missing text: {tweets['text'].isna().sum()}")
```

### Step 2.2: Quality Assessment

**Checklist (time by tier):**

| Check | 🟢 5 min | 🟡 30 min | 🔴 2 hrs |
|-------|----------|-----------|----------|
| Duplicates | Count | Remove + document | Analyze pattern |
| Missing data | Note | Strategy | Imputation |
| Date gaps | Visualize | Document | Analyze bias |
| Bot presence | Skip | Basic heuristics | Multi-method |

### Step 2.3: Bot Filtering

```python
# Tier-appropriate bot detection
if tier == "exploratory":
    pass  # Skip for exploration
    
elif tier == "pilot":
    # Basic heuristics
    tweets['is_bot'] = (
        (tweets['tweet_count'] > 1000) & 
        (tweets['account_age_days'] < 30)
    )
    print(f"Bot flagged: {tweets['is_bot'].mean():.1%}")
    
elif tier == "publication":
    # Multiple methods + manual review
    # ... comprehensive detection
```

---

## Phase 3: Network Construction

### Step 3.1: Choose Edge Type

**⚠️ CONSCIOUS CHOICE REQUIRED — No defaults allowed**

```
EDGE TYPE SELECTION

Research question: _______________

Options:
A. RETWEET — Information diffusion, amplification
   → Use if studying: spread, influence cascades
   → Limitation: Bots amplify, performative sharing

B. MENTION — Conversation, attention
   → Use if studying: discourse, engagement
   → Limitation: @mention ≠ endorsement

C. SEMANTIC SIMILARITY — Thematic alignment
   → Use if studying: framing, echoing
   → Limitation: Similarity ≠ agreement

Your choice: [ ]

Why this answers your RQ: _______________

What it MISSES that matters: _______________
```

### Step 3.2: Build Network

```python
import networkx as nx

# Example: Retweet network
G = nx.DiGraph()

for _, tweet in tweets.iterrows():
    if tweet.get('retweeted_user'):
        # Edge: original → retweeter (influence direction)
        G.add_edge(
            tweet['retweeted_user'],
            tweet['user'],
            weight=G.get_edge_data(
                tweet['retweeted_user'], 
                tweet['user'], 
                {'weight': 0}
            )['weight'] + 1
        )

print(f"Nodes: {G.number_of_nodes():,}")
print(f"Edges: {G.number_of_edges():,}")
```

### Step 3.3: Validate Structure

```python
# Basic validation
print(f"Density: {nx.density(G):.4f}")
print(f"Components: {nx.number_weakly_connected_components(G)}")

# Check for problems
if nx.density(G) < 0.001:
    print("⚠️ Very sparse — may be too fragmented")
    
if nx.density(G) > 0.1:
    print("⚠️ Very dense — check for artifacts")
```

---

## Phase 4: Analysis

### Step 4.1: Centrality Analysis

```python
# Calculate centrality
centrality = {
    'in_degree': nx.in_degree_centrality(G),
    'out_degree': nx.out_degree_centrality(G),
    'betweenness': nx.betweenness_centrality(G),  # Expensive
}

# Top nodes
for measure, scores in centrality.items():
    top_5 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"\n{measure}:")
    for node, score in top_5:
        print(f"  {node}: {score:.4f}")
```

**⚠️ VALIDATION REQUIRED**

```
TOP NODE VALIDATION

For each top-5 node, verify:
[ ] Is this a real account (not bot)?
[ ] Does high centrality make substantive sense?
[ ] What role does this account play?

Node 1: _____ Role: _____ Valid: [ ]
Node 2: _____ Role: _____ Valid: [ ]
...
```

### Step 4.2: Community Detection

```python
# Community detection
import community as community_louvain

# Convert to undirected for Louvain
G_undirected = G.to_undirected()
partition = community_louvain.best_partition(G_undirected)

n_communities = len(set(partition.values()))
print(f"Communities detected: {n_communities}")

# Modularity
modularity = community_louvain.modularity(partition, G_undirected)
print(f"Modularity: {modularity:.3f}")

if modularity < 0.3:
    print("⚠️ Low modularity — weak community structure")
```

**Stability Check (🟡🔴 tiers):**
```python
# Run multiple times, check consistency
partitions = []
for i in range(5):
    p = community_louvain.best_partition(G_undirected)
    partitions.append(p)

# Calculate stability (NMI between runs)
# Threshold: ≥80% for publication
```

---

## Phase 5: Validation

### By Tier

| Check | 🟢 Exploratory | 🟡 Pilot | 🔴 Publication |
|-------|----------------|----------|----------------|
| Data quality | Noted | Documented | Exhaustive |
| Bot detection | Skipped | Basic | Multi-method |
| Top nodes | Glanced | Top 5 verified | Top 10 verified |
| Community stability | Skipped | 3 runs | 5+ runs |
| Robustness | Parameter check | Subsample | Bootstrap |

### Robustness Checks (🟡🔴)

```python
# Subsample replication
for pct in [0.9, 0.8, 0.7]:
    G_sample = sample_network(G, pct)
    centrality_sample = nx.betweenness_centrality(G_sample)
    # Compare rank correlation with full network
    # Should be stable (r > 0.8)
```

---

## Phase 6: Interpretation

### Step 6.1: Context Checklist

Before interpreting, verify:

```
CONTEXT CHECKLIST

Data Context:
[ ] Coverage documented (what's missing?)
[ ] Time period representative?
[ ] Population bounded (who's included/excluded?)

Platform Context:
[ ] Algorithm effects considered?
[ ] Platform changes during period?

Analysis Context:
[ ] Edge type limitations acknowledged?
[ ] Centrality interpretation grounded in theory?
[ ] Alternative explanations considered?
```

### Step 6.2: Theory Integration

Connect findings to communication theory:

| Finding | Theoretical Interpretation |
|---------|---------------------------|
| High betweenness of @X | Potential gatekeeper (verify behaviorally) |
| 4 communities | Distinct publics or echo chambers? |
| Central node = news org | Intermedia agenda-setting |

### Step 6.3: Limitation Acknowledgment

**Required statement:**
```
Limitations of this analysis include:
1. [Data coverage limitation]
2. [Method limitation]
3. [Generalizability limitation]
```

---

## Outputs

By the end, you should have:

- [ ] Data provenance document
- [ ] Quality assessment report
- [ ] Network construction documentation
- [ ] Centrality results with validation
- [ ] Community detection with stability check
- [ ] Interpretation with theory integration
- [ ] Limitations acknowledged

---

## Time Summary

| Phase | 🟢 Exploratory | 🟡 Pilot | 🔴 Publication |
|-------|----------------|----------|----------------|
| Data acquisition | 1-2 hrs | 2-4 hrs | 1-2 days |
| Data preparation | 30 min | 1-2 hrs | 4-6 hrs |
| Network construction | 30 min | 1-2 hrs | 4-6 hrs |
| Analysis | 1-2 hrs | 4-6 hrs | 2-3 days |
| Validation | 30 min | 2-4 hrs | 2-3 days |
| Interpretation | 30 min | 2-4 hrs | 1-2 days |
| **TOTAL** | **4-6 hrs** | **2-3 days** | **1-2 weeks** |

---

*Guided Pipeline | CommDAAF v0.3*
