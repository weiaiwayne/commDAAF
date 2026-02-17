# Stage-Agnostic Research Support

This skill supports researchers at ANY stage of the research process — not just end-to-end pipelines.

---

## Entry Points

```
┌─────────────────────────────────────────────────────────────────────┐
│                     WHERE ARE YOU IN YOUR RESEARCH?                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  🔍 EXPLORATION         📋 VALIDATION         📊 INTERPRETATION     │
│  "I have data,          "I have code/         "I have outputs,      │
│   what's in it?"         analysis, is          what do they         │
│                          it sound?"             mean?"               │
│                                                                      │
│  → explore              → validate             → interpret           │
│  → discover             → audit                → critique            │
│  → profile              → review               → contextualize       │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  🛠️ EXECUTION           📝 DOCUMENTATION       🔄 REVISION          │
│  "Run this              "Help me write         "My results seem     │
│   analysis"              this up"               off, help debug"     │
│                                                                      │
│  → run                  → document             → debug               │
│  → analyze              → methods section      → diagnose            │
│  → compute              → report               → revise              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1: EXPLORATION

**You have:** Raw data, no clear hypothesis yet  
**You want:** Understand what's in the data, generate hypotheses

### Triggers
```
"I have this dataset, what's in it?"
"Explore this data"
"What can I study with this?"
"Profile this dataset"
"First look at [data]"
```

### What the System Does

```python
def exploration_workflow(data_path):
    """
    First-look exploration of a dataset.
    NO analysis decisions yet — just profiling.
    """
    
    return {
        'step_1': {
            'name': 'Data profiling',
            'actions': [
                'Load and validate schema',
                'Count rows, columns, missing values',
                'Identify date range',
                'Sample 10 random items for inspection'
            ]
        },
        'step_2': {
            'name': 'Content overview',
            'actions': [
                'Language distribution',
                'Top hashtags/keywords',
                'Temporal distribution (posts over time)',
                'User/account distribution'
            ]
        },
        'step_3': {
            'name': 'Descriptive statistics',
            'actions': [
                'Engagement metrics distribution',
                'Text length distribution',
                'Network density (if relational data)'
            ]
        },
        'step_4': {
            'name': 'Potential research directions',
            'output': 'Based on what I see, you could study...',
            'note': 'These are SUGGESTIONS, not prescriptions'
        }
    }
```

### Example Interaction

```
User: I have 50,000 Telegram posts about health supplements. What's here?

Agent: 
📊 **Dataset Profile: health_supplements.csv**

**Basics:**
- 50,234 posts from 127 channels
- Date range: 2024-03-01 to 2024-09-30
- Languages: English (78%), Spanish (12%), Portuguese (8%), Other (2%)
- Missing text: 0.3%

