
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json
import os

def scrape_rcp_generic_ballot():
    """Scrape RealClearPolling generic ballot average."""
    # Updated URL based on research
    url = "https://www.realclearpolling.com/polls/generic-ballot/2026/national/congressional-vote"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code != 200:
            print(f"RCP HTTP error {resp.status_code}")
            return None
            
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        # In 2026, the table structure might be different. Let's look for specific text
        # Finding the row with "RCP Average"
        avg_row = None
        for tr in soup.find_all('tr'):
            if 'RCP Average' in tr.text:
                avg_row = tr
                break
        
        if avg_row:
            cells = avg_row.find_all('td')
            if len(cells) >= 4:
                return {
                    'dem': cells[1].text.strip(),
                    'rep': cells[2].text.strip(),
                    'spread': cells[3].text.strip()
                }
    except Exception as e:
        print(f"RCP scrape error: {e}")
    
    return None


def scrape_270towin():
    """Scrape 270toWin predictions."""
    url = "https://www.270towin.com/2026-senate-election/"
    
    try:
        resp = requests.get(url, timeout=30)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return {'source': '270towin', 'scraped_at': datetime.now().isoformat()}
    except Exception as e:
        print(f"270toWin scrape error: {e}")
    
    return None


def collect_votehub():
    """Collect polling data from VoteHub API."""
    # Fallback to vote-hub.app if votehub.com/polls/api/ fails
    urls = ["https://votehub.com/polls/api/", "https://vote-hub.app/api/voter"]
    for url in urls:
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                return resp.json()
        except Exception as e:
            print(f"VoteHub API error for {url}: {e}")
    return None

def collect_538():
    """Collect generic ballot polling averages from FiveThirtyEight."""
    url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-generic-ballot/generic_topline.csv"
    try:
        df = pd.read_csv(url)
        # Convert to dictionary or list of records
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"FiveThirtyEight data error: {e}")
    return None

def collect_polls():
    """Collect all polling data."""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_dir = "agents/gemini/data/raw/polls"
    os.makedirs(output_dir, exist_ok=True)
    
    data = {
        'timestamp': timestamp,
        'rcp_generic_ballot': scrape_rcp_generic_ballot(),
        '270towin': scrape_270towin(),
        'votehub': collect_votehub(),
        'fivethirtyeight': collect_538()
    }
    
    output_file = f"{output_dir}/polls_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved: {output_file}")
    return data


if __name__ == "__main__":
    collect_polls()
