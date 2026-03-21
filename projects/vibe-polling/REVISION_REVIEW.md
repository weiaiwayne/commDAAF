# Revision Review — VibePoll-2026

**Reviewer:** Claude (OpenClaw)  
**Date:** 2026-03-19  
**Agents Reviewed:** Kimi K2.5, Gemini

---

## Executive Summary

| Agent | Revision Status | Grade |
|-------|----------------|-------|
| **Gemini** | ✅ COMPLETE | **A** |
| **Kimi** | ⚠️ DOCUMENTED BUT NOT EXECUTED | **Incomplete** |
| **Claude Code** | 🔄 Still working | — |

---

## Gemini Revision Review

### ✅ ALL Requested Revisions Completed

| Revision Request | Status | Evidence |
|-----------------|--------|----------|
| Filter to high-signal terms | ✅ Done | `process_data.py` filters to 10 terms |
| Population-weighted national aggregate | ✅ Done | US-NATIONAL in all reports |
| Run confound analysis for ALL states | ✅ Done | 14 indices tested in `confound_analysis.md` |
| Bidirectional Granger causality | ✅ Done | Both directions in `granger_report.md` |
| Add mandatory caveats to report | ✅ Done | FINAL_REPORT.md updated |
| Regenerate figures | ✅ Done | New `outputs/figures/` files |

### New Files Created (Last 30 min)
```
✅ correlation_report.md (updated)
✅ granger_report.md (updated with bidirectional)
✅ confound_analysis.md (all 14 states)
✅ REVISION_LOG.md (documentation)
✅ FINAL_REPORT.md (updated with caveats)
✅ process_data.py (high-signal filter + pop weights)
✅ analyze_confounds.py (all-state analysis)
✅ analyze_granger.py (bidirectional)
✅ merged_timeseries.parquet (reprocessed)
✅ vibe_index_timeseries.png (regenerated)
```

### Key New Findings After Revision

#### 1. Confound Analysis (All States)

| Category | Count | States |
|----------|-------|--------|
| **Likely Spurious** (drop > 0.3) | 7 | CA, GA, MN, NH, NV, OH, US-NATIONAL |
| **Not Spurious** | 7 | AZ, ME, MI, NC, PA, TX, WI |

**Critical finding:** The US-NATIONAL aggregate correlation (r=0.376) drops to **r=-0.007** after first-differencing — essentially zero. This confirms the relationship is spurious.

#### 2. Bidirectional Granger Causality

| Direction | Significant States | Interpretation |
|-----------|-------------------|----------------|
| **Vibe → Market** | US-MI (p=0.006), US-WI (p=0.028) | Search predicts markets in 2 states |
| **Market → Vibe** | US-NH (p=0.003), US-PA (p=0.0009) | Markets predict search in 2 states |

**This is NEW and important:** The relationship is bidirectional and state-specific. Michigan and Wisconsin show search leading markets; New Hampshire and Pennsylvania show markets leading search.

#### 3. Correlation Changes with Filtered Terms

| State | Original r | Revised r | Change |
|-------|-----------|-----------|--------|
| US-CA | 0.642 | 0.588 | -0.054 |
| US-NH | 0.708 | 0.226 | **-0.482** |
| US-NV | 0.649 | 0.492 | -0.157 |
| US-PA | 0.436 | -0.062 | **-0.498** |
| US-MI | 0.513 | -0.103 | **-0.616** |

**Major finding:** Many correlations REVERSED or collapsed when using only high-signal terms. The original analysis was heavily influenced by low-signal terms.

#### 4. Issue Salience Correlations

| Category | r with House Odds | Interpretation |
|----------|-------------------|----------------|
| economy | **+0.676** | Economic concern → higher Dem odds |
| ai_jobs | **-0.658** | AI concern → LOWER Dem odds |
| political | +0.269 (NS) | — |
| immigration | -0.027 (NS) | — |
| partisan_pairs | -0.284 (NS) | — |

**New insight:** AI/jobs concern is negatively correlated with Democratic odds — the opposite direction of economy!

### Code Quality Check

```python
# process_data.py — VERIFIED CORRECT
valid_terms = ['Fox News', 'CNN', 'MSNBC', 'ChatGPT', '401k', 'inflation', 
               'green card', 'asylum', 'Trump approval', 'gas prices']
df = df[df['term'].isin(valid_terms)]  # ✅ Filtering implemented

# Population weights — VERIFIED CORRECT
pop_weights = {
    'US-CA': 0.25, 'US-TX': 0.18, 'US-PA': 0.08, 'US-MI': 0.06, ...
}  # ✅ Matches reviewer specification

# analyze_confounds.py — VERIFIED CORRECT
for state in df['state'].unique():  # ✅ All states iterated
    r_raw, _ = stats.pearsonr(...)
    r_diff, _ = stats.pearsonr(diff_vibe, diff_odds)  # ✅ First-differenced
```

### Gemini Grade: **A**

✅ All revisions completed  
✅ Code changes verified  
✅ New insights generated  
✅ Caveats properly documented  
✅ Transparent revision log  

---

## Kimi K2.5 Revision Review

### ⚠️ Documented Plans But NOT Executed

| Revision Request | Status | Evidence |
|-----------------|--------|----------|
| Filter to high-signal terms | ⚠️ Planned | In REVISION_RESPONSE.md, not executed |
| Add population offset | ⚠️ Planned | Code provided, not run |
| Change baseline to OH | ⚠️ Planned | Documented, not implemented |
| Apply Bonferroni correction | ⚠️ Planned | Documented, not implemented |
| Create state demographics | ✅ Done | `state_demographics.json` created |
| Re-run regression | ❌ Not done | Old files still in place |

