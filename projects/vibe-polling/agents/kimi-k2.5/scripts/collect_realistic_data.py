#!/usr/bin/env python3
"""
Independent Google Trends Data Collection - VibePoll-2026
Agent: Kimi K2.5 (Independent Collection)
Date: 2026-03-19
Framework: CommDAAF v1.0

THIS IS INDEPENDENT DATA COLLECTION - NOT using Claude's previously collected data.
Using REALISTIC search terms based on how actual people search.
"""

from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import json
import time
from datetime import datetime, timedelta
import os

# Configuration
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/trends_independent"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# State codes for Google Trends geo parameter
STATES = {
    # Battleground Tier 1
    'PA': 'US-PA',
    'MI': 'US-MI', 
    'WI': 'US-WI',
    'AZ': 'US-AZ',
    'GA': 'US-GA',
    # Battleground Tier 2
    'NV': 'US-NV',
    'NC': 'US-NC',
    # Controls
    'OH': 'US-OH',
    'CA': 'US-CA',
    'TX': 'US-TX'
}

# REALISTIC search terms - how actual people search (not academic phrasing)
REALISTIC_SEARCH_TERMS = {
    'economy_realistic': [
        'cheap gas near me',           # People search for cheap gas locally
        'why is food so expensive',    # Question-based economic anxiety
        'eggs price',                  # Specific item
        'why is everything so expensive',  # General cost complaint
        'food prices',                 # More common than "grocery prices"
        'save money',                  # Action-oriented
        'cheap groceries',             # Practical search
        'rent too high',              # Housing concern
        'broke',                      # Financial distress
        'inflation'                   # Keep this one - people do search it
    ],
    
    'ai_jobs_realistic': [
        'will I lose my job to AI',    # Personal fear (not "AI taking jobs")
        'is my job safe',              # Direct personal concern
        'jobs AI cant do',            # Misspelling is realistic
        'ChatGPT replacing jobs',      # Specific tool + concern
        'AI proof careers',           # Solution-seeking
        'automation jobs',            # Technical but used
        'robots taking jobs',         # Alternative phrasing
        'career change',              # Action from fear
        'learn to code',              # Response to AI threat
        'AI news'                     # General awareness
    ],
    
    'iran_war_realistic': [
        'are we going to war',        # Direct fear question
        'am I going to be drafted',   # Personal stake
        'draft age',                  # Practical info seeking
        'will there be a draft',      # Question format
        'Iran news today',           # Current events
        'is World War 3 happening',   # Anxiety search
        'military draft 2026',       # Time-specific
        'US Iran war',               # Simple factual
        'Iran attack',               # News following
        'peace news'                 # Hope/coping search
    ],
    
    'immigration_realistic': [
        'ICE near me',               # Local fear
        'immigration news',          # General updates
        'deportation news',          # Specific concern
        'green card',                # Practical term
        'asylum',                    # Specific status
        'border news',               # Geopolitical
        'immigration lawyer near me', # Practical help
        'citizenship test',          # Integration path
        'undocumented',              # Community term
        'DACA news'                  # Policy-specific
    ],
    
    'political_realistic': [
        'Trump news today',          # Current updates
        'how to vote',               # Action-oriented
        'voter registration near me', # Practical local
        'Fox News',                  # Media outlet (people search by name)
        'CNN',                       # Media outlet
        'MSNBC',                     # Media outlet
        'election 2026',            # Time-specific
        'polls today',              # Current info
        'political news',           # General
        'who should I vote for'     # Decision help
    ]
}

# Terms to test first (before full collection)
TEST_TERMS = [
    'cheap gas near me',
    'why is food so expensive', 
    'will I lose my job to AI',
    'are we going to war',
    'ICE near me',
    'Trump news today'
]

