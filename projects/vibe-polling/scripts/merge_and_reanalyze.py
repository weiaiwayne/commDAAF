#!/usr/bin/env python3
"""
Data Merge and Re-Analysis — Claude Code
VibePoll-2026 | CommDAAF v1.0

This script merges data from multiple agents and re-runs temporal analysis
with REAL market data (not synthetic proxy).

Data Sources:
1. Claude Code: trends_normalized.parquet (38,311 records)
2. Codex: independent_merged_timeseries.csv (time-matched market odds)
3. Codex: r2_new_terms_2026-03-20.parquet (11,466 records, 12 terms)
4. Kimi: trends_supplemental_2026-03-20.parquet (17,381 records, 20 terms)
"""

import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
import json
import warnings
warnings.filterwarnings('ignore')

import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests, adfuller

# Paths
BASE_DIR = "/root/.openclaw/workspace/projects/vibe-polling"
OUTPUT_DIR = f"{BASE_DIR}/agents/claude-code/analysis"
COMBINED_DIR = f"{BASE_DIR}/data/combined"

# State classifications
BATTLEGROUND = ['PA', 'MI', 'WI', 'GA', 'AZ', 'NV', 'NC']
CONTROL = ['CA', 'TX', 'OH']
WATCH = ['MN', 'ME', 'NH']

def load_all_data():
    """Load data from all agents."""
    print("="*60)
    print("LOADING DATA FROM ALL AGENTS")
    print("="*60)

    # 1. Claude Code processed data
    claude_trends = pd.read_parquet(f"{BASE_DIR}/data/processed/trends_normalized.parquet")
    claude_vibe = pd.read_csv(f"{BASE_DIR}/data/processed/vibe_indices.csv")
    print(f"\n1. Claude Code trends: {len(claude_trends):,} records")
    print(f"   Claude Code vibe indices: {len(claude_vibe):,} records")

    # 2. Codex time-matched market data (CRITICAL!)
    codex_markets = pd.read_csv(f"{BASE_DIR}/agents/codex/data/processed/independent_merged_timeseries.csv")
    print(f"\n2. Codex market data: {len(codex_markets):,} records")
    print(f"   → House Dem Odds: {codex_markets['house_dem_odds'].min():.3f} - {codex_markets['house_dem_odds'].max():.3f}")
    print(f"   → Senate Dem Odds: {codex_markets['senate_dem_odds'].min():.3f} - {codex_markets['senate_dem_odds'].max():.3f}")

    # 3. Codex new terms
    codex_terms = pd.read_parquet(f"{BASE_DIR}/agents/codex/data/raw/r2_new_terms_2026-03-20.parquet")
    print(f"\n3. Codex new terms: {len(codex_terms):,} records")
    print(f"   → Unique terms: {codex_terms['term'].nunique()}")

    # 4. Kimi supplemental terms
    kimi_terms = pd.read_parquet(f"{BASE_DIR}/agents/kimi-k2.5/agents/kimi-k2.5/data/raw/trends_supplemental/trends_supplemental_2026-03-20.parquet")
    print(f"\n4. Kimi supplemental: {len(kimi_terms):,} records")
    print(f"   → Unique terms: {kimi_terms['term'].nunique()}")

    return {
        'claude_trends': claude_trends,
        'claude_vibe': claude_vibe,
        'codex_markets': codex_markets,
        'codex_terms': codex_terms,
        'kimi_terms': kimi_terms
    }


def merge_vibe_with_markets(claude_vibe, codex_markets):
    """Merge vibe indices with real market data."""
    print("\n" + "="*60)
    print("MERGING VIBE INDEX WITH REAL MARKET DATA")
    print("="*60)

    # Ensure date columns are datetime
    claude_vibe = claude_vibe.copy()
    codex_markets = codex_markets.copy()

    claude_vibe['date'] = pd.to_datetime(claude_vibe['date'])
    codex_markets['date'] = pd.to_datetime(codex_markets['date'])

    # Merge on state and date
    merged = claude_vibe.merge(
        codex_markets[['state', 'date', 'house_dem_odds', 'senate_dem_odds']],
        on=['state', 'date'],
        how='inner'
    )

    print(f"\nMerged records: {len(merged):,}")
    print(f"States: {sorted(merged['state'].unique())}")
    print(f"Date range: {merged['date'].min()} to {merged['date'].max()}")

    return merged


