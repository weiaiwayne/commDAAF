#!/usr/bin/env python3
"""
CommDAAF-Compliant Statistical Modeling - ALL Battleground States
Agent: Kimi K2.5 (Independent Analysis)
Framework: CommDAAF v1.0

Uses Negative Binomial regression with full state coverage.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import json
import os
from datetime import datetime

# Paths
DATA_PATH = "agents/kimi-k2.5/data/raw/trends/trends_full_2026-03-19.parquet"
OUTPUT_DIR = "agents/kimi-k2.5/analysis/models"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# State classifications
BATTLEGROUND_STATES = ['PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC']
CONTROL_STATES = ['CA', 'TX', 'OH']
WATCH_STATES = ['ME', 'NH', 'MN']

def prepare_data(df):
    """Prepare data for modeling."""
    print("Preparing data...")
    
    df['date'] = pd.to_datetime(df['date'])
    
    # Create state type indicator
    df['state_type'] = df['state'].apply(
        lambda x: 'battleground' if x in BATTLEGROUND_STATES 
        else 'control' if x in CONTROL_STATES 
        else 'watch'
    )
    
    # Time features
    df['days_since_start'] = (df['date'] - df['date'].min()).dt.days
    df['week'] = df['date'].dt.isocalendar().week
    
    # Individual state dummies
    for state in BATTLEGROUND_STATES + CONTROL_STATES:
        df[f'is_{state}'] = (df['state'] == state).astype(int)
    
    return df

def run_comprehensive_analysis(df):
    """Run analysis with all states."""
    print("\n" + "=" * 80)
    print("CommDAAF Statistical Modeling - ALL Battleground States")
    print("=" * 80)
    print()
    
    results_list = []
    
    # Model 1: Battleground vs Control (pooled)
    print("Model 1: Battleground vs Control States (Pooled)")
    print("-" * 80)
    
    # Filter to battleground and control only
    df_pooled = df[df['state_type'].isin(['battleground', 'control'])]
    df_pooled['is_battleground'] = (df_pooled['state_type'] == 'battleground').astype(int)
    
    y = df_pooled['interest']
    X = pd.DataFrame({
        'const': 1,
        'is_battleground': df_pooled['is_battleground'],
        'days_since_start': df_pooled['days_since_start']
    })
    
    try:
        model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
        result = model.fit()
        
        irr = np.exp(result.params)
        ci = np.exp(result.conf_int())
        
        print(f"✓ Model converged")
        print(f"  Battleground effect: IRR = {irr['is_battleground']:.3f} "
              f"(95% CI: {ci.loc['is_battleground', 0]:.3f} - {ci.loc['is_battleground', 1]:.3f})")
        print(f"  p-value: {result.pvalues['is_battleground']:.4f}")
        
        results_list.append({
            'model': 'battleground_vs_control_pooled',
            'converged': True,
            'n_obs': int(result.nobs),
            'irr_battleground': float(irr['is_battleground']),
            'ci_lower': float(ci.loc['is_battleground', 0]),
            'ci_upper': float(ci.loc['is_battleground', 1]),
            'p_value': float(result.pvalues['is_battleground'])
        })
        
    except Exception as e:
        print(f"✗ Model failed: {e}")
        results_list.append({'model': 'battleground_vs_control_pooled', 'converged': False, 'error': str(e)})
    
    # Model 2: Individual Battleground State Effects
    print("\n\nModel 2: Individual Battleground State Effects (vs CA baseline)")
    print("-" * 80)
    
    state_results = {}
    baseline_state = 'CA'
    
    for category in df['category'].unique():
        print(f"\n{category.upper()}:")
        cat_data = df[df['category'] == category]
        
        state_results[category] = {}
        
        for state in BATTLEGROUND_STATES:
            # Compare state vs CA baseline
            state_cat_data = cat_data[cat_data['state'].isin([state, baseline_state])]
            
            if len(state_cat_data) < 50:
                continue
            
            y_state = state_cat_data['interest']
            X_state = pd.DataFrame({
                'const': 1,
                'is_target_state': (state_cat_data['state'] == state).astype(int),
                'days_since_start': state_cat_data['days_since_start']
            })
            
            try:
                model_state = sm.GLM(y_state, X_state, family=sm.families.NegativeBinomial())
                result_state = model_state.fit()
                
                irr_state = np.exp(result_state.params['is_target_state'])
                ci_state = np.exp(result_state.conf_int().loc['is_target_state'])
                p_state = result_state.pvalues['is_target_state']
                
                state_results[category][state] = {
                    'irr': float(irr_state),
                    'ci_lower': float(ci_state[0]),
                    'ci_upper': float(ci_state[1]),
                    'p_value': float(p_state),
                    'n_obs': int(result_state.nobs)
                }
                
                sig = "***" if p_state < 0.001 else "**" if p_state < 0.01 else "*" if p_state < 0.05 else ""
                print(f"  {state}: IRR = {irr_state:.3f} (p = {p_state:.4f}){sig}")
                
            except Exception as e:
                print(f"  {state}: Failed - {e}")
    
    results_list.append({
        'model': 'individual_state_effects',
        'baseline': baseline_state,
        'results': state_results
    })
    
    # Model 3: Category Rankings by State
    print("\n\nModel 3: Issue Salience Rankings by State")
    print("-" * 80)
    
    rankings = {}
    
    for state in BATTLEGROUND_STATES + ['CA']:
        state_data = df[df['state'] == state]
        
        category_means = state_data.groupby('category')['interest'].mean().sort_values(ascending=False)
        
        rankings[state] = {
            'top_issue': category_means.index[0],
            'top_interest': float(category_means.iloc[0]),
            'ranking': {cat: float(val) for cat, val in category_means.items()}
        }
        
        print(f"\n{state}:")
        print(f"  Top issue: {category_means.index[0]} ({category_means.iloc[0]:.1f})")
        print(f"  2nd: {category_means.index[1]} ({category_means.iloc[1]:.1f})")
        print(f"  3rd: {category_means.index[2]} ({category_means.iloc[2]:.1f})")
    
    results_list.append({
        'model': 'state_issue_rankings',
        'rankings': rankings
    })
    
    return results_list

def interpret_comprehensive_results(results):
    """Interpret results across all states."""
    print("\n\n" + "=" * 80)
    print("Effect Size Interpretation - All States")
    print("=" * 80)
    print()
    
    interpretations = []
    
    # Interpret pooled battleground effect
    for model_result in results:
        if model_result.get('model') == 'battleground_vs_control_pooled' and model_result.get('converged'):
            irr = model_result['irr_battleground']
            ci_low = model_result['ci_lower']
            ci_high = model_result['ci_upper']
            p = model_result['p_value']
            
            if irr > 1:
                change = (irr - 1) * 100
                direction = f"{change:.1f}% higher"
            else:
                change = (1 - irr) * 100
                direction = f"{change:.1f}% lower"
            
            sig = "significant" if p < 0.05 else "not significant"
            
            interp = (f"Battleground states show {direction} search interest compared to control states "
                     f"(IRR = {irr:.3f}, 95% CI: {ci_low:.3f} - {ci_high:.3f}), p = {p:.4f} ({sig}).")
            
            print(f"BATTLEGROUND EFFECT:\n  {interp}\n")
            interpretations.append({'parameter': 'battleground_vs_control', 'interpretation': interp})
    
    # Interpret individual state effects
    for model_result in results:
        if model_result.get('model') == 'individual_state_effects':
            print("STATE-SPECIFIC EFFECTS (vs California baseline):\n")
            
            for category, states in model_result['results'].items():
                print(f"  {category.upper()}:")
                for state, res in states.items():
                    irr = res['irr']
                    p = res['p_value']
                    
                    if irr > 1:
                        change = (irr - 1) * 100
                        direction = f"{change:.1f}% higher"
                    else:
                        change = (1 - irr) * 100
                        direction = f"{change:.1f}% lower"
                    
                    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
                    
                    print(f"    {state}: {direction} than CA (IRR={irr:.3f}){sig}")
                    
                    interp = f"{state} shows {direction} {category} search interest vs CA (IRR={irr:.3f}, p={p:.4f})"
                    interpretations.append({'parameter': f'{category}_{state}', 'interpretation': interp})
                print()
    
    return interpretations

def save_comprehensive_results(results, interpretations):
    """Save all results."""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    # JSON
    json_file = f"{OUTPUT_DIR}/comprehensive_regression_results.json"
    with open(json_file, 'w') as f:
        json.dump({
            'agent': 'kimi-k2.5',
            'framework': 'commdaaf-v1.0',
            'date': timestamp,
            'data_source': 'google_trends_real',
            'model_type': 'Negative Binomial',
            'states_included': {
                'battleground': BATTLEGROUND_STATES,
                'control': CONTROL_STATES,
                'watch': WATCH_STATES
            },
            'results': results,
            'interpretations': interpretations
        }, f, indent=2, default=str)
    
    # Markdown report
    md_file = "agents/kimi-k2.5/comprehensive_regression_table.md"
    with open(md_file, 'w') as f:
        f.write("# Comprehensive Statistical Modeling Results\n\n")
        f.write(f"**Agent:** Kimi K2.5  \n")
        f.write(f"**Framework:** CommDAAF v1.0  \n")
        f.write(f"**Date:** {timestamp}  \n")
        f.write(f"**States:** All 7 battlegrounds + 3 controls + 3 watch  \n\n")
        
        f.write("## Battleground States Analyzed\n\n")
        f.write(f"**Tier 1:** {', '.join(['PA', 'MI', 'WI', 'AZ', 'GA'])}  \n")
        f.write(f"**Tier 2:** {', '.join(['NV', 'NC'])}  \n")
        f.write(f"**Control:** {', '.join(CONTROL_STATES)}  \n\n")
        
        # Pooled results
        for model_result in results:
            if model_result.get('model') == 'battleground_vs_control_pooled' and model_result.get('converged'):
                f.write("## Pooled Battleground vs Control\n\n")
                f.write(f"- **N:** {model_result['n_obs']:,}  \n")
                f.write(f"- **IRR (Battleground effect):** {model_result['irr_battleground']:.3f}  \n")
                f.write(f"- **95% CI:** {model_result['ci_lower']:.3f} - {model_result['ci_upper']:.3f}  \n")
                f.write(f"- **p-value:** {model_result['p_value']:.4f}  \n\n")
                
                if model_result['irr_battleground'] > 1:
                    f.write(f"**Interpretation:** Battleground states show {(model_result['irr_battleground']-1)*100:.1f}% higher search interest than control states.  \n\n")
                else:
                    f.write(f"**Interpretation:** Battleground states show {(1-model_result['irr_battleground'])*100:.1f}% lower search interest than control states.  \n\n")
        
        # Individual state effects
        for model_result in results:
            if model_result.get('model') == 'individual_state_effects':
                f.write("## Individual State Effects (vs California)\n\n")
                
                for category, states in model_result['results'].items():
                    f.write(f"### {category.upper()}\n\n")
                    f.write("| State | IRR | 95% CI | p-value | Interpretation |\n")
                    f.write("|-------|-----|--------|---------|----------------|\n")
                    
                    for state, res in sorted(states.items(), key=lambda x: x[1]['irr'], reverse=True):
                        sig = "***" if res['p_value'] < 0.001 else "**" if res['p_value'] < 0.01 else "*" if res['p_value'] < 0.05 else ""
                        
                        if res['irr'] > 1:
                            interp = f"+{(res['irr']-1)*100:.1f}% vs CA"
                        else:
                            interp = f"-{(1-res['irr'])*100:.1f}% vs CA"
                        
                        f.write(f"| {state} | {res['irr']:.3f} | {res['ci_lower']:.3f}-{res['ci_upper']:.3f} | {res['p_value']:.4f}{sig} | {interp} |\n")
                    
                    f.write("\n")
        
        # Rankings
        for model_result in results:
            if model_result.get('model') == 'state_issue_rankings':
                f.write("## Issue Salience Rankings by State\n\n")
                f.write("| State | Top Issue | Avg Interest | 2nd Issue | 3rd Issue |\n")
                f.write("|-------|-----------|--------------|-----------|-----------|\n")
                
                for state, ranking in sorted(model_result['rankings'].items()):
                    top3 = list(ranking['ranking'].items())[:3]
                    f.write(f"| {state} | {top3[0][0]} ({top3[0][1]:.1f}) | {ranking['top_interest']:.1f} | {top3[1][0]} ({top3[1][1]:.1f}) | {top3[2][0]} ({top3[2][1]:.1f}) |\n")
                
                f.write("\n")
    
    print(f"\n{'=' * 80}")
    print("Comprehensive Results Saved!")
    print(f"{'=' * 80}")
    print(f"✓ JSON: {json_file}")
    print(f"✓ Markdown: {md_file}")

def main():
    """Main analysis."""
    print("=" * 80)
    print("VibePoll-2026: Comprehensive Multi-State Analysis")
    print("Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print("=" * 80)
    print()
    
    # Load data
    print(f"Loading data from: {DATA_PATH}")
    df = pd.read_parquet(DATA_PATH)
    print(f"✓ Loaded {len(df):,} records")
    print(f"✓ States: {df['state'].nunique()}")
    print(f"✓ Categories: {df['category'].nunique()}")
    print()
    
    # Prepare
    df = prepare_data(df)
    
    # Run analysis
    results = run_comprehensive_analysis(df)
    
    # Interpret
    interpretations = interpret_comprehensive_results(results)
    
    # Save
    save_comprehensive_results(results, interpretations)
    
    print("\n" + "=" * 80)
    print("Comprehensive Analysis Complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
