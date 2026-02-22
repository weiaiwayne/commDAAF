# Nigeria Christian-Fulani Conflict: Enhanced Research Design

**Version 2.0** — Expanded theoretical framework and larger dataset

---

## Theoretical Framework

### Primary Theory: Framing (Entman 1993)

Frames perform four functions in news coverage:
1. **Problem Definition** — What is the issue?
2. **Causal Attribution** — Who/what caused it?
3. **Moral Evaluation** — What values are at stake?
4. **Treatment Recommendation** — What should be done?

### Secondary Theory: Second-Level Agenda Setting

Beyond issue salience, media shape *how* issues are characterized through attribute emphasis.

### Conflict Framing Literature

Drawing on:
- Semetko & Valkenburg (2000) — Generic news frames
- Entman (2004) — Cascading activation in conflict
- Baden (2018) — Frame packages and co-occurrence

---

## Research Questions (Expanded)

### RQ1: Problem Definition Frames
**How is the conflict defined across source types?**
- Religious persecution vs. land conflict vs. ethnic violence vs. state failure
- Does problem definition vary by source geography?

### RQ2: Causal Attribution
**Who/what is blamed for the conflict?**
- Fulani herders (individual actors)
- Islamic extremism (religious ideology)
- Government failure (state responsibility)
- Climate/resource scarcity (structural factors)
- Historical ethnic tensions

### RQ3: Actor Portrayal
**How are the primary actors characterized?**
- Christians: Victims, defenders, community members, or political actors?
- Fulani: Attackers, herders, ethnic group, Muslims, or complex actors?
- Government: Absent, complicit, ineffective, or responsive?

### RQ4: Solution Framing
**What remedies are proposed or implied?**
- Military intervention
- Religious freedom legislation
- Land reform / resource management
- Reconciliation / dialogue
- International intervention
- No solution mentioned

### RQ5: Frame Co-occurrence
**Which frames cluster together?**
- Does religious framing co-occur with violence but not solutions?
- Does economic framing co-occur with structural solutions?

### RQ6: Source Ideology Effects
**How does source political orientation affect framing?**
- Conservative vs. mainstream vs. progressive outlets
- Religious vs. secular outlets
- US vs. UK vs. Nigerian sources

### RQ7: Temporal Dynamics
**How does framing change around violent incidents?**
- Immediate aftermath vs. one week later vs. ongoing coverage
- Breaking news vs. analytical pieces

---

## Hypotheses

### H1: Differential Problem Definition
**US conservative media defines the problem as "Christian persecution" at higher rates than Nigerian or wire service sources.**

*Rationale:* Conservative US outlets serve audiences primed for persecution narratives and have ideological investment in religious freedom framing.

### H2: Attribution Asymmetry
**Fulani actors receive individual blame while structural causes (climate, land policy) are rarely mentioned.**

*Rationale:* News values favor identifiable agents over abstract forces; religious/ethnic conflict narratives are more compelling than climate stories.

### H3: Victim Hierarchy
**Christians are portrayed as victims significantly more often than Fulani, even when Fulani communities also suffer violence.**

*Rationale:* Western media's audience identification with Christian victims; less coverage of herder-on-herder violence or state violence against Fulani.

### H4: Solution Gap
**Religious framing correlates with *absence* of solution framing, while economic/structural framing correlates with policy solutions.**

*Rationale:* Religious persecution frame implies intractable civilizational conflict; economic frames suggest tractable policy interventions.

### H5: Source Geography Effect
**Nigerian sources show more diverse actor portrayal and higher structural attribution than international sources.**

*Rationale:* Local journalists have greater context, multiple stakeholder access, and less reliance on persecution narrative tropes.

### H6: Moral Evaluation Clustering
**Morality frame (good/evil language) clusters with religious framing but not with economic framing.**

*Rationale:* Religious conflict narratives invite moral judgment; resource competition frames are more neutral.

### H7: Intermedia Divergence
**Wire services (AP, Reuters, AFP) show significantly different framing patterns than ideological outlets.**

*Rationale:* Wire services aim for neutrality and serve diverse clients; ideological outlets frame for their audiences.

---

## Frame Operationalization (Expanded)

### Problem Definition Frames

| Frame | Definition | Indicators |
|-------|------------|------------|
| **Religious Persecution** | Conflict framed as targeting Christians for faith | persecution, anti-Christian, religious violence, faith, church attacks |
| **Ethnic Conflict** | Conflict framed as inter-ethnic | Fulani vs Berom, tribal, ethnic violence, indigenous |
| **Resource Competition** | Conflict framed as land/water disputes | land, grazing, cattle, farms, water, resources, climate |
| **State Failure** | Conflict framed as government inadequacy | government failure, military, security forces, impunity |
| **Criminal Violence** | Conflict framed as banditry/crime | bandits, kidnappers, criminal, gangs |

### Causal Attribution

| Attribution | Definition | Indicators |
|-------------|------------|------------|
| **Fulani Agency** | Fulani as intentional aggressors | Fulani attacked, herdsmen killed, militants |
| **Islamic Ideology** | Religion as motivator | jihad, Islamic extremism, Islamist, religious cleansing |
| **Climate/Environment** | Environmental factors | desertification, drought, climate change, migration |
| **Government Failure** | State as enabling factor | impunity, failure to protect, absent military |
| **Historical Tensions** | Long-standing ethnic issues | decades-old, historical, ancestral |