def run_real_correlation_analysis(merged_data):
    """Run correlation analysis with REAL market data."""
    print("\n" + "="*60)
    print("CORRELATION ANALYSIS WITH REAL MARKET DATA")
    print("="*60)

    results = {
        'raw_correlations': {},
        'first_differenced': {},
        'by_market_type': {}
    }

    # Overall correlations
    print("\n--- Overall Correlations ---")

    for market in ['house_dem_odds', 'senate_dem_odds']:
        r, p = stats.pearsonr(merged_data['vibe_index'], merged_data[market])
        print(f"\nVibe Index vs {market}:")
        print(f"  r = {r:.4f}, p = {p:.4e}")
        results['by_market_type'][market] = {'raw_r': float(r), 'raw_p': float(p)}

    # By state
    print("\n--- Correlations by State (Vibe vs House Dem Odds) ---")

    for state in sorted(merged_data['state'].unique()):
        state_data = merged_data[merged_data['state'] == state].sort_values('date')

        if len(state_data) < 30:
            print(f"  {state}: Insufficient data (n={len(state_data)})")
            continue

        vibe = state_data['vibe_index'].values
        house = state_data['house_dem_odds'].values
        senate = state_data['senate_dem_odds'].values

        # Raw correlations
        r_house, p_house = stats.pearsonr(vibe, house)
        r_senate, p_senate = stats.pearsonr(vibe, senate)

        results['raw_correlations'][state] = {
            'house_r': float(r_house),
            'house_p': float(p_house),
            'senate_r': float(r_senate),
            'senate_p': float(p_senate),
            'n': len(state_data)
        }

        state_type = "BG" if state in BATTLEGROUND else ("CTRL" if state in CONTROL else "WATCH")
        sig_h = "*" if p_house < 0.05 else ""
        sig_s = "*" if p_senate < 0.05 else ""
        print(f"  {state} ({state_type}): House r={r_house:.3f}{sig_h}, Senate r={r_senate:.3f}{sig_s}")

    # First-differenced correlations
    print("\n--- First-Differenced Correlations ---")

    for state in sorted(merged_data['state'].unique()):
        state_data = merged_data[merged_data['state'] == state].sort_values('date')

        if len(state_data) < 30:
            continue

        vibe = state_data['vibe_index'].values
        house = state_data['house_dem_odds'].values
        senate = state_data['senate_dem_odds'].values

        # First difference
        vibe_diff = np.diff(vibe)
        house_diff = np.diff(house)
        senate_diff = np.diff(senate)

        # Remove any NaN/inf
        mask = np.isfinite(vibe_diff) & np.isfinite(house_diff) & np.isfinite(senate_diff)
        vibe_diff = vibe_diff[mask]
        house_diff = house_diff[mask]
        senate_diff = senate_diff[mask]

        if len(vibe_diff) < 10:
            continue

        r_house, p_house = stats.pearsonr(vibe_diff, house_diff)
        r_senate, p_senate = stats.pearsonr(vibe_diff, senate_diff)

        results['first_differenced'][state] = {
            'house_r': float(r_house),
            'house_p': float(p_house),
            'senate_r': float(r_senate),
            'senate_p': float(p_senate)
        }

        state_type = "BG" if state in BATTLEGROUND else ("CTRL" if state in CONTROL else "WATCH")
        sig_h = "*" if p_house < 0.05 else ""
        sig_s = "*" if p_senate < 0.05 else ""
        print(f"  {state} ({state_type}): House r={r_house:.3f}{sig_h}, Senate r={r_senate:.3f}{sig_s}")

    # Summary
    print("\n--- Summary ---")
    raw_house_sig = sum(1 for s in results['raw_correlations'].values() if s['house_p'] < 0.05)
    raw_senate_sig = sum(1 for s in results['raw_correlations'].values() if s['senate_p'] < 0.05)
    diff_house_sig = sum(1 for s in results['first_differenced'].values() if s['house_p'] < 0.05)
    diff_senate_sig = sum(1 for s in results['first_differenced'].values() if s['senate_p'] < 0.05)

    total = len(results['raw_correlations'])
    print(f"Raw House correlations significant: {raw_house_sig}/{total}")
    print(f"Raw Senate correlations significant: {raw_senate_sig}/{total}")
    print(f"Differenced House significant: {diff_house_sig}/{len(results['first_differenced'])}")
    print(f"Differenced Senate significant: {diff_senate_sig}/{len(results['first_differenced'])}")

    if raw_house_sig > diff_house_sig:
        print("\n→ Correlation collapse after differencing suggests SPURIOUS relationship")

    results['summary'] = {
        'raw_house_sig': raw_house_sig,
        'raw_senate_sig': raw_senate_sig,
        'diff_house_sig': diff_house_sig,
        'diff_senate_sig': diff_senate_sig,
        'total_states': total
    }

    return results


