# CommDAAF Improvement Plan
*Based on Feb 17, 2026 Red-Teaming Session*

---

## Guiding Principle

Every improvement should be:
- **Platform-agnostic** — works for Twitter, Reddit, TikTok, YouTube, surveys, etc.
- **Method-agnostic** — applies to sentiment, networks, topics, content analysis, etc.
- **Transferable** — teaches methodological thinking, not project-specific fixes

---

## Priority 1: Sample Balance Checks

### Problem Identified
Analysis proceeded with severely imbalanced comparison groups (one group had 0.3% of data).

### General Principle
**Before comparing groups, verify each group has sufficient observations for valid inference.**

### Implementation
Add to `critical-checks.md`:
```yaml
sample_balance_check:
  trigger: any comparison across groups (time periods, categories, conditions)
  
  question: |
    Do all comparison groups have sufficient observations?
    
    Show distribution:
    | Group | N | % of Total | Sufficient? |
    
  flags:
    - "Any group with <5% of total observations"
    - "Any group with N < 30 (central limit concerns)"
    - "Ratio between largest and smallest group > 10:1"
  
  if_imbalanced:
    blocked: "Standard group comparisons (ANOVA, chi-square with expected <5)"
    instead_try:
      - "Collapse small groups into meaningful larger categories"
      - "Exclude insufficient groups and narrow scope of claims"
      - "Use regression with group as continuous/ordinal predictor"
      - "Report descriptive statistics only for small groups"
```

---

## Priority 2: Metric Comparability

### Problem Identified
Raw engagement counts compared across time periods without accounting for baseline differences (audience growth, platform changes).

### General Principle
**When comparing metrics across contexts, verify the baselines are comparable. If not, normalize or acknowledge.**

### Implementation
Add to `critical-checks.md`:
```yaml
metric_comparability:
  trigger: comparing counts/rates across time, accounts, platforms, or conditions
  
  question: |
    Are your metrics comparable across comparison units?
    
    Baselines may differ due to:
    - Audience size changes over time
    - Platform algorithm or feature changes
    - Seasonal or cyclical patterns
    - Different data collection methods
    
  if_baselines_differ:
    blocked: "Direct comparison of raw values"
    instead_try:
      - "Rate metrics (per capita, per follower, per post)"
      - "Relative measures (percentile within time period)"
      - "Include baseline as control variable"
      - "Log-transform to reduce scale effects"
      - "Binary outcome (above/below threshold)"
      
  required: |
    State explicitly:
    - What baselines might differ
    - How you're handling it (normalizing OR acknowledging as limitation)
```

---

## Priority 3: Platform/Context Change Documentation

### Problem Identified
Data spanned periods with major platform changes that could confound findings, but these weren't documented or controlled.

### General Principle
**Identify external changes during your study period that could affect your variables. Document and address them.**

### Implementation
Add to `workflows/preflight.md`:
```yaml
context_changes:
  trigger: any longitudinal or time-series analysis
  
  question: |
    What changed in your research context during the study period?
    
    Consider:
    - Platform features, algorithms, or policies
    - Major external events (elections, crises, viral moments)
    - Data collection method changes
    - Population/community changes
    
  required:
    - "List known changes with approximate dates"
    - "For each: Could it affect your variables? How?"
    
  if_changes_present:
    options:
      - "Include as control/moderator in analysis"
      - "Subset data to single-context period"
      - "Test for structural breaks"
      - "Acknowledge as limitation with direction of potential bias"
```

---

## Priority 4: Effect Size Interpretation

### Problem Identified
Effect size reported as "large" when standard thresholds classify it as "medium."

### General Principle
**Use standard thresholds for effect size interpretation. Report the category explicitly, don't round up.**

### Implementation
Add to `critical-checks.md`:
```yaml
effect_size_reporting:
  trigger: any statistical test with effect size
  
  required: |
    1. Report the effect size value
    2. State the metric used (d, r, η², δ, etc.)
    3. Classify using standard thresholds:
    
    | Metric | Small | Medium | Large |
    |--------|-------|--------|-------|
    | Cohen's d | 0.2 | 0.5 | 0.8 |
    | Pearson/Spearman r | 0.1 | 0.3 | 0.5 |
    | Cliff's δ | 0.15 | 0.33 | 0.47 |
    | η² (eta-squared) | 0.01 | 0.06 | 0.14 |
    | Odds ratio | 1.5 | 2.5 | 4.0 |
    
  warning: |
    Effect sizes near boundaries should be described conservatively.
    - 0.32 correlation is "medium" not "medium-to-large"
    - When in doubt, use the lower category
```