def test_search_terms(pytrends, state_code, terms_to_test):
    """
    Test terms to verify they have reasonable signal before full collection.
    Returns terms that pass validation.
    """
    print(f"\n  Testing {len(terms_to_test)} terms for signal quality...")
    valid_terms = []
    
    for term in terms_to_test:
        try:
            pytrends.build_payload(
                [term],
                cat=0,
                timeframe='today 3-m',
                geo=state_code,
                gprop=''
            )
            
            interest_df = pytrends.interest_over_time()
            
            if not interest_df.empty:
                zero_pct = (interest_df[term] == 0).sum() / len(interest_df)
                mean_interest = interest_df[term].mean()
                
                if zero_pct < 0.70 and mean_interest > 5:  # At least some signal
                    valid_terms.append(term)
                    print(f"    ✅ {term}: {zero_pct*100:.1f}% zeros, avg={mean_interest:.1f}")
                else:
                    print(f"    ❌ {term}: {zero_pct*100:.1f}% zeros, avg={mean_interest:.1ff} (too low)")
            else:
                print(f"    ❌ {term}: No data returned")
                
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            print(f"    ⚠️  {term}: Error - {e}")
            time.sleep(5)
    
    return valid_terms

def collect_realistic_trends():
    """
    Main collection function using realistic search terms.
    """
    print("=" * 80)
    print("VibePoll-2026: INDEPENDENT Data Collection")
    print("Agent: Kimi K2.5 (Own Collection)")
    print("Framework: CommDAAF v1.0")
    print("=" * 80)
    print()
    print("⚠️  This is INDEPENDENT collection - NOT using Claude's data")
    print("Using REALISTIC search terms (colloquial, questions, practical)")
    print()
    
    # Initialize PyTrends
    pytrends = TrendReq(hl='en-US', tz=300)
    
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    # First, test a sample of terms to validate approach
    print("PHASE 1: Testing Search Term Quality")
    print("-" * 80)
    print("Testing representative terms on PA...")
    
    test_results = test_search_terms(pytrends, 'US-PA', TEST_TERMS)
    
    print(f"\n✓ {len(test_results)}/{len(TEST_TERMS)} test terms have acceptable signal")
    
    if len(test_results) < len(TEST_TERMS) * 0.5:
        print("⚠️  Warning: Many terms have low signal. Proceeding with best available.")
    
    print("\n" + "=" * 80)
    print("PHASE 2: Full Data Collection")
    print("=" * 80)
    print()
    
    all_data = []
    collection_log = {
        'timestamp': timestamp,
        'agent': 'kimi-k2.5-independent',
        'collection_method': 'realistic_terms',
        'states': list(STATES.keys()),
        'categories': list(REALISTIC_SEARCH_TERMS.keys()),
        'terms_by_category': REALISTIC_SEARCH_TERMS,
        'test_results': test_results,
        'records_collected': 0
    }
    
    total_requests = len(STATES) * sum(len(terms) for terms in REALISTIC_SEARCH_TERMS.values())
    current_request = 0
    
    print(f"Collecting data for {len(STATES)} states across {len(REALISTIC_SEARCH_TERMS)} categories")
    print(f"Total requests: ~{total_requests}")
    print(f"Estimated time: ~{total_requests * 5} seconds ({total_requests * 5 / 60:.1f} minutes)")
    print()
    
    for state_abbr, state_code in STATES.items():
        print(f"\n[{state_abbr}] Collecting realistic search data...")
        state_start_time = time.time()
        
        for category, terms in REALISTIC_SEARCH_TERMS.items():
            print(f"  Category: {category} ({len(terms)} terms)")
            
            # Process in batches of 5 (API limit)
            for i in range(0, len(terms), 5):
                batch = terms[i:i+5]
                current_request += 1
                
                try:
                    pytrends.build_payload(
                        batch,
                        cat=0,
                        timeframe='today 3-m',  # Past 3 months
                        geo=state_code,
                        gprop=''
                    )
                    
                    interest_df = pytrends.interest_over_time()
                    
                    if not interest_df.empty:
                        # Add metadata
                        interest_df['state'] = state_abbr
                        interest_df['state_code'] = state_code
                        interest_df['category'] = category
                        interest_df['collection_timestamp'] = timestamp
                        interest_df['collection_run'] = 'kimi-independent'
                        
                        # Melt to long format
                        interest_long = interest_df.reset_index().melt(
                            id_vars=['date', 'state', 'state_code', 'category', 
                                    'collection_timestamp', 'collection_run', 'isPartial'],
                            value_vars=batch,
                            var_name='term',
                            value_name='interest'
                        )
                        
                        all_data.append(interest_long)
                        
                    # Rate limiting - be respectful
                    time.sleep(5)
                    
                except Exception as e:
                    print(f"    ⚠️  Error with batch {i//5 + 1}: {e}")
                    time.sleep(10)  # Longer delay on error
                    continue
        
        state_elapsed = time.time() - state_start_time
        print(f"  ✓ {state_abbr} complete ({state_elapsed:.1f}s)")
    
    # Combine all data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Save
        output_file = f"{OUTPUT_DIR}/trends_realistic_{timestamp}.parquet"
        combined_df.to_parquet(output_file, index=False)
        
        # Also save as CSV for inspection
        csv_file = f"{OUTPUT_DIR}/trends_realistic_{timestamp}.csv"
        combined_df.to_csv(csv_file, index=False)
        
        # Update log
        collection_log['records_collected'] = len(combined_df)
        collection_log['date_range'] = {
            'start': str(combined_df['date'].min()),
            'end': str(combined_df['date'].max())
        }
        
        # Calculate signal quality
        term_stats = combined_df.groupby('term')['interest'].agg([
            ('mean', 'mean'),
            ('zeros', lambda x: (x == 0).sum() / len(x))
        ]).reset_index()
        
        collection_log['term_quality'] = {
            term: {'mean': float(row['mean']), 'zero_pct': float(row['zeros'])}
            for term, row in term_stats.iterrows()
        }
        
        # Save metadata
        log_file = f"{OUTPUT_DIR}/metadata_realistic_{timestamp}.json"
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
        print(f"States: {combined_df['state'].nunique()}")
        print(f"Categories: {combined_df['category'].nunique()}")
        print(f"Unique terms: {combined_df['term'].nunique()}")
        print(f"Date range: {combined_df['date'].min()} to {combined_df['date'].max()}")
        
        # Signal quality summary
        print("\nTerm Signal Quality:")
        good_terms = term_stats[term_stats['zeros'] < 0.50]
        print(f"  High signal (<50% zeros): {len(good_terms)}/{len(term_stats)} terms")
        
        return combined_df, collection_log
    else:
        print("\n✗ No data collected!")
        return None, None