def run_real_granger_causality(merged_data):
    """Run Granger causality with REAL market data."""
    print("\n" + "="*60)
    print("GRANGER CAUSALITY WITH REAL MARKET DATA")
    print("="*60)

    results = {
        'vibe_to_house': {},
        'house_to_vibe': {},
        'vibe_to_senate': {},
        'senate_to_vibe': {},
        'summary': {}
    }

    max_lag = 4

    print(f"\nTesting lags 1-{max_lag} days")
    print("Significance threshold: p < 0.05")

    # Test for each state
    print("\n--- Vibe Index → House Dem Odds ---")

    vibe_house_sig = 0
    house_vibe_sig = 0
    vibe_senate_sig = 0
    senate_vibe_sig = 0
    tested = 0

    for state in sorted(merged_data['state'].unique()):
        state_data = merged_data[merged_data['state'] == state].sort_values('date')

        if len(state_data) < 30:
            continue

        tested += 1
        vibe = state_data['vibe_index'].values
        house = state_data['house_dem_odds'].values
        senate = state_data['senate_dem_odds'].values

        # Test Vibe → House
        df_vh = pd.DataFrame({'house': house, 'vibe': vibe})
        try:
            test_vh = grangercausalitytests(df_vh, maxlag=max_lag, verbose=False)
            pvals = [test_vh[lag][0]['ssr_ftest'][1] for lag in range(1, max_lag+1)]
            min_p = min(pvals)
            best_lag = pvals.index(min_p) + 1

            results['vibe_to_house'][state] = {
                'min_p': float(min_p),
                'best_lag': best_lag,
                'significant': min_p < 0.05
            }

            if min_p < 0.05:
                vibe_house_sig += 1

            state_type = "BG" if state in BATTLEGROUND else ("CTRL" if state in CONTROL else "WATCH")
            sig = "*" if min_p < 0.05 else ""
            print(f"  {state} ({state_type}): p={min_p:.4f} (lag={best_lag}) {sig}")

        except Exception as e:
            print(f"  {state}: ERROR - {e}")
            results['vibe_to_house'][state] = {'error': str(e)}

    # Test House → Vibe
    print("\n--- House Dem Odds → Vibe Index ---")

    for state in sorted(merged_data['state'].unique()):
        state_data = merged_data[merged_data['state'] == state].sort_values('date')

        if len(state_data) < 30:
            continue

        vibe = state_data['vibe_index'].values
        house = state_data['house_dem_odds'].values

        df_hv = pd.DataFrame({'vibe': vibe, 'house': house})
        try:
            test_hv = grangercausalitytests(df_hv, maxlag=max_lag, verbose=False)
            pvals = [test_hv[lag][0]['ssr_ftest'][1] for lag in range(1, max_lag+1)]
            min_p = min(pvals)
            best_lag = pvals.index(min_p) + 1

            results['house_to_vibe'][state] = {
                'min_p': float(min_p),
                'best_lag': best_lag,
                'significant': min_p < 0.05
            }

            if min_p < 0.05:
                house_vibe_sig += 1

            state_type = "BG" if state in BATTLEGROUND else ("CTRL" if state in CONTROL else "WATCH")
            sig = "*" if min_p < 0.05 else ""
            print(f"  {state} ({state_type}): p={min_p:.4f} (lag={best_lag}) {sig}")

        except Exception as e:
            results['house_to_vibe'][state] = {'error': str(e)}

    # Test Vibe → Senate
    print("\n--- Vibe Index → Senate Dem Odds ---")

    for state in sorted(merged_data['state'].unique()):
        state_data = merged_data[merged_data['state'] == state].sort_values('date')

        if len(state_data) < 30:
            continue

        vibe = state_data['vibe_index'].values
        senate = state_data['senate_dem_odds'].values

        df_vs = pd.DataFrame({'senate': senate, 'vibe': vibe})
        try:
            test_vs = grangercausalitytests(df_vs, maxlag=max_lag, verbose=False)
            pvals = [test_vs[lag][0]['ssr_ftest'][1] for lag in range(1, max_lag+1)]
            min_p = min(pvals)
            best_lag = pvals.index(min_p) + 1

            results['vibe_to_senate'][state] = {
                'min_p': float(min_p),
                'best_lag': best_lag,
                'significant': min_p < 0.05
            }

            if min_p < 0.05:
                vibe_senate_sig += 1

            state_type = "BG" if state in BATTLEGROUND else ("CTRL" if state in CONTROL else "WATCH")
            sig = "*" if min_p < 0.05 else ""
            print(f"  {state} ({state_type}): p={min_p:.4f} (lag={best_lag}) {sig}")

        except Exception as e:
            results['vibe_to_senate'][state] = {'error': str(e)}

    # Summary
    results['summary'] = {
        'vibe_to_house_sig': vibe_house_sig,
        'house_to_vibe_sig': house_vibe_sig,
        'vibe_to_senate_sig': vibe_senate_sig,
        'tested': tested
    }

    print("\n--- Summary ---")
    print(f"Vibe → House significant: {vibe_house_sig}/{tested} states")
    print(f"House → Vibe significant: {house_vibe_sig}/{tested} states")
    print(f"Vibe → Senate significant: {vibe_senate_sig}/{tested} states")

    if vibe_house_sig == 0 and vibe_senate_sig == 0:
        print("\n→ NO evidence that Google Trends predicts market movements")
    elif vibe_house_sig < tested // 2:
        print("\n→ WEAK/INCONSISTENT evidence for prediction")
    else:
        print("\n→ SOME evidence for predictive relationship")

    return results


