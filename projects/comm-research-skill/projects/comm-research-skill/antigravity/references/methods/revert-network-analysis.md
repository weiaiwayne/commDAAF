# Revert Network Analysis

*Added from Wikipedia Epistemic Authority study (March 2026)*

## Overview

Build and analyze networks from revert/deletion relationships on collaborative platforms (Wikipedia, wikis, GitHub). Reveals power asymmetries: who can remove others' work vs. whose work gets removed.

## When to Use

- Analyzing Wikipedia edit wars
- Studying moderation dynamics on any platform with revision history
- Identifying gatekeepers and power structures in collaborative spaces
- Detecting asymmetric editing patterns

## Core Concept: The Revert Network

A directed network where:
- **Nodes** = Editors/users
- **Edges** = Revert relationships (A→B means A reverted B's edit)
- **Edge weight** = Number of reverts

This captures WHO removes WHOSE contributions—a direct measure of editorial power.

## Role Classification

Classify editors into structural roles based on revert behavior:

| Role | Definition | Interpretation |
|------|------------|----------------|
| **Reverter** | Reverts others, never reverted | Gatekeepers—edits stand |
| **Reverted** | Reverted by others, never reverts | Peripheral—contributions removed |
| **Bidirectional** | Both reverts and is reverted | Contested—engaged in mutual conflicts |

## Expected Distributions (Baseline)

From Yasseri et al. (2012) and Wikipedia Epistemic Authority study:

| Role | Typical Range |
|------|---------------|
| Reverters | 35-45% |
| Reverted | 55-65% |
| Bidirectional | <5% |

**Key finding:** ~40/60 reverter/reverted split appears structural across different topics and time periods. If your sample differs dramatically, investigate why.

## Metrics to Calculate

### 1. Role Distribution
```
reverters = [e for e in editors if out_degree(e) > 0 and in_degree(e) == 0]
reverted = [e for e in editors if in_degree(e) > 0 and out_degree(e) == 0]
bidirectional = [e for e in editors if out_degree(e) > 0 and in_degree(e) > 0]
```

### 2. Concentration (Top Reverters)
- % of reverts by top 5/10 reverters
- Whether top reverters are ever reverted (usually no)

### 3. Cross-Article Specialists
- Editors appearing across multiple related articles
- May indicate topical specialization or systematic patrolling

### 4. Reciprocity
- % of reverters who are also reverted
- Low reciprocity = asymmetric power structure

## Probing Questions

1. **What platform/corpus?** (Wikipedia, GitHub, other wiki)
2. **How are reverts identified?** (API field, comment parsing, diff analysis)
3. **What time period?** (acute crisis vs. long-term)
4. **What's the article/repo scope?** (single article, topic cluster, platform-wide)
5. **Any protection levels to account for?** (EC-protected = credential barrier)

## Data Collection (Wikipedia)

### Option A: Wikipedia API
```python
# Get revision history with rv_tags
params = {
    'action': 'query',
    'prop': 'revisions',
    'titles': article_title,
    'rvlimit': 'max',
    'rvprop': 'ids|user|comment|tags'
}
# Filter for mw-revert tag
```

### Option B: XTools
- https://xtools.wmcloud.org/articleinfo/{lang}/{article}
- Provides revert counts per editor

### Option C: Existing Datasets
- Wikimedia dumps (large scale)
- ConflictWiki datasets

## Analysis Protocol

1. **Collect revisions** with user and timestamp
2. **Identify reverts** (tag or comment-based)
3. **Build directed network** (reverter → reverted)
4. **Calculate role classification** for each editor
5. **Compute concentration metrics** (top reverters' share)
6. **Compare to baselines** (40/60 split expected)
7. **Identify cross-topic specialists** if multi-article

## Integration with Discourse Analysis

**Map talk page participants to network roles:**

1. Extract talk page excerpts
2. Identify editors in each excerpt
3. Look up their network role (reverter/reverted/bidirectional)
4. Analyze whether structural position predicts discursive strategy

**Example finding:** "Editors in 'reverter' positions invoke policy 3x more frequently than those in 'reverted' positions."

## Pitfalls

- ❌ Treating all reverts equally (some remove vandalism, some remove valid content)
- ❌ Ignoring protection levels (EC articles exclude non-credentialed editors)
- ❌ Short time windows (need enough reverts for stable patterns)
- ❌ Single-article analysis (patterns may be article-specific)
- ❌ Assuming reverter = "correct" (structural power ≠ epistemic validity)

## Structural Isomorphism Finding

The Wikipedia study found **near-identical role distributions** across temporally distinct conflict clusters (Iran 2026 vs Gaza 2023-26):

| Cluster | Reverters | Reverted |
|---------|-----------|----------|
| Iran (acute) | 41.4% | 58.3% |
| Gaza (chronic) | 42.7% | 57.3% |

This suggests **platform structure** rather than topic dynamics drives these patterns. The 40/60 split may be a structural feature of Wikipedia's controversial article ecosystem.

## Reporting

> "We constructed a revert network from N revisions across M articles. Role classification revealed K% reverters vs L% reverted (cf. Yasseri et al. 2012 baseline: 35-45%/55-65%). The top 5 reverters accounted for X% of all reverts, and none were ever reverted themselves, indicating concentrated gatekeeping power."

## References

- Yasseri, T., et al. (2012). Dynamics of conflicts in Wikipedia. PLoS ONE.
- Kittur, A., et al. (2007). He says, she says: Conflict and coordination in Wikipedia. CHI 2007.
- Wikipedia Epistemic Authority study (AgentAcademy, 2026)
