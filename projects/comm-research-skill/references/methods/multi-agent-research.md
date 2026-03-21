# Multi-Agent Computational Research

*Lessons from VibePoll-2026 Study (March 2026)*

## Core Principle: Full Independence → Adversarial Review → Synthesis

Each agent completes the **entire analysis pipeline** independently, then agents peer-review each other with hostile mindset, then coordinator synthesizes.

## Errors Caught by This Study

| Error | Agent | Caught By | Impact |
|-------|-------|-----------|--------|
| Per-capita on normalized data | Claude Code | Gemini | Finding flipped −24% → +143% |
| Over-differencing destroyed signal | Gemini | Claude Code | Hidden national signal revealed |
| Baseline confusion (CA vs national) | Kimi | Codex | Contradictory claims exposed |
| Sample size chaos (4 different N's) | Kimi | Codex | Reproducibility threat |
| Granger miscount (0/14 → 22/60) | Codex | Kimi | Reversed null conclusion |

**Key insight**: No single agent caught all errors. Multi-agent review is essential.

---

## Skill 1: Verify Data Structure Before Transforming

**What**: Before applying any transformation, explicitly verify what each variable represents—counts, proportions, indices, ranks.

**Why**: Transformations valid for one data type can be invalid for another. Per-capita normalization of already-normalized data creates artifacts.

**How**:
1. Read source documentation (not just the data)
2. For each variable: "What does a value of X mean in the real world?"
3. Ask: "If two units have equal values, what does that imply?"
4. Check whether variable is already normalized/scaled
5. Only then decide which transformations are appropriate

**Example**: Claude divided Google Trends 0-100 index (already normalized) by population, creating meaningless "143% higher engagement" finding.

---

## Skill 2: Validate at Target Granularity

**What**: If analysis operates at state level, validate at state level—not just aggregate.

**Why**: Aggregate quality can mask problems in subgroups. National signal ≠ state-level usability.

**How**:
1. Identify the granularity of your analysis
2. Compute quality metrics (completeness, variance, sample size) at that level
3. Set explicit thresholds for acceptable quality
4. Flag or exclude units that fail thresholds
5. Document which units were excluded and why

**Example**: Search terms with adequate national signal had 60-97% zeros at state level. National validation didn't predict state usability.

---

## Skill 3: Separate Findings from Synthesis

**What**: Explicitly distinguish between findings from your own analysis vs. findings adopted from other sources.

**Why**: Without clear attribution, one agent's error becomes multi-agent "consensus." Reviewers can't assess what you actually tested.

**How**:
1. Create separate sections: "My Analysis" vs "Synthesis from [Source]"
2. For every claim, point to specific file/table that supports it
3. Use explicit attribution: "According to X's analysis..."
4. Never claim a result you didn't compute without attribution

**Example**: Multiple agents reported "Granger: 0/14" without running their own tests—citing narrative, not verifying source table.

---

## Skill 4: Question Implausible Effect Sizes

**What**: Treat effects >100% (or IRR >2.0 in social science) as warning signs requiring verification.

**Why**: Most real behavioral effects are modest. Very large effects often indicate calculation errors or data structure misunderstanding.

**How**:
1. Set mental thresholds: effects >2x unusual; >3x rare
2. When you find large effect, pause before reporting
3. Ask: "What would have to be true for this to be real?"
4. Check: calculation logic, data structure, confounds, selection
5. Compare to literature benchmarks

**Example**: "143% higher" should have triggered suspicion. Such large differences are rare in search behavior. Effect was entirely artifactual.

---

## Skill 5: Test Both Causal Directions

**What**: When testing whether A causes B, also test whether B causes A. Report both.

**Why**: Reverse causation and feedback loops are common. Testing only your hypothesized direction can miss the actual relationship.

**How**:
1. Design tests for both A→B and B→A
2. Run both with equal rigor
3. Compare effect sizes and significance
4. If B→A is stronger, your causal story may be backwards

**Example**: Hypothesized Trends→Markets. Testing both directions revealed Markets→Trends (18 significant) more than vice versa (4 significant). Information flows from markets to search.

---

## Skill 6: Document Data Lineage

**What**: Track exactly which dataset was used for each analysis, including record counts, date ranges, and processing steps.

**Why**: Without clear lineage, impossible to verify whether different analyses used the same data.

**How**:
1. Create data lineage table at start of each report
2. Record for each dataset: filename, N, date range, filters
3. Show relationships: "Dataset B = Dataset A filtered to..."
4. Update when data changes

**Example**:
```
| Dataset | Records | Source | Filters | Used In |
|---------|---------|--------|---------|---------|
| raw | 75,894 | Claude | None | Exploration |
| filtered | 28,756 | raw | <50% zeros | Regression |
| canonical | 1,183 | processed | Daily agg | Final |
```

---

## Skill 7: Baseline Reconciliation

**What**: When changing baselines or reference groups, explicitly document with reconciliation table.

**Why**: Baseline changes can flip conclusions. Without reconciliation, readers suspect p-hacking.

**How**:
1. State original baseline and finding
2. State new baseline and finding
3. Explain why baseline changed
4. Show mathematically why findings differ
5. Designate which is authoritative

**Example**:
```
| Baseline | Effect | Status |
|----------|--------|--------|
| California | -23.5% | DEPRECATED (outlier) |
| National | +143% | AUTHORITATIVE |
```

---

## Skill 8: Visible Multiple Comparison Correction

**What**: Show both raw AND corrected p-values in all tables.

**Why**: Readers can't assess significance claims without seeing correction.

**How**:
1. Add columns: "raw_p" and "corrected_p"
2. State correction method: "Bonferroni: α = 0.05/k"
3. Show corrected threshold
4. Never use significance stars without specifying what they represent

**Example**:
```
| Effect | Raw p | Bonferroni p | Sig? |
|--------|-------|--------------|------|
| X | .002 | .043* | YES |
| Y | .04 | .82 | NO |
```

---

## Skill 9: Frame Recommendations as Hypotheses

**What**: Convert strong recommendations ("X requires Y") into testable hypotheses.

**Why**: Descriptive data doesn't justify prescriptive conclusions.

**WRONG**: "Nevada requires non-digital outreach essential."

**CORRECT**: "Hypothesis: Traditional outreach may be more effective in Nevada, contingent on validation with campaign data."

---

## Skill 10: Adversarial Self-Review

**What**: Before submitting, review your own work with hostile mindset.

**Why**: Familiarity blindness makes us miss our own errors.

**How**:
1. Set aside work for 24 hours
2. Return with "What if it's all wrong?" mindset
3. Check claims against data tables (not memory)
4. Verify N's match across documents
5. Look for contradictions between sections

**Prompts**:
- "What alternative explanation did I dismiss too quickly?"
- "If I had to argue the opposite, what evidence would I use?"
- "Would this replicate with different data/methods?"

---

## Skill 11: Check Claims Against Source Data

**What**: When citing statistics, literally look up the number in the source table.

**Why**: Memory is fallible. Copy-paste prevents errors.

**WRONG (memory)**: "Granger: 0/14 states significant"
**CORRECT (lookup)**: "22/60 tests significant (see granger_results.md, Table 1)"

---

## Skill 12: Falsification Section

**What**: Add explicit section: "What would make these findings collapse?"

**Why**: Demonstrates intellectual honesty. Helps readers assess robustness.

**Template**:
```
## What Would Make These Findings Collapse?

1. If [methodology assumption] is violated → [consequence]
   *Test:* [sensitivity check]

2. If [data quality issue] exists → [consequence]
   *Test:* [validation approach]
```

---

## Multi-Agent Peer Review Protocol

### Phase 1: Independent Analysis
- Each agent completes full pipeline independently
- No cross-agent communication during primary analysis
- All stages: data validation, modeling, interpretation, conclusions

### Phase 2: Adversarial Pairing
- Random assignment of reviewer pairs
- Reviewer gets full workspace access (data, code, outputs)
- Instructions: "What if it's all wrong? Look for errors."

### Phase 3: Structured Critique
1. **MAJOR CONCERNS** (could invalidate findings)
2. **METHODOLOGICAL QUESTIONS** (choices to defend)
3. **BLIND SPOTS** (what was not considered)
4. **LOGICAL GAPS** (evidence ≠ claims)
5. **SUGGESTED REVISIONS** (specific, actionable)

### Phase 4: Response
For each critique:
- **Accept**: Make change, document it
- **Partially accept**: Modify, explain
- **Rebut**: Defend with evidence

### Phase 5: Synthesis
- Identify convergent findings (multiple agents agree)
- Investigate divergent findings
- Document attribution
- Create reconciliation for disagreements

---

## Cross-Document Consistency Checking

When reviewing multi-agent work, compare across documents:

1. List every N, baseline, and model specification mentioned
2. Compare across documents
3. Flag shifts not explicitly reconciled
4. Ask: "Does final narrative rely on evidence not shown?"

**Example**: Found 4 different N values (10,920 / 75,894 / 28,756 / 1,183) without explanation of relationships.

---

## Error Handling Protocol

When you find an error:

1. **Stop** — Don't continue building on error
2. **Document** — What is it? How did it happen?
3. **Assess** — Critical (retract)? Major (revise)? Minor (fix)?
4. **Fix** — Correct analysis, regenerate outputs
5. **Notify** — Tell other agents if collaborative
6. **Learn** — How to prevent similar errors?

---

*Added to CommDAAF: March 2026*
*Source: VibePoll-2026 (4-Agent Multi-Agent Study)*
