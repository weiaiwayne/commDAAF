#!/usr/bin/env python3
"""
Skill Generator for Communication Research

Takes Zotero analysis output and generates customized skill files.
Creates domain-specific method skills, theory integrations, and workflow priorities.

Usage:
    python generator.py --analysis zotero_analysis.json --output-dir ./generated/
    
Or combined with extractor:
    python extractor.py --user-id 123 --api-key xyz --output analysis
    python generator.py --analysis analysis.json --output-dir ./skills/
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path


class SkillGenerator:
    """Generate customized skill files from library analysis."""
    
    # Templates for auto-generated skills
    METHOD_TEMPLATES = {
        'network_analysis': '''# Network Analysis Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Network analysis examines relationships and structures in social data.
Based on your library, you frequently use network methods for:
{use_cases}

## Priority in Your Research: {priority}

Detected in {count} papers in your library.

## Key Methods

### 1. Network Construction
- Co-occurrence networks (hashtags, URLs, mentions)
- Interaction networks (replies, retweets, quotes)
- Affiliation networks (group membership)
- Temporal networks (time-varying edges)

### 2. Centrality Measures
- Degree centrality (connections)
- Betweenness centrality (bridging)
- Eigenvector/PageRank (influence)
- Closeness centrality (access)

### 3. Community Detection
- Louvain algorithm
- Label propagation
- Infomap
- Spectral clustering

### 4. Coordinated Behavior Detection
- Co-sharing within time windows
- Synchronized posting patterns
- Network-based clustering of coordinated actors

## Python Libraries

```python
import networkx as nx
import igraph as ig
from cdlib import algorithms  # Community detection

# For large graphs
import graph_tool  # Faster than networkx
```

## Integration with Your Platforms

{platform_notes}

## Key Citations from Your Library

{citations}

## Workflow Integration

```yaml
# Spawn network analysis agent
sessions_spawn:
  task: "Construct [network_type] network from [data_source]"
  agentId: comm-research-network
  model: deepseek/deepseek-v3  # Good at code
```

---
*Auto-generated based on your research profile*
''',
        
        'coordinated_behavior': '''# Coordinated Behavior Detection Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Detect and analyze coordinated activity across platforms.
Your library shows strong focus on this method ({count} papers).

## Priority in Your Research: {priority}

## Core Framework (Giglietto et al.)

1. **Data Collection**: Gather content with shared identifiers
2. **Co-sharing Detection**: Find accounts sharing same content rapidly
3. **Network Construction**: Build network from co-sharing patterns
4. **Community Detection**: Identify clusters of coordinated actors
5. **Validation**: Manual review of flagged networks

## Detection Signals

### Temporal
- Synchronized posting (same minute/hour)
- Rapid sequential sharing
- Activity bursts

### Network
- Dense interconnection
- Unusual follower patterns
- Amplification chains

### Content
- Identical/near-identical posts
- Shared URLs across accounts
- Hashtag coordination

## Implementation

```python
import pandas as pd
import networkx as nx
from datetime import timedelta

def detect_coordination(df, time_window='1h', min_shared=2):
    """
    Detect coordinated sharing based on temporal proximity.
    
    Args:
        df: DataFrame with columns [user_id, content_id, timestamp]
        time_window: Window for considering coordination
        min_shared: Minimum shared items to flag as coordinated
    """
    # Group by content
    coord_pairs = []
    
    for content_id, group in df.groupby('content_id'):
        if len(group) < 2:
            continue
            
        group = group.sort_values('timestamp')
        
        for i, row1 in group.iterrows():
            for j, row2 in group.iterrows():
                if i >= j:
                    continue
                    
                time_diff = row2['timestamp'] - row1['timestamp']
                if time_diff <= pd.Timedelta(time_window):
                    coord_pairs.append((row1['user_id'], row2['user_id']))
    
    # Build coordination network
    G = nx.Graph()
    for u1, u2 in coord_pairs:
        if G.has_edge(u1, u2):
            G[u1][u2]['weight'] += 1
        else:
            G.add_edge(u1, u2, weight=1)
    
    # Filter by minimum shared
    G = nx.Graph([(u, v, d) for u, v, d in G.edges(data=True) 
                  if d['weight'] >= min_shared])
    
    return G
```

## Ethical Considerations

{ethical_notes}

## Platform-Specific Notes

{platform_notes}

## Key Citations from Your Library

{citations}

---
*Auto-generated based on your research profile*
''',

        'llm_annotation': '''# LLM-Based Annotation Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Use large language models for text classification and annotation.
Emerging method detected in your library ({count} papers).

## Priority in Your Research: {priority}

## Key Approaches

### Zero-Shot Classification
```python
prompt = """
Classify this social media post into one of these categories:
- Political
- Commercial  
- Personal
- News

