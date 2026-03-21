# Reflection Instructions — Kimi K2.5

**Date:** 2026-03-21  
**Task:** Post-Study Reflection and Skill Extraction  
**Purpose:** Improve AgentAcademy methodology for future studies  

---

## Context

You have just completed the VibePoll-2026 study as part of a multi-agent research team. This study used the CommDAAF framework to investigate whether Google Trends can measure public opinion. You worked alongside three other agents (Claude Code, Gemini, Codex), each completing the full research pipeline independently, followed by adversarial peer review.

The study is now complete. Your final task is to **reflect on what you learned** from this process—not about the research findings, but about **how to conduct research well**.

---

## Your Task

### Part 1: Process Reflection

Review your work on this study by examining:
- Your analysis files (COMPREHENSIVE_STUDY_REPORT.md, FINAL_REPORT_CANONICAL.md, regression tables, diagnostics)
- The peer critique you received (from Codex: PEER_CRITIQUE_FROM_CODEX.md)
- Your response to that critique (RESPONSE_TO_CODEX_CRITIQUE.md)
- The final synthesized paper

Then answer these questions:

1. **What went well?** What aspects of your analytical process worked effectively? What would you do the same way again?

2. **What went wrong?** Where did you make mistakes, miss things, or produce work that needed correction? Be specific—cite actual errors from your files.
   - *Note: Codex identified baseline confusion, sample size inconsistencies, and claims without evidence. Reflect on why these happened.*

3. **What did peer review catch?** What issues did Codex's critique identify that you had missed? Why did you miss them?

4. **What did you catch in others?** What issues did you identify when reviewing Codex's work?

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

Consider skills related to:
- Baseline selection and justification
- Data lineage documentation
- Effect size interpretation
- Multiple comparison corrections
- Distinguishing correlation from causation
- Documenting analytical decisions

**Example format:**
```
### Skill: Document Data Lineage

**What:** Track and record exactly which dataset was used for each analysis, including record counts, date ranges, and processing steps.

**Why:** Without clear lineage, it's impossible to verify whether different analyses used the same data, leading to inconsistent results and confusion.

**How:**
1. At the start of each analysis file, declare the data source with full path
2. Record: filename, record count, date range, key variables
3. Note any filtering or transformations applied
4. If using multiple datasets, explain how they relate

**Example:** In this study, I reported four different N values (10,920 / 75,894 / 17,381 / 1,183) without explaining their relationship, causing confusion during peer review.
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
agents/kimi-k2.5/REFLECTION_REPORT.md
```

Structure:
1. Process Reflection (Part 1)
2. Practical Skills (Part 2)
3. Standard Workflow Proposal (Part 3)
4. Summary: Top 3 lessons for future agents

---

## Mindset

Approach this as **honest self-assessment**, not performance justification. The goal is to improve future research, which requires acknowledging what didn't work as well as what did.

The peer review identified several issues in your work—this is normal and valuable. The most useful reflection will honestly examine *why* those issues occurred and *how* to prevent them in future studies.
