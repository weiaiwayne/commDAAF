import pandas as pd
import os
from datetime import datetime

def create_canonical_dataset():
    """Merge data from Claude Code (base), Codex, Kimi, and Gemini into a canonical dataset."""
    print("Building canonical dataset...")
    
    dfs = []
    
    # 1. Base Data (Claude Code)
    base_file = "/root/.openclaw/workspace/projects/vibe-polling/data/raw/trends/trends_2026-03-19.parquet"
    if os.path.exists(base_file):
        base_df = pd.read_parquet(base_file)
        base_df = base_df[['date', 'state', 'term', 'category', 'interest']].copy()
        dfs.append(base_df)
        print(f"Loaded Base Data: {len(base_df)} rows")
    
    # 2. Codex Data (R2 New Terms)
    codex_file = "/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/raw/r2_new_terms_2026-03-20.parquet"
    if os.path.exists(codex_file):
        codex_df = pd.read_parquet(codex_file)
        # Codex doesn't have a category column in this specific file, add a default or map known terms
        codex_df['category'] = 'colloquial_supplemental'
        
        # Map known terms to categories if needed
        term_cats = {
            'ICE near me': 'immigration',
            'side hustle': 'economy',
            'Iran attack': 'iran_war',
            'Iran news today': 'iran_war'
        }
        codex_df['category'] = codex_df['term'].map(term_cats).fillna(codex_df['category'])
        
        codex_df = codex_df[['date', 'state', 'term', 'category', 'interest']].copy()
        dfs.append(codex_df)
        print(f"Loaded Codex Data: {len(codex_df)} rows")
        
    # 3. Kimi Data (Supplemental)
    kimi_file = "/root/.openclaw/workspace/projects/vibe-polling/agents/kimi-k2.5/agents/kimi-k2.5/data/raw/trends_supplemental/trends_supplemental_2026-03-20.parquet"
    if os.path.exists(kimi_file):
        kimi_df = pd.read_parquet(kimi_file)
        kimi_df = kimi_df[['date', 'state', 'term', 'category', 'interest']].copy()
        dfs.append(kimi_df)
        print(f"Loaded Kimi Data: {len(kimi_df)} rows")
        
    # 4. Gemini Data (Colloquial Extra)
    gemini_file = "/root/.openclaw/workspace/projects/vibe-polling/agents/gemini/agents/gemini/data/raw/trends/trends_colloquial_extra_2026-03-20_0048.parquet"
    if os.path.exists(gemini_file):
        gemini_df = pd.read_parquet(gemini_file)
        gemini_df = gemini_df.rename(columns={'value': 'interest'})
        # Our script used 'US', convert to national or exclude
        gemini_df = gemini_df[['date', 'state', 'term', 'category', 'interest']].copy()
        dfs.append(gemini_df)
        print(f"Loaded Gemini Data: {len(gemini_df)} rows")
        
    # Combine all
    if not dfs:
        print("No datasets found to merge!")
        return
        
    canonical_df = pd.concat(dfs, ignore_index=True)
    
    # --- Robust Deduplication and Normalization ---
    
    # 1. Normalize term strings (lowercase, strip whitespace)
    canonical_df['term'] = canonical_df['term'].str.lower().str.strip()
    
    # 2. Clean up state codes (e.g. 'US' vs 'US-NATIONAL', strip whitespace)
    canonical_df['state'] = canonical_df['state'].str.strip()
    # Add 'US-' prefix if it's just 2 letters
    canonical_df['state'] = canonical_df['state'].apply(lambda x: f"US-{x}" if len(x) == 2 and x != 'US' else x)
    # Map 'US' to 'US-NATIONAL'
    canonical_df['state'] = canonical_df['state'].replace({'US': 'US-NATIONAL', 'US-US': 'US-NATIONAL'})
    
    # 3. Handle 'interest' vs 'value' was already handled in merge logic, 
    # but let's ensure 'interest' is numeric and handle NaNs
    canonical_df['interest'] = pd.to_numeric(canonical_df['interest'], errors='coerce').fillna(0).astype(int)

    # 4. Final deduplication. 
    # If multiple agents have the same (date, state, term):
    # We sort by interest descending to keep the highest value (often more complete)
    # or just rely on 'keep last' if we want the latest collection agent.
    # Let's keep the highest 'interest' value if they differ, as Google Trends sometimes 
    # returns 0 for a term in a batch but non-zero when queried alone.
    
    print(f"Rows before deduplication: {len(canonical_df)}")
    canonical_df = canonical_df.sort_values(['date', 'state', 'term', 'interest'], ascending=[True, True, True, False])
    canonical_df = canonical_df.drop_duplicates(subset=['date', 'state', 'term'], keep='first')
    print(f"Rows after robust deduplication: {len(canonical_df)}")
    
    # Ensure date type is consistent
    canonical_df['date'] = pd.to_datetime(canonical_df['date'])
    canonical_df['interest'] = pd.to_numeric(canonical_df['interest'], errors='coerce').fillna(0).astype(int)
    
    # Sort
    canonical_df = canonical_df.sort_values(['term', 'state', 'date'])
    
    # Save to the main project data folder
    output_dir = "/root/.openclaw/workspace/projects/vibe-polling/data/processed"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "canonical_trends_dataset.parquet")
    canonical_df.to_parquet(output_path)
    
    print(f"\nSuccessfully created canonical dataset!")
    print(f"Location: {output_path}")
    print(f"Total Rows: {len(canonical_df)}")
    print(f"Unique Terms: {canonical_df['term'].nunique()}")
    print(f"Categories included: {list(canonical_df['category'].unique())}")
    
    # Print a summary report of terms and zero rates
    term_stats = canonical_df.groupby('term').agg(
        total_rows=('interest', 'count'),
        zero_rows=('interest', lambda x: (x == 0).sum())
    )
    term_stats['zero_rate'] = term_stats['zero_rows'] / term_stats['total_rows']
    term_stats = term_stats.sort_values('zero_rate')
    
    term_stats.to_csv(os.path.join(output_dir, "canonical_term_stats.csv"))
    print(f"Saved term statistics to {os.path.join(output_dir, 'canonical_term_stats.csv')}")

if __name__ == "__main__":
    create_canonical_dataset()
