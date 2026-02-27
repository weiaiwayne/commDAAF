# Literature Synthesis Skill

Systematic literature search, citation mapping, and synthesis for communication research.

## When to Use

- Starting a new research project
- Writing literature review sections
- Identifying research gaps
- Tracing theoretical lineages
- Finding methodological precedents
- Mapping citation networks

## Capabilities

1. **Semantic Search** - Find papers by concept, not just keywords
2. **Citation Network Mapping** - Who cites whom, influence paths
3. **Theoretical Lineage Tracing** - Foundational papers → current work
4. **Gap Identification** - What hasn't been studied?
5. **Methodology Extraction** - What methods do similar studies use?
6. **Draft Generation** - Structured lit review paragraphs with citations

## Data Sources

| Source | Access | Coverage | Best For |
|--------|--------|----------|----------|
| **Semantic Scholar** | Free API | 200M+ papers | General search, citations |
| **OpenAlex** | Free API | 250M+ works | Open access, metadata |
| **arXiv** | Free API | Preprints | CS, physics, recent work |
| **CrossRef** | Free API | DOI metadata | Citation counts, dates |
| **Google Scholar** | Web scraping | Broadest | H-index, citations |
| **Zotero** | User library | Personal | Your saved papers |

## Usage

### Basic: Concept Search

```
Find the 20 most influential papers on "framing effects in social media" 
from the last 5 years, sorted by citation count.
```

### Advanced: Theoretical Lineage

```
Trace the theoretical lineage of "moral contagion" in political communication:
1. Find Brady et al. 2017 as anchor paper
2. Identify its key citations (theoretical foundations)
3. Find papers that cite it (descendants)
4. Map the citation network
5. Identify current frontiers (recent, low-citation descendants)
```

### Gap Analysis

```
Identify research gaps in "LLM-based content analysis":
1. Search papers 2020-2026
2. Extract methods, platforms, and constructs studied
3. Create coverage matrix
4. Identify understudied combinations
```

## Output Formats

### Paper Summary
```json
{
  "title": "Emotion shapes the diffusion of moralized content",
  "authors": ["Brady, W.J.", "Wills, J.A.", "Jost, J.T.", "Tucker, J.A.", "Van Bavel, J.J."],
  "year": 2017,
  "venue": "PNAS",
  "doi": "10.1073/pnas.1618923114",
  "citations": 1847,
  "abstract": "...",
  "key_findings": [
    "Each moral-emotional word increases retweet rate by ~20%",
    "Effect is strongest for in-group content"
  ],
  "methods": ["Twitter data", "sentiment analysis", "regression"],
  "theoretical_contribution": "Moral contagion theory for social media",
  "limitations": ["Single platform", "US context"],
  "cited_by_influential": ["Vosoughi et al. 2018", "Bail et al. 2018"]
}
```

### Citation Network
```json
{
  "anchor_paper": "Brady et al. 2017",
  "foundations": [
    {"paper": "Haidt 2001", "concept": "moral emotions"},
    {"paper": "Berger & Milkman 2012", "concept": "viral content"}
  ],
  "descendants": [
    {"paper": "Rathje et al. 2021", "extension": "out-group animosity"},
    {"paper": "McLoughlin et al. 2023", "extension": "multimodal content"}
  ],
  "network_metrics": {
    "in_degree": 12,
    "out_degree": 45,
    "betweenness": 0.34
  }
}
```

### Literature Review Draft
```markdown
## Moral Content and Viral Diffusion

Research on content virality has increasingly emphasized the role of 
moral-emotional language. Brady et al. (2017) found that each moral-emotional 
word in a tweet increased its diffusion by approximately 20%, establishing 
the "moral contagion" hypothesis. This builds on earlier work showing that 
high-arousal content spreads more readily than low-arousal content 
(Berger & Milkman, 2012).

Subsequent research has extended this framework in several directions. 
Rathje et al. (2021) demonstrated that out-group animosity drives sharing 
even more strongly than moral language alone. Meanwhile, Vosoughi et al. (2018) 
showed that false news spreads faster than true news, potentially because 
falsehoods trigger stronger emotional responses.

**Research gaps**: Most studies focus on Twitter/X and US contexts. 
Cross-platform and cross-cultural replications remain limited.
```

## Integration with CommDAAF Pipeline

```python
from commdaaf import LiteratureSynthesis

lit = LiteratureSynthesis()

# Search by concept
papers = lit.search(
    query="framing effects social media protest",
    years=(2018, 2026),
    min_citations=10,
    limit=50
)

# Get citation network
network = lit.citation_network(
    anchor_doi="10.1073/pnas.1618923114",
    depth=2,  # 2 levels of citations
    direction="both"  # cited and citing
)

# Trace theoretical lineage
lineage = lit.trace_lineage(
    concept="moral contagion",
    anchor_paper="Brady et al. 2017",
    include_foundations=True,
    include_descendants=True
)

# Identify gaps
gaps = lit.identify_gaps(
    papers=papers,
    dimensions=["platform", "method", "construct", "population"]
)

# Generate draft
draft = lit.generate_review(
    papers=papers[:20],
    structure="thematic",  # or "chronological", "methodological"
    style="apa7"
)
```

## Search Strategies

### 1. Snowball Search
Start with known papers, follow citations bidirectionally:
```python
lit.snowball_search(
    seeds=["10.1073/pnas.1618923114", "10.1126/science.aap9559"],
    generations=2,
    filter_by="communication"
)
```

### 2. Concept Clustering
Group papers by semantic similarity:
```python
clusters = lit.cluster_papers(
    papers=papers,
    n_clusters=5,
    label_method="tfidf"  # Auto-generate cluster labels
)
```

### 3. Methodology Extraction
Find papers using specific methods:
```python
methods_papers = lit.search_by_method(
    methods=["negative binomial regression", "content analysis", "LLM"],
    context="social media"
)
```

## Zotero Integration

Connect to your personal library:
```python
lit.connect_zotero(
    user_id="YOUR_USER_ID",
    api_key="YOUR_API_KEY"
)

# Search your library
my_papers = lit.search_zotero(
    collection="Dissertation",
    tags=["framing", "protest"]
)

# Sync with external search
lit.sync_to_zotero(
    papers=new_papers,
    collection="To Read"
)
```

## Best Practices

1. **Start with anchor papers** - Known influential works in your area
2. **Use multiple sources** - No single database has everything
3. **Check recency** - Old citations may be superseded
4. **Read abstracts** - Don't rely solely on metadata
5. **Verify citations** - Auto-extracted citations can have errors
6. **Document your search** - Save queries for replication

## Limitations

- Citation counts favor older papers
- Not all papers are indexed in free databases
- Semantic search may miss keyword-specific papers
- Auto-generated summaries need human verification
- Some venues (books, reports) poorly covered

## References

- Aria, M., & Cuccurullo, C. (2017). bibliometrix: An R-tool for comprehensive science mapping analysis.
- Chen, C. (2006). CiteSpace II: Detecting and visualizing emerging trends.
- van Eck, N. J., & Waltman, L. (2010). Software survey: VOSviewer.
