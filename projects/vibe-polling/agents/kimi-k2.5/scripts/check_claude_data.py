#!/usr/bin/env python3
"""
Examine collected trends data and coordinate with Claude Agent
"""
import pandas as pd
import os

# Check Claude's data
claude_path = "/root/.openclaw/workspace/projects/vibe-polling/data/raw/trends/trends_2026-03-19.parquet"

if os.path.exists(claude_path):
    df = pd.read_parquet(claude_path)
    print("=== Claude's Collected Data ===")
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nDate range: {df.index.min()} to {df.index.max()}")
    print(f"\nStates: {df['state'].unique() if 'state' in df.columns else 'N/A'}")
    print(f"\nCategories: {df['category'].unique() if 'category' in df.columns else 'N/A'}")
    print(f"\nFirst 5 rows:")
    print(df.head())
else:
    print("No data found at Claude's path")
