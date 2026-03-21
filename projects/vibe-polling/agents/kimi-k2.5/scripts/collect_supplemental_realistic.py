#!/usr/bin/env python3
"""
Conservative Realistic Terms Collection - VibePoll-2026
Agent: Kimi K2.5 (Supplemental Collection)
Date: 2026-03-19
Framework: CommDAAF v1.0

Collecting missing realistic/colloquial terms with ultra-conservative rate limits
Target: Avoid IP blocking while collecting essential missing terms
"""

from pytrends.request import TrendReq
import pandas as pd
import json
import time
from datetime import datetime
import os

# Configuration - VERY CONSERVATIVE
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/trends_supplemental"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DELAY_BETWEEN_REQUESTS = 15  # 15 seconds - very conservative
DELAY_AFTER_ERROR = 60  # 1 minute after error
MAX_RETRIES = 3

# States to collect (focus on battlegrounds + key controls)
STATES = {
    'PA': 'US-PA',
    'MI': 'US-MI', 
    'WI': 'US-WI',
    'AZ': 'US-AZ',
    'GA': 'US-GA',
    'NV': 'US-NV',
    'NC': 'US-NC',
    'OH': 'US-OH',
    'CA': 'US-CA',
    'TX': 'US-TX'
}

# Missing realistic terms (not in Claude's collection)
MISSING_REALISTIC_TERMS = {
    'economy_colloquial': [
        'why is food so expensive',  # Reviewer Priority 1
        'cant afford rent',           # Shorter version of "can't afford rent"
        'food bank near me',
        'side hustle',
        'apply for food stamps',
        'how to save money'
    ],
    'war_anxiety': [
        'am I going to be drafted',
        'draft age 2026',
        'are we going to war',
        'will there be a draft',
        'Iran attack'
    ],
    'ai_anxiety': [
        'will AI take my job',
        'is my job safe from AI',
        'jobs AI cant replace',
        'ChatGPT replacing workers',
        'AI proof careers'
    ],
    'immigration_local': [
        'ICE near me',
        'deportation news',
        'immigration lawyer near me',
        'immigration news today'
    ]
}

def collect_with_backoff(pytrends, terms, state_code, category, retry_count=0):
    """
    Collect data with exponential backoff on errors.
    """
    try:
        print(f"      Requesting: {terms}")
        
        pytrends.build_payload(
            terms,
            cat=0,
            timeframe='today 3-m',
            geo=state_code,
            gprop=''
        )
        
        interest_df = pytrends.interest_over_time()
        
        if not interest_df.empty:
            # Add metadata
            interest_df['state'] = state_code
            interest_df['category'] = category
            interest_df['collection_timestamp'] = datetime.now().isoformat()
            interest_df['collection_run'] = 'kimi-supplemental'
            
            # Calculate quality metrics
            for term in terms:
                if term in interest_df.columns:
                    zero_pct = (interest_df[term] == 0).sum() / len(interest_df)
                    avg_vol = interest_df[term].mean()
                    print(f"        ✓ {term}: {zero_pct*100:.1f}% zeros, avg={avg_vol:.1f}")
            
            return interest_df
        else:
            print(f"        ⚠️  No data returned")
            return None
            
    except Exception as e:
        if '429' in str(e) and retry_count < MAX_RETRIES:
            wait_time = DELAY_AFTER_ERROR * (2 ** retry_count)
            print(f"        ⚠️  Rate limited (429). Waiting {wait_time}s...")
            time.sleep(wait_time)
            return collect_with_backoff(pytrends, terms, state_code, category, retry_count + 1)
        else:
            print(f"        ❌ Error: {e}")
            return None

