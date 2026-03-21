
import pandas as pd
import glob
import os

def merge_all_state_files():
    """Merge all state-specific trends files into a single full file."""
    trends_dir = "agents/gemini/data/raw/trends"
    pattern = os.path.join(trends_dir, "trends_[A-Z][A-Z]_2026-03-19.parquet")
    files = glob.glob(pattern)
    
    if not files:
        print("No state-specific files found.")
        return
    
    print(f"Found {len(files)} state files. Merging...")
    
    all_dfs = []
    for f in files:
        df = pd.read_parquet(f)
        all_dfs.append(df)
        
    combined = pd.concat(all_dfs, ignore_index=True)
    
    # Save the combined file
    output_file = os.path.join(trends_dir, "trends_full_2026-03-19.parquet")
    combined.to_parquet(output_file)
    print(f"Successfully merged {len(files)} states into {output_file}")
    print(f"Total records: {len(combined)}")
    print(f"Unique terms: {combined['term'].nunique()}")

if __name__ == "__main__":
    merge_all_state_files()
