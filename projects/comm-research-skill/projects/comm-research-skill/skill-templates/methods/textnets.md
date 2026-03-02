# TextNets: Text Analysis with Networks

Bipartite network analysis of documents and words.

---

## Overview

**TextNets** represents collections of texts as **bipartite networks** of documents and words. This enables novel visualization and analysis possibilities by applying network science concepts to text data.

**Key Idea:** Documents are connected through shared terms, and terms are connected through shared documents. Community detection on this bipartite structure reveals latent themes.

---

## When to Use TextNets

✅ **Good fit:**
- Discovering latent themes/topics in a corpus
- Identifying "cultural bridges" — documents linking themes
- Visualizing document-term relationships
- Comparing how different groups use language
- Finding discursive communities

❌ **Less suitable:**
- Temporal analysis (use LTTN instead)
- Information flow/diffusion (use LTTN or RNewsflow)
- Classification tasks (use LLM annotation)
- Large-scale corpora (>100K docs may be slow)

---

## Probing Questions (REQUIRED)

```
Q1: What is your unit of analysis?
    ✓ Documents (e.g., articles, tweets, speeches)
    ✓ Terms (words, phrases, n-grams)
    ✓ Both (bipartite analysis)
    ✗ "The text" — BE SPECIFIC

Q2: What type of terms will you extract?
    ✓ tokenized() — individual words, stemmed
    ✓ ngrams(n) — n-grams of specified size
    ✓ noun_phrases() — noun phrases (requires spaCy model)
    ✗ "Whatever works" — CHOICE AFFECTS RESULTS

Q3: What is min_docs threshold and why?
    ✓ 2 (default) — include rare terms
    ✓ Higher — focus on common terms (less noise)
    Note: Terms appearing in only 1 doc create no links
    ✗ "Default" — JUSTIFY YOUR CHOICE

Q4: How will you interpret clusters?
    ✓ As latent themes/topics
    ✓ As discursive communities
    ✓ Document clusters as groupings
    ✗ "The algorithm found them" — YOU MUST INTERPRET

Q5: What centrality measure is appropriate for your RQ?
    ✓ Betweenness — cultural bridges
    ✓ Degree — document/term importance
    ✓ Spanning — discursive range
    ✗ "All of them" — CHOOSE BASED ON THEORY
```

---

## Installation

```bash
pip install textnets

# Also need a spaCy language model
python -m spacy download en_core_web_sm  # English
python -m spacy download de_core_news_sm  # German
# etc.
```

**Requirements:** Python 3.9+, spaCy, igraph

---

## Core Concepts

### Bipartite Network Structure

```
Documents          Terms
    ┌──────────────────┐
    │                  │
  Doc1 ─────────── word1
    │     \      /     │
    │      \    /      │
  Doc2 ──────X──── word2
    │      /    \      │
    │     /      \     │
  Doc3 ─────────── word3
    │                  │
    └──────────────────┘

- Edges connect documents to terms they contain
- Edge weights = TF-IDF scores
- Clusters = latent themes spanning docs and terms
```

### Projections

**Document Projection:** 
- Nodes = documents
- Edge = shared terms (weighted by overlap)
- Use case: Find similar documents, document clusters

**Term Projection:**
- Nodes = terms
- Edge = co-occurrence in documents
- Use case: Find related concepts, semantic clusters

---

## Basic Usage

```python
import textnets as tn

# Set seed for reproducibility
tn.params["seed"] = 42

# Create corpus from various sources
corpus = tn.Corpus.from_csv("data.csv", doc_col="text", label_col="id")
# or
corpus = tn.Corpus.from_df(df, doc_col="text")
# or
corpus = tn.Corpus.from_dict({"doc1": "text...", "doc2": "text..."})

# Tokenize (removes stopwords, applies stemming)
tokens = corpus.tokenized()

# Create the textnet
t = tn.Textnet(tokens, min_docs=2)

# Visualize bipartite network
t.plot(
    label_nodes=True,
    show_clusters=True,
    scale_nodes_by="birank"
)
```

---

## Term Extraction Options

### Tokenized (Default)

```python
# Individual words, stemmed, stopwords removed
tokens = corpus.tokenized(
    remove_stop_words=True,  # Remove common words
    stem=True,               # Reduce to root form
    sublinear=True          # Sublinear TF-IDF scaling
)
```

