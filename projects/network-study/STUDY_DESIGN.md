# Cross-Layer Behavioral Discordance: A Novel Method for Coordination Detection

## Abstract

We propose **Cross-Layer Behavioral Discordance (CLBD)** as a novel structural indicator for detecting potentially coordinated accounts on social media. Unlike existing methods (e.g., CooRnet) that detect coordination through shared content (URLs) posted at similar times, CLBD identifies accounts whose interaction patterns are inconsistent across network layers (retweets, replies, quotes). Our analysis of 266,242 Ukraine-related tweets reveals 165 high-confidence anomalous accounts exhibiting multiple coordination signals.

## Introduction

### Existing Methods

**CooRnet/CooRTweet** (Giglietto et al., 2020) detects Coordinated Link Sharing Behavior (CLSB) by identifying accounts that share the same URLs within temporal windows. This approach:
- Requires content matching (URLs/images)
- Detects group-level coordination
- Content-dependent

### Gap in Literature

No existing method systematically analyzes **cross-layer behavioral consistency** at the individual account level. Organic users typically engage consistently across interaction types—if they retweet someone, they may also reply to or quote them occasionally. Coordinated accounts may show layer-specific behavior optimized for amplification.

## Novel Contribution: Cross-Layer Behavioral Discordance

### Definition

For each user, we define:
- **RT_targets**: Set of accounts the user retweeted
- **Convo_targets**: Set of accounts the user replied to OR quoted

**Cross-Layer Jaccard Similarity:**
```
CLBD_score = |RT_targets ∩ Convo_targets| / |RT_targets ∪ Convo_targets|
```

- **Score = 1.0**: Perfect consistency (same targets across layers)
- **Score = 0.0**: Complete discordance (no overlap between RT and conversation targets)

### Theoretical Justification

Organic social media behavior involves multi-modal engagement:
1. Users discover content creators through various means
2. Genuine interest leads to diverse engagement (RT + reply + follow)
3. Conversation targets should overlap with amplification targets

Coordinated amplification behavior:
1. Single-purpose accounts designed for reach maximization
2. RT high-profile targets for visibility
3. Minimal genuine conversation (if any, with different accounts)
4. Cross-layer overlap approaches zero

## Method

### Data
- **Source**: Ukraine-related tweets, June 7-9, 2023
- **Volume**: 266,242 tweets from 102,706 users
- **Collection**: Hashtag/keyword search

### Network Construction
Three directed networks built from explicit relationships:
1. **Retweet network**: 87,267 nodes, 150,581 edges
2. **Reply network**: 11,153 nodes, 11,504 edges
3. **Quote network**: 9,362 nodes, 10,387 edges

### Metrics Calculated
1. **Cross-Layer Jaccard** (novel): RT_targets vs Convo_targets overlap
2. **Reciprocity**: Proportion of reply targets who reply back
3. **Degree ratio**: Out-degree / (In-degree + 1)
4. **Layer count**: Number of network layers user appears in

### Multi-Signal Anomaly Detection
Combined indicator requiring multiple signals:
- Signal 1: Zero cross-layer overlap (discordant)
- Signal 2: Zero reply reciprocity
- Signal 3: Degree ratio > 5 (amplifier pattern)
- Signal 4: Single-layer activity

High-confidence anomaly: 3+ signals AND out-degree ≥ 10

## Results

### Cross-Layer Discordance Distribution

| Jaccard Score | Count | Percentage |
|---------------|-------|------------|
| Zero (completely discordant) | 2,577 | 80.3% |
| Low (0 < J < 0.1) | 138 | 4.3% |
| Medium (0.1-0.3) | 229 | 7.1% |
| High (≥0.3) | 267 | 8.3% |

**Finding**: 80.3% of multi-layer users show complete behavioral discordance.

### Reciprocity Analysis

| Metric | Value |
|--------|-------|
| Mean reciprocity | 0.3% |
| Zero reciprocity | 99.6% |

**Finding**: Nearly all users who reply receive zero replies back.

### Multi-Signal Anomaly Detection

| Anomaly Signals | Count | Percentage |
|-----------------|-------|------------|
| 0 | 3,372 | 3.4% |
| 1 | 87,358 | 88.2% |
| 2 | 7,979 | 8.1% |
| 3+ | 376 | 0.4% |

**High-confidence anomalies** (3+ signals, ≥10 out-degree): **165 accounts**

### Top Anomalous Accounts

| Username | Out-degree | In-degree | Layer Count | Signals |
|----------|------------|-----------|-------------|---------|
| joseperez1026 | 57 | 1 | 2 | 3 |
| antokrx | 43 | 1 | 1 | 3 |
| o_schei88191 | 42 | 3 | 2 | 3 |
| vbright4 | 38 | 0 | 2 | 3 |
| connorf83722540 | 37 | 1 | 3 | 3 |

### Cross-Validation

Comparison with simple broadcast detection (high RT, no replies):
- Broadcast-flagged: 552 accounts
- Multi-signal flagged: 165 accounts
- **Overlap: 0 accounts**

**Finding**: CLBD identifies a distinct set of suspicious accounts not captured by broadcast-only detection.

## Discussion

### Advantages of CLBD

1. **Content-independent**: No URL/text matching required
2. **Individual-level**: Detects per-account anomalies, not just group coordination
3. **Cross-platform applicable**: Works wherever multi-modal engagement exists
4. **Complementary**: Identifies accounts missed by existing methods

### Limitations

1. **Requires multi-layer activity**: Cannot score single-layer users
2. **Legitimate discordance exists**: Users may RT news but converse with friends
3. **Short time window**: 3-day window may not capture full engagement patterns
4. **No ground truth**: Cannot validate against known coordination labels

### Interpretation Caution

Zero cross-layer overlap alone does not confirm coordination. The multi-signal approach (CLBD + reciprocity + amplifier pattern) provides higher confidence but still requires:
- Temporal analysis (coordinated posting times)
- Content analysis (amplifying same sources)
- Account metadata (creation date clustering, follower overlap)

## Conclusion

Cross-Layer Behavioral Discordance offers a novel structural approach to coordination detection that complements existing content-based methods. The identification of 165 high-confidence anomalous accounts demonstrates the method's potential, though validation against ground truth remains necessary.

## Files

- `/tmp/ukr_networks.pkl` — Network objects
- `/tmp/ukr_structural_metrics.csv` — Per-user metrics (99,085 rows)
- `/tmp/ukr_cross_layer_discordance.csv` — CLBD scores (3,211 rows)
- `/tmp/ukr_high_confidence_anomalies.csv` — Flagged accounts (165 rows)

## References

Giglietto, F., Righetti, N., Rossi, L., & Marino, G. (2020). It takes a village to manipulate the media: coordinated link sharing behavior during 2018 and 2019 Italian elections. *Information, Communication & Society*, 23(6), 867-891.

Righetti, N., & Balluff, P. (2025). CooRTweet: A Generalized R Software for Coordinated Network Detection. *Computational Communication Research*, 7(1), 1.
