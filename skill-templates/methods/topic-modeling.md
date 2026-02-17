# Topic Modeling Method

Discover latent themes in large text corpora.

---

## Overview

Topic modeling identifies recurring themes across documents without predefined categories. Common approaches:
- **LDA (Latent Dirichlet Allocation)**: Classic probabilistic model
- **NMF (Non-negative Matrix Factorization)**: Linear algebra approach
- **BERTopic**: Transformer-based, better for short texts
- **STM (Structural Topic Model)**: Incorporates metadata

---

## Preflight Requirements

Before running topic modeling, user MUST specify:

| Requirement | Why It Matters |
|-------------|----------------|
| Research question | Discovery vs hypothesis testing? |
| Number of topics (K) | K=5 vs K=50 → completely different results |
| Preprocessing choices | Stopwords, stemming, etc. affect topics |
| Document definition | What is one "document"? |
| Minimum doc length | Short texts are problematic |
| Algorithm choice | LDA vs BERTopic vs others |
| Validation strategy | How to verify topics are meaningful |
| Interpretation plan | Who names topics? How? |

---

## Probing Questions

```yaml
topic_modeling_probing:

  q1_purpose:
    question: "Why topic modeling specifically?"
    required: true
    acceptable:
      - "Exploratory — discovering what themes exist"
      - "No predetermined categories"
      - "Too much text to read manually"
      - "Want data-driven themes"
    unacceptable:
      - "It's what people use"
      - "To analyze the text"
      - "To see what's there"
    if_unacceptable: |
      Topic modeling is ONE approach. It's good for:
      ✓ Exploration (what themes exist?)
      ✓ When you don't have predetermined categories
      ✓ Large corpora (thousands+ documents)
      
      It's NOT good for:
      ✗ Testing specific hypotheses
      ✗ When you already know categories (use classification)
      ✗ Short texts like tweets (consider BERTopic)
      ✗ Small datasets (<500 documents)
      
      Is topic modeling right for your question?

  q2_num_topics:
    question: "How many topics (K) and WHY?"
    required: true
    acceptable:
      - "Theory-driven: expect ~N themes based on [justification]"
      - "Will test multiple values and compare coherence"
      - "Domain expertise suggests ~N"
      - "Using auto-detection method"
    unacceptable:
      - "Whatever the model gives"
      - "10 seems reasonable"
      - "The default"
    if_unacceptable: |
      ⚠️ The number of topics is YOUR CHOICE, not the algorithm's.
      
      K=5 and K=50 give COMPLETELY different interpretations.
      Neither is objectively "correct."
      
      Approaches:
      1. THEORY-DRIVEN: "Literature suggests 8 main frames"
      2. EMPIRICAL: "Test K=5,10,15,20, evaluate coherence"
      3. DOMAIN EXPERTISE: "I know this field, expect ~12 themes"
      
      "10 seems reasonable" is not a justification.
      What's your approach?

  q3_preprocessing:
    question: "What preprocessing will you apply?"
    required: true
    must_specify:
      - "Stopword removal (which list?)"
      - "Lowercasing"
      - "Stemming/lemmatization (or not)"
      - "Minimum document frequency"
      - "Maximum document frequency"
      - "URL/mention handling"
    if_incomplete: |
      Preprocessing SHAPES your topics. Different choices → different topics.
      
      | Choice | Effect |
      |--------|--------|
      | Stopwords | Which words are "empty"? |
      | Stemming | "running" = "run"? Loses tense |
      | Min frequency | Rare words excluded |
      | Max frequency | Common words excluded |
      
      For social media, also consider:
      - Remove URLs? (lose content signal)
      - Remove @mentions? (lose interaction signal)
      - Remove hashtags? (often useful to keep)
      
      Specify your preprocessing pipeline.

  q4_document:
    question: "What counts as one 'document'?"
    required: true
    acceptable:
      - "Each tweet/post is a document"
      - "Aggregated by user"
      - "Aggregated by thread/conversation"
      - "Aggregated by time window (day/week)"
    unacceptable:
      - "The tweets"
      - "Each row"
    if_unacceptable: |
      Document definition affects results significantly.
      
      Options:
      - POST-LEVEL: Each tweet is a document
        → Pro: Granular
        → Con: Very short, topics may be incoherent
      
      - USER-LEVEL: All tweets by each user = one document
        → Pro: More text per document
        → Con: Mixes topics within user
      
      - THREAD-LEVEL: Conversation = one document
        → Pro: Coherent context
        → Con: May lose individual variation
      
      Which definition serves your RQ?

  q5_short_text:
    question: "How will you handle short documents?"
    required: true
    context: "Average document length in your data"
    acceptable:
      - "Aggregate short documents"
      - "Use BERTopic (handles short text better)"
      - "Set minimum length threshold"
      - "Acknowledge limitation"
    if_short_texts: |
      ⚠️ Short texts detected (avg < 50 words)
      
      Standard LDA assumes ~100+ words per document.
      Short documents → sparse, unreliable topics.
      
      Options:
      1. AGGREGATE: Combine by user/time/thread
      2. USE BERTOPIC: Designed for short text
      3. SET MINIMUM: Exclude documents < N words
      4. ACKNOWLEDGE: Report as limitation
      
      Your approach?

  q6_validation:
    question: "How will you validate topics are meaningful?"
    required: true
    acceptable:
      - "Read 20+ documents per topic before naming"
      - "Calculate coherence scores"
      - "Have domain expert review"
      - "Multiple researchers interpret independently"
    unacceptable:
      - "Look at top words"
      - "The model found them"
    if_unacceptable: |
      ⚠️ Topics are STATISTICAL ARTIFACTS, not ground truth.
      
      The model ALWAYS produces K topics.
      Doesn't mean K meaningful topics exist.
      
      Validation REQUIRES:
      1. READ actual documents in each topic (not just keywords)
      2. Can a human understand and name the topic?
      3. Do documents in the topic actually belong together?
      
      "Topic: [democracy, vote, election]" could be:
      - Pro-democracy discussion
      - Anti-democracy discussion  
      - Neutral news coverage
      - All mixed together
      
      How will you verify meaning?

  q7_naming:
    question: "Who will name topics and how?"
    required: true
    acceptable:
      - "Researcher names after reading 20+ documents"
      - "Multiple coders name independently, then reconcile"
      - "Domain expert validates names"
    unacceptable:
      - "Name based on top words"
      - "Let the model name them"
    if_unacceptable: |
      Topic NAMING is interpretation, not automatic.
      
      Bad practice: See [democracy, vote, freedom] → name "Pro-democracy"
      Good practice: Read 30 documents → "Mixed election discourse"
      
      Naming should be:
      - Based on actual documents, not just keywords
      - Conservative (don't over-interpret)
      - Validated by second reader
      
      Your naming protocol?
```

