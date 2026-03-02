# AgentAcademy Study Protocol

**Version:** 1.0  
**Last Updated:** 2026-02-27  
**Status:** Internal Reference Document

A step-by-step protocol for conducting agentic content analysis studies using CommDAAF, based on lessons learned from the #MahsaAmini virality study and related experiments.

---

## Table of Contents

1. [Pre-Study Checklist](#1-pre-study-checklist)
2. [Phase 1: Study Design](#2-phase-1-study-design)
3. [Phase 2: Data Preparation](#3-phase-2-data-preparation)
4. [Phase 3: Prompt Development](#4-phase-3-prompt-development)
5. [Phase 4: Multi-Model Coding](#5-phase-4-multi-model-coding)
6. [Phase 5: Reliability Assessment](#6-phase-5-reliability-assessment)
7. [Phase 6: Statistical Analysis](#7-phase-6-statistical-analysis)
8. [Phase 7: Interpretation & Writing](#8-phase-7-interpretation--writing)
9. [Common Failures & Solutions](#9-common-failures--solutions)
10. [Model-Specific Notes](#10-model-specific-notes)
11. [Quality Control Checklist](#11-quality-control-checklist)

---

## 1. Pre-Study Checklist

Before starting any AgentAcademy study, verify:

### API Access
- [ ] Claude API access confirmed (Anthropic)
- [ ] GLM-4.7 access via `zai-coding-plan/glm-4.7` (OpenCode) OR `zai/glm-4.7` (pay-per-token)
- [ ] Kimi K2.5 access via `kimi-coding/k2p5` (OpenCode)
- [ ] **DO NOT use OpenRouter** for AgentAcademy studies (billing model mismatch)
- [ ] **DO NOT use Mei agent** for AgentAcademy (routes through OpenRouter)

### Resources
- [ ] Study directory created: `projects/[study-name]/`
- [ ] Git repo initialized or connected
- [ ] Sufficient API credits/quota

### Theoretical Grounding
- [ ] Research question articulated
- [ ] Relevant literature identified
- [ ] Coding scheme grounded in theory (not ad-hoc)

---

## 2. Phase 1: Study Design

### 2.1 Define Research Question

Write a clear, answerable research question:

```
❌ Bad: "What makes content go viral?"
✅ Good: "Which message frames are associated with higher engagement 
         in the #MahsaAmini protest movement?"
```

### 2.2 Declare Validation Tier

**MANDATORY: Declare before proceeding**

| Tier | Validation | Claim Strength | Time Investment |
|------|------------|----------------|-----------------|
| 🟢 **EXPLORATORY** | Multi-model only | Hypothesis-generating | 2-4 hours |
| 🟡 **PILOT** | Multi-model + spot-check | Tentative conclusions | 1-2 days |
| 🔴 **PUBLICATION** | Multi-model + systematic human validation | Publication-ready | 3-5 days |

Most AgentAcademy studies are **🟢 EXPLORATORY** tier.

### 2.3 Define Constructs

For each construct to be coded:

1. **Name**: e.g., "INJUSTICE frame"
2. **Definition**: Operational definition from literature
3. **Theoretical source**: e.g., "Gamson 1992"
4. **Decision rules**: How to handle ambiguous cases
5. **Examples**: Prototypical and counter-examples

**Rule: Never proceed with undefined constructs.**

### 2.4 Document Study Parameters

Create `STUDY_DESIGN.md` with:

```markdown
# Study Design: [Name]

## Research Question
[Your RQ]

## Validation Tier
🟢 EXPLORATORY / 🟡 PILOT / 🔴 PUBLICATION

## Constructs
| Construct | Definition | Source |
|-----------|------------|--------|
| ... | ... | ... |

## Data Source
- Platform: 
- Time period:
- Collection method:
- Expected N:

## Planned Analyses
- DV: 
- IVs:
- Model:
```

---

## 3. Phase 2: Data Preparation

### 3.1 Load and Inspect Data

**Always manually inspect a sample before proceeding.**

```python
# Load data
import pandas as pd
data = pd.read_csv("raw_data.csv")

# Basic checks
print(f"N = {len(data)}")
print(f"Columns: {list(data.columns)}")
print(f"Date range: {data['created_at'].min()} to {data['created_at'].max()}")

# CRITICAL: Read 10-20 random posts
sample = data.sample(20)
for _, row in sample.iterrows():
    print(f"---\n{row['text'][:200]}")
```

**Rule: Read actual content. Metadata inspection is not enough.**

### 3.2 Check for Contamination

Look for:
- Mixed datasets (e.g., Ukraine posts in #MahsaAmini data)
- Duplicates
- Spam/bot content
- Off-topic posts

```python
# Check for unexpected content
keywords_expected = ["mahsa", "iran", "protest", "woman", "life", "freedom"]
keywords_unexpected = ["ukraine", "zelensky", "kyiv", "russia"]

for kw in keywords_unexpected:
    matches = data[data['text'].str.lower().str.contains(kw, na=False)]
    if len(matches) > 0:
        print(f"⚠️ Found {len(matches)} posts containing '{kw}'")
```

**Lesson learned:** Our #MahsaAmini dataset contained 20 Ukraine posts. Visual inspection caught this; automated checks missed it.

### 3.3 Calculate Engagement Metric

**Standard formula:**

```python
import numpy as np

data['engagement'] = (
    np.log(data['retweet_count'] + 1) + 
    np.log(data['like_count'] + 1) + 
    np.log(data['quote_count'].fillna(0) + 1)
)
```

**Document if you modify this formula.**

### 3.4 Stratified Sampling

**Standard engagement tiers:**

| Tier | Percentile | Purpose |
|------|------------|---------|
| Viral | Top 5% | What makes content break out |
| High | 75th-95th | Successful content |
| Medium | 25th-75th | Baseline performance |
| Low | Bottom 25% | Why content fails |

```python
# Calculate percentiles
p95 = data['engagement'].quantile(0.95)
p75 = data['engagement'].quantile(0.75)
p25 = data['engagement'].quantile(0.25)

# Assign tiers
def assign_tier(eng):
    if eng >= p95: return 'viral'
    elif eng >= p75: return 'high'
    elif eng >= p25: return 'medium'
    else: return 'low'

data['tier'] = data['engagement'].apply(assign_tier)

# Sample equal n per tier
n_per_tier = 100
sample = data.groupby('tier').apply(
    lambda x: x.sample(min(len(x), n_per_tier), random_state=42)
).reset_index(drop=True)
```

### 3.5 Create Batches

**Critical batch size limits:**

| Model | Max Batch Size | Recommended |
|-------|----------------|-------------|
| Claude | 100+ | 50-100 |
| GLM-4.7 | 50-100 | 50 |
| Kimi K2.5 | **25-30** | **25** |

**Kimi truncates JSON output on batches >30 posts. Always use 25-post batches for Kimi.**

```python
# Create sub-batches
batch_size = 25
batches = []
for i in range(0, len(sample), batch_size):
    batch = sample.iloc[i:i+batch_size]
    batches.append(batch)
    batch.to_json(f"batch_{i//batch_size + 1}.json", orient='records')
```

### 3.6 Verify Sample

Before coding:

```python
# Final verification
print(f"Total N: {len(sample)}")
print(f"Tier distribution: {sample['tier'].value_counts().to_dict()}")
print(f"Language distribution: {sample['lang'].value_counts().to_dict()}")
print(f"Date range: {sample['created_at'].min()} to {sample['created_at'].max()}")

# Verify no contamination
assert len(sample) == expected_n, f"Sample size mismatch"
```

---

## 4. Phase 3: Prompt Development

### 4.1 Start with CommDAAF Template

**Never use minimal prompts.** Start with full CommDAAF structure:

```markdown
# CONTENT ANALYSIS CODING INSTRUCTIONS

## TASK
For each text, assign codes for the following dimensions:
1. PRIMARY_FRAME: [list options]
2. VALENCE: positive / negative / neutral
3. AROUSAL: low / medium / high

## OUTPUT FORMAT
Return JSON array:
[{"id": "...", "frame": "...", "valence": "...", "arousal": "...", "confidence": 0.0-1.0}]

## DECISION HIERARCHY
When multiple frames apply, prioritize:
1. [highest priority]
2. ...
3. [lowest priority]

## FRAME DEFINITIONS

### FRAME_1
**Definition:** [operational definition]
**Source:** [theoretical source]
**Decision rules:**
- [rule 1]
- [rule 2]

**Examples (YES):**
- "[example 1]"
- "[example 2]"

**Counter-examples (NO):**
- "[counter-example 1]"

**Common confusions:** [list]

### FRAME_2
[repeat structure]

## VALENCE ANCHORS
- **Positive:** hope, victory, celebration, solidarity
- **Negative:** grief, anger, injustice, suffering
- **Neutral:** factual reporting, no emotional valence

## AROUSAL ANCHORS
- **Low:** calm, matter-of-fact, informational
- **Medium:** concerned, engaged, emphatic
- **High:** urgent, intense, alarming, desperate

## LANGUAGE HANDLING
[If multilingual data:]
- Persian examples: [examples]
- Arabic examples: [examples]
- Code based on meaning, not language
```

### 4.2 Include Multilingual Anchors

**If data contains non-English content:**

```markdown
## PERSIAN-SPECIFIC GUIDANCE
- "زن زندگی آزادی" (Woman Life Freedom) = SOLIDARITY/HOPE
- "مرگ بر دیکتاتور" (Death to dictator) = INJUSTICE (high arousal)
- Common Persian hashtags: #مهسا_امینی, #زن_زندگی_آزادی

## ARABIC-SPECIFIC GUIDANCE
- "المرأة الحياة الحرية" = SOLIDARITY/HOPE
- Mixed Arabic-Persian content: code dominant language sentiment
```

### 4.3 Version Your Prompts

```
commdaaf_prompt_v0.1.md  # Initial minimal prompt
commdaaf_prompt_v0.2.md  # Added decision rules
commdaaf_prompt_v0.3.md  # Added multilingual anchors
commdaaf_prompt_v0.4.md  # Refined after first batch
commdaaf_prompt_v0.5.md  # Final version used for study
```

**Track what changed between versions.**

### 4.4 Test on 5-10 Posts First

Before full run:

```python
# Test batch
test_posts = sample.head(10).to_dict('records')

# Code with each model
claude_test = code_with_claude(test_posts, prompt_v1)
glm_test = code_with_glm(test_posts, prompt_v1)
kimi_test = code_with_kimi(test_posts, prompt_v1)

# Compare outputs
for i in range(10):
    print(f"Post {i}: Claude={claude_test[i]['frame']}, GLM={glm_test[i]['frame']}, Kimi={kimi_test[i]['frame']}")
```

**If disagreement is high (>50%), refine prompt before proceeding.**

---

## 5. Phase 4: Multi-Model Coding

### 5.1 Model Configuration

**Recommended setup:**

| Model | Access Method | Notes |
|-------|---------------|-------|
| Claude Opus 4.5 | Direct API or OpenClaw | Most reliable for complex coding |
| GLM-4.7 | OpenCode `zai-coding-plan/glm-4.7` | Slower, may stall on large batches |
| Kimi K2.5 | OpenCode `kimi-coding/k2p5` | 25-post batch limit |

### 5.2 Batch Processing

**For each model, for each batch:**

```python
def process_batch(batch_file, model, prompt):
    # Load batch
    with open(batch_file) as f:
        posts = json.load(f)
    
    # Format prompt with posts
    full_prompt = prompt + "\n\n## POSTS TO CODE\n" + json.dumps(posts)
    
    # Call model API
    response = call_model(model, full_prompt)
    
    # Parse JSON response
    coded = json.loads(response)
    
    # Validate output
    assert len(coded) == len(posts), f"Missing posts in output"
    for item in coded:
        assert 'id' in item and 'frame' in item, f"Missing fields"
    
    return coded
```

### 5.3 Handle Failures

**Common failures and solutions:**

| Failure | Detection | Solution |
|---------|-----------|----------|
| Truncated JSON | `len(output) < len(input)` | Reduce batch size |
| API timeout | Exception | Retry with exponential backoff |
| Invalid JSON | Parse error | Request JSON-only response |
| Missing posts | Count mismatch | Check which posts missing, re-run |

```python
def robust_process(batch_file, model, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = process_batch(batch_file, model, prompt)
            return result
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    
    raise RuntimeError(f"Failed after {max_retries} attempts")
```

### 5.4 Save All Outputs

```
outputs/
  claude/
    batch_1_claude.json
    batch_2_claude.json
    ...
  glm/
    batch_1_glm.json
    ...
  kimi/
    batch_1_kimi.json
    ...
```

**Never overwrite outputs. Use timestamps or version numbers.**

### 5.5 Merge Results

```python
def merge_model_outputs(claude_files, glm_files, kimi_files):
    merged = {}
    
    for files, model_name in [(claude_files, 'claude'), (glm_files, 'glm'), (kimi_files, 'kimi')]:
        for f in files:
            with open(f) as fp:
                coded = json.load(fp)
            for item in coded:
                post_id = item['id']
                if post_id not in merged:
                    merged[post_id] = {'id': post_id}
                merged[post_id][f'{model_name}_frame'] = item['frame']
                merged[post_id][f'{model_name}_valence'] = item.get('valence')
                merged[post_id][f'{model_name}_arousal'] = item.get('arousal')
    
    return list(merged.values())
```

---

## 6. Phase 5: Reliability Assessment

### 6.1 Calculate Agreement

**Three metrics to report:**

```python
from sklearn.metrics import cohen_kappa_score
import itertools

def calculate_reliability(merged_data, code_var='frame'):
    models = ['claude', 'glm', 'kimi']
    
    # Extract codes per model
    codes = {m: [d[f'{m}_{code_var}'] for d in merged_data] for m in models}
    
    # 1. Three-way agreement
    three_way = sum(
        1 for i in range(len(merged_data))
        if codes['claude'][i] == codes['glm'][i] == codes['kimi'][i]
    ) / len(merged_data)
    
    # 2. Majority agreement (2/3)
    majority = sum(
        1 for i in range(len(merged_data))
        if len(set([codes['claude'][i], codes['glm'][i], codes['kimi'][i]])) <= 2
    ) / len(merged_data)
    
    # 3. Pairwise kappa
    kappas = {}
    for m1, m2 in itertools.combinations(models, 2):
        k = cohen_kappa_score(codes[m1], codes[m2])
        kappas[f'{m1}_{m2}'] = k
    
    # 4. Fleiss' kappa (requires fleiss_kappa function)
    fleiss_k = calculate_fleiss_kappa(merged_data, code_var, models)
    
    return {
        'three_way_agreement': three_way,
        'majority_agreement': majority,
        'pairwise_kappa': kappas,
        'fleiss_kappa': fleiss_k
    }
```

### 6.2 Frame-Specific Reliability

**CRITICAL: Report reliability BY FRAME, not just aggregate.**

```python
def frame_specific_reliability(merged_data, frame_var='frame'):
    frames = set()
    for d in merged_data:
        for m in ['claude', 'glm', 'kimi']:
            frames.add(d.get(f'{m}_{frame_var}'))
    
    results = {}
    for frame in frames:
        # Posts where at least one model coded this frame
        relevant = [d for d in merged_data 
                   if frame in [d.get(f'{m}_{frame_var}') for m in ['claude', 'glm', 'kimi']]]
        
        if len(relevant) < 5:
            results[frame] = {'n': len(relevant), 'three_way': None, 'flag': '⚠️ Too few cases'}
            continue
        
        three_way = sum(
            1 for d in relevant
            if d['claude_frame'] == d['glm_frame'] == d['kimi_frame'] == frame
        ) / len(relevant)
        
        results[frame] = {
            'n': len(relevant),
            'three_way': three_way,
            'flag': '✅' if three_way >= 0.5 else '⚠️ Low reliability'
        }
    
    return results
```

### 6.3 Determine Majority Vote

```python
from collections import Counter

def majority_vote(merged_data, code_var='frame'):
    for d in merged_data:
        votes = [d[f'{m}_{code_var}'] for m in ['claude', 'glm', 'kimi']]
        counter = Counter(votes)
        majority, count = counter.most_common(1)[0]
        
        d[f'{code_var}_majority'] = majority
        d[f'{code_var}_agreement'] = count  # 2 or 3
    
    return merged_data
```

### 6.4 Flag Low-Reliability Frames

```python
def flag_unreliable_frames(frame_reliability, threshold=0.4):
    flags = []
    for frame, stats in frame_reliability.items():
        if stats['three_way'] and stats['three_way'] < threshold:
            flags.append(f"⚠️ {frame}: {stats['three_way']:.0%} agreement (n={stats['n']})")
    return flags
```

**Rule: Always report frame-specific reliability. Flag frames with <40% three-way agreement.**

---

## 7. Phase 6: Statistical Analysis

### 7.1 Distribution Diagnostics (MANDATORY)

**NEVER run regression without these checks:**

```python
import numpy as np
from scipy import stats

def distribution_diagnostics(y, name="DV"):
    print(f"=== Distribution Diagnostics: {name} ===")
    
    # Basic stats
    print(f"N: {len(y)}")
    print(f"Mean: {np.mean(y):.3f}")
    print(f"Median: {np.median(y):.3f}")
    print(f"SD: {np.std(y):.3f}")
    print(f"Range: {np.min(y):.3f} - {np.max(y):.3f}")
    
    # Skewness
    skewness = stats.skew(y)
    print(f"Skewness: {skewness:.3f}")
    if abs(skewness) > 1:
        print("  ⚠️ Highly skewed (|skew| > 1)")
    
    # Zeros
    n_zeros = np.sum(y == 0)
    pct_zeros = n_zeros / len(y) * 100
    print(f"Zeros: {n_zeros} ({pct_zeros:.1f}%)")
    if pct_zeros > 15:
        print("  ⚠️ High zero proportion (>15%)")
    
    # Overdispersion
    var_mean_ratio = np.var(y) / np.mean(y) if np.mean(y) > 0 else float('inf')
    print(f"Var/Mean ratio: {var_mean_ratio:.3f}")
    if var_mean_ratio > 1.5:
        print("  ⚠️ Overdispersed (var/mean > 1.5)")
    
    # Recommendation
    print("\n=== Model Recommendation ===")
    if pct_zeros > 30:
        print("→ Zero-inflated model or Hurdle model")
    elif var_mean_ratio > 1.5:
        print("→ Negative Binomial regression")
    elif skewness > 1:
        print("→ Log-transform or Negative Binomial")
    else:
        print("→ OLS may be appropriate (verify residuals)")
    
    return {
        'skewness': skewness,
        'pct_zeros': pct_zeros,
        'var_mean_ratio': var_mean_ratio
    }
```

### 7.2 Model Selection Decision Tree

```
Is DV a count/engagement metric?
├── Yes → Check overdispersion (var/mean > 1.5?)
│   ├── Yes → Negative Binomial
│   └── No → Poisson (rare for social media data)
├── Is DV proportion/bounded?
│   └── Yes → Beta regression or logistic
└── Is DV continuous and ~normal?
    └── Yes → OLS (check residuals)

⚠️ NEVER use OLS on raw engagement counts without justification.
```

### 7.3 Run Negative Binomial (Typical Case)

```python
import statsmodels.api as sm

def run_negative_binomial(data, dv, ivs, reference_frame='SOLIDARITY'):
    # Create dummy variables
    X = pd.get_dummies(data[ivs], drop_first=False)
    
    # Drop reference category
    ref_cols = [c for c in X.columns if reference_frame in c]
    X = X.drop(columns=ref_cols)
    
    # Add constant
    X = sm.add_constant(X)
    
    # Fit model
    y = data[dv]
    model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
    results = model.fit()
    
    # Calculate IRR
    irr = np.exp(results.params)
    ci = np.exp(results.conf_int())
    
    return results, irr, ci
```

### 7.4 Report Effect Sizes

**For Negative Binomial: Report IRR, not raw coefficients.**

```python
def format_nb_results(results, irr, ci):
    output = []
    for var in irr.index:
        if var == 'const':
            continue
        row = {
            'predictor': var,
            'IRR': irr[var],
            'CI_lower': ci.loc[var, 0],
            'CI_upper': ci.loc[var, 1],
            'p': results.pvalues[var],
            'interpretation': interpret_irr(irr[var])
        }
        output.append(row)
    return pd.DataFrame(output)

def interpret_irr(irr):
    if irr > 2.5:
        return "Large positive effect"
    elif irr > 1.5:
        return "Medium positive effect"
    elif irr > 1.2:
        return "Small positive effect"
    elif irr > 0.8:
        return "Negligible effect"
    elif irr > 0.5:
        return "Small negative effect"
    else:
        return "Large negative effect"
```

### 7.5 Multiple Comparison Correction

If testing multiple frames:

```python
from statsmodels.stats.multitest import multipletests

# Get p-values for all frame comparisons
p_values = [results.pvalues[f'frame_{f}'] for f in frames if f != reference]

# Apply FDR correction
rejected, p_adj, _, _ = multipletests(p_values, method='fdr_bh')

# Report both raw and adjusted p-values
```

---

## 8. Phase 7: Interpretation & Writing

### 8.1 Summarize Key Findings

Template:

```markdown
## Key Findings

1. **[Main finding]**: [effect size], p [value]
   - Interpretation: [what this means practically]
   
2. **[Secondary finding]**: [effect size], p [value]
   - Interpretation: [what this means practically]

## Reliability Notes
- Overall Fleiss' κ = [value] ([interpretation])
- Frame-specific concerns: [list low-reliability frames]

## Limitations
- [List key limitations]
```

### 8.2 Effect Size Interpretation

**Always translate statistical effects to practical meaning:**

| IRR | Practical Meaning |
|-----|-------------------|
| 1.5 | 50% more engagement |
| 2.0 | Double the engagement |
| 2.72 | Nearly 3x engagement |
| 0.5 | Half the engagement |

### 8.3 Document Everything

Create `STUDY_REPORT.md` with:

1. Research question
2. Sample details (N, time period, language distribution)
3. Methodology (coding scheme, models used, prompt version)
4. Reliability (overall + frame-specific)
5. Results (with effect sizes)
6. Limitations
7. Files and locations

---

## 9. Common Failures & Solutions

### Data Failures

| Failure | How We Caught It | Solution | Prevention |
|---------|------------------|----------|------------|
| Dataset contamination (Ukraine in Mahsa) | Visual inspection of coded posts | Split datasets, remove contaminated | **Always read sample posts** |
| Wrong sample size | Post-merge count check | Recount and reconcile | Automated validation |
| Duplicate posts | ID collision | Deduplicate by ID | Check uniqueness before sampling |

### Prompt Failures

| Failure | How We Caught It | Solution | Prevention |
|---------|------------------|----------|------------|
| Oversimplified prompt | Low inter-model agreement | Develop full CommDAAF prompt | **Start with template** |
| Missing language anchors | Persian posts miscoded | Add Persian/Arabic examples | Include anchors for all languages |
| Ambiguous frame boundaries | HUMANITARIAN/INJUSTICE confusion | Add decision hierarchy | Anticipate overlaps |

### Technical Failures

| Failure | How We Caught It | Solution | Prevention |
|---------|------------------|----------|------------|
| Kimi batch truncation | Missing posts in output | Reduce to 25-post batches | **Always use 25 for Kimi** |
| GLM stalling | Process hangs | Smaller batches, retry | Monitor progress, timeout |
| API timeout | Exception | Exponential backoff retry | Build retry logic |

### Analytical Failures

| Failure | How We Caught It | Solution | Prevention |
|---------|------------------|----------|------------|
| OLS on skewed data | Diagnostic prompt | Negative Binomial regression | **Mandatory diagnostics** |
| Aggregate κ only | Review flagged | Report frame-specific | Include in standard pipeline |
| Valence-frame confounding | Correlation check | Document, exclude, or control | Check correlations early |

---

## 10. Model-Specific Notes

### Claude Opus 4.5
- **Strengths**: Most reliable for complex coding, follows instructions precisely
- **Weaknesses**: Cost
- **Batch size**: 50-100 posts
- **Notes**: Tends to be conservative; may under-code emotional frames

### GLM-4.7
- **Access**: `zai-coding-plan/glm-4.7` via OpenCode OR `zai/glm-4.7` direct (pay-per-token)
- **Strengths**: Good multilingual, cost-effective with coding plan
- **Weaknesses**: Can stall on large batches, slower than Claude
- **Batch size**: 50 posts max
- **Notes**: Under-coded CONFLICT significantly in our study (39% vs Claude's 100%)

### Kimi K2.5
- **Access**: `kimi-coding/k2p5` via OpenCode
- **Strengths**: Fast, good for high-volume
- **Weaknesses**: **Truncates JSON output on batches >30**
- **Batch size**: **25 posts (strict limit)**
- **Notes**: Slightly over-codes HUMANITARIAN in our study

### OpenCode Requirements
- Both GLM and Kimi via OpenCode **require PTY mode**
- Use `exec(pty=true)` for all OpenCode calls
- Monitor for stalls and timeouts

---

## 11. Quality Control Checklist

### Before Coding
- [ ] Sample size matches expected N
- [ ] Tier distribution is as planned
- [ ] No contamination detected (visual inspection)
- [ ] Prompt includes all constructs with definitions
- [ ] Prompt includes decision hierarchy
- [ ] Prompt includes multilingual anchors (if applicable)
- [ ] Test batch shows reasonable agreement

### During Coding
- [ ] Each batch returns expected N posts
- [ ] JSON parses without errors
- [ ] No obvious coding errors in spot checks
- [ ] All models complete all batches

### After Coding
- [ ] All models' outputs merged correctly
- [ ] Overall κ ≥ 0.6 (substantial agreement)
- [ ] Frame-specific reliability reported
- [ ] Low-reliability frames flagged
- [ ] Distribution diagnostics run
- [ ] Appropriate statistical model selected
- [ ] Effect sizes reported (IRR or d)
- [ ] Limitations documented

### Before Publication
- [ ] Validation tier declared and appropriate
- [ ] Human validation completed (if 🟡 or 🔴 tier)
- [ ] All files saved and version controlled
- [ ] Results reproducible from saved files

---

## Appendix: File Naming Conventions

```
projects/[study-name]/
  STUDY_DESIGN.md
  STUDY_REPORT.md
  
  data/
    raw/
      [source]_raw.csv
    processed/
      sample_n[N].csv
      batches/
        batch_1.json
        batch_2.json
        ...
  
  prompts/
    commdaaf_prompt_v0.1.md
    commdaaf_prompt_v0.2.md
    commdaaf_prompt_final.md
  
  outputs/
    claude/
      batch_1_claude.json
      ...
    glm/
      batch_1_glm.json
      ...
    kimi/
      batch_1_kimi.json
      ...
    merged/
      all_models_merged.json
      majority_vote.json
  
  analysis/
    reliability.json
    frame_reliability.json
    regression_results.json
    diagnostics.json
  
  figures/
    engagement_distribution.png
    frame_distribution.png
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-27 | Initial protocol based on #MahsaAmini study |

---

*This protocol is a living document. Update it as new lessons are learned.*
