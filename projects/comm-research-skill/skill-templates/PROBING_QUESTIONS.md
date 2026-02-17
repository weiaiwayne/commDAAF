# Master Probing Questions Index

Complete set of probing questions for all methods. System MUST ask these before proceeding.

---

## Quick Reference

| Method | Critical Questions | Minimum Specificity |
|--------|-------------------|---------------------|
| **Sentiment Analysis** | Construct, unit, tool, neutral handling, sarcasm strategy | All 6 required |
| **Topic Modeling** | Purpose, K value, preprocessing, validation, naming | All 7 required |
| **Network Analysis** | Nodes/edges, theoretical justification, centrality meaning | All 5 required |
| **Coordinated Behavior** | Operational definition, organic vs coordinated, conclusions | All 5 required |
| **LLM Annotation** | Categories, validation plan, prompt design | All 4 required |
| **Content Analysis** | Codebook, reliability plan, sampling | All 6 required |

---

## 1. SENTIMENT ANALYSIS

### Required Before Proceeding

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
    ✓ Acknowledge as limitation with estimate
    ✗ "The tool handles it" — IT DOESN'T

Q6: What's your validation plan?
    ✓ Human sample (N ≥ 200)
    ✓ Calculate agreement (κ)
    ✗ "The model is validated" — NOT ON YOUR DATA
```

---

## 2. TOPIC MODELING

### Required Before Proceeding

```
Q1: Why topic modeling specifically?
    ✓ Exploratory — discovering themes
    ✓ No predetermined categories
    ✓ Large corpus, can't read manually
    ✗ "To analyze the text" — TOO VAGUE
    ✗ "It's what people use" — NOT A REASON

Q2: How many topics (K) and WHY?
    ✓ Theory-driven expectation
    ✓ Will test multiple K values
    ✓ Domain expertise estimate
    ✗ "Whatever the model gives" — YOUR CHOICE, NOT MODEL'S
    ✗ "10 seems reasonable" — NOT A JUSTIFICATION

Q3: What preprocessing will you apply?
    Must specify ALL of:
    - Stopwords (which list?)
    - Stemming/lemmatization
    - Min/max document frequency
    - URL/mention handling
    
Q4: What counts as one 'document'?
    ✓ Each post
    ✓ Aggregated by user
    ✓ Aggregated by thread
    ✗ "The tweets" — BE SPECIFIC

Q5: How will you handle short documents?
    ✓ Aggregate
    ✓ Use BERTopic
    ✓ Set minimum length
    Required if avg doc length < 50 words

Q6: How will you validate topics are meaningful?
    ✓ Read 20+ documents per topic
    ✓ Calculate coherence scores
    ✓ Domain expert review
    ✗ "Look at top words" — INSUFFICIENT
    ✗ "The model found them" — NOT VALIDATION

Q7: Who will name topics and how?
    ✓ After reading documents
    ✓ Multiple coders independently
    ✗ "From top words" — OFTEN MISLEADING
```

---

## 3. NETWORK ANALYSIS

### Required Before Proceeding

```
Q1: What are your nodes and what are your edges?
    Must be SPECIFIC:
    ✓ "Nodes = users, edges = mentions"
    ✓ "Nodes = posts, edges = shared URLs"
    ✗ "The network" — NOT A DEFINITION
    ✗ "Connections" — WHAT KIND?

Q2: Is the network directed or undirected? Why?
    ✓ Directed (A→B means something)
    ✓ Undirected (connection is symmetric)
    Must justify choice for network type

Q3: What's the theoretical reason for this structure?
    ✓ Connected to RQ
    ✓ Grounded in theory
    ✗ "It's what you can do with data" — NOT THEORETICAL

Q4: What do you expect high centrality to mean?
    ✓ Influence (with caveats)
    ✓ Bridging between communities
    ✓ Attention received
    ✗ "Importance" — IMPORTANCE FOR WHAT?
    ✗ "They're central" — TAUTOLOGY

Q5: How will you handle isolates and boundary issues?
    ✓ Remove with justification
    ✓ Keep and report
    ✓ Analyze separately
```

---

## 4. COORDINATED BEHAVIOR DETECTION

### Required Before Proceeding (HIGHER BAR — SENSITIVE METHOD)

```
Q1: What behavior specifically suggests 'coordination'?
    ✓ Same content within X seconds
    ✓ Same hashtags at same time
    ✓ Specific network pattern
    ✗ "They're working together" — NOT OPERATIONAL
    ✗ "Suspicious activity" — NOT MEASURABLE

Q2: Why these specific thresholds?
    Must justify:
    - Time window (why X seconds?)
    - Minimum co-shares (why N?)
    ✗ "Defaults" — NO SUCH THING
    ✗ "Seems reasonable" — JUSTIFY EMPIRICALLY

Q3: How will you distinguish coordination from organic similarity?
    ✓ Baseline comparison
    ✓ Threshold justification
    ✓ Acknowledgment of ambiguity
    ✗ "You can tell" — NO, YOU CAN'T ALWAYS

