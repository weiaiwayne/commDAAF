# Sentiment Analysis Method

Analyze emotional valence, stance, or affect in text data.

---

## Overview

Sentiment analysis extracts subjective information from text. In communication research, this typically means:
- **Valence**: Positive vs negative
- **Emotions**: Anger, joy, fear, sadness, surprise, disgust
- **Stance**: Position toward a specific topic
- **Intensity**: Strength of expressed sentiment

---

## Preflight Requirements

Before running sentiment analysis, user MUST specify:

| Requirement | Why It Matters |
|-------------|----------------|
| Sentiment construct | Valence ≠ emotion ≠ stance |
| Unit of analysis | Post-level vs user-level vs aggregated |
| Tool/approach | Dictionary vs ML vs LLM |
| Categories | Binary vs ternary vs multi-class |
| Neutral handling | Include, exclude, or separate category |
| Sarcasm strategy | Detect, flag, or acknowledge limitation |
| Language(s) | Most tools are English-only |
| Validation plan | Human-coded sample required |

---

## Probing Questions

```yaml
sentiment_probing:
  
  q1_construct:
    question: "What EXACTLY do you mean by 'sentiment'?"
    required: true
    acceptable:
      - "Positive vs negative valence"
      - "Specific emotions: [list]"
      - "Stance toward [specific topic]"
      - "Affect intensity"
    unacceptable:
      - "How people feel"
      - "The mood"
      - "Sentiment"
    if_unacceptable: |
      'Sentiment' is not one thing. You must specify:
      
      - VALENCE: Is it positive/negative overall?
      - EMOTION: What specific feelings? (anger, joy, fear...)
      - STANCE: Is it for/against something specific?
      - INTENSITY: How strongly expressed?
      
      Which one matches your research question?

  q2_unit:
    question: "What's your unit of analysis?"
    required: true
    acceptable:
      - "Individual post/tweet"
      - "Aggregated by user"
      - "Aggregated by time period"
      - "Aggregated by topic/hashtag"
    unacceptable:
      - "All the data"
      - "The dataset"
    if_unacceptable: |
      Sentiment at different levels means different things:
      
      - POST LEVEL: "This specific post is negative"
      - USER LEVEL: "This user tends to be negative"
      - TIME LEVEL: "Sentiment was more negative in March"
      - TOPIC LEVEL: "Discourse about X is negative"
      
      Which level answers your research question?

  q3_tool:
    question: "What approach will you use and why?"
    required: true
    options:
      dictionary:
        examples: ["VADER", "LIWC", "SentiWordNet", "AFINN"]
        pros: "Fast, interpretable, reproducible"
        cons: "Ignores context, fails on sarcasm, domain-specific language"
        when_appropriate: "Large datasets, exploratory analysis, English text"
      
      machine_learning:
        examples: ["Fine-tuned BERT", "RoBERTa", "XLNet"]
        pros: "Better accuracy, learns patterns"
        cons: "Requires training data, less interpretable"
        when_appropriate: "When you have labeled training data"
      
      llm:
        examples: ["GPT-4", "Claude", "Gemini"]
        pros: "Context-aware, handles nuance, zero-shot"
        cons: "Expensive, inconsistent, requires validation"
        when_appropriate: "Complex content, need context understanding"
    
    unacceptable:
      - "Whatever is standard"
      - "The usual approach"
    if_unacceptable: |
      There is no "standard" approach. Each has tradeoffs:
      
      | Approach | Speed | Context | Cost | Validation Need |
      |----------|-------|---------|------|-----------------|
      | Dictionary | Fast | None | Free | Moderate |
      | ML model | Medium | Some | Medium | High |
      | LLM | Slow | High | High | Very High |
      
      Which tradeoffs fit your project?

  q4_neutral:
    question: "How will you handle neutral content?"
    required: true
    acceptable:
      - "Three categories: positive/neutral/negative"
      - "Exclude neutral from analysis (with threshold)"
      - "Binary only, acknowledge limitation"
    unacceptable:
      - "Just positive and negative"
      - "What neutral?"
    if_unacceptable: |
      Most social media content is neutral or mixed!
      
      Forcing binary classification means either:
      1. Throwing away 50%+ of your data, OR
      2. Forcing ambiguous content into pos/neg
      
      Option 2 is dangerous — creates false confidence.
      
      Your strategy for neutral content?

  q5_sarcasm:
    question: "What's your sarcasm handling strategy?"
    required: true
    acceptable:
      - "Run sarcasm detection first, flag items"
      - "Use LLM with explicit sarcasm prompt"
      - "Sample and manually review for sarcasm rate"
      - "Acknowledge as limitation, estimate prevalence"
    unacceptable:
      - "The tool handles it"
      - "What about sarcasm?"
    if_unacceptable: |
      "Great job breaking everything" = NEGATIVE
      But dictionary says: "Great" + "job" = POSITIVE
      
      Sarcasm FLIPS polarity. In political/social media data,
      sarcasm is COMMON (10-30% of negative expressions).
      
      If you don't handle sarcasm, you will SYSTEMATICALLY
      misclassify a substantial portion of your data.
      
      Your strategy?

  q6_validation:
    question: "What's your human validation plan?"
    required: true
    acceptable:
      - "Code N items manually, calculate agreement"
      - "Use existing validated dataset for testing"
      - "Inter-rater reliability with research assistant"
    unacceptable:
      - "The model is validated"
      - "I'll check a few"
    if_unacceptable: |
      Automated sentiment is NOT ground truth.
      
      Required for publication:
      1. Human-coded sample (minimum 200 items)
      2. Calculate agreement (Cohen's κ or Krippendorff's α)
      3. Report precision, recall, F1 for your data
      
      "The model was validated on other data" is insufficient.
      You must validate on YOUR data, YOUR domain, YOUR categories.
      
      Your validation plan?
```

