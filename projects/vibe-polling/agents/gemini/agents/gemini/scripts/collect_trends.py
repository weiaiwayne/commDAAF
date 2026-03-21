import pandas as pd
from datetime import datetime, timedelta
import time
import random
import os
import requests
from pytrends.request import TrendReq

# State codes for Google Trends
STATE_CODES = {
    'PA': 'US-PA', 'MI': 'US-MI', 'WI': 'US-WI', 'AZ': 'US-AZ',
    'GA': 'US-GA', 'NV': 'US-NV', 'NC': 'US-NC', 'CA': 'US-CA',
    'TX': 'US-TX', 'OH': 'US-OH', 'ME': 'US-ME', 'NH': 'US-NH',
    'MN': 'US-MN'
}

# New colloquial search terms recommended by reviewer
TERMS = {
    'economy': [
        'food prices', 'eggs price', 'cheap groceries', 
        'is market crashing', 'should I sell stocks', 'market today',
        'cheap gas near me', 'food bank near me', 'how to save money',
        'why is everything so expensive', 'can\'t afford rent', 'apply for food stamps'
    ],
    'immigration': [
        'ICE near me', 'immigration news', 'deportation news'
    ],
    'iran_war': [
        'Iran attack', 'are we going to war', 'Iran news today',
        'am I going to be drafted', 'draft age', 'will there be a draft 2026',
        'draft age 2026', 'is World War 3 happening', 'will there be a draft'
    ],
    'ai_jobs': [
        'will I lose my job to AI', 'ChatGPT jobs', 'jobs AI can\'t do',
        'AI proof careers', 'is my job safe', 'careers safe from AI',
        'is my job safe from AI', 'will ChatGPT take my job'
    ],
    'political': [
        'my congressman', 'who represents me'
    ]
}

def get_proxies():
    """Fetch free proxies to bypass rate limiting."""
    try:
        r = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=200&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https')
        if r.status_code == 200:
            data = r.json().get('data', [])
            proxies = [f"{p['protocols'][0]}://{p['ip']}:{p['port']}" for p in data]
            print(f"Fetched {len(proxies)} proxies.")
            return proxies
    except Exception as e:
        print(f"Error fetching proxies: {e}")
    return []

def collect_trends_for_state(state_code, terms, proxies, timeframe='2025-01-01 2026-03-19'):
    """Collect Google Trends data using proxies to avoid 429 errors."""
    results = []
    unique_terms = list(set(terms))
    
    for i in range(0, len(unique_terms), 5):
        batch = unique_terms[i:i+5]
        print(f"  Batch {i//5 + 1}: {batch}")
        
        success = False
        for attempt in range(10): # More attempts because free proxies fail often
            try:
                # Use a fresh instance with proxies
                pytrends = TrendReq(hl='en-US', tz=300, retries=1, backoff_factor=0.5, proxies=proxies if proxies else None)
                
                pytrends.build_payload(batch, geo=state_code, timeframe=timeframe)
                interest = pytrends.interest_over_time()
                
                if not interest.empty:
                    if 'isPartial' in interest.columns:
                        interest = interest.drop(columns=['isPartial'])
                    interest['state'] = state_code
                    results.append(interest)
                    success = True
                else:
                    success = True
                
                # Small sleep if using proxies, larger if not
                time.sleep(2 if proxies else 15)
                break
                
            except Exception as e:
                # print(f"    Attempt {attempt+1} failed: {e}")
                time.sleep(5 if proxies else 60)
        
        if not success:
            print(f"    Giving up on {state_code} batch {batch}")
    
    if results:
        combined_batch = pd.concat(results, axis=1)
        if 'state' in combined_batch.columns:
            if isinstance(combined_batch['state'], pd.DataFrame):
                state_vals = combined_batch['state'].iloc[:, 0]
            else:
                state_vals = combined_batch['state']
            combined_batch = combined_batch.drop(columns=['state'])
            combined_batch['state'] = state_vals
            
        combined_batch = combined_batch.loc[:,~combined_batch.columns.duplicated()]
        return combined_batch
    
    return pd.DataFrame()

def collect_all_states():
    timestamp = datetime.now().strftime('%Y-%m-%d')
    all_data = []
    output_dir = "agents/gemini/data/raw/trends"
    os.makedirs(output_dir, exist_ok=True)
    
    proxies = get_proxies()
    
    for state, code in STATE_CODES.items():
        print(f"Collecting: {state}")
        state_dfs = []
        for category, terms in TERMS.items():
            print(f"  Category: {category}")
            df = collect_trends_for_state(code, terms, proxies)
            if not df.empty:
                term_cols = [c for c in df.columns if c not in ['state']]
                melted = df.reset_index().melt(id_vars=['date', 'state'], value_vars=term_cols, var_name='term', value_name='value')
                melted['category'] = category
                state_dfs.append(melted)
                
        if state_dfs:
            state_combined = pd.concat(state_dfs)
            all_data.append(state_combined)
            state_combined.to_parquet(f"{output_dir}/trends_{state}_new_colloquial_{timestamp}.parquet")
            
        print(f"Finished {state}.")
    
    if all_data:
        combined = pd.concat(all_data)
        output_file = f"{output_dir}/trends_new_colloquial_{timestamp}.parquet"
        combined.to_parquet(output_file)
        print(f"Saved final merged dataset: {output_file}")
        
if __name__ == "__main__":
    collect_all_states()
