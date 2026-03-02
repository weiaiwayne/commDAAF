# GDELT Data Collection Skill

Collect and analyze global event data via GDELT.

## Overview

GDELT (Global Database of Events, Language, and Tone) monitors:
- News media worldwide (broadcast, print, web)
- 100+ languages
- Events extracted via CAMEO coding
- Sentiment, themes, locations, actors
- Updated every 15 minutes

## Data Products

| Product | Description | Access |
|---------|-------------|--------|
| **Event Database** | Structured events (who did what to whom) | BigQuery, Files |
| **GKG** | Global Knowledge Graph (themes, emotions, locations) | BigQuery, Files |
| **DOC API** | Full-text document search | REST API |
| **GEO API** | Geographic visualization | REST API |
| **TV API** | Television news monitoring | REST API |

## Access Methods

### 1. BigQuery (Recommended for large queries)
```bash
# Requires Google Cloud account
pip install google-cloud-bigquery pandas-gbq
```

```python
from google.cloud import bigquery
import pandas as pd

def query_gdelt_events(query_sql):
    """Run query on GDELT BigQuery tables."""
    client = bigquery.Client()
    
    # GDELT tables are public
    return client.query(query_sql).to_dataframe()

# Example: Events involving Russia in 2024
sql = """
SELECT 
    SQLDATE, Actor1Name, Actor2Name, 
    EventCode, GoldsteinScale, NumMentions, AvgTone,
    ActionGeo_FullName, SOURCEURL
FROM `gdelt-bq.gdeltv2.events`
WHERE SQLDATE >= 20240101 
    AND (Actor1CountryCode = 'RUS' OR Actor2CountryCode = 'RUS')
    AND NumMentions >= 5
ORDER BY NumMentions DESC
LIMIT 10000
"""

df = query_gdelt_events(sql)
```

### 2. Direct File Download (Free, no account)
```python
import requests
import zipfile
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta

def download_gdelt_events(date):
    """Download GDELT events for a specific date."""
    # Format: YYYYMMDD
    date_str = date.strftime('%Y%m%d')
    
    url = f"http://data.gdeltproject.org/events/{date_str}.export.CSV.zip"
    
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    # Unzip and read
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        csv_name = z.namelist()[0]
        with z.open(csv_name) as f:
            # GDELT has no header row
            columns = get_gdelt_columns()
            df = pd.read_csv(f, sep='\t', header=None, names=columns)
    
    return df

def get_gdelt_columns():
    """GDELT event table column names."""
    return [
        'GlobalEventID', 'Day', 'MonthYear', 'Year', 'FractionDate',
        'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',
        'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',
        'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code',
        'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
        'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
        'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code',
        'IsRootEvent', 'EventCode', 'EventBaseCode', 'EventRootCode',
        'QuadClass', 'GoldsteinScale', 'NumMentions', 'NumSources',
        'NumArticles', 'AvgTone',
        'Actor1Geo_Type', 'Actor1Geo_FullName', 'Actor1Geo_CountryCode',
        'Actor1Geo_ADM1Code', 'Actor1Geo_ADM2Code', 'Actor1Geo_Lat', 'Actor1Geo_Long',
        'Actor1Geo_FeatureID',
        'Actor2Geo_Type', 'Actor2Geo_FullName', 'Actor2Geo_CountryCode',
        'Actor2Geo_ADM1Code', 'Actor2Geo_ADM2Code', 'Actor2Geo_Lat', 'Actor2Geo_Long',
        'Actor2Geo_FeatureID',
        'ActionGeo_Type', 'ActionGeo_FullName', 'ActionGeo_CountryCode',
        'ActionGeo_ADM1Code', 'ActionGeo_ADM2Code', 'ActionGeo_Lat', 'ActionGeo_Long',
        'ActionGeo_FeatureID',
        'DATEADDED', 'SOURCEURL'
    ]
```