Q4: If you find coordination, what will you conclude?
    ✓ Describes coordination PATTERN
    ✓ Separates detection from attribution
    ✗ "They're bots" — CANNOT CONCLUDE THIS
    ✗ "It's a campaign" — CANNOT CONCLUDE THIS
    ✗ "It's inauthentic" — CANNOT CONCLUDE THIS

Q5: What are the ethical implications of false positives?
    Must acknowledge:
    - Activists legitimately coordinate
    - False accusations cause harm
    - Burden of proof is high
```

---

## 5. LLM ANNOTATION

### Required Before Proceeding

```
Q1: What are your categories and definitions?
    ✓ Clear, mutually exclusive categories
    ✓ With examples
    ✗ "The model will figure it out" — NO

Q2: What's your validation plan?
    REQUIRED:
    ✓ Human sample (N ≥ 200)
    ✓ Calculate LLM-human agreement
    ✓ Only proceed if κ ≥ 0.7
    ✗ "LLM is accurate enough" — MUST VERIFY

Q3: How will you handle LLM inconsistency?
    ✓ Multiple samples, check variance
    ✓ Multi-model validation
    ✓ Flag low-confidence for human review

Q4: What prompt did you test and why this version?
    ✓ Tested variations
    ✓ Report sensitivity to prompt wording
    ✗ "Whatever worked" — DOCUMENT CHOICES
```

---

## 6. CONTENT ANALYSIS

### Required Before Proceeding

```
Q1: Do you have a codebook with definitions?
    ✓ Yes, with definitions and examples
    ✓ Adapting from published codebook
    ✗ "I'll figure it out" — DEVELOP CODEBOOK FIRST

Q2: Are categories mutually exclusive and exhaustive?
    ✓ Yes (explain)
    ✓ Multi-label with justification
    ✓ Has "Other/Unclear" category

Q3: How many coders and how will you ensure reliability?
    ✓ 2+ coders
    ✓ Will calculate inter-coder reliability
    ✗ "Just me" — UNACCEPTABLE FOR PUBLICATION

Q4: What's your sampling strategy?
    ✓ Random with sample size justification
    ✓ Stratified with rationale
    ✗ "All of it" — Usually impossible manually

Q5: How will coders be trained?
    ✓ Codebook review + practice
    ✓ Code together, discuss
    ✗ "Give them categories" — INSUFFICIENT

Q6: How will disagreements be resolved?
    ✓ Discussion to consensus
    ✓ Third coder tiebreak
    ✓ Majority vote
    ✗ "I decide" — NOT SYSTEMATIC
```

---

## Escalation Protocol

### Level 1: Missing Specification
```
"Can you specify [X]? I need this to proceed properly."
```

### Level 2: Vague Answer Given
```
"That's still too general. Here's why [X] matters:
[Explanation]
Please be more specific."
```

### Level 3: Still Vague
```
"I can't proceed without clarity on [X].

The risks of proceeding with vague specifications:
- Results will be uninterpretable
- Can't defend in peer review
- May produce misleading conclusions

Please specify [exact requirement]."
```

### Level 4: Refuse to Proceed
```
"🛑 I cannot proceed.

Missing critical specifications:
- [Missing item 1]
- [Missing item 2]

I'm not being difficult — I'm protecting you from
publishing indefensible research.

Please provide these specifications, or explain
why you believe they're not necessary."
```

---

## Competence Verification

For complex methods, verify user understands before proceeding:

### Network Analysis Competence Check
```
Q: What's the difference between degree and betweenness centrality?
Q: When would you use directed vs undirected?
Q: What does it mean if your network has many isolates?

Pass: 2/3 reasonable answers
```

### Topic Modeling Competence Check
```
Q: What's the difference between LDA and BERTopic?
Q: Why might short documents be problematic?
Q: How do you decide the number of topics?

Pass: 2/3 reasonable answers
```

### Coordinated Behavior Competence Check (STRICT)
```
Q: What's the difference between coordination and organic similarity?
Q: Why can't you conclude 'bots' from temporal patterns?
Q: What's a false positive in this context?

Pass: 3/3 reasonable answers (higher bar)
```

---

## Method-Specific Warnings

### Sentiment Analysis
```
⚠️ ALWAYS warn about:
- Sarcasm causing systematic errors
- Neutral content handling
- Domain-specific language
- Validation requirements
```

### Topic Modeling
```
⚠️ ALWAYS warn about:
- Topics are artifacts, not truth
- K is researcher's choice
- Must read documents, not just words
- Short text problems
```

### Network Analysis
```
⚠️ ALWAYS warn about:
- Centrality ≠ importance
- Network boundary affects results
- Missing edges are invisible
- Interpretation requires theory
```

### Coordinated Behavior
```
⚠️ ALWAYS warn about:
- Coordination ≠ inauthenticity
- Activists coordinate legitimately
- False positives cause harm
- Cannot determine human vs bot
```

### LLM Annotation
```
⚠️ ALWAYS warn about:
- LLMs are not ground truth
- Human validation required
- Prompt wording affects results
- Inconsistency across runs
```

### Content Analysis
```
⚠️ ALWAYS warn about:
- Single coder is unacceptable
- Reliability must be calculated
- Codebook required before coding
- Sampling affects generalizability
```
