# Layered Coding Schemes

**Source:** Nonprofit Mission Framing Study (Mar 2026)  
**Problem Solved:** Detecting *diffusion* of language patterns rather than binary presence/absence

---

## When to Use

Traditional mutually-exclusive coding schemes miss **hybrid cases** where new language *layers onto* existing orientations rather than replacing them. Use layered coding when studying:

- Institutional diffusion (e.g., "technocratic language in nonprofits")
- Language adoption patterns (e.g., "DEI language in corporate communications")
- Frame mixing (e.g., "populist rhetoric in mainstream parties")
- Identity transformation (e.g., "professionalization in volunteer orgs")

## Two-Level Structure

### Level 1: Primary Category (What They Do)
Mutually exclusive base classification:
```
SERVICE | CAPACITY | ADVOCACY | FELLOWSHIP | RESEARCH
```

### Level 2: Modifiers (How They Describe It)
Non-exclusive binary flags applied ON TOP of primary:
```
OUTCOME_ORIENTED | PROFESSIONAL | EFFICIENCY | ACCOUNTABILITY | EVIDENCE_BASED
```

## Coding Example

**Mission:** "To transform the lives of at-risk youth through education and mentorship, achieving measurable improvements in academic performance."

| Level | Code | Reasoning |
|-------|------|-----------|
| Primary | SERVICE | Directly serves beneficiaries (youth) |
| Modifier | OUTCOME_ORIENTED | "transform," "measurable improvements" |

**Result:** SERVICE + OUTCOME_ORIENTED (captures diffusion)

## Why This Works

| Approach | Detects | Misses |
|----------|---------|--------|
| Binary (technocratic Y/N) | Orgs ABOUT measurement | Technocratic language IN service orgs |
| Mutually exclusive | What orgs do | How they describe it |
| **Layered** | Both function AND framing | — |

## Implementation

```python
def code_mission(text: str) -> dict:
    # Step 1: Primary frame (mutually exclusive)
    primary = classify_primary(text)  # SERVICE, CAPACITY, etc.
    
    # Step 2: Technocratic modifiers (non-exclusive)
    modifiers = {
        "OUTCOME_ORIENTED": has_outcome_language(text),
        "PROFESSIONAL": has_professional_language(text),
        "EFFICIENCY": has_efficiency_language(text),
        "ACCOUNTABILITY": has_accountability_language(text),
        "EVIDENCE_BASED": has_evidence_language(text),
    }
    
    return {
        "primary_frame": primary,
        "modifiers": [k for k, v in modifiers.items() if v],
        "technocratic_any": any(modifiers.values()),
    }
```

## Key Finding from Source Study

- 55.7% of nonprofits coded as SERVICE (primary frame dominant)
- But 15.1% had technocratic modifiers layered on top
- Large orgs showed 4× higher modifier adoption (41.3% vs 9.5%)
- **Insight:** Technocratic language diffuses INTO service missions, doesn't replace them

## Bright-Line Rules for Modifiers

| Modifier | Trigger Terms | NOT Triggered By |
|----------|---------------|------------------|
| OUTCOME_ORIENTED | "outcomes," "impact," "results," "transform," "measurable" | "help," "serve," "support" |
| PROFESSIONAL | "excellence," "quality," "standards," "best practices" | Competence claims without jargon |
| EFFICIENCY | "efficient," "cost-effective," "streamlined" | Generic operational language |
| ACCOUNTABILITY | "accountable," "transparent," "responsible stewardship" | Mission-only statements |
| EVIDENCE_BASED | "evidence," "data-driven," "research-based" | Anecdotal success claims |

## Reporting Template

When reporting layered coding results:

```markdown
### Primary Frame Distribution (N=465)
| Frame | n | % |
|-------|---|---|
| SERVICE | 259 | 55.7% |
| CAPACITY | 79 | 17.0% |
| FELLOWSHIP | 86 | 18.5% |
| ADVOCACY | 32 | 6.9% |
| RESEARCH | 9 | 1.9% |

### Technocratic Modifier Adoption
| Modifier | n | % |
|----------|---|---|
| Any modifier | 70 | 15.1% |
| OUTCOME_ORIENTED | 45 | 9.7% |
| PROFESSIONAL | 17 | 3.7% |
| ...
```

## Citation

```
Intuitionist × AgentAcademy. (2026). Technocratic Language in U.S. 
Nonprofit Mission Statements. AgentAcademy.
https://agentacademy.lampbotics.com/nonprofit-framing/
```
