# Phase 4: Revert Network Analysis

## Overview

Analyzing Wikipedia editing conflicts through revert networks to understand epistemic contestation patterns.

## Data Summary

| Metric | Iran Cluster | Gaza Cluster |
|--------|-------------|--------------|
| Revert edges | 506 | 330 |
| Unique editors | 3,157 | 1,909 |
| Top reverter | Mandruss (31) | Raskolnikov.Rev (21) |
| Density | Low (sparse) | Low (sparse) |

## Top Reverters

### Iran Cluster
| Editor | Reverts | Ratio | Articles |
|--------|---------|-------|----------|
| Mandruss | 31 | 35% | 1 |
| Space4Time3Continuum2x | 30 | 26% | 1 |
| Pahlevun | 16 | 11% | 8 |
| Materialscientist | 15 | 94% | 11 |
| Abo Yemen | 12 | 16% | 5 |

### Gaza Cluster
| Editor | Reverts | Ratio | Articles |
|--------|---------|-------|----------|
| Raskolnikov.Rev | 21 | 26% | 7 |
| Abo Yemen | 19 | 21% | 7 |
| Nableezy | 17 | 40% | 8 |
| Pachu Kannan | 11 | 3% | 15 |
| Cinaroot | 9 | 13% | 9 |

## Key Conflict Pairs

### Iran Cluster
1. Space4Time3Continuum2x ↔ (self-reverts?) - 22 mutual
2. 47.63.235.56 ↔ Pahlevun - 16 mutual
3. Pachu Kannan ↔ (self?) - 10 mutual

### Gaza Cluster
1. Pachu Kannan ↔ (self?) - 18 mutual
2. Alaexis ↔ Raskolnikov.Rev - 14 mutual
3. DuncanHill ↔ and - 12 mutual

## Observations

### 1. Specialist vs Generalist Reverters
- **Specialists** (single article): Mandruss, Space4Time3Continuum2x focus on one article
- **Generalists** (many articles): Pahlevun (8), Pachu Kannan (15-18) span topics

### 2. Revert Ratio Patterns
- **High ratio (>50%)**: Materialscientist (94%), Nableezy (40%), DuncanHill (55%)
  - Suggests admin/patroller role or intense conflict
- **Low ratio (<10%)**: Pachu Kannan (3%), Evaporation123 (2%)
  - Active editors who occasionally revert

### 3. Cross-Cluster Actors
These editors appear in BOTH clusters:
- **Abo Yemen**: 12 reverts (Iran), 19 reverts (Gaza)
- **Pachu Kannan**: Conflict in both clusters
- **Space4Time3Continuum2x**: Active in both
- **Materialscientist**: Admin-like behavior in both

### 4. Network Structure
- Sparse networks (most editors don't interact)
- Power-law distribution: few editors do most reverting
- Hub-and-spoke: key editors at center of conflicts

## Linking to Epistemic Injustice

| Pattern | Network Signal | EI Construct |
|---------|---------------|--------------|
| EC editors reverting IPs | High asymmetry | epistemic_dispossession |
| Repeated pair conflicts | Mutual reverts | policy_weaponization |
| Single-article specialists | Low article count | naming_dispute |
| Cross-cluster actors | Appear in both | potential coordination |

## Next Steps

1. Build actual network graph for visualization
2. Calculate centrality measures (betweenness, degree)
3. Community detection (Louvain)
4. Correlate top reverters with talk page coding results