---

## Implementation

### Approach 1: Dictionary-Based (VADER)

```python
"""
VADER Sentiment Analysis
Best for: Social media, English, when speed matters
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from typing import List, Dict, Optional

class VaderSentimentAnalyzer:
    """VADER sentiment with uncertainty quantification."""
    
    def __init__(self, neutral_threshold: float = 0.05):
        """
        Args:
            neutral_threshold: Compound scores within [-threshold, +threshold] 
                              are classified as neutral
        """
        self.analyzer = SentimentIntensityAnalyzer()
        self.neutral_threshold = neutral_threshold
        
    def analyze_text(self, text: str) -> Dict:
        """Analyze single text with uncertainty flags."""
        scores = self.analyzer.polarity_scores(text)
        
        # Classify based on compound score
        compound = scores['compound']
        if compound >= self.neutral_threshold:
            label = 'positive'
        elif compound <= -self.neutral_threshold:
            label = 'negative'
        else:
            label = 'neutral'
        
        # Detect potential issues
        issues = []
        
        # Check for sarcasm signals
        sarcasm_signals = self._detect_sarcasm_signals(text)
        if sarcasm_signals:
            issues.append(f"sarcasm_risk: {sarcasm_signals}")
        
        # Check for negation (VADER handles some, but flag anyway)
        if self._has_complex_negation(text):
            issues.append("complex_negation")
        
        # Check for questions
        if text.strip().endswith('?'):
            issues.append("is_question")
        
        # Check for mixed signals
        if scores['pos'] > 0.2 and scores['neg'] > 0.2:
            issues.append("mixed_sentiment")
        
        return {
            'text': text,
            'label': label,
            'compound': compound,
            'positive': scores['pos'],
            'negative': scores['neg'],
            'neutral': scores['neu'],
            'confidence': abs(compound),  # Higher absolute = more confident
            'issues': issues,
            'needs_review': len(issues) > 0 or abs(compound) < 0.3
        }
    
    def _detect_sarcasm_signals(self, text: str) -> List[str]:
        """Detect linguistic signals of potential sarcasm."""
        import re
        signals = []
        
        patterns = {
            'excessive_punctuation': r'[!?]{2,}',
            'all_caps': r'\b[A-Z]{3,}\b',
            'eye_roll': r'🙄',
            'air_quotes': r'["""]',
            'yeah_right': r'\b(yeah|sure|right)\s+(right|sure)\b',
        }
        
        for name, pattern in patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                signals.append(name)
        
        return signals
    
    def _has_complex_negation(self, text: str) -> bool:
        """Check for negation patterns VADER might miss."""
        import re
        complex_patterns = [
            r"not\s+\w+\s+(good|great|happy|positive)",
            r"never\s+\w+\s+happy",
            r"wouldn't\s+say.*(good|positive)",
        ]
        return any(re.search(p, text.lower()) for p in complex_patterns)
    
    def analyze_batch(self, texts: List[str]) -> pd.DataFrame:
        """Analyze multiple texts, return DataFrame."""
        results = [self.analyze_text(t) for t in texts]
        return pd.DataFrame(results)
    
    def get_validation_sample(self, df: pd.DataFrame, n: int = 200) -> pd.DataFrame:
        """Get stratified sample for human validation."""
        # Stratify by label and uncertainty
        df['uncertain'] = df['needs_review']
        
        sample = df.groupby(['label', 'uncertain'], group_keys=False).apply(
            lambda x: x.sample(min(len(x), n // 6))
        )
        
        # Add columns for human coding
        sample['human_label'] = None
        sample['human_notes'] = None
        
        return sample.head(n)


# Usage
def run_vader_analysis(texts: List[str], neutral_threshold: float = 0.05):
    """
    Complete VADER analysis pipeline.
    
    Returns results + validation sample + statistics.
    """
    analyzer = VaderSentimentAnalyzer(neutral_threshold=neutral_threshold)
    
    # Analyze all texts
    results = analyzer.analyze_batch(texts)
    
    # Get validation sample
    validation_sample = analyzer.get_validation_sample(results, n=200)
    
    # Calculate statistics
    stats = {
        'total': len(results),
        'positive': (results['label'] == 'positive').sum(),
        'negative': (results['label'] == 'negative').sum(),
        'neutral': (results['label'] == 'neutral').sum(),
        'needs_review': results['needs_review'].sum(),
        'pct_uncertain': results['needs_review'].mean() * 100,
        'sarcasm_flagged': results['issues'].apply(lambda x: 'sarcasm_risk' in str(x)).sum(),
    }
    
    print(f"Sentiment Analysis Complete")
    print(f"Total: {stats['total']}")
    print(f"Positive: {stats['positive']} ({stats['positive']/stats['total']*100:.1f}%)")
    print(f"Negative: {stats['negative']} ({stats['negative']/stats['total']*100:.1f}%)")
    print(f"Neutral: {stats['neutral']} ({stats['neutral']/stats['total']*100:.1f}%)")
    print(f"Flagged for review: {stats['needs_review']} ({stats['pct_uncertain']:.1f}%)")
    print(f"Sarcasm signals detected: {stats['sarcasm_flagged']}")
    
    return {
        'results': results,
        'validation_sample': validation_sample,
        'statistics': stats
    }
```

