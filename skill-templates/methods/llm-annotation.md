# LLM-Based Annotation Method Skill

## Overview

Use Large Language Models for text classification and annotation tasks.
Replaces or augments traditional manual coding with AI-based annotation.

Based on: Rathje et al. (2024), DAAF methodology

## When to Use LLM Annotation

✅ **Good fit:**
- Subjective judgments (sentiment, stance, framing)
- Categories with clear definitions
- Large volumes requiring scale
- Exploratory annotation before manual coding

❌ **Poor fit:**
- Highly specialized domain knowledge required
- Legal/regulatory contexts requiring human accountability
- Categories that humans can't reliably agree on (fix codebook first)

## Core Principles

1. **Never trust raw LLM output** — Always validate
2. **Document everything** — Prompts, versions, validation
3. **Use multiple strategies** — Zero-shot, few-shot, self-consistency
4. **Cross-validate with humans** — Sample comparison
5. **Report limitations** — Model, prompt, performance bounds

## Annotation Strategies

### Zero-Shot Classification

No examples provided. Relies on model's pre-training.

```python
def zero_shot_classify(text, categories, client):
    """
    Zero-shot classification.
    
    Returns: predicted category
    """
    category_list = '\n'.join([f"- {cat}" for cat in categories])
    
    prompt = f"""Classify the following text into exactly one category.

Categories:
{category_list}

Text: "{text}"

Respond with ONLY the category name, nothing else."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use cheap model for annotation
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=50
    )
    
    return response.choices[0].message.content.strip()
```

### Few-Shot Classification

Provide examples to guide the model.

```python
def few_shot_classify(text, examples, categories, client):
    """
    Few-shot classification with examples.
    
    examples: list of {"text": str, "category": str}
    """
    # Build examples string
    example_strs = []
    for ex in examples:
        example_strs.append(f'Text: "{ex["text"]}"\nCategory: {ex["category"]}')
    
    examples_block = '\n\n'.join(example_strs)
    category_list = '\n'.join([f"- {cat}" for cat in categories])
    
    prompt = f"""Classify texts into categories. Here are examples:

{examples_block}

Categories:
{category_list}

Now classify this text:
Text: "{text}"
Category:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=50
    )
    
    return response.choices[0].message.content.strip()
```

### Self-Consistency (Multiple Samples)

Sample multiple times and take majority vote.

```python
from collections import Counter

def self_consistency_classify(text, categories, client, n_samples=5):
    """
    Self-consistency classification with majority vote.
    
    More reliable than single-shot, especially for ambiguous cases.
    """
    predictions = []
    
    category_list = '\n'.join([f"- {cat}" for cat in categories])
    prompt = f"""Classify the following text into exactly one category.

Categories:
{category_list}

Text: "{text}"

Respond with ONLY the category name, nothing else."""

    for _ in range(n_samples):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,  # Higher temp for diversity
            max_tokens=50
        )
        pred = response.choices[0].message.content.strip()
        predictions.append(pred)
    
    # Majority vote
    vote_counts = Counter(predictions)
    winner, count = vote_counts.most_common(1)[0]
    confidence = count / n_samples
    
    return {
        'prediction': winner,
        'confidence': confidence,
        'all_predictions': predictions
    }
```

### Chain-of-Thought Annotation

Have the model explain its reasoning.

```python
def cot_classify(text, categories, category_definitions, client):
    """
    Chain-of-thought classification with reasoning.
    
    category_definitions: dict mapping category to definition
    """
    definitions_block = '\n'.join([
        f"- **{cat}**: {defn}" 
        for cat, defn in category_definitions.items()
    ])
    
    prompt = f"""You are annotating text for a research study.

Category definitions:
{definitions_block}

Text to classify:
"{text}"

First, explain your reasoning step by step. Consider which category definitions best match the text.
Then, provide your final classification.

Format your response as:
REASONING: [your reasoning]
CLASSIFICATION: [category name]"""

    response = client.chat.completions.create(
        model="gpt-4o",  # Use better model for CoT
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=500
    )
    
    content = response.choices[0].message.content
    
    # Parse response
    lines = content.split('\n')
    reasoning = ''
    classification = ''
    
    for line in lines:
        if line.startswith('REASONING:'):
            reasoning = line.replace('REASONING:', '').strip()
        elif line.startswith('CLASSIFICATION:'):
            classification = line.replace('CLASSIFICATION:', '').strip()
    
    return {
        'classification': classification,
        'reasoning': reasoning,
        'raw_response': content
    }
```

## Batch Processing

```python
import asyncio
from tqdm.asyncio import tqdm

async def batch_classify(texts, categories, client, strategy='zero_shot', 
                         batch_size=10, max_concurrent=5):
    """
    Batch classification with rate limiting.
    """
    results = []
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def classify_one(text, idx):
        async with semaphore:
            try:
                if strategy == 'zero_shot':
                    pred = zero_shot_classify(text, categories, client)
                elif strategy == 'self_consistency':
                    pred = self_consistency_classify(text, categories, client)
                else:
                    raise ValueError(f"Unknown strategy: {strategy}")
                
                return {'idx': idx, 'text': text, 'prediction': pred, 'error': None}
            except Exception as e:
                return {'idx': idx, 'text': text, 'prediction': None, 'error': str(e)}
    
    tasks = [classify_one(text, i) for i, text in enumerate(texts)]
    
    for batch in tqdm(range(0, len(tasks), batch_size)):
        batch_tasks = tasks[batch:batch + batch_size]
        batch_results = await asyncio.gather(*batch_tasks)
        results.extend(batch_results)
    
    return results
```

