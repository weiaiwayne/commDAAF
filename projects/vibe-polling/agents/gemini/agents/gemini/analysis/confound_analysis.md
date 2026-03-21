# Confound Analysis — VibePoll-2026

## Autocorrleation
- Market Odds 1-day Autocorrelation: 0.949
  ⚠️ High autocorrelation detected. Series may have a unit root. Use first differences for correlation.

## Time Trend
- Linear Trend Slope: 0.000776 per day
- p-value: 0.000000
  ⚠️ Significant time trend detected. Spurious correlations possible due to common trending.

## Differenced Correlation Check (US-NH)
- Raw r: 0.568
- First-Differenced r: -0.193
  ⚠️ Correlation drops significantly after differencing. Original correlation may be driven by trends, not co-fluctuation.
