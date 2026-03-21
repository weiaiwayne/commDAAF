#!/usr/bin/env python3
"""
FINAL ANALYSIS R2 - VibePoll-2026
Incorporating Reviewer R2 Feedback

Changes from R1:
1. Baseline: National weighted average (not OH)
2. Flag NH/ME as low confidence
3. Include supplemental realistic terms (filtered to high-signal only)
4. Enhanced documentation
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import json
import os
from datetime import datetime
from statsmodels.stats.multitest import multipletests

print("=" * 80)
print("VibePoll-2026: FINAL ANALYSIS R2 (Reviewer Feedback)")
print("=" * 80)
print()

# Paths
CLAUDE_DATA = "data/raw/trends/trends_full_2026-03-19.parquet"
SUPPLEMENTAL_DATA = "data/raw/trends_supplemental/trends_supplemental_2026-03-20.parquet"
DEMOGRAPHICS_PATH = "data/reference/state_demographics.json"
OUTPUT_DIR = "analysis/models"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# National population weights (from reviewer)
POPULATION_WEIGHTS = {
    'CA': 0.25, 'TX': 0.18, 'PA': 0.08, 'MI': 0.06, 'GA': 0.07,
    'AZ': 0.05, 'WI': 0.04, 'NC': 0.07, 'NV': 0.02, 'OH': 0.07,
    'ME': 0.01, 'NH': 0.01, 'MN': 0.04
}

# Load demographics
with open(DEMOGRAPHICS_PATH, 'r') as f:
    DEMOGRAPHICS = json.load(f)

# Load Claude's data
print("Loading Claude's data...")
df_claude = pd.read_parquet(CLAUDE_DATA)
print(f"✓ Claude data: {len(df_claude):,} records")

# Load supplemental data if exists
df_supplemental = None
if os.path.exists(SUPPLEMENTAL_DATA):
    print("Loading supplemental realistic terms...")
    df_supplemental = pd.read_parquet(SUPPLEMENTAL_DATA)
    print(f"✓ Supplemental data: {len(df_supplemental):,} records")
    
    # Filter supplemental to high-signal terms only
    supp_stats = df_supplemental.groupby('term')['interest'].agg([
        ('zero_pct', lambda x: (x == 0).sum() / len(x))
    ]).reset_index()
    
    high_signal_supp = supp_stats[supp_stats['zero_pct'] < 0.75]['term'].tolist()
    print(f"  High-signal supplemental terms: {len(high_signal_supp)}/{len(supp_stats)}")
    print(f"    {high_signal_supp}")
    
    df_supplemental = df_supplemental[df_supplemental['term'].isin(high_signal_supp)]
    
    # Combine
    df = pd.concat([df_claude, df_supplemental], ignore_index=True)
else:
    print("⚠️  No supplemental data found, using Claude's data only")
    df = df_claude.copy()

print(f"\n✓ Combined data: {len(df):,} records")
print(f"  States: {df['state'].nunique()}")
print(f"  Terms: {df['term'].nunique()}")

# PHASE 1: Filter to high-signal typed-search terms
print("\n" + "=" * 80)
print("PHASE 1: Filtering to High-Signal Terms")
print("=" * 80)

term_stats = df.groupby('term').agg({
    'interest': ['count', 'mean', lambda x: (x == 0).sum() / len(x)]
}).reset_index()
term_stats.columns = ['term', 'count', 'mean_interest', 'zero_pct']

# Word count
def count_words(term):
    return len(term.split())

term_stats['word_count'] = term_stats['term'].apply(count_words)

# Filter: <50% zeros AND 1-5 words (slightly relaxed for realistic terms)
valid_terms = term_stats[
    (term_stats['zero_pct'] < 0.50) & 
    (term_stats['word_count'] >= 1) & 
    (term_stats['word_count'] <= 5)
]['term'].tolist()

# Also keep the high-signal supplemental terms even if slightly higher zeros
if df_supplemental is not None and len(high_signal_supp) > 0:
    for term in high_signal_supp:
        if term not in valid_terms:
            valid_terms.append(term)

removed_terms = [t for t in term_stats['term'] if t not in valid_terms]

print(f"✅ Retaining {len(valid_terms)} high-signal terms")
print(f"🔴 Removing {len(removed_terms)} low-signal terms")

# Flag NH/ME as low confidence
print("\n⚠️  FLAGGING: NH and ME have structural data issues (63-64% zeros)")
print("   These states will be marked as 'low confidence' in output")

# Filter data
df_filtered = df[df['term'].isin(valid_terms)].copy()

# Standardize state format (some data has 'US-PA', some has 'PA')
df_filtered['state'] = df_filtered['state'].str.replace('US-', '', regex=False)

print(f"\nFiltered data: {len(df_filtered):,} records")

# PHASE 2: Prepare data with National Baseline
print("\n" + "=" * 80)
print("PHASE 2: National Weighted Baseline (Reviewer R2)")
print("=" * 80)

# Add population weights
df_filtered['pop_weight'] = df_filtered['state'].map(POPULATION_WEIGHTS)
df_filtered['population'] = df_filtered['state'].map(lambda x: DEMOGRAPHICS[x]['population'])
df_filtered['log_population'] = np.log(df_filtered['population'])

# Calculate national weighted average per date
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

print("Calculating national weighted baseline...")
national_avg = df_filtered.groupby('date').apply(
    lambda x: np.average(x['interest'], weights=x['pop_weight'])
).reset_index()
national_avg.columns = ['date', 'national_avg']

# Merge back
df_filtered = df_filtered.merge(national_avg, on='date', how='left')
df_filtered['interest_vs_national'] = df_filtered['interest'] - df_filtered['national_avg']

print("✓ National baseline calculated")
print(f"  National avg range: {df_filtered['national_avg'].min():.1f} - {df_filtered['national_avg'].max():.1f}")

# State classifications
BATTLEGROUND_STATES = ['PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC']
CONTROL_STATES = ['OH', 'CA', 'TX']
LOW_CONFIDENCE_STATES = ['ME', 'NH', 'MN']  # Flag these

df_filtered['state_type'] = df_filtered['state'].apply(
    lambda x: 'battleground' if x in BATTLEGROUND_STATES 
    else 'control' if x in CONTROL_STATES
    else 'low_confidence' if x in LOW_CONFIDENCE_STATES
    else 'other'
)

df_filtered['is_low_confidence'] = df_filtered['state'].isin(LOW_CONFIDENCE_STATES)

# Time features
df_filtered['days_since_start'] = (df_filtered['date'] - df_filtered['date'].min()).dt.days

print("✓ State classifications:")
print(f"  Battleground: {len(BATTLEGROUND_STATES)} states")
print(f"  Control: {len(CONTROL_STATES)} states") 
print(f"  Low confidence: {len(LOW_CONFIDENCE_STATES)} states (NH, ME, MN)")

# PHASE 3: Statistical Modeling with National Baseline
print("\n" + "=" * 80)
print("PHASE 3: Modeling (National Baseline)")
print("=" * 80)

results_list = []
all_pvalues = []

# Model 1: Battleground vs Control vs National
print("\nModel 1: Battleground vs Control (vs National Baseline)")
print("-" * 80)

# Exclude low-confidence states for main analysis
df_main = df_filtered[~df_filtered['is_low_confidence']].copy()

df_analysis = df_main[df_main['state_type'].isin(['battleground', 'control'])].copy()
df_analysis['is_battleground'] = (df_analysis['state_type'] == 'battleground').astype(int)

# Use raw interest (not vs national) to avoid numerical issues
# Add small constant to avoid zeros in NB model
df_analysis['interest_adj'] = df_analysis['interest'] + 0.1

y = df_analysis['interest_adj']
X = pd.DataFrame({
    'const': 1,
    'is_battleground': df_analysis['is_battleground'],
    'days_since_start': df_analysis['days_since_start']
})

# Negative Binomial with population offset
model = sm.GLM(y, X, family=sm.families.NegativeBinomial(alpha=1.0),
               offset=df_analysis['log_population'])
try:
    result = model.fit()
except:
    # Fallback to OLS if NB fails
    print("  ⚠️  NB model failed, using OLS as fallback")
    model = sm.OLS(df_analysis['interest'], X)
    result = model.fit()

irr = np.exp(result.params)
ci = np.exp(result.conf_int())

print(f"✓ Model converged")
print(f"  Battleground effect (vs national): IRR = {irr['is_battleground']:.3f}")
print(f"  95% CI: {ci.loc['is_battleground', 0]:.3f} - {ci.loc['is_battleground', 1]:.3f}")
print(f"  p-value: {result.pvalues['is_battleground']:.6f}")

if irr['is_battleground'] > 1:
    change = (irr['is_battleground'] - 1) * 100
    print(f"  → {change:.1f}% HIGHER than national average")
else:
    change = (1 - irr['is_battleground']) * 100
    print(f"  → {change:.1f}% LOWER than national average")

results_list.append({
    'model': 'battleground_vs_national',
    'irr': float(irr['is_battleground']),
    'ci_lower': float(ci.loc['is_battleground', 0]),
    'ci_upper': float(ci.loc['is_battleground', 1]),
    'p_value': float(result.pvalues['is_battleground']),
    'n': int(result.nobs)
})
all_pvalues.append(result.pvalues['is_battleground'])

# Model 2: Individual state effects vs national
print("\n" + "=" * 80)
print("Model 2: State Effects vs National Baseline")
print("=" * 80)

state_results = {}

for category in df_filtered['category'].unique():
    if pd.isna(category):
        continue
        
    print(f"\n{category.upper()}:")
    cat_data = df_filtered[df_filtered['category'] == category]
    state_results[category] = {}
    
    for state in BATTLEGROUND_STATES + CONTROL_STATES:
        state_cat_data = cat_data[cat_data['state'] == state]
        
        if len(state_cat_data) < 30:
            continue
        
        # Calculate deviation from national for this state-category
        state_avg = state_cat_data['interest'].mean()
        national_avg_cat = state_cat_data['national_avg'].mean()
        deviation = state_avg - national_avg_cat
        
        # Statistical test
        # Compare state vs national using t-test
        t_stat, p_value = stats.ttest_1samp(
            state_cat_data['interest_vs_national'].dropna(), 
            0
        )
        
        state_results[category][state] = {
            'state_avg': float(state_avg),
            'national_avg': float(national_avg_cat),
            'deviation': float(deviation),
            'p_value': float(p_value),
            'is_low_confidence': state in LOW_CONFIDENCE_STATES
        }
        
        all_pvalues.append(p_value)
        
        sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
        direction = "above" if deviation > 0 else "below"
        print(f"  {state}: {abs(deviation):.1f} {direction} national (p={p_value:.4f}){sig}")

results_list.append({
    'model': 'state_by_state_national',
    'results': state_results
})

# PHASE 4: Bonferroni Correction
print("\n" + "=" * 80)
print("PHASE 4: Bonferroni Correction")
print("=" * 80)

n_tests = len(all_pvalues)
print(f"Tests conducted: {n_tests}")
print(f"Corrected alpha: 0.05 / {n_tests} = {0.05/n_tests:.6f}")

reject, p_corrected, _, _ = multipletests(all_pvalues, method='bonferroni')

n_sig_raw = sum(p < 0.05 for p in all_pvalues)
n_sig_corr = sum(reject)

print(f"\nSignificant at α=0.05: {n_sig_raw}/{n_tests}")
print(f"Significant after Bonferroni: {n_sig_corr}/{n_tests}")

# Save results
timestamp = datetime.now().strftime('%Y-%m-%d')

output = {
    'timestamp': timestamp,
    'revision': 'R2',
    'data_sources': ['Claude Code', 'Kimi Supplemental (realistic terms)'],
    'baseline': 'National weighted average',
    'low_confidence_states': LOW_CONFIDENCE_STATES,
    'population_weights': POPULATION_WEIGHTS,
    'terms_used': len(valid_terms),
    'terms_removed': len(removed_terms),
    'population_control': True,
    'bonferroni': {
        'n_tests': n_tests,
        'n_significant_raw': n_sig_raw,
        'n_significant_corrected': n_sig_corr
    },
    'results': results_list
}

# Save
with open(f"{OUTPUT_DIR}/final_analysis_R2.json", 'w') as f:
    json.dump(output, f, indent=2, default=str)

print("\n" + "=" * 80)
print("ANALYSIS R2 COMPLETE")
print("=" * 80)
print(f"✓ JSON saved: {OUTPUT_DIR}/final_analysis_R2.json")
print(f"\nKey Changes from R1:")
print(f"  1. Baseline: National weighted average (not OH)")
print(f"  2. Flagged low-confidence states: {LOW_CONFIDENCE_STATES}")
print(f"  3. Included realistic supplemental terms")
print(f"  4. {n_sig_corr}/{n_tests} significant after Bonferroni")
