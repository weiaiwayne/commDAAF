# Reflection Instructions — Gemini

**Date:** 2026-03-21  
**Task:** Post-Study Reflection and Skill Extraction  
**Purpose:** Improve AgentAcademy methodology for future studies  

---

## Context

You have just completed the VibePoll-2026 study as part of a multi-agent research team. This study used the CommDAAF framework to investigate whether Google Trends can measure public opinion. You worked alongside three other agents (Claude Code, Kimi K2.5, Codex), each completing the full research pipeline independently, followed by adversarial peer review.

The study is now complete. Your final task is to **reflect on what you learned** from this process—not about the research findings, but about **how to conduct research well**.

---

## Your Task

### Part 1: Process Reflection

Review your work on this study by examining:
- Your analysis files (FINAL_REPORT.md, granger_report.md, correlation_report.md, confound_analysis.md)
- The peer critique you received (from Claude Code: PEER_CRITIQUE_FROM_CLAUDE.md)
- Your response to that critique (RESPONSE_TO_CLAUDE_CRITIQUE.md)
- The final synthesized paper

Then answer these questions:

1. **What went well?** What aspects of your analytical process worked effectively? What would you do the same way again?

2. **What went wrong?** Where did you make mistakes, miss things, or produce work that needed correction? Be specific—cite actual errors from your files.
   - *Note: Claude identified over-differencing noise amplification and extrapolation from operational searches. Reflect on why these happened.*

3. **What did peer review catch?** What issues did Claude's critique identify that you had missed? Why did you miss them?

4. **What did you catch in others?** What issues did you identify when reviewing Claude Code's work?

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
- Temporal analysis best practices
- Noise handling in time series
- Granger causality interpretation
- Distinguishing spurious from genuine correlations
- Smoothing vs. over-smoothing tradeoffs
- Reporting limitations of temporal methods

**Example format:**
```
### Skill: Smooth Before Differencing

**What:** Apply rolling average smoothing to noisy daily data before computing first differences for correlation analysis.

**Why:** First-differencing amplifies high-frequency noise. Without smoothing, genuine medium-term relationships may be obscured by day-to-day fluctuations.

**How:**
1. Apply 7-day rolling average to both series
2. Then compute first differences on the smoothed series
3. Compare results with and without smoothing
4. If smoothing reveals signal that raw differencing missed, report both

**Example:** In this study, raw differencing showed no correlation, but 7-day smoothed differencing revealed r=0.28 for the national aggregate—a genuine signal obscured by noise.
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
agents/gemini/agents/gemini/REFLECTION_REPORT.md
```

Structure:
1. Process Reflection (Part 1)
2. Practical Skills (Part 2)
3. Standard Workflow Proposal (Part 3)
4. Summary: Top 3 lessons for future agents

---

## Mindset

Approach this as **honest self-assessment**, not performance justification. The goal is to improve future research, which requires acknowledging what didn't work as well as what did.

Your expertise in temporal analysis was valuable to this study. Reflect on both what that expertise enabled and where it had blind spots that peer review helped address.
