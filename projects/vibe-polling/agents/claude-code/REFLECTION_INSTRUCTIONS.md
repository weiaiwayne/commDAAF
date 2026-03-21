# Reflection Instructions — Claude Code

**Date:** 2026-03-21  
**Task:** Post-Study Reflection and Skill Extraction  
**Purpose:** Improve AgentAcademy methodology for future studies  

---

## Context

You have just completed the VibePoll-2026 study as part of a multi-agent research team. This study used the CommDAAF framework to investigate whether Google Trends can measure public opinion. You worked alongside three other agents (Kimi K2.5, Gemini, Codex), each completing the full research pipeline independently, followed by adversarial peer review.

The study is now complete. Your final task is to **reflect on what you learned** from this process—not about the research findings, but about **how to conduct research well**.

---

## Your Task

### Part 1: Process Reflection

Review your work on this study by examining:
- Your analysis files and outputs
- The peer critique you received (from Gemini)
- Your response to that critique
- The final synthesized paper

Then answer these questions:

1. **What went well?** What aspects of your analytical process worked effectively? What would you do the same way again?

2. **What went wrong?** Where did you make mistakes, miss things, or produce work that needed correction? Be specific—cite actual errors from your files.

3. **What did peer review catch?** What issues did Gemini's critique identify that you had missed? Why did you miss them?

4. **What did you catch in others?** (If applicable) What issues did you identify when reviewing other agents' work?

5. **What surprised you?** What aspects of the research process or findings were unexpected?

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

**Example format:**
```
### Skill: First-Difference Time Series

**What:** Before correlating two time series, compute changes (day-to-day differences) rather than using raw levels.

**Why:** Raw correlations between trending series are spurious—both going up creates artificial correlation even without genuine relationship.

**How:**
1. For each series, compute: diff[t] = value[t] - value[t-1]
2. Correlate the differenced series instead of raw values
3. If correlation collapses (drops >50%), the raw correlation was spurious

**Example:** In this study, Nevada showed r=0.61 raw correlation but r=0.08 after differencing—revealing the relationship was artifactual.
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

---

## Output

Write your reflection to:

```
agents/claude-code/REFLECTION_REPORT.md
```

Structure:
1. Process Reflection (Part 1)
2. Practical Skills (Part 2)
3. Standard Workflow Proposal (Part 3)
4. Summary: Top 3 lessons for future agents

---

## Mindset

Approach this as **honest self-assessment**, not performance justification. The goal is to improve future research, which requires acknowledging what didn't work as well as what did.

The most valuable reflections will be specific and actionable—not "I should have been more careful" but "I should have run X check before Y step because Z can go wrong."
