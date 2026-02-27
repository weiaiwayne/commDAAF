#!/usr/bin/env python3
"""
CommDAAF Literature Synthesis

Systematic literature search, citation mapping, and synthesis.
"""

import json
import re
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field, asdict
from datetime import datetime
from urllib.parse import quote_plus
import urllib.request

@dataclass
class Paper:
    """Container for paper metadata."""
    title: str
    authors: List[str]
    year: int
    venue: Optional[str] = None
    doi: Optional[str] = None
    arxiv_id: Optional[str] = None
    abstract: Optional[str] = None
    citations: int = 0
    references: List[str] = field(default_factory=list)
    cited_by: List[str] = field(default_factory=list)
    url: Optional[str] = None
    source: str = "unknown"
    
    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v}
    
    def to_citation(self, style: str = "apa") -> str:
        """Generate citation string."""
        if style == "apa":
            authors_str = ", ".join(self.authors[:3])
            if len(self.authors) > 3:
                authors_str += " et al."
            return f"{authors_str} ({self.year}). {self.title}. {self.venue or ''}."
        else:
            return f"{self.authors[0]} et al. {self.year}"


@dataclass
class CitationNetwork:
    """Container for citation network."""
    anchor: Paper
    foundations: List[Paper] = field(default_factory=list)
    descendants: List[Paper] = field(default_factory=list)
    
    def to_dict(self):
        return {
            "anchor": self.anchor.to_dict(),
            "foundations": [p.to_dict() for p in self.foundations],
            "descendants": [p.to_dict() for p in self.descendants],
            "stats": {
                "foundation_count": len(self.foundations),
                "descendant_count": len(self.descendants),
                "total_network_size": 1 + len(self.foundations) + len(self.descendants)
            }
        }


@dataclass
class ResearchGap:
    """Container for identified research gap."""
    dimension: str
    gap_description: str
    evidence: List[str]
    opportunity: str
    priority: str  # high, medium, low


class SemanticScholarAPI:
    """Client for Semantic Scholar API."""
    
    BASE_URL = "https://api.semanticscholar.org/graph/v1"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.headers = {"x-api-key": api_key} if api_key else {}
    
    def search(
        self,
        query: str,
        limit: int = 20,
        year_range: Optional[Tuple[int, int]] = None,
        fields: str = "title,authors,year,venue,citationCount,abstract,externalIds"
    ) -> List[Paper]:
        """Search for papers by query."""
        url = f"{self.BASE_URL}/paper/search?query={quote_plus(query)}&limit={limit}&fields={fields}"
        
        if year_range:
            url += f"&year={year_range[0]}-{year_range[1]}"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            print(f"Search error: {e}")
            return []
        
        papers = []
        for item in data.get("data", []):
            paper = Paper(
                title=item.get("title", ""),
                authors=[a.get("name", "") for a in item.get("authors", [])],
                year=item.get("year", 0),
                venue=item.get("venue", ""),
                doi=item.get("externalIds", {}).get("DOI"),
                arxiv_id=item.get("externalIds", {}).get("ArXiv"),
                abstract=item.get("abstract", ""),
                citations=item.get("citationCount", 0),
                source="semantic_scholar"
            )
            papers.append(paper)
        
        return papers
    
    def get_paper(self, paper_id: str, fields: str = "title,authors,year,venue,citationCount,abstract,references,citations") -> Optional[Paper]:
        """Get paper by Semantic Scholar ID or DOI."""
        url = f"{self.BASE_URL}/paper/{paper_id}?fields={fields}"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                item = json.loads(response.read().decode())
        except Exception as e:
            print(f"Get paper error: {e}")
            return None
        
        return Paper(
            title=item.get("title", ""),
            authors=[a.get("name", "") for a in item.get("authors", [])],
            year=item.get("year", 0),
            venue=item.get("venue", ""),
            doi=item.get("externalIds", {}).get("DOI") if item.get("externalIds") else None,
            abstract=item.get("abstract", ""),
            citations=item.get("citationCount", 0),
            references=[r.get("paperId") for r in item.get("references", []) if r.get("paperId")],
            cited_by=[c.get("paperId") for c in item.get("citations", []) if c.get("paperId")],
            source="semantic_scholar"
        )
    
    def get_citations(self, paper_id: str, limit: int = 100) -> List[Paper]:
        """Get papers that cite this paper."""
        url = f"{self.BASE_URL}/paper/{paper_id}/citations?limit={limit}&fields=title,authors,year,venue,citationCount"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            print(f"Get citations error: {e}")
            return []
        
        papers = []
        for item in data.get("data", []):
            citing = item.get("citingPaper", {})
            paper = Paper(
                title=citing.get("title", ""),
                authors=[a.get("name", "") for a in citing.get("authors", [])],
                year=citing.get("year", 0),
                venue=citing.get("venue", ""),
                citations=citing.get("citationCount", 0),
                source="semantic_scholar"
            )
            papers.append(paper)
        
        return papers
    
    def get_references(self, paper_id: str, limit: int = 100) -> List[Paper]:
        """Get papers this paper cites."""
        url = f"{self.BASE_URL}/paper/{paper_id}/references?limit={limit}&fields=title,authors,year,venue,citationCount"
        
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            print(f"Get references error: {e}")
            return []
        
        papers = []
        for item in data.get("data", []):
            cited = item.get("citedPaper", {})
            if not cited:
                continue
            paper = Paper(
                title=cited.get("title", ""),
                authors=[a.get("name", "") for a in cited.get("authors", [])],
                year=cited.get("year", 0),
                venue=cited.get("venue", ""),
                citations=cited.get("citationCount", 0),
                source="semantic_scholar"
            )
            papers.append(paper)
        
        return papers


