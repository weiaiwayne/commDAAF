# Vibe Polling Study: Google Trends-Based Unconventional Public Opinion Analysis

**Study Name:** VibePoll-2026  
**Framework:** CommDAAF v1.0  
**Validation Tier:** 🟢 EXPLORATORY  
**Date:** 2026-03-19  
**Principal Investigator:** Wayne Xu (UMass-Amherst)  
**Coordinating Agent:** OpenClaw (Main Session)

---

## ⚠️ CRITICAL: COMMDAAF ACTIVATION REQUIRED ⚠️

**Before executing ANY task in this plan, you MUST:**

```
1. READ: skills/commdaaf/SKILL.md
2. READ: projects/comm-research-skill/agent-academy-study-protocol.md
3. CONFIRM: "CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."
```

**Key CommDAAF guardrails for this study:**
- ✅ Mandatory distribution diagnostics before regression
- ✅ Never use OLS on count/engagement data (use Negative Binomial)
- ✅ Report effect sizes with confidence intervals
- ✅ Document all methodological decisions
- ✅ Adversarial peer review before conclusions

**⚠️ SEARCH TERM WARNING:**
- Use ONLY realistic terms real people actually search
- NO academic jargon ("labor displacement" → "AI taking jobs")
- Verify search volume exists before including any term
- See Section 6 for detailed guidance

**Failure to activate CommDAAF = invalid analysis. HALT and re-read.**

---

## Executive Summary

This study develops and validates a "Vibe Polling" methodology using Google Trends search data from US battleground states to gauge public sentiment on key political issues ahead of the 2026 midterms and 2028 presidential election. We compare Google Trends signals to prediction market odds (Polymarket, Kalshi) and traditional polling aggregators (RealClearPolitics, 270toWin).

**Core Innovation:** Rather than asking people what they think (polls) or what they'll bet on (prediction markets), we observe what they're actually searching for — revealing revealed preferences and information-seeking behavior that may capture sentiment polls miss.

---

## Table of Contents