**Content Overview:**
- Top terms: [supplement, natural, detox, immune, wellness]
- Top hashtags: [#naturalhealth, #detox, #wellness]
- Avg post length: 234 characters
- URLs present in: 67% of posts

**Temporal Pattern:**
- Peak activity: Mondays and Thursdays
- Spike detected: April 15-20 (investigate?)

**Engagement:**
- Median views: 1,234
- Median forwards: 12
- High-engagement outliers: 847 posts (>10K views)

**Potential Research Directions:**
1. Health misinformation prevalence (needs codebook)
2. Cross-channel coordination (many channels share same URLs)
3. Commercial vs informational content distinction
4. Temporal response to health news events

⚠️ These are observations, not conclusions. 
What interests you? I can help scope a specific study.
```

---

## Stage 2: VALIDATION / AUDIT

**You have:** Existing code, analysis, or methodology  
**You want:** Someone to check if it's sound

### Triggers
```
"Review my analysis code"
"Is this methodology sound?"
"Audit my approach"
"Check my script"
"Validate my methods"
"What's wrong with this?"
```

### What the System Does

```python
def validation_workflow(artifact_type, artifact_path):
    """
    Audit existing research artifacts.
    
    artifact_type: 'code' | 'methodology' | 'codebook' | 'analysis'
    """
    
    if artifact_type == 'code':
        return code_review(artifact_path)
    elif artifact_type == 'methodology':
        return methodology_audit(artifact_path)
    elif artifact_type == 'codebook':
        return codebook_review(artifact_path)
    elif artifact_type == 'analysis':
        return analysis_audit(artifact_path)

def code_review(script_path):
    """Review analysis code for issues."""
    
    checks = {
        'correctness': [
            'Syntax errors',
            'Logic errors',
            'Edge cases handled?',
            'Error handling present?'
        ],
        'reproducibility': [
            'Random seeds set?',
            'Dependencies documented?',
            'Hardcoded paths?',
            'Version-specific code?'
        ],
        'methodology': [
            'Parameters justified?',
            'Validation included?',
            'Appropriate for data type?',
            'Known limitations of approach?'
        ],
        'documentation': [
            'Code comments adequate?',
            'Function docstrings?',
            'README present?'
        ]
    }
    
    return checks

def methodology_audit(methods_description):
    """Audit research methodology for soundness."""
    
    return {
        'internal_validity': [
            'Are constructs well-defined?',
            'Is measurement appropriate?',
            'Are confounds addressed?'
        ],
        'external_validity': [
            'Is sample representative?',
            'Are findings generalizable?',
            'Time/context limitations?'
        ],
        'reliability': [
            'Would another researcher get same results?',
            'Are procedures documented enough to replicate?',
            'Inter-coder reliability (if applicable)?'
        ],
        'ethical_considerations': [
            'IRB/ethics addressed?',
            'Privacy protected?',
            'Potential harms considered?'
        ]
    }
```

### Example Interaction

```
User: Can you review this sentiment analysis script?

Agent:
📋 **Code Review: sentiment_analysis.py**

**✅ PASSED:**
- Syntax valid
- VADER implementation correct
- Output format reasonable

**⚠️ WARNINGS:**

1. **No random seed** (line 45)
   ```python
   # Current
   sample = df.sample(200)
   
   # Recommended
   sample = df.sample(200, random_state=42)
   ```
   Impact: Validation sample not reproducible

2. **Hardcoded threshold** (line 67)
   ```python
   df['sentiment'] = df['compound'].apply(
       lambda x: 'pos' if x > 0.05 else ('neg' if x < -0.05 else 'neu')
   )
   ```
   Question: Why ±0.05? This should be justified or parameterized.

3. **No sarcasm handling** 
   VADER will misclassify sarcastic content. For political/social media 
   data, this could be 5-15% of posts. Consider:
   - LLM pre-filter for sarcasm
   - Acknowledge as limitation
   - Manual review of "positive" items with negative context words

**❌ ISSUES:**

4. **Validation sample too small** (line 78)
   ```python
   validation_sample = df.sample(50)
   ```
   50 is insufficient. Minimum 200 recommended for reliable κ.

5. **Missing neutral category handling** (line 71)
   67% of your data is classified "neutral" — is this expected?
   If not, threshold may be too strict.

**Suggested fixes attached. Want me to revise the script?**
```

---

## Stage 3: INTERPRETATION / CRITIQUE

**You have:** Analysis outputs, results, findings  
**You want:** Help understanding what they mean, identifying issues

### Triggers
```
"What do these results mean?"
"Interpret these findings"
"Critique my analysis"
"Does this make sense?"
"Help me understand this output"
"Are these results plausible?"
```

### What the System Does

```python
def interpretation_workflow(results, context):
    """
    Interpret and critique analysis outputs.
    
    results: The actual outputs (tables, figures, metrics)
    context: What analysis was run, on what data
    """
    
    return {
        'step_1': {
            'name': 'Sanity check',
            'questions': [
                'Are these results plausible?',
                'Do magnitudes make sense?',
                'Any obvious red flags?'
            ]
        },
        'step_2': {
            'name': 'Substantive interpretation',
            'questions': [
                'What do these findings mean for your RQ?',
                'How do they compare to prior literature?',
                'What mechanisms could explain this?'
            ]
        },
        'step_3': {
            'name': 'Alternative explanations',
            'questions': [
                'What else could produce these results?',
                'Confounds? Selection effects?',
                'Measurement artifacts?'
            ]
        },
        'step_4': {
            'name': 'Limitations',
            'questions': [
                'What can you NOT conclude from this?',
                'What caveats should accompany claims?'
            ]
        }
    }
```

### Example Interaction

```
User: I ran coordination detection and 73% of accounts show coordinated 
behavior. What does this mean?

Agent:
🚨 **Sanity Check: FAILED**

73% coordination is implausibly high. Typical findings:
- Most studies: 1-15%
- High-coordination events: 20-30%
- 73% suggests: **parameter issue or definition error**

**Diagnostic Questions:**

1. **Time threshold?**
   If threshold is >1 hour, you're detecting "same day posting" 
   not "coordination." What's your current setting?

2. **Content signal?**
   If matching on common hashtags (#news, #politics), you'll 
   get false positives. What are you matching on?

3. **Baseline comparison?**
   Did you compare to expected co-sharing rate? Many communities 
   legitimately share the same content.

**Before interpreting, let's diagnose:**
```
/diagnose coordination_results.csv
```

---

If this IS real (rare), possible interpretations:
- Data is from a single campaign/operation
- Very narrow topic where sharing is expected
- Platform-specific behavior (some Telegram channels cross-post everything)

But **most likely**: parameters need adjustment. Let's check.
```

### Critique Mode

For reviewing draft findings:

```
User: Here's my findings section. Critique it.

Agent:
📝 **Critique: Findings Section**

**Claim 1:** "We found strong evidence of coordinated inauthentic behavior."

⚠️ **Issues:**
- "Inauthentic" is not established — you detected coordination patterns
- "Strong evidence" — what's your threshold? p-value? Effect size?
- Recommendation: "We observed coordination patterns consistent with [X]"

**Claim 2:** "Bots were responsible for 30% of the discourse."

❌ **Problem:**
- Your method (temporal co-posting) cannot determine bot vs human
- This claim is not supported by your methodology
- Recommendation: Remove or change to "Accounts exhibiting automated 
  posting patterns contributed to 30% of posts"

**Claim 3:** "The campaign was likely foreign-originated."

❌ **Problem:**
- What evidence supports foreign origin?
- Temporal coordination doesn't indicate geography
- This is a significant attribution requiring additional evidence
- Recommendation: Remove unless you have corroborating evidence

**Overall:**
Your detection is solid. Your interpretation overreaches.
Dial back claims to what your method actually supports.

Want me to suggest revised language?
```

---

## Stage 4: EXECUTION

**You have:** Clear plan, validated methodology  
**You want:** Run the analysis

### Triggers
```
"Run this analysis"
"Execute this pipeline"
"Analyze [data] with [method]"
"Compute [metrics]"
```

### What the System Does

Standard execution with checkpoints (existing workflow).

---

## Stage 5: DOCUMENTATION

**You have:** Completed analysis, results  
**You want:** Help writing it up

### Triggers
```
"Write methods section"
"Document this analysis"
"Generate report"
"Help me write up [results]"
```

### What the System Does

```python
def documentation_workflow(project_state):
    """Generate publication-ready documentation."""
    
    outputs = {
        'methods_section': generate_methods(project_state),
        'results_section': generate_results(project_state),
        'limitations': generate_limitations(project_state),
        'data_availability': generate_data_statement(project_state),
        'reproducibility_package': generate_repo_structure(project_state)
    }
    
    return outputs
```

### Example: Auto-Generated Methods Section

```
User: Generate methods section for my sentiment analysis

Agent:
## Methods

### Data Collection
Data were collected from [PLATFORM] between [START_DATE] and [END_DATE] 
using [METHOD]. The initial dataset contained N=[N_RAW] posts.

### Sample
After applying inclusion criteria ([CRITERIA]), the final analytical 
sample contained N=[N_FINAL] posts from [N_USERS] unique accounts.

### Sentiment Analysis
Sentiment was operationalized as [DEFINITION]. We used [TOOL] 
(version [VERSION]) to classify posts as positive, negative, or neutral. 
Posts with compound scores above [THRESHOLD] were classified as positive, 
below -[THRESHOLD] as negative, and between as neutral.

#### Sarcasm Handling
[SARCASM_STRATEGY]

#### Validation
A random sample of [N_VAL] posts was independently coded by [N_CODERS] 
human coders. Inter-rater reliability between human coders was κ=[HUMAN_K]. 
Agreement between the automated classifier and human gold standard was 
κ=[MACHINE_K], indicating [INTERPRETATION].

### Limitations
[AUTO_GENERATED_LIMITATIONS]

---
*[Edit placeholders with your actual values]*
```

---

## Stage 6: REVISION / DEBUGGING

**You have:** Results that seem wrong, or analysis that failed  
**You want:** Help fixing it

### Triggers
```
"My results seem wrong"
"This doesn't look right"
"Debug this analysis"
"Why am I getting [unexpected result]?"
"Help me fix this"
```

### What the System Does

```python
def debugging_workflow(problem_description, artifacts):
    """
    Diagnose and fix research problems.
    """
    
    return {
        'step_1': {
            'name': 'Reproduce the problem',
            'action': 'Run the analysis and observe the issue'
        },
        'step_2': {
            'name': 'Isolate the cause',
            'checks': [
                'Data quality issue?',
                'Parameter setting?',
                'Code bug?',
                'Method mismatch?',
                'Expected behavior, unexpected interpretation?'
            ]
        },
        'step_3': {
            'name': 'Propose fixes',
            'action': 'Generate solutions for identified cause'
        },
        'step_4': {
            'name': 'Verify fix',
            'action': 'Re-run and confirm resolution'
        }
    }
```

### Example Interaction

```
User: My topic model keeps giving me topics that don't make sense.
      Topic 1 is ["the", "and", "to", "a"] — that's just stopwords.

Agent:
🔧 **Diagnosis: Topic Modeling Failure**

**Identified Issue:** Stopwords appearing in topics

**Likely Causes:**

1. **Stopwords not removed** (most likely)
   Check your preprocessing:
   ```python
   # Current (probably)
   vectorizer = CountVectorizer()
   
   # Should be
   vectorizer = CountVectorizer(stop_words='english')
   ```

2. **Wrong stopword list**
   English stopwords won't help if data is multilingual.
   What languages are in your data?

3. **Stopwords in topic display, not model**
   Some topic models remove stopwords for modeling but 
   include them in display. Check display code.

**Quick fix:**

```python
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Add custom stopwords for social media
custom_stops = list(ENGLISH_STOP_WORDS) + ['https', 'http', 'rt', 'amp']

vectorizer = CountVectorizer(
    stop_words=custom_stops,
    min_df=5,      # Ignore rare words
    max_df=0.95    # Ignore words in >95% of docs
)
```

Want me to review your full preprocessing pipeline?
```

---

## Implementation: Stage Detection

```python
def detect_research_stage(user_message, context):
    """
    Detect which research stage the user is in.
    """
    
    stage_patterns = {
        'exploration': [
            r"what's in (this|my|the) (data|dataset)",
            r"explore",
            r"first look",
            r"profile",
            r"what can I (study|do with)"
        ],
        'validation': [
            r"review (my|this)",
            r"audit",
            r"check (my|this)",
            r"is (this|my).*(sound|correct|right)",
            r"validate",
            r"what's wrong with"
        ],
        'interpretation': [
            r"what (do|does) (this|these) (mean|suggest)",
            r"interpret",
            r"critique",
            r"(does|do) (this|these) make sense",
            r"are (these|this) results? (plausible|reasonable)"
        ],
        'execution': [
            r"run (this|the) analysis",
            r"execute",
            r"analyze .* (with|using)",
            r"compute"
        ],
        'documentation': [
            r"write .* section",
            r"document",
            r"generate report",
            r"help me write"
        ],
        'debugging': [
            r"(seems?|look) wrong",
            r"doesn't (look|seem) right",
            r"debug",
            r"fix (this|my)",
            r"why (am I|is it) getting"
        ]
    }
    
    for stage, patterns in stage_patterns.items():
        for pattern in patterns:
            if re.search(pattern, user_message.lower()):
                return stage
    
    # Default: ask
    return 'unknown'
```

---

## Stage-Specific Probing

Different stages need different questions:

| Stage | Probing Focus |
|-------|---------------|
| **Exploration** | What's your general interest area? Any hypotheses? |
| **Validation** | What are you trying to accomplish? Known concerns? |
| **Interpretation** | What was your hypothesis? What did you expect? |
| **Execution** | Params specified? Validation plan? |
| **Documentation** | Target venue? Word limits? |
| **Debugging** | What did you expect vs what happened? |

---

## Example: Multi-Stage Session

```
Session 1 - Exploration:
User: I have data from a Telegram health group. What's here?
Agent: [Profiles data, suggests directions]

Session 2 - Execution:
User: Let's do coordination detection on this.
Agent: [Probing questions, then runs analysis]

Session 3 - Interpretation:
User: I got these results. 15% show coordination. Is that meaningful?
Agent: [Contextualizes against literature, suggests interpretations]

Session 4 - Validation:
User: Here's my code. Review it before I finalize?
Agent: [Code review, identifies issues]

Session 5 - Documentation:
User: Write up the methods section.
Agent: [Generates methods text from project state]
```

---

*Meet researchers where they are, not where you assume they are.*
