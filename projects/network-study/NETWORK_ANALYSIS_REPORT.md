# Structural Anomaly Detection in Ukraine Twitter Network

## Study Overview

**Dataset:** Ukraine-related tweets, June 7-9, 2023
**Sample size:** 266,242 tweets from 102,706 users
**Network:** 99,085 nodes, 171,406 edges (combined RT + reply + quote)

## Research Question

Can structural network anomalies (independent of content) identify potentially coordinated accounts?

## Method

Built three network layers from explicit Twitter relationships:
1. **Retweet network:** A→B if A retweeted B (87,267 nodes, 150,581 edges)
2. **Reply network:** A→B if A replied to B (11,153 nodes, 11,504 edges)
3. **Quote network:** A→B if A quoted B (9,362 nodes, 10,387 edges)

Calculated per-user structural metrics:
- In-degree / out-degree ratio
- Layer presence (RT only vs multi-layer engagement)
- Reply reciprocity (proportion of reply targets who reply back)

## Key Findings

### 1. Network Layer Segregation

| User Type | Count | Percentage |
|-----------|-------|------------|
| RT-only (single layer) | 91,774 | 92.6% |
| 2+ layers | 7,311 | 7.4% |
| All 3 layers | 1,386 | 1.4% |

**Interpretation:** The vast majority of users (93%) only appear in the retweet network — they amplify content but never engage in conversation (replies) or commentary (quotes).

### 2. Reciprocity Collapse

Reply network reciprocity statistics:
- **Mean reciprocity:** 0.003 (0.3%)
- **Median reciprocity:** 0.000
- **Users with zero reciprocity:** 6,303 (99.6% of reply network participants)

**Interpretation:** Nearly all users who reply to others receive zero replies back. This is structurally abnormal for organic conversation. In typical social networks, reciprocity ranges from 15-40%.

### 3. Amplifier Accounts

Top accounts by out-degree/in-degree ratio (pure amplifiers):

| Username | In-degree | Out-degree | Ratio |
|----------|-----------|------------|-------|
| maylisa8919 | 0 | 141 | 141.0 |
| rayospirituano | 0 | 98 | 98.0 |
| mfdiaz940821 | 0 | 86 | 86.0 |
| nailahernndezb1 | 0 | 85 | 85.0 |
| gustavo89902112 | 0 | 73 | 73.0 |
| jrabelol93 | 0 | 68 | 68.0 |
| elfinmad | 0 | 63 | 63.0 |
| onelhurtado2 | 1 | 125 | 62.5 |
| arnaysh | 0 | 62 | 62.0 |
| _notoka | 0 | 62 | 62.0 |

**Pattern:** These accounts retweet 60-141 times in 3 days but receive zero engagement back. Nobody retweets them, replies to them, or quotes them.

### 4. Broadcast Score Distribution

Accounts flagged as "broadcast pattern" (high RT, no replies):
- **High broadcast score (>0.1):** 552 accounts
- **High amplifier score (ratio>10):** 1,133 accounts

## Structural Anomaly Indicators

Based on this analysis, we identify three structural signatures that may indicate coordinated/inauthentic behavior:

### Indicator 1: Layer Isolation
- Organic users typically engage across multiple interaction types
- Users confined to RT-only may be single-purpose amplification accounts

### Indicator 2: Reciprocity Deficit
- Organic conversation involves back-and-forth
- Zero reciprocity suggests broadcast-only behavior

### Indicator 3: Asymmetric Degree Distribution
- Organic influencers have high in-degree (people engage with them)
- Pure amplifiers have high out-degree but zero in-degree

## Questions for Interpretation

1. **What explains the 99.6% zero reciprocity rate?** Is this a property of crisis communication, hashtag-based collection, or evidence of inauthentic behavior?

2. **Are the top amplifier accounts (maylisa8919 etc.) likely coordinated?** What additional evidence would strengthen or weaken this inference?

3. **What null hypothesis should we consider?** Could organic users during a crisis event show similar structural patterns?

4. **How do these structural patterns compare to known coordination detection methods?** What does this approach detect that content-based methods miss?

5. **What are the limitations of structural-only detection?** When would structural anomalies produce false positives?

## Data Files

- `/tmp/ukr_networks.pkl` — NetworkX graph objects
- `/tmp/ukr_structural_metrics.csv` — Per-user metrics (99,085 rows)