1. [Research Questions](#1-research-questions)
2. [Theoretical Framework](#2-theoretical-framework)
3. [Current Political Context (March 2026)](#3-current-political-context-march-2026)
4. [Data Sources](#4-data-sources)
5. [Battleground States](#5-battleground-states)
6. [Search Term Design](#6-search-term-design)
7. [Data Collection Protocol](#7-data-collection-protocol)
8. [Analysis Plan](#8-analysis-plan)
9. [Validation Against Traditional Measures](#9-validation-against-traditional-measures)
10. [Agent Execution Plan](#10-agent-execution-plan)
11. [Expected Outputs](#11-expected-outputs)
12. [Quality Control](#12-quality-control)
13. [Limitations](#13-limitations)
14. [File Structure](#14-file-structure)
15. [Timeline](#15-timeline)

---

## 1. Research Questions

### Primary RQ
**RQ1:** Can Google Trends search volume for issue-related terms in battleground states predict or correlate with prediction market movements and traditional polling shifts?

### Secondary RQs
**RQ2:** Which issue categories (economy, immigration, foreign policy, AI/automation) show the strongest Trends-to-sentiment correlation?

**RQ3:** Do Google Trends signals lead, lag, or move synchronously with prediction markets?

**RQ4:** Are there state-level variations in issue salience that traditional national polls miss?

---

## 2. Theoretical Framework

### 2.1 Revealed Preference Theory
Search behavior represents **revealed preferences** — what people actually care about vs. what they claim to care about in surveys. When someone searches "gas prices near me" at 2am, they're revealing genuine economic anxiety.

### 2.2 Information Seeking as Political Engagement
Political information-seeking behavior (searching candidate names, policy terms) correlates with voting intention and turnout (Stephens-Davidowitz 2017).

### 2.3 Wisdom of Crowds vs. Wisdom of Search
Prediction markets aggregate distributed knowledge via betting. Google Trends aggregates distributed attention via searching. Both may outperform traditional polls under certain conditions (Berg et al. 2008; Mavragani & Tsagarakis 2016).

### 2.4 Prior Literature
| Study | Finding | Relevance |
|-------|---------|-----------|
| Stephens-Davidowitz (2017) | GT predicted Trump 2016 better than polls | Direct precedent |
| Ma-Kellams et al. (2020) | GT main predictor of electoral choice | Search > demographics |
| Chen et al. (2024) | Polymarket validated for academic research | PM as benchmark |
| Berg et al. (2008) | Prediction markets outperform polls 74% | PM baseline |

---

## 3. Current Political Context (March 2026)

### 3.1 Major Events/Issues

| Issue | Status (March 2026) | Search Relevance |
|-------|---------------------|------------------|
| **Iran War** | Active conflict since Feb 28; only 25% support US strikes (Reuters/Ipsos); 74% oppose ground troops (Quinnipiac) | High search volume expected for war news, casualties, gas prices |
| **Economy** | Rough start to 2026; job losses, rising gas prices, uncertainty (AP/PBS) | "Cost of living" top voter concern (52%, Politico) |
| **Gas Prices** | $90/barrel oil; >$3/gallon nationally; war-driven spike | Direct pocketbook issue |
| **Immigration/ICE** | Massive crackdown; 50% support abolishing ICE (Guardian poll); "phase two" deportations | Highly polarizing |
| **AI/Automation** | 85M jobs displaced globally (estimated); Anthropic CEO warns 10-20% unemployment possible | Growing anxiety |
| **Epstein Files** | 3.5M pages released; heavily redacted; ongoing controversy | Episodic attention spikes |
| **Inflation** | Above Fed 2% target; tariff effects working through economy | Persistent concern |

### 3.2 Midterm Landscape

| Indicator | Current Status |
|-----------|---------------|
| Polymarket: Dem House odds | ~74-78% |
| Polymarket: "Dem Sweep" | 50% |
| Key Senate races | GA (Ossoff), MI, ME, NC |
| Trump approval | Mixed; Iran war hurting |
| Top voter issue | Cost of living (52%) |

---

## 4. Data Sources

### 4.1 Google Trends
- **API:** PyTrends (unofficial) or manual CSV export
- **Granularity:** Weekly or daily
- **Geographic:** State-level (battleground states)
- **Time range:** 2025-01-01 to present (to capture Trump 2nd term)
- **Normalization:** Relative search volume (0-100 scale)

### 4.2 Prediction Markets
| Platform | Markets | Access |
|----------|---------|--------|
| **Polymarket** | Balance of Power 2026, State Senate races | `gamma-api.polymarket.com` (free, no auth) |
| **Kalshi** | House/Senate control, state races | `api.elections.kalshi.com` |

**Key markets to track:**
- "Democrats win House 2026"
- "Republicans win Senate 2026"  
- "Balance of Power: 2026 Midterms"
- State-specific Senate races (GA, MI, TX)

### 4.3 Traditional Polls
| Aggregator | URL | Scraping/Access |
|------------|-----|-----------------|
| RealClearPolitics | realclearpolitics.com/epolls/2026/ | Scrape or manual |
| 270toWin | 270towin.com/2026-senate-election/ | Scrape or manual |
| FiveThirtyEight | fivethirtyeight.com/politics/ | API (limited) |

**Metrics to collect:**
- Generic ballot (D vs R)
- Congressional approval
- Trump approval (state-level if available)
- Issue-specific polling (economy, immigration, etc.)

---

## 5. Battleground States

### 5.1 Core Battleground States (7)

| State | 2024 Trump Margin | Key 2026 Race | Priority |
|-------|-------------------|---------------|----------|
| **Pennsylvania** | +1.8% | House seats, Gov | Tier 1 |
| **Michigan** | +1.4% | Senate (D-held), Gov | Tier 1 |
| **Wisconsin** | +0.9% | Gov | Tier 1 |
| **Arizona** | +2.2% | House seats | Tier 1 |
| **Georgia** | +2.2% | Senate (Ossoff) | Tier 1 |
| **Nevada** | +3.0% | House seats | Tier 2 |
| **North Carolina** | +3.3% | Senate (R-held) | Tier 2 |

### 5.2 Emerging Battlegrounds (Watch List)

| State | Notes |
|-------|-------|
| **Maine** | Senate race (Collins?), could flip |
| **New Hampshire** | Potential GOP target if AZ/NV drift R |
| **Minnesota** | Watch if Latino shift continues |

### 5.3 Control States (for baseline)

| State | Lean | Purpose |
|-------|------|---------|
| California | Safe D | Liberal baseline |
| Texas | Safe R | Conservative baseline |
| Ohio | Lean R | Midwest non-battleground |

---

## 6. Search Term Design

### ⚠️ CRITICAL: REALISTIC SEARCH TERMS ONLY ⚠️

**This is the most important methodological decision in the study.**

Agents MUST exercise extreme care when proposing or modifying search terms. The validity of Google Trends data depends entirely on using terms that **real people actually type into Google** — not academic jargon, not policy abstractions, not researcher-invented phrases.

**Before adding ANY search term, ask:**
1. Would my neighbor type this into Google?
2. Would a tired person at 11pm type this exact phrase?
3. Is this how the term appears in news headlines people click?
4. Have I verified this term has actual search volume on Google Trends?

**Common mistakes to AVOID:**

| ❌ Academic/Abstract | ✅ Real Search Behavior |
|---------------------|------------------------|
| "economic anxiety" | "gas prices near me" |
| "immigration enforcement" | "ICE raid" |
| "labor market displacement" | "AI taking jobs" |
| "electoral participation" | "how to vote" |
| "foreign policy concerns" | "Iran war" |
| "inflationary pressures" | "why is food so expensive" |
| "authoritarian governance" | (people don't search this) |

**Validation requirement:** Before finalizing any term list, agents SHOULD:
1. Spot-check 5-10 terms on Google Trends to verify search volume
2. Look at "Related queries" for real user phrasing
3. Remove any term with near-zero volume in target states

### 6.1 Design Principles

1. **Realistic terms:** What people ACTUALLY type, not academic abstractions
2. **Specificity:** "gas prices near me" > "inflation"
3. **Action-oriented:** Terms suggesting intent or concern
4. **Avoid leading:** Don't assume partisan framing
5. **Include misspellings:** Common typos matter
6. **Verify volume:** Check Google Trends before including

### 6.2 Issue Categories & Search Terms

#### ECONOMY / COST OF LIVING
| Term | Rationale |
|------|-----------|
| `gas prices` | Direct pocketbook concern |
| `gas prices near me` | Local intent |
| `grocery prices` | Food inflation |
| `rent prices` | Housing costs |
| `cost of living` | General economic anxiety |
| `inflation` | Macro-level concern |
| `recession` | Fear-based searching |
| `unemployment benefits` | Job loss anxiety |
| `food stamps` / `SNAP benefits` | Economic hardship |
| `minimum wage` | Working class concern |
| `401k` / `stock market crash` | Investor anxiety |

#### IMMIGRATION / ICE
| Term | Rationale |
|------|-----------|
| `ICE raid` | Enforcement activity |
| `deportation` | Policy concern |
| `immigration lawyer` | Personal need |
| `asylum` | Policy/humanitarian |
| `border wall` | Symbolic issue |
| `illegal immigration` | Right-leaning framing |
| `undocumented immigrants` | Left-leaning framing |
| `work visa` / `H1B` | Legal immigration |
| `green card` | Immigration process |
| `DACA` | Specific policy |

#### FOREIGN POLICY / IRAN WAR
| Term | Rationale |
|------|-----------|
| `Iran war` | Direct conflict search |
| `Iran news` | Following developments |
| `US troops Iran` | Casualty concerns |
| `draft` / `military draft` | Fear-based (likely spike if escalation) |
| `Iran casualties` | Human cost |
| `Strait of Hormuz` | Oil supply concern |
| `oil prices` | Economic impact of war |
| `World War 3` | Catastrophizing/fear |
| `nuclear war` | Extreme fear |

#### AI / AUTOMATION / JOBS
| Term | Rationale |
|------|-----------|
| `AI taking jobs` | Direct fear |
| `will AI replace` | Uncertainty |
| `ChatGPT` | Specific tool awareness |
| `AI layoffs` | Job loss news |
| `automation` | General displacement |
| `learn to code` | Reskilling intent |
| `career change` | Economic anxiety |
| `job training` | Adaptation |
| `trucking jobs` | Blue collar concern |
| `customer service jobs` | White collar concern |

#### EPSTEIN FILES
| Term | Rationale |
|------|-----------|
| `Epstein files` | Direct search |
| `Epstein list` | Looking for names |
| `Epstein documents` | Primary source seeking |
| `Epstein names` | Curiosity about associates |
| `Jeffrey Epstein` | General interest |

#### POLITICAL / ELECTORAL
| Term | Rationale |
|------|-----------|
| `how to vote` | Engagement intent |
| `voter registration` | Participation intent |
| `midterm elections` | Awareness |
| `who is my representative` | Civic engagement |
| `Trump approval` | Presidential tracking |
| `impeachment` | Political drama |
| `Democrat` / `Republican` | Party searching |
| `[Candidate name]` | Specific race awareness |

#### HEALTHCARE / SOCIAL
| Term | Rationale |
|------|-----------|
| `health insurance` | Coverage concern |
| `Affordable Care Act` / `Obamacare` | Policy |
| `Medicare` / `Medicaid` | Government programs |
| `abortion laws` + `[state]` | Post-Dobbs |
| `gun laws` + `[state]` | After any shooting |

### 6.3 Comparison Pairs (Partisan Signal Detection)

Track search ratios to detect partisan lean:
- `Fox News` vs `CNN` vs `MSNBC`
- `Trump rally` vs `protest`
- `illegal immigration` vs `undocumented immigrants`
- `pro-life` vs `pro-choice`
- `Second Amendment` vs `gun control`

### 6.4 State-Specific Terms

| State | Local Terms to Add |
|-------|-------------------|
| Michigan | `auto industry`, `UAW`, `Detroit jobs` |
| Pennsylvania | `fracking`, `steel jobs`, `Philadelphia crime` |
| Arizona | `border patrol`, `Phoenix traffic`, `water shortage` |
| Georgia | `Atlanta traffic`, `election fraud` (legacy), `Stacey Abrams` |
| Wisconsin | `dairy farms`, `Milwaukee crime`, `cheese prices` (seriously) |

---

## 7. Data Collection Protocol

### 7.1 Google Trends Collection

**Frequency:** Weekly snapshot (every Sunday)

**Script: `collect_trends.py`**

```python
"""
Google Trends data collection for Vibe Polling study.
Run weekly via cron or manual execution.
"""

from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime, timedelta
import time
import json

# Configuration
STATES = {
    'battleground': ['PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC'],
    'control': ['CA', 'TX', 'OH'],
    'watch': ['ME', 'NH', 'MN']
}

# Flatten for iteration
ALL_STATES = STATES['battleground'] + STATES['control'] + STATES['watch']

# State codes for Google Trends (use geo parameter)
STATE_CODES = {
    'PA': 'US-PA', 'MI': 'US-MI', 'WI': 'US-WI', 'AZ': 'US-AZ',
    'GA': 'US-GA', 'NV': 'US-NV', 'NC': 'US-NC', 'CA': 'US-CA',
    'TX': 'US-TX', 'OH': 'US-OH', 'ME': 'US-ME', 'NH': 'US-NH',
    'MN': 'US-MN'
}

# Search term categories
TERMS = {
    'economy': [
        'gas prices', 'gas prices near me', 'grocery prices', 'rent prices',
        'cost of living', 'inflation', 'recession', 'unemployment benefits',
        'food stamps', 'minimum wage', '401k'
    ],
    'immigration': [
        'ICE raid', 'deportation', 'immigration lawyer', 'asylum',
        'border wall', 'illegal immigration', 'undocumented immigrants',
        'work visa', 'H1B', 'DACA'
    ],
    'iran_war': [
        'Iran war', 'Iran news', 'US troops Iran', 'military draft',
        'Iran casualties', 'Strait of Hormuz', 'oil prices',
        'World War 3', 'nuclear war'
    ],
    'ai_jobs': [
        'AI taking jobs', 'will AI replace', 'ChatGPT', 'AI layoffs',
        'automation', 'learn to code', 'career change', 'job training'
    ],
    'epstein': [
        'Epstein files', 'Epstein list', 'Epstein documents',
        'Epstein names', 'Jeffrey Epstein'
    ],
    'political': [
        'how to vote', 'voter registration', 'midterm elections',
        'Trump approval', 'impeachment'
    ],
    'partisan_pairs': [
        'Fox News', 'CNN', 'MSNBC',
        'illegal immigration', 'undocumented immigrants',
        'pro-life', 'pro-choice'
    ]
}

def collect_trends_for_state(state_code, terms, timeframe='today 3-m'):
    """
    Collect Google Trends data for a state and list of terms.
    
    Args:
        state_code: Google geo code (e.g., 'US-PA')
        terms: List of search terms (max 5 per request)
        timeframe: Time range (e.g., 'today 3-m' for past 3 months)
    
    Returns:
        DataFrame with search interest over time
    """
    pytrends = TrendReq(hl='en-US', tz=300)  # EST timezone
    
    results = []
    
    # Google Trends API allows max 5 terms per request
    for i in range(0, len(terms), 5):
        batch = terms[i:i+5]
        
        try:
            pytrends.build_payload(batch, geo=state_code, timeframe=timeframe)
            interest = pytrends.interest_over_time()
            
            if not interest.empty:
                interest['state'] = state_code
                results.append(interest)
            
            # Rate limiting
            time.sleep(2)
            
        except Exception as e:
            print(f"Error for {state_code} batch {i//5}: {e}")
            time.sleep(10)
    
    if results:
        return pd.concat(results, axis=1)
    return pd.DataFrame()


def collect_all_states():
    """
    Main collection function. Run weekly.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d')
    all_data = []
    
    for state, code in STATE_CODES.items():
        print(f"Collecting: {state}")
        
        for category, terms in TERMS.items():
            print(f"  Category: {category}")
            
            df = collect_trends_for_state(code, terms)
            if not df.empty:
                df['category'] = category
                df['collected_at'] = timestamp
                all_data.append(df)
            
            time.sleep(5)  # Between categories
    
    # Combine and save
    if all_data:
        combined = pd.concat(all_data)
        output_file = f"data/trends/trends_{timestamp}.parquet"
        combined.to_parquet(output_file)
        print(f"Saved: {output_file}")
        return combined
    
    return None


if __name__ == "__main__":
    collect_all_states()
```

### 7.2 Prediction Market Collection

**Script: `collect_markets.py`**

```python
"""
Prediction market data collection from Polymarket and Kalshi.
"""

import requests
import pandas as pd
from datetime import datetime
import json

# Polymarket API (gamma-api)
POLYMARKET_BASE = "https://gamma-api.polymarket.com"

# Key markets to track
POLYMARKET_SLUGS = [
    "balance-of-power-2026-midterms",
    "will-democrats-win-the-house-in-2026",
    "will-republicans-win-the-senate-in-2026",
    # Add state-specific as available
]

def collect_polymarket():
    """Collect current odds from Polymarket."""
    results = []
    
    for slug in POLYMARKET_SLUGS:
        try:
            url = f"{POLYMARKET_BASE}/markets/{slug}"
            resp = requests.get(url, timeout=30)
            
            if resp.status_code == 200:
                data = resp.json()
                results.append({
                    'market': slug,
                    'timestamp': datetime.now().isoformat(),
                    'outcomes': data.get('outcomes', []),
                    'volume': data.get('volume'),
                    'liquidity': data.get('liquidity')
                })
        except Exception as e:
            print(f"Error fetching {slug}: {e}")
    
    return results


def collect_kalshi():
    """Collect current odds from Kalshi."""
    # Kalshi API endpoint for 2026 elections
    url = "https://trading-api.kalshi.com/v2/markets"
    params = {
        'limit': 100,
        'status': 'open',
        'series_ticker': 'CONGRESS'  # Adjust as needed
    }
    
    try:
        resp = requests.get(url, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json().get('markets', [])
    except Exception as e:
        print(f"Kalshi error: {e}")
    
    return []


def save_market_snapshot():
    """Save daily market snapshot."""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'timestamp': timestamp,
        'polymarket': collect_polymarket(),
        'kalshi': collect_kalshi()
    }
    
    output_file = f"data/markets/markets_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved: {output_file}")
    return data


if __name__ == "__main__":
    save_market_snapshot()
```

### 7.3 Polling Aggregator Collection

**Script: `collect_polls.py`**

```python
"""
Polling data collection from RCP and 270toWin.
Semi-automated (may require manual review).
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_rcp_generic_ballot():
    """Scrape RealClearPolitics generic ballot average."""
    url = "https://www.realclearpolitics.com/epolls/other/2026_generic_congressional_vote-7785.html"
    
    try:
        resp = requests.get(url, timeout=30)
        soup = BeautifulSoup(resp.content, 'html.parser')
        
        # Find the RCP average row
        # Note: Actual selectors may need adjustment
        table = soup.find('table', {'class': 'data'})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                if 'RCP Average' in row.text:
                    cells = row.find_all('td')
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
        
        # Extract state-by-state ratings
        # Actual implementation depends on page structure
        # This is a placeholder
        return {'source': '270towin', 'scraped_at': datetime.now().isoformat()}
    
    except Exception as e:
        print(f"270toWin scrape error: {e}")
    
    return None


def collect_polls():
    """Collect all polling data."""
    timestamp = datetime.now().strftime('%Y-%m-%d')
    
    data = {
        'timestamp': timestamp,
        'rcp_generic_ballot': scrape_rcp_generic_ballot(),
        '270towin': scrape_270towin()
    }
    
    output_file = f"data/polls/polls_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved: {output_file}")
    return data


if __name__ == "__main__":
    collect_polls()
```

---

## 8. Analysis Plan

### 8.1 Descriptive Analysis

**For each data collection wave:**

1. **Trends distribution by state**
   - Heatmap: States × Issues
   - Time series: Weekly trend for each term

2. **Cross-state comparisons**
   - Which issues are hot in which states?
   - Do battleground states differ from control states?

3. **Temporal patterns**
   - Event-driven spikes (Iran escalation, Epstein release, ICE raids)
   - Weekly cycles (political news cycles)

### 8.2 Correlation Analysis

**Hypothesis: Trends signals correlate with prediction market movements**

```python
def analyze_trends_market_correlation(trends_df, market_df):
    """
    Correlate Google Trends with prediction market movements.
    
    Tests:
    1. Same-day correlation (synchronous)
    2. Trends leads market (predictive)
    3. Market leads trends (reactive)
    """
    
    from scipy import stats
    
    results = []
    
    # Lag analysis: -7 to +7 days
    for lag in range(-7, 8):
        # Shift trends relative to market
        shifted = trends_df['value'].shift(lag)
        
        # Calculate correlation
        valid = ~(shifted.isna() | market_df['price'].isna())
        corr, p = stats.pearsonr(shifted[valid], market_df['price'][valid])
        
        results.append({
            'lag_days': lag,
            'correlation': corr,
            'p_value': p,
            'interpretation': 'Trends leads' if lag > 0 else 'Market leads' if lag < 0 else 'Synchronous'
        })
    
    return pd.DataFrame(results)
```

### 8.3 Issue Salience Index

**Create composite indices for each issue area:**

```python
def calculate_issue_salience(trends_df, state, issue_category):
    """
    Calculate normalized issue salience index.
    
    Formula:
    salience = mean(z-scores of all terms in category)
    """
    import numpy as np
    from scipy.stats import zscore
    
    # Filter to state and category
    subset = trends_df[
        (trends_df['state'] == state) & 
        (trends_df['category'] == issue_category)
    ]
    
    # Z-score normalize each term
    normalized = subset.groupby('term')['value'].transform(zscore)
    
    # Average across terms
    salience = normalized.groupby(subset['date']).mean()
    
    return salience
```

### 8.4 Vibe Index Construction

**Create a single "political vibe" index per state:**

```python
def calculate_vibe_index(trends_df, state, weights=None):
    """
    Weighted composite of issue saliences.
    
    Default weights based on polling importance:
    - economy: 0.35
    - immigration: 0.20
    - foreign_policy: 0.15
    - healthcare: 0.15
    - other: 0.15
    """
    if weights is None:
        weights = {
            'economy': 0.35,
            'immigration': 0.20,
            'iran_war': 0.15,
            'ai_jobs': 0.10,
            'political': 0.20
        }
    
    components = {}
    for category, weight in weights.items():
        salience = calculate_issue_salience(trends_df, state, category)
        components[category] = salience * weight
    
    vibe_index = sum(components.values())
    
    return vibe_index, components
```

### 8.5 Validation Against Polls

**Compare Vibe Index to polling movements:**

```python
def validate_against_polls(vibe_index, polls_df):
    """
    Correlate Vibe Index with generic ballot / approval changes.
    """
    from scipy import stats
    
    # Align dates
    merged = vibe_index.to_frame('vibe').join(
        polls_df.set_index('date')['dem_lead'], 
        how='inner'
    )
    
    # Correlation
    corr, p = stats.pearsonr(merged['vibe'], merged['dem_lead'])
    
    # Granger causality (simple lag test)
    # Does vibe predict next week's polling?
    merged['vibe_lag1'] = merged['vibe'].shift(1)
    merged['poll_change'] = merged['dem_lead'].diff()
    
    lag_corr, lag_p = stats.pearsonr(
        merged['vibe_lag1'].dropna(),
        merged['poll_change'].dropna()
    )
    
    return {
        'concurrent_r': corr,
        'concurrent_p': p,
        'predictive_r': lag_corr,
        'predictive_p': lag_p
    }
```

---

## 9. Validation Against Traditional Measures

### 9.1 Benchmarks

| Source | Metric | Expected Relationship |
|--------|--------|----------------------|
| Polymarket | Dem House odds | Positive correlation with economy anxiety in red areas |
| Kalshi | GOP Senate odds | Positive correlation with immigration searches in border states |
| RCP | Generic ballot | Vibe Index should track within ±3% |
| FiveThirtyEight | Approval rating | State-level approval should correlate with local issue salience |

### 9.2 Success Criteria

| Criterion | Threshold | Measurement |
|-----------|-----------|-------------|
| Concurrent correlation (Trends vs. Market) | r > 0.3 | Pearson correlation |
| Predictive power (Trends → Market) | Granger p < 0.05 | Granger causality test |
| State differentiation | >20% variance explained by state | ANOVA |
| Issue distinctiveness | Categories load separately | Factor analysis |

### 9.3 Failure Modes to Watch

1. **Noise dominance:** Search data too noisy to extract signal
2. **Lag mismatch:** Trends and markets operate on different timescales
3. **Platform bias:** Google users ≠ voters
4. **Event confounding:** Major events swamp baseline patterns

---

## 10. Agent Execution Plan

### 10.0 MANDATORY: Activate CommDAAF Guardrails

**⚠️ ALL AGENTS MUST READ AND FOLLOW COMMDAAF BEFORE ANY ANALYSIS ⚠️**

Before executing ANY task in this plan, each agent MUST:

1. **Load the CommDAAF skill:**
   ```
   Read: skills/commdaaf/SKILL.md
   ```

2. **Load the AgentAcademy protocol:**
   ```
   Read: projects/comm-research-skill/agent-academy-study-protocol.md
   ```

3. **Declare validation tier:** This study is **🟢 EXPLORATORY**

4. **Follow CommDAAF core behaviors:**
   - Never run analysis without explicit parameters
   - Probe before proceeding (ask clarifying questions)
   - Require distribution diagnostics before regression
   - Report effect sizes, not just p-values
   - Document all methodological decisions

5. **Activate these CommDAAF guardrails:**
   - ✅ Mandatory distribution diagnostics (Section 7.1 of protocol)
   - ✅ Model selection decision tree (NB for count data, not OLS)
   - ✅ Effect size interpretation (IRR for count models)
   - ✅ Multiple comparison correction if testing multiple terms
   - ✅ Adversarial peer review before conclusions

**If an agent fails to acknowledge CommDAAF activation, halt and re-prompt.**

### 10.1 Multi-Agent Architecture

| Agent | Tool | Model | Role |
|-------|------|-------|------|
| **Coordinator** | OpenClaw | Claude Opus 4.5 | Orchestration, synthesis, reporting |
| **Data Analyst 1** | Claude Code | Claude Sonnet 4.5 | Trends collection, cleaning, descriptives |
| **Data Analyst 2** | OpenCode | GLM-4.7 | Market data, correlation analysis |
| **Statistician** | OpenCode | Kimi K2.5 | Regression modeling, validation |
| **Reviewer** | OpenClaw | DeepSeek/Grok | Adversarial review |

### 10.2 Execution Sequence

**Phase 1: Data Collection (Day 1)**

```bash
# Claude Code - Trends collection
claude-code run "
FIRST: Read skills/commdaaf/SKILL.md and activate CommDAAF guardrails.
Confirm: 'CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY.'

⚠️ SEARCH TERM VALIDATION (CRITICAL - see Section 6):
Before collecting data, verify search terms are REALISTIC:
- Would a real person type this into Google?
- Spot-check 5-10 terms on Google Trends for actual volume
- Replace any academic jargon with real-world phrasing
- Remove zero-volume terms
- Log any term modifications with rationale

THEN:
1. Create directory structure per PLAN.md section 14
2. Validate search terms per above (document in logs/)
3. Run collect_trends.py for all states
4. Save to data/trends/trends_YYYY-MM-DD.parquet
5. Generate initial summary stats
6. Document any data collection decisions in logs/collection_log.txt
"

# OpenCode GLM - Market collection
opencode -m zai-coding-plan/glm-4.7 run "
FIRST: Read skills/commdaaf/SKILL.md and activate CommDAAF guardrails.
Confirm: 'CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY.'

THEN:
1. Run collect_markets.py
2. Run collect_polls.py
3. Save to respective directories
4. Cross-check data completeness
5. Document any issues in logs/collection_log.txt
"
```

**Phase 2: Data Processing (Day 1-2)**

```bash
# Claude Code - Data cleaning
claude-code run "
FIRST: Confirm CommDAAF v1.0 active. If not, read skills/commdaaf/SKILL.md.

THEN:
1. Load all collected data
2. Handle missing values (DOCUMENT all decisions per CommDAAF transparency requirement)
3. Normalize search volumes across states
4. Calculate z-scores per term
5. Save processed data to data/processed/
6. Log all transformations with rationale
"

# OpenCode Kimi - Data validation
opencode -m kimi-coding/k2p5 run "
FIRST: Read skills/commdaaf/SKILL.md and activate CommDAAF guardrails.
Confirm: 'CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY.'

THEN (per CommDAAF Section 7.1 - MANDATORY DIAGNOSTICS):
1. Verify data integrity
2. Check for outliers
3. Generate distribution diagnostics:
   - Skewness for all numeric variables
   - % zeros
   - Variance/mean ratio
4. Flag any anomalies
5. Output diagnostics to analysis/descriptives/distribution_diagnostics.json
"
```

**Phase 3: Analysis (Day 2-3)**

```bash
# Claude Code - Descriptive analysis
claude-code run "
FIRST: Confirm CommDAAF v1.0 active.

THEN:
1. Generate heatmaps: States × Issues
2. Create time series plots with event annotations
3. Calculate issue salience indices (document weighting decisions)
4. Build Vibe Index per state
5. Save figures to outputs/figures/
6. All figures must include clear labels, legends, and source notes
"

# OpenCode GLM - Correlation analysis
opencode -m zai-coding-plan/glm-4.7 run "
FIRST: Confirm CommDAAF v1.0 active.

THEN:
1. Merge Trends with market data
2. Run lag correlation analysis (-7 to +7 days)
3. Test Granger causality
4. Document lead/lag relationships
5. Report correlation coefficients WITH confidence intervals
6. Flag any r > 0.7 as potentially spurious (check for confounds)
"

# OpenCode Kimi - Statistical modeling
opencode -m kimi-coding/k2p5 run "
FIRST: Confirm CommDAAF v1.0 active.

CRITICAL - FOLLOW COMMDAAF REGRESSION PROTOCOL (Section 7):
1. Run distribution diagnostics on ALL DVs BEFORE model selection
2. Apply model selection decision tree:
   - Count/engagement data → Negative Binomial (NOT OLS)
   - >15% zeros → Zero-inflated model
   - Overdispersed (var/mean > 1.5) → NB over Poisson
3. Validate against polling data
4. Report effect sizes:
   - IRR for count models (with 95% CI)
   - Cohen's d for continuous
5. Apply Bonferroni/FDR correction if testing multiple terms
6. Save results to analysis/models/regression_results.json

⚠️ NEVER run OLS on raw search volume without justification.
"
```

**Phase 4: Synthesis (Day 3-4)**

```bash
# OpenClaw Coordinator
sessions_send(
    message="Synthesize all agent outputs into STUDY_REPORT.md",
    task="
1. Collect outputs from Claude Code, GLM, Kimi
2. Reconcile any disagreements
3. Write findings summary
4. Draft limitations section
5. Prepare visualizations for report
"
)
```

**Phase 5: Adversarial Review (Day 4)**

```bash
# OpenClaw - Spawn adversarial reviewers
sessions_spawn(
    agentId="reviewer-deepseek",
    task="Review STUDY_REPORT.md using Reviewer 2 protocol from CommDAAF v1.0"
)

sessions_spawn(
    agentId="reviewer-grok", 
    task="Review STUDY_REPORT.md using Reviewer 2 protocol from CommDAAF v1.0"
)
```

### 10.3 Model-Specific Instructions

**For ALL Models — CommDAAF Activation (REQUIRED):**
```
Before starting any task, confirm you have read and activated CommDAAF:
1. Read: skills/commdaaf/SKILL.md
2. Read: projects/comm-research-skill/agent-academy-study-protocol.md  
3. State: "CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."
4. Proceed with task following CommDAAF guardrails.
```

**For Claude Code:**
- Handle data collection and visualization
- Use pandas, matplotlib, seaborn
- Document all decisions in code comments (CommDAAF transparency)
- Save intermediate outputs
- Log all methodological choices

**For OpenCode GLM-4.7:**
- Run via `zai-coding-plan/glm-4.7`
- Use PTY mode for all calls
- Handle with smaller batches if stalling
- Focus on correlation/causality analysis
- Report confidence intervals (CommDAAF requirement)

**For OpenCode Kimi K2.5:**
- Run via `kimi-coding/k2p5`
- Use 25-item batches MAX (hard limit from AgentAcademy protocol)
- Focus on statistical modeling
- **Distribution diagnostics mandatory** (CommDAAF Section 7.1)
- **Never use OLS on count data** — use Negative Binomial

---

## 11. Expected Outputs

### 11.1 Data Files

```
data/
  trends/
    trends_2026-03-19.parquet
    trends_2026-03-26.parquet
    ...
  markets/
    markets_2026-03-19.json
    markets_2026-03-26.json
    ...
  polls/
    polls_2026-03-19.json
    ...
  processed/
    trends_normalized.parquet
    vibe_indices.csv
    merged_timeseries.parquet
```

### 11.2 Analysis Files

```
analysis/
  descriptives/
    state_issue_heatmap.png
    term_timeseries.png
    distribution_diagnostics.json
  correlations/
    trends_market_correlations.csv
    lag_analysis.csv
    granger_results.json
  models/
    regression_results.json
    validation_metrics.json
```

### 11.3 Reports

```
reports/
  STUDY_DESIGN.md
  STUDY_REPORT.md
  LIMITATIONS.md
  REVIEWER_2_DEEPSEEK.md
  REVIEWER_2_GROK.md
  EXECUTIVE_SUMMARY.md
```

### 11.4 Key Figures

1. **Heatmap:** Issue salience by state (battleground vs. control)
2. **Time series:** Vibe Index over time with major events annotated
3. **Scatter:** Vibe Index vs. prediction market odds
4. **Lag correlation plot:** Optimal lag identification
5. **State comparison:** Battleground vs. control trends

---

## 12. Quality Control

### 12.0 CommDAAF Activation Verification

**Before any work begins, verify each agent has:**

- [ ] Read `skills/commdaaf/SKILL.md`
- [ ] Read `projects/comm-research-skill/agent-academy-study-protocol.md`
- [ ] Confirmed activation with: "CommDAAF v1.0 activated. Validation tier: 🟢 EXPLORATORY."
- [ ] Acknowledged mandatory diagnostics requirement
- [ ] Acknowledged adversarial review requirement

**If any agent proceeds without CommDAAF acknowledgment → HALT and re-prompt.**

### 12.1 Pre-Collection Checklist

- [ ] CommDAAF activated by all agents (see 12.0)
- [ ] **Search terms validated for realism** (see Section 6):
  - [ ] No academic jargon in term list
  - [ ] 5-10 terms spot-checked on Google Trends for volume
  - [ ] Terms phrased as real users would type them
  - [ ] Zero-volume terms removed
- [ ] All API access verified (Google Trends, Polymarket, Kalshi)
- [ ] Scripts tested on small sample
- [ ] Storage structure created
- [ ] Rate limiting implemented
- [ ] Error handling robust

### 12.2 Data Quality Checks

- [ ] No missing states
- [ ] Date ranges complete
- [ ] No extreme outliers unexplained
- [ ] Cross-state normalization applied
- [ ] Term frequencies plausible

### 12.3 Analysis Checks

- [ ] Distribution diagnostics run before any regression
- [ ] Effect sizes reported (not just p-values)
- [ ] Multiple comparison correction if needed
- [ ] Residuals checked for OLS models
- [ ] Lag structure documented

### 12.4 Report Checks

- [ ] All claims supported by data
- [ ] Limitations honest and complete
- [ ] Adversarial review completed
- [ ] Reviewer concerns addressed

---

## 13. Limitations

### 13.1 Known Limitations

1. **Sample bias:** Google users ≠ all voters (skews younger, more educated)
2. **Platform changes:** Google Trends methodology may change
3. **Normalization issues:** Relative search volume, not absolute
4. **Confounders:** Major events can dominate signal
5. **Ecological fallacy:** State-level patterns ≠ individual behavior
6. **API reliability:** PyTrends is unofficial, may break
7. **Temporal granularity:** Weekly data may miss short-term dynamics

### 13.2 What This Study Cannot Do

- **Cannot predict election outcomes** — this is exploratory
- **Cannot establish causality** — correlation only
- **Cannot capture non-searchers** — offline opinion invisible
- **Cannot account for search intent** — same term, different meanings

### 13.3 Mitigation Strategies

| Limitation | Mitigation |
|------------|------------|
| Sample bias | Compare to known demographics; use as complement, not replacement |
| API changes | Version lock PyTrends; document methodology |
| Confounders | Event annotation; subperiod analysis |
| Ecological fallacy | Explicit caveat in all state-level claims |

---

## 14. File Structure

```
projects/vibe-polling/
├── PLAN.md                          # This document
├── STUDY_DESIGN.md                  # Formal study design
├── STUDY_REPORT.md                  # Final report
├── LIMITATIONS.md                   # Detailed limitations
├── README.md                        # Quick start guide
│
├── scripts/
│   ├── collect_trends.py            # Google Trends collection
│   ├── collect_markets.py           # Prediction market collection
│   ├── collect_polls.py             # Polling aggregator scraping
│   ├── process_data.py              # Data cleaning/normalization
│   ├── analyze_correlations.py      # Correlation analysis
│   ├── build_vibe_index.py          # Vibe Index construction
│   ├── validate_against_polls.py    # Validation analysis
│   └── generate_figures.py          # Visualization
│
├── data/
│   ├── raw/
│   │   ├── trends/                  # Raw Google Trends exports
│   │   ├── markets/                 # Raw market data
│   │   └── polls/                   # Raw polling data
│   ├── processed/
│   │   ├── trends_normalized.parquet
│   │   ├── vibe_indices.csv
│   │   └── merged_timeseries.parquet
│   └── reference/
│       ├── state_codes.json
│       └── term_categories.json
│
├── analysis/
│   ├── descriptives/
│   ├── correlations/
│   └── models/
│
├── outputs/
│   ├── figures/
│   │   ├── state_issue_heatmap.png
│   │   ├── vibe_index_timeseries.png
│   │   ├── trends_market_scatter.png
│   │   └── lag_correlation.png
│   └── tables/
│       ├── correlation_matrix.csv
│       └── regression_results.csv
│
├── reports/
│   ├── REVIEWER_2_DEEPSEEK.md
│   ├── REVIEWER_2_GROK.md
│   └── EXECUTIVE_SUMMARY.md
│
└── logs/
    ├── collection_log.txt
    └── analysis_log.txt
```

---

## 15. Timeline

| Day | Phase | Activities | Agent(s) |
|-----|-------|------------|----------|
| 1 | Collection | Run all collection scripts; verify data | Claude Code, GLM |
| 1-2 | Processing | Clean, normalize, merge data | Claude Code, Kimi |
| 2-3 | Analysis | Descriptives, correlations, modeling | All |
| 3-4 | Synthesis | Write report, generate figures | Coordinator |
| 4 | Review | Adversarial peer review | Reviewers |
| 5 | Finalize | Address reviewer comments; publish | Coordinator |

**Total estimated time:** 4-5 days active work

---

## Appendix A: Term-by-Term Justification

| Term | Why Realistic | Expected Signal |
|------|---------------|-----------------|
| `gas prices near me` | #1 local search for gas; action-oriented | Direct economic anxiety |
| `ICE raid` | News-driven; fear/concern | Immigration salience spike |
| `Iran war` | Active conflict; info-seeking | Foreign policy engagement |
| `AI taking jobs` | Direct fear query; not abstract | Automation anxiety |
| `how to vote` | Civic engagement intent | Electoral mobilization |
| `Epstein files` | Curiosity-driven; episodic | Trust/scandal interest |

---

## Appendix B: State-Specific Considerations

### Pennsylvania
- Fracking is local economic issue
- Philadelphia vs. rural divide
- Key House districts flipped in 2024

### Michigan
- Auto industry central to identity
- UAW strikes in 2025 still resonant
- Detroit economic anxiety

### Georgia
- 2020 election controversy legacy
- Ossoff defending Senate seat
- Atlanta suburban shift

### Arizona
- Border state; immigration salient
- Water scarcity emerging issue
- Phoenix heat/climate concern

---

## Appendix C: Potential Extensions

1. **Real-time dashboard:** Live Vibe Index tracking
2. **Comparison to X/Twitter sentiment:** Social media validation
3. **Local news integration:** Correlate with regional news cycles
4. **Demographic weighting:** Adjust for Google user demographics
5. **Spanish-language terms:** Capture Latino voter sentiment

---

*Document version: 1.0*  
*Created: 2026-03-19*  
*Framework: CommDAAF v1.0*
