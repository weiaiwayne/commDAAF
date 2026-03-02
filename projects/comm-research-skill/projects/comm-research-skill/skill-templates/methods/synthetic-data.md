# Synthetic Data Generation for Communication Research

Using LLMs to generate synthetic social media and text data.

⚠️ **EMERGING METHOD** — Use with extensive validation. Not for primary analysis.

---

## Overview

Synthetic data generation uses LLMs to create artificial text that mimics real social media posts, survey responses, or other communication data.

**Primary Uses:**
- Data augmentation (expand small datasets)
- Privacy preservation (when real data is sensitive)
- Method testing (validate pipelines before real data)
- Counterfactual generation (explore "what if" scenarios)

**NOT for:**
- Making claims about real human behavior
- Replacing real data collection
- Primary substantive analysis

---

## When to Use Synthetic Data

✅ **Appropriate:**
- Testing analysis pipelines before real data arrives
- Augmenting small training datasets for ML
- Generating examples for codebook development
- Privacy-sensitive contexts where real data can't be shared
- Creating balanced datasets (oversample minority classes)

❌ **Inappropriate:**
- Primary source for substantive claims
- Studying actual human behavior
- When real data is accessible
- High-stakes decisions

---

## Probing Questions (REQUIRED)

```
Q1: Why synthetic instead of real data?
    ✓ Real data unavailable (access/privacy)
    ✓ Augmenting small training set
    ✓ Method testing/development
    ✗ "It's easier" — NOT ACCEPTABLE

Q2: How will you validate synthetic data quality?
    ✓ Compare distributions to real data
    ✓ Check for platform-appropriate patterns
    ✓ Human review for plausibility
    ✗ "Trust the LLM" — VALIDATION REQUIRED

Q3: How will you document synthetic data in publications?
    ✓ Clearly labeled as synthetic
    ✓ Generation method in methods section
    ✓ Prompts in appendix
    ✗ "Not mentioned" — UNETHICAL

Q4: What are the limitations of your synthetic approach?
    ✓ List specific limitations
    ✓ Acknowledge what synthetic data CANNOT tell you
```

---

## Generation Strategies

### Strategy 1: Direct Generation

```python
def generate_posts_direct(
    topic: str,
    platform: str,
    n_posts: int,
    model: str = "gpt-4o",
    temperature: float = 0.9
) -> List[str]:
    """
    Generate synthetic posts with direct prompting.
    
    Args:
        topic: What the posts should be about
        platform: Target platform style (twitter, reddit, telegram, etc.)
        n_posts: Number of posts to generate
        model: LLM to use
        temperature: Higher = more diverse
    """
    
    platform_guidance = {
        'twitter': "280 characters max, hashtags common, informal tone",
        'reddit': "Longer form, may include formatting, community-specific language",
        'telegram': "Medium length, may be forwarded messages, can include emojis",
        'facebook': "Personal tone, longer posts acceptable, reactions expected",
        'tiktok': "Very short captions, heavy hashtag use, trendy language"
    }
    
    prompt = f"""Generate {n_posts} realistic {platform} posts about {topic}.

Platform style: {platform_guidance.get(platform, 'standard social media')}

Requirements:
- Each post should be realistic and natural
- Vary sentiment, perspective, and style
- Include appropriate hashtags/mentions for {platform}
- Mix of engagement levels implied
- NO numbering or prefixes

Generate exactly {n_posts} posts, one per line:"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=n_posts * 100
    )
    
    posts = response.choices[0].message.content.strip().split('\n')
    return [p.strip() for p in posts if p.strip()]
```

### Strategy 2: Persona-Based Generation

```python
def generate_posts_persona(
    topic: str,
    personas: List[dict],
    posts_per_persona: int,
    model: str = "gpt-4o"
) -> List[dict]:
    """
    Generate posts from specific personas for more realistic diversity.
    
    personas: List of {"name": str, "description": str, "stance": str}
    """
    
    all_posts = []
    
    for persona in personas:
        prompt = f"""You are: {persona['description']}
Your stance on {topic}: {persona['stance']}

Write {posts_per_persona} social media posts about {topic} from this perspective.
Posts should reflect your persona's voice, vocabulary, and viewpoint.

Generate posts, one per line:"""

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        
        posts = response.choices[0].message.content.strip().split('\n')
        
        for post in posts:
            if post.strip():
                all_posts.append({
                    'text': post.strip(),
                    'persona': persona['name'],
                    'stance': persona['stance'],
                    'synthetic': True
                })
    
    return all_posts

# Example usage
personas = [
    {
        "name": "health_advocate",
        "description": "A public health professional who promotes evidence-based medicine",
        "stance": "pro-vaccine, cites scientific sources"
    },
    {
        "name": "skeptic",
        "description": "Someone concerned about medical autonomy and government overreach",
        "stance": "vaccine-hesitant, questions mandates"
    },
    {
        "name": "parent",
        "description": "A worried parent trying to make the best decision for their children",
        "stance": "uncertain, seeking information"
    }
]

posts = generate_posts_persona("COVID vaccines", personas, posts_per_persona=10)
```

