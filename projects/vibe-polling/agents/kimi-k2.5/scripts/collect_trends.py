#!/usr/bin/env python3
"""
Real Google Trends Data Collection for VibePoll-2026
Agent: Kimi K2.5 (Independent Analysis)
Framework: CommDAAF v1.0

Collects REAL search volume data from Google Trends API.
Uses PyTrends with rate limiting to avoid blocks.
"""

from pytrends.request import TrendReq
import pandas as pd
import json
import time
from datetime import datetime
import os

# Configuration
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/trends"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Focus on key battleground states only (reduce API load)
STATE_CODES = {
    'PA': 'US-PA',
    'MI': 'US-MI', 
    'AZ': 'US-AZ',
    'GA': 'US-GA'
}

# High-priority search terms only (reduce API calls)
SEARCH_TERMS = {
    'economy': ['gas prices', 'inflation', 'recession'],
    'iran_war': ['Iran war', 'World War 3'],
    'political': ['how to vote', 'Trump approval']
}

def collect_trends_batch(pytrends, state_code, terms, category, timeframe='today 3-m'):
    """Collect trends for a batch of terms."""
    try:
        print(f"    Requesting: {terms}")
        
        pytrends.build_payload(
            terms,
            cat=0,
            timeframe=timeframe,
            geo=state_code,
            gprop=''
        )
        
        interest_df = pytrends.interest_over_time()
        
        if not interest_df.empty:
            interest_df['state'] = state_code
            interest_df['category'] = category
            interest_df['collected_at'] = datetime.now().isoformat()
            return interest_df
        
        return pd.DataFrame()
        
    except Exception as e:
        print(f"    ⚠️  Error: {e}")
        return pd.DataFrame()

def collect_real_trends():
    """Collect real Google Trends data."""
    print("=" * 70)
    print("VibePoll-2026: REAL Google Trends Data Collection")
    print(f"Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print("=" * 70)
    print()
    
    # Initialize PyTrends
    pytrends = TrendReq(hl='en-US', tz=300)
    
    timestamp = datetime.now().strftime('%Y-%m-%d')
    all_data = []
    
    total_requests = len(STATE_CODES) * sum(len(terms) for terms in SEARCH_TERMS.values())
    current_request = 0
    
    print(f"Collecting REAL data from Google Trends API...")
    print(f"States: {len(STATE_CODES)} | Categories: {len(SEARCH_TERMS)}")
    print(f"This will take approximately {total_requests * 5} seconds due to rate limiting")
    print()
    
    for state_abbr, state_code in STATE_CODES.items():
        print(f"[{state_abbr}] Collecting data...")
        
        for category, terms in SEARCH_TERMS.items():
            print(f"  Category: {category}")
            
            # Process in batches of 5 (API limit)
            for i in range(0, len(terms), 5):
                batch = terms[i:i+5]
                current_request += 1
                
                df = collect_trends_batch(pytrends, state_code, batch, category)
                
                if not df.empty:
                    all_data.append(df)
                    print(f"    ✓ Got {len(df)} data points")
                else:
                    print(f"    ✗ No data returned")
                
                # Rate limiting - critical to avoid blocks
                time.sleep(5)
        
        print()
    
    # Save collected data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=False)
        
        # Save as parquet
        output_file = f"{OUTPUT_DIR}/trends_{timestamp}.parquet"
        combined_df.to_parquet(output_file, index=True)
        
        # Save as CSV for easy inspection
        csv_file = f"{OUTPUT_DIR}/trends_{timestamp}.csv"
        combined_df.to_csv(csv_file)
        
        # Metadata
        metadata = {
            'collection_date': timestamp,
            'agent': 'kimi-k2.5',
            'framework': 'commdaaf-v1.0',
            'data_type': 'REAL',
            'source': 'Google Trends API via PyTrends',
            'states': list(STATE_CODES.keys()),
            'categories': list(SEARCH_TERMS.keys()),
            'total_records': len(combined_df),
            'date_range': {
                'start': str(combined_df.index.min()),
                'end': str(combined_df.index.max())
            },
            'collection_params': {
                'timeframe': 'today 3-m',
                'geo_level': 'state'
            }
        }
        
        metadata_file = f"{OUTPUT_DIR}/metadata_{timestamp}.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print("=" * 70)
        print("Collection complete!")
        print("=" * 70)
        print(f"✓ Parquet: {output_file}")
        print(f"✓ CSV: {csv_file}")
        print(f"✓ Metadata: {metadata_file}")
        print(f"  Total records: {len(combined_df):,}")
        print(f"  States: {combined_df['state'].nunique()}")
        print(f"  Date range: {combined_df.index.min().date()} to {combined_df.index.max().date()}")
        
        return combined_df
    else:
        print("✗ No data collected!")
        return None

if __name__ == "__main__":
    df = collect_real_trends()
