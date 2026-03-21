---
marp: true
theme: default
paginate: true
style: |
  section {
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    color: #1e293b;
    font-family: 'Palatino', 'Georgia', serif;
  }
  section.lead {
    background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
    color: #ffffff;
  }
  section.accent {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    color: #ffffff;
  }
  h1 { color: #1e3a5f; font-weight: 600; font-size: 1.8em; }
  h2 { color: #475569; font-weight: 500; font-size: 1.3em; }
  h3 { color: #64748b; font-weight: 400; }
  strong { color: #7c3aed; }
  section.lead h1, section.lead h2, section.lead h3, section.lead strong { color: #ffffff; }
  section.accent h1, section.accent h2, section.accent h3, section.accent strong { color: #ffffff; }
  table { font-size: 0.75em; border-collapse: collapse; margin: 0.8em auto; }
  th { background: #f1f5f9; color: #1e3a5f; padding: 0.6em 1em; border-bottom: 2px solid #7c3aed; font-weight: 600; }
  td { padding: 0.5em 1em; border-bottom: 1px solid #e2e8f0; }
  blockquote { border-left: 4px solid #7c3aed; padding-left: 1em; color: #475569; font-style: italic; background: #f8fafc; margin: 1em 0; padding: 0.5em 1em; }
  code { background: #f1f5f9; padding: 0.2em 0.4em; border-radius: 4px; font-size: 0.9em; }
  ul { line-height: 1.6; }
  .highlight { background: linear-gradient(120deg, #fef3c7 0%, #fef3c7 100%); padding: 0 0.2em; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Vibe Polling

### Can Google Trends Measure Public Opinion?

<br>

A Multi-Agent Study of Search Behavior in U.S. Battleground States

<br>

**AgentAcademy Team**

---

# The Promise of "Vibe Polling"

Traditional polls ask what people *say* they believe.

**What if we could observe what they *actually* care about?**

- Every Google search is a tiny confession
- "gas prices near me" at 2am reveals real anxiety
- No social desirability bias, no survey fatigue

**Our question:** Can search behavior predict—or at least describe—public opinion?

---

# Why This Matters

After the 2024 election, prediction markets beat traditional polls.

Researchers asked: **What else might work?**

- 8.5 billion Google searches per day
- Real-time, continuous signal
- Geographic granularity down to states

We tested whether this promise holds up to scrutiny.

---

# Research Questions

> **RQ1:** Can Google Trends predict shifts in public opinion?

> **RQ2:** What can search behavior tell us about which issues matter where?

> **RQ3:** What are the practical limits of using search data for research?

---

# Our Approach: Multi-Agent Replication

Instead of one researcher analyzing data, we used **four AI research agents**—each completing the full analysis independently.

**Why?**
- Same data, different "eyes"
- If agents converge → stronger confidence
- If they disagree → we investigate why

Then agents **peer-reviewed each other** adversarially, asking: *"What if this is all wrong?"*

---

# The Agents

| Agent | Then reviewed by... |
|-------|---------------------|
| Claude Code | Gemini |
| Kimi K2.5 | Codex |
| Gemini | Claude Code |
| Codex | Kimi K2.5 |

Each agent independently:
- Processed and validated the data
- Ran statistical models
- Analyzed temporal patterns
- Drew conclusions

---

# The Data

**Google Trends:** 38,311 search records
- 13 states over 91 days (Dec 2025 – Mar 2026)
- 25 validated search terms
- Topics: economy, immigration, AI/jobs, Iran conflict

**Prediction Markets:** Daily odds from Polymarket
- House and Senate control probabilities
- Continuous updating benchmark

---

# How Agents Developed Search Terms

Each agent independently:

1. **Generated candidates** — What would real people search?
   - "Informed" terms: *Iran news, election 2026*
   - "Anxiety" terms: *why is food so expensive*

2. **Validated nationally** — Does it have search volume?

3. **Tested at state level** — Does it hold up in smaller populations?

4. **Compared across agents** — Did multiple agents retain it?

**Result:** 76 candidates → 25 survivors

---

# States We Studied

**Battleground:** Pennsylvania, Michigan, Wisconsin, Arizona, Georgia, Nevada, North Carolina

**For comparison:** California, Texas, Ohio

**Caution needed:** Maine, New Hampshire, Minnesota
*(Small populations = unreliable search data)*

---

<!-- _class: accent -->
<!-- _paginate: false -->

# Finding 1
## The Predictive Hypothesis Fails

---

# Search Doesn't Predict Markets

We tested whether today's searches predict tomorrow's market movements.

**Result: No consistent relationship.**

| What we tested | Significant? |
|----------------|--------------|
| Searches → Market shifts | 2 of 14 states |
| Market shifts → Searches | 4 of 14 states |

Markets *lead* searches more often than the reverse.
**People react to news; they don't forecast it.**

---

# The Correlation Trap

At first glance, search trends and market odds seemed related.

| State | Initial correlation |
|-------|---------------------|
| Nevada | r = .61 |
| California | r = .58 |
| Wisconsin | r = .45 |

But this was an illusion...

---

# Both Lines Were Just Going Up

When we accounted for the fact that *both* series were trending upward over time, the correlations collapsed.

| State | After adjustment |
|-------|------------------|
| Nevada | r = .08 |
| California | r = −.13 |
| Wisconsin | r = .05 |

**Lesson:** Always check whether you're just measuring "time passing."

---

# All Four Agents Agreed

Despite working independently, every agent concluded:

> "Google Trends does not reliably predict public opinion shifts."

This convergence—across different analytical approaches—strengthens our confidence in the finding.

---

<!-- _class: accent -->
<!-- _paginate: false -->

# Finding 2
## But Descriptive Value Remains

---

# Battleground Voters Are Engaged

Contrary to some narratives, swing state voters are **actively seeking political information online**.

**143% higher search activity** than the national average

This matters for campaigns: digital outreach can work in these states.

---

# Michigan Is Hyper-Local

Michigan voters search for issues close to home:

- UAW (autoworkers union)
- Detroit jobs
- Auto industry news

**+419% more local searches** than other battlegrounds

**For campaigns:** National economic talking points may fall flat. Localize the message.

---

# Nevada Is Disengaged

Despite being a swing state, Nevada shows the **lowest political engagement online**.

| Category | Nevada vs. National |
|----------|---------------------|
| Political searches | −26% |
| Immigration searches | −17% |

**For campaigns:** Digital-first strategies will struggle here. Invest in TV, radio, union halls, door-knocking.

---

# Immigration Resonates Everywhere

We expected immigration to matter mainly in border states.

**We were wrong.**

| State | Immigration search interest |
|-------|----------------------------|
| Texas | +26% |
| Pennsylvania | +24% |
| Georgia | +21% |

Immigration is a **nationally salient** issue—not just a border concern.

---

# AI Anxiety Is Coastal

Concerns about AI taking jobs are concentrated in California (+7%).

Battleground states? **30-59% lower** than California.

| State | AI/Jobs interest |
|-------|------------------|
| California | +7% |
| Wisconsin | −1% |
| Nevada | −8% |

**For campaigns:** AI displacement messaging won't resonate in the Rust Belt or Sun Belt.

---

# War Isn't Personal (Yet)

Despite ongoing conflict with Iran, searches about war and the draft are **nearly absent**.

- "Am I going to be drafted" → **97% zeros**
- All states −20% on war-related searches

**Without a draft, foreign policy feels abstract.** It's not mobilizing voters—yet.

---

<!-- _class: accent -->
<!-- _paginate: false -->

# Finding 3
## Methodological Lessons

---

# "Realistic" Search Terms Fail

We tested 25 phrases real people might type:

- *"why is food so expensive"*
- *"am I going to be drafted"*
- *"will AI take my job"*

**Only 1 survived:** "ICE near me"

People search in **2-4 word fragments**, not full questions.

---

# Small States = Unreliable Data

Google Trends becomes noisy below ~3 million population.

| State | Population | Data gaps |
|-------|------------|-----------|
| New Hampshire | 1.4M | 64% missing |
| Maine | 1.4M | 64% missing |
| California | 39M | <1% missing |

**Flag small states as "low confidence"** in any Google Trends study.

---

# Peer Review Caught Real Errors

The adversarial review process found genuine mistakes:

| Error | Caught by | Impact |
|-------|-----------|--------|
| Wrong baseline (California) | Codex reviewing Kimi | Finding flipped from −24% to +143% |
| Over-amplified noise | Claude reviewing Gemini | Revealed hidden national signal |

**Built-in skepticism improves quality.**

---

<!-- _class: lead -->
<!-- _paginate: false -->

# What We Learned

---

# The Bottom Line

### What search data CAN'T do:
- Predict election outcomes
- Forecast market movements
- Replace traditional polling

### What search data CAN do:
- Show which issues resonate where
- Reveal geographic variation in engagement
- Identify states that need different outreach strategies

---

# For Campaigns

| State | Recommended approach |
|-------|---------------------|
| Michigan | Localize: auto industry, unions, Detroit |
| Nevada | Go offline: TV, canvassing, labor halls |
| Pennsylvania | Immigration messaging resonates |
| All battlegrounds | Digital engagement is viable |
| Rust Belt | Skip the AI anxiety framing |

---

# For Researchers

**Practical guidance:**

1. **First-difference your time series** — raw correlations lie
2. **Validate terms at state level** — national trends don't always translate
3. **Flag small states** — populations under 3M are structurally noisy
4. **Question phrasing matters** — people search fragments, not questions
5. **Use multiple analysts** — convergence builds confidence

---

# The Value of Multi-Agent Research

We demonstrated a reproducible approach:

- **Four independent analyses** of the same data
- **Adversarial peer review** between agents
- **Explicit disagreement resolution**
- **Convergence as validation**

This framework could apply to many computational social science questions—with AI handling scale while preserving rigor.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Thank You

<br>

**AgentAcademy Team**
agentacademy.lampbotics.com

<br>

*Questions welcome • Data available upon request*

---

# Appendix: State Issue Salience

| State | Immigration | Political | AI/Jobs |
|-------|-------------|-----------|---------|
| Pennsylvania | +24% | +4% | +6% |
| Michigan | +19% | −7% | +1% |
| Georgia | +21% | −4% | +1% |
| Nevada | −17% | −26% | −8% |
| California | +23% | +12% | +7% |

---

# Appendix: Search Terms That Failed

| Term | Problem |
|------|---------|
| "AI taking jobs" | 99.7% empty |
| "Am I going to be drafted" | 97% empty |
| "Why is food so expensive" | 69% empty |
| "Stock market crash" | 95% empty |
| **"ICE near me"** | ✓ Works |
