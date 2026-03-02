# Frame Analysis Method Skill

Systematic identification and analysis of frames in communication.

---

## Overview

**Framing** = selecting and emphasizing certain aspects of a perceived reality to promote a particular interpretation, evaluation, or solution.

Frame analysis is central to communication research, examining how:
- Media present issues (media frames)
- Audiences understand issues (audience frames)
- Elites construct issues (elite frames)

---

## Probing Questions (REQUIRED)

Before proceeding, specify:

```
Q1: What TYPE of framing are you studying?
    ✓ Media frames (how news covers an issue)
    ✓ Audience frames (how people interpret an issue)
    ✓ Strategic frames (how actors try to influence perception)
    ✗ "Just frames" — TOO VAGUE

Q2: Inductive or deductive approach?
    ✓ Inductive: Let frames emerge from data
    ✓ Deductive: Apply existing typology (specify which)
    ✗ "Both" without explanation — PICK PRIMARY

Q3: What's your unit of analysis?
    ✓ Article/post
    ✓ Paragraph
    ✓ Sentence
    ✓ Entire coverage period
    ✗ "The text" — BE SPECIFIC

Q4: What frame elements will you code?
    ✓ Problem definition
    ✓ Causal attribution
    ✓ Moral evaluation
    ✓ Treatment recommendation
    ✓ All four (Entman's framework)
    ✗ "The framing" — FRAMES HAVE COMPONENTS

Q5: How will you validate frame identification?
    ✓ Multiple coders + reliability
    ✓ Member checking (for audience frames)
    ✓ Citation of established typology
    ✗ "I'll know it when I see it" — UNACCEPTABLE
```

---

## Theoretical Foundations

### Entman's Framing Functions (1993)

Frames perform four functions:
1. **Define problems** — What is the issue?
2. **Diagnose causes** — Who/what is responsible?
3. **Make moral judgments** — Is it good/bad?
4. **Suggest remedies** — What should be done?

### Generic vs Issue-Specific Frames

**Generic frames** (apply across issues):
- Conflict frame
- Human interest frame
- Economic consequences frame
- Morality frame
- Responsibility frame

**Issue-specific frames** (developed for particular topics):
- Immigration: "threat" vs "humanitarian" vs "economic contributor"
- Climate: "scientific consensus" vs "uncertainty" vs "economic cost"
- Health: "individual responsibility" vs "systemic factors"

---

## Approaches

### 1. Manual Frame Analysis (Gold Standard)

Traditional qualitative or quantitative content analysis:

```python
def manual_frame_analysis_workflow():
    """
    Workflow for rigorous manual frame analysis.
    """
    
    steps = {
        1: "Sample selection",
        2: "Initial reading (immersion)",
        3: "Frame identification (inductive) OR codebook application (deductive)",
        4: "Codebook development/refinement",
        5: "Coder training",
        6: "Independent coding",
        7: "Reliability calculation",
        8: "Disagreement resolution",
        9: "Final coding",
        10: "Analysis and interpretation"
    }
    
    return steps
```

**Codebook Template:**
```markdown
# Frame Analysis Codebook

## Frame: [Frame Name]

**Definition:** 
[Clear, operational definition of what this frame entails]

**Indicators (code as present if ANY appear):**
- [Specific phrase, term, or argument pattern]
- [Another indicator]
- [Another indicator]

**Examples:**
> "Quote that exemplifies this frame" — Source

**Non-examples (to clarify boundaries):**
> "Quote that might seem like this frame but isn't" — Reason why

**Coding rule:** Code [unit] as having this frame if [specific criterion].
```

### 2. LLM-Assisted Frame Identification

Use LLMs to scale frame analysis:

```python
def llm_frame_detection(text, frames, definitions, client):
    """
    LLM-assisted frame detection.
    
    Args:
        text: Content to analyze
        frames: List of frame names
        definitions: Dict mapping frame to definition
    """
    
    definitions_text = "\n\n".join([
        f"**{frame}:** {defn}" 
        for frame, defn in definitions.items()
    ])
    
    prompt = f"""You are a trained content analyst identifying frames in text.

## Frame Definitions

{definitions_text}

## Text to Analyze

"{text}"

## Task

Identify which frame(s) are present in this text. For each frame detected:
1. State the frame name
2. Quote the specific evidence (exact words from text)
3. Explain why this evidence indicates the frame

If no frames are clearly present, state "No clear frame detected."

Multiple frames can be present in one text.

## Response Format

FRAME: [name]
EVIDENCE: "[quote]"
REASONING: [explanation]

FRAME: [name]
EVIDENCE: "[quote]"
REASONING: [explanation]

[etc.]
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    return parse_frame_response(response.choices[0].message.content)
```

### 3. Computational Frame Analysis

Automated approaches for large-scale analysis:

#### Topic Models as Frame Proxies

```python
def topic_to_frame_analysis(corpus, n_topics=10):
    """
    Use topic modeling to identify potential frames.
    
    Note: Topics ≠ frames, but can indicate frame packages.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF
    
    # NMF often more interpretable for framing
    vectorizer = TfidfVectorizer(
        max_df=0.95, 
        min_df=5,
        stop_words='english'
    )
    tfidf = vectorizer.fit_transform(corpus)
    
    nmf = NMF(n_components=n_topics, random_state=42)
    doc_topics = nmf.fit_transform(tfidf)
    
    # Get top words per topic
    feature_names = vectorizer.get_feature_names_out()
    topics = {}
    for topic_idx, topic in enumerate(nmf.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-15:-1]]
        topics[topic_idx] = top_words
    
    # NOTE: These are NOT frames yet!
    # Researcher must interpret topics and validate as frames
    
    return doc_topics, topics
```

#### Keyword Co-occurrence

```python
def frame_signature_detection(texts, frame_lexicons):
    """
    Detect frames via keyword co-occurrence patterns.
    
    frame_lexicons: Dict mapping frame name to keyword list
    """
    import numpy as np
    
    results = []
    
    for text in texts:
        text_lower = text.lower()
        scores = {}
        
        for frame, keywords in frame_lexicons.items():
            # Count keyword occurrences
            count = sum(1 for kw in keywords if kw.lower() in text_lower)
            # Normalize by lexicon size
            scores[frame] = count / len(keywords)
        
        # Determine dominant frame
        if max(scores.values()) > 0.1:  # Threshold for detection
            dominant = max(scores, key=scores.get)
        else:
            dominant = "None detected"
        
        results.append({
            'text': text,
            'scores': scores,
            'dominant_frame': dominant
        })
    
    return results
```

#### Embedding-Based Frame Classification

```python
def embedding_frame_classifier(texts, labeled_examples, model_name='all-MiniLM-L6-v2'):
    """
    Classify frames using sentence embeddings.
    
    labeled_examples: Dict mapping frame to list of example texts
    """
    from sentence_transformers import SentenceTransformer
    from sklearn.neighbors import KNeighborsClassifier
    import numpy as np
    
    model = SentenceTransformer(model_name)
    
    # Embed labeled examples
    train_texts = []
    train_labels = []
    for frame, examples in labeled_examples.items():
        train_texts.extend(examples)
        train_labels.extend([frame] * len(examples))
    
    train_embeddings = model.encode(train_texts)
    
    # Train classifier
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(train_embeddings, train_labels)
    
    # Classify new texts
    new_embeddings = model.encode(texts)
    predictions = classifier.predict(new_embeddings)
    probabilities = classifier.predict_proba(new_embeddings)
    
    return predictions, probabilities
```

---

## Validation Requirements

### For Manual Analysis

```yaml
manual_validation:
  minimum_coders: 2
  reliability_metric: Krippendorff's alpha or Cohen's κ
  acceptable_threshold: 
    κ >= 0.70 (good)
    κ >= 0.80 (excellent)
  
  process:
    1. Train coders with codebook + examples
    2. Practice coding session (discuss disagreements)
    3. Independent coding of reliability sample (20%+)
    4. Calculate reliability
    5. If below threshold: refine codebook, retrain
    6. Document final reliability in paper
```

