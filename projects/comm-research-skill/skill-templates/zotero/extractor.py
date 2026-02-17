#!/usr/bin/env python3
"""
Zotero Library Extractor for Communication Research Skill

Connects to a researcher's Zotero library and extracts:
- Methods used in the field
- Theoretical frameworks
- Data sources/platforms studied
- Key citations

Then generates domain-specific skill recommendations.

Usage:
    python extractor.py --user-id YOUR_USER_ID --api-key YOUR_API_KEY
    python extractor.py --user-id 6345227 --api-key abc123 --output analysis.json

Requirements:
    pip install pyzotero
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from collections import Counter
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict

try:
    from pyzotero import zotero
except ImportError:
    print("Error: pyzotero not installed. Run: pip install pyzotero")
    sys.exit(1)


@dataclass
class ExtractionResult:
    """Structured extraction from a single paper."""
    item_key: str
    title: str
    year: Optional[str]
    methods: List[str]
    theories: List[str]
    platforms: List[str]
    data_sources: List[str]
    concepts: List[str]
    tags: List[str]


@dataclass 
class LibraryAnalysis:
    """Aggregated analysis of entire library."""
    user_id: str
    total_items: int
    analysis_date: str
    methods: Dict[str, int]
    theories: Dict[str, int]
    platforms: Dict[str, int]
    data_sources: Dict[str, int]
    concepts: Dict[str, int]
    skill_recommendations: List[Dict[str, Any]]
    top_tags: Dict[str, int]


class ZoteroExtractor:
    """Extract research patterns from Zotero library."""
    
    # Detection patterns for methods
    METHOD_PATTERNS = {
        'network_analysis': r'network analysis|social network|graph analysis|centrality|gephi|igraph|networkx',
        'content_analysis': r'content analysis|coding scheme|intercoder|manual coding|qualitative coding',
        'topic_modeling': r'topic model|lda|latent dirichlet|bertopic|structural topic|stm',
        'sentiment_analysis': r'sentiment|opinion mining|polarity|valence|vader|textblob',
        'machine_learning': r'machine learning|classifier|supervised learning|random forest|neural network|deep learning',
        'llm_annotation': r'llm|large language model|gpt-4|claude|chatgpt|zero-shot|few-shot classification',
        'coordinated_behavior': r'coordinat\w+ (inauthentic|behavior)|astroturf|bot detection|information operation',
        'survey_research': r'\bsurvey\b|questionnaire|likert|self-report|panel study',
        'experimental': r'\bexperiment\b|treatment condition|control group|randomized|a/b test',
        'agent_simulation': r'agent.based|simulation|abm|computational model|artificial societ',
        'discourse_analysis': r'discourse analysis|critical discourse|conversation analysis',
        'frame_analysis': r'frame analysis|framing analysis|media frames',
        'regression_analysis': r'regression|ols|logistic|multilevel|hierarchical linear',
        'text_classification': r'text classif|document classif|categorization',
        'named_entity': r'named entity|ner|entity extraction',
        'embedding': r'word embedding|word2vec|bert|sentence embedding|semantic similarity',
    }
    
    # Detection patterns for theories
    THEORY_PATTERNS = {
        'attention_economy': r'attention econom|attention scarc|herbert simon|attention as resource',
        'networked_publics': r'networked public|network society|castells|boyd',
        'framing_theory': r'framing theory|frame analysis|entman|scheufele',
        'agenda_setting': r'agenda.setting|mccombs|shaw|second.level agenda',
        'diffusion': r'diffusion of innovation|cascade|viral spread|information diffusion|contagion',
        'echo_chambers': r'echo chamber|filter bubble|polarization|selective exposure',
        'platform_governance': r'platform governance|content moderation|platform accountability',
        'uses_gratifications': r'uses and gratification|u&g|gratification sought',
        'social_capital': r'social capital|bridging|bonding|putnam|lin',
        'collective_action': r'collective action|social movement|mobilization|protest',
        'public_sphere': r'public sphere|habermas|deliberation|deliberative',
        'spiral_of_silence': r'spiral of silence|noelle-neumann|opinion climate',
        'two_step_flow': r'two.step flow|opinion leader|katz|lazarsfeld',
        'artificial_sociality': r'artificial sociali|human-ai|machine fluency|meta-authenticity',
        'algorithmic_curation': r'algorithmic|recommender|personalization|filter',
    }
    
    # Platform patterns
    PLATFORM_PATTERNS = {
        'twitter': r'\btwitter\b|tweet|\bx\b(?=\s+(platform|api|data))|x\.com',
        'facebook': r'facebook|meta platform',
        'reddit': r'\breddit\b|subreddit|r/',
        'telegram': r'\btelegram\b',
        'youtube': r'youtube|video platform',
        'tiktok': r'tiktok|short.form video',
        'instagram': r'instagram|ig stories',
        'weibo': r'weibo|chinese social media',
        'whatsapp': r'whatsapp|messaging app',
        'bluesky': r'bluesky|at protocol|decentralized social',
        'mastodon': r'mastodon|fediverse|activitypub',
        'linkedin': r'linkedin|professional network',
        'twitch': r'\btwitch\b|streaming platform',
        'discord': r'\bdiscord\b|discord server',
        'wechat': r'wechat|weixin',
    }
    
    # Data source patterns
    DATA_SOURCE_PATTERNS = {
        'mediacloud': r'mediacloud|media cloud',
        'gdelt': r'\bgdelt\b|global database of events',
        'crowdtangle': r'crowdtangle|ct api',
        'pushshift': r'pushshift',
        'common_crawl': r'common crawl',
        'internet_archive': r'internet archive|wayback',
        'academic_api': r'academic api|twitter v2|research api',
        'news_api': r'news api|gnews|newsapi',
    }
    
    # Concept patterns (research topics)
    CONCEPT_PATTERNS = {
        'misinformation': r'misinformation|disinformation|fake news|false information',
        'polarization': r'polariz|partisan|ideological divide',
        'health_communication': r'health communicat|vaccine|covid|pandemic|public health',
        'political_communication': r'political communicat|election|campaign|voting|candidate',
        'climate_communication': r'climate communicat|climate change|environmental',
        'crisis_communication': r'crisis communicat|emergency|disaster',
        'science_communication': r'science communicat|scientific literacy|sci comm',
        'journalism': r'journalism|news|reporter|media coverage',
        'influencer': r'influencer|creator economy|content creator',
        'harassment': r'harassment|hate speech|toxic|abuse online',
        'privacy': r'privacy|surveillance|data protection',
        'moderation': r'content moderation|platform governance|takedown',
    }

    def __init__(self, user_id: str, api_key: str):
        """Initialize with Zotero credentials."""
        self.user_id = user_id
        self.api_key = api_key
        self.zot = zotero.Zotero(user_id, 'user', api_key)
        self.items: List[Dict] = []
        self.extractions: List[ExtractionResult] = []
        
    def fetch_library(self, limit: Optional[int] = None) -> List[Dict]:
        """Fetch all items from Zotero library."""
        print(f"Fetching library for user {self.user_id}...")
        
        if limit:
            self.items = self.zot.top(limit=limit)
        else:
            self.items = self.zot.everything(self.zot.top())
        
        # Filter out attachments
        self.items = [
            item for item in self.items 
            if item.get('data', {}).get('itemType') not in ['attachment', 'note']
        ]
        
        print(f"Fetched {len(self.items)} items (excluding attachments)")
        return self.items
    
    def _extract_patterns(self, text: str, patterns: Dict[str, str]) -> List[str]:
        """Match text against pattern dictionary."""
        text_lower = text.lower()
        matches = []
        for name, pattern in patterns.items():
            if re.search(pattern, text_lower, re.IGNORECASE):
                matches.append(name)
        return matches
    
    def extract_from_item(self, item: Dict) -> ExtractionResult:
        """Extract research patterns from single item."""
        data = item.get('data', {})
        
        # Build text corpus from available fields
        text_parts = [
            data.get('title', ''),
            data.get('abstractNote', ''),
            data.get('shortTitle', ''),
            ' '.join([t.get('tag', '') for t in data.get('tags', [])]),
        ]
        
        # Include notes if available
        for note in data.get('notes', []):
            if isinstance(note, dict):
                text_parts.append(note.get('note', ''))
        
        full_text = ' '.join(filter(None, text_parts))
        
        # Extract year
        date_str = data.get('date', '')
        year_match = re.search(r'(\d{4})', date_str)
        year = year_match.group(1) if year_match else None
        
        # Get tags
        tags = [t.get('tag', '') for t in data.get('tags', [])]
        
        return ExtractionResult(
            item_key=item.get('key', ''),
            title=data.get('title', 'Untitled'),
            year=year,
            methods=self._extract_patterns(full_text, self.METHOD_PATTERNS),
            theories=self._extract_patterns(full_text, self.THEORY_PATTERNS),
            platforms=self._extract_patterns(full_text, self.PLATFORM_PATTERNS),
            data_sources=self._extract_patterns(full_text, self.DATA_SOURCE_PATTERNS),
            concepts=self._extract_patterns(full_text, self.CONCEPT_PATTERNS),
            tags=tags,
        )
    
    def analyze_library(self) -> LibraryAnalysis:
        """Analyze entire library and aggregate findings."""
        if not self.items:
            self.fetch_library()
        
        # Extract from each item
        method_counter = Counter()
        theory_counter = Counter()
        platform_counter = Counter()
        source_counter = Counter()
        concept_counter = Counter()
        tag_counter = Counter()
        
        for item in self.items:
            extraction = self.extract_from_item(item)
            self.extractions.append(extraction)
            
            method_counter.update(extraction.methods)
            theory_counter.update(extraction.theories)
            platform_counter.update(extraction.platforms)
            source_counter.update(extraction.data_sources)
            concept_counter.update(extraction.concepts)
            tag_counter.update(extraction.tags)
        
        # Generate skill recommendations
        recommendations = self._generate_recommendations(
            method_counter, theory_counter, platform_counter, concept_counter
        )
        
        return LibraryAnalysis(
            user_id=self.user_id,
            total_items=len(self.items),
            analysis_date=datetime.now().isoformat(),
            methods=dict(method_counter.most_common()),
            theories=dict(theory_counter.most_common()),
            platforms=dict(platform_counter.most_common()),
            data_sources=dict(source_counter.most_common()),
            concepts=dict(concept_counter.most_common()),
            skill_recommendations=recommendations,
            top_tags=dict(tag_counter.most_common(20)),
        )
    
    def _generate_recommendations(
        self, 
        methods: Counter, 
        theories: Counter,
        platforms: Counter,
        concepts: Counter,
    ) -> List[Dict[str, Any]]:
        """Generate skill recommendations based on analysis."""
        recommendations = []
        
        # Method-based recommendations
        method_skills = {
            'network_analysis': {
                'skill': 'methods/network-analysis.md',
                'priority': 'high',
                'reason': 'Network analysis appears frequently in your library',
            },
            'coordinated_behavior': {
                'skill': 'methods/coordinated-behavior.md', 
                'priority': 'high',
                'reason': 'Coordinated behavior detection is a core method',
            },
            'topic_modeling': {
                'skill': 'methods/topic-modeling.md',
                'priority': 'standard',
                'reason': 'Topic modeling used for text analysis',
            },
            'llm_annotation': {
                'skill': 'methods/llm-annotation.md',
                'priority': 'emerging',
                'reason': 'LLM-based annotation is an emerging method in your field',
            },
            'sentiment_analysis': {
                'skill': 'methods/sentiment-analysis.md',
                'priority': 'standard',
                'reason': 'Sentiment analysis commonly used',
            },
            'agent_simulation': {
                'skill': 'methods/agent-simulation.md',
                'priority': 'advanced',
                'reason': 'Agent-based modeling for simulation studies',
            },
        }
        
        for method, count in methods.most_common():
            if method in method_skills and count >= 2:
                rec = method_skills[method].copy()
                rec['count'] = count
                recommendations.append(rec)
        
        # Platform-based recommendations
        for platform, count in platforms.most_common(5):
            if count >= 3:
                recommendations.append({
                    'skill': f'data-sources/{platform}.md',
                    'priority': 'high' if count >= 5 else 'standard',
                    'reason': f'{platform.title()} appears in {count} papers',
                    'count': count,
                })
        
        # Theory-based recommendations
        theory_skills = {
            'attention_economy': 'theories/attention-economy.md',
            'networked_publics': 'theories/networked-publics.md',
            'coordinated_behavior': 'theories/coordinated-behavior.md',
            'artificial_sociality': 'theories/artificial-sociality.md',
            'framing_theory': 'theories/framing.md',
            'agenda_setting': 'theories/agenda-setting.md',
        }
        
        for theory, count in theories.most_common():
            if theory in theory_skills and count >= 2:
                recommendations.append({
                    'skill': theory_skills[theory],
                    'priority': 'theory',
                    'reason': f'{theory.replace("_", " ").title()} framework used in {count} papers',
                    'count': count,
                })
        
        # Sort by count
        recommendations.sort(key=lambda x: x.get('count', 0), reverse=True)
        
        return recommendations
    
    def export_json(self, path: str) -> None:
        """Export analysis to JSON file."""
        analysis = self.analyze_library()
        
        with open(path, 'w') as f:
            json.dump(asdict(analysis), f, indent=2)
        
        print(f"Exported analysis to {path}")
    
    def export_markdown(self, path: str) -> str:
        """Export analysis to markdown file."""
        analysis = self.analyze_library()
        
        md = f"""# Zotero Library Analysis

