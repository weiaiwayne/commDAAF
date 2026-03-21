#!/usr/bin/env python3
"""
Polling Data Collection for VibePoll-2026

CommDAAF v1.0 - EXPLORATORY Tier
Collects polling data from key sources for 2026 midterm tracking.

Data Sources (prioritized by Silver Bulletin ratings):
1. 270toWin - Race ratings and predictions
2. Quinnipiac University Poll - Battleground state polls
3. Marist Poll (NPR/PBS) - National and state polls
4. Emerson College Polling - State polls
5. Race to the WH - Polling aggregator

Top-Rated Pollsters (Silver Bulletin 2026):
- Washington Post, Marquette University, NYT/Siena (elite tier)
- Quinnipiac, Marist, Emerson (high quality)

Output: data/raw/polls/polls_YYYY-MM-DD.json
"""

import json
import re
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "polls"
LOG_DIR = PROJECT_ROOT / "logs"

# URLs
SOURCES = {
    '270towin': {
        'senate': 'https://www.270towin.com/2026-senate-election/',
        'house': 'https://www.270towin.com/2026-house-election/',
        'governors': 'https://www.270towin.com/2026-governor-election/'
    },
    'quinnipiac': {
        'base': 'https://poll.qu.edu',
        'results': 'https://poll.qu.edu/poll-results'
    },
    'marist': {
        'base': 'https://maristpoll.marist.edu',
        'latest': 'https://maristpoll.marist.edu/latest-polls/'
    },
    'emerson': {
        'base': 'https://emersoncollegepolling.com',
        'polls': 'https://emersoncollegepolling.com/'
    },
    'racetothewh': {
        'senate': 'https://www.racetothewh.com/senate/26polls',
        'house': 'https://www.racetothewh.com/house'
    }
}

# Request settings
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Battleground states we're tracking
BATTLEGROUND_STATES = ['PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC', 'ME', 'NH', 'MN']

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


