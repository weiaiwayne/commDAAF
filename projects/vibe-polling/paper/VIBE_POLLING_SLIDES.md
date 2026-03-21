---
marp: true
theme: uncover
paginate: true
style: |
  :root {
    --color-background: #0f0f23;
    --color-foreground: #f0f0f0;
    --color-highlight: #00d4ff;
    --color-dimmed: #888;
  }
  section {
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
    color: #f0f0f0;
    font-family: 'Inter', 'SF Pro Display', -apple-system, sans-serif;
  }
  section.lead {
    background: linear-gradient(135deg, #1a1a3e 0%, #2d1b4e 50%, #0f0f23 100%);
  }
  section.invert {
    background: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
    color: #0f0f23;
  }
  h1 {
    color: #00d4ff;
    font-weight: 700;
    letter-spacing: -0.02em;
  }
  h2 {
    color: #c4b5fd;
    font-weight: 500;
  }
  h3 {
    color: #94a3b8;
    font-weight: 400;
  }
  strong {
    color: #00d4ff;
  }
  table {
    font-size: 0.85em;
    border-collapse: collapse;
    margin: 1em auto;
  }
  th {
    background: rgba(0, 212, 255, 0.15);
    color: #00d4ff;
    padding: 0.6em 1em;
    border-bottom: 2px solid #00d4ff;
  }
  td {
    padding: 0.5em 1em;
    border-bottom: 1px solid #333;
  }
  blockquote {
    border-left: 4px solid #7c3aed;
    padding-left: 1em;
    color: #c4b5fd;
    font-style: italic;
  }
  code {
    background: rgba(0, 212, 255, 0.1);
    color: #00d4ff;
    padding: 0.2em 0.5em;
    border-radius: 4px;
  }
  a {
    color: #00d4ff;
  }
  footer {
    color: #555;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Vibe Polling

## Can Google Trends Predict Public Opinion?

### A Multi-Agent Computational Analysis

<br>

**AgentAcademy Team**

---

# Research Context

## The "Vibe Polling" Proposition

- **2024 election:** Prediction markets outperformed traditional polls
- **Intuition:** Search behavior = real-time sentiment indicator
  - Anxious about inflation → search "gas prices"
  - Concerned about immigration → search "deportation"
- **Question:** Can we predict elections from Google Trends?

---

# Research Questions

> **RQ1 (Predictive):** Can Google Trends search behavior predict public opinion dynamics?

> **RQ2 (Descriptive):** What does search behavior reveal about issue salience across states?

> **RQ3 (Methodological):** What validity constraints affect Google Trends for measuring public opinion?

---

# Novel Methodology

## Multi-Agent Computational Framework

| Agent | Role |
|-------|------|
| **Claude Code** | Data collection & processing |
| **Kimi K2.5** | Statistical modeling |
| **Gemini** | Temporal analysis |
| **Codex** | Term validation |
| **Reviewer** | Cross-validation |

*Computational triangulation to reduce confirmation bias*

---

# Data Overview

## Collection Parameters

| Parameter | Value |
|-----------|-------|
| Period | Dec 2025 – Mar 2026 (91 days) |
| States | 13 (7 battleground, 3 control, 3 watch) |
| Records | 38,311 (filtered from 75,894) |
| Terms | 25 validated |
| Markets | Polymarket + Kalshi |

---

# States Analyzed

**Battleground Tier 1:** PA, MI, WI, AZ, GA

**Battleground Tier 2:** NV, NC

**Control:** CA (Safe D), TX (Safe R), OH (Lean R)

**Watch:** ME, NH, MN

---

# Search Term Categories

| Category | Weight | Example Terms |
|----------|--------|---------------|
| Economy | 35% | gas prices, 401k, inflation |
| Immigration | 20% | asylum, green card, ICE near me |
| Political | 15% | Trump approval, how to vote |
| Iran War | 15% | Iran news |
| AI/Jobs | 10% | ChatGPT, automation |
| Epstein | 5% | Epstein files |

---

<!-- _class: invert -->
<!-- _paginate: false -->

# Results
## RQ1: Predictive Validity

---

# Granger Causality: Complete Failure

## 0 of 14 States Significant

| Direction | States Tested | Significant |
|-----------|---------------|-------------|
| Trends → Markets | 14 | **0** |
| Markets → Trends | 14 | **0** |

<br>

### ❌ Google Trends does NOT predict opinion shifts

---

# The Spurious Correlation Trap

## Raw vs. First-Differenced

| State | Raw *r* | Differenced *r* | Drop |
|-------|---------|-----------------|------|
| California | .659 | −.131 | **79%** |
| National | .611 | −.069 | **68%** |
| Nevada | .657 | −.074 | **73%** |
| Pennsylvania | .493 | −.154 | **65%** |

**All correlations are spurious artifacts**

---

# Why Correlations Collapse

## Both Series Trending Upward

- Market odds autocorrelation: **r = 0.949**
- Significant linear time trend
- Any trending series shows spurious correlation

<br>

### ⚠️ Always first-difference time series correlations

---

<!-- _class: invert -->
<!-- _paginate: false -->

# Results
## RQ2: Descriptive Findings

---

# Finding 1: Battlegrounds ARE Engaged

## +143% Higher Political Search Interest

- **IRR = 2.43** (95% CI: 2.36–2.50)
- After population controls
- Previous −23.5% finding was artifact

<br>

**Battleground voters seek more political information**

---

# Finding 2: Michigan is Hyper-Local

## +419% State-Specific Searches

| Top Michigan Searches |
|----------------------|
| UAW |
| Detroit jobs |
| Auto industry |

<br>

**📍 Campaign implication:** Localize messaging in MI

---

# Finding 3: Nevada is Disengaged

## −88% Political Search Interest

| Category | NV vs. National |
|----------|-----------------|
| Political | **−26%** |
| Immigration | −17% |
| Partisan Media | −9% |

<br>

**📺 Campaign implication:** Non-digital outreach needed

---

# Finding 4: Immigration Beyond Borders

## Not Just Border States

| State | Immigration Deviation |
|-------|----------------------|
| Texas | +26% |
| **Pennsylvania** | **+24%** |
| **Georgia** | **+21%** |
| Arizona | +6% |

<br>

**🗺️ Immigration is nationally salient**

---

# Finding 5: AI Anxiety is Coastal

## California: +7% AI/Jobs Searches

| State | AI/Jobs Deviation |
|-------|-------------------|
| **California** | **+7%** |
| Pennsylvania | +6% |
| Michigan | +1% |
| Wisconsin | −1% |

<br>

**💻 AI fears concentrated in tech hubs**

---

# Finding 6: War Isn't Personal Yet

## All States: −20% to −23% Iran War Searches

- Despite active conflict
- "Am I going to be drafted": **97% zeros**
- No draft = no personal salience

<br>

**🔇 Voters are not Googling the war**

---

<!-- _class: invert -->
<!-- _paginate: false -->

# Results
## RQ3: Methodological Findings

---

# Realistic Search Terms FAIL

## Validation Attrition

| Stage | Terms Passed |
|-------|--------------|
| Initial candidates | 25 |
| National validation | 12 |
| State-level collection | 3 |
| Full quality check | **1** |

<br>

**Only "ICE near me" survived**

---

# Why Realistic Terms Fail

## People Don't Type Full Sentences

| What Researchers Think | What People Type |
|------------------------|------------------|
| "why is food so expensive" | food prices |
| "will AI take my job" | AI jobs |
| "am I going to be drafted" | draft age |

<br>

**2-4 word fragments, not questions**

---

# Small States Are Unreliable

## Structural Google Trends Limitation

| State | Population | Zero Rate |
|-------|------------|-----------|
| New Hampshire | 1.4M | **64%** |
| Maine | 1.4M | **64%** |
| California | 39M | <1% |

<br>

**⚠️ Flag states <3M as low-confidence**

---

<!-- _class: invert -->
<!-- _paginate: false -->

# Summary

---

# Key Takeaways

| Domain | Finding |
|--------|---------|
| **Predictive** | ❌ 0/14 Granger causality — all spurious |
| **Descriptive** | ✅ Battlegrounds +143%, MI hyper-local, NV disengaged |
| **Methodological** | ⚠️ Colloquial terms fail (1/25), small states unreliable |

---

# Campaign Implications

| State | Strategy |
|-------|----------|
| **Michigan** | Localize: UAW, auto jobs, Detroit |
| **Nevada** | Go offline: TV, unions, canvassing |
| **Pennsylvania** | Immigration messaging resonates |
| **All Battlegrounds** | High digital engagement viable |
| **Rust Belt** | Don't lead with AI anxiety |

---

# Theoretical Contribution

## What "Vibes" Actually Capture

> Google Trends measures **what the public is curious about**—not how they will vote

- Search ≠ sentiment
- Curiosity ≠ commitment  
- Attention ≠ attitude

<br>

**Descriptive value YES, predictive value NO**

---

# Methodological Contribution

## Multi-Agent Computational Triangulation

- Independent analysis reduces confirmation bias
- Cross-validation catches spurious findings
- CommDAAF protocol enforces rigor

<br>

**AI-assisted research WITH human oversight**

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Questions?

<br>

**AgentAcademy Team**
agentacademy.lampbotics.com

*Data and code available upon request*

---

# Appendix: Granger Causality

| State | F-stat | p-value | Sig |
|-------|--------|---------|-----|
| PA | 0.73 | .400 | ❌ |
| MI | 1.25 | .326 | ❌ |
| WI | 0.27 | .605 | ❌ |
| AZ | 0.36 | .831 | ❌ |
| GA | 0.02 | .881 | ❌ |
| NV | 1.21 | .281 | ❌ |
| NC | 1.14 | .336 | ❌ |
| National | 0.59 | .709 | ❌ |

---

# Appendix: Failed Search Terms

## Terms with >50% Zeros

| Term | Zero Rate |
|------|-----------|
| AI taking jobs | 99.7% |
| Will AI replace | 99.4% |
| Am I going to be drafted | 97% |
| Stock market crash | 95% |
| US troops Iran | 88% |
| Grocery prices | 84% |
| Why is food so expensive | 69% |

---

# Appendix: State Comparison

| State | Immigration | Political | AI/Jobs |
|-------|-------------|-----------|---------|
| PA | +24% | +4% | +6% |
| MI | +19% | −7% | +1% |
| WI | — | −17% | +4% |
| AZ | +6% | −10% | +3% |
| GA | +21% | −4% | +1% |
| NV | −17% | **−26%** | +4% |
| NC | +20% | −21% | −5% |
| CA | +23% | +12% | **+7%** |
| TX | +26% | −12% | −1% |
