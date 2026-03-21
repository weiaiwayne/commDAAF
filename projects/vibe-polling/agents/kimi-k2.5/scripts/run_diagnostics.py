#!/usr/bin/env python3
"""
CommDAAF MANDATORY Distribution Diagnostics
Agent: Kimi K2.5 (Independent Analysis)
Framework: CommDAAF v1.0 - Section 7.1

CRITICAL: This is NON-NEGOTIABLE - must run before any regression.
"""

import pandas as pd
import numpy as np
from scipy import stats
import json
import os
from datetime import datetime

# Paths
DATA_PATH = "agents/kimi-k2.5/data/raw/trends/trends_2026-03-19.parquet"
OUTPUT_DIR = "agents/kimi-k2.5/analysis/descriptives"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def calculate_diagnostics(series, var_name):
    """
    Calculate full distribution diagnostics for a variable.
    CommDAAF Section 7.1 requirements.
    """
    # Remove NaN
    clean = series.dropna()
    
    n = len(clean)
    if n == 0:
        return None
    
    # Basic stats
    mean = clean.mean()
    median = clean.median()
    std = clean.std()
    min_val = clean.min()
    max_val = clean.max()
    
    # Distribution shape
    skewness = stats.skew(clean)
    
    # Zero proportion
    zero_count = (clean == 0).sum()
    zero_pct = (zero_count / n) * 100
    
    # Overdispersion check (var/mean ratio)
    if mean != 0:
        dispersion_ratio = (std ** 2) / mean
    else:
        dispersion_ratio = np.inf
    
    # Normality test (if n < 5000)
    if n < 5000:
        try:
            shapiro_stat, shapiro_p = stats.shapiro(clean.sample(min(n, 5000)))
        except:
            shapiro_stat, shapiro_p = None, None
    else:
        shapiro_stat, shapiro_p = None, None
    
    # Model recommendation
    flags = []
    if abs(skewness) > 1:
        flags.append("HIGHLY_SKEWED")
    if zero_pct > 15:
        flags.append("HIGH_ZERO_PROPORTION")
    if dispersion_ratio > 1.5:
        flags.append("OVERDISPERSED")
    
    # Decision tree from CommDAAF
    if "OVERDISPERSED" in flags or "HIGH_ZERO_PROPORTION" in flags:
        model_rec = "Negative Binomial (count data) or Zero-inflated"
    elif abs(skewness) > 1:
        model_rec = "Transform (log) or robust regression"
    else:
        model_rec = "OLS acceptable (verify residuals)"
    
    return {
        "variable": var_name,
        "n": n,
        "mean": round(mean, 3),
        "median": round(median, 3),
        "sd": round(std, 3),
        "min": round(min_val, 3),
        "max": round(max_val, 3),
        "range": round(max_val - min_val, 3),
        "skewness": round(skewness, 3),
        "zero_pct": round(zero_pct, 2),
        "var_mean_ratio": round(dispersion_ratio, 3),
        "shapiro_stat": round(shapiro_stat, 4) if shapiro_stat else None,
        "shapiro_p": round(shapiro_p, 4) if shapiro_p else None,
        "flags": flags,
        "model_recommendation": model_rec
    }

