
import pandas as pd
import numpy as np
from scipy import stats
import os
import matplotlib.pyplot as plt

def calculate_lag_correlations(series_x, series_y, max_lag=7):
    """Calculate correlation at various lags."""
    lags = range(-max_lag, max_lag + 1)
    corrs = []
    ps = []
    
    for lag in lags:
        if lag < 0:
            # y leads x or x lags y
            x_shifted = series_x.iloc[-lag:]
            y_aligned = series_y.iloc[:lag]
        elif lag > 0:
            # x leads y or y lags x
            x_shifted = series_x.iloc[:-lag]
            y_aligned = series_y.iloc[lag:]
        else:
            x_shifted = series_x
            y_aligned = series_y
            
        r, p = stats.pearsonr(x_shifted, y_aligned)
        corrs.append(r)
        ps.append(p)
        
    return lags, corrs, ps

def analyze_lags():
    """Identify optimal lead/lag relationships."""
    processed_dir = "agents/gemini/data/processed"
    merged_file = f"{processed_dir}/merged_timeseries.parquet"
    
    if not os.path.exists(merged_file):
        print("Merged timeseries not found.")
        return
    
    df = pd.read_parquet(merged_file)
    
    # Analyze state-level vibe vs market
    results = []
    
    for state in df['state'].unique():
        state_df = df[df['state'] == state].dropna(subset=['vibe_index', 'house_dem_odds'])
        
        if len(state_df) > 15:
            lags, corrs, ps = calculate_lag_correlations(state_df['vibe_index'], state_df['house_dem_odds'])
            
            # Find optimal lag (max absolute correlation)
            abs_corrs = [abs(c) for c in corrs]
            max_idx = np.argmax(abs_corrs)
            opt_lag = lags[max_idx]
            opt_r = corrs[max_idx]
            opt_p = ps[max_idx]
            
            results.append({
                'Pair': f'Vibe Index ({state}) ↔ House Odds',
                'Optimal Lag': opt_lag,
                'r at Optimal': opt_r,
                'p': opt_p,
                'Interpretation': 'Trends leads market' if opt_lag > 0 else 'Market leads trends' if opt_lag < 0 else 'Synchronous'
            })

    results_df = pd.DataFrame(results)
    os.makedirs("agents/gemini/analysis/correlations", exist_ok=True)
    results_df.to_csv("agents/gemini/analysis/correlations/lag_analysis.csv", index=False)
    
    # Save a summary report
    with open("agents/gemini/lag_report.md", 'w') as f:
        f.write("# Lag Analysis Report — VibePoll-2026\n\n")
        f.write(results_df.to_string(index=False))
        f.write("\n\n## Methodology\n")
        f.write("- Cross-correlation analysis performed at lags -7 to +7 days.\n")
        f.write("- Positive lag: Trends leads market (predictive signal).\n")
        f.write("- Negative lag: Market leads trends (reactive signal).\n")
    
    print("Lag analysis complete.")

if __name__ == "__main__":
    analyze_lags()