---

## Implementation

### LDA with Gensim

```python
"""
LDA Topic Modeling with validation and coherence.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from collections import Counter

class LDATopicModeler:
    """LDA topic modeling with full validation pipeline."""
    
    def __init__(self, 
                 num_topics: int,
                 min_doc_length: int = 20,
                 min_df: int = 5,
                 max_df_ratio: float = 0.5):
        """
        Args:
            num_topics: Number of topics (K)
            min_doc_length: Minimum words per document
            min_df: Minimum document frequency for words
            max_df_ratio: Maximum document frequency ratio for words
        """
        self.num_topics = num_topics
        self.min_doc_length = min_doc_length
        self.min_df = min_df
        self.max_df_ratio = max_df_ratio
        
        self.dictionary = None
        self.corpus = None
        self.model = None
        
    def preprocess(self, 
                   texts: List[str],
                   remove_stopwords: bool = True,
                   lemmatize: bool = True,
                   remove_urls: bool = True,
                   remove_mentions: bool = True,
                   custom_stopwords: List[str] = None) -> List[List[str]]:
        """
        Preprocess texts into tokens.
        
        Returns list of token lists.
        """
        import re
        import nltk
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        
        # Download required NLTK data
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('punkt', quiet=True)
        
        stop_words = set(stopwords.words('english'))
        if custom_stopwords:
            stop_words.update(custom_stopwords)
        
        lemmatizer = WordNetLemmatizer() if lemmatize else None
        
        processed = []
        excluded_short = 0
        
        for text in texts:
            # URL removal
            if remove_urls:
                text = re.sub(r'https?://\S+', '', text)
            
            # Mention removal
            if remove_mentions:
                text = re.sub(r'@\w+', '', text)
            
            # Basic cleaning
            text = re.sub(r'[^\w\s]', ' ', text.lower())
            
            # Tokenize
            tokens = text.split()
            
            # Remove stopwords
            if remove_stopwords:
                tokens = [t for t in tokens if t not in stop_words]
            
            # Lemmatize
            if lemmatize:
                tokens = [lemmatizer.lemmatize(t) for t in tokens]
            
            # Filter short tokens
            tokens = [t for t in tokens if len(t) > 2]
            
            # Check minimum length
            if len(tokens) >= self.min_doc_length:
                processed.append(tokens)
            else:
                excluded_short += 1
        
        print(f"Preprocessed {len(processed)} documents")
        print(f"Excluded {excluded_short} documents below min length ({self.min_doc_length})")
        
        return processed
    
    def fit(self, tokenized_docs: List[List[str]], 
            passes: int = 15,
            iterations: int = 400) -> 'LDATopicModeler':
        """
        Fit LDA model.
        """
        from gensim import corpora, models
        
        # Create dictionary
        self.dictionary = corpora.Dictionary(tokenized_docs)
        
        # Filter extremes
        self.dictionary.filter_extremes(
            no_below=self.min_df,
            no_above=self.max_df_ratio
        )
        
        # Create corpus
        self.corpus = [self.dictionary.doc2bow(doc) for doc in tokenized_docs]
        
        print(f"Dictionary size: {len(self.dictionary)}")
        print(f"Corpus size: {len(self.corpus)}")
        
        # Fit LDA
        self.model = models.LdaMulticore(
            corpus=self.corpus,
            id2word=self.dictionary,
            num_topics=self.num_topics,
            passes=passes,
            iterations=iterations,
            random_state=42
        )
        
        return self
    
    def get_topics(self, num_words: int = 10) -> List[Dict]:
        """Get topics with top words."""
        topics = []
        
        for idx in range(self.num_topics):
            words = self.model.show_topic(idx, num_words)
            topics.append({
                'topic_id': idx,
                'top_words': [w[0] for w in words],
                'word_weights': {w[0]: w[1] for w in words},
                'label': None,  # To be filled by human
                'validated': False
            })
        
        return topics
    
    def calculate_coherence(self, tokenized_docs: List[List[str]]) -> Dict:
        """Calculate coherence scores."""
        from gensim.models import CoherenceModel
        
        coherence_cv = CoherenceModel(
            model=self.model,
            texts=tokenized_docs,
            dictionary=self.dictionary,
            coherence='c_v'
        ).get_coherence()
        
        coherence_umass = CoherenceModel(
            model=self.model,
            corpus=self.corpus,
            dictionary=self.dictionary,
            coherence='u_mass'
        ).get_coherence()
        
        # Per-topic coherence
        topic_coherences = CoherenceModel(
            model=self.model,
            texts=tokenized_docs,
            dictionary=self.dictionary,
            coherence='c_v'
        ).get_coherence_per_topic()
        
        return {
            'coherence_cv': coherence_cv,
            'coherence_umass': coherence_umass,
            'per_topic': topic_coherences,
            'interpretation': self._interpret_coherence(coherence_cv)
        }
    
    def _interpret_coherence(self, cv_score: float) -> str:
        """Interpret coherence score."""
        if cv_score > 0.6:
            return "Good coherence — topics likely meaningful"
        elif cv_score > 0.4:
            return "Moderate coherence — review topics carefully"
        else:
            return "Low coherence — topics may be unreliable"
    
    def get_document_topics(self, 
                           tokenized_docs: List[List[str]],
                           threshold: float = 0.1) -> List[Dict]:
        """Get topic distribution for each document."""
        results = []
        
        for idx, doc in enumerate(tokenized_docs):
            bow = self.dictionary.doc2bow(doc)
            topic_dist = self.model.get_document_topics(bow, minimum_probability=threshold)
            
            # Get dominant topic
            if topic_dist:
                dominant = max(topic_dist, key=lambda x: x[1])
                results.append({
                    'doc_idx': idx,
                    'dominant_topic': dominant[0],
                    'dominant_prob': dominant[1],
                    'topic_distribution': dict(topic_dist),
                    'is_mixed': len([t for t in topic_dist if t[1] > 0.2]) > 1
                })
            else:
                results.append({
                    'doc_idx': idx,
                    'dominant_topic': None,
                    'dominant_prob': None,
                    'topic_distribution': {},
                    'is_mixed': False
                })
        
        return results
    
    def get_validation_documents(self, 
                                 tokenized_docs: List[List[str]],
                                 original_texts: List[str],
                                 docs_per_topic: int = 20) -> Dict[int, List[Dict]]:
        """
        Get sample documents for each topic for human validation.
        
        CRITICAL: Topics must be validated by reading actual documents,
        not just looking at top words.
        """
        doc_topics = self.get_document_topics(tokenized_docs)
        
        validation_docs = {i: [] for i in range(self.num_topics)}
        
        for doc_info in doc_topics:
            if doc_info['dominant_topic'] is not None:
                topic = doc_info['dominant_topic']
                if len(validation_docs[topic]) < docs_per_topic:
                    validation_docs[topic].append({
                        'doc_idx': doc_info['doc_idx'],
                        'text': original_texts[doc_info['doc_idx']],
                        'probability': doc_info['dominant_prob']
                    })
        
        return validation_docs


def find_optimal_k(tokenized_docs: List[List[str]], 
                   k_range: range = range(5, 21, 5)) -> Dict:
    """
    Test multiple K values and compare coherence.
    
    USE THIS to justify your K, not arbitrary choice.
    """
    results = []
    
    for k in k_range:
        print(f"Testing K={k}...")
        modeler = LDATopicModeler(num_topics=k)
        modeler.fit(tokenized_docs)
        coherence = modeler.calculate_coherence(tokenized_docs)
        
        results.append({
            'k': k,
            'coherence_cv': coherence['coherence_cv'],
            'coherence_umass': coherence['coherence_umass']
        })
    
    # Find best K
    best = max(results, key=lambda x: x['coherence_cv'])
    
    return {
        'results': results,
        'best_k': best['k'],
        'best_coherence': best['coherence_cv'],
        'recommendation': f"K={best['k']} has highest coherence ({best['coherence_cv']:.3f})"
    }
```

