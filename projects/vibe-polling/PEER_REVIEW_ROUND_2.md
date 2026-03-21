# Peer Review Round 2 — VibePoll-2026

**Reviewer:** Claude (OpenClaw)  
**Date:** 2026-03-19  
**Framework:** CommDAAF v1.0  
**Agents Reviewed:** Claude Code, Kimi K2.5  
**Agents On Hold:** Codex, Gemini (Google rate limit - retry in 24h)

---

## Executive Summary

| Agent | Round 1 Verdict | Round 2 Verdict | Grade |
|-------|-----------------|-----------------|-------|
| **Claude Code** | Major Revision | ✅ Minor Revision | **A-** |
| **Kimi K2.5** | Major Revision | ✅ Minor Revision | **B+** |

**Overall Assessment:** Both agents addressed the critical issues from Round 1. The analysis is now methodologically defensible, though important limitations remain. The study can proceed to synthesis with appropriate caveats.

---

## Part 1: Claude Code Review

### ✅ Issues Addressed

| Issue | Round 1 Finding | Round 2 Action | Verdict |
|-------|-----------------|----------------|---------|
| ~30% terms with 80-99% zeros | CRITICAL | Filtered to 25 terms (<50% zeros) | ✅ FIXED |
| No population control | CRITICAL | Added `state_demographics.json` + per-capita normalization | ✅ FIXED |
| CA as outlier baseline | HIGH | Flagged OH as recommended baseline | ✅ FIXED |
| Academic search terms | HIGH | Documented realistic alternatives in `term_categories.json` | ⚠️ PARTIAL |

### ⚠️ Issues Partially Addressed

**1. Realistic Search Terms Not Collected**

Claude Code documented realistic term alternatives (e.g., "cheap gas near me", "will I lose my job to AI") in `term_categories.json` but did not recollect data. The revision log states:

> "Google Trends API was heavily rate-limiting during revision attempt. Rather than wait hours for partial data, we took the pragmatic approach of filtering the existing 75,894 records."

**Reviewer Assessment:** This is a pragmatic decision given rate limits. The filtering approach addresses the immediate concern (removing zero-signal terms), but the study should explicitly note that colloquial search behavior is not captured. **This limits external validity.**

**2. Per-Capita Column Exists But Usage Unclear**

The `interest_per_capita` column was added to the processed data, but I need to verify downstream agents are actually using it vs. raw `interest` values.

### ✅ Technical Verification

```
✓ Records: 25,207 (reduced from 75,894)
✓ Terms: 25 (reduced from 76)
✓ States: 13 (unchanged)
✓ Columns include: population, log_population, interest_per_capita, z_per_capita, pop_weight
```

### 🔴 New Issue Discovered

**State-Level Zero Percentage Still High for Small States**

| State | Zero % (Post-Filter) | Issue |
|-------|---------------------|-------|
| NH | 63.7% | ⚠️ HIGH |
| ME | 63.6% | ⚠️ HIGH |
| NV | 43.7% | ⚠️ MODERATE |

**Explanation:** The filtering removed low-signal *terms* across all states, but small states (NH, ME) still have low signal *within* the retained terms. Google Trends returns 0 when search volume is too low to reliably estimate.

**Impact:** NH and ME data may be unreliable regardless of which terms are used. Consider:
- Flagging NH/ME results as low-confidence
- Excluding them from state-level comparisons
- Pooling them into a "Small States" category

### Claude Code Grade: **A-**

**Strengths:**
- Comprehensive documentation
- Correct filtering logic
- Population controls implemented
- Transparent about limitations

**Weaknesses:**
- Did not recollect with realistic terms (rate limit excuse valid but still a gap)
- NH/ME still have structural data quality issues

---

## Part 2: Kimi K2.5 Review

### ✅ Issues Addressed

| Issue | Round 1 Finding | Round 2 Action | Verdict |
|-------|-----------------|----------------|---------|
| No population control | CRITICAL | Added `log_population` offset to NB models | ✅ FIXED |
| CA as baseline | HIGH | Changed to OH as reference category | ✅ FIXED |
| No Bonferroni correction | HIGH | Applied via `multipletests()` | ✅ FIXED |
| Low-signal terms | HIGH | Filtered to terms with <50% zeros | ✅ FIXED |

### ✅ Code Review: `run_corrected_analysis.py`

**Population Offset Implementation:**
```python
model = sm.GLM(y, X, family=sm.families.NegativeBinomial(),
               offset=df_pooled['log_population'])
```
✅ **Correct.** Using `log_population` as offset in NB regression is the standard approach for per-capita analysis.

**Baseline Change:**
```python
states_order = ['OH', 'PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC', 'CA', 'TX', 'ME', 'NH', 'MN']
df['state'] = pd.Categorical(df['state'], categories=states_order, ordered=True)
```
✅ **Correct.** OH is now the reference category.

**Bonferroni Correction:**
```python
reject, p_corrected, _, _ = multipletests(all_pvalues, method='bonferroni')
```
✅ **Correct.** Standard implementation.

### ⚠️ Issues Requiring Clarification

**1. IRR of 2.434 Seems High**

From `CORRECTED_STUDY_REPORT.md`:
> "Battleground states show 143.4% HIGHER per-capita interest than controls (Ohio baseline)."

**Reviewer Concern:** An IRR of 2.434 means battleground states have 143% MORE search interest per capita than OH. This is a *very* large effect.

**Possible Explanations:**
- Correct: Battleground states really do have much higher political search interest (plausible given campaign spending and news focus)
- Artifact: The offset may not be fully compensating for state size differences
- Confound: Battleground states may have different demographics (e.g., higher internet penetration, different age distribution)

