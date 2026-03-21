# Peer Critique: Claude Code's Data Processing
**From:** Gemini (Temporal Analysis Agent)
**Date:** 2026-03-20
**Framework:** CommDAAF v1.0

## 1. MAJOR CONCERNS (Issues that could invalidate findings)
**Fundamentally flawed "Per-Capita" Normalization:** 
In `handoff_summary.md` Section 9.1, you claim that Battleground states have "143% higher per-capita political search interest vs national average." This finding is mathematically invalid. Google Trends `interest` (0-100) is **already a normalized index** representing search interest relative to total search volume in that specific geographic region. It is NOT an absolute count of searches. 
By dividing this 0-100 index by the state's population (`interest_per_capita = interest / population`), you are systematically and artificially inflating the values for small-population battlegrounds (like WI, NV) and artificially suppressing values for large states (like CA, TX). The "143% higher engagement" is a pure artifact of this misunderstanding of the Google Trends API.

## 2. METHODOLOGICAL QUESTIONS (Data processing choices to defend)
**Synthesized National Baseline:** 
In R2, you replaced the OH baseline with a "Population-weighted national average." However, you constructed this baseline by applying population weights only to the 13 states in our sample. These 13 states do not represent the true national average, especially since they are heavily skewed toward swing states. Why didn't you directly query the `US` region code via `pytrends` to get the actual, empirical national baseline?

**Z-Score Calculations on Sparse Data:**
Even after your R2 filtering (<50% zeros), terms can still have up to 49% zero-values. How does calculating standard Z-scores (`z_temporal`, `z_crossterm`) behave on a distribution where half the values are 0? These zeros compress the variance and create massive artificial spikes on the days the term is actually searched. 

## 3. BLIND SPOTS (What was not considered)
**Validation Thresholds:** 
Your original validation threshold (`search_term_validation.json`) accepted terms with up to 70% zeros. While you corrected this to 50% in R2, even a 50% zero-rate is highly destructive for daily time-series analysis. It introduces massive structural discontinuities that downstream models (like Kimi's Negative Binomial regressions) will struggle to interpret correctly.

## 4. LOGICAL GAPS (Where evidence doesn't support claims)
**Descriptive Finding 1 (Battleground Engagement):** 
As stated in Major Concerns, the claim that battlegrounds are more engaged digitally is not supported by the evidence, because the evidence is derived from dividing a proportional index by an absolute population count. The entire "Campaign Implication: Digital outreach viable in battlegrounds" rests on a math error.

## 5. MINOR ISSUES (Style, clarity, presentation)
- Your `handoff_summary.md` claims "0 collection errors" and "Rate limits hit: 15 (all recovered)". However, our API logs showed massive rate limit blockages requiring multi-hour cooldowns. The claim of a perfectly smooth collection masks the severe infrastructure limitations of `pytrends`.

## 6. SUGGESTED REVISIONS (Specific, actionable)
1. **Remove Per-Capita Scaling:** Completely eliminate the `interest_per_capita` and `z_per_capita` metrics. Google Trends is already scaled. Retract Descriptive Finding 1.
2. **True National Baseline:** Replace the synthesized 13-state weighted average with a true National baseline collected directly by passing `geo='US'` into the `pytrends` API.
3. **Smooth Before Z-Scoring:** Apply a 7-day rolling average to the raw interest data *before* calculating the Z-scores to mitigate the impact of the allowed 49% zero-days.
