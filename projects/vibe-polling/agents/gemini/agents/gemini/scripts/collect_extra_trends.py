import pandas as pd
from pytrends.request import TrendReq
import time
from datetime import datetime
import os

STATE_CODES = {
    'US': 'US', # National
    'PA': 'US-PA', 'MI': 'US-MI', 'WI': 'US-WI', 'AZ': 'US-AZ',
    'GA': 'US-GA', 'NV': 'US-NV', 'NC': 'US-NC', 'CA': 'US-CA',
    'TX': 'US-TX', 'OH': 'US-OH', 'ME': 'US-ME', 'NH': 'US-NH',
    'MN': 'US-MN'
}

TERMS = ['side hustle', 'am I going to be drafted', 'is my job safe from AI', 'ICE near me', 'why is food so expensive']

def collect():
    pytrends = TrendReq(hl='en-US', tz=300)
    all_data = []
    
    for state, code in STATE_CODES.items():
        print(f"Collecting {code}...")
        success = False
        for attempt in range(3):
            try:
                pytrends.build_payload(TERMS, geo=code, timeframe='2025-01-01 2026-03-19')
                df = pytrends.interest_over_time()
                if not df.empty:
                    if 'isPartial' in df.columns:
                        df = df.drop(columns=['isPartial'])
                    df['state'] = code
                    
                    # Melt to match previous format
                    term_cols = [c for c in df.columns if c != 'state']
                    df = df.reset_index().melt(id_vars=['date', 'state'], value_vars=term_cols, var_name='term', value_name='value')
                    
                    # Add category mappings
                    cat_map = {
                        'side hustle': 'economy',
                        'why is food so expensive': 'economy',
                        'am I going to be drafted': 'iran_war',
                        'is my job safe from AI': 'ai_jobs',
                        'ICE near me': 'immigration'
                    }
                    df['category'] = df['term'].map(cat_map)
                    
                    all_data.append(df)
                success = True
                time.sleep(15) # Conservative delay
                break
            except Exception as e:
                print(f"Error {code}: {e}")
                time.sleep(60)
                
    if all_data:
        combined = pd.concat(all_data)
        os.makedirs("agents/gemini/data/raw/trends", exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
        out_file = f"agents/gemini/data/raw/trends/trends_colloquial_extra_{timestamp}.parquet"
        combined.to_parquet(out_file)
        print(f"Saved {out_file}")
        return combined

if __name__ == "__main__":
    collect()