**User ID:** {analysis.user_id}  
**Total Items:** {analysis.total_items}  
**Analysis Date:** {analysis.analysis_date}

---

## Methods Detected

| Method | Count |
|--------|-------|
"""
        for method, count in sorted(analysis.methods.items(), key=lambda x: -x[1]):
            md += f"| {method.replace('_', ' ').title()} | {count} |\n"
        
        md += """
## Theoretical Frameworks

| Theory | Count |
|--------|-------|
"""
        for theory, count in sorted(analysis.theories.items(), key=lambda x: -x[1]):
            md += f"| {theory.replace('_', ' ').title()} | {count} |\n"
        
        md += """
## Platforms Studied

| Platform | Count |
|----------|-------|
"""
        for platform, count in sorted(analysis.platforms.items(), key=lambda x: -x[1]):
            md += f"| {platform.title()} | {count} |\n"
        
        md += """
## Data Sources

| Source | Count |
|--------|-------|
"""
        for source, count in sorted(analysis.data_sources.items(), key=lambda x: -x[1]):
            md += f"| {source.replace('_', ' ').title()} | {count} |\n"
        
        md += """
## Research Topics

| Concept | Count |
|---------|-------|
"""
        for concept, count in sorted(analysis.concepts.items(), key=lambda x: -x[1]):
            md += f"| {concept.replace('_', ' ').title()} | {count} |\n"
        
        md += """
