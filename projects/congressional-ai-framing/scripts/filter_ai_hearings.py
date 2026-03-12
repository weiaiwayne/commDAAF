#!/usr/bin/env python3
"""
Filter congressional hearings to identify those primarily about AI.
Addresses 64% false positive rate in pilot.
"""

import json
import re
from pathlib import Path
from typing import Tuple

# AI-related keywords for title matching
AI_TITLE_KEYWORDS = [
    r'\bai\b',
    r'artificial intelligence',
    r'machine learning',
    r'algorithm',
    r'chatbot',
    r'deepfake',
    r'deep\s*fake',
    r'generative',
    r'large language model',
    r'\bllm\b',
    r'autonomous',
    r'facial recognition',
    r'deepseek',
    r'openai',
    r'chatgpt',
    r'gpt-\d',
    r'neural network',
    r'automation',
    r'technology',  # Added
    r'tech\b',      # Added
    r'digital',     # Added
    r'cyber',       # Added
    r'data',        # Added
    r'innovation',  # Added
]

# AI keywords for content matching (broader)
AI_CONTENT_KEYWORDS = [
    r'\bartificial intelligence\b',
    r'\bmachine learning\b',
    r'\bdeep learning\b',
    r'\bneural network',
    r'\balgorithm',
    r'\bautomation\b',
    r'\bautomated\b',
    r'\bchatbot',
    r'\bai\s+system',
    r'\bai\s+model',
    r'\bai\s+tool',
    r'\bgenerative ai\b',
    r'\blarge language model',
    r'\bllm\b',
    r'\bdeepfake',
    r'\bfacial recognition\b',
    r'\bcomputer vision\b',
    r'\bnatural language processing\b',
    r'\bnlp\b',
    r'\brobot',
    r'\bautonomous',
]

# Committees known to focus on AI
AI_COMMITTEES = [
    'artificial intelligence',
    'technology',
    'science',
    'innovation',
    'cybersecurity',
    'intellectual property',
]


def count_ai_mentions(text: str) -> int:
    """Count AI-related keyword mentions in text."""
    text_lower = text.lower()
    count = 0
    for pattern in AI_CONTENT_KEYWORDS:
        matches = re.findall(pattern, text_lower)
        count += len(matches)
    return count


def has_ai_title(title: str) -> bool:
    """Check if title contains AI-related keywords."""
    title_lower = title.lower()
    for pattern in AI_TITLE_KEYWORDS:
        if re.search(pattern, title_lower):
            return True
    return False


def has_ai_committee(committee: str) -> bool:
    """Check if committee is AI-related."""
    if not committee:
        return False
    committee_lower = committee.lower()
    for kw in AI_COMMITTEES:
        if kw in committee_lower:
            return True
    return False


def calculate_ai_relevance(hearing: dict) -> Tuple[float, dict]:
    """
    Calculate AI relevance score for a hearing.
    Returns (score, details).
    
    Score interpretation:
    - 0.8+ : Definitely about AI
    - 0.5-0.8: Likely about AI
    - 0.3-0.5: Possibly about AI
    - <0.3: Probably not about AI
    """
    details = {}
    score = 0.0
    
    title = hearing.get('title', '') or ''
    excerpt = hearing.get('excerpt', '') or ''
    committee = hearing.get('committee', '') or ''
    excerpt_length = len(excerpt)
    
    # 1. Title contains AI keywords (strong signal) - up to 0.4
    if has_ai_title(title):
        score += 0.4
        details['ai_title'] = True
    else:
        details['ai_title'] = False
    
    # 2. AI mention density in excerpt - up to 0.4
    ai_mentions = count_ai_mentions(excerpt)
    details['ai_mentions'] = ai_mentions
    
    # Calculate density (mentions per 1000 chars)
    if excerpt_length > 0:
        density = (ai_mentions / excerpt_length) * 1000
        details['ai_density'] = round(density, 2)
        
        # Score based on density
        if density >= 5:
            score += 0.4
        elif density >= 2:
            score += 0.3
        elif density >= 1:
            score += 0.2
        elif density >= 0.5:
            score += 0.1
    
    # 3. AI-related committee - up to 0.2
    if has_ai_committee(committee):
        score += 0.2
        details['ai_committee'] = True
    else:
        details['ai_committee'] = False
    
    details['relevance_score'] = round(score, 2)
    
    return score, details


def filter_hearings(
    hearings: list,
    min_score: float = 0.5,
    return_all: bool = False
) -> list:
    """
    Filter hearings by AI relevance score.
    
    Args:
        hearings: List of hearing dicts
        min_score: Minimum relevance score to include
        return_all: If True, return all with scores; if False, filter
    
    Returns:
        List of hearings (filtered or annotated)
    """
    results = []
    
    for hearing in hearings:
        score, details = calculate_ai_relevance(hearing)
        
        annotated = {**hearing, **details}
        
        if return_all:
            results.append(annotated)
        elif score >= min_score:
            results.append(annotated)
    
    return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Filter AI-relevant hearings")
    parser.add_argument("-i", "--input", required=True, help="Input JSON file")
    parser.add_argument("-o", "--output", required=True, help="Output JSON file")
    parser.add_argument("-s", "--min-score", type=float, default=0.5, help="Min relevance score")
    parser.add_argument("--all", action="store_true", help="Output all with scores")
    
    args = parser.parse_args()
    
    with open(args.input) as f:
        hearings = json.load(f)
    
    filtered = filter_hearings(hearings, args.min_score, args.all)
    
    with open(args.output, 'w') as f:
        json.dump(filtered, f, indent=2)
    
    print(f"Input: {len(hearings)} hearings")
    print(f"Output: {len(filtered)} hearings (min_score={args.min_score})")
    
    # Show score distribution
    if args.all:
        scores = [h['relevance_score'] for h in filtered]
        high = sum(1 for s in scores if s >= 0.5)
        med = sum(1 for s in scores if 0.3 <= s < 0.5)
        low = sum(1 for s in scores if s < 0.3)
        print(f"Score distribution: High(≥0.5)={high}, Med(0.3-0.5)={med}, Low(<0.3)={low}")


if __name__ == "__main__":
    main()
