#!/usr/bin/env python3
"""Code a single batch using Claude via the CommDAAF prompt."""

import json
import sys
from pathlib import Path

def load_prompt():
    """Load the CommDAAF coding prompt."""
    prompt_path = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/prompts/commdaaf_global_south.md")
    return prompt_path.read_text()

def prepare_batch_content(batch_data, country):
    """Prepare batch content for coding."""
    docs = []
    for item in batch_data:
        doc = {
            'id': item.get('id', ''),
            'title': item.get('title', ''),
            'country': country,
        }
        
        # Add content based on country format
        if country == 'ZA':
            doc['content'] = item.get('content', '')[:8000]  # Truncate for context
        elif country == 'BR':
            doc['content'] = f"Ementa: {item.get('ementa', '')}\nPalavras-chave: {item.get('keywords', '')}"
        elif country == 'IN':
            doc['content'] = f"Summary: {item.get('summary', '')}\nKey Provisions: {', '.join(item.get('key_provisions', []))}"
        
        docs.append(doc)
    
    return docs

def main():
    if len(sys.argv) < 3:
        print("Usage: code_batch.py <country_code> <batch_file>")
        print("  country_code: ZA (South Africa), BR (Brazil), IN (India)")
        sys.exit(1)
    
    country = sys.argv[1].upper()
    batch_file = Path(sys.argv[2])
    
    if not batch_file.exists():
        print(f"Error: Batch file not found: {batch_file}")
        sys.exit(1)
    
    # Load batch
    with open(batch_file) as f:
        batch_data = json.load(f)
    
    # Prepare content
    docs = prepare_batch_content(batch_data, country)
    
    # Load prompt
    prompt = load_prompt()
    
    # Output the prompt + data for coding
    print("=== COMMDAAF CODING REQUEST ===")
    print(f"Country: {country}")
    print(f"Batch: {batch_file.name}")
    print(f"Documents: {len(docs)}")
    print()
    print("=== PROMPT ===")
    print(prompt)
    print()
    print("=== DOCUMENTS TO CODE ===")
    print(json.dumps(docs, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
