# Critical Audit: Communication Research Skill

**Date:** 2026-02-17  
**Perspectives:** PM + User + Academic Researcher  
**Context:** Post-API age reality check

---

## Executive Summary

The system has strong methodological rigor but **critical gaps in the post-API data access reality**. Current architecture assumes API access as primary data source — this assumption is now **catastrophically wrong** for most social media platforms.

**Severity Ratings:**
- 🔴 Critical: Must fix before production
- 🟠 High: Should fix, affects adoption
- 🟡 Medium: Nice to have, improves UX
- 🟢 Low: Future enhancement

---

## 1. POST-API AGE DATA ACCESS (🔴 CRITICAL)

### The Problem

The entire data source architecture assumes researchers can **query APIs to collect data**. This was true in 2020. It's not true in 2026:

| Platform | API Status (2026) | Reality |
|----------|-------------------|---------|
| Twitter/X | $5K+/mo for meaningful access | Effectively dead for academics |
| Reddit | API pricing killed most research | Limited, expensive |
| Facebook/Meta | CrowdTangle dead, Content Library restricted | Requires application, waiting lists |
| TikTok | Research API exists | Heavily restricted, geofenced |
| Instagram | No research API | Essentially impossible |

### What's Missing

1. **Existing Dataset Workflows**
   - Most research now uses **pre-collected datasets** from archives
   - No guidance on finding, evaluating, citing existing data
   - No skill for "work with what exists vs collect new"

2. **Data Access Pathways**
   - No mention of **DSA Article 40** (EU law mandating research access)
   - No guidance on **academic data partnerships** (Social Science One, etc.)
   - No **ICWSM/AAAI shared tasks** datasets
   - No **data request templates** for platforms

3. **Alternative Collection Methods**
   - Scraping ethics/legality unclear
   - No browser extension data donation workflows
   - No survey-based data collection
   - No participant-shared data workflows

### Recommendation

Create `workflows/data-access-strategy.md`:
```markdown
# Data Access Decision Tree

## Before ANY project, ask:

1. Does a dataset already exist?
   → Check: ICPSR, Harvard Dataverse, Zenodo, DocNow
   → If yes: Use it (with citation)

2. Can you get access through official channels?
   → DSA Art. 40 request (EU platforms)
   → Meta Content Library application
   → TikTok Research API application
   → Academic consortium membership

3. Can you work with a platform partner?
   → X (Twitter) Academic Research partnerships
   → Reddit data partnerships

4. Do you need truly real-time data?
   → If no: existing datasets suffice
   → If yes: consider Bluesky, Mastodon (open protocols)

5. As last resort (with ethics review):
   → Browser extension with informed consent
   → User data donation
   → Survey-embedded collection
```

---

## 2. USER EXPERIENCE FRICTION (🟠 HIGH)

### The Probing Questions Problem

**Current state:** 6-7 mandatory questions before ANY analysis runs.

**User reality:** 
- Experienced researchers know what they want
- 7 questions feels like an interrogation, not assistance
- Researchers will abandon tool if it blocks them

### Evidence of Problem

From `PROBING_QUESTIONS.md`:
```
| Sentiment Analysis | 6 questions | All 6 required |
| Topic Modeling     | 7 questions | All 7 required |
```

An experienced researcher who's run 50 sentiment analyses doesn't need to answer "What do you mean by sentiment?" every time.

### Recommendation

**Tiered Engagement Model:**

```yaml
# config.yaml addition

researcher_profile:
  experience_level: novice | intermediate | expert
  verified_methods: []  # Methods they've demonstrated competence in

engagement_mode:
  novice:     full_probing       # All questions
  intermediate: spot_check       # Key questions only
  expert:     fast_track         # Specify params, skip quiz

# Fast track for experts
expert_request_format: |
  "Run sentiment analysis:
   - Tool: VADER
   - Unit: post-level
   - Neutral threshold: ±0.05
   - Sarcasm handling: flag and exclude
   - Validation: 200-item sample
   
   Confirm and proceed."
```

**Competence Caching:**
Once a researcher demonstrates understanding of a method, cache it:
```json
{
  "researcher_id": "wayne",
  "verified_competence": {
    "sentiment_analysis": "2026-02-15",
    "network_analysis": "2026-02-10"
  },
  "failed_competence": {
    "coordinated_behavior": "2026-02-12"  // Must re-verify
  }
}
```

