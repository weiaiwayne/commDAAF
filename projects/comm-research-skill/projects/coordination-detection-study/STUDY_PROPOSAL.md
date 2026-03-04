# Novel Study Proposal: Coordination Detection via Temporal-Textual Clustering

**Date:** 2026-03-04
**Status:** PROPOSAL (awaiting approval)

---

## Theoretical Foundation

### From Wayne's Zotero Library:
- **"Amplifying the regime: identifying coordinated activity of pro-government Telegram channels in Russia and Belarus"**
- **"It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections"**
- **"Opinion leadership in a leaderless movement"** (LIHKG study)

### Theory: Coordinated Inauthentic Behavior (CIB)

Coordination detection typically requires platform metadata (account age, posting frequency, follower networks). But what if we could detect coordination from **content patterns alone**?

**Theoretical mechanism:**
1. Coordinated actors post similar content within narrow time windows
2. This creates detectable "bursts" of textually-similar posts
3. Organic content has higher variance in timing and phrasing
4. Coordination signatures may predict engagement differently than organic content

---

## Research Questions

### RQ1: Detection
**Can temporal-textual clustering identify coordination signatures in crisis discourse without account-level metadata?**

### RQ2: Engagement
**Do posts with coordination signatures achieve different engagement than organic posts?**

### RQ3: Cross-Context
**Do coordination patterns differ between war discourse (Ukraine) and protest discourse (#MahsaAmini)?**

---

## Novel Method: Temporal-Textual Clustering (TTC)

**NOT LLM annotation.** This method uses:
- Embedding-based similarity (sentence transformers)
- Time-window clustering
- Statistical detection of non-random patterns

### Step 1: Temporal Binning
```python
# Bin posts into time windows (e.g., 5-minute, 15-minute, 1-hour)
for window_size in [5, 15, 60]:  # minutes
    bins = create_time_bins(posts, window_size)
```

### Step 2: Within-Bin Textual Similarity
```python
# For each bin, compute pairwise cosine similarity
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

for bin in bins:
    embeddings = model.encode([p['text'] for p in bin])
    similarity_matrix = cosine_similarity(embeddings)
    avg_similarity = similarity_matrix.mean()
```

### Step 3: Coordination Score
```python
# Posts are "coordinated" if:
# - Posted within short time window
# - High textual similarity to other posts in window
# - Similarity exceeds baseline (bootstrapped null distribution)

coordination_score = (within_bin_similarity - baseline_similarity) / baseline_std
```

### Step 4: Engagement Comparison
```python
# Compare engagement: coordinated vs organic posts
coordinated = posts[posts['coordination_score'] > 2.0]
organic = posts[posts['coordination_score'] <= 2.0]
effect_size = cohens_d(coordinated['engagement'], organic['engagement'])
```

---

## Why This Is Novel

| Existing Approaches | This Study |
|---------------------|------------|
| Require account metadata | **Content-only detection** |
| Platform-specific features | **Platform-agnostic** |
| Focus on bot detection | **Focus on coordination patterns** |
| Binary classification | **Continuous coordination score** |
| Human annotation for ground truth | **Statistical baseline comparison** |

**Key innovation:** We detect coordination **without knowing who is coordinating** — purely from content timing + similarity patterns.

---

## Dataset Options

| Dataset | N | Time Span | Fit |
|---------|---|-----------|-----|
| #EndSARS | ~60K? | 2 weeks (Oct-Nov 2020) | ✅ High (protest, coordination suspected) |
| UKR-tweets | ~68MB | War period | ✅ High (state actors suspected) |
| Belarus | Previous run | 2020 protests | ⚠️ Already analyzed |
| #MahsaAmini | 400 coded | Sept-Oct 2022 | ⚠️ Small N |

**Recommendation:** #EndSARS — Nigerian protest with suspected coordination, large N, not yet analyzed with this method.

---

## Expected Contributions

### Methodological
1. **Content-only coordination detection** — no account metadata needed
2. **Continuous coordination score** — not binary bot/not-bot
3. **Cross-platform applicable** — works on any timestamped text data

### Theoretical  
1. **Test coordination-engagement relationship** — does coordination boost or hurt engagement?
2. **Compare coordination across crisis types** — war vs protest
3. **Quantify "leaderless" movements** — are they actually leaderless?

### Empirical
1. First application of temporal-textual clustering to crisis discourse
2. Coordination signatures in #EndSARS (understudied African protest)

---

## What Claude Will Do (Single-Model First)

1. Load and preprocess #EndSARS dataset
2. Generate text embeddings (sentence-transformers)
3. Implement temporal binning + similarity calculation
4. Bootstrap null distribution for baseline
5. Calculate coordination scores for all posts
6. Compare engagement: coordinated vs organic
7. Visualize temporal patterns
8. Write preliminary findings

**No LLM annotation involved.**

---

## Validation Plan

Since this is a **new method**, validation requires:

1. **Face validity:** Manually inspect high-coordination posts — do they look coordinated?
2. **Convergent validity:** Do high-coordination posts share other suspicious features (e.g., duplicate text, suspicious timing patterns)?
3. **Predictive validity:** Does coordination score predict engagement differently than random noise?

---

## Questions Before Proceeding

1. Is #EndSARS the right dataset, or prefer another?
2. Time window sizes to test (5min, 15min, 1hr)?
3. Embedding model preference (multilingual needed for #EndSARS?)
4. Any theoretical framing preferences?

---

*Awaiting approval to proceed.*
