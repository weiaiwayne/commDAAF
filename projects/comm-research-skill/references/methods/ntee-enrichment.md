# NTEE Enrichment for Nonprofit Research

**Source:** Nonprofit Mission Framing Study (Mar 2026)  
**Problem Solved:** Adding subsector controls to nonprofit analyses using free APIs

---

## Overview

The National Taxonomy of Exempt Entities (NTEE) is the standard classification for U.S. nonprofits. When analyzing nonprofits, **subsector controls are essential** because organizational type strongly predicts language, behavior, and outcomes.

## Primary Source: ProPublica Nonprofit Explorer

**API:** `https://projects.propublica.org/nonprofits/api/v2/`

### Lookup by EIN
```python
import requests

def get_ntee_from_propublica(ein: str) -> dict:
    """Fetch NTEE code and org info from ProPublica."""
    url = f"https://projects.propublica.org/nonprofits/api/v2/organizations/{ein}.json"
    
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            org = data.get("organization", {})
            return {
                "ein": ein,
                "name": org.get("name"),
                "ntee_code": org.get("ntee_code"),
                "subsection": org.get("subsection_code"),
                "state": org.get("state"),
                "city": org.get("city"),
                "total_revenue": org.get("total_revenue"),
                "source": "propublica",
            }
    except Exception as e:
        pass
    
    return {"ein": ein, "ntee_code": None, "source": "propublica_miss"}
```

### Search by Name
```python
def search_propublica(query: str, state: str = None) -> list:
    """Search for nonprofits by name."""
    url = "https://projects.propublica.org/nonprofits/api/v2/search.json"
    params = {"q": query}
    if state:
        params["state[id]"] = state
    
    resp = requests.get(url, params=params, timeout=10)
    if resp.status_code == 200:
        return resp.json().get("organizations", [])
    return []
```

## NTEE Code Structure

NTEE codes follow the pattern: `[Letter][2 digits]` (e.g., `B20` = Elementary/Secondary Education)

### Major Categories
| Letter | Category |
|--------|----------|
| A | Arts, Culture, Humanities |
| B | Education |
| C | Environment |
| D | Animal-Related |
| E | Health Care |
| F | Mental Health |
| G | Disease/Disorders |
| H | Medical Research |
| I | Crime/Legal |
| J | Employment |
| K | Food/Agriculture |
| L | Housing/Shelter |
| M | Public Safety |
| N | Recreation/Sports |
| O | Youth Development |
| P | Human Services |
| Q | International |
| R | Civil Rights |
| S | Community Improvement |
| T | Philanthropy/Voluntarism |
| U | Science/Technology |
| V | Social Science |
| W | Public Policy |
| X | Religion |
| Y | Mutual/Membership Benefit |
| Z | Unknown |

## Fallback: IRS Subsection Codes

When ProPublica doesn't have NTEE, use IRS subsection as proxy:

```python
SUBSECTION_TO_CATEGORY = {
    3: "Mutual_Benefit",      # 501(c)(3) but member-focused
    4: "Mutual_Benefit",      # Civic leagues, social welfare
    5: "Mutual_Benefit",      # Labor, agricultural orgs
    6: "Mutual_Benefit",      # Business leagues
    7: "Recreation",          # Social/recreation clubs
    8: "Mutual_Benefit",      # Fraternal beneficiary societies
    9: "Mutual_Benefit",      # Fraternal associations
    10: "Mutual_Benefit",     # Domestic fraternal societies
    13: "Religion",           # Cemetery companies
    14: "Mutual_Benefit",     # Credit unions
    19: "Mutual_Benefit",     # Veterans organizations
}

def fallback_to_subsection(subsection: int) -> str:
    return SUBSECTION_TO_CATEGORY.get(subsection, "Unknown")
```

## Full Enrichment Pipeline

```python
def enrich_with_ntee(missions: list) -> list:
    """Add NTEE codes to mission list."""
    enriched = []
    
    for m in missions:
        ein = m.get("ein", "").replace("-", "")
        
        # Try ProPublica first
        pp = get_ntee_from_propublica(ein)
        
        if pp.get("ntee_code"):
            m["ntee_code"] = pp["ntee_code"]
            m["ntee_major"] = NTEE_LETTER_TO_CATEGORY.get(pp["ntee_code"][0], "Unknown")
            m["ntee_source"] = "propublica"
        elif pp.get("subsection"):
            m["ntee_code"] = None
            m["ntee_major"] = fallback_to_subsection(pp["subsection"])
            m["ntee_source"] = "subsection_fallback"
        else:
            m["ntee_code"] = None
            m["ntee_major"] = "Unknown"
            m["ntee_source"] = "none"
        
        enriched.append(m)
    
    return enriched
```

## Coverage Expectations

From the Nonprofit Framing study (N=465):

| Source | Coverage |
|--------|----------|
| ProPublica NTEE | 52% (241/465) |
| Subsection fallback | 45% (211/465) |
| No data | 3% (13/465) |
| **Total classified** | **97%** |

## Using NTEE in Regression

```python
import pandas as pd
import statsmodels.api as sm

# Create dummies (reference = Human_Services)
ntee_dummies = pd.get_dummies(df["ntee_major"], prefix="ntee", drop_first=False)
ntee_dummies = ntee_dummies.drop("ntee_Human_Services", axis=1)  # Reference

# Filter low-n categories
min_n = 10
valid_cols = [c for c in ntee_dummies.columns if ntee_dummies[c].sum() >= min_n]
ntee_dummies = ntee_dummies[valid_cols]

# Add to model
X = pd.concat([df[["log_revenue"]], ntee_dummies], axis=1)
X = sm.add_constant(X)
y = df["technocratic_any"]

model = sm.Logit(y, X).fit()
print(model.summary())
```

## Rate Limiting

ProPublica has no documented rate limits, but be respectful:

```python
import time

def batch_enrich(eins: list, delay: float = 0.5) -> list:
    """Enrich with polite delays."""
    results = []
    for i, ein in enumerate(eins):
        results.append(get_ntee_from_propublica(ein))
        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(eins)}...")
        time.sleep(delay)
    return results
```

## Alternative Sources

| Source | Coverage | API? | Notes |
|--------|----------|------|-------|
| ProPublica | Good | Yes | Free, no key needed |
| IRS BMF | Complete | No | Bulk download only |
| GuideStar/Candid | Best | Yes | Requires paid subscription |
| NCCS | Good | Yes | Academic access |

## Citation

```
Intuitionist × AgentAcademy. (2026). Technocratic Language in U.S. 
Nonprofit Mission Statements. AgentAcademy.
https://agentacademy.lampbotics.com/nonprofit-framing/
```
