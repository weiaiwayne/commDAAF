#!/usr/bin/env python3
"""
Filter full transcripts to identify hearings primarily about AI.
More accurate than filtering excerpts.
"""

import json
import re
from pathlib import Path
from collections import Counter

# Strong AI indicators (high weight)
STRONG_AI_TERMS = [
    r'artificial intelligence',
    r'machine learning',
    r'deep learning',
    r'neural network',
    r'large language model',
    r'\bllm\b',
    r'\bllms\b',
    r'chatgpt',
    r'gpt-\d',
    r'openai',
    r'deepseek',
    r'anthropic',
    r'claude\s+ai',
    r'generative ai',
    r'gen\s*ai',
    r'ai\s+model',
    r'ai\s+system',
    r'ai\s+safety',
    r'ai\s+risk',
    r'ai\s+regulation',
    r'ai\s+governance',
    r'ai\s+policy',
    r'ai\s+act',
    r'algorithmic',
    r'deepfake',
    r'facial recognition',
    r'computer vision',
    r'natural language processing',
    r'autonomous\s+system',
    r'autonomous\s+vehicle',
    r'autonomous\s+weapon',
]

# Moderate AI indicators (medium weight)  
MODERATE_AI_TERMS = [
    r'\bai\b(?!\s*port)',  # AI but not "airport"
    r'algorithm',
    r'automat',
    r'chatbot',
    r'robot',
    r'intelligent\s+system',
    r'predictive\s+model',
    r'data\s+model',
]

def count_matches(text: str, patterns: list) -> int:
    """Count total matches for patterns in text."""
    text_lower = text.lower()
    total = 0
    for pattern in patterns:
        matches = re.findall(pattern, text_lower)
        total += len(matches)
    return total


def analyze_transcript(transcript_path: Path) -> dict:
    """Analyze a transcript file for AI relevance."""
    
    with open(transcript_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Get title from content
    title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Unknown"
    title = re.sub(r'^-\s*', '', title)
    
    # Count AI mentions
    text_only = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
    
    strong_count = count_matches(text_only, STRONG_AI_TERMS)
    moderate_count = count_matches(text_only, MODERATE_AI_TERMS)
    
    # Calculate word count for density
    words = len(text_only.split())
    
    # Calculate relevance score
    # Strong terms worth 2 points, moderate worth 1
    weighted_score = (strong_count * 2) + moderate_count
    
    # Normalize by document length (per 1000 words)
    if words > 0:
        density = (weighted_score / words) * 1000
    else:
        density = 0
    
    # Determine if primarily about AI
    # Thresholds based on analysis
    if density >= 5 or strong_count >= 20:
        relevance = "HIGH"
        is_ai_hearing = True
    elif density >= 2 or strong_count >= 10:
        relevance = "MEDIUM"
        is_ai_hearing = True
    elif density >= 1 or strong_count >= 5:
        relevance = "LOW"
        is_ai_hearing = False  # Mentions AI but not primarily about it
    else:
        relevance = "NONE"
        is_ai_hearing = False
    
    return {
        'id': transcript_path.stem,
        'title': title,
        'strong_ai_mentions': strong_count,
        'moderate_ai_mentions': moderate_count,
        'total_words': words,
        'ai_density': round(density, 2),
        'relevance': relevance,
        'is_ai_hearing': is_ai_hearing
    }


def filter_transcripts(transcript_dir: Path, output_path: Path):
    """Analyze all transcripts and output filtered list."""
    
    transcripts = list(transcript_dir.glob("CHRG-*.html")) + list(transcript_dir.glob("CHRG-*.txt"))
    
    results = []
    for t in transcripts:
        try:
            analysis = analyze_transcript(t)
            results.append(analysis)
        except Exception as e:
            print(f"Error processing {t}: {e}")
    
    # Sort by AI density
    results.sort(key=lambda x: x['ai_density'], reverse=True)
    
    # Save results
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Summary
    high = sum(1 for r in results if r['relevance'] == 'HIGH')
    med = sum(1 for r in results if r['relevance'] == 'MEDIUM')
    low = sum(1 for r in results if r['relevance'] == 'LOW')
    none = sum(1 for r in results if r['relevance'] == 'NONE')
    
    print(f"Total transcripts: {len(results)}")
    print(f"AI Relevance: HIGH={high}, MEDIUM={med}, LOW={low}, NONE={none}")
    print(f"Valid AI hearings (HIGH+MEDIUM): {high + med}")
    
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--transcripts", required=True, help="Transcript directory")
    parser.add_argument("-o", "--output", required=True, help="Output JSON path")
    
    args = parser.parse_args()
    
    filter_transcripts(Path(args.transcripts), Path(args.output))
