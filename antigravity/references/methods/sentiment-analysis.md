# Sentiment Analysis

## Probing Questions (ALL REQUIRED)

```
Q1: What EXACTLY do you mean by 'sentiment'?
    ✓ Positive/negative valence
    ✓ Specific emotions (list them)
    ✓ Stance toward specific topic
    ✗ "How people feel" — TOO VAGUE

Q2: What's your unit of analysis?
    ✓ Individual post
    ✓ Aggregated by user
    ✓ Aggregated by time
    ✗ "All the data" — UNACCEPTABLE

Q3: What approach and why?
    Must justify: Dictionary vs ML vs LLM
    ✗ "Whatever is standard" — NO STANDARD EXISTS

Q4: How will you handle neutral content?
    ✓ Three categories with threshold
    ✓ Exclude with justification
    ✗ "Just positive and negative" — FORCES FALSE PRECISION

Q5: What's your sarcasm strategy?
    ✓ Detect and flag
    ✓ LLM with explicit prompt
    ✓ Acknowledge as limitation
    ✗ "The tool handles it" — IT DOESN'T

Q6: Validation plan?
    ✓ Human sample (N ≥ 200)
    ✓ Calculate agreement (κ)
    ✗ "The model is validated" — NOT ON YOUR DATA
```

## Approaches

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **VADER** | Fast, social media tuned | No context, misses sarcasm | Quick exploration |
| **TextBlob** | Simple, subjectivity score | Generic, not domain-specific | Basic analysis |
| **LLM** | Context-aware, nuanced | Expensive, requires validation | High-stakes analysis |
| **Fine-tuned** | Domain-specific | Requires training data | Large-scale projects |

## Critical Checks

- [ ] Sarcasm detection layer runs BEFORE sentiment (especially for political/climate)
- [ ] Neutral threshold defined explicitly (e.g., ±0.05)
- [ ] Human validation sample planned (N≥200)
- [ ] Unit of analysis matches RQ

## Common Mistakes

| Mistake | Why It's Wrong |
|---------|----------------|
| Binary sentiment only | Forces false precision, loses nuance |
| Ignoring sarcasm | Climate/politics = high sarcasm rate |
| Document-level only | Misses aspect-level sentiment |
| No validation | Dictionary ≠ ground truth |