### 3. DOC API (Full-text search)
```python
def search_gdelt_docs(query, mode='artlist', maxrecords=250,
                      startdatetime=None, enddatetime=None,
                      sourcelang='english'):
    """
    Search GDELT document database.
    
    Args:
        query: Search terms
        mode: 'artlist' (articles), 'timelinevol' (volume over time), etc.
        maxrecords: Max results (up to 250)
        startdatetime: Format YYYYMMDDHHMMSS
        enddatetime: Format YYYYMMDDHHMMSS
        sourcelang: Language filter
    """
    base_url = "https://api.gdeltproject.org/api/v2/doc/doc"
    
    params = {
        'query': query,
        'mode': mode,
        'maxrecords': maxrecords,
        'format': 'json'
    }
    
    if startdatetime:
        params['startdatetime'] = startdatetime
    if enddatetime:
        params['enddatetime'] = enddatetime
    if sourcelang:
        params['sourcelang'] = sourcelang
    
    response = requests.get(base_url, params=params)
    return response.json()

# Example: Search for climate change articles
results = search_gdelt_docs(
    query='climate change policy',
    startdatetime='20240101000000',
    enddatetime='20240131235959',
    maxrecords=250
)
```

### 4. GKG (Global Knowledge Graph)
```python
def query_gkg(sql):
    """Query GDELT GKG via BigQuery."""
    from google.cloud import bigquery
    client = bigquery.Client()
    return client.query(sql).to_dataframe()

# Example: Themes and sentiment about COVID
sql = """
SELECT 
    DATE, DocumentIdentifier, V2Themes, V2Tone,
    V2Locations, V2Persons, V2Organizations
FROM `gdelt-bq.gdeltv2.gkg`
WHERE DATE >= 20240101
    AND V2Themes LIKE '%HEALTH_PANDEMIC%'
LIMIT 1000
"""
```

## CAMEO Event Codes

GDELT uses CAMEO codes for event types:

| Code Range | Category |
|------------|----------|
| 01 | Make public statement |
| 02 | Appeal |
| 03 | Express intent to cooperate |
| 04 | Consult |
| 05 | Engage in diplomatic cooperation |
| 06 | Engage in material cooperation |
| 07 | Provide aid |
| 08 | Yield |
| 09 | Investigate |
| 10 | Demand |
| 11 | Disapprove |
| 12 | Reject |
| 13 | Threaten |
| 14 | Protest |
| 15 | Exhibit force posture |
| 16 | Reduce relations |
| 17 | Coerce |
| 18 | Assault |
| 19 | Fight |
| 20 | Use unconventional mass violence |

## Goldstein Scale

Measures cooperation/conflict (-10 to +10):
- +10: Extreme cooperation
- 0: Neutral
- -10: Extreme conflict

```python
def filter_conflict_events(df, threshold=-5):
    """Filter to high-conflict events."""
    return df[df['GoldsteinScale'] <= threshold]

def filter_cooperation_events(df, threshold=5):
    """Filter to high-cooperation events."""
    return df[df['GoldsteinScale'] >= threshold]
```

## Research Applications

### Conflict Studies
- Track conflict escalation/de-escalation
- Identify key actors in conflicts
- Geographic spread of violence

### Protest Research
- Monitor protest events globally
- Track government responses
- Identify mobilization patterns

### Media Studies
- News coverage patterns
- Geographic attention distribution
- Tone analysis by source

### Crisis Response
- Real-time event monitoring
- Early warning systems
- Response coordination

## Data Schema

### Event Object
```python
{
    'GlobalEventID': int,
    'Day': int,  # YYYYMMDD
    'Actor1Name': str,
    'Actor1CountryCode': str,
    'Actor2Name': str,
    'Actor2CountryCode': str,
    'EventCode': str,  # CAMEO code
    'GoldsteinScale': float,  # -10 to +10
    'NumMentions': int,
    'NumSources': int,
    'AvgTone': float,  # -100 to +100
    'ActionGeo_FullName': str,
    'ActionGeo_Lat': float,
    'ActionGeo_Long': float,
    'SOURCEURL': str
}
```

## Cost Considerations

| Method | Cost |
|--------|------|
| File download | Free |
| DOC/GEO API | Free |
| BigQuery | ~$5/TB scanned (free tier available) |

## Ethical Considerations

- Events are machine-coded (may have errors)
- Coverage varies by region/language
- Goldstein scores are approximate
- Source bias affects event detection
- Real-time data may be incomplete

## Workflow Integration

```yaml
# Spawn GDELT collection agent
sessions_spawn:
  task: "Monitor GDELT events in {region} for {event_type} over {date_range}"
  agentId: comm-research-collector
  model: google/gemini-2.0-flash
```

## Key Citations

- Leetaru, K., & Schrodt, P. A. (2013). GDELT: Global data on events, location, and tone, 1979–2012. *ISA Annual Convention*.
- GDELT documentation: [gdeltproject.org](https://www.gdeltproject.org/)

---
*Part of Communication Research Skill for OpenClaw*