class OpenAlexAPI:
    """Client for OpenAlex API."""
    
    BASE_URL = "https://api.openalex.org"
    
    def __init__(self, email: Optional[str] = None):
        self.email = email
    
    def search(
        self,
        query: str,
        limit: int = 20,
        year_range: Optional[Tuple[int, int]] = None
    ) -> List[Paper]:
        """Search for works by query."""
        url = f"{self.BASE_URL}/works?search={quote_plus(query)}&per_page={limit}"
        
        if year_range:
            url += f"&filter=publication_year:{year_range[0]}-{year_range[1]}"
        
        if self.email:
            url += f"&mailto={self.email}"
        
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            print(f"OpenAlex search error: {e}")
            return []
        
        papers = []
        for item in data.get("results", []):
            paper = Paper(
                title=item.get("title", ""),
                authors=[a.get("author", {}).get("display_name", "") 
                        for a in item.get("authorships", [])[:5]],
                year=item.get("publication_year", 0),
                venue=item.get("primary_location", {}).get("source", {}).get("display_name") if item.get("primary_location") else None,
                doi=item.get("doi", "").replace("https://doi.org/", "") if item.get("doi") else None,
                citations=item.get("cited_by_count", 0),
                source="openalex"
            )
            papers.append(paper)
        
        return papers