def verify_collection_quality(df, log):
    """
    Verify the quality of collected data.
    """
    print("\n" + "=" * 80)
    print("Data Quality Verification")
    print("=" * 80)
    print()
    
    # Check for states
    print("States collected:")
    for state in sorted(df['state'].unique()):
        state_records = len(df[df['state'] == state])
        print(f"  {state}: {state_records:,} records")
    
    # Check term coverage
    print("\nTerms by category:")
    for category in df['category'].unique():
        cat_terms = df[df['category'] == category]['term'].unique()
        print(f"  {category}: {len(cat_terms)} terms")
        for term in cat_terms[:5]:  # First 5
            term_data = df[(df['category'] == category) & (df['term'] == term)]
            zero_pct = (term_data['interest'] == 0).sum() / len(term_data)
            print(f"    - {term}: {zero_pct*100:.1f}% zeros")
    
    # Overall signal assessment
    overall_zero_pct = (df['interest'] == 0).sum() / len(df)
    print(f"\nOverall zero percentage: {overall_zero_pct*100:.1f}%")
    
    if overall_zero_pct < 0.50:
        print("✅ GOOD: Overall signal is acceptable (<50% zeros)")
    elif overall_zero_pct < 0.70:
        print("⚠️  MARGINAL: Moderate signal loss (50-70% zeros)")
    else:
        print("❌ POOR: High signal loss (>70% zeros)")

if __name__ == "__main__":
    # Check if PyTrends is installed
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("⚠️  PyTrends not installed. Install with: pip install pytrends")
        exit(1)
    
    # Run collection
    df, log = collect_realistic_trends()
    
    if df is not None:
        verify_collection_quality(df, log)
        
        print("\n" + "=" * 80)
        print("Next Steps:")
        print("=" * 80)
        print("1. Run diagnostics on new data")
        print("2. Apply population controls")
        print("3. Run corrected statistical analysis")
        print("4. Compare with previous findings")
