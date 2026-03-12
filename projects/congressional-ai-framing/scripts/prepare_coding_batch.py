#!/usr/bin/env python3
"""
Prepare congressional hearing transcripts for CommDAAF coding.
Extracts opening statements and key testimony sections.
"""

import json
import re
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup
import html

def clean_text(text: str) -> str:
    """Clean and normalize transcript text."""
    # Remove HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove page numbers
    text = re.sub(r'\[\[Page \d+\]\]', '', text)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    return text.strip()


def extract_content(html_content: str) -> dict:
    """Extract structured content from hearing HTML."""
    
    # For GPO hearings, content is in <pre> tags
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get title
    title_tag = soup.find('title')
    title = title_tag.get_text().strip() if title_tag else "Unknown"
    title = re.sub(r'^- ', '', title)
    
    # Get the main text content
    pre_tag = soup.find('pre')
    if pre_tag:
        text = pre_tag.get_text()
    else:
        text = soup.get_text()
    
    # Extract key sections
    sections = {
        'title': title,
        'full_text': text,
        'opening_statements': [],
        'witness_testimony': [],
        'metadata': {}
    }
    
    # Try to find opening statements
    opening_match = re.search(
        r'OPENING STATEMENT[S]?\s+OF\s+([^\n]+)(.*?)(?=OPENING STATEMENT|WITNESS|PANEL|$)',
        text, 
        re.IGNORECASE | re.DOTALL
    )
    if opening_match:
        sections['opening_statements'].append({
            'speaker': opening_match.group(1).strip(),
            'text': clean_text(opening_match.group(2)[:3000])  # Limit length
        })
    
    # Try to find witness testimony
    testimony_matches = re.finditer(
        r'(?:STATEMENT OF|TESTIMONY OF)\s+([^\n]+)(.*?)(?=STATEMENT OF|TESTIMONY OF|PANEL|QUESTIONS|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )
    for match in testimony_matches:
        sections['witness_testimony'].append({
            'speaker': match.group(1).strip(),
            'text': clean_text(match.group(2)[:3000])
        })
    
    # Extract metadata from text
    congress_match = re.search(r'(\d+)(?:TH|ST|ND|RD)\s+CONGRESS', text, re.IGNORECASE)
    if congress_match:
        sections['metadata']['congress'] = int(congress_match.group(1))
    
    chamber_match = re.search(r'(HOUSE|SENATE)', text, re.IGNORECASE)
    if chamber_match:
        sections['metadata']['chamber'] = chamber_match.group(1).upper()
    
    committee_match = re.search(r'COMMITTEE ON[^\n]+', text, re.IGNORECASE)
    if committee_match:
        sections['metadata']['committee'] = committee_match.group(0).strip()
    
    return sections


def create_coding_excerpt(hearing_id: str, content: dict, max_chars: int = 4000) -> dict:
    """Create a coding excerpt from hearing content."""
    
    # Prioritize opening statements, then witness testimony
    excerpt_parts = []
    
    # Add title
    excerpt_parts.append(f"HEARING: {content['title']}\n")
    
    # Add opening statements (truncated)
    for stmt in content['opening_statements'][:2]:
        text = stmt['text'][:1500] if len(stmt['text']) > 1500 else stmt['text']
        excerpt_parts.append(f"\n[OPENING - {stmt['speaker']}]\n{text}")
    
    # Add witness testimony (truncated)
    for testimony in content['witness_testimony'][:2]:
        text = testimony['text'][:1000] if len(testimony['text']) > 1000 else testimony['text']
        excerpt_parts.append(f"\n[WITNESS - {testimony['speaker']}]\n{text}")
    
    # If no structured content found, use raw text
    if len(excerpt_parts) == 1:
        # Just use first portion of full text
        raw_text = clean_text(content['full_text'])
        # Skip the header boilerplate
        start_idx = raw_text.find('The Committee met') or raw_text.find('The Subcommittee met') or 0
        if start_idx > 0:
            raw_text = raw_text[start_idx:]
        excerpt_parts.append(raw_text[:max_chars])
    
    excerpt = '\n'.join(excerpt_parts)
    
    # Truncate to max length
    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars] + "..."
    
    return {
        'id': hearing_id,
        'title': content['title'],
        'congress': content['metadata'].get('congress'),
        'chamber': content['metadata'].get('chamber'),
        'committee': content['metadata'].get('committee'),
        'excerpt': excerpt,
        'excerpt_length': len(excerpt)
    }


def prepare_batch(
    transcript_dir: Path,
    output_path: Path,
    n: int = 25,
    congress_filter: Optional[list] = None
) -> list:
    """Prepare a batch of hearings for coding."""
    
    transcripts = list(transcript_dir.glob("CHRG-*.html")) + list(transcript_dir.glob("CHRG-*.txt"))
    
    if congress_filter:
        filtered = []
        for t in transcripts:
            for c in congress_filter:
                if f"CHRG-{c}" in t.name:
                    filtered.append(t)
                    break
        transcripts = filtered
    
    # Sort by name (roughly by date for same congress)
    transcripts = sorted(transcripts, reverse=True)
    
    # Sample
    import random
    random.seed(42)
    if len(transcripts) > n:
        transcripts = random.sample(transcripts, n)
    
    batch = []
    for transcript_path in transcripts:
        try:
            with open(transcript_path, 'r', encoding='utf-8', errors='replace') as f:
                html_content = f.read()
            
            hearing_id = transcript_path.stem
            content = extract_content(html_content)
            excerpt = create_coding_excerpt(hearing_id, content)
            batch.append(excerpt)
            
        except Exception as e:
            print(f"Error processing {transcript_path}: {e}")
    
    # Save batch
    with open(output_path, 'w') as f:
        json.dump(batch, f, indent=2)
    
    print(f"Prepared {len(batch)} hearings for coding")
    return batch


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Prepare hearing batch for coding")
    parser.add_argument("-n", "--num", type=int, default=25, help="Number of hearings")
    parser.add_argument("-c", "--congress", type=str, help="Congress numbers (comma-separated)")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output JSON path")
    parser.add_argument("-t", "--transcripts", type=str, required=True, help="Transcript directory")
    
    args = parser.parse_args()
    
    congress_filter = None
    if args.congress:
        congress_filter = [c.strip() for c in args.congress.split(',')]
    
    prepare_batch(
        transcript_dir=Path(args.transcripts),
        output_path=Path(args.output),
        n=args.num,
        congress_filter=congress_filter
    )
