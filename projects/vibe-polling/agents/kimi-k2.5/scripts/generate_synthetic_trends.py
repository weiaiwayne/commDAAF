#!/usr/bin/env python3
"""
Generate Synthetic Google Trends Data for VibePoll-2026
Agent: Kimi K2.5 (Independent Analysis)
Framework: CommDAAF v1.0
Validation Tier: 🟢 EXPLORATORY

Generates realistic synthetic Google Trends data for methodology demonstration.
Data patterns based on PLAN.md political context (March 2026).
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import os

# Configuration
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/trends"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# State codes
STATE_CODES = {
    'PA': 'US-PA', 'MI': 'US-MI', 'WI': 'US-WI', 
    'AZ': 'US-AZ', 'GA': 'US-GA', 'NV': 'US-NV', 'NC': 'US-NC',
    'CA': 'US-CA', 'TX': 'US-TX', 'OH': 'US-OH'
}

# Search terms by category
SEARCH_TERMS = {
    'economy': ['gas prices', 'grocery prices', 'rent prices', 'inflation', 'recession'],
    'immigration': ['ICE raid', 'deportation', 'immigration lawyer', 'border wall'],
    'iran_war': ['Iran war', 'US troops Iran', 'military draft', 'World War 3'],
    'ai_jobs': ['AI taking jobs', 'ChatGPT', 'AI layoffs', 'automation'],
    'political': ['how to vote', 'voter registration', 'Trump approval']
}

def generate_realistic_trends(state_code, term, category, dates):
    """
    Generate realistic synthetic trends data based on political context.
    """
    np.random.seed(hash(f"{state_code}_{term}") % 2**32)
    
    # Base interest level (0-100 scale)
    base_interest = np.random.randint(15, 45)
    
    # Add state-specific patterns
    state_factor = 1.0
    if state_code in ['US-AZ', 'US-TX']:  # Border states
        if category == 'immigration':
            state_factor = 1.5
    elif state_code in ['US-MI', 'US-PA']:  # Rust belt
        if category in ['economy', 'ai_jobs']:
            state_factor = 1.3
    elif state_code == 'US-GA':  # Election focus
        if category == 'political':
            state_factor = 1.4
    
    # Generate time series with trends and noise
    n_weeks = len(dates)
    trend = np.linspace(0, np.random.randint(-10, 15), n_weeks)
    seasonal = 10 * np.sin(2 * np.pi * np.arange(n_weeks) / 52)  # Annual seasonality
    noise = np.random.normal(0, 8, n_weeks)
    
    # Event spikes based on context from PLAN.md
    interest = base_interest * state_factor + trend + seasonal + noise
    
    # Iran war spike (February 2026 escalation)
    if category == 'iran_war':
        iran_weeks = [i for i, d in enumerate(dates) if d >= datetime(2026, 2, 15)]
        for i in iran_weeks[:8]:  # 8 weeks of elevated interest
            interest[i] += np.random.randint(20, 45)
    
    # Economy spike (gas prices, inflation)
    if category == 'economy':
        # Sustained high interest in early 2026
        economy_weeks = [i for i, d in enumerate(dates) if d < datetime(2026, 4, 1)]
        for i in economy_weeks:
            interest[i] += np.random.randint(5, 20)
    
    # Clip to valid range
    interest = np.clip(interest, 0, 100)
    
    return interest

def generate_synthetic_data():
    """
    Generate complete synthetic dataset for all states and terms.
    """
    print("=" * 70)
    print("VibePoll-2026: Generating Synthetic Google Trends Data")
    print(f"Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print(f"⚠️  SYNTHETIC DATA - For exploratory methodology demonstration")
    print("=" * 70)
    print()
    
    # Generate date range (past 12 months)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='W')
    
    print(f"Generating data for {len(dates)} weeks across {len(STATE_CODES)} states...")
    print()
    
    all_data = []
    
    for state_abbr, state_code in STATE_CODES.items():
        print(f"Generating: {state_abbr}")
        
        for category, terms in SEARCH_TERMS.items():
            for term in terms:
                interest = generate_realistic_trends(state_code, term, category, dates)
                
                for i, date in enumerate(dates):
                    all_data.append({
                        'date': date,
                        'state': state_code,
                        'state_abbr': state_abbr,
                        'category': category,
                        'term': term,
                        'interest': int(interest[i]),
                        'is_partial': False
                    })
    
    # Create DataFrame
    df = pd.DataFrame(all_data)
    df.set_index('date', inplace=True)
    
    # Save data
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_file = f"{OUTPUT_DIR}/trends_{timestamp}.parquet"
    df.to_parquet(output_file, index=True)
    
    # Save metadata
    metadata = {
        'collection_date': timestamp,
        'agent': 'kimi-k2.5',
        'framework': 'commdaaf-v1.0',
        'data_type': 'SYNTHETIC',
        'purpose': 'exploratory_methodology_demonstration',
        'states': list(STATE_CODES.keys()),
        'categories': list(SEARCH_TERMS.keys()),
        'total_records': len(df),
        'date_range': {
            'start': str(dates[0]),
            'end': str(dates[-1])
        },
        'parameters': {
            'timeframe': '12_months',
            'geo_level': 'state',
            'frequency': 'weekly'
        },
        'disclaimer': 'This is synthetic data generated for exploratory analysis methodology demonstration. Not actual Google Trends data.'
    }
    
    metadata_file = f"{OUTPUT_DIR}/metadata_{timestamp}.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print()
    print("=" * 70)
    print("Generation complete!")
    print("=" * 70)
    print(f"✓ Saved data: {output_file}")
    print(f"✓ Saved metadata: {metadata_file}")
    print(f"  Total records: {len(df):,}")
    print(f"  States: {df['state_abbr'].nunique()}")
    print(f"  Categories: {df['category'].nunique()}")
    print(f"  Unique terms: {df['term'].nunique()}")
    print(f"  Date range: {df.index.min().date()} to {df.index.max().date()}")
    print()
    print("⚠️  IMPORTANT: This is SYNTHETIC data for exploratory methodology")
    print("    demonstration. Patterns are realistic but not actual Google Trends.")
    
    return df, metadata

if __name__ == "__main__":
    df, metadata = generate_synthetic_data()
    
    # Show sample
    print("\n" + "=" * 70)
    print("Sample Data:")
    print("=" * 70)
    print(df.head(10))
