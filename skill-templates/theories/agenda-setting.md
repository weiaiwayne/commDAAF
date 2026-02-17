# Agenda-Setting Theory

## Core Concept

The media may not tell people *what* to think, but they tell people *what to think about* by emphasizing certain issues over others.

**First Level**: Issue salience (what topics)  
**Second Level**: Attribute salience (how topics are characterized)  
**Network Agenda Setting**: Relationships between issues

---

## Evolution of Agenda-Setting

| Era | Model | Focus |
|-----|-------|-------|
| **Classic** | McCombs & Shaw (1972) | Media → Public agenda |
| **Intermedia** | Vliegenthart & Walgrave (2008) | Media → Media agenda |
| **Network** | Guo & McCombs (2011) | Issue networks, attribute bundles |
| **Reversed** | Digital era | Public → Media agenda |

---

## Operationalizing Agenda-Setting

### Measuring Agendas

| Agenda | Data Source | Operationalization |
|--------|-------------|-------------------|
| **Media agenda** | News content | Topic frequency, prominence |
| **Public agenda** | Social media, surveys | Discussion volume, trends |
| **Policy agenda** | Government records | Legislative attention |

### Key Metrics

- **Salience**: Frequency / prominence of issue
- **Rank correlation**: Agreement between agendas
- **Time lag**: How long for transfer
- **Attribute association**: Which attributes bundled with issues

---

## Method-Theory Mapping

| Method | Agenda-Setting Application |
|--------|---------------------------|
| **Topic modeling** | Identify issues on agenda |
| **Time series** | Track salience over time |
| **Granger causality** | Test agenda transfer direction |
| **Network analysis** | Map issue relationships (NAS) |
| **Frame analysis** | Second-level attribute salience |

---

## Key Questions for Your Research

1. **Whose agenda are you measuring?**
   - Media (which outlets?)
   - Public (which platforms? which users?)
   - Elite (politicians, experts?)

2. **What's the time frame?**
   - Issue cycles vary (days vs. months)
   - Lag between agendas

3. **What's the direction?**
   - Classic: Media → Public
   - Intermedia: Elite media → Other media
   - Reversed: Public → Media

4. **First or second level?**
   - Issues (first) or attributes (second)?

---

## Network Agenda-Setting (NAS)

Beyond single issues — how are issues *connected*?

```
Traditional:           Network:
Issue A → Salience    Issue A ←→ Issue B
Issue B → Salience         ↘   ↗
Issue C → Salience    Issue C ←→ Issue D
```

**Method**: Build issue co-occurrence networks from media and public, compare structure.

---

## Common Mistakes

| Mistake | Why It's Wrong | Better Approach |
|---------|----------------|-----------------|
| Correlation = causation | Co-movement ≠ influence | Use Granger causality, lag analysis |
| Ignoring time lag | Agenda transfer takes time | Test multiple lag windows |
| Single platform | Platforms have different agendas | Multi-platform comparison |
| Ignoring algorithms | Trending topics are curated | Account for platform curation |

---

## Key Citations

- McCombs & Shaw (1972). The agenda-setting function of mass media
- Vliegenthart & Walgrave (2008). When the media matter for politics
- Guo & McCombs (2011). Network agenda setting
- Vargo et al. (2014). Network issue agendas on Twitter
- Harder et al. (2017). Toward a cyclical model of agenda-setting

---

## Integration with CommDAAF

When studying agenda-setting:

1. **Data**: Parallel media + public data over time
2. **Method**: Topic modeling + time series + causality tests
3. **Validation**: Test direction with lag analysis
4. **Interpretation**: Correlation ≠ causation; control for confounds

---

*Theory Module | CommDAAF v0.3*