### BERTopic for Short Texts

```python
"""
BERTopic for short texts (tweets, comments, etc.)
"""

from bertopic import BERTopic
from typing import List, Dict, Optional
import pandas as pd

class BERTopicModeler:
    """BERTopic wrapper with validation."""
    
    def __init__(self, 
                 min_topic_size: int = 10,
                 n_gram_range: tuple = (1, 2)):
        """
        Args:
            min_topic_size: Minimum documents per topic
            n_gram_range: N-gram range for topic representation
        """
        self.min_topic_size = min_topic_size
        self.n_gram_range = n_gram_range
        self.model = None
        
    def fit(self, texts: List[str]) -> 'BERTopicModeler':
        """
        Fit BERTopic model.
        
        BERTopic automatically determines number of topics.
        """
        self.model = BERTopic(
            min_topic_size=self.min_topic_size,
            n_gram_range=self.n_gram_range,
            verbose=True
        )
        
        self.topics, self.probs = self.model.fit_transform(texts)
        
        print(f"Found {len(set(self.topics)) - 1} topics (excluding outliers)")
        
        return self
    
    def get_topic_info(self) -> pd.DataFrame:
        """Get topic information."""
        return self.model.get_topic_info()
    
    def get_topic_words(self, topic_id: int, n_words: int = 10) -> List[str]:
        """Get top words for a topic."""
        return [w[0] for w in self.model.get_topic(topic_id)[:n_words]]
    
    def get_document_topics(self, texts: List[str]) -> List[Dict]:
        """Get topic assignments for documents."""
        results = []
        
        for idx, (text, topic, prob) in enumerate(zip(texts, self.topics, self.probs)):
            results.append({
                'doc_idx': idx,
                'text': text[:200] + '...' if len(text) > 200 else text,
                'topic': topic,
                'probability': float(max(prob)) if hasattr(prob, '__iter__') else float(prob),
                'is_outlier': topic == -1
            })
        
        return results
    
    def reduce_topics(self, nr_topics: int):
        """Reduce to specific number of topics."""
        self.model.reduce_topics(self.texts, nr_topics=nr_topics)
        return self
    
    def visualize_topics(self):
        """Create interactive topic visualization."""
        return self.model.visualize_topics()
    
    def visualize_documents(self, texts: List[str]):
        """Create document visualization."""
        return self.model.visualize_documents(texts, self.topics)


def run_bertopic_analysis(texts: List[str],
                          min_topic_size: int = 10) -> Dict:
    """
    Complete BERTopic analysis pipeline.
    """
    modeler = BERTopicModeler(min_topic_size=min_topic_size)
    modeler.fit(texts)
    
    # Get results
    topic_info = modeler.get_topic_info()
    doc_topics = modeler.get_document_topics(texts)
    
    # Statistics
    n_outliers = sum(1 for d in doc_topics if d['is_outlier'])
    
    return {
        'model': modeler,
        'topic_info': topic_info,
        'document_topics': doc_topics,
        'n_topics': len(topic_info) - 1,  # Exclude outlier topic
        'n_outliers': n_outliers,
        'pct_outliers': n_outliers / len(texts) * 100
    }
```

