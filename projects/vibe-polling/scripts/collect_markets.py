#!/usr/bin/env python3
"""
Prediction Market Data Collection for VibePoll-2026

CommDAAF v1.0 - EXPLORATORY Tier
Collects odds from Polymarket and Kalshi for 2026 midterm elections.

Data Sources:
- Polymarket: gamma-api.polymarket.com (free, no auth)
- Kalshi: trading-api.kalshi.com (public endpoints)

Output: data/raw/markets/markets_YYYY-MM-DD.json
"""

import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import requests

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "markets"
LOG_DIR = PROJECT_ROOT / "logs"

# API endpoints
POLYMARKET_BASE = "https://gamma-api.polymarket.com"
KALSHI_BASE = "https://api.elections.kalshi.com/v1"

# Request settings
TIMEOUT = 30
RETRY_DELAY = 5
MAX_RETRIES = 3

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "collection_log.txt", mode='a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Key Polymarket markets for 2026 midterms
POLYMARKET_MARKETS = [
    # Balance of Power
    "balance-of-power-2026-midterms",
    "will-democrats-win-the-house-in-2026",
    "will-republicans-win-the-senate-in-2026",
    "will-democrats-win-both-the-house-and-senate-in-2026",
    # Presidential approval/outlook
    "trump-approval-rating-march-2026",
    "will-trump-be-impeached-in-his-second-term",
    # Key Senate races
    "georgia-senate-2026",
    "michigan-senate-2026",
    "maine-senate-2026",
    "north-carolina-senate-2026",
]

# Kalshi market tickers for 2026
KALSHI_TICKERS = [
    "CONGRESS-26",
    "HOUSE-26",
    "SENATE-26",
]


