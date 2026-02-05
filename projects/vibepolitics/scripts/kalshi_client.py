#!/usr/bin/env python3
"""
Kalshi API Client with RSA Authentication
"""
import json
import time
import base64
import requests
from datetime import datetime
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Load credentials
SECRETS_DIR = Path.home() / ".openclaw/secrets/kalshi"
API_KEY = (SECRETS_DIR / "api_key.txt").read_text().strip()
PRIVATE_KEY_PEM = (SECRETS_DIR / "private_key.pem").read_text()

# API base URL
BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

def load_private_key():
    """Load RSA private key from PEM"""
    return serialization.load_pem_private_key(
        PRIVATE_KEY_PEM.encode(),
        password=None,
        backend=default_backend()
    )

def sign_request(method: str, path: str, timestamp: str) -> str:
    """Sign API request with RSA private key"""
    private_key = load_private_key()
    message = f"{timestamp}{method}{path}".encode()
    
    signature = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

def kalshi_request(method: str, endpoint: str, params: dict = None, data: dict = None):
    """Make authenticated request to Kalshi API"""
    path = f"/trade-api/v2{endpoint}"
    url = f"{BASE_URL}{endpoint}"
    timestamp = str(int(time.time() * 1000))
    
    signature = sign_request(method.upper(), path, timestamp)
    
    headers = {
        "KALSHI-ACCESS-KEY": API_KEY,
        "KALSHI-ACCESS-SIGNATURE": signature,
        "KALSHI-ACCESS-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }
    
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        json=data,
        timeout=30
    )
    
    return response

def get_markets(limit=100, cursor=None, status="active"):
    """Get markets list"""
    params = {"limit": limit, "status": status}
    if cursor:
        params["cursor"] = cursor
    return kalshi_request("GET", "/markets", params=params)

def get_market(ticker: str):
    """Get single market details"""
    return kalshi_request("GET", f"/markets/{ticker}")

def get_events(limit=100, status="active"):
    """Get events list"""
    params = {"limit": limit, "status": status}
    return kalshi_request("GET", "/events", params=params)

def get_event(ticker: str):
    """Get single event details"""
    return kalshi_request("GET", f"/events/{ticker}")

def get_series(series_ticker: str):
    """Get series details"""
    return kalshi_request("GET", f"/series/{series_ticker}")

def get_market_history(ticker: str, limit=1000):
    """Get market trade history"""
    params = {"limit": limit}
    return kalshi_request("GET", f"/markets/{ticker}/history", params=params)

def get_market_candlesticks(series_ticker: str, ticker: str, period="1h"):
    """Get market candlesticks"""
    params = {"period_interval": period}
    return kalshi_request("GET", f"/series/{series_ticker}/markets/{ticker}/candlesticks", params=params)

if __name__ == "__main__":
    print("Testing Kalshi API connection...")
    
    # Test basic auth
    response = get_markets(limit=3)
    print(f"\nMarkets response status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Success! Found {len(data.get('markets', []))} markets")
        for m in data.get('markets', [])[:3]:
            print(f"  - {m.get('ticker')}: {m.get('title', m.get('subtitle', 'N/A'))}")
    else:
        print(f"Error: {response.text}")
