# Comprehensive Statistical Modeling Results

**Agent:** Kimi K2.5  
**Framework:** CommDAAF v1.0  
**Date:** 2026-03-19  
**States:** All 7 battlegrounds + 3 controls + 3 watch  

## Battleground States Analyzed

**Tier 1:** PA, MI, WI, AZ, GA  
**Tier 2:** NV, NC  
**Control:** CA, TX, OH  

## Pooled Battleground vs Control

- **N:** 58,695  
- **IRR (Battleground effect):** 0.765  
- **95% CI:** 0.751 - 0.779  
- **p-value:** 0.0000  

**Interpretation:** Battleground states show 23.5% lower search interest than control states.  

## Individual State Effects (vs California)

### ECONOMY

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 0.919 | 0.846-0.999 | 0.0467* | -8.1% vs CA |
| GA | 0.906 | 0.834-0.984 | 0.0193* | -9.4% vs CA |
| NC | 0.898 | 0.827-0.976 | 0.0112* | -10.2% vs CA |
| MI | 0.835 | 0.768-0.907 | 0.0000*** | -16.5% vs CA |
| AZ | 0.813 | 0.748-0.883 | 0.0000*** | -18.7% vs CA |
| NV | 0.703 | 0.646-0.763 | 0.0000*** | -29.7% vs CA |
| WI | 0.668 | 0.615-0.726 | 0.0000*** | -33.2% vs CA |

### IMMIGRATION

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 0.830 | 0.758-0.907 | 0.0000*** | -17.0% vs CA |
| GA | 0.768 | 0.702-0.840 | 0.0000*** | -23.2% vs CA |
| NC | 0.710 | 0.649-0.777 | 0.0000*** | -29.0% vs CA |
| MI | 0.696 | 0.636-0.761 | 0.0000*** | -30.4% vs CA |
| AZ | 0.534 | 0.488-0.585 | 0.0000*** | -46.6% vs CA |
| WI | 0.475 | 0.434-0.520 | 0.0000*** | -52.5% vs CA |
| NV | 0.243 | 0.222-0.267 | 0.0000*** | -75.7% vs CA |

### IRAN_WAR

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 0.879 | 0.783-0.986 | 0.0276* | -12.1% vs CA |
| GA | 0.809 | 0.720-0.909 | 0.0003*** | -19.1% vs CA |
| AZ | 0.730 | 0.649-0.821 | 0.0000*** | -27.0% vs CA |
| NC | 0.704 | 0.626-0.792 | 0.0000*** | -29.6% vs CA |
| MI | 0.675 | 0.600-0.760 | 0.0000*** | -32.5% vs CA |
| WI | 0.561 | 0.497-0.633 | 0.0000*** | -43.9% vs CA |
| NV | 0.533 | 0.472-0.601 | 0.0000*** | -46.7% vs CA |

### AI_JOBS

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| GA | 0.709 | 0.645-0.780 | 0.0000*** | -29.1% vs CA |
| PA | 0.700 | 0.636-0.769 | 0.0000*** | -30.0% vs CA |
| NC | 0.655 | 0.596-0.720 | 0.0000*** | -34.5% vs CA |
| MI | 0.495 | 0.450-0.545 | 0.0000*** | -50.5% vs CA |
| AZ | 0.490 | 0.446-0.539 | 0.0000*** | -51.0% vs CA |
| NV | 0.424 | 0.385-0.467 | 0.0000*** | -57.6% vs CA |
| WI | 0.410 | 0.372-0.451 | 0.0000*** | -59.0% vs CA |

### EPSTEIN

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 1.045 | 0.910-1.199 | 0.5338 | +4.5% vs CA |
| MI | 1.027 | 0.895-1.179 | 0.7010 | +2.7% vs CA |
| GA | 1.010 | 0.880-1.160 | 0.8853 | +1.0% vs CA |
| NC | 0.974 | 0.848-1.118 | 0.7075 | -2.6% vs CA |
| AZ | 0.949 | 0.826-1.089 | 0.4541 | -5.1% vs CA |
| WI | 0.931 | 0.811-1.070 | 0.3142 | -6.9% vs CA |
| NV | 0.896 | 0.780-1.029 | 0.1211 | -10.4% vs CA |

### POLITICAL

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 0.806 | 0.715-0.910 | 0.0005*** | -19.4% vs CA |
| GA | 0.624 | 0.553-0.704 | 0.0000*** | -37.6% vs CA |
| MI | 0.518 | 0.459-0.585 | 0.0000*** | -48.2% vs CA |
| AZ | 0.451 | 0.400-0.510 | 0.0000*** | -54.9% vs CA |
| WI | 0.323 | 0.286-0.366 | 0.0000*** | -67.7% vs CA |
| NC | 0.281 | 0.248-0.318 | 0.0000*** | -71.9% vs CA |
| NV | 0.121 | 0.107-0.138 | 0.0000*** | -87.9% vs CA |

### PARTISAN_PAIRS

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| PA | 1.073 | 0.972-1.185 | 0.1632 | +7.3% vs CA |
| MI | 1.023 | 0.926-1.130 | 0.6545 | +2.3% vs CA |
| NC | 0.974 | 0.882-1.076 | 0.6017 | -2.6% vs CA |
| AZ | 0.934 | 0.845-1.031 | 0.1763 | -6.6% vs CA |
| WI | 0.911 | 0.825-1.007 | 0.0674 | -8.9% vs CA |
| GA | 0.907 | 0.821-1.002 | 0.0552 | -9.3% vs CA |
| NV | 0.742 | 0.672-0.820 | 0.0000*** | -25.8% vs CA |

### STATE_SPECIFIC

| State | IRR | 95% CI | p-value | Interpretation |
|-------|-----|--------|---------|----------------|
| MI | 5.191 | 4.605-5.851 | 0.0000*** | +419.1% vs CA |
| GA | 2.777 | 2.452-3.144 | 0.0000*** | +177.7% vs CA |
| PA | 1.957 | 1.720-2.226 | 0.0000*** | +95.7% vs CA |
| AZ | 1.832 | 1.607-2.088 | 0.0000*** | +83.2% vs CA |
| WI | 0.005 | 0.002-0.012 | 0.0000*** | -99.5% vs CA |

## Issue Salience Rankings by State

| State | Top Issue | Avg Interest | 2nd Issue | 3rd Issue |
|-------|-----------|--------------|-----------|-----------|
| AZ | partisan_pairs (17.7) | 17.7 | economy (15.4) | political (14.4) |
| CA | political (30.0) | 30.0 | immigration (23.8) | ai_jobs (19.6) |
| GA | political (19.4) | 19.4 | immigration (18.3) | economy (17.2) |
| MI | state_specific (27.6) | 27.6 | partisan_pairs (19.3) | immigration (16.5) |
| NC | partisan_pairs (18.4) | 18.4 | economy (17.1) | immigration (16.9) |
| NV | partisan_pairs (14.1) | 14.1 | economy (13.5) | ai_jobs (8.3) |
| PA | political (24.9) | 24.9 | partisan_pairs (20.3) | immigration (19.7) |
| WI | partisan_pairs (17.2) | 17.2 | economy (12.8) | immigration (11.4) |

