
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
import os
import json

def analyze_granger():
    """Test Granger causality between Trends and Markets."""
    processed_dir = "agents/gemini/data/processed"
    merged_file = f"{processed_dir}/merged_timeseries.parquet"
    
    if not os.path.exists(merged_file):
        print("Merged timeseries not found.")
        return
    
    df = pd.read_parquet(merged_file)
    
    results_list = []
    
    # Test for each state
    for state in df['state'].unique():
        state_df = df[df['state'] == state].dropna(subset=['vibe_index', 'house_dem_odds']).copy()
        
        if len(state_df) > 20:
            # Apply 7-day rolling average to smooth high-frequency noise before differencing
            state_df['vibe_smoothed'] = state_df['vibe_index'].rolling(window=7, min_periods=1).mean()
            state_df['odds_smoothed'] = state_df['house_dem_odds'].rolling(window=7, min_periods=1).mean()
            
            # We need stationary data for Granger. Let's use first differences of the smoothed data.
            data = state_df[['odds_smoothed', 'vibe_smoothed']].diff().dropna()
            
            try:
                # Test at lags 1 to 7
                res = grangercausalitytests(data, maxlag=7, verbose=False)
                
                # Find the lag with smallest p-value
                min_p = 1.0
                best_lag = 0
                f_stat = 0
                
                for lag, result in res.items():
                    # ssr_ftest is [f_stat, p_val, df_denom, df_num]
                    p = result[0]['ssr_ftest'][1]
                    if p < min_p:
                        min_p = p
                        best_lag = lag
                        f_stat = result[0]['ssr_ftest'][0]
                
                results_list.append({
                    'State': state,
                    'Pair': 'Vibe Index → House Odds',
                    'Best Lag': int(best_lag),
                    'F-statistic': float(f_stat),
                    'P-value': float(min_p),
                    'Granger Causes': min_p < 0.05
                })
                
                # Reverse direction (House Odds -> Vibe Index)
                data_reverse = state_df[['vibe_smoothed', 'odds_smoothed']].diff().dropna()
                res_reverse = grangercausalitytests(data_reverse, maxlag=7, verbose=False)
                
                min_p_r = 1.0
                best_lag_r = 0
                f_stat_r = 0
                
                for lag, result in res_reverse.items():
                    p = result[0]['ssr_ftest'][1]
                    if p < min_p_r:
                        min_p_r = p
                        best_lag_r = lag
                        f_stat_r = result[0]['ssr_ftest'][0]
                        
                results_list.append({
                    'State': state,
                    'Pair': 'House Odds → Vibe Index',
                    'Best Lag': int(best_lag_r),
                    'F-statistic': float(f_stat_r),
                    'P-value': float(min_p_r),
                    'Granger Causes': min_p_r < 0.05
                })
                
            except Exception as e:
                print(f"Granger test failed for {state}: {e}")

    results_df = pd.DataFrame(results_list)
    os.makedirs("agents/gemini/analysis/correlations", exist_ok=True)
    
    # Save as JSON for programmatic use
    results_df.to_json("agents/gemini/analysis/correlations/granger_results.json", orient='records', indent=2)
    
    # Save report
    with open("agents/gemini/granger_report.md", 'w') as f:
        f.write("# Granger Causality Report — VibePoll-2026\n\n")
        f.write(results_df.to_string(index=False))
        f.write("\n\n## Caveats\n")
        f.write("- Granger causality tests whether past values of X predict Y better than past values of Y alone.\n")
        f.write("- Analysis performed on first-differenced data to ensure stationarity.\n")
        f.write("- Max lag tested: 7 days.\n")
    
    print("Granger causality analysis complete.")

if __name__ == "__main__":
    analyze_granger()
