# Global South AI Governance Framing Study

## Research Question
How do Global South nations frame artificial intelligence in legislative discourse compared to the United States?

## Countries
| Country | Data Source | Documents | Type |
|---------|-------------|-----------|------|
| 🇺🇸 USA | GovInfo (Congress) | 192 | Committee hearings |
| 🇿🇦 South Africa | PMG.org.za | 41 | Committee meetings |
| 🇧🇷 Brazil | Câmara API | 54 | Legislative proposals |

## Data Collection Summary

### South Africa (Complete)
- **Source:** Parliamentary Monitoring Group (pmg.org.za)
- **Method:** Scraped search results for "artificial intelligence"
- **Total indexed:** 370 committee meetings
- **AI filtering:** 
  - HIGH: 13 (3.5%)
  - MEDIUM: 28 (7.6%)
  - LOW: 329 (88.9%)
- **Valid for coding:** 41 meetings
- **Date range:** 2017-2025
- **Language:** English

### Brazil (Complete)
- **Source:** Câmara dos Deputados Open Data API
- **Method:** API search for AI-related keywords
- **Total propositions:** 54 (direct AI legislation)
- **AI events:** 63 committee events
- **Date range:** 2020-2026
- **Language:** Portuguese
- **Key legislation:**
  - PL 2338/2023: Marco Legal da IA (main AI framework)
  - PL 974/2026: AI governance
  - PL 904/2026: AI transparency & auditability
  - PL 762/2026: High-consequence AI regulation

## Coding Scheme

Adapted from US Congressional AI Framing study (8 frames):

| Frame | Definition | Keywords |
|-------|------------|----------|
| INNOVATION | Economic opportunity, competitiveness, growth | innovation, competitiveness, development, growth |
| RISK_SAFETY | Existential/catastrophic threats | existential, catastrophic, control, alignment |
| RISK_HARM | Concrete harms (children, users, vulnerable) | harm, abuse, manipulation, misinformation |
| RISK_ECONOMIC | Job loss, inequality, displacement | jobs, unemployment, inequality, workers |
| GOVERNANCE | Regulatory approaches, oversight | regulation, oversight, audit, compliance |
| SOVEREIGNTY | National security, geopolitical competition | sovereignty, security, China, defense |
| RIGHTS | Privacy, discrimination, civil liberties | privacy, discrimination, bias, rights |
| TECHNICAL | Scientific explanations, technical standards | algorithm, model, training, data |

### Country-Specific Adaptations

**South Africa:**
- 4IR (Fourth Industrial Revolution) framing
- Digital inclusion / rural access
- Skills development
- Unemployment context (high baseline)

**Brazil:**
- Marco Civil da Internet precedent
- Data protection (LGPD alignment)
- Small business / SIMPLES considerations
- Social media regulation context

## Methodology

### Multi-Model Validation
Same approach as US study:
1. **Claude** (primary coder)
2. **Kimi** (validation)
3. Inter-coder reliability: κ ≥ 0.60 threshold

### Batch Structure
- 25 documents per batch (Kimi limit)
- South Africa: 2 batches (41 meetings)
- Brazil: 3 batches (54 propositions)

## File Locations
```
/root/.openclaw/workspace/projects/global-south-ai-framing/
├── STUDY_DESIGN.md           # This file
├── scripts/
│   ├── scrape_pmg.py         # SA scraper
│   ├── scrape_brazil.py      # Brazil scraper
│   └── filter_sa_transcripts.py
├── data/
│   ├── south-africa/
│   │   ├── meetings_index.json
│   │   ├── valid_ai_meetings.json
│   │   ├── ai_analysis.json
│   │   └── transcripts/
│   └── brazil/
│       ├── proposicoes_index.json
│       ├── proposicoes_detailed.json
│       └── eventos_ai.json
├── prompts/
│   └── commdaaf_global_south.md
└── outputs/
    ├── south-africa/
    └── brazil/
```

## Timeline
- [x] Data collection: South Africa
- [x] Data collection: Brazil  
- [ ] Create coding batches
- [ ] Claude coding: SA
- [ ] Claude coding: Brazil
- [ ] Kimi validation
- [ ] Comparative analysis
- [ ] Paper writing

## Expected Contributions
1. First systematic comparison of AI policy framing across Global South
2. Test of CommDAAF methodology on non-English (Portuguese) content
3. Insights on whether AI governance discourse is converging globally