---

## 3. MISSING METHODS (🟠 HIGH)

### Critical Gaps

| Method | Status | Priority |
|--------|--------|----------|
| **Frame Analysis** | Missing | High — core comm method |
| **Discourse Analysis** | Missing | High — qualitative turn |
| **Comparative Platform Analysis** | Missing | High — post-migration reality |
| **Longitudinal Analysis** | Missing | Medium — time-series guidance |
| **Mixed Methods** | Missing | High — qual-quant integration |
| **Survey Integration** | Missing | Medium — primary data |
| **Interview Coding** | Missing | Medium — qualitative support |

### Frame Analysis Especially

Frame analysis is **central to communication research** but completely absent. This is a significant gap:

```markdown
# Needed: methods/frame-analysis.md

## Types
- Media frames
- Audience frames  
- Frame building vs frame setting

## Methods
- Inductive (let frames emerge)
- Deductive (apply existing typology)
- LLM-assisted frame detection

## Key Decisions
- Unit (article, paragraph, sentence?)
- Frame inventory (create or adapt?)
- Coder training for abstract constructs
```

---

## 4. PLATFORM COVERAGE GAPS (🟠 HIGH)

### Missing Platforms

| Platform | Importance | Status |
|----------|------------|--------|
| **TikTok** | Critical | MISSING |
| **Instagram** | High | MISSING |
| **WhatsApp** | High for non-US research | MISSING |
| **Mastodon/Fediverse** | Growing | MISSING |
| **LinkedIn** | Professional/political | MISSING |
| **Discord** | Communities | MISSING |
| **Twitch** | Streaming politics | MISSING |

### TikTok is CRITICAL

TikTok is now **the dominant platform for political content** among young audiences. Having Twitter but not TikTok is a 2020 decision in 2026.

**Needed:** `data-sources/tiktok.md`
```markdown
# TikTok Research Options

## Official
- TikTok Research API (apply: developers.tiktok.com)
- Restrictions: US/EU researchers, approved topics only

## Datasets
- TikTok Videos Research Dataset (NUS)
- SharedTok collaborative archive

## Workarounds (with ethics)
- User-shared data with consent
- Public API limitations
```

---

## 5. REPRODUCIBILITY GAPS (🟡 MEDIUM)

### What's Missing

1. **Pre-registration Support**
   - No template for pre-registering computational studies
   - No guidance on what to pre-register (vs exploratory)
   - No OSF integration

2. **Version Control**
   - Scripts exist but no git workflow guidance
   - No requirements.txt / environment.yaml templates
   - No Docker containerization for true reproducibility

3. **Data Citation**
   - No standard format for citing datasets
   - No DOI generation workflow
   - No data availability statement templates

### Recommendation

Add `workflows/reproducibility.md`:
```markdown
# Reproducibility Checklist

## Pre-Registration (if confirmatory)
- [ ] Hypothesis registered before data access
- [ ] Analysis plan specified
- [ ] OSF/AsPredicted link

## Code
- [ ] All code in version control
- [ ] Environment specified (requirements.txt)
- [ ] Random seeds set and documented
- [ ] README with execution instructions

## Data
- [ ] Data citation with DOI
- [ ] Data availability statement
- [ ] If restricted: access instructions

## Methods
- [ ] Prompts in appendix (for LLM methods)
- [ ] Parameters documented
- [ ] Validation metrics reported
```

---

## 6. COLLABORATION GAPS (🟡 MEDIUM)

### Single-Researcher Assumption

The entire system assumes a single researcher working alone. Reality:

- Research teams
- PI + RAs
- Multi-site collaborations
- Co-authors with different skill levels

### Missing

1. **Role-based access**
   - PI sees everything
   - RA sees assigned tasks
   - Collaborator sees shared projects

2. **Handoff workflows**
   - "Here's where I left off"
   - Session continuity between people

3. **Review workflows**
   - Co-author review before publication
   - Advisor review of student work

---

## 7. ETHICAL/LEGAL GAPS (🟠 HIGH)

### What's Unclear

