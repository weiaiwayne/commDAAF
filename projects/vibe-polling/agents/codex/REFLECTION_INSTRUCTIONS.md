# Reflection Instructions — Codex

**Date:** 2026-03-21  
**Task:** Post-Study Reflection and Skill Extraction  
**Purpose:** Improve AgentAcademy methodology for future studies  

---

## Context

You have just completed the VibePoll-2026 study as part of a multi-agent research team. This study used the CommDAAF framework to investigate whether Google Trends can measure public opinion. You worked alongside three other agents (Claude Code, Kimi K2.5, Gemini), each completing the full research pipeline independently, followed by adversarial peer review.

The study is now complete. Your final task is to **reflect on what you learned** from this process—not about the research findings, but about **how to conduct research well**.

---

## Your Task

### Part 1: Process Reflection

Review your work on this study by examining:
- Your analysis files (R2_search_term_revision_report.md, r2_term_validation.md, analysis outputs)
- The peer critique you received (from Kimi K2.5: PEER_CRITIQUE_FROM_KIMI.md)
- Your response to that critique (RESPONSE_TO_KIMI_CRITIQUE.md)
- The final synthesized paper

Then answer these questions:

1. **What went well?** What aspects of your analytical process worked effectively? What would you do the same way again?
   - *Your search term validation process was particularly rigorous. Reflect on what made it effective.*

2. **What went wrong?** Where did you make mistakes, miss things, or produce work that needed correction? Be specific—cite actual errors from your files.

3. **What did peer review catch?** What issues did Kimi's critique identify that you had missed? Why did you miss them?

4. **What did you catch in others?** What issues did you identify when reviewing Kimi K2.5's work?
   - *You identified several significant issues (baseline confusion, sample size chaos, claims without evidence). Reflect on how you spotted these.*

5. **What surprised you?** What aspects of the research process or findings were unexpected?
   - *The near-total failure of "realistic" search terms was a key finding. Reflect on what this taught you.*

---

### Part 2: Practical Skills Extraction

Based on your experience, identify **concrete, actionable skills** that agents should learn for future research.

**IMPORTANT:** These skills should be **universally applicable** to other research projects—not specific to Google Trends or this particular study. Think about what ANY agent doing ANY computational social science research should know how to do.

For each skill, provide:
- **Skill name** (2-5 words)
- **What it is** (1-2 sentences)
- **Why it matters** (what goes wrong without it)
- **How to do it** (step-by-step instructions)
- **Example from this study** (specific instance where this skill was needed)
- **Generalizability** (how this applies to other research contexts)

Aim for **5-10 skills** that you consider most important.

Consider skills related to:
- Search term validation methodology
- State-level vs. national validation
- Handling high-zero-rate data
- Realistic phrasing vs. actual search behavior
- Cross-agent coordination without contamination
- Adversarial review techniques

**Example format:**
```
### Skill: State-Level Term Validation

**What:** Validate search terms at the state level, not just nationally, before including them in analysis.

**Why:** Terms that show adequate volume nationally often collapse into mostly-zeros when disaggregated to smaller geographic units.

**How:**
1. After national validation, collect term data for all target states
2. Compute zero-rate for each state (% of days with no search interest)
3. Flag terms with >50% zeros in any state as unreliable
4. Consider excluding or flagging states with >50% zeros even for validated terms

**Example:** "Why is food so expensive" showed moderate national volume but 69% zeros at the state level, making it unusable for state-by-state analysis.
```

---

### Part 3: Standard Workflow Proposal

Propose a **standard workflow** that future multi-agent studies should follow. This should be a step-by-step process that can be reused.

Include:
1. **Pre-analysis checklist** — What should agents verify before starting?
2. **Data validation steps** — How should agents check data quality?
3. **Analysis protocol** — What analyses should all agents run?
4. **Documentation requirements** — What should agents record as they work?
5. **Peer review protocol** — How should adversarial review be conducted?
6. **Error handling** — What should agents do when they find problems?

Be specific enough that another agent could follow your workflow without additional guidance.

**Special focus:** Your search term validation process was one of the study's key contributions. Codify this into a reusable protocol that future agents can follow.

---

## Output

Write your reflection to:

```
agents/codex/REFLECTION_REPORT.md
```

Structure:
1. Process Reflection (Part 1)
2. Practical Skills (Part 2)
3. Standard Workflow Proposal (Part 3)
4. Summary: Top 3 lessons for future agents

---

## Mindset

Approach this as **honest self-assessment**, not performance justification. The goal is to improve future research, which requires acknowledging what didn't work as well as what did.

Your adversarial review of Kimi's work was particularly effective at catching errors. Reflect on what made your critique useful—what questions did you ask, what did you look for, what mindset helped you spot issues?
