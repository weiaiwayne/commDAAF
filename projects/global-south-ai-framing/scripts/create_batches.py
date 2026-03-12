#!/usr/bin/env python3
"""Create coding batches for South Africa and Brazil."""

import json
from pathlib import Path

DATA_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data")
BATCH_SIZE = 25

def create_sa_batches():
    """Create South Africa batches from valid AI meetings."""
    print("Creating South Africa batches...")
    
    # Load valid meetings
    with open(DATA_DIR / "south-africa/valid_ai_meetings.json") as f:
        meetings = json.load(f)
    
    print(f"  Valid meetings: {len(meetings)}")
    
    # Load transcripts
    transcripts_dir = DATA_DIR / "south-africa/transcripts"
    
    batches = []
    batch = []
    
    for meeting in meetings:
        meeting_id = meeting['meeting_id']
        transcript_file = transcripts_dir / f"{meeting_id}.txt"
        
        if not transcript_file.exists():
            print(f"  Warning: Missing transcript {meeting_id}")
            continue
        
        with open(transcript_file) as f:
            content = f.read()
        
        # Truncate if too long (keep first 15000 chars)
        if len(content) > 15000:
            content = content[:15000] + "\n\n[... TRUNCATED ...]"
        
        batch.append({
            'id': meeting_id,
            'title': meeting['title'],
            'date': meeting['date'],
            'url': meeting['url'],
            'content': content,
            'ai_density': meeting.get('density', 0),
            'classification': meeting.get('classification', 'UNKNOWN')
        })
        
        if len(batch) >= BATCH_SIZE:
            batches.append(batch)
            batch = []
    
    if batch:
        batches.append(batch)
    
    # Save batches
    output_dir = DATA_DIR / "south-africa/batches"
    output_dir.mkdir(exist_ok=True)
    
    for i, b in enumerate(batches, 1):
        with open(output_dir / f"batch_{i:02d}.json", 'w') as f:
            json.dump(b, f, indent=2)
        print(f"  Batch {i}: {len(b)} meetings")
    
    print(f"  Total batches: {len(batches)}")
    return batches

def create_brazil_batches():
    """Create Brazil batches from propositions."""
    print("\nCreating Brazil batches...")
    
    # Load propositions
    with open(DATA_DIR / "brazil/proposicoes_detailed.json") as f:
        props = json.load(f)
    
    print(f"  Total propositions: {len(props)}")
    
    batches = []
    batch = []
    
    for prop in props:
        # Create content from ementa, keywords, and tramitacoes
        content_parts = [
            f"Tipo: {prop.get('siglaTipo', '')} {prop.get('numero', '')}/{prop.get('ano', '')}",
            f"Ementa: {prop.get('ementa', '')}",
            f"Palavras-chave: {prop.get('keywords', '')}",
            f"Data: {prop.get('dataApresentacao', '')}",
            ""
        ]
        
        # Add tramitacoes
        trams = prop.get('tramitacoes', [])
        if trams:
            content_parts.append("Tramitações:")
            for t in trams[:3]:  # Last 3 actions
                content_parts.append(f"  - {t.get('dataHora', '')}: {t.get('descricaoTramitacao', '')}")
                if t.get('despacho'):
                    content_parts.append(f"    Despacho: {t['despacho'][:300]}...")
        
        content = "\n".join(content_parts)
        
        batch.append({
            'id': str(prop.get('id', '')),
            'title': f"{prop.get('siglaTipo', '')} {prop.get('numero', '')}/{prop.get('ano', '')}",
            'date': prop.get('dataApresentacao', ''),
            'url': prop.get('urlInteiroTeor', ''),
            'ementa': prop.get('ementa', ''),
            'keywords': prop.get('keywords', ''),
            'content': content
        })
        
        if len(batch) >= BATCH_SIZE:
            batches.append(batch)
            batch = []
    
    if batch:
        batches.append(batch)
    
    # Save batches
    output_dir = DATA_DIR / "brazil/batches"
    output_dir.mkdir(exist_ok=True)
    
    for i, b in enumerate(batches, 1):
        with open(output_dir / f"batch_{i:02d}.json", 'w') as f:
            json.dump(b, f, indent=2, ensure_ascii=False)
        print(f"  Batch {i}: {len(b)} propositions")
    
    print(f"  Total batches: {len(batches)}")
    return batches

def main():
    print("=" * 50)
    print("Creating Coding Batches for Global South AI Study")
    print("=" * 50)
    
    sa_batches = create_sa_batches()
    brazil_batches = create_brazil_batches()
    
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  South Africa: {sum(len(b) for b in sa_batches)} meetings in {len(sa_batches)} batches")
    print(f"  Brazil: {sum(len(b) for b in brazil_batches)} propositions in {len(brazil_batches)} batches")
    print("=" * 50)

if __name__ == "__main__":
    main()