class MarketCollector:
    """Collects prediction market data."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'VibePoll-2026/1.0 (Academic Research)',
            'Accept': 'application/json'
        })
        self.stats = {
            'polymarket_collected': 0,
            'kalshi_collected': 0,
            'errors': 0
        }

    def _request(self, url: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """Make HTTP request with retries."""
        for attempt in range(MAX_RETRIES):
            try:
                resp = self.session.get(url, params=params, timeout=TIMEOUT)

                if resp.status_code == 200:
                    return resp.json()
                elif resp.status_code == 404:
                    logger.warning(f"Not found: {url}")
                    return None
                elif resp.status_code == 429:
                    logger.warning(f"Rate limited, waiting...")
                    time.sleep(RETRY_DELAY * (attempt + 1))
                else:
                    logger.warning(f"HTTP {resp.status_code}: {url}")

            except requests.exceptions.Timeout:
                logger.warning(f"Timeout on {url}, retrying...")
                time.sleep(RETRY_DELAY)
            except requests.exceptions.RequestException as e:
                logger.error(f"Request error: {e}")
                time.sleep(RETRY_DELAY)

        self.stats['errors'] += 1
        return None

    def collect_polymarket(self) -> List[Dict]:
        """
        Collect data from Polymarket.

        Uses the gamma-api which provides market data without authentication.
        """
        logger.info("Collecting Polymarket data...")
        results = []

        # First, try to get markets list
        markets_url = f"{POLYMARKET_BASE}/markets"
        all_markets = self._request(markets_url, params={'limit': 100, 'active': True})

        if all_markets:
            # Filter for election-related markets
            election_markets = [
                m for m in all_markets
                if any(kw in m.get('question', '').lower()
                       for kw in ['2026', 'midterm', 'house', 'senate', 'congress', 'election'])
            ]

            for market in election_markets:
                market_data = {
                    'source': 'polymarket',
                    'market_id': market.get('id'),
                    'slug': market.get('slug'),
                    'question': market.get('question'),
                    'outcomes': market.get('outcomes', []),
                    'outcomePrices': market.get('outcomePrices', []),
                    'volume': market.get('volume'),
                    'liquidity': market.get('liquidity'),
                    'startDate': market.get('startDate'),
                    'endDate': market.get('endDate'),
                    'collected_at': datetime.now().isoformat()
                }
                results.append(market_data)
                self.stats['polymarket_collected'] += 1

            logger.info(f"  Found {len(results)} election markets")

        # Also try specific slugs
        for slug in POLYMARKET_MARKETS:
            url = f"{POLYMARKET_BASE}/markets/{slug}"
            data = self._request(url)

            if data:
                # Check if we already have this market
                existing_ids = {r.get('market_id') for r in results}
                if data.get('id') not in existing_ids:
                    market_data = {
                        'source': 'polymarket',
                        'market_id': data.get('id'),
                        'slug': slug,
                        'question': data.get('question'),
                        'outcomes': data.get('outcomes', []),
                        'outcomePrices': data.get('outcomePrices', []),
                        'volume': data.get('volume'),
                        'liquidity': data.get('liquidity'),
                        'collected_at': datetime.now().isoformat()
                    }
                    results.append(market_data)
                    self.stats['polymarket_collected'] += 1
                    logger.info(f"  Collected: {slug}")

            time.sleep(1)  # Rate limiting

        return results

    def collect_kalshi(self) -> List[Dict]:
        """
        Collect data from Kalshi.

        Kalshi has a public API for viewing market data.
        """
        logger.info("Collecting Kalshi data...")
        results = []

        # Try events endpoint
        events_url = f"{KALSHI_BASE}/events"
        params = {
            'limit': 100,
            'status': 'open',
            'with_nested_markets': True
        }

        events = self._request(events_url, params)

        if events and 'events' in events:
            for event in events['events']:
                event_title = event.get('title', '').lower()

                # Filter for election events
                if any(kw in event_title for kw in ['2026', 'congress', 'house', 'senate', 'election', 'midterm']):
                    for market in event.get('markets', []):
                        market_data = {
                            'source': 'kalshi',
                            'event_ticker': event.get('event_ticker'),
                            'event_title': event.get('title'),
                            'market_ticker': market.get('ticker'),
                            'market_title': market.get('title'),
                            'yes_bid': market.get('yes_bid'),
                            'yes_ask': market.get('yes_ask'),
                            'no_bid': market.get('no_bid'),
                            'no_ask': market.get('no_ask'),
                            'last_price': market.get('last_price'),
                            'volume': market.get('volume'),
                            'open_interest': market.get('open_interest'),
                            'close_time': market.get('close_time'),
                            'collected_at': datetime.now().isoformat()
                        }
                        results.append(market_data)
                        self.stats['kalshi_collected'] += 1

            logger.info(f"  Found {len(results)} election markets")

        # Also try specific tickers
        for ticker in KALSHI_TICKERS:
            url = f"{KALSHI_BASE}/events/{ticker}"
            data = self._request(url)

            if data and 'event' in data:
                event = data['event']
                for market in event.get('markets', []):
                    # Check for duplicates
                    existing_tickers = {r.get('market_ticker') for r in results}
                    if market.get('ticker') not in existing_tickers:
                        market_data = {
                            'source': 'kalshi',
                            'event_ticker': ticker,
                            'event_title': event.get('title'),
                            'market_ticker': market.get('ticker'),
                            'market_title': market.get('title'),
                            'yes_bid': market.get('yes_bid'),
                            'yes_ask': market.get('yes_ask'),
                            'last_price': market.get('last_price'),
                            'volume': market.get('volume'),
                            'collected_at': datetime.now().isoformat()
                        }
                        results.append(market_data)
                        self.stats['kalshi_collected'] += 1
                        logger.info(f"  Collected: {ticker}")

            time.sleep(1)

        return results

    def collect_all(self) -> Dict:
        """Collect from all sources."""
        logger.info("=" * 60)
        logger.info("Starting Prediction Market Collection")
        logger.info("=" * 60)

        timestamp = datetime.now().isoformat()

        data = {
            'metadata': {
                'timestamp': timestamp,
                'study': 'VibePoll-2026',
                'framework': 'CommDAAF v1.0'
            },
            'polymarket': self.collect_polymarket(),
            'kalshi': self.collect_kalshi(),
            'stats': self.stats
        }

        logger.info("=" * 60)
        logger.info("COLLECTION COMPLETE")
        logger.info(f"Polymarket markets: {self.stats['polymarket_collected']}")
        logger.info(f"Kalshi markets: {self.stats['kalshi_collected']}")
        logger.info(f"Errors: {self.stats['errors']}")
        logger.info("=" * 60)

        return data

    def save(self, data: Dict, output_dir: Path) -> Path:
        """Save collected data to JSON."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        output_file = output_dir / f"markets_{timestamp}.json"

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)

        logger.info(f"Saved: {output_file}")
        return output_file


def main():
    """Main collection function."""
    collector = MarketCollector()
    data = collector.collect_all()

    if data['polymarket'] or data['kalshi']:
        output_file = collector.save(data, OUTPUT_DIR)

        print("\n" + "=" * 60)
        print("MARKET DATA SUMMARY")
        print("=" * 60)
        print(f"Polymarket markets: {len(data['polymarket'])}")
        print(f"Kalshi markets: {len(data['kalshi'])}")

        # Show key markets
        if data['polymarket']:
            print("\nKey Polymarket Odds:")
            for m in data['polymarket'][:5]:
                q = m.get('question', m.get('slug', 'Unknown'))[:50]
                prices = m.get('outcomePrices', [])
                print(f"  - {q}: {prices}")

        print(f"\nOutput: {output_file}")

        return data

    logger.warning("No market data collected!")
    return None


if __name__ == "__main__":
    main()
