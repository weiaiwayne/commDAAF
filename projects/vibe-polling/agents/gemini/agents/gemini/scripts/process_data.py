
import pandas as pd
import numpy as np
import json
import os
from scipy.stats import zscore

def process_trends():
    """Load and process Google Trends data."""
    trends_file = "/root/.openclaw/workspace/projects/vibe-polling/data/processed/canonical_trends_dataset.parquet"
    if not os.path.exists(trends_file):
        print("Trends file not found.")
        return None
    
    df = pd.read_parquet(trends_file)
    
    # Filter to high-signal terms as requested by reviewer
    valid_terms = ['fox news', 'cnn', 'msnbc', 'chatgpt', '401k', 'inflation', 
                   'green card', 'asylum', 'trump approval', 'gas prices', 
                   'ice near me', 'side hustle', 'am i going to be drafted', 
                   'is my job safe from ai', 'why is food so expensive']
    
    df['term'] = df['term'].str.lower().str.strip()
    df = df[df['term'].isin([t.lower() for t in valid_terms])]
    
    # Rename interest to value to match downstream logic
    if 'interest' in df.columns:
        df = df.rename(columns={'interest': 'value'})
    
    # Calculate Z-scores per term within each state
    df['zscore'] = df.groupby(['state', 'term'])['value'].transform(lambda x: zscore(x, ddof=1) if len(x) > 1 else 0)
    
    # Calculate Issue Salience (mean z-score per state/category/date)
    salience = df.groupby(['date', 'state', 'category'])['zscore'].mean().reset_index()
    
    # Calculate Vibe Index (weighted average of issue salience)
    weights = {
        'economy': 0.35,
        'immigration': 0.20,
        'iran_war': 0.15,
        'ai_jobs': 0.10,
        'political': 0.20,
        'partisan_pairs': 0.10,
        'epstein': 0.05
    }
    
    salience['weighted_val'] = salience.apply(lambda row: row['zscore'] * weights.get(row['category'], 0), axis=1)
    vibe_index = salience.groupby(['date', 'state'])['weighted_val'].sum().reset_index().rename(columns={'weighted_val': 'vibe_index'})
    
    # Calculate population-weighted national vibe
    pop_weights = {
        'US-CA': 0.25, 'US-TX': 0.18, 'US-PA': 0.08, 'US-MI': 0.06, 'US-GA': 0.07,
        'US-OH': 0.07, 'US-NC': 0.07, 'US-AZ': 0.04, 'US-WI': 0.04, 'US-NV': 0.02,
        'US-MN': 0.04, 'US-ME': 0.01, 'US-NH': 0.01
    }
    vibe_index['pop_weight'] = vibe_index['state'].map(pop_weights)
    
    # Create a national dataframe
    national_vibe = vibe_index.groupby('date').apply(
        lambda x: np.average(x['vibe_index'], weights=x['pop_weight']) if x['pop_weight'].sum() > 0 else np.nan
    ).reset_index(name='vibe_index')
    national_vibe['state'] = 'US-NATIONAL'
    national_vibe['pop_weight'] = 1.0
    
    vibe_index = pd.concat([vibe_index, national_vibe], ignore_index=True)
    
    return vibe_index, salience

def process_markets():
    """Load and process historical market data."""
    historical_file = "agents/gemini/data/raw/markets/historical_market_odds.csv"
    if not os.path.exists(historical_file):
        print("Historical market file not found.")
        return None
    
    market_daily = pd.read_csv(historical_file)
    market_daily['date'] = pd.to_datetime(market_daily['date'])
    return market_daily

def merge_and_save():
    """Merge all sources and save processed data."""
    vibe_df, salience_df = process_trends()
    market_df = process_markets()
    
    if vibe_df is not None and market_df is not None:
        # Merge vibe index with market data
        # Since markets might only have one date (today), this might be a small merge
        # for a historical study, we'd have more market dates.
        # But let's merge what we have.
        
        merged = vibe_df.merge(market_df, on='date', how='left')
        
        output_dir = "agents/gemini/data/processed"
        os.makedirs(output_dir, exist_ok=True)
        
        merged.to_parquet(f"{output_dir}/merged_timeseries.parquet")
        vibe_df.to_csv(f"{output_dir}/vibe_indices.csv", index=False)
        salience_df.to_csv(f"{output_dir}/issue_salience.csv", index=False)
        
        print(f"Saved merged data to {output_dir}")
        return merged
    return None

if __name__ == "__main__":
    merge_and_save()