## Validation

### Human Comparison

```python
def validate_against_human(llm_labels, human_labels):
    """
    Compare LLM annotations to human gold standard.
    """
    from sklearn.metrics import classification_report, confusion_matrix, cohen_kappa_score
    
    # Filter to items with both labels
    valid_mask = (llm_labels.notna()) & (human_labels.notna())
    llm = llm_labels[valid_mask]
    human = human_labels[valid_mask]
    
    results = {
        'n_compared': len(llm),
        'accuracy': (llm == human).mean(),
        'cohen_kappa': cohen_kappa_score(human, llm),
        'classification_report': classification_report(human, llm, output_dict=True),
        'confusion_matrix': confusion_matrix(human, llm).tolist()
    }
    
    return results
```

### Inter-Model Agreement

Compare annotations from different models.

```python
def inter_model_agreement(texts, categories, models):
    """
    Compare annotations across different models.
    
    models: list of (model_name, client) tuples
    """
    all_predictions = {}
    
    for model_name, client in models:
        preds = []
        for text in texts:
            pred = zero_shot_classify(text, categories, client)
            preds.append(pred)
        all_predictions[model_name] = preds
    
    # Calculate pairwise agreement
    import pandas as pd
    from sklearn.metrics import cohen_kappa_score
    
    agreement_matrix = pd.DataFrame(
        index=[m[0] for m in models],
        columns=[m[0] for m in models]
    )
    
    for m1 in all_predictions:
        for m2 in all_predictions:
            kappa = cohen_kappa_score(all_predictions[m1], all_predictions[m2])
            agreement_matrix.loc[m1, m2] = kappa
    
    return {
        'predictions': pd.DataFrame(all_predictions),
        'agreement_matrix': agreement_matrix
    }
```

## Model Routing for Cost

Different tasks → different models:

| Task | Model | Cost | Notes |
|------|-------|------|-------|
| Simple classification | GPT-4o-mini | $0.15/1M | Fast, cheap |
| Few-shot with examples | GPT-4o | $2.50/1M | Better example use |
| Chain-of-thought | Claude Opus | $15/1M | Best reasoning |
| Validation sample | Human | $$ | Gold standard |

```python
def route_annotation_task(task_type, complexity):
    """Route annotation to appropriate model."""
    
    if task_type == 'binary_classification' and complexity == 'low':
        return 'gpt-4o-mini'
    elif task_type == 'multiclass' and complexity == 'low':
        return 'gpt-4o-mini'
    elif task_type == 'multiclass' and complexity == 'high':
        return 'gpt-4o'
    elif task_type == 'requires_reasoning':
        return 'claude-3-opus'
    else:
        return 'gpt-4o-mini'  # Default to cheap
```

## Prompt Engineering Tips

1. **Be specific about output format**
   ```
   Respond with ONLY the category name, nothing else.
   ```

2. **Include edge case guidance**
   ```
   If the text could fit multiple categories, choose the PRIMARY category.
   If unsure, classify as "Uncertain".
   ```

3. **Provide category definitions**
   ```
   Categories:
   - Positive: Expresses favorable sentiment toward the subject
   - Negative: Expresses unfavorable sentiment toward the subject
   - Neutral: Factual statement without clear sentiment
   ```

4. **Use consistent formatting**
   ```
   Always present categories in same order
   Always use same prompt template
   ```

## Output Format

```yaml
# annotation_results.yaml

metadata:
  task: "stance_classification"
  model: "gpt-4o-mini"
  strategy: "few_shot"
  n_examples: 5
  date: "2026-02-17"

categories:
  - Support
  - Oppose
  - Neutral

validation:
  n_human_validated: 100
  accuracy: 0.87
  cohen_kappa: 0.79
  
  per_category:
    Support:
      precision: 0.89
      recall: 0.85
      f1: 0.87
    Oppose:
      precision: 0.88
      recall: 0.91
      f1: 0.89
    Neutral:
      precision: 0.82
      recall: 0.78
      f1: 0.80

results:
  total_annotated: 5000
  distribution:
    Support: 1823
    Oppose: 2156
    Neutral: 1021
```

## Reproducibility Checklist

- [ ] Document model name and version
- [ ] Save exact prompts used
- [ ] Record temperature and sampling parameters
- [ ] Set random seeds where applicable
- [ ] Archive model API responses
- [ ] Report validation metrics
- [ ] Note date (models update over time)

## Reporting Guidelines

When publishing LLM annotation results:

1. **State the model** — Name, version, date
2. **Include prompts** — Full text in appendix
3. **Report validation** — Human comparison on sample
4. **Acknowledge limitations** — Model biases, failure modes
5. **Enable replication** — Code and prompts available
