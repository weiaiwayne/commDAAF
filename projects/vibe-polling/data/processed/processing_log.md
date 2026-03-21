# Data Processing Log — VibePoll-2026

**Framework:** CommDAAF v1.0
**Generated:** 2026-03-20T00:37:16.796146

---

## Processing Statistics

| Metric | Value |
|--------|-------|
| Raw records | 98371 |
| States | 13 |
| Terms | 95 |
| Categories | 9 |
| Date range | (Timestamp('2025-12-19 00:00:00'), Timestamp('2026-03-19 00:00:00')) |
| Missing values handled | 0 |
| Salience records | 1183 |

---

## Methodological Decisions

Per CommDAAF transparency requirement, all processing decisions are documented below:

### Load Data

**Decision:** Loaded 98371 records

**Rationale:** Raw parquet file from Google Trends collection

**Impact:** States: 13, Terms: 95

---

### Filter Low Signal

**Decision:** Removed 58 terms with >50% zeros

**Rationale:** Per reviewer critique: terms with 80-99% zeros have no signal

**Impact:** Removed: ['DACA', 'Epstein documents', 'Epstein list', 'Epstein names', 'Iran attack', 'Iran news today', 'Milwaukee crime', 'Philadelphia crime', 'Phoenix traffic', 'SNAP benefits']...

---

### Missing Values

**Decision:** No missing values found

**Rationale:** Data is complete from collection

**Impact:** No imputation needed

---

### Normalization

**Decision:** Applied temporal z-score (within term, across time)

**Rationale:** Normalizes each term relative to its own history

**Impact:** Enables comparison of term trends regardless of baseline volume

---

### Normalization

**Decision:** Applied cross-term z-score (within state-date, across terms)

**Rationale:** Normalizes terms relative to other terms on same day

**Impact:** Shows which terms are unusually high/low for that state-day

---

### Normalization

**Decision:** Created combined z-score (average of temporal and cross-term)

**Rationale:** Balanced measure capturing both temporal and relative salience

**Impact:** Primary metric for Vibe Index calculation

---

### Population Normalization

**Decision:** Applied per-capita normalization (interest per million residents)

**Rationale:** Controls for state population differences (CA 39M vs NH 1.4M)

**Impact:** Addresses reviewer critique: raw CA searches 3.4x higher than NH

---

### Population Normalization

**Decision:** Created z_per_capita (z-score of per-capita interest)

**Rationale:** Enables population-controlled comparisons across states

**Impact:** Per reviewer: this should eliminate Battleground Paradox artifact

---

### National Baseline

**Decision:** Calculated population-weighted national average as baseline

**Rationale:** R2 revision: Ohio is no longer swing state (Trump +11 in 2024), use national avg instead

**Impact:** interest_vs_national shows state deviation from population-weighted national trend

---

### Issue Salience

**Decision:** Calculated issue salience per state-date-category

**Rationale:** Mean of combined z-scores for all terms in category

**Impact:** Categories: ['economy', 'immigration', 'political', 'iran_war', 'ai_jobs', 'epstein']

---

### Vibe Index

**Decision:** Calculated weighted Vibe Index

**Rationale:** Weights: {'economy': 0.35, 'immigration': 0.2, 'political': 0.15, 'iran_war': 0.15, 'ai_jobs': 0.1, 'epstein': 0.05}

**Impact:** Single composite metric per state-date

---

### Vibe Index

**Decision:** Added 7-day rolling average

**Rationale:** Smooths daily fluctuations for trend analysis

**Impact:** Useful for correlation with weekly polling data

---


## Output Files

1. `trends_normalized.parquet` - Full normalized dataset with z-scores
2. `issue_salience.csv` - Issue salience per state-date-category
3. `vibe_indices.csv` - Weighted Vibe Index per state-date

---

## Issue Weights (from PLAN.md)

| Category | Weight | Rationale |
|----------|--------|-----------|
| economy | 0.35 | Top voter concern (cost of living 52%) |
| immigration | 0.20 | Highly polarizing, active enforcement |
| political | 0.15 | Electoral engagement indicators |
| iran_war | 0.15 | Active conflict, approval impact |
| ai_jobs | 0.10 | Growing but not yet top concern |
| epstein | 0.05 | Episodic, scandal interest |

---

*Log generated following CommDAAF v1.0 transparency protocol*
