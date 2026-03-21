# Confound Analysis — VibePoll-2026

## Autocorrleation
- Market Odds 1-day Autocorrelation: 0.972
  ⚠️ High autocorrelation detected. Series may have a unit root. Use first differences for correlation.

## Time Trend
- Linear Trend Slope: 0.000913 per day
- p-value: 0.000000
  ⚠️ Significant time trend detected. Spurious correlations possible due to common trending.

## Differenced Correlation Check (All States)
State | Raw r | Differenced r | Drop | Likely Spurious
---|---|---|---|---
US-AZ | 0.288 | -0.245 | 0.532 | ⚠️ Yes
US-CA | 0.580 | 0.106 | 0.474 | ⚠️ Yes
US-GA | 0.255 | -0.086 | 0.342 | ⚠️ Yes
US-ME | 0.142 | -0.016 | 0.158 | No
US-MI | 0.403 | 0.088 | 0.316 | ⚠️ Yes
US-MN | 0.338 | 0.041 | 0.297 | No
US-NATIONAL | 0.497 | 0.281 | 0.216 | No
US-NC | 0.169 | 0.017 | 0.152 | No
US-NH | 0.214 | -0.011 | 0.226 | No
US-NV | 0.271 | -0.081 | 0.352 | ⚠️ Yes
US-OH | 0.404 | 0.012 | 0.392 | ⚠️ Yes
US-PA | 0.444 | 0.117 | 0.327 | ⚠️ Yes
US-TX | 0.422 | -0.035 | 0.457 | ⚠️ Yes
US-WI | 0.360 | 0.082 | 0.277 | No
