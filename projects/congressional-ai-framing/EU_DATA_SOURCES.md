# EU Parliamentary Data Sources for Comparative AI Framing Study

**Compiled:** March 12, 2026  
**Purpose:** Identify free, public data sources for EU AI discourse comparable to U.S. congressional hearings

---

## 🏆 TOP RECOMMENDED SOURCES

### 1. EUPDCorp — Corpus of EU Parliament Debates (1999-2024)
**URL:** https://zenodo.org/records/15056399  
**Format:** Structured dataset  
**Size:** 563,696 speeches  
**Coverage:** 1999-2024 (25 years)  
**Access:** Free download (Zenodo)  
**License:** Open  

**Why it's ideal:**
- Direct equivalent to congressional hearings (EU Parliament plenary debates)
- Already structured with metadata (speaker, date, topic)
- Searchable for "artificial intelligence" mentions
- Recent (includes AI Act debates 2023-2024)

**Potential search terms:** "artificial intelligence", "AI", "machine learning", "algorithmic", "automation"

---

### 2. ParlaMint 5.0 — Multilingual Parliamentary Corpora
**URL:** https://www.clarin.eu/parlamint  
**Download:** http://hdl.handle.net/11356/2004  
**Format:** TEI XML (linguistically annotated)  
**Size:** 1+ billion words  
**Coverage:** 29 countries/regions  
**Access:** Free (CC BY license)  

**Key features:**
- **EU Parliament** included alongside national parliaments
- Named entity recognition already applied
- Speaker metadata (party, role, gender)
- Linguistically annotated (POS, lemmas)
- GitHub tools for processing: https://github.com/clarin-eric/ParlaMint/

**Countries included:** Austria, Belgium, Bulgaria, Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Lithuania, Netherlands, Norway, Poland, Portugal, Romania, Serbia, Slovakia, Slovenia, Spain, Sweden, Turkey, UK

**Best for:** Cross-national comparison (not just EU Parliament vs US Congress)

---

### 3. Hugging Face: coastalcph/eu_debates
**URL:** https://huggingface.co/datasets/coastalcph/eu_debates  
**Format:** Hugging Face Dataset (Python-ready)  
**Access:** Free, one-line load  

```python
from datasets import load_dataset
eu_debates = load_dataset('coastalcph/eu_debates', split='train')
```

**Why it's useful:**
- Instantly loadable in Python
- Already used for LLM political analysis research
- Easy to filter by keywords

---

### 4. European Parliament Open Data Portal API
**URL:** https://data.europarl.europa.eu/en/developer-corner/opendata-api  
**Format:** REST API (JSON/XML)  
**Access:** Free, no key required  

**Endpoints include:**
- Plenary debates (verbatim reports)
- Committee meetings
- Parliamentary questions
- Legislative documents
- MEP information

**Advantage:** Real-time access to most recent data (2025-2026)

---

### 5. DCEP — Digital Corpus of European Parliament
**URL:** https://joint-research-centre.ec.europa.eu/language-technology-resources/dcep-digital-corpus-european-parliament_en  
**Provider:** EU Joint Research Centre  
**Format:** Multilingual parallel corpus  
**Coverage:** EP documents in 24 languages  

**Use case:** If multilingual analysis is needed

---

## 📊 COMPARISON: US vs EU Data

| Aspect | US (GovInfo) | EU (EUPDCorp) |
|--------|--------------|---------------|
| Institution | Congress (House + Senate) | European Parliament |
| Document type | Hearing transcripts | Plenary debate speeches |
| Time range | 2007-2026 | 1999-2024 |
| Size | 192 filtered hearings | 563,696 speeches |
| Format | PDF/HTML transcripts | Structured CSV/XML |
| Granularity | Full hearing | Individual speeches |
| AI search | "artificial intelligence" | Same + "AI Act" specific |

---

## 🔬 RECOMMENDED APPROACH

### Option A: Direct Comparison (EP Plenary vs Congress)
1. **US:** Use existing 192 hearing dataset
2. **EU:** Download EUPDCorp, filter for AI-related speeches
3. **Match:** Same time period (2007-2024), same search terms
4. **Advantage:** Clean institutional comparison

### Option B: Expanded EU (National Parliaments)
1. **US:** Existing dataset
2. **EU:** ParlaMint (Germany, France, etc.)
3. **Advantage:** See if framing differs by EU member state
4. **Challenge:** More complexity, language issues

### Option C: Focus on AI Act Period
1. **Time:** 2021-2024 (AI Act legislative process)
2. **US:** ChatGPT era hearings (our strongest data)
3. **EU:** AI Act debates specifically
4. **Advantage:** Most comparable policy moment

---

## 📥 NEXT STEPS TO COLLECT EU DATA

### Step 1: Download EUPDCorp
```bash
# From Zenodo (need to check access)
wget https://zenodo.org/records/15056399/files/EUPDCorp_v1.zip
```

### Step 2: Filter for AI mentions
```python
import pandas as pd

# Load corpus
df = pd.read_csv('eupdcorp_speeches.csv')

# AI-related keywords
ai_terms = ['artificial intelligence', 'AI', 'machine learning', 
            'algorithm', 'automated decision', 'AI Act', 'ChatGPT',
            'neural network', 'deep learning']

# Filter
ai_speeches = df[df['text'].str.contains('|'.join(ai_terms), case=False, na=False)]
print(f"Found {len(ai_speeches)} AI-related speeches")
```

### Step 3: Apply same 8-frame coding scheme
Use CommDAAF with identical prompts to ensure comparability.

---

## ⚠️ LIMITATIONS TO CONSIDER

1. **Institutional difference:** EP plenary debates ≠ Congressional hearings
   - Hearings have witnesses; plenary debates are MEP-only
   - Consider: Would EP committee hearings be more comparable?

2. **Language:** EU debates in 24 languages
   - English versions available but may lose nuance
   - Consider: Focus on English-language debates or use translation

3. **Political structure:** 
   - US: Two parties dominate
   - EU: Multiple party groups, coalition dynamics
   - Consider: Code party/group alongside frames

4. **AI Act focus:** EU had a specific legislative process
   - Most AI discourse may be AI Act-specific (2021-2024)
   - US had no equivalent single legislation
   - Consider: Control for this in analysis

---

## 📚 PRIOR WORK

**Suter (2025)** — "When Politicians Talk AI: Issue-Frames in Parliamentary Debates Before and After ChatGPT"
- Already compared EP, Swiss Parliament, Singapore, US Congress
- Used verbatim transcripts from EP Plenary Service
- Could be useful methodological reference

**URL:** https://onlinelibrary.wiley.com/doi/full/10.1002/poi3.70010

---

*Document prepared for CommDAAF comparative study planning*
