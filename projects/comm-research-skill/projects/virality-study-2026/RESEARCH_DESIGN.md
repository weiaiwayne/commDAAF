# Online Virality in Crisis Discourse: A Multi-Model CommDAAF Test Study

**AgentAcademy Study** — Testing CommDAAF as Multi-Model Guardrail  
**Date:** 2026-02-27

---

## Literature Foundation

### From Zotero Library
- **Giglietto et al. (2020)**: Coordinated behavior amplifies message spread; network structure matters
- **Kuznetsova (2025)**: Pro-government channels use coordinated amplification in autocracies
- **Gruzd et al.**: Twitter as imagined community; network position affects reach

### From Virality Research
- **Brady et al. (2017)**: Moral-emotional language increases diffusion by 20% per word
- **PMC (2022)**: High arousal increases retweet probability; negative valence effects mixed
- **Hoang et al.**: Socio-political tweets spread differently than general content

### Key Insight
Virality = f(Content framing, Emotional arousal, Source credibility, Network position)

---

## Theoretical Framework

### Information Diffusion in Crisis Contexts
Drawing on:
1. **Framing Theory (Entman 1993)** — How problems are defined shapes engagement
2. **Emotional Contagion** — High-arousal emotions spread faster (Berger & Milkman 2012)
3. **Two-Step Flow** — Influentials amplify messages (Katz & Lazarsfeld, updated for social media)
4. **Networked Publics** — Platform affordances shape what spreads (boyd 2010)

### Context-Specific Considerations
| Dataset | Context | Expected Dynamics |
|---------|---------|-------------------|
| **#MahsaAmini** | Anti-regime protest under internet blackout | Solidarity, injustice frames; diaspora amplification |
| **Ukraine War** | 4 months into conflict, global attention | Conflict, humanitarian frames; verified sources advantage |

---

## Research Questions

### RQ1: Content Framing & Virality
**What content frames predict higher composite engagement across crisis contexts?**

### RQ2: Source Effects on Virality  
**How do source characteristics (followers, verification, account age) moderate content-virality relationships?**

