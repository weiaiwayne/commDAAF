
import requests
import pandas as pd
from datetime import datetime
import json
import os

# Polymarket API (gamma-api)
POLYMARKET_BASE = "https://gamma-api.polymarket.com"

# Key markets to track (using event slugs from research)
POLYMARKET_SLUGS = [
    "which-party-will-win-the-house-in-2026",
    "which-party-will-win-the-senate-in-2026",
    "2026-midterms-house-popular-vote-margin-of-victory",
    "republican-house-seats-after-the-2026-midterm-elections",
    "republican-senate-seats-after-the-2026-midterm-elections",
    "blue-wave-in-2026",
]

def collect_polymarket():
    """Collect current odds from Polymarket."""
    results = []
    
    for slug in POLYMARKET_SLUGS:
        try:
            # Using /events endpoint as per research
            url = f"{POLYMARKET_BASE}/events?slug={slug}"
            resp = requests.get(url, timeout=30)
            
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, list) and len(data) > 0:
                    event = data[0]
                    # Each event contains one or more markets
                    markets = event.get('markets', [])
                    for market in markets:
                        results.append({
                            'event_slug': slug,
                            'market_slug': market.get('slug'),
                            'question': market.get('question'),
                            'timestamp': datetime.now().isoformat(),
                            'outcomes': market.get('outcomes', []),
                            'outcomePrices': market.get('outcomePrices', []),
                            'volume': market.get('volume'),
                            'liquidity': market.get('liquidity')
                        })
                else:
                    print(f"No event found for slug {slug}")
        except Exception as e:
            print(f"Error fetching {slug}: {e}")
    
    return results


# Kalshi API (trade-api/v2)
KALSHI_BASE = "https://api.elections.kalshi.com/trade-api/v2"

# Kalshi event tickers from research
KALSHI_TICKERS = ["CONTROLH-26", "CONTROLS-26", "BOP-26", "HPOP-26"]

def collect_kalshi():
    """Collect current odds from Kalshi."""
    results = []
    
    for ticker in KALSHI_TICKERS:
        try:
            # Use /events endpoint with nested markets for full outcome data
            url = f"{KALSHI_BASE}/events/{ticker}?with_nested_markets=true"
            resp = requests.get(url, timeout=30)
            
            if resp.status_code == 200:
                data = resp.json()
                event = data.get('event', {})
                markets = event.get('markets', [])
                
                for market in markets:
                    results.append({
                        'event_ticker': ticker,
                        'market_ticker': market.get('ticker'),
                        'title': market.get('title'),
                        'timestamp': datetime.now().isoformat(),
                        'yes_price': market.get('yes_price'),
                        'no_price': market.get('no_price'),
                        'volume': market.get('volume'),
                        'liquidity': market.get('liquidity')
                    })
            else:
                print(f"Kalshi API error for {ticker} ({resp.status_code}): {resp.text}")
        except Exception as e:
            print(f"Kalshi error for {ticker}: {e}")
    
    return results

def collect_historical_polymarket(token_id, slug):
    """Fetch all available historical price data for a token."""
    # startTs for 2025-01-01
    url = f"https://clob.polymarket.com/prices-history?market={token_id}&interval=all&startTs=1735689600"
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            history = resp.json().get('history', [])
            df = pd.DataFrame(history)
            if not df.empty:
                df['date'] = pd.to_datetime(df['t'], unit='s').dt.date
                df['market_slug'] = slug
                return df
    except Exception as e:
        print(f"Error fetching historical for {slug}: {e}")
    return pd.DataFrame()

def save_market_snapshot():
    """Save daily market snapshot and historical data."""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_dir = "agents/gemini/data/raw/markets"
    os.makedirs(output_dir, exist_ok=True)
    
    snapshot = {
        'timestamp': timestamp,
        'polymarket': collect_polymarket(),
        'kalshi': collect_kalshi()
    }
    
    with open(f"{output_dir}/markets_{timestamp}.json", 'w') as f:
        json.dump(snapshot, f, indent=2)
    
    # Also fetch and save historical data for key tokens
    # House Dem Yes: 83247781037352156539108067944461291821683755894607244160607042790356561625563
    # Senate Dem Yes: 113287701564209339913693347405685749986285999146352375265161592243948562084773
    
    historical_house = collect_historical_polymarket("83247781037352156539108067944461291821683755894607244160607042790356561625563", "house_dem_odds")
    historical_senate = collect_historical_polymarket("113287701564209339913693347405685749986285999146352375265161592243948562084773", "senate_dem_odds")
    
    if not historical_house.empty or not historical_senate.empty:
        combined_hist = pd.concat([historical_house, historical_senate])
        # Aggregate to daily first (taking the last price of the day)
        daily_hist = combined_hist.sort_values('t').groupby(['date', 'market_slug']).last().reset_index()
        # Pivot to have house_dem_odds and senate_dem_odds as columns
        pivoted = daily_hist.pivot(index='date', columns='market_slug', values='p').reset_index()
        pivoted.to_csv(f"{output_dir}/historical_market_odds.csv", index=False)
        print(f"Saved historical market odds to {output_dir}")
    
    print(f"Saved snapshot to {output_dir}/markets_{timestamp}.json")
    return snapshot


if __name__ == "__main__":
    save_market_snapshot()