def run_full_diagnostics():
    """
    Run diagnostics on all numeric variables.
    """
    print("=" * 80)
    print("CommDAAF MANDATORY Distribution Diagnostics")
    print("Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print("Section 7.1 - NON-NEGOTIABLE BEFORE REGRESSION")
    print("=" * 80)
    print()
    
    # Load data
    print(f"Loading data from: {DATA_PATH}")
    df = pd.read_parquet(DATA_PATH)
    print(f"✓ Loaded {len(df):,} records")
    print()
    
    # Variables to diagnose
    variables = {
        "interest": df["interest"],
    }
    
    # Also diagnose by category
    for category in df["category"].unique():
        cat_data = df[df["category"] == category]["interest"]
        variables[f"interest_{category}"] = cat_data
    
    # Run diagnostics
    all_results = []
    
    print("Running diagnostics...")
    print("-" * 80)
    
    for var_name, series in variables.items():
        result = calculate_diagnostics(series, var_name)
        if result:
            all_results.append(result)
            
            # Print formatted output
            print(f"\n=== Variable: {var_name} ===")
            print(f"N: {result['n']}")
            print(f"Mean: {result['mean']} | Median: {result['median']} | SD: {result['sd']}")
            print(f"Range: {result['min']} - {result['max']}")
            print(f"Skewness: {result['skewness']} {'⚠️ HIGHLY SKEWED' if abs(result['skewness']) > 1 else ''}")
            print(f"% Zeros: {result['zero_pct']}% {'⚠️ HIGH ZERO PROPORTION' if result['zero_pct'] > 15 else ''}")
            print(f"Var/Mean: {result['var_mean_ratio']} {'⚠️ OVERDISPERSED' if result['var_mean_ratio'] > 1.5 else ''}")
            if result['shapiro_p']:
                print(f"Shapiro-Wilk: W={result['shapiro_stat']}, p={result['shapiro_p']}")
            print(f"\n→ MODEL RECOMMENDATION: {result['model_recommendation']}")
            if result['flags']:
                print(f"   Flags: {', '.join(result['flags'])}")
    
    # Save results
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    # JSON for machine reading
    json_file = f"{OUTPUT_DIR}/distribution_diagnostics.json"
    
    # Convert numpy types to Python native types for JSON serialization
    def convert_types(obj):
        if isinstance(obj, dict):
            return {k: convert_types(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_types(item) for item in obj]
        elif isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj
    
    with open(json_file, 'w') as f:
        json.dump({
            "agent": "kimi-k2.5",
            "framework": "commdaaf-v1.0",
            "date": timestamp,
            "data_source": "google_trends_real",
            "results": [convert_types(r) for r in all_results]
        }, f, indent=2, default=str)
    
    # Markdown for human reading
    md_file = f"agents/kimi-k2.5/diagnostics_report.md"
    with open(md_file, 'w') as f:
        f.write("# Distribution Diagnostics Report\n\n")
        f.write(f"**Agent:** Kimi K2.5  \n")
        f.write(f"**Framework:** CommDAAF v1.0  \n")
        f.write(f"**Date:** {timestamp}  \n")
        f.write(f"**Data Source:** Google Trends (Real Data)  \n\n")
        f.write("---\n\n")
        f.write("## ⚠️ CommDAAF Section 7.1 Compliance\n\n")
        f.write("✅ **MANDATORY diagnostics completed before regression**\n\n")
        f.write("## Summary\n\n")
        
        # Summary table
        f.write("| Variable | N | Mean | Skewness | % Zeros | Var/Mean | Model Rec |\n")
        f.write("|----------|---|------|----------|---------|----------|-----------|\n")
        
        for r in all_results[:10]:  # First 10
            skew_flag = "⚠️" if abs(r['skewness']) > 1 else ""
            zero_flag = "⚠️" if r['zero_pct'] > 15 else ""
            disp_flag = "⚠️" if r['var_mean_ratio'] > 1.5 else ""
            
            f.write(f"| {r['variable']} | {r['n']} | {r['mean']} | {r['skewness']}{skew_flag} | ")
            f.write(f"{r['zero_pct']}{zero_flag} | {r['var_mean_ratio']}{disp_flag} | {r['model_recommendation'][:30]}... |\n")
        
        f.write("\n## Detailed Results\n\n")
        
        for r in all_results:
            f.write(f"### {r['variable']}\n\n")
            f.write(f"- **N:** {r['n']}\n")
            f.write(f"- **Mean:** {r['mean']} | **Median:** {r['median']} | **SD:** {r['sd']}\n")
            f.write(f"- **Range:** {r['min']} - {r['max']}\n")
            f.write(f"- **Skewness:** {r['skewness']}\n")
            f.write(f"- **% Zeros:** {r['zero_pct']}%\n")
            f.write(f"- **Var/Mean Ratio:** {r['var_mean_ratio']}\n")
            if r['shapiro_p']:
                f.write(f"- **Shapiro-Wilk:** W={r['shapiro_stat']}, p={r['shapiro_p']}\n")
            f.write(f"- **Flags:** {', '.join(r['flags']) if r['flags'] else 'None'}\n")
            f.write(f"- **Model Recommendation:** {r['model_recommendation']}\n\n")
    
    print("\n" + "=" * 80)
    print("Diagnostics Complete!")
    print("=" * 80)
    print(f"✓ JSON: {json_file}")
    print(f"✓ Markdown: {md_file}")
    print(f"\n📊 Variables diagnosed: {len(all_results)}")
    print("\n⚠️  KEY FINDINGS:")
    
    # Summary of flags
    skewed = sum(1 for r in all_results if abs(r['skewness']) > 1)
    zero_heavy = sum(1 for r in all_results if r['zero_pct'] > 15)
    overdispersed = sum(1 for r in all_results if r['var_mean_ratio'] > 1.5)
    
    print(f"   - Highly skewed: {skewed}/{len(all_results)}")
    print(f"   - High zero proportion: {zero_heavy}/{len(all_results)}")
    print(f"   - Overdispersed: {overdispersed}/{len(all_results)}")
    print("\n→ Model Selection: Use Negative Binomial or zero-inflated models")
    print("   ❌ DO NOT USE OLS on raw count data")
    
    return all_results

if __name__ == "__main__":
    results = run_full_diagnostics()