### Approach 2: LLM-Based with Context

```python
"""
LLM-based sentiment analysis with context awareness.
Better for: Sarcasm, nuanced content, domain-specific text
"""

import asyncio
from typing import List, Dict, Optional
import json

class LLMSentimentAnalyzer:
    """Context-aware sentiment using LLM."""
    
    def __init__(self, model: str = "google/gemini-2.0-flash", 
                 categories: List[str] = None):
        self.model = model
        self.categories = categories or ['positive', 'negative', 'neutral']
        
    def _build_prompt(self, text: str, include_reasoning: bool = True) -> str:
        """Build analysis prompt with sarcasm awareness."""
        
        category_str = " / ".join(self.categories)
        
        if include_reasoning:
            return f"""Analyze the sentiment of this text.

IMPORTANT: Before classifying, check for:
1. Sarcasm or irony (words say positive but mean negative, or vice versa)
2. Context that might change meaning
3. Quoted text (whose sentiment is it?)

Text: "{text}"

Respond in this exact JSON format:
{{
    "literal_meaning": "what the words literally say",
    "likely_intent": "what the author probably means",
    "is_sarcastic": true/false,
    "sarcasm_signals": ["list of signals if sarcastic, else empty"],
    "sentiment": "{category_str}",
    "confidence": "high/medium/low",
    "reasoning": "one sentence explanation"
}}"""
        else:
            return f"""Classify sentiment as {category_str}.
Text: "{text}"
Sentiment:"""

    async def analyze_text(self, text: str) -> Dict:
        """Analyze single text with context reasoning."""
        prompt = self._build_prompt(text)
        
        response = await call_llm(self.model, prompt)
        
        try:
            result = json.loads(response)
            result['text'] = text
            result['model'] = self.model
            return result
        except json.JSONDecodeError:
            # Fallback parsing
            return {
                'text': text,
                'sentiment': self._extract_sentiment(response),
                'raw_response': response,
                'parse_error': True
            }
    
    async def analyze_batch(self, texts: List[str], 
                           batch_size: int = 10) -> List[Dict]:
        """Analyze batch with rate limiting."""
        results = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            batch_results = await asyncio.gather(
                *[self.analyze_text(t) for t in batch]
            )
            results.extend(batch_results)
            
            # Rate limiting
            if i + batch_size < len(texts):
                await asyncio.sleep(1)
        
        return results
    
    def _extract_sentiment(self, response: str) -> str:
        """Extract sentiment from non-JSON response."""
        response_lower = response.lower()
        for cat in self.categories:
            if cat in response_lower:
                return cat
        return 'unknown'


async def run_llm_sentiment(texts: List[str], 
                           model: str = "google/gemini-2.0-flash",
                           categories: List[str] = None):
    """
    Complete LLM sentiment analysis pipeline.
    """
    analyzer = LLMSentimentAnalyzer(model=model, categories=categories)
    
    print(f"Analyzing {len(texts)} texts with {model}...")
    results = await analyzer.analyze_batch(texts)
    
    # Convert to DataFrame
    import pandas as pd
    df = pd.DataFrame(results)
    
    # Statistics
    stats = {
        'total': len(df),
        'sarcasm_detected': df.get('is_sarcastic', pd.Series([False]*len(df))).sum(),
        'high_confidence': (df.get('confidence', '') == 'high').sum(),
        'low_confidence': (df.get('confidence', '') == 'low').sum(),
    }
    
    for cat in analyzer.categories:
        stats[cat] = (df['sentiment'] == cat).sum()
    
    return {
        'results': df,
        'statistics': stats
    }
```