class PollCollector:
    """Collects polling data from multiple sources."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.stats = {
            '270towin': 0,
            'quinnipiac': 0,
            'marist': 0,
            'emerson': 0,
            'racetothewh': 0,
            'errors': 0
        }

    def _fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a webpage."""
        try:
            resp = self.session.get(url, timeout=TIMEOUT)
            if resp.status_code == 200:
                return BeautifulSoup(resp.content, 'html.parser')
            else:
                logger.warning(f"HTTP {resp.status_code}: {url}")
                return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            self.stats['errors'] += 1
            return None

    def _extract_number(self, text: str) -> Optional[float]:
        """Extract numeric value from text."""
        if not text:
            return None
        cleaned = re.sub(r'[^\d.\-]', '', str(text))
        try:
            return float(cleaned) if cleaned else None
        except ValueError:
            return None

    def collect_270towin_senate(self) -> Dict:
        """Collect 270toWin Senate race ratings."""
        logger.info("Collecting 270toWin Senate ratings...")

        result = {
            'source': '270towin',
            'type': 'senate_2026',
            'url': SOURCES['270towin']['senate'],
            'collected_at': datetime.now().isoformat(),
            'races': [],
            'summary': {'safe_d': 0, 'likely_d': 0, 'lean_d': 0,
                       'tossup': 0,
                       'lean_r': 0, 'likely_r': 0, 'safe_r': 0}
        }

        soup = self._fetch_page(SOURCES['270towin']['senate'])
        if not soup:
            return result

        # Look for state elements in the page
        # 270toWin uses various class patterns for states

        # Try to find the ratings table or map data
        for element in soup.find_all(['div', 'td', 'span', 'a']):
            text = element.get_text(strip=True)
            classes = ' '.join(element.get('class', []))

            # Look for state abbreviations with ratings
            state_match = re.search(r'\b(A[KLRZ]|C[AOT]|DE|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHVJMY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])\b', text)

            if state_match:
                state = state_match.group(1)

                # Determine rating from context
                rating = None
                full_text = text.lower()
                class_text = classes.lower()

                # Check classes and text for rating indicators
                if 'safe' in class_text and ('dem' in class_text or 'd4' in class_text):
                    rating = 'Safe D'
                elif 'safe' in class_text and ('rep' in class_text or 'r4' in class_text):
                    rating = 'Safe R'
                elif 'likely' in class_text and ('dem' in class_text or 'd3' in class_text):
                    rating = 'Likely D'
                elif 'likely' in class_text and ('rep' in class_text or 'r3' in class_text):
                    rating = 'Likely R'
                elif 'lean' in class_text and ('dem' in class_text or 'd2' in class_text):
                    rating = 'Lean D'
                elif 'lean' in class_text and ('rep' in class_text or 'r2' in class_text):
                    rating = 'Lean R'
                elif 'toss' in class_text or 'tossup' in full_text:
                    rating = 'Tossup'

                if rating and state not in [r['state'] for r in result['races']]:
                    result['races'].append({
                        'state': state,
                        'rating': rating,
                        'battleground': state in BATTLEGROUND_STATES
                    })

                    # Update summary
                    rating_key = rating.lower().replace(' ', '_')
                    if rating_key in result['summary']:
                        result['summary'][rating_key] += 1

                    self.stats['270towin'] += 1

        # Also try to extract any embedded JSON data
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'senate' in script.string.lower():
                # Try to find JSON data
                json_match = re.search(r'\{[^{}]*"state"[^{}]*\}', script.string)
                if json_match:
                    try:
                        data = json.loads(json_match.group())
                        logger.info(f"  Found embedded data: {data}")
                    except json.JSONDecodeError:
                        pass

        logger.info(f"  Found {len(result['races'])} Senate races")
        return result

    def collect_270towin_house(self) -> Dict:
        """Collect 270toWin House predictions."""
        logger.info("Collecting 270toWin House ratings...")

        result = {
            'source': '270towin',
            'type': 'house_2026',
            'url': SOURCES['270towin']['house'],
            'collected_at': datetime.now().isoformat(),
            'prediction': None,
            'competitive_races': []
        }

        soup = self._fetch_page(SOURCES['270towin']['house'])
        if not soup:
            return result

        # Look for seat count predictions
        for element in soup.find_all(['div', 'span', 'h2', 'h3']):
            text = element.get_text(strip=True)

            # Look for Democrat/Republican seat predictions
            dem_match = re.search(r'Democrat[s]?\s*[:=]?\s*(\d+)', text, re.I)
            rep_match = re.search(r'Republican[s]?\s*[:=]?\s*(\d+)', text, re.I)

            if dem_match and rep_match:
                result['prediction'] = {
                    'democrat_seats': int(dem_match.group(1)),
                    'republican_seats': int(rep_match.group(1))
                }
                self.stats['270towin'] += 1
                break

        logger.info(f"  House prediction: {result['prediction']}")
        return result

    def collect_quinnipiac(self) -> Dict:
        """Collect latest Quinnipiac polls."""
        logger.info("Collecting Quinnipiac polls...")

        result = {
            'source': 'quinnipiac',
            'url': SOURCES['quinnipiac']['results'],
            'collected_at': datetime.now().isoformat(),
            'polls': []
        }

        soup = self._fetch_page(SOURCES['quinnipiac']['results'])
        if not soup:
            return result

        # Look for poll entries (usually in article or list format)
        for article in soup.find_all(['article', 'div', 'li']):
            title = article.find(['h2', 'h3', 'h4', 'a'])
            if not title:
                continue

            title_text = title.get_text(strip=True)

            # Filter for relevant political polls
            if any(kw in title_text.lower() for kw in
                   ['approval', 'election', 'vote', 'senate', 'house', 'trump',
                    'democrat', 'republican', 'iran', 'economy']):

                # Try to extract date
                date_elem = article.find(['time', 'span'], class_=lambda x: x and 'date' in str(x).lower())
                date_text = date_elem.get_text(strip=True) if date_elem else None

                # Try to extract link
                link = title.get('href') if title.name == 'a' else None
                if link and not link.startswith('http'):
                    link = urljoin(SOURCES['quinnipiac']['base'], link)

                poll_entry = {
                    'title': title_text[:200],
                    'date': date_text,
                    'url': link,
                    'battleground_relevant': any(state in title_text for state in BATTLEGROUND_STATES)
                }

                # Avoid duplicates
                if poll_entry not in result['polls']:
                    result['polls'].append(poll_entry)
                    self.stats['quinnipiac'] += 1

        logger.info(f"  Found {len(result['polls'])} Quinnipiac polls")
        return result

    def collect_marist(self) -> Dict:
        """Collect latest Marist/NPR/PBS polls."""
        logger.info("Collecting Marist polls...")

        result = {
            'source': 'marist',
            'url': SOURCES['marist']['latest'],
            'collected_at': datetime.now().isoformat(),
            'polls': []
        }

        soup = self._fetch_page(SOURCES['marist']['latest'])
        if not soup:
            return result

        # Marist typically lists polls with titles and dates
        for article in soup.find_all(['article', 'div', 'li', 'a']):
            # Look for poll titles
            if article.name == 'a' and article.get('href', '').startswith('/polls/'):
                title_text = article.get_text(strip=True)
                link = urljoin(SOURCES['marist']['base'], article.get('href'))

                if title_text and len(title_text) > 10:
                    poll_entry = {
                        'title': title_text[:200],
                        'url': link,
                        'has_crosstabs': True  # Marist typically provides PDFs
                    }

                    if poll_entry not in result['polls']:
                        result['polls'].append(poll_entry)
                        self.stats['marist'] += 1

        # Also look for article blocks
        for block in soup.find_all(['div', 'article'], class_=lambda x: x and 'poll' in str(x).lower()):
            title_elem = block.find(['h2', 'h3', 'h4', 'a'])
            if title_elem:
                title_text = title_elem.get_text(strip=True)
                link_elem = block.find('a', href=True)
                link = urljoin(SOURCES['marist']['base'], link_elem['href']) if link_elem else None

                poll_entry = {
                    'title': title_text[:200],
                    'url': link,
                    'has_crosstabs': True
                }

                if poll_entry['title'] and poll_entry not in result['polls']:
                    result['polls'].append(poll_entry)
                    self.stats['marist'] += 1

        logger.info(f"  Found {len(result['polls'])} Marist polls")
        return result

    def collect_emerson(self) -> Dict:
        """Collect latest Emerson College polls."""
        logger.info("Collecting Emerson polls...")

        result = {
            'source': 'emerson',
            'url': SOURCES['emerson']['polls'],
            'collected_at': datetime.now().isoformat(),
            'polls': []
        }

        soup = self._fetch_page(SOURCES['emerson']['polls'])
        if not soup:
            return result

        # Look for poll entries
        for article in soup.find_all(['article', 'div', 'li']):
            title = article.find(['h2', 'h3', 'h4', 'a'])
            if not title:
                continue

            title_text = title.get_text(strip=True)

            # Filter for relevant polls (2026, state names, political topics)
            if any(kw in title_text.lower() for kw in
                   ['2026', 'poll', 'approval', 'election', 'senate', 'governor']) or \
               any(state in title_text for state in BATTLEGROUND_STATES):

                link = title.get('href') if title.name == 'a' else None
                if link and not link.startswith('http'):
                    link = urljoin(SOURCES['emerson']['base'], link)

                poll_entry = {
                    'title': title_text[:200],
                    'url': link
                }

                if poll_entry not in result['polls']:
                    result['polls'].append(poll_entry)
                    self.stats['emerson'] += 1

        logger.info(f"  Found {len(result['polls'])} Emerson polls")
        return result

    def collect_all(self) -> Dict:
        """Collect from all polling sources."""
        logger.info("=" * 60)
        logger.info("Starting Polling Data Collection")
        logger.info("=" * 60)

        timestamp = datetime.now().isoformat()

        data = {
            'metadata': {
                'timestamp': timestamp,
                'study': 'VibePoll-2026',
                'framework': 'CommDAAF v1.0',
                'sources': list(SOURCES.keys()),
                'top_pollsters_note': 'Silver Bulletin 2026 top-rated: Washington Post, Marquette, NYT/Siena'
            },
            '270towin_senate': self.collect_270towin_senate(),
            '270towin_house': self.collect_270towin_house(),
            'quinnipiac': self.collect_quinnipiac(),
            'marist': self.collect_marist(),
            'emerson': self.collect_emerson(),
            'stats': self.stats
        }

        logger.info("=" * 60)
        logger.info("COLLECTION COMPLETE")
        for source, count in self.stats.items():
            if source != 'errors':
                logger.info(f"  {source}: {count} items")
        logger.info(f"  Errors: {self.stats['errors']}")
        logger.info("=" * 60)

        return data

    def save(self, data: Dict, output_dir: Path) -> Path:
        """Save collected data to JSON."""
        timestamp = datetime.now().strftime('%Y-%m-%d')
        output_file = output_dir / f"polls_{timestamp}.json"

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)

        logger.info(f"Saved: {output_file}")
        return output_file


