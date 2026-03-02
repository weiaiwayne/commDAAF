# LTTN: Latent Temporal-Thematic Network Analysis

⚠️ **EXPERIMENTAL** — This method is under active development. Use with caution and validate results carefully.

**Author:** Wayne Xu  
**Version:** 2.0  
**Status:** Research prototype

---

## Overview

LTTN (Latent Temporal-Thematic Network) detects **information flow patterns** in social media by creating directional edges between semantically similar posts within a time window.

**Key Innovation (v2):** Solves the "Hashtag Glue Effect" where generic hashtags (#Ukraine, #news) artificially cluster unrelated posts.

### The Problem: Hashtag Glue Effect

Original similarity methods suffer from:
- Generic, high-frequency hashtags act as artificial bridges
- Posts with only generic hashtags + link cluster together even if links are unrelated
- Low-information hashtags dominate when tweet body is short

### The Solution: Dual-Signal Similarity

LTTN v2 introduces:
1. **Text Decomposition** — Separate body text from hashtags before embedding
2. **Body-Priority Embeddings** — Embed clean body text (without hashtags)
3. **IDF-Weighted Hashtag Similarity** — Rare hashtags (#BuchaMassacre) count more than common ones (#Ukraine)
4. **Composite Scoring** — Weighted combination: body (70%) + hashtags (30%)
5. **Stop-Hashtag Filtering** — Completely exclude most generic tags

---

## When to Use LTTN

✅ **Good fit:**
- Tracking narrative/information flow across groups
- Cross-lingual information spread (LaBSE handles multiple languages)
- Detecting coordinated messaging patterns
- Understanding how topics evolve temporally

❌ **Less suitable:**
- Simple topic clustering (use topic modeling instead)
- Bot detection (LTTN detects similarity, not automation)
- Real-time monitoring (computationally intensive)

---

## Probing Questions (REQUIRED)

```
Q1: What are you trying to detect with LTTN?
    ✓ Information flow between communities
    ✓ Narrative propagation patterns  
    ✓ Cross-lingual content spread
    ✗ "Coordinated behavior" — LTTN detects SIMILARITY, not coordination intent

Q2: What's your time window and why?
    ✓ 6 hours (default) — fast-moving events
    ✓ 24 hours — slower discourse
    ✓ Custom with justification
    ✗ "Default" — MUST justify based on platform/topic dynamics

Q3: How will you handle the body/hashtag weight balance?
    ✓ 70/30 default (body priority)
    ✓ Custom weights with rationale
    Note: Higher body weight = semantic similarity matters more
          Higher hashtag weight = signal similarity matters more

Q4: What stop-hashtags will you use?
    ✓ Domain-specific list (e.g., #Ukraine, #Russia for that conflict)
    ✓ Default generic news tags
    Note: MUST customize for your topic — generic defaults may not fit

Q5: How will you validate the edges?
    ✓ Manual review of sample pairs
    ✓ Stratified by similarity score
    ✓ Inter-rater reliability
    ✗ "Trust the algorithm" — VALIDATION REQUIRED
```

---

## Configuration

```python
@dataclass
class LTTNv2Config:
    """
    Configuration for LTTN v2 Multi-Signal Similarity.
    """
    # Weights (must sum to 1.0)
    body_weight: float = 0.7          # Weight for body text similarity
    hashtag_weight: float = 0.3       # Weight for hashtag similarity
    
    # Thresholds
    similarity_threshold: float = 0.7  # Minimum composite similarity for edge
    min_body_similarity: float = 0.3   # Minimum body-only similarity required
    
    # Hashtag handling
    stop_hashtags: Set[str] = None     # Hashtags to exclude completely
    idf_smoothing: int = 1             # Smoothing for IDF calculation
    
    # Text handling
    min_body_length: int = 20          # Minimum chars; shorter uses full-text fallback
    
    # Temporal
    time_window_hours: int = 6         # Time window for edge creation
    
    # Processing
    batch_size: int = 1000             # Batch size for memory management
```

### Parameter Guidance

| Parameter | Default | When to Adjust |
|-----------|---------|----------------|
| `body_weight` | 0.7 | ↑ if you want semantic meaning to dominate |
| `hashtag_weight` | 0.3 | ↑ if hashtags carry important signal in your domain |
| `similarity_threshold` | 0.7 | ↓ for more edges (noisier), ↑ for fewer (cleaner) |
| `min_body_similarity` | 0.3 | ↑ to filter hashtag-only matches |
| `time_window_hours` | 6 | ↑ for slower platforms (Telegram), ↓ for fast (Twitter) |
| `stop_hashtags` | Generic set | **MUST customize for your topic** |

---

## Algorithm

### Step 1: Text Decomposition

```python
def extract_hashtags(text: str) -> List[str]:
    """Extract hashtags, normalized to lowercase, excluding stop-hashtags."""
    hashtags = re.findall(r'#\w+', text.lower())
    return [h for h in hashtags if h not in stop_hashtags]

def extract_body(text: str) -> str:
    """Extract body text by removing hashtags and cleaning whitespace."""
    body = re.sub(r'#\w+', '', text)
    return ' '.join(body.split()).strip()
```

### Step 2: IDF Calculation for Hashtags

```python
def compute_idf(texts: List[str]) -> Dict[str, float]:
    """
    IDF(t) = log(N / (df(t) + smoothing))
    
    Higher IDF = rarer, more informative hashtag
    Lower IDF = common, less informative hashtag
    """
    doc_freq = Counter()
    for text in texts:
        unique_hashtags = set(extract_hashtags(text))
        for hashtag in unique_hashtags:
            doc_freq[hashtag] += 1
    
    return {
        hashtag: np.log(len(texts) / (df + smoothing))
        for hashtag, df in doc_freq.items()
    }
```

### Step 3: Body-Priority Embeddings

```python
# Use LaBSE for cross-lingual semantic embeddings
model = SentenceTransformer('sentence-transformers/LaBSE')

# Embed body text (not full text with hashtags)
def get_embedding_text(row):
    if len(row['body_text']) >= min_body_length:
        return row['body_text']  # Body only
    else:
        return row['text']  # Fallback to full text for short posts

embeddings = model.encode(df['embedding_text'].tolist())
```

### Step 4: Multi-Signal Similarity

```python
def calculate_composite_similarity(
    embedding1, embedding2,
    hashtags1, hashtags2
) -> Tuple[float, float, float]:
    """
    Returns: (composite_similarity, body_similarity, hashtag_similarity)
    """
    # Body similarity (cosine of embeddings)
    body_sim = cosine_similarity(embedding1, embedding2)
    
    # Hashtag similarity (IDF-weighted Jaccard)
    shared = set(hashtags1) & set(hashtags2)
    union = set(hashtags1) | set(hashtags2)
    
    shared_weight = sum(idf.get(h, 0) for h in shared)
    union_weight = sum(idf.get(h, 0) for h in union)
    hashtag_sim = shared_weight / union_weight if union_weight > 0 else 0
    
    # Composite
    composite = body_weight * body_sim + hashtag_weight * hashtag_sim
    
    return composite, body_sim, hashtag_sim
```

### Step 5: Temporal Edge Creation

```python
def create_edges(df, config):
    """
    Create directional edges between posts within time window
    that exceed similarity threshold.
    """
    edges = []
    
    for i, source in df.iterrows():
        # Find targets within time window (AFTER source)
        window_end = source['time'] + timedelta(hours=config.time_window_hours)
        targets = df[(df['time'] > source['time']) & (df['time'] <= window_end)]
        
        for j, target in targets.iterrows():
            composite, body, hashtag = calculate_composite_similarity(
                source['embedding'], target['embedding'],
                source['hashtags'], target['hashtags']
            )
            
            # Check thresholds
            if composite >= config.similarity_threshold:
                if body >= config.min_body_similarity:
                    edges.append({
                        'from': source['id'],
                        'to': target['id'],
                        'composite_similarity': composite,
                        'body_similarity': body,
                        'hashtag_similarity': hashtag,
                        'time_lag_hours': (target['time'] - source['time']).hours
                    })
    
    return edges
```

### Step 6: Aggregation (Optional)

```python
def aggregate_to_groups(edges, df, group_col):
    """
    Aggregate document-level edges to group-level flow.
    E.g., flow between user categories, communities, countries.
    """
    # Map documents to groups
    edges['from_group'] = edges['from'].map(df[group_col])
    edges['to_group'] = edges['to'].map(df[group_col])
    
    # Remove self-loops
    edges = edges[edges['from_group'] != edges['to_group']]
    
    # Aggregate
    flow = edges.groupby(['from_group', 'to_group']).agg(
        link_count=('from', 'size'),
        avg_composite_similarity=('composite_similarity', 'mean'),
        avg_body_similarity=('body_similarity', 'mean'),
        avg_hashtag_similarity=('hashtag_similarity', 'mean')
    )
    
    return flow
```

---

## Validation Protocol

**LTTN edges MUST be validated before interpretation.**

### Validation Sample Strategy

```python
def generate_validation_sample(edges, n=100):
    """
    Stratified sample across similarity ranges.
    """
    # Stratify by body similarity
    edges['body_sim_bin'] = pd.cut(
        edges['body_similarity'],
        bins=[0, 0.4, 0.6, 0.8, 1.0],
        labels=['low', 'medium', 'high', 'very_high']
    )
    
    # Sample from each bin
    samples = []
    for bin_name in ['low', 'medium', 'high', 'very_high']:
        bin_edges = edges[edges['body_sim_bin'] == bin_name]
        samples.append(bin_edges.sample(min(25, len(bin_edges))))
    
    return pd.concat(samples)
```

### Human Scoring Guide

| Score | Label | Description |
|-------|-------|-------------|
| **5** | Identical | Near-duplicate, translation, or repost |
| **4** | High | Same topic, similar argument/theme |
| **3** | Moderate | Broadly shared topic, different focus |
| **2** | Weak | Shared generic hashtags/keywords, no semantic link |
| **1** | Unrelated | False positive |

### Validation Requirements

```yaml
validation:
  minimum_sample: 100 pairs
  stratified_by: body_similarity bins
  coders: 2+ (calculate inter-rater reliability)
  target_agreement: κ >= 0.7
  
  focus_areas:
    - Pairs in 0.70-0.80 range (edge cases)
    - Low body / high hashtag similarity (potential hashtag glue)
    - Cross-lingual pairs (LaBSE performance)
```

---

## Output Schema

### Edge List (CSV)

| Column | Type | Description |
|--------|------|-------------|
| `from` | str | Source document ID |
| `to` | str | Target document ID |
| `composite_similarity` | float | Weighted composite score |
| `body_similarity` | float | Cosine similarity of body embeddings |
| `hashtag_similarity` | float | IDF-weighted hashtag Jaccard |
| `time_lag_hours` | float | Hours between posts |

### Aggregated Flow (CSV)

| Column | Type | Description |
|--------|------|-------------|
| `from_group` | str | Source group |
| `to_group` | str | Target group |
| `link_count` | int | Number of edges |
| `avg_composite_similarity` | float | Mean composite similarity |
| `flow_normalized_by_source` | float | Edges / source group size |

### Network (GraphML)

Exportable to Gephi, NetworkX for visualization:
- Nodes = groups
- Edges = flow with similarity attributes

---

## Known Limitations

⚠️ **Communicate these in publications:**

1. **Similarity ≠ Influence** — LTTN detects similar content appearing later, not causation
2. **Threshold sensitivity** — Results depend heavily on similarity_threshold choice
3. **Stop-hashtag dependency** — Wrong stop-hashtags can miss or inflate patterns
4. **Computational cost** — O(n²) in worst case; batch processing helps but still expensive
5. **LaBSE limitations** — May struggle with very short text, domain-specific language
6. **Temporal assumption** — Assumes later post was influenced by earlier; may not hold

---

## Comparison to Other Methods

| Method | Detects | LTTN Advantage |
|--------|---------|----------------|
| **Coordinated Behavior** | Temporal co-posting | LTTN adds semantic similarity |
| **Topic Modeling** | Thematic clusters | LTTN adds temporal direction |
| **Network Analysis** | Structural patterns | LTTN creates edges from content |
| **Simple Embedding Similarity** | Semantic similarity | LTTN handles hashtag glue problem |

---

## Example Use Case

**Research Question:** How do narratives about [event] flow between pro-X and pro-Y communities?

```python
# Configuration
config = LTTNv2Config(
    body_weight=0.7,
    hashtag_weight=0.3,
    similarity_threshold=0.75,  # Stricter for cleaner flow
    time_window_hours=12,       # 12-hour window for Telegram
    stop_hashtags={'#ukraine', '#russia', '#war', ...}
)

# Run LTTN
edges = calculate_directional_flow_v2(df, config)

# Aggregate to community level
flow = aggregate_to_groups(edges, df, group_col='community')

# Validate
validation_sample = generate_validation_sample(edges, n=100)
# → Human review → Calculate agreement → Report in paper
```

---

## Citation

If using LTTN, cite:

```bibtex
@software{xu2026lttn,
  author = {Xu, Wayne},
  title = {LTTN: Latent Temporal-Thematic Network Analysis},
  version = {2.0},
  year = {2026},
  note = {Experimental method for detecting information flow in social media}
}
```

---

## Development Status

| Component | Status |
|-----------|--------|
| Core algorithm | ✅ Implemented |
| IDF-weighted hashtags | ✅ Implemented |
| LaBSE embeddings | ✅ Implemented |
| Validation protocol | ✅ Defined |
| Benchmarking vs v1 | 🔄 In progress |
| Parameter sensitivity analysis | 📋 Planned |
| Documentation | ✅ This file |

**Feedback welcome.** This method is under active development.

---

*Part of Communication Research Skill for OpenClaw*
