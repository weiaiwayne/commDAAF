# LLM Methods Landscape for Communication Research

A survey of Large Language Model applications in computational communication research (2024-2026).

---

## Overview

LLMs have transformed computational social science. This document surveys the emerging methods and their applications to communication research.

**Key Finding (Ziems et al., 2024):** LLMs can augment CSS research in two primary ways:
1. Serving as **zero-shot data annotators** on human annotation teams
2. Bootstrapping challenging **creative generation tasks**

---

## 1. LLM-Based Text Annotation

### What It Is
Using LLMs (GPT-4, Claude, Gemini) to classify text instead of or alongside human coders.

### Key Findings
- **Gilardi et al. (2023):** ChatGPT outperforms crowd workers for text-annotation tasks
- **Zero-shot performance** often matches or exceeds trained human coders
- **Multi-model validation** improves reliability

### Implementation
See `methods/llm-annotation.md` for detailed guidance.

### Best Practices
```yaml
llm_annotation_best_practices:
  - Always validate against human gold standard (N >= 200)
  - Use multiple models for epistemic diversity
  - Document prompts in appendix
  - Report model version and date
  - Acknowledge prompt sensitivity
  - Calculate inter-model agreement
```

### Open Questions
- How do LLM biases affect annotation?
- What's the optimal human-AI division of labor?
- How do we handle LLM inconsistency?

---

## 2. Synthetic Data Generation

### What It Is
Using LLMs to generate synthetic social media posts, survey responses, or other text data.

### Applications
- **Data augmentation** — Expand small training datasets
- **Privacy preservation** — Generate synthetic data when real data is sensitive
- **Platform-specific generation** — Generate data mimicking specific platforms
- **Counterfactual generation** — "What if this post was more positive?"

### Key Papers
- **Bertaglia et al. (2024):** Synthetic Instagram posts for sponsored content detection
- **Synthetic Multi-platform Social Media Datasets (2025):** GPT-4o best matches real data patterns
- **MIT Computational Linguistics (2025):** Evaluation of synthetic user-generated text

### Implementation

```python
def generate_synthetic_posts(
    topic: str,
    platform: str,
    n_posts: int,
    model: str = "gpt-4o"
):
    """
    Generate synthetic social media posts.
    
    ⚠️ WARNING: Synthetic data is NOT real data.
    Use for augmentation/testing, not primary analysis.
    """
    
    prompt = f"""Generate {n_posts} realistic {platform} posts about {topic}.

Each post should:
- Match typical {platform} posting style and length
- Include appropriate hashtags/mentions for {platform}
- Vary in sentiment and perspective
- Be realistic (not obviously AI-generated)

Format: One post per line, no numbering."""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9  # Higher for diversity
    )
    
    return response.choices[0].message.content.split('\n')
```

### Validation Requirements

```yaml
synthetic_data_validation:
  required:
    - Compare statistical properties to real data
    - Check for hallucinated entities/events
    - Verify platform-appropriate formatting
    - Test downstream model performance
  
  report:
    - How synthetic data was generated
    - Model and parameters used
    - Validation against real data
    - Limitations of synthetic approach
```

### Ethical Considerations
- ⚠️ Synthetic data can perpetuate biases
- ⚠️ Must clearly label as synthetic in publications
- ⚠️ Not suitable for studying real human behavior
- ✅ Useful for testing methods, not for substantive claims

---

## 3. LLM-Powered Agent-Based Simulation

### What It Is
Using LLMs as the "brain" of agents in social simulations, replacing rule-based decision-making with natural language reasoning.

### Key Developments
- **LLM Archetypes (MIT Media Lab, 2025):** Scale to millions of agents efficiently
- **Generative Agent-Based Models:** Simulate social media conversations
- **ElectionSim:** 14,490 LLM agents simulating election dynamics

### Applications in Communication Research
- Simulating misinformation spread
- Modeling opinion dynamics
- Testing intervention strategies
- Studying platform effects

### Architecture

```python
class LLMAgent:
    """
    An agent powered by an LLM for social simulation.
    """
    
    def __init__(self, persona: str, model: str = "gpt-4o-mini"):
        self.persona = persona
        self.model = model
        self.memory = []
    
    def perceive(self, environment_state: dict):
        """Process environmental information."""
        self.memory.append(environment_state)
    
    def decide(self, options: List[str]) -> str:
        """Make a decision based on persona and memory."""
        prompt = f"""You are: {self.persona}
        
Recent context: {self.memory[-5:]}

Options: {options}

Based on your persona and the context, which option would you choose?
Respond with ONLY the option, nothing else."""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    def act(self, action: str, environment):
        """Execute action in the environment."""
        environment.apply_action(self, action)
```

### Validation Challenges

The **central challenge** (Guo et al., 2025) is validation:
- How do we know simulated behavior matches reality?
- What's the appropriate level of abstraction?
- How do we handle LLM inconsistency?

```yaml
validation_approaches:
  behavioral_matching:
    - Compare to empirical data distributions
    - Test against known social phenomena
    - Validate against experimental results
  
  sensitivity_analysis:
    - Vary prompts and observe stability
    - Test with different models
    - Check parameter sensitivity
  
  face_validity:
    - Domain expert review of agent behavior
    - Qualitative assessment of plausibility
```

### ⚠️ Critical Limitations
- LLMs trained on text may not reflect true human decision-making
- Expensive at scale
- Results depend heavily on persona design
- Reproducibility challenges

