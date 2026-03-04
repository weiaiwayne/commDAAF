# Cross-Context Comparative Analysis
## Protest (#MahsaAmini) vs War (Ukraine)

**Date:** 2026-03-04
**Total N:** 719 (380 protest + 339 war)
**Coded by:** Claude Opus 4.5 (GLM/Kimi validation pending)

---

## Key Finding: Context Shapes Framing

**Frame × Context Association: χ²=236.09, p<0.001**

| Frame | Protest | War | Interpretation |
|-------|---------|-----|----------------|
| SOLIDARITY | **34.2%** | 8.8% | Protest = collective identity |
| INFORMATIONAL | 8.4% | **56.6%** | War = news reporting |
| CALL_TO_ACTION | **18.9%** | 3.5% | Protest = mobilization |
| INJUSTICE | 11.1% | 13.0% | Similar across contexts |

**Theoretical Implication:** Frame prevalence is context-dependent. Protest discourse emphasizes solidarity and mobilization; war discourse emphasizes information.

---

## RQ1: Does Diaspora/Language Effect Generalize?

### Protest Context
- English: mean=2.81, n=87
- Persian: mean=1.90, n=263
- **Δ = +0.91, t=3.08, p=0.002** ✅ CONFIRMED

### War Context
- English: mean=1.73, n=298
- Persian: mean=5.97, n=1 (!)
- **Cannot test** — only 1 Persian post in Ukraine sample

### Conclusion
Language/diaspora effect **confirmed in protest context** but **untestable in war context** due to sample composition. The Ukraine sample is 88% English — a different population, not a replication opportunity.

---

## RQ2: Does INFORMATIONAL Frame Effect Generalize?

### Previous Claim
#MahsaAmini study found INFORMATIONAL frame → IRR=2.72 (highest engagement).

### Cross-Context Test

| Context | INFORMATIONAL vs Others | p-value |
|---------|------------------------|---------|
| Protest | -0.03 (no difference) | 0.94 |
| War | **-0.47** (WORSE) | 0.04 |

### Regression: engagement ~ INFORMATIONAL * Context

| Variable | β | p |
|----------|---|---|
| INFORMATIONAL | -0.47 | 0.058 |
| PROTEST | +0.05 | 0.840 |
| INFORMATIONAL × PROTEST | +0.44 | 0.365 |

**Interpretation:** The interaction is not significant, meaning INFORMATIONAL's effect doesn't differ between contexts. But the MAIN effect of INFORMATIONAL is negative (β=-0.47), suggesting INFORMATIONAL posts get LESS engagement, not more.

### Why Does This Contradict Earlier Finding?
1. **Model specification:** Earlier study used Negative Binomial with controls; this uses simple t-test
2. **Confounding:** INFORMATIONAL may correlate with other engagement predictors
3. **Sampling:** Different samples within same dataset

### Conclusion
The "INFORMATIONAL wins" finding **does not replicate** in either context using simple comparison. The earlier IRR=2.72 may be model-dependent or confounded.

---

## RQ3: Frame Effectiveness by Context

| Frame | Protest Eng | War Eng | Which context benefits? |
|-------|-------------|---------|------------------------|
| CALL_TO_ACTION | 1.80 | 3.16 | **War (+1.36)** |
| CONFLICT | 3.01 | 2.25 | **Protest (+0.76)** |
| HOPE | 2.20 | 2.34 | Similar |
| HUMANITARIAN | 1.79 | 1.27 | **Protest (+0.52)** |
| INFORMATIONAL | 2.02 | 1.54 | **Protest (+0.48)** |
| INJUSTICE | 2.69 | 1.95 | **Protest (+0.74)** |
| SOLIDARITY | 1.82 | 1.47 | **Protest (+0.35)** |

**Observation:** Most frames perform better in protest context, except CALL_TO_ACTION which performs better in war context.

**Theoretical Implication:** War context has lower overall engagement. The single frame that outperforms (CALL_TO_ACTION) may reflect urgent appeals for support/donations.

---

## Limitations

1. **Ukraine sample heavily English (88%)** — Cannot test language effects
2. **Different time periods** — June-Oct 2022 for both, but different events
3. **Claude coding only** — GLM/Kimi validation pending
4. **No account-level controls** — Follower count, verification not included

---

## Revised Conclusions

### What Holds
1. **Context shapes frame prevalence** — Protest ≠ War
2. **Diaspora/language effect exists in protest** — English > Persian

### What Doesn't Hold
1. **"INFORMATIONAL wins" doesn't generalize** — Not supported in cross-context analysis
2. **Cannot test diaspora effect in war** — Sample is homogeneously English

### Implications for CommDAAF
- Add **context as mandatory variable** in cross-dataset studies
- Add **language composition check** before testing diaspora effects
- Require **simple comparison + regression** to validate frame effects

---

*Analysis conducted by Claude Opus 4.5. Awaiting GLM/Kimi validation of Ukraine codings.*
