# Iran Intermedia Agenda-Setting Study

**AgentAcademy Test Study** — CommDAAF Framework Validation

---

## Theoretical Framework

### Primary Theory: Intermedia Agenda-Setting (Reese & Danielian, 1989)

Elite media (wire services, prestige press) set the agenda for other outlets through:
1. **First-level**: Issue salience transfer
2. **Second-level**: Attribute/frame transfer

### Research Questions

- RQ1: How do frames differ across source tiers (wire vs national vs regional)?
- RQ2: Do wire service frames propagate to national outlets?
- RQ3: How does source geography affect Iran coverage framing?

---

## Hypotheses

| ID | Hypothesis | Operationalization |
|----|------------|-------------------|
| H1 | Wire services show more neutral framing | Lower conflict frame %, higher "both sides" language |
| H2 | US sources emphasize "Iranian threat" | Higher threat/danger language, nuclear focus |
| H3 | Israeli sources show highest conflict framing | Military action emphasis, security frame |
| H4 | Al Jazeera shows more regional context | Palestinian linkage, broader Middle East framing |

---

## Frame Operationalization (Entman 1993)

### Problem Definition Frames
| Frame | Indicators |
|-------|------------|
| **Nuclear Threat** | nuclear, enrichment, weapons, IAEA, uranium |
| **Regional Conflict** | proxy, Hezbollah, Hamas, Israel, attack, strike |
| **Diplomatic** | talks, negotiations, JCPOA, sanctions, diplomacy |
| **Human Rights** | protests, crackdown, dissidents, women, repression |
| **Terrorism/Threat** | terrorist, threat, danger, attack, militia |

### Causal Attribution
| Attribution | Indicators |
|-------------|------------|
| **Iran as aggressor** | Iran attacked, Tehran ordered, regime-backed |
| **Israel as aggressor** | Israel struck, IDF attacked, assassination |
| **US policy** | sanctions, Biden/Trump policy, pressure |
| **Regional dynamics** | proxy war, Axis of Resistance, regional tensions |

### Moral Evaluation
| Evaluation | Indicators |
|------------|------------|
| **Iran negative** | regime, mullahs, theocracy, authoritarian |
| **Iran neutral** | government, officials, Tehran |
| **Balanced** | both sides, tensions, conflict |

---

## Data Collection Plan

### GDELT DOC API Queries
```
Iran nuclear (IAEA OR enrichment OR weapons)
Iran Israel (attack OR strike OR conflict)
Iran (Hezbollah OR Hamas OR proxy)
Iran sanctions (US OR Biden OR Trump)
```

### Source Categories
| Category | Domains |
|----------|---------|
| Wire Services | reuters.com, apnews.com, afp.com |
| US Mainstream | nytimes.com, washingtonpost.com, cnn.com |
| US Conservative | foxnews.com, breitbart.com |
| Israeli | haaretz.com, timesofisrael.com, jpost.com |
| Al Jazeera | aljazeera.com |
| UK | bbc.com, theguardian.com |

### Period: January 2024 – February 2026

---

## Multi-Model Validation Protocol

1. **Claude** (anthropic/claude-sonnet-4-20250514) — Primary analysis
2. **GLM** (zai/glm-4.7) — Chinese model validation
3. **Kimi** (kimi/k2.5) — Additional Chinese model

Each model independently:
- Codes sample headlines for frames
- Analyzes full-text sample
- Reports frame distributions
- Flags ambiguous cases

Convergence target: 2/3 models agree on dominant frame

---

*CommDAAF Framework v0.3 — AgentAcademy Test Study*
