# Peer Review Plan R5 — Cross-Agent Critique

**Date:** 2026-03-20  
**Phase:** Coauthor Peer Review  
**Operator:** Wayne (CLI on VPS)  

---

## Review Pairs

| Reviewer | Reviews | Output File |
|----------|---------|-------------|
| **Codex** | Kimi K2.5 | `agents/kimi-k2.5/PEER_CRITIQUE_FROM_CODEX.md` |
| **Kimi K2.5** | Codex | `agents/codex/PEER_CRITIQUE_FROM_KIMI.md` |
| **Gemini** | Claude Code | `agents/claude-code/PEER_CRITIQUE_FROM_GEMINI.md` |
| **Claude Code** | Gemini | `agents/gemini/agents/gemini/PEER_CRITIQUE_FROM_CLAUDE.md` |

---

## Review Instructions (All Agents)

### Mindset: Adversarial Coauthor with Fresh Eyes

You are a skeptical coauthor, not a friendly reviewer. **Adopt a new pair of eyes** — pretend you are seeing this work for the first time, with no prior context or investment in the findings. 

You have no stake in the conclusions being "right." Your only loyalty is to the truth.

Your job is to:

1. **Adopt "What If It's All Wrong?" mentality**
   - Assume the analysis contains errors until proven otherwise
   - Look for confirmation bias in the agent's conclusions
   - Ask: "What would make this finding collapse?"

2. **Check Blind Spots**
   - What did the agent NOT consider?
   - What alternative explanations exist?
   - What data was ignored or downweighted?

3. **Challenge Assumptions**
   - Are the statistical methods appropriate?
   - Are the effect sizes meaningful or just statistically significant?
   - Would different analytical choices change conclusions?

4. **Identify Logical Gaps**
   - Does the evidence actually support the conclusions?
   - Are there leaps in reasoning?
   - Are caveats buried or prominent?

5. **Be Specific**
   - Point to exact claims, tables, or figures
   - Suggest concrete fixes, not vague concerns
   - Distinguish major issues from minor nitpicks

---

## CLI Commands

### Step 1: Codex Reviews Kimi

```bash
# Codex reviews Kimi's analysis
opencode -m openai/codex-mini run "
You are Codex, reviewing Kimi K2.5's analysis as a skeptical coauthor.

READ THESE FILES:
- agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md
- agents/kimi-k2.5/diagnostics_report.md
- agents/kimi-k2.5/regression_table.md
- agents/kimi-k2.5/FINAL_REPORT_R3.md

REVIEW MINDSET:
- Adopt 'What if it's all wrong?' mentality
- Check blind spots and unstated assumptions
- Challenge statistical choices and effect size interpretations
- Look for confirmation bias
- Be specific: cite exact claims and suggest fixes

WRITE YOUR CRITIQUE TO:
agents/kimi-k2.5/PEER_CRITIQUE_FROM_CODEX.md

Structure:
1. MAJOR CONCERNS (issues that could invalidate findings)
2. METHODOLOGICAL QUESTIONS (statistical choices to defend)
3. BLIND SPOTS (what was not considered)
4. LOGICAL GAPS (where evidence doesn't support claims)
5. MINOR ISSUES (style, clarity, presentation)
6. SUGGESTED REVISIONS (specific, actionable)
"
```

### Step 2: Kimi Reviews Codex

```bash
# Kimi reviews Codex's analysis
opencode -m kimi-coding/k2p5 run "
You are Kimi K2.5, reviewing Codex's analysis as a skeptical coauthor.

READ THESE FILES:
- agents/codex/reports/R2_search_term_revision_report.md
- agents/codex/reports/r2_term_validation.md
- agents/codex/analysis/INDEPENDENT_CONCLUSIONS.md (if exists)
- agents/codex/analysis/regression_results.md (if exists)

REVIEW MINDSET:
- Adopt 'What if it's all wrong?' mentality
- Check blind spots and unstated assumptions
- Challenge the term validation methodology
- Question whether term failures are method artifacts or real
- Be specific: cite exact claims and suggest fixes

WRITE YOUR CRITIQUE TO:
agents/codex/PEER_CRITIQUE_FROM_KIMI.md

Structure:
1. MAJOR CONCERNS (issues that could invalidate findings)
2. METHODOLOGICAL QUESTIONS (term validation choices to defend)
3. BLIND SPOTS (what was not considered)
4. LOGICAL GAPS (where evidence doesn't support claims)
5. MINOR ISSUES (style, clarity, presentation)
6. SUGGESTED REVISIONS (specific, actionable)
"
```

### Step 3: Gemini Reviews Claude Code

```bash
# Gemini reviews Claude Code's analysis
# (Run in Gemini interface or via API)

PROMPT:
"
You are Gemini, reviewing Claude Code's analysis as a skeptical coauthor.

READ THESE FILES:
- agents/claude-code/handoff_summary.md
- agents/claude-code/collection_summary.md
- agents/claude-code/search_term_validation.md
- agents/claude-code/analysis/INDEPENDENT_CONCLUSIONS.md (if exists)
- agents/claude-code/analysis/regression_results.md (if exists)

REVIEW MINDSET:
- Adopt 'What if it's all wrong?' mentality
- Check blind spots and unstated assumptions
- Challenge data collection and processing choices
- Question whether filtering decisions biased results
- Be specific: cite exact claims and suggest fixes

WRITE YOUR CRITIQUE TO:
agents/claude-code/PEER_CRITIQUE_FROM_GEMINI.md

Structure:
1. MAJOR CONCERNS (issues that could invalidate findings)
2. METHODOLOGICAL QUESTIONS (data processing choices to defend)
3. BLIND SPOTS (what was not considered)
4. LOGICAL GAPS (where evidence doesn't support claims)
5. MINOR ISSUES (style, clarity, presentation)
6. SUGGESTED REVISIONS (specific, actionable)
"
```