### For LLM-Assisted Analysis

```yaml
llm_validation:
  human_sample: 200+ items
  comparison: LLM vs human coders
  report:
    - Agreement rate
    - Cohen's κ or equivalent
    - False positive/negative patterns
    - Frames where LLM struggles
  
  process:
    1. Develop codebook (human-created)
    2. Human-code validation sample
    3. LLM-code same sample
    4. Compare results
    5. If κ < 0.70: refine prompt, try different model
    6. Document discrepancies in paper
```

### For Computational Analysis

```yaml
computational_validation:
  human_interpretation: Required
  steps:
    1. Run computational analysis
    2. Human interprets output (e.g., topic → frame?)
    3. Validate interpretation:
       - Read documents in each cluster
       - Check if frame label fits
       - Multiple researchers agree on labels
    4. Cross-validate with manual coding subset
```

---

## Common Frame Typologies

### Semetko & Valkenburg (2000) — News Frames

```python
GENERIC_NEWS_FRAMES = {
    'conflict': {
        'definition': 'Emphasizes conflict between individuals, groups, or institutions',
        'indicators': [
            'disagreement', 'clash', 'battle', 'fight',
            'two sides', 'versus', 'opposition', 'debate'
        ]
    },
    'human_interest': {
        'definition': 'Brings a human face or emotional angle to the issue',
        'indicators': [
            'personal story', 'individual experience', 'emotional',
            'human cost', 'family', 'victim', 'survivor'
        ]
    },
    'economic_consequences': {
        'definition': 'Focuses on economic impact',
        'indicators': [
            'cost', 'profit', 'economic', 'financial',
            'jobs', 'business', 'market', 'price'
        ]
    },
    'morality': {
        'definition': 'Puts the issue in context of moral or religious tenets',
        'indicators': [
            'moral', 'ethical', 'values', 'right', 'wrong',
            'religious', 'principles', 'justice'
        ]
    },
    'responsibility': {
        'definition': 'Attributes responsibility for cause or solution',
        'indicators': [
            'government should', 'blame', 'responsible',
            'accountable', 'fault', 'duty', 'obligation'
        ]
    }
}
```

### Issue-Specific Examples

#### Immigration Frames
```python
IMMIGRATION_FRAMES = {
    'threat': ['illegal', 'invasion', 'crime', 'security', 'border'],
    'humanitarian': ['refugee', 'asylum', 'human rights', 'families', 'children'],
    'economic': ['workers', 'jobs', 'labor', 'contribution', 'economy'],
    'legal': ['legal status', 'documentation', 'visa', 'citizenship', 'law'],
    'cultural': ['assimilation', 'integration', 'diversity', 'values', 'identity']
}
```

#### Climate Change Frames
```python
CLIMATE_FRAMES = {
    'scientific_certainty': ['consensus', 'evidence', 'research', 'scientists agree'],
    'uncertainty': ['debate', 'uncertain', 'question', 'some scientists'],
    'economic_opportunity': ['green jobs', 'innovation', 'growth', 'opportunity'],
    'economic_threat': ['cost', 'regulation', 'burden', 'jobs lost'],
    'moral_duty': ['future generations', 'responsibility', 'planet', 'moral'],
    'national_security': ['security', 'threat', 'migration', 'conflict', 'stability']
}
```

---

## Analysis Workflow

### Inductive Frame Analysis

