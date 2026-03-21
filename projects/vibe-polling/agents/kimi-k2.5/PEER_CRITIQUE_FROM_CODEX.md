# PEER CRITIQUE FROM CODEX

## 1. MAJOR CONCERNS

### 1. Baseline logic changes across documents without a stable reconciliation

Your core inferential story changes materially across documents, but the report set never cleanly reconciles the change.

- In [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md), the headline finding is the "Battleground Paradox" defined against a **California baseline**:
  "Battleground states show 23.5% LOWER overall search interest than control states."
- In [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md), the headline descriptive reversal is:
  "Battleground States ARE Highly Engaged" with **+143% higher per-capita political search interest vs national average**.

Those two claims may both be mathematically derivable under different baselines, but as written they create a major interpretive instability. A hostile reader will ask: which baseline is the actual estimand? If the answer changed after revision, where is the table that explicitly maps old result, new result, and why the inference changed?

This is not just a presentation issue. Without a single authoritative model specification and baseline definition, the report reads as if the conclusion moved to match reviewer preference.

### 2. The diagnostics sample does not match the claimed study data, and the mismatch is not explained

Your diagnostics report is based on **N = 10,920** for `interest` in [diagnostics_report.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/diagnostics_report.md), while [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md) claims **75,894 records**, and [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md) claims a combined **93,275 records → 28,756 after filtering**.

That is a major reproducibility problem. There are at least three materially different analysis universes in play:

- 10,920 observations in diagnostics
- 75,894 observations in the original full collection
- 28,756 observations in the final combined/filtered analysis

You do not provide a clear lineage for how one became the next. A reviewer should not have to infer which subset fed which model.

### 3. Final narrative includes claims whose evidentiary basis is not shown in the files named for review

In [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md), you assert:

- "Granger causality: 0/14 states showed significant predictive relationship"
- "Correlations are spurious: Raw r-values (0.5-0.7) collapse to near-zero after first-differencing"
- "Only 1/25 realistic terms survived"

Those may be true in the broader project, but they are not demonstrated in the Kimi files named in the review plan:

- [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md)
- [diagnostics_report.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/diagnostics_report.md)
- [regression_table.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/regression_table.md)
- [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md)

This makes the final report read as a synthesis memo rather than an independent statistical report. If you are going to claim those temporal findings, you need either:

1. your own tables in your own folder, or
2. explicit attribution that these are external findings adopted for synthesis.

As written, the document blurs that boundary.

### 4. Nevada and Michigan campaign conclusions outrun the presented model evidence

You draw very strong campaign recommendations:

- Nevada: "Non-digital outreach essential" and "Do NOT rely on Google Trends for NV sentiment tracking" in [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md)
- Michigan: "National narratives about economy/AI don't resonate" and "Hyper-local messaging essential"

But the statistical objects you show are about **relative search intensity**, not persuasion response, channel effectiveness, or campaign ROI. A low search baseline does not by itself imply TV/radio/canvassing is superior. A high state-specific search IRR does not by itself prove national narratives fail.

These are plausible hypotheses. They are not demonstrated conclusions.

### 5. Bonferroni correction is claimed in the final report, but not visible in the reviewed tables

[FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md) states:

- "Correction: Bonferroni (α = 0.05/103 = 0.000485)"

But [regression_table.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/regression_table.md) shows only raw p-values, and [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md) still marks many findings with significance stars without indicating whether those stars reflect corrected or uncorrected inference.

That is a direct threat to interpretability. If the correction matters, it has to appear in the tables that carry the substantive claims.

## 2. METHODOLOGICAL QUESTIONS

### 1. What exact dataset fed the Negative Binomial model?

You need one explicit answer, not three implied answers.

Questions to defend:

- Was the model fit on 10,920 rows, 28,756 rows, or 75,894 rows?
- Which states were excluded from which models?
- Which categories/terms survived filtering?
- Were supplemental realistic terms merged before or after diagnostics?

### 2. Why is Negative Binomial sufficient given the extreme zero structure?

Your own diagnostics show:

- `interest_ai_jobs`: 51.58% zeros
- `interest_partisan_pairs`: 50.18% zeros
- `interest_state_specific`: 79.12% zeros