---

## 4. Multi-Model Validation (Epistemic Diversity)

### What It Is
Using multiple different LLMs and treating disagreement as a signal of uncertainty.

### Rationale
Different models have different:
- Training data
- Biases
- Strengths and weaknesses
- "Perspectives"

### Implementation

```python
def multi_model_classify(text: str, categories: List[str]) -> dict:
    """
    Classify text using multiple models.
    Return predictions and agreement metrics.
    """
    models = [
        ("gpt-4o", "openai"),
        ("claude-sonnet-4", "anthropic"),
        ("gemini-2.0-flash", "google"),
        ("deepseek-v3", "deepseek")
    ]
    
    predictions = {}
    for model_name, provider in models:
        predictions[model_name] = classify(text, categories, model_name)
    
    # Calculate agreement
    values = list(predictions.values())
    agreement = len(set(values)) == 1
    
    # Majority vote
    from collections import Counter
    majority = Counter(values).most_common(1)[0][0]
    
    return {
        'predictions': predictions,
        'agreement': agreement,
        'majority_vote': majority,
        'confidence': Counter(values).most_common(1)[0][1] / len(models)
    }
```

### When to Use Multi-Model
- High-stakes classifications (coordination detection, misinformation)
- Ambiguous cases
- Novel domains where single-model performance is uncertain
- Building trust in automated annotations

### Interpreting Disagreement
```yaml
disagreement_interpretation:
  all_agree: High confidence, proceed
  3/4_agree: Moderate confidence, consider majority
  2/4_agree: Low confidence, flag for human review
  all_disagree: Very uncertain, require human judgment
```

---

## 5. LLM-Assisted Qualitative Analysis

### What It Is
Using LLMs to assist (not replace) qualitative coding and interpretation.

### Applications
- **Initial coding suggestions:** LLM proposes codes, human verifies
- **Theme identification:** LLM identifies potential themes across data
- **Quote extraction:** LLM finds relevant quotes for themes
- **Memo generation:** LLM drafts analytical memos

### Best Practices
```yaml
llm_qualitative_best_practices:
  - LLM assists, human decides
  - Always read original data
  - Treat LLM suggestions as hypotheses
  - Document LLM role in methods
  - Maintain audit trail
```

---

## 6. Emerging Methods

### Chain-of-Thought for Complex Judgments
```python
def cot_classify(text, categories):
    """Chain-of-thought classification for complex judgments."""
    prompt = f"""Classify this text into one of: {categories}

Text: "{text}"

Think step by step:
1. What is the main topic?
2. What sentiment or stance is expressed?
3. What evidence points to each category?
4. Which category best fits?

REASONING: [your step-by-step reasoning]
CLASSIFICATION: [category]"""
    
    # Parse reasoning and classification from response
```

### Retrieval-Augmented Classification
```python
def rag_classify(text, categories, context_db):
    """Classify with relevant context retrieval."""
    # Retrieve similar previously-classified examples
    similar = context_db.search(text, k=5)
    
    # Include in prompt
    examples = "\n".join([f"Example: {s.text} -> {s.label}" for s in similar])
    
    prompt = f"""Based on these examples:
{examples}

Classify: "{text}"
Category:"""
```

### LLM-Powered Literature Review
- Systematic review assistance
- Gap identification
- Synthesis generation

---

## Method Comparison

| Method | Primary Use | Maturity | Validation Difficulty |
|--------|-------------|----------|----------------------|
| **LLM Annotation** | Text classification | High | Medium |
| **Synthetic Data** | Data augmentation | Medium | High |
| **Agent Simulation** | Social dynamics | Low | Very High |
| **Multi-Model** | Uncertainty quantification | Medium | Low |
| **Qualitative Assist** | Coding assistance | Medium | Medium |

---

## Recommended Adoption Path

### Now (Mature)
1. LLM annotation with human validation
2. Multi-model validation for sensitive classifications
3. Qualitative coding assistance

### Soon (Emerging)
4. Synthetic data for augmentation (with heavy validation)
5. Chain-of-thought for complex judgments

### Later (Experimental)
6. Agent-based simulation (validation challenges unresolved)

---

## Key Citations

```bibtex
@article{Ziems2024,
  title={Can Large Language Models Transform Computational Social Science?},
  author={Ziems, Caleb and others},
  journal={Computational Linguistics},
  volume={50},
  number={1},
  pages={237--291},
  year={2024}
}

@article{Gilardi2023,
  title={ChatGPT outperforms crowd workers for text-annotation tasks},
  author={Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Maël},
  journal={Proceedings of the National Academy of Sciences},
  volume={120},
  number={30},
  year={2023}
}

@article{Gao2024,
  title={Large language models empowered agent-based modeling and simulation: 
         a survey and perspectives},
  author={Gao, Chen and others},
  journal={Humanities and Social Sciences Communications},
  year={2024}
}
```

---

## Integration with This Skill

| LLM Method | Relevant Skill File |
|------------|---------------------|
| Annotation | `methods/llm-annotation.md` |
| Multi-model | `methods/validation.md` |
| Agent simulation | Future: `methods/llm-simulation.md` |
| Synthetic data | Future: `methods/synthetic-data.md` |

---

*This landscape document reflects the state of LLM methods as of February 2026. The field is evolving rapidly.*
