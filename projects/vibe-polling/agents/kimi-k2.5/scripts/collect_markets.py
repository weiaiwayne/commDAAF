#!/usr/bin/env python3
"""
Prediction Market Data Collection for VibePoll-2026
Agent: Kimi K2.5 (Independent Analysis)
Framework: CommDAAF v1.0

Collects odds data from Polymarket and Kalshi for validation against Google Trends.
"""

import requests
import pandas as pd
import json
from datetime import datetime
import os

# Configuration
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/markets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Polymarket API endpoints
POLYMARKET_BASE = "https://gamma-api.polymarket.com"

# Key markets to track for 2026 midterms
POLYMARKET_MARKETS = [
    {
        'slug': 'balance-of-power-2026-midterms',
        'name': 'Balance of Power 2026',
        'category': 'congress'
    },
    {
        'slug': 'will-democrats-win-the-house-in-2026',
        'name': 'Democrats Win House 2026',
        'category': 'house'
    },
    {
        'slug': 'will-republicans-win-the-senate-in-2026',
        'name': 'Republicans Win Senate 2026',
        'category': 'senate'
    }
]


def collect_polymarket():
    """
    Collect current odds from Polymarket API.
    Returns list of market data dictionaries.
    """
    results = []
    
    print("Collecting Polymarket data...")
    
    for market in POLYMARKET_MARKETS:
        try:
            url = f"{POLYMARKET_BASE}/markets/{market['slug']}"
            
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract key fields
                market_data = {
                    'platform': 'polymarket',
                    'market_slug': market['slug'],
                    'market_name': market['name'],
                    'category': market['category'],
                    'timestamp': datetime.now().isoformat(),
                    'question': data.get('question'),
                    'description': data.get('description'),
                    'volume': data.get('volume'),
                    'liquidity': data.get('liquidity'),
                    'volume_24h': data.get('volume24hr'),
                    'status': data.get('active'),
                    'outcomes': []
                }
                
                # Extract outcome prices
                outcomes = data.get('outcomes', [])
                for outcome in outcomes:
                    market_data['outcomes'].append({
                        'name': outcome.get('name'),
                        'price': outcome.get('price'),  # 0-1 scale
                        'probability': outcome.get('probability'),
                        'volume': outcome.get('volume')
                    })
                
                results.append(market_data)
                print(f"  ✓ {market['name']}: {len(outcomes)} outcomes")
                
            else:
                print(f"  ✗ {market['name']}: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"  ✗ Error collecting {market['name']}: {e}")
    
    return results


def collect_kalshi():
    """
    Collect data from Kalshi API.
    Note: Kalshi may require authentication for some endpoints.
    """
    results = []
    
    print("\nCollecting Kalshi data...")
    
    try:
        # Kalshi public API endpoint
        url = "https://trading-api.kalshi.com/v2/markets"
        
        # Search for 2026 election markets
        params = {
            'limit': 100,
            'status': 'open',
            'event_ticker': 'KXCONGRESS'  # Congress-related markets
        }
        
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            markets = data.get('markets', [])
            
            for market in markets:
                # Filter for 2026 election markets
                ticker = market.get('ticker', '')
                if '2026' in ticker or 'CONGRESS' in ticker:
                    market_data = {
                        'platform': 'kalshi',
                        'ticker': ticker,
                        'title': market.get('title'),
                        'description': market.get('description'),
                        'timestamp': datetime.now().isoformat(),
                        'yes_ask': market.get('yes_ask'),  # Price to buy YES
                        'yes_bid': market.get('yes_bid'),  # Price to sell YES
                        'volume': market.get('volume'),
                        'open_interest': market.get('open_interest'),
                        'close_time': market.get('close_time')
                    }
                    results.append(market_data)
            
            print(f"  ✓ Collected {len(results)} markets")
        else:
            print(f"  ✗ Kalshi API: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"  ✗ Error collecting Kalshi data: {e}")
    
    return results


def collect_all_markets():
    """
    Main collection function - aggregates all prediction market data.
    """
    print("=" * 70)
    print("VibePoll-2026: Prediction Market Data Collection")
    print(f"Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print("=" * 70)
    print()
    
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    # Collect from all sources
    polymarket_data = collect_polymarket()
    kalshi_data = collect_kalshi()
    
    # Combine
    all_data = {
        'collection_timestamp': timestamp,
        'agent': 'kimi-k2.5',
        'framework': 'commdaaf-v1.0',
        'sources': {
            'polymarket': polymarket_data,
            'kalshi': kalshi_data
        },
        'summary': {
            'total_markets': len(polymarket_data) + len(kalshi_data),
            'polymarket_count': len(polymarket_data),
            'kalshi_count': len(kalshi_data)
        }
    }
    
    # Save
    output_file = f"{OUTPUT_DIR}/markets_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(all_data, f, indent=2)
    
    print(f"\n{'=' * 70}")
    print("Collection complete!")
    print(f"{'=' * 70}")
    print(f"✓ Saved: {output_file}")
    print(f"  Total markets: {all_data['summary']['total_markets']}")
    print(f"  Polymarket: {all_data['summary']['polymarket_count']}")
    print(f"  Kalshi: {all_data['summary']['kalshi_count']}")
    
    return all_data


if __name__ == "__main__":
    data = collect_all_markets()
