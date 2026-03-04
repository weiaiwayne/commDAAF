# Methodology Fixes: Addressing Reviewer Critiques

Based on critical reviews from Claude, Kimi, and GLM (Reviewer 2), this document outlines fixes for identified methodological issues.

---

## Study 1: Diaspora & Temporal Dynamics

### Issue 1: RQ2 Unsupported (CRITICAL)
**Problem:** Frame prevalence shifts are significant (χ²=18.36, p=0.005), but effectiveness changes have p>0.27.

**Fix:**
1. ✅ Retract claim that "effectiveness changes" are supported
2. ✅ Report only: "Frame PREVALENCE shifts across phases, but effectiveness changes not statistically significant"
3. 🔄 Need larger N to detect effect sizes for effectiveness

**Corrected conclusion:** Frame distribution changes over protest lifecycle (what people post), but we cannot conclude frame effectiveness changes (how audiences respond).

---

### Issue 2: Small N Cells (CRITICAL)
**Problem:** CONFLICT×EN = 5, making claims like "4.35x advantage" unreliable.

**Fix:**
1. 🔄 Code Ukraine data (adds 339 posts, total N=719)
2. 🔄 Apply bootstrap confidence intervals for small cells
3. ✅ Report which cells have reliable vs. unreliable estimates

**Minimum N per cell for inference:**
- n ≥ 30 for parametric tests
- n ≥ 10 for non-parametric
- n < 10: report as "exploratory, not inferential"

**Cells to flag:**
| Cell | N | Status |
|------|---|--------|
| CONFLICT×EN | 5 | ⚠️ Exploratory only |
| HUMANITARIAN×EN | 3 | ⚠️ Exploratory only |
| INJUSTICE×EN | 6 | ⚠️ Exploratory only |

---

### Issue 3: Arbitrary Phase Boundaries
**Problem:** Sept 16-22 (onset) vs Sept 23+ (peak) has no theoretical justification.

**Fix:**
1. 🔄 Add sensitivity analysis with alternative boundaries:
   - 5/12 split (shorter onset)
   - 10/7 split (longer onset)
   - Data-driven changepoint detection
2. 🔄 Report if findings hold across boundary specifications

---

### Issue 4: Multiple Comparison Correction
**Problem:** 4 RQs × multiple tests, no correction applied.

**Fix:**
1. ✅ Apply Benjamini-Hochberg FDR correction
2. Report both raw and adjusted p-values

**Tests to correct:**
- RQ1: 7 frame×language comparisons = 7 tests
- RQ2: 7 frame×phase comparisons = 7 tests  
- RQ3: 7 Gini comparisons = 7 tests
- RQ4: 7 peak/trough + 7 correlations = 14 tests
- **Total: 35 tests → FDR threshold q=0.05**

---

### Issue 5: Language ≠ Diaspora
**Problem:** English posts could be journalists, bots, Iranians code-switching.

**Fix:**
1. ❌ Cannot fix without account metadata (location, bio, network)
2. ✅ Reframe claims: "Language-moderated effects" not "Diaspora amplification"
3. 🔄 Future work: Collect account-level data for proper diaspora identification

---

### Issue 6: Coordination Claims Without Null Model
**Problem:** 8:1 peak/trough could be timezone effects.

**Fix:**
1. 🔄 Build null model: Random permutation of timestamps
2. Compare observed clustering to null distribution
3. Report: "Clustering exceeds random baseline by X standard deviations"

---

## Study 2: Engagement Decomposition

### Issue 7: Zero-Inflation in RT/Like Ratio
**Problem:** Many posts have 0 RTs → RT/Like = 0, violating OLS assumptions.

**Fix:**
1. 🔄 Use Tobit regression (censored at 0)
2. 🔄 Or use hurdle model: P(RT>0) × E[RT|RT>0]
3. Alternative: Log(RT/Like + 1) transformation

---

### Issue 8: Sample Mismatch (Claude n=249 vs GLM/Kimi n=339)
**Problem:** Different models analyzed different samples.

**Fix:**
1. ✅ All models use identical filtered sample (n=249 with engagement)
2. Re-run GLM/Kimi validation on n=249

---

### Issue 9: Low R² (3.8%)
**Problem:** Model explains almost nothing.

**Fix:**
1. 🔄 Add missing variables:
   - Time of posting (hour, day of week)
   - Tweet type (original vs reply vs quote)
   - Media attachment (image, video)
   - Sentiment (positive/negative tone)
2. 🔄 Report this as model limitation, not finding

---

### Issue 10: H3 Interaction Not Properly Tested
**Problem:** Claimed "opposite of expected" without formal interaction test.

**Fix:**
1. 🔄 Add `log_followers × hashtag_count` interaction term
2. Report interaction coefficient and p-value
3. If not significant, remove "Account Size Paradox" claim

---

### Issue 11: Emoji Finding Overinterpreted (p=0.057)
**Problem:** Marginal significance spun as theory.

**Fix:**
1. ✅ Report as "exploratory finding, not significant at α=0.05"
2. ✅ Remove "emotional bonding" theoretical interpretation
3. Note: GLM found p=0.017, so finding may be sensitive to specification

---

## Cross-Study Issues

### Issue 12: Inconsistent Validation Standards
**Problem:** Study 1 used 3-model; Study 2 did not.

**Fix:**
1. 🔄 Re-run Study 2 with 3-model validation (in progress)
2. Establish standard: All inferential claims require 3-model agreement

---

### Issue 13: Single Dataset
**Problem:** All findings are #MahsaAmini-specific.

**Fix:**
1. 🔄 Code Ukraine data for cross-context comparison (in progress)
2. Test if effects generalize across protest vs. war contexts
3. Future: Add #HongKongProtests, #BlackLivesMatter for broader validation

---

## Implementation Status

| Fix | Status | Priority |
|-----|--------|----------|
| Retract RQ2 effectiveness claim | ✅ Done | Critical |
| Code Ukraine data | 🔄 In progress | Critical |
| Bootstrap CI for small cells | 🔄 Pending | High |
| FDR correction | 🔄 Pending | High |
| Sensitivity analysis (phases) | 🔄 Pending | High |
| Null model for coordination | 🔄 Pending | Medium |
| Zero-inflated model for RT/Like | 🔄 Pending | Medium |
| Add interaction term for H3 | 🔄 Pending | Medium |
| Reframe "Diaspora" as "Language-moderated" | ✅ Done | High |
| Tone down theoretical claims | ✅ Done | High |

---

## Revised Conclusions (Post-Fix)

### Study 1 (Revised)
1. **RQ1 (Language Effect):** English posts receive higher engagement than Persian (p<0.02), with frame-dependent moderation. *Exploratory; small N in some cells.*
2. **RQ2 (Temporal):** Frame PREVALENCE shifts across phases (p=0.005). Effectiveness changes not significant (p>0.27).
3. **RQ3 (Power Law):** Engagement follows power law (α=2.24). Frames differ in concentration (Gini 0.83-0.98).
4. **RQ4 (Coordination):** Temporal clustering exists but cannot distinguish from timezone effects without null model.

### Study 2 (Revised)
1. **Hashtag count:** Positive association with RT/Like ratio (p≈0.05). Effect size small.
2. **Mentions:** Direction consistent with theory (negative), but not significant.
3. **Emoji:** Negative association, significance varies by model (p=0.017-0.068). Exploratory.
4. **Follower interaction:** No significant interaction; remove "Account Size Paradox."

---

*Document created to track methodology fixes based on 3-model peer review*
