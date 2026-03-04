# CLBD vs CooRnet Comparison

## Summary

**Overlap: 1.2%** — Methods detect almost entirely different suspicious accounts.

## Methodology Comparison

| Aspect | CooRnet | CLBD (Ours) |
|--------|---------|-------------|
| **Unit of analysis** | Pairs/groups of accounts | Individual accounts |
| **Detection signal** | Same content/sources shared | Behavioral discordance across layers |
| **Requires** | URL/content matching OR source tracking | Multi-layer network data |
| **Detects** | Coordinated amplification networks | Single-purpose amplifiers |
| **False positive risk** | Organic sharing of viral content | Legitimate users who RT news but talk to friends |

## Results on Ukraine Data (June 7-9, 2023)

### CooRnet-Style Detection
- Co-retweeting analysis (accounts that RT same sources)
- **2,426** sources retweeted by 5+ accounts
- **64M+** co-retweeting pairs
- **9,368** accounts flagged with co-RT score

Top CooRnet-flagged accounts:
| Username | Score | Pattern |
|----------|-------|---------|
| rclaussen2 | 13,895 | High co-RT overlap |
| onelhurtado2 | 11,625 | Previously flagged as amplifier |
| habirumo | 11,464 | High co-RT overlap |
| maylisa8919 | 10,159 | Previously flagged as amplifier |

### CLBD Detection
- Cross-layer behavioral discordance
- RT targets vs conversation targets overlap
- Multi-signal scoring (discordance + reciprocity + amplification + layer isolation)
- **165** high-confidence anomalies

### Overlap Analysis

| Set | Count |
|-----|-------|
| CLBD only | 163 |
| CooRnet only | 163 |
| **Both** | **2** |

Overlapping accounts: `joseperez1026`, `jooou_sama2`

## Interpretation

### Why Low Overlap?

1. **Different coordination types:** 
   - CooRnet catches coordinated groups
   - CLBD catches behavioral anomalies

2. **Different signals:**
   - CooRnet: "Do they amplify the same content?"
   - CLBD: "Is their behavior internally consistent?"

3. **Complementary detection:**
   - An account can be in a coordinated group but behave "normally" (RT + reply + quote same targets)
   - An account can be behaviorally discordant but not part of a coordinated group

### Novel Contribution Validated

The 1.2% overlap demonstrates that CLBD identifies a **distinct population** of suspicious accounts not captured by existing coordination detection methods.

## Recommended Combination

For comprehensive coordination detection:

1. **Run CooRnet** → Identify coordinated groups
2. **Run CLBD** → Identify individual behavioral anomalies
3. **Intersect results** → High-confidence coordination (accounts flagged by both)
4. **Union results** → Comprehensive suspicious account list

## Files

- `/tmp/ukr_coornet_style.csv` — CooRnet-style scores
- `/tmp/ukr_high_confidence_anomalies.csv` — CLBD anomalies
- `/tmp/ukr_clbd_vs_coornet.csv` — Comparison (not yet created)