---

## Validation Requirements

### Topic Validation Checklist

```yaml
validation_checklist:
  
  before_naming:
    - "Read at least 20 documents per topic"
    - "Check if documents in topic are coherent"
    - "Identify documents that don't fit"
    - "Note topic overlap or ambiguity"
  
  naming:
    - "Name conservatively (don't over-interpret)"
    - "Have second researcher validate names"
    - "Document naming rationale"
    - "Note limitations in topic definitions"
  
  reporting:
    - "Report coherence scores"
    - "Report number of topics tested"
    - "Report preprocessing choices"
    - "Include sample documents for each topic"
    - "Note outliers/unassigned documents"
```

### Coherence Thresholds

| Coherence (C_v) | Interpretation |
|-----------------|----------------|
| > 0.65 | Good — topics likely meaningful |
| 0.50 - 0.65 | Moderate — review carefully |
| 0.40 - 0.50 | Fair — may need adjustment |
| < 0.40 | Poor — reconsider approach |

---

## Reporting Template

```markdown
## Topic Modeling Methods

### Research Question
[How topic modeling addresses your RQ]

### Algorithm & Parameters
- **Algorithm**: [LDA / BERTopic / STM]
- **Number of topics (K)**: [N]
- **Justification for K**: [Theory / Empirical testing / Domain expertise]
- **Preprocessing**: [Describe all steps]

### K Selection (if empirical)
| K | Coherence (C_v) |
|---|-----------------|
| 5 | [value] |
| 10 | [value] |
| 15 | [value] |
Selected K=[N] based on [criteria]

### Coherence Scores
- **C_v**: [value] ([interpretation])
- **UMass**: [value]

### Topic Descriptions

| Topic | Label | Top Words | Documents | Validation |
|-------|-------|-----------|-----------|------------|
| 0 | [Name] | [words] | N (X%) | [who validated] |
| 1 | [Name] | [words] | N (X%) | [who validated] |
...

### Topic Validation
- **Documents read per topic**: [N]
- **Validator(s)**: [who]
- **Inter-validator agreement**: [if applicable]

### Limitations
1. [Limitation 1]
2. [Limitation 2]
```

---

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Naming from words only | May misinterpret topic | Read actual documents |
| Arbitrary K | Results are meaningless | Test multiple K values |
| No preprocessing documentation | Not reproducible | Document every step |
| Ignoring outliers | Losing data | Report and analyze outliers |
| Over-interpreting | Making claims data doesn't support | Be conservative |