### Approach 3: Multi-Model Validation

```python
"""
Multi-model sentiment for uncertainty quantification.
When models disagree, flag for human review.
"""

async def multi_model_sentiment(text: str, 
                                models: List[str] = None) -> Dict:
    """
    Classify with multiple models; disagreement = uncertainty.
    """
    if models is None:
        models = [
            'google/gemini-2.0-flash',
            'anthropic/claude-sonnet-4',
            'openai/gpt-4o-mini'
        ]
    
    results = {}
    
    prompt = f"""Classify sentiment as positive/negative/neutral.
Consider sarcasm and context.
Text: "{text}"
Classification:"""
    
    for model in models:
        response = await call_llm(model, prompt)
        results[model] = parse_sentiment(response)
    
    # Check agreement
    labels = list(results.values())
    unique = set(labels)
    
    if len(unique) == 1:
        return {
            'text': text,
            'sentiment': labels[0],
            'unanimous': True,
            'confidence': 'high',
            'model_results': results
        }
    else:
        from collections import Counter
        counts = Counter(labels)
        majority = counts.most_common(1)[0]
        
        return {
            'text': text,
            'sentiment': 'AMBIGUOUS',
            'majority_label': majority[0],
            'majority_count': majority[1],
            'unanimous': False,
            'confidence': 'low',
            'needs_human_review': True,
            'model_results': results,
            'note': f"Models disagree: {dict(counts)}"
        }
```

---

## Validation Requirements

### Minimum Standards

| Metric | Required Value |
|--------|----------------|
| Human validation sample | ≥ 200 items |
| Inter-rater reliability | κ ≥ 0.7 |
| Report precision | Required |
| Report recall | Required |
| Report F1 | Required |
| Sensitivity analysis | Required if using threshold |

### Validation Code

```python
def validate_sentiment_analysis(human_labels: List[str], 
                                auto_labels: List[str]) -> Dict:
    """
    Calculate validation metrics for sentiment analysis.
    """
    from sklearn.metrics import classification_report, cohen_kappa_score
    from sklearn.metrics import confusion_matrix
    import numpy as np
    
    # Classification report
    report = classification_report(human_labels, auto_labels, output_dict=True)
    
    # Cohen's Kappa
    kappa = cohen_kappa_score(human_labels, auto_labels)
    
    # Confusion matrix
    cm = confusion_matrix(human_labels, auto_labels)
    
    # Check if acceptable
    acceptable = kappa >= 0.7
    
    return {
        'classification_report': report,
        'kappa': kappa,
        'confusion_matrix': cm.tolist(),
        'acceptable': acceptable,
        'recommendation': 'Proceed with analysis' if acceptable else 
            'Improve model or refine categories before proceeding'
    }
```

---

## Reporting Template

```markdown
## Sentiment Analysis Methods

### Approach
- **Method**: [Dictionary/ML/LLM]
- **Tool**: [Specific tool/model]
- **Categories**: [List categories]

### Parameters
- **Neutral threshold**: [value if applicable]
- **Sarcasm handling**: [strategy]
- **Unit of analysis**: [post/user/aggregated]

### Validation
- **Sample size**: N items coded by human
- **Agreement (κ)**: [value]
- **Precision**: [value] (95% CI: [low, high])
- **Recall**: [value] (95% CI: [low, high])
- **F1**: [value]

### Flagged Items
- **Total flagged for review**: N (X%)
- **Sarcasm signals detected**: N
- **Human-reviewed from flags**: N

### Limitations
1. [Limitation 1]
2. [Limitation 2]
3. [Limitation 3]
```

---

## Workflow Integration

```yaml
# Sentiment analysis workflow
sentiment_analysis:
  
  preflight:
    - verify_construct_definition
    - verify_unit_of_analysis
    - verify_tool_selection
    - verify_neutral_handling
    - verify_sarcasm_strategy
    - verify_validation_plan
  
  execution:
    - run_analysis_with_uncertainty
    - flag_uncertain_items
    - detect_sarcasm_signals
    - generate_validation_sample
  
  validation:
    - human_code_sample
    - calculate_agreement
    - check_threshold_met
    
  post_analysis:
    - sensitivity_check_if_threshold
    - generate_report
    - document_limitations
```