1. **Platform ToS Compliance**
   - Which collection methods violate ToS?
   - What are the risks?
   - When is ToS violation acceptable (public interest)?

2. **IRB/Ethics Board**
   - When is IRB required?
   - Template for IRB application
   - Exemption criteria

3. **Data Protection**
   - GDPR implications for EU data
   - Data retention policies
   - Anonymization requirements

4. **Publication Ethics**
   - Quoting public posts: consent needed?
   - Identifying accounts: when acceptable?
   - Platform notification requirements

### Recommendation

Add `workflows/ethics-compliance.md`:
```markdown
# Ethics Decision Tree

## Is IRB Required?
- Human subjects → likely yes
- Public data only → maybe exempt
- Analyzing without contact → possibly exempt
- Any intervention → definitely yes

## Data Protection
- EU subjects → GDPR applies
- Identifiable data → extra protections
- Sensitive topics → heightened scrutiny

## Publication
- Before quoting: is user identifiable?
- Before identifying: public figure exception?
- Before publishing: could this harm subjects?
```

---

## 8. DIFFERENTIATION FROM DAAF (🟡 MEDIUM)

### Current Weakness

If someone asks "why use this instead of DAAF?", the answer is unclear.

### Differentiation Strategy

| Feature | DAAF | Comm Research Skill |
|---------|------|---------------------|
| **Domain** | General data analysis | Communication research specific |
| **Rigor** | Trust user | Enforce methods standards |
| **Data Era** | API-centric | Post-API aware |
| **Epistemology** | Single model | Multi-model validation |
| **Theory** | Atheoretical | Communication theories built-in |
| **Output** | Analysis | Publication-ready methods sections |

### Key Differentiator: Publication-Ready Output

DAAF gives you results. This skill should give you:
- Methods section draft
- Limitations paragraph
- Proper citations
- Reproducibility materials

---

## 9. ONBOARDING FRICTION (🟡 MEDIUM)

### Current State

`ONBOARDING.md` assumes:
- User has Zotero API key
- User knows Python
- User can edit YAML
- User understands research methods terminology

### Reality

Many comm researchers:
- Use EndNote or Mendeley (not Zotero)
- Don't code
- Want GUI configuration
- Are students learning methods

### Recommendation

**Multiple Onboarding Paths:**

```markdown
# Choose Your Path

## Quick Start (I know what I'm doing)
→ Edit config.yaml directly
→ Run analysis

## Guided Setup (Help me configure)
→ Answer questions in chat
→ I'll build your config

## Learning Mode (Teach me)
→ Explain methods as we go
→ Extra documentation
→ Recommended readings
```

---

## 10. ERROR HANDLING & RECOVERY (🟡 MEDIUM)

### Missing

1. **What happens when API fails?**
   - Rate limits hit
   - Authentication expires
   - Platform blocks IP

2. **What happens when analysis fails?**
   - Script errors
   - Model API down
   - Unexpected data format

3. **Partial progress recovery**
   - Crashed after 10k of 100k items
   - How to resume?

### Recommendation

Add `workflows/error-recovery.md` with:
- Common errors and solutions
- Checkpoint/resume patterns
- Fallback strategies

---

## Summary: Priority Actions

### 🔴 Must Fix (Critical)

1. **Data Access Strategy** — Create realistic post-API workflows
2. **TikTok Data Source** — Platform is too important to ignore
3. **Ethics/Compliance Workflow** — Legal risks are real

### 🟠 Should Fix (High)

4. **Expert Fast-Track** — Don't interrogate experienced researchers
5. **Frame Analysis Method** — Core comm research method
6. **Existing Dataset Workflows** — Most research uses archived data

### 🟡 Nice to Have (Medium)

7. **Reproducibility Workflow** — Pre-reg, version control, containers
8. **Collaboration Support** — Teams, handoffs, reviews
9. **Multiple Onboarding Paths** — Don't assume technical users
10. **Error Recovery** — Graceful failures

---

## Competitive Position After Fixes

If we address critical gaps, this becomes:

> The only AI research assistant designed for the **post-API era**, with built-in **methodological rigor enforcement** and **multi-model epistemics** for communication research.

That's a unique value proposition DAAF can't claim.