def analyze_supplemental_terms(kimi_terms, codex_terms):
    """Analyze the realistic/colloquial terms from other agents."""
    print("\n" + "="*60)
    print("ANALYZING SUPPLEMENTAL SEARCH TERMS")
    print("="*60)

    results = {
        'kimi_terms': {},
        'codex_terms': {},
        'combined_quality': {}
    }

    # Standardize state codes
    kimi_terms = kimi_terms.copy()
    kimi_terms['state'] = kimi_terms['state'].str.replace('US-', '')

    # Analyze Kimi terms
    print("\n--- Kimi Supplemental Terms Quality ---")
    print(f"Total records: {len(kimi_terms):,}")
    print(f"Unique terms: {kimi_terms['term'].nunique()}")

    for term in sorted(kimi_terms['term'].unique()):
        term_data = kimi_terms[kimi_terms['term'] == term]
        pct_zeros = (term_data['interest'] == 0).sum() / len(term_data) * 100
        mean_interest = term_data['interest'].mean()

        status = "✓ VALID" if pct_zeros < 50 else "✗ LOW SIGNAL"
        results['kimi_terms'][term] = {
            'pct_zeros': float(pct_zeros),
            'mean_interest': float(mean_interest),
            'valid': pct_zeros < 50
        }
        print(f"  {term}: {pct_zeros:.1f}% zeros, mean={mean_interest:.1f} [{status}]")

    # Analyze Codex terms
    print("\n--- Codex R2 Terms Quality ---")
    print(f"Total records: {len(codex_terms):,}")

    for term in sorted(codex_terms['term'].unique()):
        term_data = codex_terms[codex_terms['term'] == term]
        pct_zeros = (term_data['interest'] == 0).sum() / len(term_data) * 100
        mean_interest = term_data['interest'].mean()

        status = "✓ VALID" if pct_zeros < 50 else "✗ LOW SIGNAL"
        results['codex_terms'][term] = {
            'pct_zeros': float(pct_zeros),
            'mean_interest': float(mean_interest),
            'valid': pct_zeros < 50
        }
        print(f"  {term}: {pct_zeros:.1f}% zeros, mean={mean_interest:.1f} [{status}]")

    # Summary
    kimi_valid = sum(1 for t in results['kimi_terms'].values() if t['valid'])
    codex_valid = sum(1 for t in results['codex_terms'].values() if t['valid'])

    print(f"\n--- Summary ---")
    print(f"Kimi valid terms: {kimi_valid}/{len(results['kimi_terms'])}")
    print(f"Codex valid terms: {codex_valid}/{len(results['codex_terms'])}")

    results['combined_quality'] = {
        'kimi_valid': kimi_valid,
        'kimi_total': len(results['kimi_terms']),
        'codex_valid': codex_valid,
        'codex_total': len(results['codex_terms'])
    }

    return results