Post: [text]

Category:
"""
```

### Few-Shot Classification
```python
prompt = """
Classify posts as "Coordinated" or "Organic" based on these examples:

[Examples]
Post: "Share this NOW! Our candidate needs your support! #Vote2024"
Label: Coordinated (mobilization language, urgency)

Post: "Just voted for the first time, feeling proud"
Label: Organic (personal, authentic)

[Task]
Post: [text]
Label:
"""
```

### Multi-Model Validation
Use different models for annotation and review:
- Annotator: Gemini Flash (fast, cheap)
- Reviewer: Claude/GPT-4 (catches errors)
- Disagreement → human review

## Cost Optimization

| Model | Cost per 1M tokens | Speed | Use Case |
|-------|-------------------|-------|----------|
| Gemini Flash | ~$0.075 | Fast | Bulk annotation |
| GPT-4o-mini | ~$0.15 | Fast | Standard tasks |
| Claude Sonnet | ~$3 | Medium | Complex reasoning |

## Validation Strategy

1. Sample N items (e.g., 200)
2. Human-code the sample
3. Compare LLM labels to human
4. Calculate inter-rater reliability
5. Document in methods section

## Integration with Your Research

{platform_notes}

## Key Citations

{citations}

---
*Auto-generated based on your research profile*
''',
    }
    
    THEORY_TEMPLATES = {
        'attention_economy': '''# Attention Economy Framework (Auto-Customized)

*Integrated based on your Zotero library*

## Core Principle

"What information consumes is rather obvious: it consumes the attention 
of its recipients." — Herbert Simon

In your research context, attention economy appears in {count} papers.

## Key Concepts

1. **Attention Scarcity**: Finite human attention vs. infinite content
2. **Competition**: Content competes for limited attention
3. **Inequality**: Power-law distribution of attention
4. **Algorithmic Mediation**: Platforms shape attention allocation

## Measurement Approaches

### Platform Metrics as Attention Proxies
- Engagement (likes, shares, comments)
- View counts / impressions
- Watch time / scroll depth
- Click-through rates

### Aggregate Measures
- Attention Gini coefficient (inequality)
- Concentration ratios
- Long-tail analysis

## Research Questions

- How is attention distributed across actors?
- What content features predict attention capture?
- How do algorithms shape attention flows?
- What are consequences of attention inequality?

## Connection to Your Methods

{method_connections}

## Key Citations from Your Library

{citations}

---
*Auto-generated based on your research profile*
''',
        
        'artificial_sociality': '''# Artificial Sociality Framework (Auto-Customized)

*Integrated based on your Zotero library*

## Core Concept

The study of social interaction between humans and artificial agents.
Highly relevant to your work on agentic AI ({count} papers).

## Key Concepts

### Meta-Authenticity
Artificial actors performing authenticity while acknowledging artificiality.
Relevant for studying AI personas, virtual influencers, chatbots.

### Machine Fluency
The skill of effectively instructing AI agents.
A new source of heterogeneity in outcomes.

### Agentic Attention
How AI agents mediate and allocate attention on behalf of humans.

## Research Applications

### AI-Mediated Communication
- How do AI agents shape human-human communication?
- What happens when AI agents interact?
- Implications for research practice itself

### Reflexive Research Design
- This skill package is itself an example of artificial sociality
- Document how AI tools shape your research process
- Consider AI's role in knowledge production

## Connection to Your Methods

{method_connections}

## Key Citations from Your Library

{citations}

---
*Auto-generated based on your research profile*
''',
    }
    
    def __init__(self, analysis: Dict[str, Any]):
        """Initialize with analysis data."""
        self.analysis = analysis
        self.generated_files: List[str] = []
        
    @classmethod
    def from_json(cls, path: str) -> 'SkillGenerator':
        """Load analysis from JSON file."""
        with open(path) as f:
            analysis = json.load(f)
        return cls(analysis)
    
    def _get_priority(self, count: int) -> str:
        """Determine priority level from count."""
        if count >= 10:
            return "CRITICAL"
        elif count >= 5:
            return "HIGH"
        elif count >= 3:
            return "STANDARD"
        else:
            return "OPTIONAL"
    
    def _get_platform_notes(self, platforms: Dict[str, int]) -> str:
        """Generate platform-specific notes."""
        if not platforms:
            return "No specific platform focus detected."
        
        top_platforms = sorted(platforms.items(), key=lambda x: -x[1])[:3]
        notes = []
        for platform, count in top_platforms:
            notes.append(f"- **{platform.title()}**: Appears in {count} papers")
        
        return '\n'.join(notes)
    
    def _get_citations_placeholder(self, method: str) -> str:
        """Get citation placeholder for method."""
        return f"*Add key citations for {method} from your library here*"
    
    def _get_use_cases(self, method: str, concepts: Dict[str, int]) -> str:
        """Infer use cases from detected concepts."""
        use_cases = []
        
        concept_method_map = {
            'network_analysis': ['polarization', 'misinformation', 'political_communication', 'collective_action'],
            'coordinated_behavior': ['misinformation', 'political_communication'],
            'llm_annotation': ['misinformation', 'health_communication', 'political_communication'],
        }
        
        relevant_concepts = concept_method_map.get(method, [])
        
        for concept in relevant_concepts:
            if concept in concepts:
                use_cases.append(f"- {concept.replace('_', ' ').title()} research")
        
        if not use_cases:
            use_cases.append("- General communication research applications")
        
        return '\n'.join(use_cases)
    
    def generate_method_skill(self, method: str, count: int, output_dir: Path) -> str:
        """Generate customized method skill file."""
        if method not in self.METHOD_TEMPLATES:
            return None
        
        template = self.METHOD_TEMPLATES[method]
        
        content = template.format(
            priority=self._get_priority(count),
            count=count,
            use_cases=self._get_use_cases(method, self.analysis.get('concepts', {})),
            platform_notes=self._get_platform_notes(self.analysis.get('platforms', {})),
            citations=self._get_citations_placeholder(method),
            ethical_notes="- Coordination ≠ inauthenticity\n- Document methodology transparently\n- Avoid false positives",
            network_type="co-sharing",
            data_source="collected posts",
        )
        
        # Write file
        methods_dir = output_dir / 'methods'
        methods_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{method.replace('_', '-')}.md"
        filepath = methods_dir / filename
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        self.generated_files.append(str(filepath))
        return str(filepath)
    
    def generate_theory_skill(self, theory: str, count: int, output_dir: Path) -> str:
        """Generate customized theory skill file."""
        if theory not in self.THEORY_TEMPLATES:
            return None
        
        template = self.THEORY_TEMPLATES[theory]
        
        # Build method connections
        methods = self.analysis.get('methods', {})
        method_notes = []
        for m, c in sorted(methods.items(), key=lambda x: -x[1])[:3]:
            method_notes.append(f"- **{m.replace('_', ' ').title()}** ({c} papers)")
        
        content = template.format(
            count=count,
            method_connections='\n'.join(method_notes) if method_notes else "No specific method connections detected.",
            citations=self._get_citations_placeholder(theory),
        )
        
        # Write file
        theories_dir = output_dir / 'theories'
        theories_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{theory.replace('_', '-')}.md"
        filepath = theories_dir / filename
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        self.generated_files.append(str(filepath))
        return str(filepath)
    
    def generate_config(self, output_dir: Path) -> str:
        """Generate customized config based on analysis."""
        platforms = self.analysis.get('platforms', {})
        methods = self.analysis.get('methods', {})
        
        # Determine priority data sources
        priority_sources = []
        for platform, count in sorted(platforms.items(), key=lambda x: -x[1])[:5]:
            if count >= 2:
                priority_sources.append(platform)
        
        # Determine priority methods
        priority_methods = []
        for method, count in sorted(methods.items(), key=lambda x: -x[1])[:5]:
            if count >= 2:
                priority_methods.append(method.replace('_', '-'))
        
        config = {
            "generated_date": datetime.now().isoformat(),
            "source_library": self.analysis.get('user_id'),
            "total_papers_analyzed": self.analysis.get('total_items'),
            "priorities": {
                "data_sources": priority_sources,
                "methods": priority_methods,
            },
            "model_routing": {
                "orchestrator": "anthropic/claude-opus-4",
                "data_collection": "google/gemini-2.0-flash",
                "text_analysis": "deepseek/deepseek-v3",
                "code_review": "openai/gpt-4o",
                "synthesis": "anthropic/claude-opus-4",
            },
        }
        
        filepath = output_dir / 'config.json'
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.generated_files.append(str(filepath))
        return str(filepath)
    
    def generate_readme(self, output_dir: Path) -> str:
        """Generate README for generated skills."""
        methods = self.analysis.get('methods', {})
        theories = self.analysis.get('theories', {})
        platforms = self.analysis.get('platforms', {})
        
        readme = f"""# Auto-Generated Skills

