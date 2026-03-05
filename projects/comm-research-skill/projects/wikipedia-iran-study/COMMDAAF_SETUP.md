# CommDAAF Setup for Wikipedia Epistemic Contestation Study

*Ensuring multi-model validation with proper configuration*

---

## Pre-Study Checklist ✓

### API Access Configuration

| Model | Access Method | Status |
|-------|---------------|--------|
| **Claude** | Direct Anthropic API | ✅ Active (current session) |
| **GLM-4.7** | `opencode -m zai-coding-plan/glm-4.7` | ⬜ To verify |
| **Kimi K2.5** | `kimi-coding/k2p5` via OpenCode | ⬜ To verify |

### ⚠️ DO NOT USE
- ❌ OpenRouter (billing model mismatch)
- ❌ Mei agent (routes through OpenRouter)
- ❌ Free proxies (may have content filters for Iran content)

---

## Study Parameters

### Validation Tier
**🟡 PILOT** — Preprint-ready, multi-model validation

### Research Question
**How do Wikipedia editors engage in epistemic contestation during geopolitical conflict, and what forms of epistemic injustice emerge?**

### Constructs (Grounded in Theory)

| Construct | Definition | Source |
|-----------|------------|--------|
| **Testimonial Injustice** | Speaker's credibility discounted due to identity/prejudice | Fricker 2007 |
| **Hermeneutical Injustice** | Systemic absence of interpretive resources | Fricker 2007 |
| **Epistemic Dispossession** | Platform structures extract/redistribute epistemic resources | Kwok 2025 |
| **Policy Weaponization** | Using Wikipedia policies (NPOV, RS, UNDUE) to delegitimize | Ajmani et al. 2024 |
| **Naming Dispute** | Contestation over terminology (war vs conflict) | Entman 1993 |
| **Source Hierarchy** | Arguments about source reliability/hierarchy | Wikipedia RS policy |

---

## Multi-Model Coding Protocol

### Phase 1: Coding Scheme Development

1. **Draft codebook** based on theoretical framework
2. **Pilot on 20 excerpts** with Claude
3. **Refine** based on problematic cases
4. **Lock codebook** before multi-model deployment

### Phase 2: Independent Coding

Each model codes **same 100 talk page excerpts** independently:

```bash
# Claude (direct - this session)
# [Claude codes via current conversation]

# GLM-4.7 (via OpenCode with PTY)
opencode -m zai-coding-plan/glm-4.7 run "
Load the CommDAAF coding scheme from projects/comm-research-skill/projects/wikipedia-iran-study/CODEBOOK.md
Code the following Wikipedia talk page excerpt for epistemic injustice indicators:
[EXCERPT]
Output JSON: {testimonial_injustice, hermeneutical_injustice, epistemic_dispossession, policy_weaponization, naming_dispute, source_hierarchy, confidence}
"

# Kimi K2.5 (via OpenCode)
opencode -m kimi-coding/k2p5 run "
[Same prompt as GLM]
"
```

### Phase 3: Reliability Assessment

Calculate per-construct agreement:

| Metric | Formula | Threshold |
|--------|---------|-----------|
| **Overall κ** | Cohen's kappa (3-way) | ≥ 0.60 |
| **Per-construct κ** | Individual construct agreement | Report all |
| **Convergence rate** | % where all 3 agree | ≥ 70% |

**Flag constructs with κ < 0.50** — may need redefinition.

### Phase 4: Disagreement Resolution

| Disagreement Type | Resolution |
|-------------------|------------|
| 2 agree, 1 disagrees | Majority rules |
| All 3 disagree | Human adjudication |
| Low-confidence codes | Human review |

---

## Data Pipeline

### Step 1: Wikipedia API Collection

```python
import requests
import json

def get_revision_history(article_title, limit=500):
    """Fetch revision history for a Wikipedia article."""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": article_title,
        "prop": "revisions",
        "rvprop": "ids|timestamp|user|comment|size",
        "rvlimit": limit,
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_talk_page(article_title):
    """Fetch talk page content."""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": f"Talk:{article_title}",
        "prop": "wikitext",
        "format": "json"
    }
    response = requests.get(url, params=params)
    return response.json()
```

### Step 2: Data Storage Structure

