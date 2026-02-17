# LLM-Based Annotation Skill (Auto-Customized)

*Generated from your Zotero library analysis*

## Overview

Use large language models for text classification and annotation.
Emerging method detected in your library (67 papers).

## Priority in Your Research: CRITICAL

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

- **Twitter**: Appears in 293 papers
- **Facebook**: Appears in 89 papers
- **Weibo**: Appears in 31 papers

## Key Citations

*Add key citations for llm_annotation from your library here*

---
*Auto-generated based on your research profile*