def write_updated_conclusions(corr_results, granger_results, term_results):
    """Write updated conclusions with real market data."""

    with open(f"{OUTPUT_DIR}/INDEPENDENT_CONCLUSIONS_UPDATED.md", 'w') as f:
        f.write("# INDEPENDENT CONCLUSIONS — UPDATED WITH MERGED DATA\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("**Agent:** Claude Code (Claude Opus 4.5)\n")
        f.write("**Framework:** CommDAAF v1.0\n\n")
        f.write("---\n\n")

        f.write("## Data Sources Merged\n\n")
        f.write("This analysis combines data from multiple agents:\n\n")
        f.write("| Source | Data Type | Records |\n")
        f.write("|--------|-----------|--------|\n")
        f.write("| Claude Code | Processed trends | 38,311 |\n")
        f.write("| Codex | Time-matched market odds | 1,183 |\n")
        f.write("| Codex | R2 new terms | 11,466 |\n")
        f.write("| Kimi | Supplemental terms | 17,381 |\n\n")

        f.write("**Critical improvement:** Codex provided time-matched market data (House & Senate Dem odds) that overlaps with our Google Trends data (Dec 2025 - Mar 2026).\n\n")

        f.write("---\n\n")

        f.write("## Primary Research Question\n\n")
        f.write("**Does Google Trends data predict prediction market movements?**\n\n")

        # Determine answer based on Granger results
        vibe_house = granger_results['summary']['vibe_to_house_sig']
        vibe_senate = granger_results['summary']['vibe_to_senate_sig']
        tested = granger_results['summary']['tested']

        if vibe_house == 0 and vibe_senate == 0:
            f.write("### Answer: **NO**\n\n")
            f.write(f"Granger causality tests with REAL market data show:\n")
            f.write(f"- Vibe Index → House odds: {vibe_house}/{tested} states significant\n")
            f.write(f"- Vibe Index → Senate odds: {vibe_senate}/{tested} states significant\n\n")
            f.write("**Google Trends does NOT predict market movements.**\n\n")
        elif vibe_house + vibe_senate < tested:
            f.write("### Answer: **WEAK/INCONSISTENT**\n\n")
            f.write(f"Granger causality shows mixed results:\n")
            f.write(f"- Vibe Index → House odds: {vibe_house}/{tested} states significant\n")
            f.write(f"- Vibe Index → Senate odds: {vibe_senate}/{tested} states significant\n\n")
            f.write("Evidence is too inconsistent to claim predictive power.\n\n")
        else:
            f.write("### Answer: **SOME EVIDENCE**\n\n")
            f.write(f"Granger causality shows:\n")
            f.write(f"- Vibe Index → House odds: {vibe_house}/{tested} states significant\n")
            f.write(f"- Vibe Index → Senate odds: {vibe_senate}/{tested} states significant\n\n")

        f.write("---\n\n")

        f.write("## Correlation Analysis (Real Market Data)\n\n")

        summary = corr_results['summary']
        f.write(f"| Metric | Raw | First-Differenced |\n")
        f.write(f"|--------|-----|-------------------|\n")
        f.write(f"| House correlations significant | {summary['raw_house_sig']}/{summary['total_states']} | {summary['diff_house_sig']}/{summary['total_states']} |\n")
        f.write(f"| Senate correlations significant | {summary['raw_senate_sig']}/{summary['total_states']} | {summary['diff_senate_sig']}/{summary['total_states']} |\n\n")

        if summary['raw_house_sig'] > summary['diff_house_sig']:
            f.write("**Conclusion:** Correlations collapse after first-differencing, confirming SPURIOUS relationship.\n\n")

        f.write("---\n\n")

        f.write("## Supplemental Terms Analysis\n\n")
        f.write("Realistic/colloquial terms collected by Kimi and Codex:\n\n")

        quality = term_results['combined_quality']
        f.write(f"| Source | Valid Terms | Total | Pass Rate |\n")
        f.write(f"|--------|-------------|-------|----------|\n")
        f.write(f"| Kimi | {quality['kimi_valid']} | {quality['kimi_total']} | {quality['kimi_valid']/quality['kimi_total']*100:.0f}% |\n")
        f.write(f"| Codex | {quality['codex_valid']} | {quality['codex_total']} | {quality['codex_valid']/quality['codex_total']*100:.0f}% |\n\n")

        f.write("**Valid terms (>50% non-zero):**\n")
        for term, data in term_results['kimi_terms'].items():
            if data['valid']:
                f.write(f"- `{term}` ({data['pct_zeros']:.1f}% zeros)\n")

        f.write("\n**Failed terms (>50% zeros):**\n")
        failed = [t for t, d in term_results['kimi_terms'].items() if not d['valid']]
        for term in failed[:5]:
            f.write(f"- `{term}` ({term_results['kimi_terms'][term]['pct_zeros']:.1f}% zeros)\n")
        if len(failed) > 5:
            f.write(f"- ... and {len(failed)-5} more\n")

        f.write("\n---\n\n")

        f.write("## Final Conclusion\n\n")
        f.write("**With real market data merged from Codex, my independent conclusion is:**\n\n")

        if vibe_house == 0 and vibe_senate == 0:
            f.write("**Google Trends does NOT predict prediction market movements.**\n\n")
            f.write("The initial conclusion from synthetic proxy analysis is CONFIRMED by real data.\n\n")
        else:
            f.write("**Evidence is mixed/weak for predictive relationship.**\n\n")

        f.write("**Descriptive value remains:** Google Trends provides valuable insights about voter attention and issue salience, even without predictive power.\n\n")

        f.write("---\n\n")
        f.write("*Updated analysis with merged agent data*\n")
        f.write("*Claude Code (Claude Opus 4.5) | VibePoll-2026 | CommDAAF v1.0*\n")

    print(f"\nWrote: {OUTPUT_DIR}/INDEPENDENT_CONCLUSIONS_UPDATED.md")


def save_combined_data(merged_vibe_markets, kimi_terms, codex_terms):
    """Save combined dataset for future use."""
    import os
    os.makedirs(COMBINED_DIR, exist_ok=True)

    merged_vibe_markets.to_csv(f"{COMBINED_DIR}/vibe_with_markets.csv", index=False)
    print(f"Saved: {COMBINED_DIR}/vibe_with_markets.csv")

    # Metadata
    metadata = {
        'created_at': datetime.now().isoformat(),
        'created_by': 'Claude Code',
        'sources': {
            'vibe_indices': 'Claude Code processed data',
            'market_odds': 'Codex independent_merged_timeseries.csv',
            'kimi_terms': 'Kimi supplemental_2026-03-20.parquet',
            'codex_terms': 'Codex r2_new_terms_2026-03-20.parquet'
        },
        'records': {
            'merged_vibe_markets': len(merged_vibe_markets),
            'kimi_terms': len(kimi_terms),
            'codex_terms': len(codex_terms)
        }
    }

    with open(f"{COMBINED_DIR}/data_sources.json", 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"Saved: {COMBINED_DIR}/data_sources.json")


def main():
    """Main analysis pipeline with merged data."""
    print("="*60)
    print("CLAUDE CODE — MERGED DATA RE-ANALYSIS")
    print("VibePoll-2026 | CommDAAF v1.0")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)

    # Load all data
    data = load_all_data()

    # Merge vibe with real market data
    merged = merge_vibe_with_markets(data['claude_vibe'], data['codex_markets'])

    # Run correlation with real data
    corr_results = run_real_correlation_analysis(merged)

    # Run Granger with real data
    granger_results = run_real_granger_causality(merged)

    # Analyze supplemental terms
    term_results = analyze_supplemental_terms(data['kimi_terms'], data['codex_terms'])

    # Save combined data
    save_combined_data(merged, data['kimi_terms'], data['codex_terms'])

    # Write updated conclusions
    write_updated_conclusions(corr_results, granger_results, term_results)

    print("\n" + "="*60)
    print("MERGED ANALYSIS COMPLETE")
    print("="*60)

    return {
        'correlation': corr_results,
        'granger': granger_results,
        'terms': term_results
    }


if __name__ == "__main__":
    main()
