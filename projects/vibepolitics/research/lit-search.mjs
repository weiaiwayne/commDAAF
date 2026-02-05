#!/usr/bin/env node
/**
 * VibePolitics Literature Search Pipeline
 * Uses Semantic Scholar + Scopus APIs to find and organize relevant papers
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';

// Load API keys
const secrets = JSON.parse(readFileSync('/root/.openclaw/secrets/scholarly-apis.json', 'utf8'));
const SS_API_KEY = secrets.semantic_scholar;
const SCOPUS_API_KEY = secrets.scopus;

// Search queries organized by concept
const SEARCH_QUERIES = {
  // Core Theories
  "information_cascade": [
    "information cascade political behavior",
    "informational cascades elections voting",
    "Bikhchandani Hirshleifer Welch cascade"
  ],
  "threshold_models": [
    "threshold model collective behavior Granovetter",
    "collective action threshold tipping point"
  ],
  "elite_mass_opinion": [
    "elite mass opinion divergence",
    "Zaller public opinion formation",
    "opinion leaders political influence"
  ],
  "prediction_markets": [
    "prediction markets election forecasting accuracy",
    "betting markets polls comparison",
    "political prediction markets efficiency"
  ],
  "rational_inattention": [
    "rational inattention theory political",
    "information cost attention allocation",
    "Sims rational inattention"
  ],
  "cognitive_labor": [
    "cognitive labor information discovery",
    "information acquisition cost political",
    "attention allocation political information"
  ],
  "framing_effects": [
    "framing effects political opinion",
    "Chong Druckman framing",
    "media framing public opinion"
  ],
  "diffusion_innovations": [
    "diffusion innovations political Rogers",
    "opinion diffusion social networks",
    "political information spread"
  ],
  // Methodological
  "google_trends_elections": [
    "Google Trends election prediction",
    "search data political forecasting",
    "online search behavior voting"
  ],
  "multi_agent_forecasting": [
    "multi-agent system forecasting",
    "LLM agent political analysis",
    "ensemble prediction political"
  ],
  "opinion_shift_detection": [
    "opinion shift detection time series",
    "attitude change measurement",
    "public opinion dynamics"
  ]
};

// Rate limiting helper
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Semantic Scholar API
async function searchSemanticScholar(query, limit = 20) {
  const url = new URL('https://api.semanticscholar.org/graph/v1/paper/search');
  url.searchParams.set('query', query);
  url.searchParams.set('limit', limit);
  url.searchParams.set('fields', 'paperId,title,abstract,year,citationCount,authors,venue,externalIds,url');
  
  const response = await fetch(url.toString(), {
    headers: {
      'x-api-key': SS_API_KEY
    }
  });
  
  if (!response.ok) {
    console.error(`SS API error: ${response.status} ${response.statusText}`);
    return { data: [] };
  }
  
  return response.json();
}

// Scopus API
async function searchScopus(query, limit = 20) {
  const url = new URL('https://api.elsevier.com/content/search/scopus');
  url.searchParams.set('query', `TITLE-ABS-KEY(${query})`);
  url.searchParams.set('count', limit);
  url.searchParams.set('sort', 'citedby-count');
  
  const response = await fetch(url.toString(), {
    headers: {
      'X-ELS-APIKey': SCOPUS_API_KEY,
      'Accept': 'application/json'
    }
  });
  
  if (!response.ok) {
    console.error(`Scopus API error: ${response.status} ${response.statusText}`);
    const text = await response.text();
    console.error(text.slice(0, 500));
    return { 'search-results': { entry: [] } };
  }
  
  return response.json();
}

// Process Semantic Scholar results
function processSSResults(results, concept) {
  if (!results.data) return [];
  
  return results.data.map(paper => ({
    source: 'semantic_scholar',
    concept: concept,
    paperId: paper.paperId,
    title: paper.title,
    authors: paper.authors?.map(a => a.name).join(', ') || 'Unknown',
    year: paper.year,
    venue: paper.venue || 'Unknown',
    citations: paper.citationCount || 0,
    abstract: paper.abstract?.slice(0, 500) || '',
    doi: paper.externalIds?.DOI || null,
    url: paper.url || `https://www.semanticscholar.org/paper/${paper.paperId}`
  }));
}

// Process Scopus results
function processScopusResults(results, concept) {
  const entries = results['search-results']?.entry || [];
  
  return entries.map(paper => ({
    source: 'scopus',
    concept: concept,
    paperId: paper['dc:identifier'] || null,
    title: paper['dc:title'] || 'Unknown',
    authors: paper['dc:creator'] || 'Unknown',
    year: paper['prism:coverDate']?.slice(0, 4) || null,
    venue: paper['prism:publicationName'] || 'Unknown',
    citations: parseInt(paper['citedby-count']) || 0,
    abstract: paper['dc:description'] || '',
    doi: paper['prism:doi'] || null,
    url: paper['prism:url'] || null
  }));
}

// Deduplicate by DOI or title similarity
function deduplicatePapers(papers) {
  const seen = new Map();
  const unique = [];
  
  for (const paper of papers) {
    // Key by DOI if available, else normalized title
    const key = paper.doi || paper.title.toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 50);
    
    if (!seen.has(key)) {
      seen.set(key, true);
      unique.push(paper);
    }
  }
  
  return unique;
}

// Main search function
async function runSearch() {
  console.log('🔍 VibePolitics Literature Search Pipeline');
  console.log('=========================================\n');
  
  const allPapers = [];
  const conceptResults = {};
  
  for (const [concept, queries] of Object.entries(SEARCH_QUERIES)) {
    console.log(`\n📚 Searching: ${concept}`);
    conceptResults[concept] = [];
    
    for (const query of queries) {
      console.log(`   Query: "${query}"`);
      
      // Search Semantic Scholar
      try {
        const ssResults = await searchSemanticScholar(query, 15);
        const ssPapers = processSSResults(ssResults, concept);
        console.log(`   └─ Semantic Scholar: ${ssPapers.length} papers`);
        conceptResults[concept].push(...ssPapers);
        allPapers.push(...ssPapers);
      } catch (e) {
        console.error(`   └─ SS Error: ${e.message}`);
      }
      
      await sleep(200); // Rate limit
      
      // Search Scopus
      try {
        const scopusResults = await searchScopus(query, 10);
        const scopusPapers = processScopusResults(scopusResults, concept);
        console.log(`   └─ Scopus: ${scopusPapers.length} papers`);
        conceptResults[concept].push(...scopusPapers);
        allPapers.push(...scopusPapers);
      } catch (e) {
        console.error(`   └─ Scopus Error: ${e.message}`);
      }
      
      await sleep(300); // Rate limit
    }
  }
  
  // Deduplicate
  console.log('\n🔄 Deduplicating...');
  const uniquePapers = deduplicatePapers(allPapers);
  console.log(`   Total: ${allPapers.length} → Unique: ${uniquePapers.length}`);
  
  // Sort by citations
  uniquePapers.sort((a, b) => b.citations - a.citations);
  
  // Filter high-impact (>50 citations or recent <2022)
  const highImpact = uniquePapers.filter(p => 
    p.citations >= 50 || (p.year && parseInt(p.year) >= 2022)
  );
  console.log(`   High-impact papers: ${highImpact.length}`);
  
  // Save results
  const outputPath = '/root/.openclaw/workspace/projects/vibepolitics/research/literature_search_results.json';
  writeFileSync(outputPath, JSON.stringify({
    searchDate: new Date().toISOString(),
    totalFound: allPapers.length,
    uniquePapers: uniquePapers.length,
    highImpactPapers: highImpact.length,
    bySource: {
      semantic_scholar: uniquePapers.filter(p => p.source === 'semantic_scholar').length,
      scopus: uniquePapers.filter(p => p.source === 'scopus').length
    },
    papers: uniquePapers,
    highImpact: highImpact
  }, null, 2));
  console.log(`\n✅ Results saved to: ${outputPath}`);
  
  // Generate markdown summary
  generateMarkdownSummary(uniquePapers, conceptResults);
  
  return uniquePapers;
}

// Generate readable markdown summary
function generateMarkdownSummary(papers, conceptResults) {
  let md = `# Literature Search Results
*Generated: ${new Date().toISOString()}*

## Summary
- **Total papers found:** ${papers.length}
- **High-citation (≥50):** ${papers.filter(p => p.citations >= 50).length}
- **Recent (≥2022):** ${papers.filter(p => p.year >= 2022).length}

---

## Top 30 Most-Cited Papers

| # | Title | Authors | Year | Citations | Venue |
|---|-------|---------|------|-----------|-------|
`;

  papers.slice(0, 30).forEach((p, i) => {
    const title = p.title.length > 60 ? p.title.slice(0, 57) + '...' : p.title;
    const authors = p.authors.length > 30 ? p.authors.slice(0, 27) + '...' : p.authors;
    const venue = p.venue.length > 25 ? p.venue.slice(0, 22) + '...' : p.venue;
    md += `| ${i+1} | ${title} | ${authors} | ${p.year || '?'} | ${p.citations} | ${venue} |\n`;
  });

  md += `\n---\n\n## Papers by Concept\n\n`;

  for (const [concept, conceptPapers] of Object.entries(conceptResults)) {
    const unique = deduplicatePapers(conceptPapers);
    const sorted = unique.sort((a, b) => b.citations - a.citations).slice(0, 10);
    
    md += `### ${concept.replace(/_/g, ' ').toUpperCase()}\n\n`;
    
    if (sorted.length === 0) {
      md += `*No papers found*\n\n`;
      continue;
    }
    
    sorted.forEach((p, i) => {
      md += `${i+1}. **${p.title}** (${p.year || '?'})\n`;
      md += `   - Authors: ${p.authors}\n`;
      md += `   - Citations: ${p.citations} | Venue: ${p.venue}\n`;
      if (p.doi) md += `   - DOI: ${p.doi}\n`;
      md += `\n`;
    });
    
    md += `\n`;
  }

  md += `---\n\n## BibTeX Export (Top 20)\n\n\`\`\`bibtex\n`;
  
  papers.slice(0, 20).forEach((p, i) => {
    const key = p.authors.split(',')[0]?.replace(/[^a-zA-Z]/g, '') || 'Unknown';
    md += `@article{${key}${p.year || 'nd'},
  title = {${p.title}},
  author = {${p.authors}},
  year = {${p.year || 'n.d.'}},
  journal = {${p.venue}},
  doi = {${p.doi || 'N/A'}}
}\n\n`;
  });
  
  md += `\`\`\`\n`;

  const mdPath = '/root/.openclaw/workspace/projects/vibepolitics/research/LITERATURE_SEARCH_RESULTS.md';
  writeFileSync(mdPath, md);
  console.log(`📝 Markdown summary saved to: ${mdPath}`);
}

// Run
runSearch().catch(console.error);
