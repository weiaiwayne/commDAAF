
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_figures():
    """Generate key figures for the study."""
    processed_dir = "agents/gemini/data/processed"
    vibe_file = f"{processed_dir}/vibe_indices.csv"
    merged_file = f"{processed_dir}/merged_timeseries.parquet"
    
    if not os.path.exists(vibe_file):
        print("Data files not found.")
        return
        
    vibe_df = pd.read_csv(vibe_file)
    vibe_df['date'] = pd.to_datetime(vibe_df['date'])
    
    merged_df = pd.read_parquet(merged_file)
    merged_df['date'] = pd.to_datetime(merged_df['date'])
    
    output_dir = "agents/gemini/outputs/figures"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Vibe Index Timeseries for Battleground States
    plt.figure(figsize=(12, 6))
    bg_states = ['US-PA', 'US-MI', 'US-WI', 'US-AZ', 'US-GA', 'US-NV', 'US-NC']
    bg_df = vibe_df[vibe_df['state'].isin(bg_states)]
    sns.lineplot(data=bg_df, x='date', y='vibe_index', hue='state')
    plt.title('Vibe Index Over Time (Battleground States)')
    plt.ylabel('Vibe Index (Weighted Z-Score)')
    plt.savefig(f"{output_dir}/vibe_index_timeseries.png")
    plt.close()
    
    # 2. Vibe Index vs House Odds (US-NH as top correlation)
    plt.figure(figsize=(10, 6))
    nh_df = merged_df[merged_df['state'] == 'US-NH'].dropna(subset=['vibe_index', 'house_dem_odds'])
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Vibe Index (NH)', color='tab:blue')
    ax1.plot(nh_df['date'], nh_df['vibe_index'], color='tab:blue', label='Vibe Index')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('House Dem Odds', color='tab:red')
    ax2.plot(nh_df['date'], nh_df['house_dem_odds'], color='tab:red', label='House Odds')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    plt.title('Vibe Index vs House Control Odds (New Hampshire)')
    fig.tight_layout()
    plt.savefig(f"{output_dir}/vibe_vs_market_nh.png")
    plt.close()
    
    # 3. Correlation Heatmap
    corr_df = pd.read_csv("agents/gemini/analysis/correlations/concurrent_correlations.csv")
    # Take just vibe vs house
    vibe_house = corr_df[corr_df['Variable 2'] == 'House Dem Odds']
    vibe_house = vibe_house[vibe_house['Variable 1'].str.contains('Vibe Index')]
    vibe_house['state'] = vibe_house['Variable 1'].str.extract(r'\((.*)\)')
    
    plt.figure(figsize=(10, 8))
    sns.barplot(data=vibe_house.sort_values('r', ascending=False), x='r', y='state', palette='viridis')
    plt.title('Vibe Index to House Control Correlation (Pearson r)')
    plt.xlabel('Correlation Coefficient (r)')
    plt.savefig(f"{output_dir}/correlation_by_state.png")
    plt.close()
    
    print("Figures generated successfully.")

if __name__ == "__main__":
    generate_figures()
