
import pandas as pd
import numpy as np
from scipy import stats
import os

def analyze_states():
    """Compare battleground vs control states."""
    processed_dir = "agents/gemini/data/processed"
    vibe_file = f"{processed_dir}/vibe_indices.csv"
    salience_file = f"{processed_dir}/issue_salience.csv"
    
    if not os.path.exists(vibe_file):
        print("Data files not found.")
        return
    
    vibe_df = pd.read_csv(vibe_file)
    salience_df = pd.read_csv(salience_file)
    
    # Define state categories
    battleground = ['US-PA', 'US-MI', 'US-WI', 'US-AZ', 'US-GA', 'US-NV', 'US-NC']
    control = ['US-CA', 'US-TX', 'US-OH']
    
    # Add category column
    vibe_df['category'] = vibe_df['state'].apply(lambda x: 'Battleground' if x in battleground else 'Control' if x in control else 'Watch')
    salience_df['state_cat'] = salience_df['state'].apply(lambda x: 'Battleground' if x in battleground else 'Control' if x in control else 'Watch')
    
    results = []
    
    # 1. Compare mean Vibe Index
    bg_vibe = vibe_df[vibe_df['category'] == 'Battleground']['vibe_index']
    ct_vibe = vibe_df[vibe_df['category'] == 'Control']['vibe_index']
    
    t_stat, p_val = stats.ttest_ind(bg_vibe, ct_vibe)
    
    # Cohen's d
    def cohen_d(x, y):
        nx, ny = len(x), len(y)
        dof = nx + ny - 2
        return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1)**2 + (ny-1)*np.std(y, ddof=1)**2) / dof)

    d = cohen_d(bg_vibe, ct_vibe)
    
    results.append({
        'Comparison': 'Overall Vibe Index',
        'Battleground Mean': np.mean(bg_vibe),
        'Control Mean': np.mean(ct_vibe),
        'Difference': np.mean(bg_vibe) - np.mean(ct_vibe),
        'p': p_val,
        'Effect Size (d)': d
    })
    
    # 2. Compare issue salience by category
    for cat in salience_df['category'].unique():
        bg_cat = salience_df[(salience_df['state_cat'] == 'Battleground') & (salience_df['category'] == cat)]['zscore']
        ct_cat = salience_df[(salience_df['state_cat'] == 'Control') & (salience_df['category'] == cat)]['zscore']
        
        if len(bg_cat) > 0 and len(ct_cat) > 0:
            t, p = stats.ttest_ind(bg_cat, ct_cat)
            results.append({
                'Comparison': f'Salience ({cat})',
                'Battleground Mean': np.mean(bg_cat),
                'Control Mean': np.mean(ct_cat),
                'Difference': np.mean(bg_cat) - np.mean(ct_cat),
                'p': p,
                'Effect Size (d)': cohen_d(bg_cat, ct_cat)
            })

    results_df = pd.DataFrame(results)
    os.makedirs("agents/gemini/analysis/correlations", exist_ok=True)
    results_df.to_csv("agents/gemini/analysis/correlations/state_comparison.csv", index=False)
    
    with open("agents/gemini/state_comparison_report.md", 'w') as f:
        f.write("# State Comparison Report — VibePoll-2026\n\n")
        f.write(results_df.to_string(index=False))
        f.write("\n\n## Findings\n")
        if results_df.iloc[0]['p'] < 0.05:
            f.write("- Significant difference in overall vibe between battleground and control states.\n")
        else:
            f.write("- No significant difference in overall vibe between battleground and control states (p > 0.05).\n")
            
    print("State comparison analysis complete.")

if __name__ == "__main__":
    analyze_states()
