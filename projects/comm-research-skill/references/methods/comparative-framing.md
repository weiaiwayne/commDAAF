# Comparative Framing Analysis

*Lessons from Global South AI Framing Study (March 2026)*

## Effect Size Reporting

Always report effect sizes alongside significance tests:

```
| Frame | Group A | Group B | Diff | χ² | Cramér's V |
|-------|---------|---------|------|-----|-----------|
| X     | 22%     | 1%      | -21  | 24.1** | .32 |
```

**Cramér's V benchmarks** (Cohen, 1988):
- V = .10 → Small effect
- V = .30 → Medium effect  
- V = .50 → Large effect

## Multiple Comparisons

When testing multiple frames (e.g., 8 frames):
- Apply Bonferroni correction: α = .05/k
- Mark findings: ** survives correction, * does not
- Only make strong claims about ** findings

## Reliability Flagging

When per-frame κ < .60:
1. Flag with † in tables
2. Add footnote: "†Reliability κ = .XX; interpret with caution"
3. Caveat in Findings section
4. Note in Limitations

**Do NOT**: Bury reliability issues only in Methods section.

## Cross-National Document Comparability

Different countries = different document types:
- US congressional hearings ≠ Brazilian committee reports
- This is **inherent** to cross-national comparison
- Requires full subsection in Discussion, not just a sentence

**Template language**:
> "A significant limitation deserves direct acknowledgment: [Country A] data comprises [type] while [Country B] data comprises [type]. These document types have different rhetorical conventions that may independently affect framing patterns."

## Causal Claim Hedging

Cross-sectional observational data cannot establish causation.

**Avoid**:
- "X explains Y"
- "The divergence reflects..."
- "Because [country] is [status], they frame..."

**Use**:
- "X may reflect Y"
- "We propose—as a hypothesis—that..."
- "This hypothesis would predict..."
- "Testing requires additional cases"

## Small Sample Handling

When country N < 10:
- Report separately as "exploratory"
- Do not include in aggregate statistics
- Caveat: "findings should not be overgeneralized"

## Multi-Round Peer Review Workflow

1. **Round 1**: Two independent AI reviewers
   - Expect: Major Revision
   - Different models catch different issues:
     - GLM → Methods, statistics, replicability
     - Kimi → Theory, literature, conceptual coherence

2. **Address concerns**: Create detailed Response to Reviewers

3. **Round 2**: Same models re-review
   - Target: Minor Revision
   - If still Major → iterate

4. **Document everything**: All reviews + responses should be published with paper

## Adjudication Protocol

When resolving inter-coder disagreements:
1. Document criteria **prospectively** (before reviewing cases)
2. Apply criteria consistently
3. Report as "resolved disagreements" not "κ = 1.0"
4. Acknowledge: "some documents presented genuine ambiguity"

---

*Added to CommDAAF: March 2026*
*Source: Global South AI Framing Study (AgentAcademy)*
