# Overnight Study: Novel RQ Generation

**Date:** 2026-03-04  
**Status:** In Progress  
**Deliverable:** Full study package by morning

---

## Phase 1: Zotero Library Analysis

### Research Interests Identified

| Theme | Evidence (titles) | Count |
|-------|-------------------|-------|
| Agentic AI | "AI Agents and Academia", "Agentic AI and Social Science" | 15 |
| AI in research | "AI is turning research into monoculture", "Sycophancy in LLMs" | 33 |
| Coordination detection | "Amplifying the regime", "It takes a village to manipulate" | 2+ |
| Network analysis | "Building a Network Theory of Social Capital" | 6 |
| Social movements | "Opinion leadership in leaderless movement" | 2+ |
| Public sphere | "Networked publics", "AI in Public Sphere" | 6+ |
| Attention economy | "Agentic Attention Economy" | 1+ |

### Gap Identified

Wayne's library is heavy on:
- AI/LLM methodology
- Coordination/manipulation detection  
- Network theory

But **most AgentAcademy studies have been frame analysis**. This creates a gap:
- Network-based approaches under-explored
- Coordination detection not applied to the datasets
- Emotional/affective dimensions under-studied

---

## Phase 2: Method Selection with Justification

### Candidate Methods (Not Frame Analysis)

| Method | Feasibility | Theoretical Fit | Novelty | Choice |
|--------|-------------|-----------------|---------|--------|
| **Hashtag Network Analysis** | ✅ High | Social capital, coordination | ✅ Novel | **SELECTED** |
| Emotion/Sentiment Analysis | ✅ High | Affective intelligence | Medium | Backup |
| Linguistic Complexity | ✅ High | ELM, cognitive load | Medium | - |
| Time-Series Clustering | ⚠️ Need timestamps | Coordination | High | - |
| Account Network | ❌ No @ network data | Influence | - | Not feasible |

### Why Hashtag Network Analysis?

**Alignment with Wayne's research:**
1. "Amplifying the regime: identifying coordinated activity" → coordination detection via network patterns
2. "Building a Network Theory of Social Capital" → network theory
3. "Opinion leadership in a leaderless movement" → centrality = influence

**Why NOT frame analysis:**
- Already done extensively
- Doesn't address structural/network questions
- Misses coordination detection angle

**Why NOT sentiment analysis:**
- Common approach, less novel
- Doesn't leverage Wayne's network expertise

**Theoretical grounding:**
- **Bridging vs bonding social capital** (Putnam, 2000; Burt, 2004)
- **Hashtag publics** (Bruns & Burgess, 2015)
- **Connective action** (Bennett & Segerberg, 2012)

---

## Phase 3: Research Questions & Hypotheses

### RQ1: Network Structure
**How do hashtag co-occurrence networks differ structurally between war discourse and protest discourse?**

**H1a:** Protest discourse will show higher network density (more hashtag co-occurrence) than war discourse, reflecting coalition-building needs.

**H1b:** War discourse will show higher modularity (distinct clusters) than protest discourse, reflecting specialized information streams (military, diplomatic, humanitarian).

### RQ2: Bridging Hashtags
**Which hashtags serve as bridges connecting otherwise separate discourse communities?**

**H2:** In protest contexts, identity hashtags (#MahsaAmini) will have higher betweenness centrality than tactical hashtags (#OpIran), reflecting their role in unifying diverse grievances.

### RQ3: Network Position and Engagement
**Does a post's position in the hashtag network predict its engagement?**

**H3:** Posts using high-betweenness hashtags (bridges) will receive higher engagement than posts using peripheral hashtags, because they reach multiple communities.

---

## Phase 4: Methodology

### 4.1 Data Sampling

**Ukraine corpus:** Draw NEW sample (not previously coded)
- Source: `/root/.openclaw/workspace/projects/virality-study-2026/ukraine_june22_regression_data.json`
- Sample: 200 posts not in previous analysis

**MahsaAmini corpus:** Draw NEW sample
- Source: `/root/.openclaw/workspace/projects/virality-study-2026/coding_batch_*.json`
- Sample: 200 posts not in previous analysis

### 4.2 Hashtag Extraction

For each post:
1. Extract all hashtags using regex: `#\w+`
2. Normalize to lowercase
3. Create co-occurrence edges (hashtags appearing in same post)

### 4.3 Network Construction

**Nodes:** Unique hashtags  
**Edges:** Weighted by co-occurrence frequency  
**Separate networks:** One for Ukraine, one for MahsaAmini

### 4.4 Network Metrics

| Metric | Definition | Hypothesis |
|--------|------------|------------|
| Density | Proportion of possible edges present | H1a |
| Modularity | Degree of community structure | H1b |
| Betweenness centrality | Bridging position | H2 |
| Degree | Connection count | Descriptive |

### 4.5 Engagement Prediction (H3)

For each post:
1. Calculate average betweenness of hashtags used
2. Regress engagement on betweenness + controls
3. Controls: log_followers (if available), text_length, has_media

### 4.6 Multi-Model Validation

**Task for AI agents:**
- Claude: Network interpretation + hypothesis testing
- GLM: Independent replication
- Kimi: Cross-review and critique

---

## Phase 5: Execution Plan

1. [ ] Extract new samples (200 + 200)
2. [ ] Extract hashtags from all posts
3. [ ] Build co-occurrence networks
4. [ ] Calculate network metrics
5. [ ] Test H1a, H1b (structural differences)
6. [ ] Test H2 (bridging hashtags)
7. [ ] Test H3 (engagement prediction)
8. [ ] Multi-model interpretation
9. [ ] Adversarial review
10. [ ] Write up as theory paper

---

## Phase 6: Expected Contributions

### Theoretical
- Network perspective on digital crisis discourse
- Bridging vs bonding in crisis hashtag use
- Position-based attention in movement communication

### Methodological  
- Hashtag network analysis for cross-context comparison
- ACA applied to network (not just content) analysis

### Empirical
- First systematic comparison of hashtag networks in war vs protest
- Evidence on bridging hashtags and engagement

---

*Design complete. Beginning execution.*