### Strategy 3: Example-Conditioned Generation

```python
def generate_posts_conditioned(
    examples: List[str],
    n_generate: int,
    category: str = None,
    model: str = "gpt-4o"
) -> List[str]:
    """
    Generate synthetic posts conditioned on real examples.
    More realistic but requires seed data.
    """
    
    # Sample examples to include in prompt
    sample_examples = random.sample(examples, min(5, len(examples)))
    examples_text = "\n".join([f"- {ex}" for ex in sample_examples])
    
    category_instruction = f" in the '{category}' category" if category else ""
    
    prompt = f"""Here are examples of real social media posts{category_instruction}:

{examples_text}

Generate {n_generate} NEW posts that are similar in style, topic, and tone.
- Match the language patterns and vocabulary
- Vary the specific content
- Make them realistic and natural
- Do NOT copy the examples directly

New posts (one per line):"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    
    return response.choices[0].message.content.strip().split('\n')
```

### Strategy 4: Attribute-Controlled Generation

```python
def generate_posts_controlled(
    attributes: dict,
    n_posts: int,
    model: str = "gpt-4o"
) -> List[str]:
    """
    Generate posts with specific controlled attributes.
    
    attributes: {
        'topic': str,
        'sentiment': 'positive' | 'negative' | 'neutral',
        'platform': str,
        'has_url': bool,
        'has_hashtags': bool,
        'length': 'short' | 'medium' | 'long',
        'formality': 'informal' | 'formal'
    }
    """
    
    prompt = f"""Generate {n_posts} social media posts with these exact attributes:

- Topic: {attributes.get('topic', 'general')}
- Sentiment: {attributes.get('sentiment', 'mixed')}
- Platform: {attributes.get('platform', 'twitter')}
- Contains URL: {attributes.get('has_url', False)}
- Contains hashtags: {attributes.get('has_hashtags', True)}
- Length: {attributes.get('length', 'medium')}
- Formality: {attributes.get('formality', 'informal')}

Each post MUST match ALL specified attributes.
One post per line:"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    
    return response.choices[0].message.content.strip().split('\n')
```

---

## Validation Protocol

### Step 1: Statistical Validation

```python
def validate_synthetic_stats(real_data: List[str], synthetic_data: List[str]) -> dict:
    """Compare statistical properties of real vs synthetic."""
    
    def get_stats(texts):
        lengths = [len(t) for t in texts]
        hashtag_counts = [t.count('#') for t in texts]
        mention_counts = [t.count('@') for t in texts]
        url_counts = [len(re.findall(r'http\S+', t)) for t in texts]
        
        return {
            'length_mean': np.mean(lengths),
            'length_std': np.std(lengths),
            'hashtags_mean': np.mean(hashtag_counts),
            'mentions_mean': np.mean(mention_counts),
            'url_rate': np.mean([1 if c > 0 else 0 for c in url_counts])
        }
    
    real_stats = get_stats(real_data)
    synth_stats = get_stats(synthetic_data)
    
    comparison = {}
    for key in real_stats:
        comparison[key] = {
            'real': real_stats[key],
            'synthetic': synth_stats[key],
            'diff_pct': abs(real_stats[key] - synth_stats[key]) / (real_stats[key] + 0.001) * 100
        }
    
    return comparison
```

### Step 2: Linguistic Validation

```python
def validate_synthetic_linguistic(real_data: List[str], synthetic_data: List[str]) -> dict:
    """Compare linguistic properties."""
    
    from collections import Counter
    
    def get_vocab(texts):
        words = ' '.join(texts).lower().split()
        return Counter(words)
    
    real_vocab = get_vocab(real_data)
    synth_vocab = get_vocab(synthetic_data)
    
    # Vocabulary overlap
    real_top100 = set([w for w, c in real_vocab.most_common(100)])
    synth_top100 = set([w for w, c in synth_vocab.most_common(100)])
    
    overlap = len(real_top100 & synth_top100) / 100
    
    return {
        'vocab_overlap_top100': overlap,
        'real_unique_words': len(real_vocab),
        'synth_unique_words': len(synth_vocab)
    }
```

### Step 3: Human Validation

```python
def create_human_validation_task(real_data: List[str], synthetic_data: List[str], n_samples: int = 50):
    """Create a task for human validators to distinguish real from synthetic."""
    
    # Sample equal amounts
    real_sample = random.sample(real_data, n_samples // 2)
    synth_sample = random.sample(synthetic_data, n_samples // 2)
    
    # Mix and shuffle
    validation_set = []
    for text in real_sample:
        validation_set.append({'text': text, 'source': 'real', 'human_guess': None})
    for text in synth_sample:
        validation_set.append({'text': text, 'source': 'synthetic', 'human_guess': None})
    
    random.shuffle(validation_set)
    
    # Save for human annotation
    output = "# Synthetic Data Validation Task\n\n"
    output += "For each post, guess: REAL or SYNTHETIC\n\n"
    
    for i, item in enumerate(validation_set):
        output += f"## Post {i+1}\n\n{item['text']}\n\nYour guess: [ ]\n\n---\n\n"
    
    return validation_set, output
```

