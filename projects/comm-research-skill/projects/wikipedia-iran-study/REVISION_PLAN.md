# Revision Plan: "Whose History?" Preprint

**Based on:** Internal review + GLM-4.7 review + Kimi K2.5 review  
**Date:** March 6, 2026  
**Current version:** PREPRINT_v2.md

---

## Consensus Assessment

| Reviewer | Verdict | Key Concern |
|----------|---------|-------------|
| Internal | Major Revisions | κ transparency, causal overclaims |
| GLM-4.7 | Major Revisions | No baseline, methods not integrated |
| Kimi K2.5 | Minor Revision | Theory underdeveloped, generalizability |

**Synthesis:** The paper has strong methodological innovation (multi-model LLM coding) and exemplary transparency. Main gaps are: (1) no comparison baseline, (2) theory doesn't advance beyond applying Fricker, (3) methods remain disconnected.

---

## Priority 1: Must Fix Before Submission

### 1.1 Add Comparison Baseline ⚠️ CRITICAL

**Problem:** All three reviewers flag this. Without baseline, we can't know if 41% reverters is exceptional.

**Solution Options:**
| Option | Effort | Value |
|--------|--------|-------|
| A. Sample 25-50 non-conflict Wikipedia articles | High | High |
| B. Use published Wikipedia statistics as proxy | Low | Medium |
| C. Narrow claims to "high-conflict articles only" | Low | Low |

**Recommended:** Option B + C combined
- Find published data on typical Wikipedia revert patterns (Yasseri et al. 2012 has some)
- Compare our 41% reverter rate to known baselines
- Explicitly limit all claims to "high-conflict Middle East articles"

**Action items:**
1. Search literature for baseline revert statistics
2. Add "Comparison to Prior Work" subsection in Discussion
3. Revise all generalizing claims (Abstract, Introduction, Conclusion)

---

### 1.2 Develop Platform-Specific Theory ⚠️ CRITICAL

**Problem:** Paper applies Fricker but doesn't advance theory. Reviewers want distinction between "epistemic injustice" vs "legitimate platform governance."

**Solution:** Add new theoretical contribution:

**Proposed Concept: "Credential-Based Epistemic Authority"**
- Fricker: identity-based prejudice → testimonial injustice
- Wikipedia: credential-based authority (edit count, EC status, tenure)
- Key question: When does credential-based authority become unjust?

**New theoretical claims:**
1. Platform epistemics differ from face-to-face because authority markers are behavioral (what you did) not demographic (who you are)
2. This creates a continuum from legitimate meritocracy to exclusionary credentialism
3. The line between them depends on whether credentials track relevant epistemic virtues

**Action items:**
1. Add Section 2.4: "From Identity to Credentials: Platform-Specific Epistemic Authority"
2. Revise Discussion to use new framework
3. Articulate conditions under which EC protection crosses from governance to injustice

---

### 1.3 Integrate Methods ⚠️ IMPORTANT

**Problem:** GLM notes network analysis and discourse analysis remain disconnected.

**Solution:** Add integration analysis:

**New analysis:**
1. Map talk page participants to revert network positions
2. Cross-tabulate: Do "reverter" editors use different discursive strategies than "reverted" editors?
3. For illustrative cases (iran_087, iran_113), show network position

**Action items:**
1. Run network-discourse mapping analysis
2. Add Table: "Talk Page Participants by Network Role"
3. Revise Section 4.2.3 to include network position for each case

---

## Priority 2: Should Fix

### 2.1 Strengthen Small-N Constructs

**Problem:** Testimonial injustice (n=4), Policy weaponization (n=4) have too few cases.

**Solution options:**
| Option | Action |
|--------|--------|
| A. Drop low-N constructs | Remove from main analysis, note as "exploratory" |
| B. Expand sample | Code more excerpts (not realistic per Wayne) |
| C. Reframe | Present as "proof of concept" not findings |

**Recommended:** Option A
- Focus main findings on Source Hierarchy (κ=0.47, validated) and Naming Dispute (frequent)
- Move low-N constructs to "Exploratory Observations" subsection
- Explicitly state: "Insufficient data for reliable conclusions on testimonial injustice, policy weaponization"

**Action items:**
1. Reorganize Section 4.2.2 into "Primary Findings" and "Exploratory Observations"
2. Revise claims to weight toward high-reliability constructs

---

### 2.2 Address Temporal Asymmetry

