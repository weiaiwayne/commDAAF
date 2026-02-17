# Information Diffusion Theory

## Core Concept

How information, ideas, and behaviors spread through social networks. Understanding diffusion patterns reveals influence structures and information dynamics.

---

## Key Models

### Cascade Models

| Model | Mechanism | Application |
|-------|-----------|-------------|
| **Independent Cascade** | Probabilistic activation | Viral content spread |
| **Linear Threshold** | Cumulative social pressure | Behavior adoption |
| **Epidemiological (SIR)** | Infection/recovery | Misinformation spread |

### Diffusion Patterns (Goel et al., 2016)

| Pattern | Structure | Example |
|---------|-----------|---------|
| **Broadcast** | Star (one-to-many) | Celebrity tweet |
| **Viral** | Deep chains | True viral spread |
| **Structural** | Multiple hubs | News diffusion |

**Key finding**: True viral cascades are rare; most spread is broadcast.

---

## Operationalizing Diffusion

### Measuring Spread

| Metric | Definition | What It Captures |
|--------|------------|------------------|
| **Cascade size** | Total adopters | Reach |
| **Cascade depth** | Longest chain | Viral potential |
| **Cascade breadth** | Max nodes at any level | Broadcast vs. viral |
| **Structural virality** | Wiener index | Overall structure |

### Identifying Influence

| Approach | Method | Limitation |
|----------|--------|------------|
| **Centrality** | Network position | Position ≠ causation |
| **Temporal** | Who posted first | Correlation issue |
| **Causal** | Randomized experiments | Rarely feasible |
| **Granger** | Time series causality | Observational only |

---

## Echoing vs. Sharing (Narrative Diffusion)

### Key Distinction

| Echoing | Sharing |
|---------|---------|
| Same message, different words | Same content, forwarded |
| Semantic similarity | Explicit retweet/share |
| Harder to detect | Easy to detect |
| May indicate deeper adoption | May be performative |

### Detection Methods

- **Retweet/share networks**: Explicit forwarding
- **Semantic similarity**: Echoing without attribution
- **Temporal embedding similarity**: LTTN-style approaches

---

## Method-Theory Mapping

| Method | Diffusion Application |
|--------|----------------------|
| **Cascade reconstruction** | Map spread structure |
| **Network analysis** | Identify influential positions |
| **Time series** | Temporal dynamics |
| **Semantic similarity** | Detect echoing |
| **Topic modeling** | Track idea spread |

---

## Key Questions for Your Research

1. **What's diffusing?**
   - Specific content (URL, image)
   - Ideas/frames (semantic)
   - Behaviors (adoption)

2. **What's the mechanism?**
   - Social influence (peer pressure)
   - Information exposure (awareness)
   - Algorithmic amplification (platform)

3. **What's the structure?**
   - Broadcast (hub-driven)
   - Viral (peer-to-peer chains)
   - Mixed

4. **Can you establish causation?**
   - Temporal precedence helps but doesn't prove
   - Confounds (shared exposure to external event)

---

## Common Mistakes

| Mistake | Why It's Wrong | Better Approach |
|---------|----------------|-----------------|
| Correlation = influence | Shared exposure confounds | Control for external events |
| Retweet = adoption | May be performative | Distinguish sharing from believing |
| Ignoring platform | Algorithms shape spread | Account for algorithmic curation |
| Assuming linearity | Diffusion is complex | Model nonlinear dynamics |

---

## Virality Myths

1. **"Content goes viral"** → Most spread is broadcast, not viral
2. **"Influencers cause virality"** → Structural virality is rare even from influencers
3. **"Quality spreads"** → Platform algorithms dominate content factors

---

## Key Citations

- Rogers (1962). Diffusion of Innovations
- Watts & Dodds (2007). Influentials, networks, and public opinion formation
- Bakshy et al. (2011). Everyone's an influencer
- Goel et al. (2016). The structural virality of online diffusion
- Vosoughi et al. (2018). The spread of true and false news online

---

## Integration with CommDAAF

When studying diffusion:

1. **Data**: Timestamped content with sharing/interaction data
2. **Method**: Cascade reconstruction + network analysis
3. **Validation**: Control for external events, platform effects
4. **Interpretation**: Distinguish correlation from causation; broadcast from viral

---

*Theory Module | CommDAAF v0.3*