*Generated from Zotero library analysis*

**Source:** User {self.analysis.get('user_id')}  
**Papers analyzed:** {self.analysis.get('total_items')}  
**Generated:** {datetime.now().isoformat()}

## Your Research Profile

### Top Methods
"""
        for method, count in sorted(methods.items(), key=lambda x: -x[1])[:5]:
            readme += f"- {method.replace('_', ' ').title()} ({count} papers)\n"
        
        readme += "\n### Top Theories\n"
        for theory, count in sorted(theories.items(), key=lambda x: -x[1])[:5]:
            readme += f"- {theory.replace('_', ' ').title()} ({count} papers)\n"
        
        readme += "\n### Top Platforms\n"
        for platform, count in sorted(platforms.items(), key=lambda x: -x[1])[:5]:
            readme += f"- {platform.title()} ({count} papers)\n"
        
        readme += """
## Generated Files

"""
        for f in self.generated_files:
            readme += f"- `{f}`\n"
        
        readme += """
## Usage

Copy these files to your skill directory:

```bash
cp -r generated/* ~/.openclaw/workspace/skills/comm-research/
```

Then the skill will use your customized method and theory files.

## Customization

These files are starting points. Edit them to:
- Add specific citations from your library
- Adjust method parameters for your use cases
- Add platform-specific notes
- Integrate with your existing workflows

