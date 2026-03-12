#!/usr/bin/env python3
"""Scrape Brazil Câmara dos Deputados for AI-related speeches and debates."""

import requests
import json
import time
from pathlib import Path
from datetime import datetime

BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
OUTPUT_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data/brazil")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# AI-related keywords in Portuguese
AI_KEYWORDS = [
    "inteligência artificial",
    "inteligencia artificial", 
    "IA",
    "machine learning",
    "aprendizado de máquina",
    "aprendizado de maquina",
    "deep learning",
    "aprendizado profundo",
    "ChatGPT",
    "robô",
    "robo",
    "automação",
    "automacao",
    "algoritmo",
    "transformação digital",
    "transformacao digital",
]

def search_proposicoes(keyword, page=1, items=100):
    """Search for bills/propositions mentioning AI."""
    url = f"{BASE_URL}/proposicoes"
    params = {
        'keywords': keyword,
        'ordenarPor': 'id',
        'ordem': 'DESC',
        'pagina': page,
        'itens': items
    }
    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    return resp.json()

def search_discursos(keyword, data_inicio="2020-01-01", data_fim="2026-12-31"):
    """Search for speeches mentioning AI."""
    # The API doesn't have a direct keyword search for speeches
    # We need to get speeches and filter by content
    # Alternative: search via the website or use proposicoes
    pass

def get_proposicao_details(prop_id):
    """Get full details of a proposition."""
    url = f"{BASE_URL}/proposicoes/{prop_id}"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.json()

def get_proposicao_tramitacoes(prop_id):
    """Get processing history of a proposition."""
    url = f"{BASE_URL}/proposicoes/{prop_id}/tramitacoes"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.json()

def search_eventos(data_inicio="2020-01-01", data_fim="2026-12-31"):
    """Search for committee events/hearings."""
    url = f"{BASE_URL}/eventos"
    params = {
        'dataInicio': data_inicio,
        'dataFim': data_fim,
        'ordenarPor': 'dataHoraInicio',
        'ordem': 'DESC',
        'itens': 100
    }
    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    return resp.json()

def main():
    print("=" * 60)
    print("Brazil Câmara dos Deputados AI Data Scraper")
    print("=" * 60)
    
    all_proposicoes = []
    seen_ids = set()
    
    # Search for AI-related propositions
    print("\n[1/3] Searching for AI-related propositions...")
    for keyword in AI_KEYWORDS[:5]:  # Start with main keywords
        print(f"  Searching: '{keyword}'...")
        try:
            result = search_proposicoes(keyword, page=1, items=100)
            props = result.get('dados', [])
            
            new_count = 0
            for p in props:
                if p['id'] not in seen_ids:
                    seen_ids.add(p['id'])
                    all_proposicoes.append(p)
                    new_count += 1
            
            print(f"    Found {len(props)} results, {new_count} new (total: {len(all_proposicoes)})")
            time.sleep(0.5)
            
        except Exception as e:
            print(f"    Error: {e}")
    
    print(f"\nTotal unique propositions: {len(all_proposicoes)}")
    
    # Save propositions index
    with open(OUTPUT_DIR / "proposicoes_index.json", 'w') as f:
        json.dump(all_proposicoes, f, indent=2, ensure_ascii=False)
    
    # Get detailed info for each proposition
    print("\n[2/3] Fetching proposition details...")
    detailed_props = []
    
    for i, prop in enumerate(all_proposicoes[:150]):  # Limit to 150
        prop_id = prop['id']
        print(f"  [{i+1}/{min(150, len(all_proposicoes))}] Fetching {prop_id}...", end=" ", flush=True)
        
        try:
            details = get_proposicao_details(prop_id)
            tramitacoes = get_proposicao_tramitacoes(prop_id)
            
            detailed_props.append({
                'id': prop_id,
                'siglaTipo': prop.get('siglaTipo', ''),
                'numero': prop.get('numero', ''),
                'ano': prop.get('ano', ''),
                'ementa': details.get('dados', {}).get('ementa', ''),
                'keywords': details.get('dados', {}).get('keywords', ''),
                'dataApresentacao': details.get('dados', {}).get('dataApresentacao', ''),
                'urlInteiroTeor': details.get('dados', {}).get('urlInteiroTeor', ''),
                'tramitacoes': tramitacoes.get('dados', [])[:5],  # Last 5 actions
                'uri': prop.get('uri', '')
            })
            print("OK")
            time.sleep(0.3)
            
        except Exception as e:
            print(f"ERROR: {e}")
    
    # Save detailed propositions
    with open(OUTPUT_DIR / "proposicoes_detailed.json", 'w') as f:
        json.dump(detailed_props, f, indent=2, ensure_ascii=False)
    
    # Also try to get recent events mentioning AI
    print("\n[3/3] Searching for recent committee events...")
    try:
        events = search_eventos(data_inicio="2023-01-01")
        all_events = events.get('dados', [])
        
        # Filter for AI-related events by description
        ai_events = []
        for event in all_events:
            desc = (event.get('descricao', '') + ' ' + event.get('descricaoTipo', '')).lower()
            if any(kw.lower() in desc for kw in ['inteligência artificial', 'inteligencia artificial', 'ia', 'tecnologia', 'digital', 'inovação']):
                ai_events.append(event)
        
        print(f"  Total events: {len(all_events)}, AI-related: {len(ai_events)}")
        
        with open(OUTPUT_DIR / "eventos_ai.json", 'w') as f:
            json.dump(ai_events, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"  Error fetching events: {e}")
    
    print(f"\n{'=' * 60}")
    print("Brazil data collection complete!")
    print(f"  Propositions indexed: {len(all_proposicoes)}")
    print(f"  Detailed propositions: {len(detailed_props)}")
    print(f"  Output directory: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