### N-grams

```python
# Sequences of N words
bigrams = corpus.ngrams(2)   # "new york", "climate change"
trigrams = corpus.ngrams(3)  # "new york times"
```

### Noun Phrases

```python
# Multi-word noun phrases (requires good spaCy model)
np = corpus.noun_phrases(
    remove=["common phrase to exclude"]
)
```

---

## Textnet Parameters

```python
t = tn.Textnet(
    tokens,
    min_docs=2,        # Minimum docs a term must appear in
    max_docs=None,     # Maximum docs (filter very common terms)
    connected=False,   # Keep only largest connected component?
    doc_attrs={}       # Additional document attributes
)
```

### Parameter Guidance

| Parameter | Default | Guidance |
|-----------|---------|----------|
| `min_docs` | 2 | ↑ for cleaner network, ↓ for rare terms |
| `max_docs` | None | Set to filter very common (uninformative) terms |
| `connected` | False | True if you want single component |

---

## Projections

### Document Network

```python
# Project to document-only network
docs = t.project(node_type=tn.DOC)

# Documents connected if they share terms
# Edge weight = strength of term overlap

# Visualize
docs.plot(
    label_nodes=True,
    scale_nodes_by="betweenness"  # Cultural bridges
)

# Analyze
docs.top_betweenness()    # Bridge documents
docs.top_spanning()       # Discursive range (Stoltz & Taylor 2019)
```

### Term Network

```python
# Project to term-only network
terms = t.project(node_type=tn.TERM)

# Terms connected if they co-occur in documents
# Edge weight = co-occurrence strength

# Visualize with backbone extraction
terms.plot(
    label_nodes=True,
    color_clusters=True,
    alpha=0.4  # Backbone pruning (significance threshold)
)

# Analyze
terms.top_betweenness()   # Bridging concepts
terms.top_degree()        # Central terms
```

---

## Centrality Measures

### For Bipartite Network

```python
# BiRank (bipartite centrality)
t.top_birank()

# HITS (hubs and authorities)
t.top_hits()    # Hub scores
t.top_cohits()  # Authority scores
```

### For Projected Networks

```python
# Standard centrality measures
net.top_betweenness()    # Bridges between clusters
net.top_closeness()      # Close to all other nodes
net.top_degree()         # Most connections (unweighted)
net.top_strength()       # Most connections (weighted)
net.top_ev()             # Eigenvector centrality
net.top_pagerank()       # PageRank

# Special: Textual spanning (documents only)
docs.top_spanning()      # Spans discursive distance
```

### Interpreting Centrality

| Measure | High Score Means |
|---------|------------------|
| **Betweenness** | Bridges between themes; "cultural broker" |
| **Degree** | Uses many different terms / appears in many docs |
| **Spanning** | Similar to dissimilar documents; broad reach |
| **BiRank** | Important in bipartite structure |

---

## Community Detection

TextNets uses the **Leiden algorithm** for community detection, which works on bipartite networks.

```python
# Visualize communities
t.plot(show_clusters=True)
# or
t.plot(color_clusters=True)

# Get cluster assignments
t.top_cluster_nodes()
```

### Interpreting Clusters

- **In bipartite network:** Clusters contain both docs AND terms = latent themes
- **In term network:** Clusters = semantic groupings
- **In document network:** Clusters = document groupings

---

## Visualization Options

```python
t.plot(
    # Node labeling
    label_nodes=True,
    label_term_nodes=True,
    label_doc_nodes=True,
    label_edges=False,
    
    # Scaling
    scale_nodes_by="degree",      # or "birank", "betweenness", etc.
    scale_edges_by="weight",
    
    # Clustering
    show_clusters=True,           # Draw polygons
    color_clusters=True,          # Color by cluster
    
    # Layout (for bipartite)
    layout="bipartite_layout",    # or "circular_layout", "sugiyama_layout"
    
    # Filtering
    node_label_filter=lambda n: n.betweenness() > threshold,
    
    # Backbone (projected only)
    alpha=0.4                     # Significance for edge pruning
)
```

---

## Saving Results

```python
# Save network
t.save_graph("textnet.gml")           # GML format
t.save_graph("textnet.graphml")       # GraphML format

# Save visualization
fig = t.plot(label_nodes=True)
fig.savefig("textnet.png", dpi=300)
fig.savefig("textnet.svg")            # Vector format
```