### RQ3: Generalizability
**Do the same predictors of virality hold across protest discourse (#MahsaAmini) and war discourse (Ukraine)?**

---

## Hypotheses

### Content Hypotheses (Grounded in Literature)

| ID | Hypothesis | Basis |
|----|------------|-------|
| **H1a** | Posts with **INJUSTICE frames** receive higher engagement than neutral posts | Brady et al. 2017; moral content spreads |
| **H1b** | Posts with **SOLIDARITY frames** receive higher engagement | Protest mobilization literature |
| **H1c** | Posts with **CONFLICT frames** receive higher engagement than INFORMATIONAL | Semetko & Valkenburg; conflict = newsworthy |
| **H2** | Posts with **high emotional arousal** (anger, hope) outperform low-arousal posts | PMC 2022; arousal drives transmission |
| **H3** | Posts with **negative valence** have **mixed effects**: boost in protest, dampen in war | Context-dependent emotional dynamics |

### Source Hypotheses

| ID | Hypothesis | Basis |
|----|------------|-------|
| **H4** | **Follower count** positively predicts engagement (log-linear relationship) | Network reach; but diminishing returns |
| **H5** | **Verified accounts** receive higher engagement, controlling for followers | Credibility signal |
| **H6** | **Account age** positively predicts engagement (established > new) | Trust, non-bot signal |

### Generalizability Hypothesis

| ID | Hypothesis | Basis |
|----|------------|-------|
| **H7** | Frame effects on virality are **consistent across datasets** (protest vs war) | Testing universal vs context-specific drivers |

---

## Frame Typology (Deductive)

Using adapted Semetko & Valkenburg (2000) + protest-specific frames:

| Frame | Definition | Indicators |
|-------|------------|------------|
| **INJUSTICE** | Wrongdoing, victimization, rights violation | killed, murdered, victims, oppression, brutality |
| **SOLIDARITY** | Unity, collective action, support | together, united, support, stand with, we |
| **CONFLICT** | Clash between actors, violence, war | attack, fight, battle, war, versus, against |
| **HUMANITARIAN** | Human suffering, aid, refugees | civilians, refugees, humanitarian, suffering, children |
| **HOPE** | Positive future, change possible | freedom, future, change, victory, hope |
| **INFORMATIONAL** | Neutral reporting, facts | update, report, according to, officials say |
| **CALL_TO_ACTION** | Mobilization, demands | join, protest, demand, action, must |

### Emotional Dimensions (Coded separately)

| Dimension | Values |
|-----------|--------|
| **Valence** | Positive / Negative / Neutral |
| **Arousal** | High / Medium / Low |

---

## Dependent Variable: Composite Engagement

```
ENGAGEMENT = log(retweet_count + 1) + log(like_count + 1) + log(quote_count + 1)
```

Using log transformation to handle extreme skew (median RT=21, max=22,881 in MahsaAmini).

### Engagement Tiers for Stratified Sampling

| Tier | Definition | Purpose |
|------|------------|---------|
| **Viral** | Top 5% engagement | Identify what makes content spread |
| **Medium** | 25th-75th percentile | Typical engagement |
| **Low** | Bottom 25% | Baseline comparison |

---

## Sampling Strategy

### Requirements
1. **Stratified by engagement tier** — Equal representation of viral/medium/low
2. **Time-weighted** — Avoid event spike domination
3. **Sufficient N for regression** — Rule of thumb: 10-20 cases per predictor

### Sampling Protocol

**Per Dataset:**
1. Calculate composite engagement score
2. Identify engagement tier cutoffs (5%, 25%, 75%)
3. Divide time period into equal segments (e.g., daily)
4. Sample proportionally from each tier × time segment
5. Target: **300 posts per dataset** (100 per tier)
6. Total: **600 posts** for cross-dataset analysis

### Deduplication
- Remove retweets (analyze original content only)
- Remove duplicate text (same content, different users)
- Remove non-English/non-relevant posts

---

## Multi-Model Analysis Protocol

### Phase 1: Frame Coding (LLM-assisted)
Each model independently codes all 600 posts for:
- Primary frame (7 categories)
- Emotional valence (3 levels)
- Emotional arousal (3 levels)

### Phase 2: Quantitative Analysis
- Descriptive statistics by frame × dataset
- Regression: Engagement ~ Frame + Source_Controls + Dataset
- Interaction effects: Frame × Dataset

### Phase 3: Cross-Model Validation
- Compare frame coding agreement across models
- Report inter-model reliability (Krippendorff's α)
- Flag disagreements for review

### Models
| Model | Role |
|-------|------|
| **Claude** | Primary analyst |
| **GLM-4.7** | Independent validation |
| **Kimi K2.5** | Independent validation |

---

## CommDAAF Tier Declaration

**🟡 PILOT** — Committee presentation, working paper

### Validation Requirements (per CommDAAF v0.4)
- [ ] Human validation sample: N ≥ 100
- [ ] Inter-coder reliability: κ ≥ 0.6
- [ ] Subsample replication: 80%
- [ ] Alternative explanations paragraph

---

## Expected Outputs

1. **Frame distribution by dataset** — What frames dominate each crisis?
2. **Engagement predictors** — Which frames/sources drive virality?
3. **Cross-dataset comparison** — Universal vs context-specific effects
4. **CommDAAF gap identification** — What did the framework miss?
5. **Skill improvements** — New checks for virality analysis

---

## Timeline

| Phase | Duration | Tasks |
|-------|----------|-------|
| **Data Prep** | 30 min | Sample, clean, dedupe |
| **Frame Coding** | 2 hrs | 3-model independent coding |
| **Analysis** | 1 hr | Regression, comparison |
| **Synthesis** | 30 min | Cross-model validation, findings |

---

*CommDAAF v0.4 | AgentAcademy Test Study*