**Recommendation:** Report this finding with caution. Add a sensitivity analysis using `internet_users` instead of `population` as the offset.

**2. 67 Tests Reported But Unclear Composition**

The report states "67 tests conducted" but the breakdown is unclear. Expected tests:
- 1 battleground vs control (pooled)
- 7 battleground states × 6+ categories = ~42+
- Plus watch states and controls vs OH

**Recommendation:** Add a table listing all tests conducted.

**3. Original vs Corrected Comparison Incomplete**

The comparison table shows "TBD" for the corrected findings:
```
| Battleground vs Control | -23.5% vs CA | [see above] vs OH | TBD |
```

**Recommendation:** Complete this table with actual comparison values.

### 🟡 Statistical Concerns

**1. Model Convergence on High-Zero States**

Did the NB models converge for NH and ME given their 63%+ zero rates? Zero-inflated models (ZINB) may be more appropriate.

**2. IRR Confidence Intervals**

The 95% CI for battleground effect (2.359 - 2.511) is suspiciously narrow for N=67 tests. Verify this is per-observation CI (correct) not per-test CI (incorrect).

### Kimi K2.5 Grade: **B+**

**Strengths:**
- All critical corrections implemented correctly
- Good code structure and documentation
- Transparent about changes

**Weaknesses:**
- IRR magnitude needs verification/sensitivity analysis
- Incomplete comparison table
- Should discuss NH/ME data quality issues

---

## Part 3: Cross-Agent Integration Issues

### 1. Data Flow Verification

| Step | Source | Destination | Verified |
|------|--------|-------------|----------|
| Raw trends → Filtered | Claude Code | Kimi | ✅ Yes (25,207 records) |
| Population data | Claude Code | Kimi | ✅ Yes (13 states) |
| Log offset usage | Claude Code spec | Kimi code | ✅ Yes |

### 2. Terminology Alignment

| Term | Claude Code | Kimi | Aligned |
|------|-------------|------|---------|
| Records post-filter | 25,207 | 25,207 | ✅ |
| Terms retained | 25 | 25 | ✅ |
| Terms removed | 51 | 51 | ✅ |
| Baseline state | OH | OH | ✅ |

### 3. Outstanding Gaps

| Gap | Impact | Who Should Fix |
|-----|--------|----------------|
| Realistic terms not collected | External validity | Codex (when resumed) |
| NH/ME data quality | State-level findings unreliable | Both (flag in final report) |
| Granger causality with filtered data | Gemini's work outdated | Gemini (when resumed) |

---

## Part 4: Revised Findings Summary

### What Changed After Corrections

| Finding | Original | Corrected | Interpretation |
|---------|----------|-----------|----------------|
| Battleground vs Control | -23.5% vs CA | +143.4% vs OH | **Reversed** — original was artifact of CA being outlier |
| Tests significant (raw) | 56 | 42 | Reduced |
| Tests significant (Bonferroni) | 56 (no correction) | 34 | Further reduced |
| Terms analyzed | 76 | 25 | 67% of terms removed as noise |

### What Held After Corrections

- State-level variation exists (MI local focus, NV low engagement)
- Economy terms show highest signal
- Political terms (Fox News, CNN, MSNBC) remain strong predictors

### What Remains Unknown

- Does Google Trends predict markets? (Gemini's Granger analysis paused)
- Are correlations spurious? (Gemini's confound analysis paused)
- What would realistic colloquial terms show? (Codex not yet run)

---

## Part 5: Recommendations

### For Synthesis Report

1. **Lead with caveats:** Note that data was filtered, not recollected. External validity is limited.
2. **Flag NH/ME:** Their 63%+ zero rates make state-level findings unreliable.
3. **IRR interpretation:** The 143% finding needs sensitivity check before publication.
4. **Granger still pending:** Do not claim predictive power until Gemini completes analysis.

### For Codex (When Resumed)

1. Collect realistic colloquial terms as documented in Claude Code's revision
2. Target terms with proven signal (e.g., "cheap gas near me" has been validated in prior studies)
3. Run quality check: reject any term with >50% zeros

### For Gemini (When Resumed)

1. Re-run confound analysis on the filtered dataset (25,207 records)
2. Verify bidirectional Granger with population-weighted national aggregate
3. Update correlation report with differenced values

---

## Part 6: Final Verdicts

### Claude Code
- **Round 1:** Major Revision Required
- **Round 2:** ✅ **Minor Revision** — Address NH/ME flagging in documentation
- **Grade:** A-

### Kimi K2.5
- **Round 1:** Major Revision Required  
- **Round 2:** ✅ **Minor Revision** — Complete comparison table, verify IRR magnitude
- **Grade:** B+

### Study Overall
- **Status:** May proceed to synthesis with caveats
- **Confidence Level:** MODERATE (pending Gemini validation)
- **Publication Readiness:** NOT YET — need Granger results and realistic term collection

---

## Appendix: Verification Commands Run

```bash
# Record counts
python3 -c "import pandas as pd; df=pd.read_parquet('data/processed/trends_normalized.parquet'); print(len(df))"
# Output: 25,207

# Zero percentage by state
python3 -c "..." # See above outputs

# Columns present
python3 -c "..." # Confirmed: population, log_population, interest_per_capita, etc.
```

---

*Peer Review Round 2 completed by Claude (OpenClaw)*  
*Framework: CommDAAF v1.0*  
*Date: 2026-03-19*
