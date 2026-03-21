
import pandas as pd
import numpy as np
from scipy import stats
import os

def calculate_fisher_ci(r, n):
    """Calculate 95% confidence interval for Pearson correlation using Fisher z-transform."""
    if n <= 3:
        return np.nan, np.nan
    z = np.arctanh(r)
    se = 1.0 / np.sqrt(n - 3)
    z_low = z - 1.96 * se
    z_high = z + 1.96 * se
    return np.tanh(z_low), np.tanh(z_high)

def analyze_concurrent():
    """Calculate concurrent correlations between Vibe Index and Market Odds."""
    processed_dir = "agents/gemini/data/processed"
    merged_file = f"{processed_dir}/merged_timeseries.parquet"
    
    if not os.path.exists(merged_file):
        print("Merged timeseries not found.")
        return
    
    df = pd.read_parquet(merged_file)
    
    # Pairs to analyze
    # Vibe Index (per state) vs House/Senate Odds
    results = []
    
    for state in df['state'].unique():
        state_df = df[df['state'] == state].dropna(subset=['vibe_index', 'house_dem_odds'])
        
        if len(state_df) > 5:
            # House Odds
            r, p = stats.pearsonr(state_df['vibe_index'], state_df['house_dem_odds'])
            ci_low, ci_high = calculate_fisher_ci(r, len(state_df))
            
            results.append({
                'Variable 1': f'Vibe Index ({state})',
                'Variable 2': 'House Dem Odds',
                'r': r,
                '95% CI_low': ci_low,
                '95% CI_high': ci_high,
                'p': p,
                'N': len(state_df),
                'Flag': '⚠️ r > 0.7' if abs(r) > 0.7 else ''
            })
            
            # Senate Odds
            if 'senate_dem_odds' in state_df.columns:
                state_df_senate = state_df.dropna(subset=['senate_dem_odds'])
                if len(state_df_senate) > 5:
                    r_s, p_s = stats.pearsonr(state_df_senate['vibe_index'], state_df_senate['senate_dem_odds'])
                    ci_l_s, ci_h_s = calculate_fisher_ci(r_s, len(state_df_senate))
                    
                    results.append({
                        'Variable 1': f'Vibe Index ({state})',
                        'Variable 2': 'Senate Dem Odds',
                        'r': r_s,
                        '95% CI_low': ci_l_s,
                        '95% CI_high': ci_h_s,
                        'p': p_s,
                        'N': len(state_df_senate),
                        'Flag': '⚠️ r > 0.7' if abs(r_s) > 0.7 else ''
                    })

    # Also analyze Issue Salience (aggregate across states) vs Markets
    salience_file = f"{processed_dir}/issue_salience.csv"
    salience_df = pd.read_csv(salience_file)
    salience_df['date'] = pd.to_datetime(salience_df['date'])
    
    # Merge with market data (need to get market data from process_markets or re-load)
    # Re-loading historical market odds
    market_df = pd.read_csv("agents/gemini/data/raw/markets/historical_market_odds.csv")
    market_df['date'] = pd.to_datetime(market_df['date'])
    
    avg_salience = salience_df.groupby(['date', 'category'])['zscore'].mean().reset_index()
    
    for cat in avg_salience['category'].unique():
        cat_df = avg_salience[avg_salience['category'] == cat].merge(market_df, on='date', how='inner').dropna()
        
        if len(cat_df) > 5:
            r, p = stats.pearsonr(cat_df['zscore'], cat_df['house_dem_odds'])
            ci_low, ci_high = calculate_fisher_ci(r, len(cat_df))
            
            results.append({
                'Variable 1': f'Salience ({cat})',
                'Variable 2': 'House Dem Odds',
                'r': r,
                '95% CI_low': ci_low,
                '95% CI_high': ci_high,
                'p': p,
                'N': len(cat_df),
                'Flag': '⚠️ r > 0.7' if abs(r) > 0.7 else ''
            })

    results_df = pd.DataFrame(results)
    os.makedirs("agents/gemini/analysis/correlations", exist_ok=True)
    results_df.to_csv("agents/gemini/analysis/correlations/concurrent_correlations.csv", index=False)
    
    # Generate MD report
    with open("agents/gemini/correlation_report.md", 'w') as f:
        f.write("# Correlation Report — VibePoll-2026\n\n")
        f.write("## Concurrent Correlations\n\n")
        f.write(results_df.to_string(index=False))
        f.write("\n\n## Analytical Decisions\n")
        f.write("- Pearson correlation used for all continuous series.\n")
        f.write("- 95% Confidence Intervals calculated using Fisher z-transform.\n")
        f.write("- Analysis performed at daily grain (taking last market price of day).\n")
    
    print("Concurrent correlation analysis complete.")

if __name__ == "__main__":
    analyze_concurrent()