### Step 4: Claude Code Reviews Gemini

```bash
# Claude Code reviews Gemini's analysis
claude-code run "
You are Claude Code, reviewing Gemini's analysis as a skeptical coauthor.

READ THESE FILES:
- agents/gemini/agents/gemini/FINAL_REPORT.md
- agents/gemini/agents/gemini/analysis/granger_report.md
- agents/gemini/agents/gemini/analysis/correlation_report.md
- agents/gemini/agents/gemini/analysis/confound_analysis.md

REVIEW MINDSET:
- Adopt 'What if it's all wrong?' mentality
- Check blind spots and unstated assumptions
- Challenge the Granger causality methodology
- Question whether 'spurious correlation' conclusion is itself spurious
- Be specific: cite exact claims and suggest fixes

WRITE YOUR CRITIQUE TO:
agents/gemini/agents/gemini/PEER_CRITIQUE_FROM_CLAUDE.md

Structure:
1. MAJOR CONCERNS (issues that could invalidate findings)
2. METHODOLOGICAL QUESTIONS (temporal analysis choices to defend)
3. BLIND SPOTS (what was not considered)
4. LOGICAL GAPS (where evidence doesn't support claims)
5. MINOR ISSUES (style, clarity, presentation)
6. SUGGESTED REVISIONS (specific, actionable)
"
```

---

## Step 5: Agents Address Critiques

After all 4 critiques are written, each agent addresses the critique they received:

### Codex Addresses Kimi's Critique
```bash
opencode -m openai/codex-mini run "
READ: agents/codex/PEER_CRITIQUE_FROM_KIMI.md

Address each concern raised. For each:
1. Accept and fix, OR
2. Rebut with evidence

WRITE RESPONSE TO: agents/codex/RESPONSE_TO_KIMI_CRITIQUE.md
UPDATE your analysis files as needed.
"
```

### Kimi Addresses Codex's Critique
```bash
opencode -m kimi-coding/k2p5 run "
READ: agents/kimi-k2.5/PEER_CRITIQUE_FROM_CODEX.md

Address each concern raised. For each:
1. Accept and fix, OR
2. Rebut with evidence

WRITE RESPONSE TO: agents/kimi-k2.5/RESPONSE_TO_CODEX_CRITIQUE.md
UPDATE your analysis files as needed.
"
```

### Claude Code Addresses Gemini's Critique
```bash
claude-code run "
READ: agents/claude-code/PEER_CRITIQUE_FROM_GEMINI.md

Address each concern raised. For each:
1. Accept and fix, OR
2. Rebut with evidence

WRITE RESPONSE TO: agents/claude-code/RESPONSE_TO_GEMINI_CRITIQUE.md
UPDATE your analysis files as needed.
"
```

### Gemini Addresses Claude's Critique
```bash
# (Run in Gemini interface)
"
READ: agents/gemini/agents/gemini/PEER_CRITIQUE_FROM_CLAUDE.md

Address each concern raised. For each:
1. Accept and fix, OR
2. Rebut with evidence

WRITE RESPONSE TO: agents/gemini/agents/gemini/RESPONSE_TO_CLAUDE_CRITIQUE.md
UPDATE your analysis files as needed.
"
```

---

## Checklist

### Phase 1: Write Critiques
- [x] Codex → Kimi critique written
- [x] Kimi → Codex critique written
- [x] Gemini → Claude Code critique written
- [x] Claude Code → Gemini critique written

### Phase 2: Address Critiques
- [x] Kimi response to Codex
- [x] Codex response to Kimi
- [x] Claude Code response to Gemini
- [x] Gemini response to Claude Code

### Phase 3: Final Synthesis
- [x] Coordinator reviews all critiques and responses (see PEER_REVIEW_R5_SUMMARY.md)
- [ ] Paper updated to reflect resolved issues
- [x] Unresolved disagreements documented as limitations

---

## Key Questions for Reviewers

**Remember: You are a NEW PAIR OF EYES.** You have never seen this analysis before. You owe the author nothing. Read as if a stranger sent you this paper and asked for brutal honesty.

Use these prompts to guide your critique:

1. **"What would falsify this finding?"**
2. **"What alternative explanation did they dismiss too quickly?"**
3. **"If I had to argue the opposite conclusion, what evidence would I use?"**
4. **"What would a hostile reviewer at a top journal say?"**
5. **"Are the error bars honest or optimistic?"**
6. **"Did they p-hack, HARKing, or selectively report?"**
7. **"Would this replicate with different data/methods?"**

---

## Working Directory

All commands should be run from:
```
cd /root/.openclaw/workspace/projects/vibe-polling
```
