#!/usr/bin/env python3
"""
CommDAAF Zotero Adapter

Analyzes your Zotero library to customize CommDAAF skills
based on your research methods and domain.

Usage:
    python zotero_adapt.py --user-id YOUR_ID --api-key YOUR_KEY
"""

import argparse
import json
from collections import Counter

try:
    from pyzotero import zotero
except ImportError:
    print("Install pyzotero: pip install pyzotero")
    exit(1)


def get_library(user_id: str, api_key: str, limit: int = 100):
    """Fetch items from Zotero library."""
    zot = zotero.Zotero(user_id, 'user', api_key)
    items = zot.top(limit=limit)
    return items


def analyze_methods(items: list) -> dict:
    """Analyze which methods appear in library."""
    method_keywords = {
        'sentiment': ['sentiment', 'valence', 'emotion', 'opinion mining'],
        'topic_modeling': ['topic model', 'lda', 'bertopic', 'latent dirichlet'],
        'network': ['network analysis', 'graph', 'centrality', 'community detection'],
        'framing': ['frame analysis', 'framing', 'media frames'],
        'content': ['content analysis', 'codebook', 'coding scheme'],
        'coordination': ['coordinated', 'inauthentic', 'bot detection', 'astroturf'],
        'llm': ['large language model', 'gpt', 'chatgpt', 'llm', 'annotation'],
    }
    
    counts = Counter()
    for item in items:
        text = json.dumps(item.get('data', {})).lower()
        for method, keywords in method_keywords.items():
            if any(kw in text for kw in keywords):
                counts[method] += 1
    
    return dict(counts)


def analyze_domains(items: list) -> dict:
    """Analyze research domains in library."""
    domain_keywords = {
        'political': ['political', 'election', 'campaign', 'voting', 'democracy'],
        'health': ['health', 'medical', 'covid', 'pandemic', 'vaccine'],
        'climate': ['climate', 'environment', 'sustainability', 'carbon'],
        'misinformation': ['misinformation', 'disinformation', 'fake news', 'fact-check'],
        'social_movements': ['protest', 'movement', 'activism', 'mobilization'],
    }
    
    counts = Counter()
    for item in items:
        text = json.dumps(item.get('data', {})).lower()
        for domain, keywords in domain_keywords.items():
            if any(kw in text for kw in keywords):
                counts[domain] += 1
    
    return dict(counts)


def generate_profile(methods: dict, domains: dict) -> dict:
    """Generate researcher profile from analysis."""
    profile = {
        'methods': {
            'primary': [],
            'secondary': [],
        },
        'domains': {
            'primary': [],
            'secondary': [],
        },
        'recommendations': [],
    }
    
    # Sort by frequency
    sorted_methods = sorted(methods.items(), key=lambda x: x[1], reverse=True)
    sorted_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)
    
    # Assign primary/secondary
    for i, (method, count) in enumerate(sorted_methods):
        if count > 0:
            if i < 2:
                profile['methods']['primary'].append(method)
            else:
                profile['methods']['secondary'].append(method)
    
    for i, (domain, count) in enumerate(sorted_domains):
        if count > 0:
            if i < 2:
                profile['domains']['primary'].append(domain)
            else:
                profile['domains']['secondary'].append(domain)
    
    # Generate recommendations
    if 'sentiment' in profile['methods']['primary']:
        if 'political' in profile['domains']['primary'] or 'climate' in profile['domains']['primary']:
            profile['recommendations'].append(
                "High sarcasm domain detected. Always run sarcasm detection before sentiment analysis."
            )
    
    if 'coordination' in profile['methods']['primary']:
        profile['recommendations'].append(
            "Coordinated behavior research requires extra rigor. Review coordinated-behavior.md carefully."
        )
    
    return profile


def main():
    parser = argparse.ArgumentParser(description='Analyze Zotero library for CommDAAF')
    parser.add_argument('--user-id', required=True, help='Zotero user ID')
    parser.add_argument('--api-key', required=True, help='Zotero API key')
    parser.add_argument('--limit', type=int, default=100, help='Max items to analyze')
    parser.add_argument('--output', default='commdaaf_profile.json', help='Output file')
    args = parser.parse_args()
    
    print(f"Fetching library for user {args.user_id}...")
    items = get_library(args.user_id, args.api_key, args.limit)
    print(f"Analyzing {len(items)} items...")
    
    methods = analyze_methods(items)
    domains = analyze_domains(items)
    profile = generate_profile(methods, domains)
    
    print("\n=== CommDAAF Profile ===")
    print(f"Primary methods: {', '.join(profile['methods']['primary']) or 'None detected'}")
    print(f"Primary domains: {', '.join(profile['domains']['primary']) or 'None detected'}")
    
    if profile['recommendations']:
        print("\nRecommendations:")
        for rec in profile['recommendations']:
            print(f"  • {rec}")
    
    with open(args.output, 'w') as f:
        json.dump(profile, f, indent=2)
    print(f"\nProfile saved to {args.output}")


if __name__ == '__main__':
    main()
