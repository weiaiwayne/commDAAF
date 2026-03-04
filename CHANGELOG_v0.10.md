# CommDAAF v0.10 Changelog
## Lessons from Autonomous RQ Generation Study (2026-03-04)

---

## New Features

### 1. Adversarial Peer Review Phase (REQUIRED)

**Location:** Add to `SKILL.md` after Phase 5 (Reliability Assessment)

```markdown
## Phase 6: Adversarial Peer Review

Before finalizing ANY study, require:

### 6.1 Multi-Model Critique
- Each participating model writes Reviewer 2 critique
- Critiques must be independent (no cross-reading)
- Minimum 3 perspectives for publication-tier

### 6.2 Critique Requirements
Each reviewer must identify:
- ≥3 methodological concerns
- ≥2 alternative explanations
- ≥1 confounding variable
- Specific claims that outrun evidence

### 6.3 Response Protocol
Create table:
| Critique | Response | Action Taken |

If critique CANNOT be addressed:
- Downgrade claim confidence
- Add to Limitations section
- Consider retracting claim

### 6.4 Verdict Thresholds
- "Accept" from all 3 → Proceed
- "Minor revision" majority → Fix and proceed
- "Major revision" from any → Must revise
- "Reject" from any → Retract or redesign
```

---

### 2. Multi-Label Frame Coding Option

**Location:** Add to `references/methods/frame-analysis.md`

```markdown
## Multi-Label Coding (v0.10)

For complex contexts (war, crisis, multi-issue movements):

### When to Use
- Inter-coder κ < 0.6 on single-label scheme
- Qualitative analysis shows consistent multi-frame posts
- Frame boundaries theoretically overlap

### Schema
| Field | Required | Description |
|-------|----------|-------------|
| PRIMARY_FRAME | Yes | Dominant frame |
| SECONDARY_FRAME | If applicable | Second frame present |
| FRAME_CONFIDENCE | Yes | HIGH/MEDIUM/LOW |

### Decision Hierarchy (for single-label fallback)
1. If INJUSTICE + any other → INJUSTICE (perpetrator takes precedence)
2. If CONFLICT + INFO → CONFLICT (action takes precedence)
3. If SOLIDARITY + INFO → SOLIDARITY (identity takes precedence)
4. If ambiguous → Code as INFO with MEDIUM confidence
```

---

### 3. Cross-Context Generalizability Check

**Location:** Add to `references/workflows/tiered-validation.md`

```markdown
## Cross-Context Requirement (v0.10)

For 🔴 PUBLICATION tier:
- Test findings in ≥2 contexts (e.g., protest + war)
- Report context × effect interactions
- If effect doesn't generalize → downgrade to context-specific claim

### Context Comparison Protocol
1. Code second dataset with same scheme
2. Test: Does effect replicate? (same direction, p<0.05)
3. Test interaction: context × predictor
4. If interaction significant → effect is context-dependent

### Claim Language
- ✅ "In protest contexts, X predicts Y"
- ❌ "X predicts Y" (implies universal)
```

---

### 4. Language Composition Check

**Location:** Add to `references/methods/content-analysis.md`

```markdown
## Language Audit (v0.10)

Before testing "diaspora" or "language" effects:

### Minimum Requirements
- ≥30 posts in each language being compared
- Report language distribution in Methods
- If <30 in any language → "Cannot test language effects"

### Sample Composition Table (Required)
| Language | N | % | Can Test? |
|----------|---|---|-----------|
| English | 298 | 88% | ✅ |
| Persian | 1 | 0.3% | ❌ |

If majority language >80% → Acknowledge homogeneous sample
```

---

### 5. Qualitative Disagreement Analysis

**Location:** Add to `references/workflows/reliability.md`

```markdown
## Disagreement Analysis (v0.10)

When inter-model κ < 0.7:

### Required Analysis
1. Identify top disagreement patterns (e.g., INFO→CONFLICT)
2. Pull 5 exemplar posts per pattern
3. Qualitative interpretation: WHY do models disagree?
4. Update coding scheme based on findings

### Documentation
Create `DISAGREEMENT_ANALYSIS.md`:
- Pattern counts
- Exemplar texts
- Theoretical interpretation
- Proposed scheme refinements
```

---

## Bug Fixes

### Issue: RQ2 Effectiveness Claimed Despite p>0.27
**Fix:** Add significance threshold check:
```
If p > 0.05 for primary comparison → CANNOT claim "supported"
Report as: "Direction consistent but not significant (p=X)"
```

### Issue: Small N Cells Reported as "High Confidence"
**Fix:** Add cell-size warning:
```
If any cell n < 10 → Flag in results
If any cell n < 30 → Cannot make inferential claims
```

### Issue: Inconsistent Validation (Study 1 = 3-model, Study 2 = 1-model)
**Fix:** Standardize:
```
🟢 EXPLORATORY: 1-model acceptable
🟡 PILOT: 2-model minimum
🔴 PUBLICATION: 3-model required
```

---

## Lessons Encoded

From this study, we learned:

1. **Autonomous RQ generation works** — AI can identify novel, literature-grounded questions
2. **Multi-model validation catches reliability issues** — κ=0.31 would have been missed by single-model
3. **Adversarial review is brutal but necessary** — 3 Reviewer 2s found ~20 major issues
4. **Cross-context comparison is essential** — "INFORMATIONAL wins" didn't generalize
5. **Qualitative analysis explains quantitative failures** — Disagreement patterns reveal scheme problems

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.10 | 2026-03-04 | Adversarial peer review, multi-label coding, cross-context checks |
| 0.9 | 2026-02-27 | AgentAcademy protocol, preprints |
| 0.8 | 2026-02-26 | Iran study improvements |

---

*Changelog generated from autonomous AgentAcademy study*
