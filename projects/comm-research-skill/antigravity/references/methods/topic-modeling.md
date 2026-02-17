# Topic Modeling

## Probing Questions (ALL REQUIRED)

```
Q1: Why topic modeling specifically?
    ✓ Exploratory — discovering themes
    ✓ No predetermined categories
    ✓ Large corpus, can't read manually
    ✗ "To analyze the text" — TOO VAGUE

Q2: How many topics (K) and WHY?
    ✓ Theory-driven expectation
    ✓ Will test multiple K values
    ✓ Domain expertise estimate
    ✗ "Whatever the model gives" — YOUR CHOICE
    ✗ "10 seems reasonable" — NOT A JUSTIFICATION

Q3: What preprocessing?
    Must specify ALL:
    - Stopwords (which list?)
    - Stemming/lemmatization
    - Min/max document frequency
    - URL/mention handling

Q4: What counts as one 'document'?
    ✓ Each post
    ✓ Aggregated by user
    ✓ Aggregated by thread
    ✗ "The tweets" — BE SPECIFIC

Q5: How will you handle short documents?
    ✓ Aggregate
    ✓ Use BERTopic
    ✓ Set minimum length
    Required if avg doc length < 50 words

Q6: How will you validate topics?
    ✓ Read 20+ documents per topic
    ✓ Calculate coherence scores
    ✓ Domain expert review
    ✗ "Look at top words" — INSUFFICIENT

Q7: Who will name topics and how?
    ✓ After reading documents
    ✓ Multiple coders independently
    ✗ "From top words" — OFTEN MISLEADING
```

## Approaches

| Method | Best For | Document Length | Speed |
|--------|----------|-----------------|-------|
| **LDA** | Interpretability | Long (100+ words) | Fast |
| **BERTopic** | Short texts, semantics | Any | Medium |
| **NMF** | Sparse data | Medium | Fast |
| **Top2Vec** | Automatic K | Any | Slow |

## K Selection Strategy

1. **Start with theory** — How many themes do you expect?
2. **Test range** — Run K = [theory-5, theory+10]
3. **Coherence scores** — Use c_v or u_mass
4. **Human validation** — Read actual documents
5. **Elbow method** — Plot perplexity/coherence

## Critical Checks

- [ ] K justified (not arbitrary)
- [ ] Preprocessing documented
- [ ] Short document strategy defined
- [ ] Human reads 20+ docs per topic
- [ ] Topic names from documents, not just words