def collect_supplemental_data():
    """
    Main collection with ultra-conservative rate limiting.
    """
    print("=" * 80)
    print("Supplemental Realistic Terms Collection")
    print("Agent: Kimi K2.5 | Ultra-Conservative Mode")
    print("=" * 80)
    print()
    print("⚠️  Using 15-second delays to avoid rate limiting")
    print("⚠️  This will take significant time")
    print()
    
    # Initialize PyTrends
    pytrends = TrendReq(hl='en-US', tz=300)
    
    timestamp = datetime.now().strftime('%Y-%m-%d')
    all_data = []
    collection_log = {
        'timestamp': timestamp,
        'agent': 'kimi-k2.5-supplemental',
        'collection_method': 'realistic_terms_conservative',
        'delay_seconds': DELAY_BETWEEN_REQUESTS,
        'states': list(STATES.keys()),
        'terms_by_category': MISSING_REALISTIC_TERMS,
        'records_collected': 0,
        'terms_collected': [],
        'terms_failed': []
    }
    
    total_requests = len(STATES) * sum(len(terms) for terms in MISSING_REALISTIC_TERMS.values())
    current_request = 0
    
    print(f"Collecting {total_requests} term-state combinations")
    print(f"Estimated time: ~{total_requests * DELAY_BETWEEN_REQUESTS / 60:.1f} minutes")
    print(f"With error delays: ~{total_requests * (DELAY_BETWEEN_REQUESTS + 10) / 60:.1f} minutes")
    print()
    
    for state_abbr, state_code in STATES.items():
        print(f"\n[{state_abbr}] Starting collection...")
        state_start = time.time()
        
        for category, terms in MISSING_REALISTIC_TERMS.items():
            print(f"  Category: {category}")
            
            # Process in batches of 5 (API limit)
            for i in range(0, len(terms), 5):
                batch = terms[i:i+5]
                current_request += 1
                
                print(f"    Batch {i//5 + 1}/{(len(terms) + 4)//5} [{current_request}/{total_requests}]")
                
                df = collect_with_backoff(pytrends, batch, state_code, category)
                
                if df is not None:
                    # Melt to long format
                    interest_long = df.reset_index().melt(
                        id_vars=['date', 'state', 'category', 'collection_timestamp', 
                                'collection_run', 'isPartial'],
                        value_vars=batch,
                        var_name='term',
                        value_name='interest'
                    )
                    all_data.append(interest_long)
                    collection_log['terms_collected'].extend(batch)
                else:
                    collection_log['terms_failed'].extend(batch)
                
                # Conservative delay
                if current_request < total_requests:
                    print(f"      Waiting {DELAY_BETWEEN_REQUESTS}s...")
                    time.sleep(DELAY_BETWEEN_REQUESTS)
        
        state_elapsed = time.time() - state_start
        print(f"  ✓ {state_abbr} complete ({state_elapsed:.1f}s)")
    
    # Save results
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Save parquet
        output_file = f"{OUTPUT_DIR}/trends_supplemental_{timestamp}.parquet"
        combined_df.to_parquet(output_file, index=False)
        
        # Save CSV
        csv_file = f"{OUTPUT_DIR}/trends_supplemental_{timestamp}.csv"
        combined_df.to_csv(csv_file, index=False)
        
        # Update log
        collection_log['records_collected'] = len(combined_df)
        collection_log['unique_terms_collected'] = len(set(collection_log['terms_collected']))
        collection_log['unique_terms_failed'] = len(set(collection_log['terms_failed']))
        
        # Calculate quality
        if len(combined_df) > 0:
            term_stats = combined_df.groupby('term')['interest'].agg([
                ('mean', 'mean'),
                ('zeros', lambda x: (x == 0).sum() / len(x))
            ]).reset_index()
            
            collection_log['term_quality'] = {
                row['term']: {'mean': float(row['mean']), 'zero_pct': float(row['zeros'])}
                for _, row in term_stats.iterrows()
            }
        
        # Save metadata
        log_file = f"{OUTPUT_DIR}/metadata_supplemental_{timestamp}.json"
        with open(log_file, 'w') as f:
            json.dump(collection_log, f, indent=2, default=str)
        
        print("\n" + "=" * 80)
        print("Collection Complete!")
        print("=" * 80)
        print(f"✓ Parquet: {output_file}")
        print(f"✓ CSV: {csv_file}")
        print(f"✓ Metadata: {log_file}")
        print()
        print(f"Total records: {len(combined_df):,}")
        print(f"Terms collected: {collection_log['unique_terms_collected']}")
        print(f"Terms failed: {collection_log['unique_terms_failed']}")
        
        # Quality summary
        if len(combined_df) > 0:
            good_terms = term_stats[term_stats['zeros'] < 0.50]
            print(f"High signal terms (<50% zeros): {len(good_terms)}/{len(term_stats)}")
        
        return combined_df, collection_log
    else:
        print("\n✗ No data collected!")
        return None, None

if __name__ == "__main__":
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("⚠️  PyTrends not installed. Install with: pip install pytrends")
        exit(1)
    
    df, log = collect_supplemental_data()
    
    if df is not None:
        print("\n" + "=" * 80)
        print("Next Steps:")
        print("=" * 80)
        print("1. Verify term quality")
        print("2. Merge with Claude's data")
        print("3. Re-run analysis with national baseline")
        print("4. Flag NH/ME as low confidence")