### Step 4: Downstream Validation

```python
def validate_downstream_performance(
    real_train: List[str], 
    real_test: List[str],
    synthetic_augment: List[str],
    classifier
) -> dict:
    """
    Test if synthetic data improves or degrades downstream task performance.
    """
    
    # Train on real only
    classifier_real = clone(classifier)
    classifier_real.fit(real_train)
    score_real_only = classifier_real.score(real_test)
    
    # Train on real + synthetic
    classifier_augmented = clone(classifier)
    classifier_augmented.fit(real_train + synthetic_augment)
    score_augmented = classifier_augmented.score(real_test)
    
    return {
        'real_only_accuracy': score_real_only,
        'augmented_accuracy': score_augmented,
        'improvement': score_augmented - score_real_only
    }
```

---

## Validation Checklist

```yaml
before_using_synthetic_data:
  statistical:
    - [ ] Length distribution matches real data (±20%)
    - [ ] Hashtag frequency matches platform norms
    - [ ] URL/mention patterns appropriate
    - [ ] Temporal patterns (if applicable) are realistic
  
  linguistic:
    - [ ] Top vocabulary overlaps substantially (>60%)
    - [ ] Platform-specific language present
    - [ ] No obvious LLM artifacts ("As an AI...", etc.)
  
  human:
    - [ ] Humans can't reliably distinguish (accuracy ~50-60%)
    - [ ] No glaring implausibility flagged
  
  downstream:
    - [ ] Augmentation improves or maintains performance
    - [ ] No unexpected biases introduced

reporting_requirements:
  - [ ] "Synthetic data" clearly labeled in paper
  - [ ] Generation method described in methods
  - [ ] Prompts included in appendix
  - [ ] Validation results reported
  - [ ] Limitations acknowledged
```

---

## Common Issues and Solutions

### Issue 1: Posts Too Polished

```yaml
problem: LLM generates grammatically perfect posts
solution: 
  - Add "include occasional typos and informal language" to prompt
  - Use higher temperature
  - Example-conditioned generation
```

### Issue 2: Missing Platform-Specific Patterns

```yaml
problem: Twitter posts without hashtags, Reddit without formatting
solution:
  - Include specific platform guidance in prompt
  - Show examples from target platform
  - Post-process to add missing elements
```

### Issue 3: Hallucinated Entities

```yaml
problem: LLM invents fake people, events, organizations
solution:
  - Review for named entities
  - Constrain prompts to avoid specific claims
  - Use real entity lists as constraints
```

### Issue 4: Lack of Diversity

```yaml
problem: All posts sound similar
solution:
  - Persona-based generation
  - Generate in batches with different temperatures
  - Explicitly request diversity in prompt
```

---

## Ethical Guidelines

```yaml
ethical_requirements:
  transparency:
    - Always label synthetic data as synthetic
    - Never present synthetic as real
    - Document generation method
  
  bias_awareness:
    - LLMs have training biases
    - Synthetic data may amplify these biases
    - Validate for demographic balance
  
  privacy:
    - Don't generate identifiable fake personas
    - Don't create synthetic data mimicking real individuals
    - Consider potential misuse of generated content
  
  limitations:
    - Synthetic data reflects LLM's training, not reality
    - Cannot discover new phenomena with synthetic data
    - Findings don't generalize to real populations
```

---

## Output Schema

```yaml
synthetic_dataset:
  metadata:
    generator: "gpt-4o"
    generation_date: "2026-02-17"
    prompt_template: "See appendix A"
    temperature: 0.9
    n_generated: 5000
    validation_status: "passed"
    
  validation_results:
    length_diff_pct: 12.3
    vocab_overlap: 0.73
    human_accuracy: 0.54  # Can't distinguish
    downstream_improvement: +2.3%
    
  data:
    - text: "Post content..."
      synthetic: true
      generation_params: {...}
```

---

## Key Citations

```bibtex
@article{Bertaglia2024,
  title={Synthetic Instagram Posts for Sponsored Content Detection},
  author={Bertaglia, Thales and others},
  year={2024}
}

@article{SyntheticMultiplatform2025,
  title={Towards High-Fidelity Synthetic Multi-platform Social Media Datasets},
  author={...},
  journal={arXiv},
  year={2025}
}

@article{Staab2024,
  title={Author Profiling with LLMs},
  author={Staab, Robin and others},
  year={2024}
}
```

---

*Synthetic data is a tool, not a replacement for real data. Validate extensively.*
