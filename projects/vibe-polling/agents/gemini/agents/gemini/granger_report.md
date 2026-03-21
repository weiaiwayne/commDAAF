# Granger Causality Report — VibePoll-2026

      State                    Pair  Best Lag  F-statistic  P-value  Granger Causes
      US-AZ Vibe Index → House Odds         4     5.565652 0.000440            True
      US-AZ House Odds → Vibe Index         5     3.192186 0.010399            True
      US-CA Vibe Index → House Odds         7     0.639358 0.722205           False
      US-CA House Odds → Vibe Index         1     0.364002 0.547557           False
      US-GA Vibe Index → House Odds         3     1.337049 0.266537           False
      US-GA House Odds → Vibe Index         1     6.475023 0.012353            True
      US-ME Vibe Index → House Odds         4     0.375974 0.825300           False
      US-ME House Odds → Vibe Index         1     0.567153 0.453031           False
      US-MI Vibe Index → House Odds         7     2.315214 0.032263            True
      US-MI House Odds → Vibe Index         5     0.723111 0.607700           False
      US-MN Vibe Index → House Odds         3     0.653816 0.582366           False
      US-MN House Odds → Vibe Index         5     1.602566 0.166750           False
US-NATIONAL Vibe Index → House Odds         4     1.877557 0.120324           False
US-NATIONAL House Odds → Vibe Index         1     4.111946 0.045043            True
      US-NC Vibe Index → House Odds         2     2.389969 0.096601           False
      US-NC House Odds → Vibe Index         2     1.365474 0.259754           False
      US-NH Vibe Index → House Odds         1     0.869427 0.353194           False
      US-NH House Odds → Vibe Index         3     1.251210 0.295233           False
      US-NV Vibe Index → House Odds         1     0.330850 0.566356           False
      US-NV House Odds → Vibe Index         4     1.771715 0.140553           False
      US-OH Vibe Index → House Odds         4     0.328627 0.858150           False
      US-OH House Odds → Vibe Index         2     0.538889 0.585001           False
      US-PA Vibe Index → House Odds         1     2.028077 0.157299           False
      US-PA House Odds → Vibe Index         4     7.811904 0.000016            True
      US-TX Vibe Index → House Odds         4     1.032089 0.394610           False
      US-TX House Odds → Vibe Index         5     1.136073 0.346681           False
      US-WI Vibe Index → House Odds         3     1.900633 0.134210           False
      US-WI House Odds → Vibe Index         2     2.758238 0.068002           False

## Caveats
- Granger causality tests whether past values of X predict Y better than past values of Y alone.
- Analysis performed on first-differenced data to ensure stationarity.
- Max lag tested: 7 days.
