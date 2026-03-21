#!/usr/bin/env python3
"""
Google Trends Data Collection for VibePoll-2026

CommDAAF v1.0 - EXPLORATORY Tier
Collects search interest data for all validated terms across battleground states.

Rate Limiting Strategy:
- 3-6 second delays between requests
- Max 5 terms per API call (Google limit)
- Exponential backoff on 429 errors
- State-by-state collection to manage load

Output: data/raw/trends/trends_YYYY-MM-DD.parquet
"""

import json
import time
import random
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import warnings
warnings.filterwarnings('ignore')

from pytrends.request import TrendReq
import pandas as pd

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "trends"
LOG_DIR = PROJECT_ROOT / "logs"

# Rate limiting - CONSERVATIVE settings to prevent IP blocking
MIN_DELAY = 8      # Increased from 3
MAX_DELAY = 15     # Increased from 6
BACKOFF_MULTIPLIER = 3  # Increased from 2
MAX_RETRIES = 5    # Increased from 3
BATCH_SIZE = 5     # Google Trends API limit

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "collection_log.txt"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class TrendsCollector:
    """Collects Google Trends data for VibePoll study."""

    def __init__(self, timeframe: str = 'today 3-m'):
        """
        Initialize collector.

        Args:
            timeframe: Google Trends timeframe
                - 'today 3-m': Past 3 months
                - 'today 12-m': Past 12 months
                - '2025-01-01 2026-03-19': Custom range
        """
        self.pytrends = TrendReq(hl='en-US', tz=300)
        self.timeframe = timeframe
        self.collected_data: List[pd.DataFrame] = []
        self.errors: List[Dict] = []
        self.stats = {
            'states_completed': 0,
            'terms_collected': 0,
            'errors': 0,
            'rate_limits_hit': 0
        }

    def _delay(self, attempt: int = 0):
        """Rate limiting with exponential backoff."""
        base_delay = random.uniform(MIN_DELAY, MAX_DELAY)
        delay = base_delay * (BACKOFF_MULTIPLIER ** attempt)
        time.sleep(delay)

    def _batch_terms(self, terms: List[str]) -> List[List[str]]:
        """Split terms into batches of BATCH_SIZE."""
        return [terms[i:i+BATCH_SIZE] for i in range(0, len(terms), BATCH_SIZE)]

    def collect_batch(self, terms: List[str], geo: str,
                      category: str) -> Optional[pd.DataFrame]:
        """
        Collect trends for a batch of terms (max 5).

        Args:
            terms: List of search terms (max 5)
            geo: Geographic code (e.g., 'US-PA')
            category: Category name for labeling

        Returns:
            DataFrame with trends data or None on failure
        """
        for attempt in range(MAX_RETRIES):
            try:
                self.pytrends.build_payload(
                    terms,
                    geo=geo,
                    timeframe=self.timeframe
                )

                interest = self.pytrends.interest_over_time()

                if interest.empty:
                    logger.warning(f"No data for {terms} in {geo}")
                    return None

                # Drop isPartial column if present
                if 'isPartial' in interest.columns:
                    interest = interest.drop('isPartial', axis=1)

                # Melt to long format
                interest = interest.reset_index()
                melted = interest.melt(
                    id_vars=['date'],
                    var_name='term',
                    value_name='interest'
                )

                # Add metadata
                melted['geo'] = geo
                melted['state'] = geo.replace('US-', '')
                melted['category'] = category
                melted['collected_at'] = datetime.now().isoformat()

                return melted

            except Exception as e:
                error_str = str(e)
                if '429' in error_str or 'Too Many Requests' in error_str:
                    self.stats['rate_limits_hit'] += 1
                    logger.warning(f"Rate limited, backing off (attempt {attempt+1})")
                    self._delay(attempt + 1)
                else:
                    logger.error(f"Error collecting {terms} for {geo}: {error_str}")
                    self.errors.append({
                        'terms': terms,
                        'geo': geo,
                        'error': error_str,
                        'timestamp': datetime.now().isoformat()
                    })
                    return None

        logger.error(f"Failed after {MAX_RETRIES} retries: {terms} in {geo}")
        self.stats['errors'] += 1
        return None

    def collect_state(self, state_code: str, state_info: Dict,
                      term_categories: Dict) -> List[pd.DataFrame]:
        """
        Collect all terms for a single state.

        Args:
            state_code: State abbreviation (e.g., 'PA')
            state_info: State metadata from state_codes.json
            term_categories: All term categories

        Returns:
            List of DataFrames with collected data
        """
        geo = state_info['code']
        state_data = []

        logger.info(f"Collecting data for {state_info.get('name', state_code)} ({geo})")

        for category, cat_data in term_categories.items():
            # Skip non-term categories
            if category == 'partisan_pairs':
                # Extract terms from pairs
                pairs = cat_data.get('pairs', [])
                terms = []
                for pair in pairs:
                    terms.extend([pair['left'], pair['right']])
                terms = list(set(terms))  # Deduplicate
            elif category == 'state_specific':
                # Only collect state-specific terms for this state
                terms = cat_data.get(state_code, [])
                if not terms:
                    continue
            else:
                terms = cat_data.get('terms', [])

            if not terms:
                continue

            # Process in batches
            batches = self._batch_terms(terms)

            for i, batch in enumerate(batches):
                logger.info(f"  {category} batch {i+1}/{len(batches)}: {batch}")

                df = self.collect_batch(batch, geo, category)

                if df is not None:
                    state_data.append(df)
                    self.stats['terms_collected'] += len(batch)

                self._delay()

        self.stats['states_completed'] += 1
        return state_data

    def collect_all(self, state_codes: Dict, term_categories: Dict,
                    state_filter: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Collect trends for all states.

        Args:
            state_codes: State definitions from state_codes.json
            term_categories: Term definitions from term_categories.json
            state_filter: Optional list of state codes to collect (for testing)

        Returns:
            Combined DataFrame with all collected data
        """
        start_time = datetime.now()
        logger.info("=" * 60)
        logger.info("Starting Google Trends Collection")
        logger.info(f"Timeframe: {self.timeframe}")
        logger.info("=" * 60)

        all_data = []

        # Collect all state types
        for state_type in ['battleground', 'control', 'watch']:
            states = state_codes.get(state_type, {})

            for state_code, state_info in states.items():
                if state_filter and state_code not in state_filter:
                    continue

                state_dfs = self.collect_state(state_code, state_info, term_categories)
                all_data.extend(state_dfs)

                # Longer delay between states - CONSERVATIVE
                time.sleep(random.uniform(15, 25))

        # Combine all data
        if all_data:
            combined = pd.concat(all_data, ignore_index=True)

            # Add collection metadata
            combined['collection_run'] = start_time.isoformat()
            combined['timeframe'] = self.timeframe

            elapsed = (datetime.now() - start_time).total_seconds() / 60

            logger.info("=" * 60)
            logger.info("COLLECTION COMPLETE")
            logger.info(f"Time elapsed: {elapsed:.1f} minutes")
            logger.info(f"States completed: {self.stats['states_completed']}")
            logger.info(f"Terms collected: {self.stats['terms_collected']}")
            logger.info(f"Rate limits hit: {self.stats['rate_limits_hit']}")
            logger.info(f"Errors: {self.stats['errors']}")
            logger.info("=" * 60)

            return combined

        logger.warning("No data collected!")
        return pd.DataFrame()

    def save(self, df: pd.DataFrame, output_dir: Path) -> Path:
        """Save collected data to parquet file."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        output_file = output_dir / f"trends_{timestamp}.parquet"

        df.to_parquet(output_file, index=False)
        logger.info(f"Saved: {output_file}")
        logger.info(f"Records: {len(df)}")

        # Also save errors if any
        if self.errors:
            error_file = output_dir / f"trends_{timestamp}_errors.json"
            with open(error_file, 'w') as f:
                json.dump(self.errors, f, indent=2)
            logger.info(f"Errors saved: {error_file}")

        return output_file


def main(test_mode: bool = False):
    """
    Main collection function.

    Args:
        test_mode: If True, only collect 2 states for testing
    """
    # Load reference data
    with open(REFERENCE_DIR / "state_codes.json") as f:
        state_codes = json.load(f)

    with open(REFERENCE_DIR / "term_categories.json") as f:
        term_categories = json.load(f)

    # Count expected collections
    total_states = sum(len(state_codes[t]) for t in ['battleground', 'control', 'watch'])
    total_terms = sum(
        len(cat.get('terms', []))
        for cat in term_categories.values()
        if isinstance(cat, dict) and 'terms' in cat
    )

    logger.info(f"States to collect: {total_states}")
    logger.info(f"Base terms per state: ~{total_terms}")

    # Initialize collector
    # Use longer timeframe for more data points
    collector = TrendsCollector(timeframe='today 3-m')

    # Test mode: only collect PA and CA
    state_filter = ['PA', 'CA'] if test_mode else None

    if test_mode:
        logger.info("*** TEST MODE: Only collecting PA and CA ***")

    # Collect data
    df = collector.collect_all(state_codes, term_categories, state_filter)

    if not df.empty:
        # Save to parquet
        output_file = collector.save(df, OUTPUT_DIR)

        # Print summary stats
        print("\n" + "=" * 60)
        print("DATA SUMMARY")
        print("=" * 60)
        print(f"Total records: {len(df)}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        print(f"States: {df['state'].nunique()}")
        print(f"Terms: {df['term'].nunique()}")
        print(f"Categories: {df['category'].nunique()}")
        print(f"\nOutput: {output_file}")

        return df

    return None


if __name__ == "__main__":
    import sys
    test_mode = '--test' in sys.argv
    main(test_mode=test_mode)