---

## Complete Example

```python
import textnets as tn
import pandas as pd

# Reproducibility
tn.params["seed"] = 42

# Load data
df = pd.read_csv("speeches.csv")
corpus = tn.Corpus.from_df(df, doc_col="text", lang="en")

# Extract noun phrases for thematic analysis
np = corpus.noun_phrases()

# Create textnet (min 3 docs for cleaner network)
t = tn.Textnet(np, min_docs=3)

# Bipartite visualization
t.plot(
    label_nodes=True,
    show_clusters=True,
    scale_nodes_by="birank"
)

# Project to documents
docs = t.project(node_type=tn.DOC)

# Find cultural bridges
print("Cultural Bridges (high betweenness):")
print(docs.top_betweenness(10))

# Find documents spanning themes
print("\nDiscursive Range (high spanning):")
print(docs.top_spanning(10))

# Project to terms
terms = t.project(node_type=tn.TERM)

# Visualize with backbone
terms.plot(
    label_nodes=True,
    color_clusters=True,
    alpha=0.4,
    scale_nodes_by="betweenness"
)

# Save for Gephi
docs.save_graph("doc_network.graphml")
terms.save_graph("term_network.graphml")
```

---

## Research Applications

### Advocacy Organizations (Bail 2016)
- How do organizations stimulate conversation?
- Which orgs bridge different discourse communities?
- What themes connect disparate groups?

### Political Discourse
- How do politicians' speeches cluster thematically?
- Who are the "cultural bridges" in political discourse?
- What terms link different political communities?

### Media Studies
- How do news sources cover topics differently?
- What themes emerge across coverage?
- Which sources bridge discourse communities?

---

## Validation

### Cluster Interpretation

```yaml
validation_steps:
  1. Examine top terms in each cluster
  2. Read representative documents from each cluster
  3. Name clusters based on content (not just top terms)
  4. Check: Do documents in same cluster actually belong together?
  5. Consider: Multiple researchers independently label clusters
```

### Centrality Validation

```yaml
validation_steps:
  1. Examine high-centrality nodes
  2. Read actual content
  3. Verify interpretation makes sense
  4. Consider: Does high betweenness actually = bridging in your domain?
```

---

## Comparison to Other Methods

| Method | Focus | TextNets Advantage |
|--------|-------|-------------------|
| Topic Modeling | Latent topics | Network structure, visualization |
| Clustering | Document groups | Bipartite structure, term-doc links |
| Word Embeddings | Semantic similarity | Explicit network, interpretable |
| LTTN | Temporal flow | TextNets: thematic structure, no time |

---

## Known Limitations

1. **Bag of words** — ignores word order and context
2. **Computationally intensive** — large corpora may be slow
3. **Parameter sensitivity** — min_docs affects results significantly
4. **TF-IDF weighting** — may not capture semantic similarity as well as embeddings
5. **Language models** — noun_phrases requires good spaCy model

---

## Key Citations

```bibtex
@article{Bail2016,
  author = {Christopher A. Bail},
  title = {Combining natural language processing and network analysis 
           to examine how advocacy organizations stimulate conversation 
           on social media},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {113},
  number = {42},
  pages = {11823--11828},
  year = {2016},
  doi = {10.1073/pnas.1607151113}
}

@article{Boy2020,
  author = {John D. Boy},
  title = {textnets: A Python Package for Text Analysis with Networks},
  journal = {Journal of Open Source Software},
  volume = {5},
  number = {54},
  pages = {2594},
  year = {2020},
  doi = {10.21105/joss.02594}
}

@article{StoltzTaylor2019,
  author = {Dustin S. Stoltz and Marshall A. Taylor},
  title = {Textual Spanning: Finding Discursive Holes in Text Networks},
  journal = {Socius},
  volume = {5},
  year = {2019},
  doi = {10.1177/2378023119827674}
}
```

---

## Resources

- **Documentation:** https://textnets.readthedocs.io
- **GitHub:** https://github.com/jboynyc/textnets
- **PyPI:** https://pypi.org/project/textnets/
- **Tutorial Notebook:** Available in docs

---

*Part of Communication Research Skill for OpenClaw*