```python
def inductive_frame_workflow(corpus, sample_size=100):
    """
    Discover frames from data (grounded approach).
    """
    
    workflow = {
        'step_1': {
            'action': 'Random sample of texts',
            'size': sample_size,
            'output': 'initial_sample.csv'
        },
        'step_2': {
            'action': 'Open coding',
            'process': 'Read each text, note recurring themes/arguments',
            'output': 'open_codes.md'
        },
        'step_3': {
            'action': 'Axial coding',
            'process': 'Group open codes into potential frames',
            'output': 'candidate_frames.md'
        },
        'step_4': {
            'action': 'Frame definition',
            'process': 'Define each frame with indicators and examples',
            'output': 'codebook_v1.md'
        },
        'step_5': {
            'action': 'Pilot coding',
            'process': 'Apply codebook to new sample, refine',
            'output': 'codebook_v2.md'
        },
        'step_6': {
            'action': 'Reliability testing',
            'process': 'Two+ coders, calculate agreement',
            'output': 'reliability_report.md'
        },
        'step_7': {
            'action': 'Full coding',
            'process': 'Apply finalized codebook to corpus',
            'output': 'coded_data.csv'
        }
    }
    
    return workflow
```

### Deductive Frame Analysis

```python
def deductive_frame_workflow(corpus, existing_typology):
    """
    Apply existing frame typology to new data.
    """
    
    workflow = {
        'step_1': {
            'action': 'Adapt existing codebook',
            'process': 'Review typology, adapt for your context',
            'cite': existing_typology
        },
        'step_2': {
            'action': 'Pilot test',
            'process': 'Apply to small sample, check fit',
            'note': 'May need to add/drop frames for your context'
        },
        'step_3': {
            'action': 'Coder training',
            'process': 'Train coders on adapted codebook'
        },
        'step_4': {
            'action': 'Reliability testing',
            'process': 'Independent coding, calculate agreement'
        },
        'step_5': {
            'action': 'Full coding',
            'process': 'Apply to full corpus'
        },
        'step_6': {
            'action': 'Report adaptation',
            'process': 'Document how you adapted original typology'
        }
    }
    
    return workflow
```

---

## Output Format

```yaml
# frame_analysis_results.yaml

metadata:
  approach: inductive | deductive
  typology_source: "[citation if deductive]"
  unit: article | paragraph | sentence
  corpus_size: 5000
  coded_by: human | llm | hybrid
  
frames_identified:
  - name: "Threat Frame"
    definition: "Presents issue as danger to security/safety"
    frequency: 0.23
    examples:
      - text: "The policy poses a clear danger to national security"
        source: article_123
    indicators:
      - "danger"
      - "threat"
      - "security"
    entman_functions:
      problem: "Policy endangers nation"
      cause: "Foreign actors/poor policy"
      moral: "Security is paramount"
      remedy: "Protective measures needed"

validation:
  coders: 2
  reliability_sample: 500
  cohens_kappa: 0.78
  per_frame_kappa:
    threat: 0.82
    opportunity: 0.75
    neutral: 0.71

distribution:
  threat: 1150
  opportunity: 850
  neutral: 3000
```

---

## Common Mistakes

```yaml
mistakes:
  - mistake: "Treating topic as frame"
    example: "'Immigration' is not a frame; how immigration is presented is the frame"
    fix: "Focus on how the issue is characterized, not what the issue is"
    
  - mistake: "Single-coder analysis"
    example: "I coded all 5000 articles myself"
    fix: "Frame identification requires inter-coder reliability"
    
  - mistake: "Keyword counting as frame analysis"
    example: "Counted 'crime' mentions as 'threat frame'"
    fix: "Frames are arguments, not just words. Context matters."
    
  - mistake: "No definition of frames"
    example: "We identified three frames: positive, negative, neutral"
    fix: "Define what makes each frame distinct. Those are valences, not frames."
    
  - mistake: "Ignoring frame elements"
    example: "We found the economic frame"
    fix: "Specify: economic cost, economic opportunity, economic responsibility?"
```

---

## Key Citations

- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*.
- Semetko, H. A., & Valkenburg, P. M. (2000). Framing European politics. *Journal of Communication*.
- Matthes, J., & Kohring, M. (2008). The content analysis of media frames. *Journal of Communication*.
- Chong, D., & Druckman, J. N. (2007). Framing theory. *Annual Review of Political Science*.
- Baden, C. (2018). Reconstructing frames: From isolated frame elements to coherent frame configurations. *Journalism Studies*.

---

*Part of Communication Research Skill for OpenClaw*