## Skill Recommendations

Based on your library, prioritize these skills:

| Skill | Priority | Reason |
|-------|----------|--------|
"""
        for rec in analysis.skill_recommendations[:15]:
            md += f"| `{rec['skill']}` | {rec['priority']} | {rec['reason']} |\n"
        
        md += """
---

*Generated by Communication Research Skill Zotero Adapter*
"""
        
        with open(path, 'w') as f:
            f.write(md)
        
        print(f"Exported analysis to {path}")
        return md


def main():
    parser = argparse.ArgumentParser(
        description='Analyze Zotero library for communication research patterns'
    )
    parser.add_argument('--user-id', required=True, help='Zotero user ID')
    parser.add_argument('--api-key', required=True, help='Zotero API key')
    parser.add_argument('--output', '-o', default='zotero_analysis', 
                       help='Output filename (without extension)')
    parser.add_argument('--format', choices=['json', 'md', 'both'], default='both',
                       help='Output format')
    parser.add_argument('--limit', type=int, help='Limit number of items to fetch')
    
    args = parser.parse_args()
    
    extractor = ZoteroExtractor(args.user_id, args.api_key)
    extractor.fetch_library(limit=args.limit)
    
    if args.format in ('json', 'both'):
        extractor.export_json(f"{args.output}.json")
    
    if args.format in ('md', 'both'):
        extractor.export_markdown(f"{args.output}.md")
    
    print("\nDone! Use the analysis to customize your skill package.")


if __name__ == '__main__':
    main()
