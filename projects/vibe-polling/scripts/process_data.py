#!/usr/bin/env python3
"""
Data Processing Pipeline for VibePoll-2026

CommDAAF v1.0 - EXPLORATORY Tier
Processes raw Google Trends data: normalization, z-scores, issue salience indices.

Key transformations:
1. Handle missing values
2. Z-score normalize within term across time
3. Z-score normalize within state across terms
4. Calculate issue salience indices
5. Build Vibe Index per state

Output:
- data/processed/trends_normalized.parquet
- data/processed/issue_salience.csv
- data/processed/vibe_indices.csv
- data/processed/processing_log.md
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
from scipy import stats

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "trends"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"
LOG_DIR = PROJECT_ROOT / "logs"

# Issue weights from PLAN.md
ISSUE_WEIGHTS = {
    'economy': 0.35,
    'immigration': 0.20,
    'political': 0.15,
    'iran_war': 0.15,
    'ai_jobs': 0.10,
    'epstein': 0.05
}

# State populations for per-capita normalization (Census 2020)
STATE_POPULATIONS = {
    'CA': 39538223, 'TX': 29145505, 'PA': 13002700, 'MI': 10077331,
    'GA': 10711908, 'AZ': 7151502, 'WI': 5893718, 'NC': 10439388,
    'NV': 3104614, 'OH': 11799448, 'ME': 1362359, 'NH': 1377529, 'MN': 5706494
}

# Population weights for national aggregates
POPULATION_WEIGHTS = {
    'CA': 0.25, 'TX': 0.18, 'PA': 0.08, 'MI': 0.06, 'GA': 0.07,
    'AZ': 0.04, 'WI': 0.04, 'NC': 0.07, 'NV': 0.02, 'OH': 0.07,
    'ME': 0.01, 'NH': 0.01, 'MN': 0.04
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "processing_log.txt", mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes raw Google Trends data for analysis."""

    def __init__(self):
        self.processing_log: List[Dict] = []
        self.stats = {}

    def log_decision(self, step: str, decision: str, rationale: str,
                     impact: str = None):
        """Log a methodological decision per CommDAAF transparency requirement."""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'step': step,
            'decision': decision,
            'rationale': rationale,
            'impact': impact
        }
        self.processing_log.append(entry)
        logger.info(f"[{step}] {decision}")

    def load_data(self, filepath: Path) -> pd.DataFrame:
        """Load raw trends data."""
        logger.info(f"Loading data from {filepath}")
        df = pd.read_parquet(filepath)

        self.stats['raw_records'] = len(df)
        self.stats['raw_states'] = df['state'].nunique()
        self.stats['raw_terms'] = df['term'].nunique()
        self.stats['raw_categories'] = df['category'].nunique()
        self.stats['date_range'] = (df['date'].min(), df['date'].max())

        self.log_decision(
            'load_data',
            f'Loaded {len(df)} records',
            'Raw parquet file from Google Trends collection',
            f"States: {df['state'].nunique()}, Terms: {df['term'].nunique()}"
        )

        return df

    def filter_low_signal_terms(self, df: pd.DataFrame, max_zero_pct: float = 0.50) -> pd.DataFrame:
        """Filter out terms with too many zeros (per reviewer critique)."""
        logger.info(f"Filtering terms with >{max_zero_pct*100:.0f}% zeros...")

        # Calculate zero percentage per term
        zero_pct = df.groupby('term')['interest'].apply(lambda x: (x == 0).sum() / len(x))

        # Identify low-signal terms
        low_signal_terms = zero_pct[zero_pct > max_zero_pct].index.tolist()
        high_signal_terms = zero_pct[zero_pct <= max_zero_pct].index.tolist()

        # Log removed terms
        if low_signal_terms:
            self.log_decision(
                'filter_low_signal',
                f'Removed {len(low_signal_terms)} terms with >{max_zero_pct*100:.0f}% zeros',
                'Per reviewer critique: terms with 80-99% zeros have no signal',
                f'Removed: {low_signal_terms[:10]}...' if len(low_signal_terms) > 10 else f'Removed: {low_signal_terms}'
            )

        # Filter dataframe
        df_filtered = df[df['term'].isin(high_signal_terms)].copy()

        self.stats['terms_before_filter'] = df['term'].nunique()
        self.stats['terms_after_filter'] = df_filtered['term'].nunique()
        self.stats['low_signal_terms_removed'] = len(low_signal_terms)

        logger.info(f"  Kept {len(high_signal_terms)} terms, removed {len(low_signal_terms)}")

        return df_filtered

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values in the dataset."""
        logger.info("Handling missing values...")

        # Check for missing values
        missing_counts = df.isnull().sum()
        total_missing = missing_counts.sum()

        if total_missing == 0:
            self.log_decision(
                'missing_values',
                'No missing values found',
                'Data is complete from collection',
                'No imputation needed'
            )
            return df

        # Log missing value analysis
        self.log_decision(
            'missing_values',
            f'Found {total_missing} missing values',
            'Analyzing pattern of missingness',
            str(missing_counts[missing_counts > 0].to_dict())
        )

        # For interest values: fill with 0 (Google Trends returns 0 for no searches)
        if 'interest' in df.columns and df['interest'].isnull().any():
            missing_interest = df['interest'].isnull().sum()
            df['interest'] = df['interest'].fillna(0)

            self.log_decision(
                'missing_values',
                f'Filled {missing_interest} missing interest values with 0',
                'Google Trends returns 0 for terms with no search volume',
                'Conservative approach - assumes no searches'
            )

        self.stats['missing_handled'] = total_missing
        return df

    def normalize_zscore(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply z-score normalization."""
        logger.info("Applying z-score normalization...")

        # Z-score within each term across time (temporal normalization)
        df['z_temporal'] = df.groupby(['state', 'term'])['interest'].transform(
            lambda x: stats.zscore(x, nan_policy='omit') if x.std() > 0 else 0
        )

        self.log_decision(
            'normalization',
            'Applied temporal z-score (within term, across time)',
            'Normalizes each term relative to its own history',
            'Enables comparison of term trends regardless of baseline volume'
        )

        # Z-score within each state across terms (cross-term normalization)
        df['z_crossterm'] = df.groupby(['state', 'date'])['interest'].transform(
            lambda x: stats.zscore(x, nan_policy='omit') if x.std() > 0 else 0
        )

        self.log_decision(
            'normalization',
            'Applied cross-term z-score (within state-date, across terms)',
            'Normalizes terms relative to other terms on same day',
            'Shows which terms are unusually high/low for that state-day'
        )

        # Combined z-score (average of both)
        df['z_combined'] = (df['z_temporal'] + df['z_crossterm']) / 2

        self.log_decision(
            'normalization',
            'Created combined z-score (average of temporal and cross-term)',
            'Balanced measure capturing both temporal and relative salience',
            'Primary metric for Vibe Index calculation'
        )

        # Handle any NaN from zscore calculation
        for col in ['z_temporal', 'z_crossterm', 'z_combined']:
            nan_count = df[col].isna().sum()
            if nan_count > 0:
                df[col] = df[col].fillna(0)
                logger.info(f"  Filled {nan_count} NaN values in {col} with 0")

        self.stats['z_temporal_mean'] = df['z_temporal'].mean()
        self.stats['z_temporal_std'] = df['z_temporal'].std()

        return df

    def normalize_population(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply per-capita normalization to control for state population."""
        logger.info("Applying per-capita normalization...")

        # Add population column
        df['population'] = df['state'].map(STATE_POPULATIONS)
        df['log_population'] = np.log(df['population'])

        # Per-capita interest (per million residents)
        df['interest_per_capita'] = df['interest'] / df['population'] * 1e6

        self.log_decision(
            'population_normalization',
            'Applied per-capita normalization (interest per million residents)',
            'Controls for state population differences (CA 39M vs NH 1.4M)',
            'Addresses reviewer critique: raw CA searches 3.4x higher than NH'
        )

        # Z-score on per-capita values
        df['z_per_capita'] = df.groupby(['state', 'term'])['interest_per_capita'].transform(
            lambda x: stats.zscore(x, nan_policy='omit') if x.std() > 0 else 0
        )

        # Handle NaN
        if df['z_per_capita'].isna().any():
            nan_count = df['z_per_capita'].isna().sum()
            df['z_per_capita'] = df['z_per_capita'].fillna(0)
            logger.info(f"  Filled {nan_count} NaN values in z_per_capita with 0")

        self.log_decision(
            'population_normalization',
            'Created z_per_capita (z-score of per-capita interest)',
            'Enables population-controlled comparisons across states',
            'Per reviewer: this should eliminate Battleground Paradox artifact'
        )

        # Add population weight for national aggregates
        df['pop_weight'] = df['state'].map(POPULATION_WEIGHTS)

        self.stats['pop_normalized'] = True

        return df

    def calculate_national_baseline(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate national weighted average as baseline (R2 revision: NOT Ohio)."""
        logger.info("Calculating national weighted average baseline...")

        # Calculate population-weighted national average per date-term
        def weighted_avg(group):
            weights = group['state'].map(POPULATION_WEIGHTS)
            if weights.sum() > 0:
                return np.average(group['interest'], weights=weights)
            return group['interest'].mean()

        national_avg = df.groupby(['date', 'term']).apply(weighted_avg).reset_index()
        national_avg.columns = ['date', 'term', 'national_avg']

        # Merge back
        df = df.merge(national_avg, on=['date', 'term'], how='left')

        # Calculate deviation from national average
        df['interest_vs_national'] = df['interest'] - df['national_avg']

        self.log_decision(
            'national_baseline',
            'Calculated population-weighted national average as baseline',
            'R2 revision: Ohio is no longer swing state (Trump +11 in 2024), use national avg instead',
            'interest_vs_national shows state deviation from population-weighted national trend'
        )

        return df

    def calculate_issue_salience(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate issue salience index per state per week."""
        logger.info("Calculating issue salience indices...")

        # Filter to weighted categories only
        weighted_cats = list(ISSUE_WEIGHTS.keys())
        df_weighted = df[df['category'].isin(weighted_cats)].copy()

        # Group by state, date, category and calculate mean z-score
        salience = df_weighted.groupby(
            ['state', 'date', 'category']
        )['z_combined'].mean().reset_index()

        salience.columns = ['state', 'date', 'category', 'salience']

        # Pivot to wide format
        salience_wide = salience.pivot_table(
            index=['state', 'date'],
            columns='category',
            values='salience',
            fill_value=0
        ).reset_index()

        self.log_decision(
            'issue_salience',
            'Calculated issue salience per state-date-category',
            'Mean of combined z-scores for all terms in category',
            f'Categories: {weighted_cats}'
        )

        self.stats['salience_records'] = len(salience_wide)

        return salience_wide

    def calculate_vibe_index(self, salience_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate weighted Vibe Index per state per date."""
        logger.info("Calculating Vibe Index...")

        vibe_df = salience_df.copy()

        # Calculate weighted sum
        vibe_df['vibe_index'] = 0
        for category, weight in ISSUE_WEIGHTS.items():
            if category in vibe_df.columns:
                vibe_df['vibe_index'] += vibe_df[category] * weight

        self.log_decision(
            'vibe_index',
            'Calculated weighted Vibe Index',
            f'Weights: {ISSUE_WEIGHTS}',
            'Single composite metric per state-date'
        )

        # Add rolling average (7-day)
        vibe_df = vibe_df.sort_values(['state', 'date'])
        vibe_df['vibe_index_7d'] = vibe_df.groupby('state')['vibe_index'].transform(
            lambda x: x.rolling(7, min_periods=1).mean()
        )

        self.log_decision(
            'vibe_index',
            'Added 7-day rolling average',
            'Smooths daily fluctuations for trend analysis',
            'Useful for correlation with weekly polling data'
        )

        self.stats['vibe_states'] = vibe_df['state'].nunique()
        self.stats['vibe_dates'] = vibe_df['date'].nunique()

        return vibe_df

    def generate_processing_log(self, output_path: Path):
        """Generate markdown processing log."""
        log_content = f"""# Data Processing Log — VibePoll-2026

**Framework:** CommDAAF v1.0
**Generated:** {datetime.now().isoformat()}

---

## Processing Statistics

| Metric | Value |
|--------|-------|
| Raw records | {self.stats.get('raw_records', 'N/A')} |
| States | {self.stats.get('raw_states', 'N/A')} |
| Terms | {self.stats.get('raw_terms', 'N/A')} |
| Categories | {self.stats.get('raw_categories', 'N/A')} |
| Date range | {self.stats.get('date_range', 'N/A')} |
| Missing values handled | {self.stats.get('missing_handled', 0)} |
| Salience records | {self.stats.get('salience_records', 'N/A')} |

---

## Methodological Decisions

Per CommDAAF transparency requirement, all processing decisions are documented below:

"""
        for entry in self.processing_log:
            log_content += f"""### {entry['step'].replace('_', ' ').title()}

**Decision:** {entry['decision']}

**Rationale:** {entry['rationale']}

**Impact:** {entry['impact'] or 'N/A'}

---

"""

        log_content += f"""
## Output Files

1. `trends_normalized.parquet` - Full normalized dataset with z-scores
2. `issue_salience.csv` - Issue salience per state-date-category
3. `vibe_indices.csv` - Weighted Vibe Index per state-date

---

## Issue Weights (from PLAN.md)

| Category | Weight | Rationale |
|----------|--------|-----------|
| economy | 0.35 | Top voter concern (cost of living 52%) |
| immigration | 0.20 | Highly polarizing, active enforcement |
| political | 0.15 | Electoral engagement indicators |
| iran_war | 0.15 | Active conflict, approval impact |
| ai_jobs | 0.10 | Growing but not yet top concern |
| epstein | 0.05 | Episodic, scandal interest |

---

*Log generated following CommDAAF v1.0 transparency protocol*
"""

        with open(output_path, 'w') as f:
            f.write(log_content)

        logger.info(f"Processing log saved: {output_path}")

    def process_all(self, input_file: Path) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Run full processing pipeline."""
        logger.info("=" * 60)
        logger.info("Starting Data Processing Pipeline")
        logger.info("CommDAAF v1.0 - EXPLORATORY Tier")
        logger.info("=" * 60)

        # Load data
        df = self.load_data(input_file)

        # Filter low-signal terms (per reviewer critique)
        df = self.filter_low_signal_terms(df, max_zero_pct=0.50)

        # Handle missing values
        df = self.handle_missing_values(df)

        # Normalize
        df = self.normalize_zscore(df)

        # Per-capita normalization (addresses reviewer critique)
        df = self.normalize_population(df)

        # National weighted average baseline (R2 revision: NOT Ohio)
        df = self.calculate_national_baseline(df)

        # Calculate salience
        salience_df = self.calculate_issue_salience(df)

        # Calculate Vibe Index
        vibe_df = self.calculate_vibe_index(salience_df)

        logger.info("=" * 60)
        logger.info("PROCESSING COMPLETE")
        logger.info("=" * 60)

        return df, salience_df, vibe_df


def main():
    """Main processing function."""
    # Find latest trends file
    trends_files = list(RAW_DIR.glob("trends_*.parquet"))
    if not trends_files:
        logger.error("No trends data found!")
        return

    latest_file = max(trends_files, key=lambda p: p.stat().st_mtime)
    logger.info(f"Processing: {latest_file}")

    # Process
    processor = DataProcessor()
    df_normalized, df_salience, df_vibe = processor.process_all(latest_file)

    # Save outputs
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Normalized trends
    output_trends = PROCESSED_DIR / "trends_normalized.parquet"
    df_normalized.to_parquet(output_trends, index=False)
    logger.info(f"Saved: {output_trends} ({len(df_normalized)} records)")

    # Issue salience
    output_salience = PROCESSED_DIR / "issue_salience.csv"
    df_salience.to_csv(output_salience, index=False)
    logger.info(f"Saved: {output_salience} ({len(df_salience)} records)")

    # Vibe indices
    output_vibe = PROCESSED_DIR / "vibe_indices.csv"
    df_vibe.to_csv(output_vibe, index=False)
    logger.info(f"Saved: {output_vibe} ({len(df_vibe)} records)")

    # Processing log
    output_log = PROCESSED_DIR / "processing_log.md"
    processor.generate_processing_log(output_log)

    # Print summary
    print("\n" + "=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Normalized trends: {len(df_normalized)} records")
    print(f"Issue salience: {len(df_salience)} state-date-category combinations")
    print(f"Vibe indices: {len(df_vibe)} state-date pairs")
    print(f"\nZ-score statistics:")
    print(f"  Temporal z-score mean: {df_normalized['z_temporal'].mean():.4f}")
    print(f"  Temporal z-score std: {df_normalized['z_temporal'].std():.4f}")
    print(f"\nVibe Index statistics:")
    print(f"  Mean: {df_vibe['vibe_index'].mean():.4f}")
    print(f"  Std: {df_vibe['vibe_index'].std():.4f}")
    print(f"  Min: {df_vibe['vibe_index'].min():.4f}")
    print(f"  Max: {df_vibe['vibe_index'].max():.4f}")

    return df_normalized, df_salience, df_vibe


if __name__ == "__main__":
    main()
