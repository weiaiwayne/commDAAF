# Granger Causality Report — VibePoll-2026

State                    Pair  Best Lag  F-statistic  P-value  Granger Causes
US-AZ Vibe Index → House Odds         5     0.494773 0.775998           False
US-CA Vibe Index → House Odds         5     1.599154 0.210856           False
US-GA Vibe Index → House Odds         7     0.325034 0.927958           False
US-ME Vibe Index → House Odds         1     0.118824 0.732718           False
US-MI Vibe Index → House Odds         5     0.752386 0.595168           False
US-MN Vibe Index → House Odds         5     0.656388 0.660743           False
US-NC Vibe Index → House Odds         2     0.744311 0.484559           False
US-NH Vibe Index → House Odds         1     0.212917 0.647819           False
US-NV Vibe Index → House Odds         1     0.395504 0.534180           False
US-OH Vibe Index → House Odds         1     0.069750 0.793508           False
US-PA Vibe Index → House Odds         7     1.110628 0.415927           False
US-TX Vibe Index → House Odds         5     0.387849 0.850624           False
US-WI Vibe Index → House Odds         1     0.193060 0.663531           False

## Caveats
- Granger causality tests whether past values of X predict Y better than past values of Y alone.
- Analysis performed on first-differenced data to ensure stationarity.
- Max lag tested: 7 days.