---
*Generated by Communication Research Skill Zotero Adapter*
"""
        
        filepath = output_dir / 'README.md'
        with open(filepath, 'w') as f:
            f.write(readme)
        
        return str(filepath)
    
    def generate_all(self, output_dir: str) -> List[str]:
        """Generate all customized skills."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate method skills for detected methods
        methods = self.analysis.get('methods', {})
        for method, count in methods.items():
            if count >= 2:  # Only generate if appears in 2+ papers
                self.generate_method_skill(method, count, output_path)
        
        # Generate theory skills for detected theories
        theories = self.analysis.get('theories', {})
        for theory, count in theories.items():
            if count >= 2:
                self.generate_theory_skill(theory, count, output_path)
        
        # Generate config
        self.generate_config(output_path)
        
        # Generate README
        self.generate_readme(output_path)
        
        print(f"\nGenerated {len(self.generated_files)} files in {output_dir}")
        return self.generated_files


def main():
    parser = argparse.ArgumentParser(
        description='Generate customized skills from Zotero analysis'
    )
    parser.add_argument('--analysis', required=True, help='Path to analysis JSON file')
    parser.add_argument('--output-dir', '-o', default='./generated',
                       help='Output directory for generated skills')
    
    args = parser.parse_args()
    
    generator = SkillGenerator.from_json(args.analysis)
    files = generator.generate_all(args.output_dir)
    
    print("\nGenerated files:")
    for f in files:
        print(f"  - {f}")


if __name__ == '__main__':
    main()