### Actor Portrayal

| Actor | Portrayal | Indicators |
|-------|-----------|------------|
| **Christians as Victims** | Passive suffering | killed, massacred, targeted, fled, displaced |
| **Christians as Resisters** | Active defense | defending, protecting, vigilante, fighting back |
| **Fulani as Aggressors** | Active violence | attacked, invaded, killed, burned |
| **Fulani as Community** | Ethnic/economic group | herders, pastoralists, community, nomads |
| **Government as Absent** | Not mentioned or inactive | (absence of government action) |
| **Government as Actor** | Active response | deployed, arrested, condemned, intervened |

### Solution Framing

| Solution | Definition | Indicators |
|----------|------------|------------|
| **Military** | Force-based response | troops, military, security, deployment, strike |
| **Legislative** | Policy/law changes | bill, law, act, legislation, congress |
| **Dialogue** | Reconciliation approach | peace, dialogue, reconciliation, mediation |
| **International** | External intervention | UN, US, international community, sanctions |
| **Structural** | Address root causes | land reform, climate adaptation, grazing routes |
| **None** | No solution mentioned | (absence of remedy language) |

---

## Data Collection Plan (Expanded)

### Target: 1,000+ articles

### GDELT Queries (Expanded)

```python
GDELT_QUERIES = [
    # Core conflict terms
    'Nigeria (Fulani OR herdsmen) (Christian OR church OR attack)',
    'Nigeria (farmer OR herder) conflict',
    'Plateau Nigeria violence',
    'Benue Nigeria (attack OR killing)',
    'Nigeria (Christian OR Christians) persecution',
    
    # Solution-focused
    'Nigeria Fulani (peace OR dialogue OR reconciliation)',
    'Nigeria (military OR troops) Fulani',
    'Nigeria government (Fulani OR herdsmen)',
    
    # Source-specific
    'Nigeria Fulani sourcecountry:NG',
    'Nigeria Fulani domain:reuters.com OR domain:apnews.com',
    'Nigeria Fulani domain:bbc.com OR domain:aljazeera.com',
    
    # Structural framing
    'Nigeria (herder OR farmer) (land OR grazing OR climate)',
]
```

### MediaCloud Collections

| Collection | ID | Description |
|------------|----|----|
| US National | 34412234 | Major US news sources |
| UK National | 34412476 | UK sources |
| Center for Media Engagement | 200363048 | US digital native |
| Nigeria (if available) | TBD | Nigerian sources |

### Source Classification

```python
SOURCE_CATEGORIES = {
    'conservative_us': ['breitbart.com', 'foxnews.com', 'dailycaller.com', 'dailysignal.com', 'townhall.com'],
    'mainstream_us': ['nytimes.com', 'washingtonpost.com', 'cnn.com', 'nbcnews.com', 'abcnews.go.com'],
    'christian_media': ['christianpost.com', 'christiandaily.com', 'ncregister.com', 'catholicnewsagency.com'],
    'wire_services': ['reuters.com', 'apnews.com', 'afp.com'],
    'uk_media': ['bbc.com', 'theguardian.com', 'telegraph.co.uk'],
    'nigerian_media': ['punchng.com', 'premiumtimesng.com', 'dailypost.ng', 'saharareporters.com', 'thecable.ng'],
    'pan_african': ['allafrica.com', 'africanews.com']
}
```

---

## Analysis Plan

### Phase 1: Expanded Data Collection
- Run all GDELT queries with rate limiting
- Collect all MediaCloud collections
- Deduplicate across sources
- Target: 1,000+ unique articles

### Phase 2: LLM-Assisted Frame Coding
- Use Claude to code each article for:
  - Problem definition frame
  - Causal attribution
  - Actor portrayal
  - Solution framing
  - Overall tone
- Validate with human coding sample (100 articles)

### Phase 3: Quantitative Analysis
- Frame prevalence by source type
- Chi-square tests for frame × source associations
- Co-occurrence analysis (which frames cluster?)
- Temporal analysis if date range permits

### Phase 4: Hypothesis Testing
- Statistical tests for each H1-H7
- Effect size reporting
- Confidence intervals

---

## Validation Protocol

1. **Codebook Development:** Define each frame with examples
2. **LLM Prompt Engineering:** Create consistent coding prompts
3. **Human Validation Sample:** 100 articles coded by human
4. **Agreement Calculation:** Compare LLM vs human codes
5. **Refinement:** Adjust prompts if κ < 0.70
6. **Full Coding:** Apply to entire corpus

---

## Expected Deliverables

1. **Dataset:** 1,000+ coded articles (CSV)
2. **Codebook:** Frame definitions and coding rules
3. **Analysis Report:** Full hypothesis testing results
4. **Visualization:** Frame prevalence charts, source comparisons
5. **Discussion:** Implications for conflict coverage

---

*Research Design v2.0 — CommDAAF Framework*
