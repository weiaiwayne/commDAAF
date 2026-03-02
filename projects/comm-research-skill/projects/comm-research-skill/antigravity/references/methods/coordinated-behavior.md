# Coordinated Behavior Detection

⚠️ **HIGH BAR METHOD** — Sensitive conclusions, requires extra rigor.

## Probing Questions (ALL REQUIRED — STRICT)

```
Q1: What behavior suggests 'coordination'?
    ✓ Same content within X seconds
    ✓ Same hashtags at same time
    ✓ Specific network pattern
    ✗ "They're working together" — NOT OPERATIONAL
    ✗ "Suspicious activity" — NOT MEASURABLE

Q2: How distinguish organic from coordinated?
    ✓ Baseline comparison (what's normal?)
    ✓ Statistical threshold with justification
    ✗ "It looks coordinated" — SUBJECTIVE
    ✗ "High similarity" — COMPARED TO WHAT?

Q3: What conclusions will you draw?
    ✓ "Accounts exhibit coordinated posting patterns"
    ✓ "Behavior consistent with automation"
    ✗ "These are bots" — CANNOT CONCLUDE
    ✗ "State-sponsored campaign" — REQUIRES MORE EVIDENCE

Q4: False positive tolerance?
    ✓ Define acceptable threshold
    ✓ Plan for manual review of flagged accounts
    ✗ "The model is accurate" — NOT YOUR DATA

Q5: Validation approach?
    ✓ Manual review of sample
    ✓ Comparison to known campaigns
    ✓ Cross-method validation
```

## What You CAN and CANNOT Conclude

### ✅ CAN Conclude
- Accounts show synchronized posting patterns
- Timing similarity exceeds organic baseline
- Content overlap statistically significant
- Network structure consistent with coordination

### ❌ CANNOT Conclude (Without Additional Evidence)
- These are "bots"
- This is a "state-sponsored campaign"
- Accounts are "inauthentic"
- Actors have malicious intent

## Methods

| Method | What It Detects | Limitation |
|--------|-----------------|------------|
| **Temporal similarity** | Same-time posting | Breaking news causes organic spikes |
| **Content similarity** | Shared text/URLs | Viral content spreads organically |
| **Network co-occurrence** | Same targets | Popular accounts get many mentions |
| **Behavioral fingerprinting** | Similar patterns | Legitimate tools create patterns |

## Baseline Requirements

You MUST establish:
1. What does ORGANIC behavior look like?
2. What threshold separates normal from suspicious?
3. What's your false positive rate on organic data?

## Critical Checks

- [ ] Operational definition documented
- [ ] Baseline comparison performed
- [ ] Conclusions limited to observed behavior
- [ ] Manual validation of flagged accounts
- [ ] Limitations clearly stated
