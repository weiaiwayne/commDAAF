#!/usr/bin/env python3
"""
Polling Data Collection for VibePoll-2026
Agent: Kimi K2.5 (Independent Analysis)  
Framework: CommDAAF v1.0

Collects polling data from RealClearPolitics and 270toWin for validation.
Uses web scraping with BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
import os
import re

# Configuration
OUTPUT_DIR = "agents/kimi-k2.5/data/raw/polls"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def scrape_rcp_generic_ballot():
    """
    Scrape RealClearPolitics generic congressional ballot average.
    """
    print("Scraping RealClearPolitics...")
    
    try:
        url = "https://www.realclearpolitics.com/epolls/other/2026_generic_congressional_vote-7785.html"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find RCP average row
            tables = soup.find_all('table')
            
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    if 'RCP Average' in row.get_text():
                        cells = row.find_all('td')
                        if len(cells) >= 4:
                            return {
                                'source': 'rcp',
                                'metric': 'generic_ballot',
                                'democrat': cells[1].get_text(strip=True),
                                'republican': cells[2].get_text(strip=True),
                                'dem_lead': cells[3].get_text(strip=True),
                                'scraped_at': datetime.now().isoformat(),
                                'url': url
                            }
            
            print("  ⚠️  RCP Average row not found")
            return None
            
        else:
            print(f"  ✗ RCP: HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"  ✗ Error scraping RCP: {e}")
        return None


def scrape_270towin_senate():
    """
    Scrape 270toWin Senate predictions for 2026.
    """
    print("Scraping 270toWin...")
    
    try:
        url = "https://www.270towin.com/2026-senate-election/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract state ratings
            # Look for map data or state list
            state_ratings = []
            
            # Find all state cells
            state_elements = soup.find_all(['div', 'td'], class_=re.compile('state|senate'))
            
            for elem in state_elements:
                text = elem.get_text(strip=True)
                # Look for state abbreviations or names
                if len(text) <= 20:  # Likely a state name or rating
                    state_ratings.append(text)
            
            return {
                'source': '270towin',
                'metric': 'senate_map',
                'states_found': len(state_ratings),
                'sample_data': state_ratings[:10],  # First 10 for reference
                'scraped_at': datetime.now().isoformat(),
                'url': url
            }
            
        else:
            print(f"  ✗ 270toWin: HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"  ✗ Error scraping 270toWin: {e}")
        return None


def collect_manual_polls():
    """
    Manually collected polling data from recent sources.
    This serves as backup when scraping fails.
    """
    print("Loading manual polling data...")
    
    # Recent polling data (March 2026 context from PLAN.md)
    manual_data = {
        'polymarket_house_odds': {
            'source': 'polymarket',
            'date': '2026-03-19',
            'metric': 'dem_house_win_probability',
            'value': 0.76,  # ~76% from PLAN.md
            'note': 'From PLAN.md Section 3.2'
        },
        'polymarket_sweep_odds': {
            'source': 'polymarket', 
            'date': '2026-03-19',
            'metric': 'dem_sweep_probability',
            'value': 0.50,
            'note': 'From PLAN.md Section 3.2'
        },
        'top_issue_polling': {
            'source': 'politico',
            'date': '2026-03',
            'metric': 'top_voter_issue',
            'value': 'cost_of_living',
            'percentage': 52,
            'note': 'From PLAN.md Section 3.1'
        },
        'iran_war_support': {
            'source': 'reuters_ipsos',
            'date': '2026-03',
            'metric': 'support_us_strikes_iran',
            'value': 0.25,
            'note': 'From PLAN.md Section 3.1 - 25% support'
        },
        'iran_ground_troops_opposition': {
            'source': 'quinnipiac',
            'date': '2026-03',
            'metric': 'oppose_ground_troops_iran',
            'value': 0.74,
            'note': 'From PLAN.md Section 3.1 - 74% oppose'
        }
    }
    
    print(f"  ✓ Loaded {len(manual_data)} manual data points")
    
    return manual_data


def collect_all_polls():
    """
    Main collection function - aggregates all polling data.
    """
    print("=" * 70)
    print("VibePoll-2026: Polling Data Collection")
    print(f"Agent: Kimi K2.5 | Framework: CommDAAF v1.0")
    print("=" * 70)
    print()
    
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    # Try scraping first
    rcp_data = scrape_rcp_generic_ballot()
    win_data = scrape_270towin_senate()
    
    # Add manual data as backup/supplement
    manual_data = collect_manual_polls()
    
    # Combine
    all_data = {
        'collection_timestamp': timestamp,
        'agent': 'kimi-k2.5',
        'framework': 'commdaaf-v1.0',
        'sources': {
            'rcp_generic_ballot': rcp_data,
            '270towin_senate': win_data,
            'manual_context': manual_data
        },
        'summary': {
            'scraped_sources': sum([1 for x in [rcp_data, win_data] if x is not None]),
            'manual_entries': len(manual_data),
            'total_entries': len(manual_data) + sum([1 for x in [rcp_data, win_data] if x is not None])
        }
    }
    
    # Save
    output_file = f"{OUTPUT_DIR}/polls_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(all_data, f, indent=2)
    
    print(f"\n{'=' * 70}")
    print("Collection complete!")
    print(f"{'=' * 70}")
    print(f"✓ Saved: {output_file}")
    print(f"  Scraped sources: {all_data['summary']['scraped_sources']}")
    print(f"  Manual entries: {all_data['summary']['manual_entries']}")
    print(f"  Total entries: {all_data['summary']['total_entries']}")
    
    return all_data


if __name__ == "__main__":
    # Check if BeautifulSoup is installed
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("⚠️  BeautifulSoup not installed. Install with: pip install beautifulsoup4")
        exit(1)
    
    data = collect_all_polls()