**Problem:** Iran (1 week) vs Gaza (2.5 years) not comparable.

**Solution:** Theorize the difference rather than treating as limitation.

**New framing:**
- Iran = acute conflict dynamics (initial framing contests, breaking news)
- Gaza = chronic conflict dynamics (established narratives, entrenched camps)
- Structural similarity (41-43% reverters) despite temporal difference suggests platform affordances drive patterns

**Action items:**
1. Add paragraph in Section 4.3 theorizing temporal difference
2. Reframe RQ3 findings as "structural isomorphism despite temporal divergence"

---

### 2.3 Add Visualization

**Problem:** GLM requests network diagrams.

**Solution:** Create 2-3 figures:
1. Revert network diagram (one per cluster) showing role distribution
2. Inter-model agreement heatmap
3. (Optional) Temporal pattern of reverts

**Action items:**
1. Generate network visualizations using existing data
2. Add Figure captions and integrate into text

---

## Priority 3: Nice to Have

### 3.1 Expand Model Justification

**Why Claude + GLM + Kimi?**
- Claude: Western, safety-focused, conservative coding
- GLM: Chinese, different training corpus, state-adjacent
- Kimi: Chinese, strong multilingual, consumer-focused

Add 1-2 sentences in Section 3.4.3 explaining rationale.

### 3.2 Report Confidence Intervals

Add 95% CIs to proportion estimates (41.4% ± X%).

### 3.3 Ethics Statement

Add brief ethics note:
- Wikipedia data is public
- No IRB required for public data analysis
- Editor pseudonyms preserved

---

## Revised Paper Structure

```
1. Introduction (revised claims)
2. Theoretical Framework
   2.1 Epistemic Injustice (existing)
   2.2 Extensions to Platform Contexts (existing)
   2.3 Wikipedia's Editorial Structure (existing)
   2.4 From Identity to Credentials: Platform-Specific Theory (NEW)
   2.5 Research Questions (existing)
3. Methods (add visualization, ethics note)
4. Findings
   4.1 Revert Network Structure (add comparison to baseline)
   4.2 Talk Page Discourse
       4.2.1 Inter-Model Agreement (existing)
       4.2.2 Primary Findings: Source Hierarchy & Naming (revised)
       4.2.3 Exploratory Observations (moved low-N constructs)
       4.2.4 Network-Discourse Integration (NEW)
   4.3 Cross-Cluster Comparison (add temporal theorization)
5. Discussion
   5.1 What We Found (existing)
   5.2 Credential-Based Epistemic Authority (NEW framing)
   5.3 When Does Governance Become Injustice? (NEW)
   5.4 Alternative Explanations (existing, condensed)
   5.5 Multi-Model Coding as Construct Validation (existing)
   5.6 Limitations (existing)
6. Conclusion (revised claims)
```

---

## Implementation Timeline

| Task | Effort | Dependency |
|------|--------|------------|
| 1.1 Baseline comparison | 2-3 hrs | Literature search |
| 1.2 Theory development | 3-4 hrs | None |
| 1.3 Method integration | 2-3 hrs | Data analysis |
| 2.1 Reorg low-N constructs | 1 hr | None |
| 2.2 Temporal theorization | 1 hr | None |
| 2.3 Visualizations | 2 hrs | Data |
| 3.x Minor fixes | 1 hr | None |

**Total estimated:** 12-15 hours

---

## Key Claims After Revision

**Before (v2):**
> "We find asymmetric revert structures and evidence of contestation... Whether these patterns constitute 'epistemic injustice' remains an open question."

**After (v3):**
> "We find asymmetric revert structures consistent with Wikipedia's credential-based epistemic authority system. Source hierarchy debates emerged as a cross-culturally stable form of contestation (κ=0.47), while other epistemic injustice constructs showed systematic interpretive divergence across Western and Chinese-trained models. We propose that platform epistemics operate through credential-based authority rather than identity-based prejudice, creating a continuum from legitimate governance to exclusionary credentialism. Our multi-model coding approach offers a new method for identifying which social concepts are culturally robust versus culturally contested."

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `PREPRINT_v3.md` | Full revision |
| `figures/revert_network_iran.png` | New |
| `figures/revert_network_gaza.png` | New |
| `figures/agreement_heatmap.png` | New |
| `analysis/network_discourse_mapping.json` | New analysis |

---

*Plan created: March 6, 2026*
