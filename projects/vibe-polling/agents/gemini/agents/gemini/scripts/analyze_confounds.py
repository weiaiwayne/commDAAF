
import pandas as pd
import numpy as np
from scipy import stats
import os

def analyze_confounds():
    """Check for autocorrelation and platform effects."""
    processed_dir = "agents/gemini/data/processed"
    merged_file = f"{processed_dir}/merged_timeseries.parquet"
    
    if not os.path.exists(merged_file):
        print("Merged timeseries not found.")
        return
    
    df = pd.read_parquet(merged_file)
    
    # Check for autocorrelation in House Odds
    market_df = df[['date', 'house_dem_odds']].drop_duplicates().dropna()
    
    # Simple check: Correlation of series with its 1-day lag
    acf_market = market_df['house_dem_odds'].autocorr(lag=1)
    
    # Check for time trend
    market_df['days'] = (market_df['date'] - market_df['date'].min()).dt.days
    slope, intercept, r_val, p_val, std_err = stats.linregress(market_df['days'], market_df['house_dem_odds'])
    
    with open("agents/gemini/confound_analysis.md", 'w') as f:
        f.write("# Confound Analysis — VibePoll-2026\n\n")
        f.write(f"## Autocorrleation\n")
        f.write(f"- Market Odds 1-day Autocorrelation: {acf_market:.3f}\n")
        if acf_market > 0.8:
            f.write("  ⚠️ High autocorrelation detected. Series may have a unit root. Use first differences for correlation.\n")
            
        f.write(f"\n## Time Trend\n")
        f.write(f"- Linear Trend Slope: {slope:.6f} per day\n")
        f.write(f"- p-value: {p_val:.6f}\n")
        if p_val < 0.05:
            f.write("  ⚠️ Significant time trend detected. Spurious correlations possible due to common trending.\n")

        f.write(f"\n## Differenced Correlation Check (All States)\n")
        f.write("State | Raw r | Differenced r | Drop | Likely Spurious\n")
        f.write("---|---|---|---|---\n")
        
        for state in df['state'].unique():
            state_df = df[df['state'] == state].dropna(subset=['vibe_index', 'house_dem_odds']).copy()
            
            # Apply 7-day rolling average to smooth high-frequency noise before differencing
            state_df['vibe_smoothed'] = state_df['vibe_index'].rolling(window=7, min_periods=1).mean()
            state_df['odds_smoothed'] = state_df['house_dem_odds'].rolling(window=7, min_periods=1).mean()
            
            if len(state_df) > 5:
                # Raw correlation (on smoothed data to be fair)
                r_raw, _ = stats.pearsonr(state_df['vibe_smoothed'], state_df['odds_smoothed'])
                
                # First-differenced correlation on smoothed data
                diff_vibe = state_df['vibe_smoothed'].diff().dropna()
                diff_odds = state_df['odds_smoothed'].diff().dropna()
                if len(diff_vibe) > 5:
                    r_diff, _ = stats.pearsonr(diff_vibe, diff_odds)
                    drop = r_raw - r_diff
                    spurious = abs(drop) > 0.3
                    
                    f.write(f"{state} | {r_raw:.3f} | {r_diff:.3f} | {drop:.3f} | {'⚠️ Yes' if spurious else 'No'}\n")

    print("Confound analysis complete.")

if __name__ == "__main__":
    analyze_confounds()