---

## Priority 5: Directional Consistency

### Problem Identified  
Reported a negative correlation but interpreted it as a positive relationship.

### General Principle
**Verify that your statistical result's direction matches your verbal interpretation.**

### Implementation
Add to `critical-checks.md`:
```yaml
directional_consistency:
  trigger: any correlation, regression coefficient, or group difference
  
  verification: |
    Before writing interpretation, confirm:
    
    CORRELATIONS:
    - Positive r/ρ → "as X increases, Y increases"
    - Negative r/ρ → "as X increases, Y decreases"
    
    GROUP COMPARISONS:
    - Group A mean > Group B mean → "A has higher Y than B"
    - Check which group is which in your code
    
    REGRESSION:
    - Positive β → "unit increase in X associated with β increase in Y"
    - Negative β → "unit increase in X associated with β decrease in Y"
    
  checkpoint: |
    [ ] I have verified the sign/direction in my output
    [ ] My verbal interpretation matches the statistical direction
    [ ] I have not confused comparison group order
```

---

## Priority 6: Confound Awareness

### Problem Identified
Attributed outcome differences to one variable without controlling for co-varying content features.

### General Principle
**Identify variables that co-vary with your predictor and could alternatively explain your outcome.**

### Implementation
Add to `workflows/critical-checks.md`:
```yaml
confound_identification:
  trigger: any analysis claiming X relates to Y
  
  question: |
    What else varies with X that could explain Y?
    
    Common confounds in communication research:
    - Content features (length, media, formatting)
    - Source characteristics (popularity, verification, history)
    - Temporal factors (time of day, day of week, season)
    - Audience factors (demographics, prior engagement)
    - Platform factors (algorithm exposure, feature availability)
    
  required:
    - "List 3+ potential confounds"
    - "For each: Do you have data to control for it?"
    
  if_cannot_control:
    instead_try:
      - "Stratify analysis (examine relationship within subgroups)"
      - "Match cases on confounders"
      - "Acknowledge specific confounds as limitations"
      - "Narrow claims to association, not effect"
```

---

## Priority 7: Multiple Testing Awareness

### Problem Identified
Multiple statistical tests run without correction or acknowledgment.

### General Principle
**When running multiple tests, account for inflated false positive risk.**

### Implementation
Add to `methods/` skills where multiple tests are common:
```yaml
multiple_testing:
  trigger: >2 statistical tests in analysis
  
  context: |
    False positive risk with multiple tests (α = 0.05):
    - 3 tests → 14% chance of at least one false positive
    - 5 tests → 23%
    - 10 tests → 40%
    
  options:
    correction:
      - "Bonferroni: α/n (conservative)"
      - "FDR/Benjamini-Hochberg (less conservative)"
      - "Holm-Bonferroni (step-down)"
    
    design:
      - "Pre-specify one primary test, label others exploratory"
      - "Use omnibus test first, post-hocs only if significant"
    
    transparency:
      - "Report all tests run, not just significant ones"
      - "Label analysis as exploratory if many tests"
```

---

## Implementation Checklist

### Week 1
- [ ] Add sample balance check to `critical-checks.md`
- [ ] Add metric comparability check to `critical-checks.md`
- [ ] Add effect size reference table to `critical-checks.md`
- [ ] Add directional consistency checkpoint to `critical-checks.md`

### Week 2
- [ ] Add context change documentation to `preflight.md`
- [ ] Add confound identification to `critical-checks.md`
- [ ] Add multiple testing awareness to method skills

### Week 3
- [ ] Run AgentAcademy session to verify improvements work
- [ ] Refine based on what still gets missed

---

## Success Criteria

These improvements work if:
1. A researcher using ANY platform data gets the same methodological guidance
2. The checks catch issues through general principles, not pattern-matching specific datasets
3. The "instead, try" alternatives are applicable across research contexts
4. Next AgentAcademy session scores B+ or higher

---

*Plan revised: Feb 17, 2026*
*Principle: Teach transferable methodology, not project-specific fixes*
