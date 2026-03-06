# Phase 4: Revert Network Analysis Results

## Executive Summary

Analysis of 965 revert actions across 100 Wikipedia articles reveals highly asymmetric editing conflicts where a small number of established editors systematically revert contributions from a much larger pool of participants. Combined with talk page analysis, we find evidence of **structural epistemic injustice** in Wikipedia's coverage of Middle East conflicts.

---

## 1. Network Structure

### 1.1 Basic Metrics

| Metric | Iran Cluster | Gaza Cluster |
|--------|-------------|--------------|
| Total reverts | 575 | 390 |
| Unique editors | 727 | 464 |
| Network density | 0.001 | 0.002 |
| Top 5 reverters share | 18.1% | 19.7% |

### 1.2 Role Distribution

| Role | Iran | Gaza |
|------|------|------|
| **Pure reverters** (never reverted) | 41.4% | 42.7% |
| **Pure reverted** (never revert) | 58.3% | 57.3% |
| **Bidirectional** (both) | 0.3% | 0.0% |

**Key Finding:** Revert conflicts are almost entirely one-directional. A minority of editors (41-43%) do all the reverting, while the majority (57-58%) only get reverted. This structural asymmetry suggests power concentration.

### 1.3 Power Concentration

**Iran Cluster Top Reverters:**
1. Mandruss: 31 reverts, 0 reverted (+31 net)
2. Space4Time3Continuum2x: 30 reverts, 0 reverted (+30 net)
3. Pahlevun: 16 reverts, 0 reverted (+16 net)

**Gaza Cluster Top Reverters:**
1. Raskolnikov.Rev: 21 reverts, 0 reverted (+21 net)
2. Abo Yemen: 19 reverts, 0 reverted (+19 net)
3. Nableezy: 17 reverts, 0 reverted (+17 net)

**Interpretation:** Top reverters are NEVER reverted themselves, suggesting they occupy protected positions in the editing hierarchy (likely Extended Confirmed status, admin-like authority, or established consensus-holders).

---

## 2. Cross-Cluster Analysis

### 2.1 Shared Actors

**122 editors** appear in both Iran and Gaza article clusters.

Notable cross-cluster actors:
- **Pachu Kannan**: 8 reverts (Iran), 11 reverts (Gaza)
- **DuncanHill**: 2 reverts (Iran), 6 reverts (Gaza)
- **Abo Yemen**: 12 reverts (Iran), 19 reverts (Gaza)

**Implication:** Some editors systematically patrol multiple Middle East conflict articles, suggesting organized watchlisting or topical specialization.

### 2.2 Specialist vs. Generalist Patterns

| Pattern | Example | Articles | Interpretation |
|---------|---------|----------|----------------|
| Specialist | Mandruss | 1 article | Focused gatekeeper |
| Generalist | Pahlevun | 8 articles | Topical patroller |
| Cross-cluster | Abo Yemen | Both clusters | Regional specialist |

---

## 3. Linking Networks to Epistemic Injustice

### 3.1 Talk Page Coding Results (v2.0)

| Construct | Cases | Example |
|-----------|-------|---------|
| naming_dispute | 5 | "Why is this called 'Twelve-Day War'?" |
| testimonial_injustice | 3 | "hasbara" accusation; "your narrative" dismissal |
| epistemic_dispossession | 2 | "You may not participate until EC status" |
| source_hierarchy | 2 | Iran International dismissed as unreliable |
| policy_weaponization | 1 | WP:NPOV cited without engagement |
| hermeneutical_injustice | 0 | (None detected) |

### 3.2 Correlation Patterns

| Network Pattern | EI Manifestation |
|-----------------|------------------|
| Pure reverters (41%) | Hold power to define content |
| Pure reverted (58%) | Subject to gatekeeping |
| EC-only discussions | Explicit exclusion (iran_087) |
| Naming debates | Terminology control (5 cases) |
| Source disputes | Geopolitical source hierarchies |

### 3.3 Key Cases

**iran_087** (epistemic_dispossession):
> "This discussion format is not available to non-EC editors"

- Editor attempting to add UN genocide finding
- Explicitly excluded based on edit count
- Network position: "pure reverted" (no reverting power)

**iran_113** (testimonial_injustice + naming_dispute):
> "Whoever came up with that should be banned"

- Dispute over "Twelve-Day War" naming
- Personal attack dismissing naming decision
- Reflects power struggle over framing

---

## 4. Theoretical Implications

### 4.1 Structural Epistemic Injustice

The network analysis reveals that Wikipedia's editing structure creates **systematic asymmetries** that map onto Fricker's (2007) epistemic injustice framework:

1. **Testimonial Injustice**: Editors dismissed based on account age, not argument quality
2. **Epistemic Dispossession**: EC protection excludes newcomers from contentious topics
3. **Source Hierarchy**: Geopolitical origins of sources used to dismiss content

### 4.2 Platform Affordances

Wikipedia's design features contribute to injustice:
- **Edit protection** creates in-group/out-group dynamics
- **Revert tools** privilege defenders of status quo
- **Policy acronyms** (WP:RS, WP:NPOV) weaponizable

### 4.3 The "Pure Reverter" Class

The 41-43% of editors who revert but are never reverted constitute a de facto **editorial elite**. Their position is structurally protected:
- Cannot be challenged through the same mechanisms they use
- Accumulate EC status that reinforces position
- Control talk page discourse through participation thresholds

---

## 5. Limitations

1. **Snapshot data**: 72-hour windows may miss longer-term patterns
2. **Parsing artifacts**: "Contributions/X" vs "X" creates duplicate nodes
3. **Attribution gaps**: Cannot link all talk page editors to revert network
4. **Selection bias**: High-conflict articles over-sampled by design

---

## 6. Files

- `analysis/iran_cluster/network_analysis.json`
- `analysis/gaza_cluster/network_analysis.json`
- `coding/v2/` - All v2.0 coded excerpts
- `analysis/PHASE4_RESULTS.md` - This document

---

## 7. Next Steps

1. **Preprint drafting**: Synthesize findings into "Whose History?" paper
2. **Visualization**: Network graphs showing power asymmetries
3. **Temporal analysis**: How do revert patterns change during conflict escalation?
4. **Editor interviews**: Qualitative validation with Wikipedia editors
