# Preprint Readiness Audit

**Study:** #MahsaAmini Virality Study  
**Date:** 2026-02-27  
**Auditor:** Claude (as final adjudicator)

---

## 🔴 Critical Issues (Must Fix)

### 1. Statistical Model Mismatch
- **Problem:** DV is continuous (0.00-11.99), but we used Negative Binomial which assumes integer counts
- **Evidence:** 298/380 values are non-integers
- **Fix Options:**
  - (a) Use OLS on the already log-transformed DV
  - (b) Get raw counts and use NB on those
- **Impact:** Current NB results may be misspecified

### 2. Frame-Valence Confounding  
- **Problem:** Perfect/near-perfect correlation between certain frames and valence:
  - CONFLICT: 100% negative
  - HUMANITARIAN: 100% negative  
  - INJUSTICE: 98% negative
  - HOPE: 0% negative (100% positive)
  - SOLIDARITY: 3% negative
- **Impact:** Cannot separate frame effect from valence effect for these frames
- **Fix:** Report as limitation; consider frame-only model without valence

### 3. Low Reliability on Key Frames
- **Problem:** 3-way model agreement varies dramatically by frame:
  - CONFLICT: 33% (poor)
  - HUMANITARIAN: 45% (poor)
  - INJUSTICE: 49% (poor)
  - INFORMATIONAL: 50% (moderate)
  - HOPE: 65% (good)
  - CALL_TO_ACTION: 65% (good)
  - SOLIDARITY: 66% (good)
- **Impact:** Claims about CONFLICT/HUMANITARIAN/INJUSTICE are based on unreliable codings
- **Fix:** Report frame-specific reliability; caveat findings for low-agreement frames

---

## 🟡 Moderate Issues (Should Address)

### 4. Small Cell Size
- CONFLICT n=18 (too small for stable regression estimates)
- Consider merging or noting instability

### 5. Zero Structure
- ALL 79 zeros (20.8%) are in "low" tier
- Suggests stratified sampling by engagement level
- Need to document sampling design explicitly

### 6. Predictor Correlation
- Valence-Arousal r = -0.33 (moderate)
- Should check VIF and report

---

## 🟢 Documentation Gaps

### 7. Sampling Procedure
- Time period?
- "Viral" threshold definition?
- Platform (Twitter/X)?
- Collection method (API/scrape)?

### 8. Engagement Formula
- Need to confirm: `log(RT+1) + log(like+1) + log(quote+1)`?
- Or: `log(RT + like + quote + 1)`?

### 9. Persian Text Handling
- Models received Persian text without special instructions
- Mixed Persian/English/Arabic content

### 10. Human Validation
- CommDAAF requires N≥50 human validation for Tier 🟢 EXPLORATORY
- Current study: 0 human codings
- Must either validate or frame as "LLM-only pilot"

---

## Recommended Actions

1. **Clarify DV** - Get original engagement formula, determine correct model
2. **Re-run regression** - With properly specified model (likely OLS)
3. **Report frame-specific reliability** - Don't hide low agreement
4. **Add limitations section** covering:
   - Frame-valence confounding
   - Small cells (CONFLICT)
   - LLM-only coding (no human validation)
   - Single platform, specific time period
5. **Document sampling** - Full transparency on data collection
6. **Frame appropriately** - "Exploratory pilot study" not "definitive findings"

---

## Verdict

**UPDATED 2026-02-27:** Issues addressed below.

---

## Fixes Applied

### ✅ Statistical Model Fixed
- Changed from Negative Binomial to OLS with HC3 robust SEs
- Appropriate for log-transformed continuous DV
- Results: `regression_corrected.json`

### ✅ Valence Dropped
- Removed due to frame-valence confounding
- Documented in limitations

### ✅ Frame-Specific Reliability Added
- Full table in `frame_reliability.json`
- Caveats added for CONFLICT (33%), HUMANITARIAN (45%), INJUSTICE (49%)

### ✅ Limitations Section Added
- 7 explicit limitations documented
- Framed as exploratory pilot study

### ✅ Full Study Writeup
- See `STUDY_WRITEUP.md` for preprint draft

---

## Current Status: READY for preprint

With caveats:
- Framed as "Exploratory Pilot Study"
- All limitations explicitly documented
- No overclaiming on CONFLICT finding (low reliability, small n)
