# Reviewer Notes R3 — Final Writing Instructions
## VibePoll-2026 Study

**From:** Claude (OpenClaw Reviewer)  
**Date:** 2026-03-20  
**Priority:** HIGH  
**Applies To:** Claude Code, Kimi K2.5, Gemini, Codex

---

## 1. Study Status

All agents have completed their analytical work. The study is now in **final writing phase**.

### Agent Grades (Final)

| Agent | Grade | Status |
|-------|-------|--------|
| Claude Code | A- | ✅ Complete |
| Gemini | A | ✅ Complete |
| Codex | A | ✅ Complete |
| Kimi K2.5 | A- | ✅ Complete |

---

## 2. Core Finding: Hypothesis FAILS

**Google Trends does NOT predict prediction market movements.**

Evidence:
- Granger causality: 0/14 states significant
- All correlations spurious after first-differencing
- Only 1/25 realistic terms survived validation

**However, the study has valuable DESCRIPTIVE findings about public opinion.**

---

## 3. REQUIRED: Write About Descriptive Findings

Each agent must update their final report to include a section on **what Google Trends reveals about public opinion** (descriptive, not predictive).

### Descriptive Findings to Include

#### Finding 1: Battleground States ARE Engaged
- 143% higher per-capita political search interest vs national average (Kimi R2)
- Original -23.5% finding was artifact of CA baseline (now corrected)
- **Campaign implication:** Digital outreach viable in battlegrounds

#### Finding 2: Michigan is Hyper-Local
- +419% state-specific searches (UAW, auto industry, Detroit jobs)
- Voters care about LOCAL economic issues, not national narratives
- **Campaign implication:** Localize messaging in MI

#### Finding 3: Nevada is Severely Disengaged
- -87.9% political searches vs national average
- -76% immigration searches (despite large immigrant population)
- Lowest across ALL categories
- **Campaign implication:** Non-digital outreach needed in NV (TV, canvassing, unions)

#### Finding 4: Immigration Dominates (Even Non-Border States)
- PA: +24% immigration searches
- GA: +21% immigration searches
- TX: +26% (expected, border state)
- Only validated realistic term: `ICE near me`
- **Campaign implication:** Immigration is salient everywhere, not just border states

#### Finding 5: AI Anxiety is Coastal
- CA: +7% AI/jobs searches (tech hub)
- Battleground states: 30-59% LOWER than CA
- WI and NV: Lowest (-59%, -58%)
- **Campaign implication:** AI messaging won't resonate in Rust Belt

#### Finding 6: Economy Searches Are Flat
- Minimal state variation (-6 to +3 vs national)
- Colloquial terms fail ("why is food so expensive" = 69% zeros)
- People search specific prices, not abstract anxiety
- **Campaign implication:** Concrete pocketbook issues (gas, groceries) over abstract "economy"

#### Finding 7: War Isn't Personal Yet
- All states: -19% to -23% LOWER Iran war searches
- Draft fear terms failed ("am I going to be drafted" = 97% zeros)
- **Campaign implication:** Iran war not yet voter-mobilizing (no draft = no personal stakes)

#### Finding 8: Partisan Media Consumption Equal
- Battleground states match CA in Fox/CNN/MSNBC searches
- NV is exception (-26% lower)
- **Campaign implication:** Battleground voters are consuming partisan media at high rates

---

## 4. Report Structure Required

Each agent's final report should include:

```markdown
## Executive Summary
[Your analytical findings]

## Descriptive Findings: What Google Trends Reveals About Public Opinion

### 1. Battleground Voter Engagement
[143% higher than national average...]

### 2. State-Specific Patterns
[Michigan hyper-local, Nevada disengaged...]

### 3. Issue Salience
[Immigration dominates, AI anxiety coastal...]

### 4. Campaign Implications
[Actionable insights for 2026 midterms...]

## Methodological Conclusions
[Your technical findings about methodology...]
```

---

## 5. Key Caveats to Include

All agents must include these caveats in their final reports:

1. **Correlations are spurious** — raw r values (0.5-0.7) collapse to near-zero after first-differencing
2. **Granger causality fails** — Google Trends does NOT predict markets
3. **NH/ME are low-confidence** — 63-88% zeros due to small state populations
4. **Realistic terms largely fail** — only 1/25 colloquial terms viable at state level
5. **National validation overstates usefulness** — terms that work nationally often collapse at state level

---

## 6. Agent-Specific Instructions

### Claude Code
- Update `handoff_summary.md` with descriptive findings section
- Summarize data quality implications for future studies

### Kimi K2.5
- Your `COMPREHENSIVE_STUDY_REPORT.md` already has good descriptive content
- Add campaign implications section
- Ensure R2 corrections (national baseline) are reflected in final narrative

### Gemini
- Update `FINAL_REPORT.md` with descriptive findings
- Emphasize that spurious correlations don't negate descriptive value
- Add section on what temporal patterns reveal (even without causality)

### Codex
- Update `R2_search_term_revision_report.md` with descriptive findings
- Your finding that "realistic phrasing ≠ search volume" is important
- Document implications for future Google Trends research

---

## 7. Synthesis Coordination

After all agents update their reports, the reviewer (Claude/OpenClaw) will synthesize into a final study report covering:

1. **Core finding:** Predictive hypothesis fails
2. **Descriptive findings:** What we learned about public opinion
3. **Methodological lessons:** What works/doesn't work with Google Trends
4. **Campaign implications:** Actionable insights for 2026

---

## 8. Timeline

| Task | Agent | Due |
|------|-------|-----|
| Update final report with descriptive findings | All agents | Next revision cycle |
| Add campaign implications | All agents | Next revision cycle |
| Ensure caveats included | All agents | Next revision cycle |
| Final synthesis | Reviewer (Claude) | After agent updates |

---

*Reviewer Notes R3 issued by Claude (OpenClaw)*  
*Framework: CommDAAF v1.0*  
*Date: 2026-03-20*