### Evidence of Non-Completion

```bash
# Files modified in last 30 minutes:
/agents/kimi-k2.5/data/reference/state_demographics.json   # ✅ NEW
/agents/kimi-k2.5/REVISION_RESPONSE.md                      # ✅ NEW

# Regression files still from original run (03:13, not updated):
/agents/kimi-k2.5/comprehensive_regression_table.md        # OLD (03:13)
/agents/kimi-k2.5/diagnostics_report.md                    # OLD (02:44)
/agents/kimi-k2.5/regression_table.md                      # OLD (02:51)
```

### What Kimi Did

1. ✅ Created excellent `REVISION_RESPONSE.md` documenting all planned changes
2. ✅ Created `state_demographics.json` with population data
3. ✅ Acknowledged all critique points
4. ✅ Provided correct code snippets for fixes

### What Kimi Did NOT Do

1. ❌ Actually run the revised analysis
2. ❌ Generate new regression tables with population offset
3. ❌ Apply Bonferroni correction to results
4. ❌ Update findings with new baseline (OH)

### Kimi Grade: **Incomplete**

The revision documentation is excellent (would be A-grade), but the actual analysis was not re-run. The regression tables and findings are still from the original (flawed) analysis.

**Kimi needs to:**
1. Execute `run_comprehensive_modeling.py` with population offset
2. Generate new `comprehensive_regression_table.md`
3. Update `COMPREHENSIVE_STUDY_REPORT.md` with revised findings

---

## Comparison: Original vs Revised Findings

### Gemini's Correlation Analysis

| Metric | Original | Revised | Change |
|--------|----------|---------|--------|
| Strongest state correlation | US-NH r=0.708 | US-CA r=0.588 | Different state |
| National correlation | N/A | r=0.376 → -0.007 (differenced) | Spurious confirmed |
| Terms included | ~50 | 10 | 80% filtered |
| Granger Vibe→Market | 0/13 states | 2/13 states (MI, WI) | Weak signal found |
| Granger Market→Vibe | Not tested | 2/13 states (NH, PA) | Reverse causality! |

### Kimi's Regression Analysis

| Metric | Original | Revised | Change |
|--------|----------|---------|--------|
| Battleground vs Control | -23.5% (IRR=0.765) | NOT RE-RUN | Unknown |
| Baseline state | California | Should be Ohio | NOT DONE |
| Population control | None | Should be offset | NOT DONE |
| Bonferroni correction | None | α=0.00089 | NOT DONE |

---

## Updated Conclusions

### What We Now Know (from Gemini's revision)

1. **Correlations are largely spurious** — 7/14 indices show >0.3 drop after differencing
2. **No national predictive relationship** — US-NATIONAL r drops from 0.376 to -0.007
3. **State-specific bidirectional effects exist:**
   - MI, WI: Search → Markets (potential predictive signal)
   - NH, PA: Markets → Search (reactive behavior)
4. **Economy and AI show opposite effects:**
   - Economy concern → higher Dem odds (+0.68)
   - AI concern → lower Dem odds (-0.66)
5. **Original correlations were inflated by low-signal terms**

### What We Still Don't Know (awaiting Kimi's revision)

1. Whether "Battleground Paradox" survives population control
2. How state comparisons change with OH baseline
3. Which findings survive Bonferroni correction
4. Whether Michigan +419% state-specific effect is real or artifact

---

## Recommendations

### For Kimi
```bash
# Execute these to complete revision:
cd /root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5
python scripts/run_comprehensive_modeling.py  # With population offset
# Then update COMPREHENSIVE_STUDY_REPORT.md with new findings
```

### For Final Report

Include these statements (now supported by Gemini's revision):

1. > "Google Trends search volume does NOT consistently predict prediction market movements nationally. The US-NATIONAL correlation (r=0.376) is spurious, dropping to r=-0.007 after first-differencing."

2. > "State-specific effects exist: Michigan and Wisconsin show weak predictive signals (search → markets), while New Hampshire and Pennsylvania show reactive behavior (markets → search)."

3. > "Economy-related search interest correlates positively with Democratic odds (r=0.68), while AI/jobs concern correlates negatively (r=-0.66), suggesting different voter segments."

---

## Files Reviewed

### Gemini (All Updated)
```
✅ agents/gemini/agents/gemini/REVISION_LOG.md
✅ agents/gemini/agents/gemini/FINAL_REPORT.md
✅ agents/gemini/agents/gemini/correlation_report.md
✅ agents/gemini/agents/gemini/granger_report.md
✅ agents/gemini/agents/gemini/confound_analysis.md
✅ agents/gemini/agents/gemini/scripts/process_data.py
✅ agents/gemini/agents/gemini/scripts/analyze_confounds.py
✅ agents/gemini/agents/gemini/scripts/analyze_granger.py
```

### Kimi (Partial)
```
✅ agents/kimi-k2.5/REVISION_RESPONSE.md (excellent documentation)
✅ agents/kimi-k2.5/data/reference/state_demographics.json (created)
❌ agents/kimi-k2.5/comprehensive_regression_table.md (NOT updated)
❌ agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md (NOT updated)
```

---

*Revision review completed by Claude (OpenClaw)*  
*Date: 2026-03-19*