def main():
    """Main collection function."""
    collector = PollCollector()
    data = collector.collect_all()

    output_file = collector.save(data, OUTPUT_DIR)

    print("\n" + "=" * 60)
    print("POLLING DATA SUMMARY")
    print("=" * 60)

    # 270toWin Senate
    senate = data.get('270towin_senate', {})
    if senate.get('races'):
        print(f"\n270toWin Senate Races: {len(senate['races'])}")
        print(f"  Summary: {senate.get('summary')}")
        # Show battleground races
        bg_races = [r for r in senate['races'] if r.get('battleground')]
        if bg_races:
            print(f"  Battleground races: {len(bg_races)}")
            for race in bg_races:
                print(f"    - {race['state']}: {race['rating']}")

    # 270toWin House
    house = data.get('270towin_house', {})
    if house.get('prediction'):
        print(f"\n270toWin House: D {house['prediction']['democrat_seats']} / R {house['prediction']['republican_seats']}")

    # Pollster polls
    for source in ['quinnipiac', 'marist', 'emerson']:
        source_data = data.get(source, {})
        polls = source_data.get('polls', [])
        if polls:
            print(f"\n{source.title()} Polls: {len(polls)}")
            for poll in polls[:3]:
                print(f"  - {poll['title'][:60]}...")

    print(f"\nOutput: {output_file}")

    return data


if __name__ == "__main__":
    main()