class LiteratureSynthesis:
    """Main interface for literature synthesis."""
    
    def __init__(self, semantic_scholar_key: Optional[str] = None, email: Optional[str] = None):
        self.ss = SemanticScholarAPI(api_key=semantic_scholar_key)
        self.oa = OpenAlexAPI(email=email)
    
    def search(
        self,
        query: str,
        years: Optional[Tuple[int, int]] = None,
        min_citations: int = 0,
        limit: int = 50,
        sources: List[str] = ["semantic_scholar", "openalex"]
    ) -> List[Paper]:
        """
        Search for papers across multiple sources.
        
        Args:
            query: Search query
            years: (start_year, end_year) filter
            min_citations: Minimum citation count
            limit: Max results per source
            sources: Which APIs to query
        
        Returns:
            Deduplicated list of papers sorted by citations
        """
        all_papers = []
        
        if "semantic_scholar" in sources:
            ss_papers = self.ss.search(query, limit=limit, year_range=years)
            all_papers.extend(ss_papers)
        
        if "openalex" in sources:
            oa_papers = self.oa.search(query, limit=limit, year_range=years)
            all_papers.extend(oa_papers)
        
        # Deduplicate by title similarity
        seen_titles = set()
        unique_papers = []
        for paper in all_papers:
            title_key = re.sub(r'[^a-z0-9]', '', paper.title.lower())[:50]
            if title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_papers.append(paper)
        
        # Filter by citations
        filtered = [p for p in unique_papers if p.citations >= min_citations]
        
        # Sort by citations
        filtered.sort(key=lambda p: p.citations, reverse=True)
        
        return filtered
    
    def citation_network(
        self,
        paper_id: str,
        depth: int = 1,
        direction: str = "both",
        limit_per_level: int = 20
    ) -> CitationNetwork:
        """
        Build citation network around an anchor paper.
        
        Args:
            paper_id: Semantic Scholar ID or DOI
            depth: How many citation levels to traverse
            direction: 'citing', 'cited', or 'both'
            limit_per_level: Max papers per level
        
        Returns:
            CitationNetwork object
        """
        anchor = self.ss.get_paper(paper_id)
        if not anchor:
            raise ValueError(f"Could not find paper: {paper_id}")
        
        foundations = []
        descendants = []
        
        if direction in ["cited", "both"]:
            foundations = self.ss.get_references(paper_id, limit=limit_per_level)
        
        if direction in ["citing", "both"]:
            descendants = self.ss.get_citations(paper_id, limit=limit_per_level)
        
        # Sort by citations
        foundations.sort(key=lambda p: p.citations, reverse=True)
        descendants.sort(key=lambda p: p.citations, reverse=True)
        
        return CitationNetwork(
            anchor=anchor,
            foundations=foundations[:limit_per_level],
            descendants=descendants[:limit_per_level]
        )
    
    def trace_lineage(
        self,
        anchor_paper: str,
        include_foundations: bool = True,
        include_descendants: bool = True,
        foundation_threshold: int = 100,  # Min citations for foundations
        descendant_recency: int = 3  # Years for recent descendants
    ) -> Dict:
        """
        Trace theoretical lineage of a concept through an anchor paper.
        
        Returns structured lineage with foundations, anchor, and frontier.
        """
        network = self.citation_network(
            anchor_paper,
            direction="both",
            limit_per_level=50
        )
        
        # Filter foundations to influential papers
        influential_foundations = [
            p for p in network.foundations 
            if p.citations >= foundation_threshold
        ]
        
        # Filter descendants to recent papers (frontier)
        current_year = datetime.now().year
        frontier = [
            p for p in network.descendants
            if p.year and p.year >= current_year - descendant_recency
        ]
        
        return {
            "anchor": network.anchor.to_dict(),
            "foundations": [p.to_dict() for p in influential_foundations[:10]],
            "frontier": [p.to_dict() for p in frontier[:10]],
            "total_descendants": len(network.descendants),
            "summary": f"Paper builds on {len(influential_foundations)} influential works and has {len(frontier)} recent extensions"
        }
    
    def identify_gaps(
        self,
        papers: List[Paper],
        dimensions: List[str] = ["platform", "method", "construct", "population"]
    ) -> List[ResearchGap]:
        """
        Identify research gaps from a set of papers.
        
        This is a simplified heuristic approach—full gap analysis
        requires human judgment.
        """
        gaps = []
        
        # Extract abstracts for analysis
        texts = [p.abstract or p.title for p in papers]
        combined = " ".join(texts).lower()
        
        # Platform coverage heuristics
        platforms = {
            "twitter": ["twitter", "tweet", "x.com"],
            "facebook": ["facebook", "meta", "fb"],
            "instagram": ["instagram", "ig"],
            "tiktok": ["tiktok", "douyin"],
            "youtube": ["youtube"],
            "reddit": ["reddit"],
            "telegram": ["telegram"],
            "whatsapp": ["whatsapp"]
        }
        
        platform_counts = {}
        for platform, keywords in platforms.items():
            count = sum(1 for kw in keywords if kw in combined)
            platform_counts[platform] = count
        
        # Find understudied platforms
        studied = [p for p, c in platform_counts.items() if c > 0]
        understudied = [p for p, c in platform_counts.items() if c == 0]
        
        if understudied:
            gaps.append(ResearchGap(
                dimension="platform",
                gap_description=f"Limited research on: {', '.join(understudied[:3])}",
                evidence=[f"{p}: {c} mentions" for p, c in platform_counts.items()],
                opportunity=f"Replicate existing findings on {understudied[0]}",
                priority="medium"
            ))
        
        # Method coverage heuristics
        methods = {
            "llm": ["llm", "gpt", "chatgpt", "claude", "large language model"],
            "content_analysis": ["content analysis", "coding", "codebook"],
            "network_analysis": ["network analysis", "social network", "graph"],
            "experiment": ["experiment", "rct", "randomized"],
            "survey": ["survey", "questionnaire"],
            "interview": ["interview", "qualitative"]
        }
        
        method_counts = {}
        for method, keywords in methods.items():
            count = sum(1 for kw in keywords if kw in combined)
            method_counts[method] = count
        
        if method_counts.get("llm", 0) == 0:
            gaps.append(ResearchGap(
                dimension="method",
                gap_description="No papers using LLM-based methods",
                evidence=["LLM/GPT/Claude keywords not found in corpus"],
                opportunity="Apply LLM content analysis to existing research questions",
                priority="high"
            ))
        
        return gaps
    
    def generate_review(
        self,
        papers: List[Paper],
        structure: str = "thematic",
        style: str = "apa7",
        max_papers: int = 20
    ) -> str:
        """
        Generate a literature review draft from papers.
        
        Args:
            papers: List of papers to synthesize
            structure: 'thematic', 'chronological', or 'methodological'
            style: Citation style
            max_papers: Max papers to include
        
        Returns:
            Markdown-formatted review draft
        """
        papers = papers[:max_papers]
        
        lines = []
        lines.append("## Literature Review Draft")
        lines.append("")
        lines.append(f"*Generated from {len(papers)} papers. Requires human editing.*")
        lines.append("")
        
        if structure == "chronological":
            papers_sorted = sorted(papers, key=lambda p: p.year)
            
            lines.append("### Chronological Development")
            lines.append("")
            
            current_period = None
            for paper in papers_sorted:
                period = f"{(paper.year // 5) * 5}s"
                if period != current_period:
                    lines.append(f"\n#### {period}")
                    current_period = period
                
                lines.append(f"- {paper.to_citation(style)} [Citations: {paper.citations}]")
        
        elif structure == "thematic":
            # Group by citation count (proxy for influence)
            influential = [p for p in papers if p.citations >= 100]
            moderate = [p for p in papers if 20 <= p.citations < 100]
            recent = [p for p in papers if p.citations < 20]
            
            if influential:
                lines.append("### Foundational Works")
                lines.append("")
                for paper in influential[:5]:
                    lines.append(f"**{paper.to_citation(style)}** (Citations: {paper.citations})")
                    if paper.abstract:
                        lines.append(f"> {paper.abstract[:200]}...")
                    lines.append("")
            
            if moderate:
                lines.append("### Key Contributions")
                lines.append("")
                for paper in moderate[:5]:
                    lines.append(f"- {paper.to_citation(style)} [Citations: {paper.citations}]")
                lines.append("")
            
            if recent:
                lines.append("### Recent Developments")
                lines.append("")
                for paper in recent[:5]:
                    lines.append(f"- {paper.to_citation(style)} [Citations: {paper.citations}]")
        
        lines.append("")
        lines.append("---")
        lines.append("*Note: This is an auto-generated draft. Verify citations, add synthesis, and check for accuracy.*")
        
        return "\n".join(lines)
    
    def export_bibtex(self, papers: List[Paper]) -> str:
        """Export papers to BibTeX format."""
        entries = []
        for i, paper in enumerate(papers):
            author_key = paper.authors[0].split()[-1].lower() if paper.authors else "unknown"
            key = f"{author_key}{paper.year}_{i}"
            
            entry = f"""@article{{{key},
  title = {{{paper.title}}},
  author = {{{' and '.join(paper.authors)}}},
  year = {{{paper.year}}},
  journal = {{{paper.venue or 'Unknown'}}},
  doi = {{{paper.doi or ''}}},
  note = {{Citations: {paper.citations}}}
}}"""
            entries.append(entry)
        
        return "\n\n".join(entries)


if __name__ == "__main__":
    # Demo
    lit = LiteratureSynthesis()
    
    print("=== Searching for 'framing social media protest' ===")
    papers = lit.search(
        query="framing social media protest",
        years=(2018, 2026),
        min_citations=10,
        limit=10
    )
    
    for p in papers[:5]:
        print(f"- [{p.citations}] {p.title[:60]}... ({p.year})")
    
    print("\n=== Generating Review Draft ===")
    draft = lit.generate_review(papers, structure="thematic")
    print(draft[:1000])