```
projects/wikipedia-iran-study/
├── data/
│   ├── iran_cluster/
│   │   ├── revisions/          # Revision histories
│   │   ├── talk_pages/         # Talk page content
│   │   └── metadata.json       # Article metadata
│   └── gaza_cluster/
│       ├── revisions/
│       ├── talk_pages/
│       └── metadata.json
├── coding/
│   ├── CODEBOOK.md             # Finalized coding scheme
│   ├── excerpts.json           # Sampled excerpts for coding
│   ├── claude_codes.json       # Claude's coding output
│   ├── glm_codes.json          # GLM's coding output
│   ├── kimi_codes.json         # Kimi's coding output
│   └── reliability.json        # Inter-model agreement
├── analysis/
│   ├── networks/               # Revert network data
│   ├── temporal/               # Time-series data
│   └── integrated/             # Combined findings
└── outputs/
    ├── PREPRINT.md             # Draft preprint
    └── figures/                # Visualizations
```

---

## Prompt Templates

### Coding Prompt (All Models)

```markdown
# Wikipedia Talk Page Epistemic Injustice Coding

You are coding Wikipedia talk page excerpts for forms of epistemic injustice.

## Codebook

### TESTIMONIAL_INJUSTICE
Definition: A speaker's credibility is discounted due to identity, experience level, or prejudicial stereotyping.
Examples:
- "You only have 50 edits, you don't understand how Wikipedia works"
- "That's a pro-Iran source, obviously biased"
- "New accounts shouldn't be commenting on contentious topics"

### HERMENEUTICAL_INJUSTICE
Definition: Systemic absence of interpretive resources to make sense of experience; lack of vocabulary or frameworks.
Examples:
- Disputes over whether "war" or "conflict" is the appropriate term
- Arguments that certain events cannot be named (e.g., "genocide")
- Missing categories for certain phenomena

### EPISTEMIC_DISPOSSESSION
Definition: Platform structures systematically extract or redistribute epistemic resources to benefit dominant groups.
Examples:
- Extended confirmed protection excluding new editors
- Consensus mechanisms favoring experienced editors
- Arbitration processes privileging certain camps

### POLICY_WEAPONIZATION
Definition: Using Wikipedia policies (NPOV, RS, UNDUE, SYNTHESIS) to delegitimize opposing viewpoints.
Examples:
- "This violates WP:UNDUE" to remove minority perspectives
- "Not a reliable source" to exclude non-Western media
- "WP:SYNTHESIS" to prevent connecting documented facts

### NAMING_DISPUTE
Definition: Explicit contestation over terminology (war vs conflict, massacre vs incident, genocide vs allegations).
Examples:
- "This should be called a 'conflict' not 'war'"
- "The term 'genocide' is POV"
- Arguments over article titles

### SOURCE_HIERARCHY
Definition: Arguments establishing hierarchies of source reliability, often along national/ideological lines.
Examples:
- "Iranian state media is not reliable"
- "Western sources are biased"
- Debates over Al Jazeera, Times of Israel, ISW, etc.

## Task

Code the following excerpt. Output JSON only.

## Excerpt
[INSERT EXCERPT]

## Output Format
{
  "testimonial_injustice": true/false,
  "hermeneutical_injustice": true/false,
  "epistemic_dispossession": true/false,
  "policy_weaponization": true/false,
  "naming_dispute": true/false,
  "source_hierarchy": true/false,
  "primary_form": "most_prominent_category_or_none",
  "confidence": 0.0-1.0,
  "reasoning": "brief explanation"
}
```

---

## Quality Control Checklist

### Before Multi-Model Coding
- [ ] Codebook finalized and locked
- [ ] 20+ pilot excerpts coded by human
- [ ] Ambiguous cases documented with decision rules
- [ ] All models tested with sample prompt

### During Coding
- [ ] Same excerpts sent to all models (verbatim)
- [ ] Model outputs logged with timestamps
- [ ] API errors documented

### After Coding
- [ ] Per-construct κ calculated and reported
- [ ] Low-agreement constructs flagged
- [ ] Disagreements adjudicated
- [ ] Final codes exported for analysis

---

## Model-Specific Notes

### Claude (Anthropic)
- Tends toward nuanced, hedged responses
- Good at identifying subtle testimonial injustice
- May over-identify hermeneutical injustice

### GLM-4.7 (via OpenCode)
- Strong on policy-related content
- May have different perspective on Western/non-Western sources
- **⚠️ Use via OpenCode only** (not direct z.ai for content-filtered topics)

### Kimi K2.5 (via OpenCode)
- **⚠️ 25-post batch limit** (truncates JSON otherwise)
- Good at technical Wikipedia policy analysis
- May have different framing of Iran-related content

### Diversity Value
Using US-based (Claude) + Chinese-based (GLM, Kimi) models provides:
- Different cultural perspectives on "neutrality"
- Cross-validation of framing interpretations
- Detection of systematic model bias

---

*Ready for data collection and coding upon approval.*
