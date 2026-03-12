#!/usr/bin/env python3
"""Filter South Africa PMG transcripts for AI-focused content."""

import json
import re
from pathlib import Path
from collections import Counter

DATA_DIR = Path("/root/.openclaw/workspace/projects/global-south-ai-framing/data/south-africa")
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"

# AI-related terms (case-insensitive)
AI_TERMS = {
    'strong': [
        r'\bartificial\s+intelligence\b',
        r'\bAI\b',  # Standalone AI
        r'\bmachine\s+learning\b',
        r'\bdeep\s+learning\b',
        r'\bneural\s+network',
        r'\bChatGPT\b',
        r'\bGPT[-\s]?\d?\b',
        r'\bLLM\b',
        r'\blarge\s+language\s+model',
        r'\bgenerative\s+AI\b',
        r'\bAI\s+system',
        r'\bAI\s+technolog',
        r'\bAI\s+regulation',
        r'\bAI\s+governance',
        r'\bAI\s+ethics',
        r'\bAI\s+bias',
        r'\bAI\s+chip',
        r'\brobot\w*\b',
        r'\bautomation\b',
        r'\balgorithm\w*\b',
    ],
    'medium': [
        r'\b4th\s+industrial\s+revolution\b',
        r'\b4IR\b',
        r'\bfourth\s+industrial\s+revolution\b',
        r'\bdigital\s+transformation\b',
        r'\bdigitisation\b',
        r'\bdigitalization\b',
        r'\bdata\s+science\b',
        r'\bpredictive\s+analytics\b',
        r'\bcomputer\s+vision\b',
        r'\bfacial\s+recognition\b',
        r'\bnatural\s+language\s+processing\b',
        r'\bNLP\b',
        r'\bcyber[-\s]?security\b',
        r'\bsmart\s+cit(?:y|ies)\b',
    ]
}

def count_ai_terms(text):
    """Count AI-related terms in text."""
    text_lower = text.lower()
    counts = {'strong': 0, 'medium': 0, 'terms': Counter()}
    
    for category, patterns in AI_TERMS.items():
        for pattern in patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                counts[category] += len(matches)
                # Normalize the term for counting
                term = pattern.replace(r'\b', '').replace(r'\s+', ' ')[:20]
                counts['terms'][term] += len(matches)
    
    return counts

def calculate_ai_density(text, counts):
    """Calculate AI term density per 1000 words."""
    word_count = len(text.split())
    if word_count == 0:
        return 0
    total_ai_terms = counts['strong'] + counts['medium']
    return (total_ai_terms / word_count) * 1000

def classify_meeting(counts, density):
    """Classify meeting as HIGH, MEDIUM, or LOW AI relevance."""
    # HIGH: 20+ strong terms OR density >= 5 per 1000 words
    if counts['strong'] >= 20 or density >= 5:
        return 'HIGH'
    # MEDIUM: 10+ strong terms OR 5+ strong + some medium
    elif counts['strong'] >= 10 or (counts['strong'] >= 5 and counts['medium'] >= 5):
        return 'MEDIUM'
    # LOW: minimal AI content
    else:
        return 'LOW'

def analyze_transcripts():
    """Analyze all transcripts for AI content."""
    results = []
    
    # Load meeting index
    with open(DATA_DIR / "meetings_index.json") as f:
        meetings_index = {m['meeting_id']: m for m in json.load(f)}
    
    for transcript_file in sorted(TRANSCRIPTS_DIR.glob("*.txt")):
        meeting_id = transcript_file.stem
        
        with open(transcript_file) as f:
            text = f.read()
        
        counts = count_ai_terms(text)
        density = calculate_ai_density(text, counts)
        classification = classify_meeting(counts, density)
        
        # Get metadata from index
        metadata = meetings_index.get(meeting_id, {})
        
        results.append({
            'meeting_id': meeting_id,
            'title': metadata.get('title', ''),
            'date': metadata.get('date', ''),
            'url': metadata.get('url', ''),
            'char_count': len(text),
            'word_count': len(text.split()),
            'strong_terms': counts['strong'],
            'medium_terms': counts['medium'],
            'density': round(density, 2),
            'classification': classification,
            'top_terms': dict(counts['terms'].most_common(5))
        })
    
    return results

def main():
    print("Analyzing South Africa PMG transcripts for AI content...")
    print("=" * 60)
    
    results = analyze_transcripts()
    
    # Sort by classification and density
    results.sort(key=lambda x: (
        {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}[x['classification']],
        -x['density']
    ))
    
    # Count by classification
    counts = Counter(r['classification'] for r in results)
    
    print(f"\nClassification Distribution:")
    print(f"  HIGH:   {counts['HIGH']} ({counts['HIGH']/len(results)*100:.1f}%)")
    print(f"  MEDIUM: {counts['MEDIUM']} ({counts['MEDIUM']/len(results)*100:.1f}%)")
    print(f"  LOW:    {counts['LOW']} ({counts['LOW']/len(results)*100:.1f}%)")
    print(f"  Total:  {len(results)}")
    
    # Save full results
    with open(DATA_DIR / "ai_analysis.json", 'w') as f:
        json.dump(results, f, indent=2)
    
    # Create filtered list (HIGH + MEDIUM)
    valid_meetings = [r for r in results if r['classification'] in ['HIGH', 'MEDIUM']]
    
    with open(DATA_DIR / "valid_ai_meetings.json", 'w') as f:
        json.dump(valid_meetings, f, indent=2)
    
    print(f"\nValid AI-focused meetings: {len(valid_meetings)}")
    print(f"\nSaved to:")
    print(f"  {DATA_DIR / 'ai_analysis.json'}")
    print(f"  {DATA_DIR / 'valid_ai_meetings.json'}")
    
    # Print top 15 HIGH meetings
    print(f"\n{'=' * 60}")
    print("Top 15 HIGH AI relevance meetings:")
    print("-" * 60)
    for r in results[:15]:
        if r['classification'] == 'HIGH':
            print(f"  [{r['meeting_id']}] {r['title'][:60]}...")
            print(f"    Date: {r['date']} | Strong: {r['strong_terms']} | Density: {r['density']}")
    
    return results

if __name__ == "__main__":
    main()