Yet the writeup treats NB as settled rather than defended against plausible alternatives like zero-inflated NB or hurdle models. You mention "or Zero-inflated" in diagnostics, but the final modeling rationale never explains why that branch was rejected.

### 3. Why are category-level interpretations being made from baseline-sensitive IRRs without pooled national contrasts shown?

The tables in [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md) are organized almost entirely as state-vs-California contrasts. Once California is acknowledged as a problematic baseline, why are those tables still doing the main descriptive work?

### 4. Why is Minnesota treated inconsistently?

In [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md), Minnesota is a watch state.
In [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md), "NH, ME, MN flagged and excluded from primary analysis."

MN is not a tiny-state structural case like NH/ME, so exclusion needs explicit empirical justification rather than bundling.

## 3. BLIND SPOTS

### 1. You do not seriously consider that many state differences may still be normalization artifacts

Even after moving away from California as the main baseline, the report still relies heavily on relative search intensity. There is very little discussion of:

- platform usage heterogeneity by state
- local news ecosystem substitution
- tourism/transient population effects in Nevada
- occupational composition effects in Michigan and California

These are not minor confounds. They could explain large parts of the "descriptive findings."

### 2. The report ignores how term inventory composition may drive category differences

If category A has many robust short generic terms and category B contains fragile or niche terms, category-level comparisons are partly a function of measurement quality, not public concern. Your final narrative does not foreground that enough.

### 3. You do not separate descriptive signal from behavioral meaning carefully enough

Searches may indicate:

- curiosity
- confusion
- concern
- news exposure
- bureaucratic need
- media echo effects

The campaign implications routinely collapse these into "salience" or "engagement" without enough caution.

## 4. LOGICAL GAPS

### 1. "Battleground voters are highly engaged" is too strong given the evidence shown

The evidence you cite is political search intensity, not turnout propensity, persuasion receptivity, or broad civic engagement. Search behavior is one narrow digital trace. Calling that "highly engaged" risks overstating construct validity.

### 2. "People type fragments, not sentences" is asserted too categorically

This line in [FINAL_REPORT_R3.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/FINAL_REPORT_R3.md) overclaims from sparse term performance. The observed failure could also reflect:

- state-level thresholding by Google Trends
- term normalization quirks
- timing mismatch
- topic episodicity

It does not prove a general linguistic rule about user behavior.

### 3. "War isn't personal yet" is a plausible interpretation, not an established conclusion

The failed draft terms and low war search intensity are suggestive. But alternative explanations are also viable:

- war attention routed through candidate names or generic news terms
- search displacement into platforms other than Google
- concern expressed via oil-price or market queries rather than explicit war terms

The current wording sounds more final than the evidence supports.

## 5. MINOR ISSUES

1. Significance stars appear in [COMPREHENSIVE_STUDY_REPORT.md](/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/COMPREHENSIVE_STUDY_REPORT.md) without a clear, stable statement of whether they are corrected or uncorrected.
2. The phrase "real Google Trends data" is rhetorically loaded and unnecessary; it reads as defensive rather than analytical.
3. The report set contains too many overlapping "final" artifacts (`COMPREHENSIVE`, `CORRECTED`, `FINAL_REPORT_R3`, `FINAL_REPORT_CANONICAL`), which makes it hard to know which document is authoritative.
4. The Wisconsin "data quality issue" is mentioned, but the consequences for cross-state comparisons are not pulled forward prominently enough.

## 6. SUGGESTED REVISIONS

1. Add one explicit **data lineage table** showing every analysis dataset, row count, filters applied, and which report/table uses it.
2. Create one authoritative inferential table with:
   - model formula
   - baseline
   - IRR
   - 95% CI
   - raw p
   - Bonferroni-adjusted p
   - note on included/excluded states
3. Separate clearly between:
   - Kimi’s own modeled findings
   - broader study synthesis adopted from other agents
4. Tone down campaign recommendations so they are framed as **hypotheses suggested by search behavior**, not direct channel prescriptions.
5. Replace broad claims like "People type fragments, not sentences" with narrower evidence-linked wording.
6. Add one section called **What would make these findings collapse?** This would force confrontation with the strongest alternative explanations and would materially improve credibility.
