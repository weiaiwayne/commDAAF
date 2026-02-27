# Content Analysis Method

Systematic coding of text for patterns and meaning.

---

## Overview

Content analysis is the systematic classification of text (or other media) into categories. Types:
- **Manual content analysis**: Human coders apply codebook
- **Automated content analysis**: Algorithms classify text
- **Hybrid**: Human-AI collaboration

---

## Preflight Requirements

| Requirement | Why It Matters |
|-------------|----------------|
| Codebook | Categories must be defined before coding |
| Unit of analysis | What gets coded (post, sentence, account)? |
| Sampling strategy | Can't code everything — how to sample? |
| Inter-coder reliability plan | Multiple coders required for validity |
| Reliability threshold | κ ≥ 0.7 minimum for publication |

---

## Probing Questions

```yaml
content_analysis_probing:

  q1_codebook:
    question: "Do you have a codebook with clear category definitions?"
    required: true
    acceptable:
      - "Yes, with definitions and examples for each category"
      - "Adapting from [published codebook]"
      - "Developing codebook — plan to pilot test"
    unacceptable:
      - "I'll figure it out as I go"
      - "The categories are obvious"
    if_unacceptable: |
      ⚠️ Content analysis requires a CODEBOOK.
      
      A codebook includes:
      1. Clear definition for each category
      2. Inclusion/exclusion criteria
      3. Examples of content that fits
      4. Examples of edge cases
      
      Without a codebook:
      - Coding is subjective and unreliable
      - Results are not replicable
      - Cannot train other coders
      
      Develop your codebook first, then come back.

  q2_categories:
    question: "Are your categories mutually exclusive and exhaustive?"
    required: true
    checks:
      mutually_exclusive: "Can one item belong to only one category?"
      exhaustive: "Can every item be assigned to a category?"
    if_not_exclusive: |
      If items can belong to multiple categories:
      - Use multi-label coding
      - Report agreement differently
      - Analysis is more complex
      
      Is multi-label appropriate for your RQ?
    if_not_exhaustive: |
      You need an "Other" or "Unclear" category.
      
      Otherwise:
      - Coders forced to pick wrong category
      - Creates measurement error
      
      Add residual category?

  q3_coders:
    question: "How many coders and how will you ensure reliability?"
    required: true
    acceptable:
      - "2+ coders, will calculate inter-coder reliability"
      - "Using LLM + human validation sample"
      - "Established codebook from prior study"
    unacceptable:
      - "Just me"
      - "I'll be consistent"
    if_unacceptable: |
      ⚠️ Single-coder content analysis is NOT acceptable for publication.
      
      Requirements:
      1. At least 2 independent coders
      2. Code overlapping sample (10-20% of data)
      3. Calculate agreement (Cohen's κ or Krippendorff's α)
      4. Target: κ ≥ 0.7 (0.8+ preferred)
      
      If using LLM as "coder":
      - Still need human validation
      - Calculate LLM-human agreement
      
      Your reliability plan?

  q4_sampling:
    question: "What's your sampling strategy?"
    required: true
    options:
      random:
        description: "Simple random sample"
        when: "Population is homogeneous"
      stratified:
        description: "Sample within subgroups"
        when: "Need representation across categories"
      purposive:
        description: "Select specific cases"
        when: "Studying particular phenomenon"
      full_population:
        description: "Code everything"
        when: "Small dataset OR automated coding"
    if_vague: |
      You can't code everything manually (usually).
      
      Sampling considerations:
      - How representative must sample be?
      - What claims do you want to make?
      - Resources available?
      
      For claims about population:
      - N ≥ 385 for ±5% margin at 95% CI
      - Stratify if subgroups matter
      
      Your sampling approach and justification?

  q5_training:
    question: "How will coders be trained?"
    required: true
    acceptable:
      - "Codebook review + practice rounds"
      - "Code together, discuss disagreements, refine"
      - "Formal training protocol with test set"
    unacceptable:
      - "Give them the categories"
      - "They'll figure it out"
    if_unacceptable: |
      Coder training is essential for reliability.
      
      Training protocol should include:
      1. Study codebook together
      2. Code practice set independently
      3. Compare, discuss disagreements
      4. Revise codebook if needed
      5. Code reliability sample
      6. Achieve threshold BEFORE main coding
      
      Your training plan?

  q6_disagreement:
    question: "How will you handle coder disagreements?"
    required: true
    acceptable:
      - "Discussion to consensus"
      - "Third coder tiebreak"
      - "Majority vote (if 3+ coders)"
      - "Record both, analyze separately"
    unacceptable:
      - "One coder decides"
      - "Go with my judgment"
    if_unacceptable: |
      Disagreement resolution must be systematic.
      
      Options:
      1. DISCUSSION: Talk through, reach consensus
         - Good: Catches errors
         - Bad: Time-consuming
      
      2. TIEBREAK: Third coder or expert decides
         - Good: Efficient
         - Bad: Introduces third perspective
      
      3. MAJORITY: If 3+ coders, go with majority
         - Good: Efficient
         - Bad: Requires 3+ coders
      
      4. RECORD BOTH: Keep disagreement as data
         - Good: Preserves uncertainty
         - Bad: Complex analysis
      
      Your approach?
```

---

## Implementation

### Manual Content Analysis Pipeline

```python
"""
Content Analysis Pipeline with reliability calculation.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from sklearn.metrics import cohen_kappa_score
import krippendorff

class ContentAnalysisPipeline:
    """Pipeline for rigorous content analysis."""
    
    def __init__(self, 
                 categories: List[str],
                 codebook: Dict[str, Dict] = None):
        """
        Args:
            categories: List of category names
            codebook: Dict with {category: {definition, examples, exclusions}}
        """
        self.categories = categories
        self.codebook = codebook or {}
        self.codings = {}
        
    def create_coding_sheet(self, 
                           data: pd.DataFrame,
                           text_column: str,
                           id_column: str,
                           sample_size: int = None,
                           stratify_by: str = None) -> pd.DataFrame:
        """
        Create coding sheet for human coders.
        """
        if sample_size and sample_size < len(data):
            if stratify_by:
                sample = data.groupby(stratify_by, group_keys=False).apply(
                    lambda x: x.sample(min(len(x), sample_size // data[stratify_by].nunique()))
                )
            else:
                sample = data.sample(n=sample_size, random_state=42)
        else:
            sample = data.copy()
        
        coding_sheet = pd.DataFrame({
            'id': sample[id_column],
            'text': sample[text_column],
        })
        
        # Add category columns
        for cat in self.categories:
            coding_sheet[f'code_{cat}'] = None
        
        coding_sheet['coder_id'] = None
        coding_sheet['coder_notes'] = None
        coding_sheet['confidence'] = None
        
        return coding_sheet
    
    def create_reliability_sample(self,
                                  coding_sheet: pd.DataFrame,
                                  reliability_pct: float = 0.15) -> pd.DataFrame:
        """
        Create sample for inter-coder reliability testing.
        
        Both coders should code this sample independently.
        """
        n_reliability = max(50, int(len(coding_sheet) * reliability_pct))
        
        reliability_sample = coding_sheet.sample(
            n=min(n_reliability, len(coding_sheet)),
            random_state=42
        )
        
        print(f"Reliability sample: {len(reliability_sample)} items")
        print(f"({len(reliability_sample)/len(coding_sheet)*100:.1f}% of data)")
        
        return reliability_sample
    
    def calculate_reliability(self,
                             coder1_labels: List,
                             coder2_labels: List,
                             metric: str = 'both') -> Dict:
        """
        Calculate inter-coder reliability.
        
        Args:
            coder1_labels: Labels from coder 1
            coder2_labels: Labels from coder 2
            metric: 'kappa', 'alpha', or 'both'
        """
        results = {}
        
        # Cohen's Kappa (for 2 coders)
        if metric in ['kappa', 'both']:
            kappa = cohen_kappa_score(coder1_labels, coder2_labels)
            results['cohens_kappa'] = kappa
            results['kappa_interpretation'] = self._interpret_kappa(kappa)
        
        # Krippendorff's Alpha (more general)
        if metric in ['alpha', 'both']:
            reliability_data = [coder1_labels, coder2_labels]
            alpha = krippendorff.alpha(reliability_data=reliability_data,
                                       level_of_measurement='nominal')
            results['krippendorffs_alpha'] = alpha
            results['alpha_interpretation'] = self._interpret_alpha(alpha)
        
        # Agreement percentage
        agreement = sum(c1 == c2 for c1, c2 in zip(coder1_labels, coder2_labels))
        results['percent_agreement'] = agreement / len(coder1_labels) * 100
        
        # Recommendation
        kappa_val = results.get('cohens_kappa', 0)
        if kappa_val >= 0.8:
            results['recommendation'] = 'Excellent reliability. Proceed with coding.'
        elif kappa_val >= 0.7:
            results['recommendation'] = 'Acceptable reliability. Proceed with caution.'
        elif kappa_val >= 0.6:
            results['recommendation'] = 'Marginal reliability. Review codebook and retrain.'
        else:
            results['recommendation'] = 'Poor reliability. Revise codebook before proceeding.'
        
        return results
    
    def _interpret_kappa(self, kappa: float) -> str:
        """Interpret Cohen's Kappa."""
        if kappa > 0.80:
            return "Almost perfect agreement"
        elif kappa > 0.60:
            return "Substantial agreement"
        elif kappa > 0.40:
            return "Moderate agreement"
        elif kappa > 0.20:
            return "Fair agreement"
        else:
            return "Poor agreement"
    
    def _interpret_alpha(self, alpha: float) -> str:
        """Interpret Krippendorff's Alpha."""
        if alpha >= 0.80:
            return "Reliable"
        elif alpha >= 0.67:
            return "Tentatively reliable"
        else:
            return "Unreliable — do not proceed"
    
    def merge_codings(self,
                      coder1_df: pd.DataFrame,
                      coder2_df: pd.DataFrame,
                      resolve_method: str = 'discussion') -> pd.DataFrame:
        """
        Merge codings from two coders.
        
        Args:
            coder1_df: Codings from coder 1
            coder2_df: Codings from coder 2
            resolve_method: How to handle disagreements
        """
        merged = coder1_df.copy()
        merged.columns = [f"{c}_coder1" if c.startswith('code_') else c 
                         for c in merged.columns]
        
        for col in coder2_df.columns:
            if col.startswith('code_'):
                merged[f"{col}_coder2"] = coder2_df[col].values
        
        # Identify disagreements
        code_cols = [c for c in self.categories]
        for cat in code_cols:
            c1 = f"code_{cat}_coder1"
            c2 = f"code_{cat}_coder2"
            merged[f"disagree_{cat}"] = merged[c1] != merged[c2]
        
        # Summary
        disagreements = merged[[c for c in merged.columns if c.startswith('disagree_')]].sum()
        print(f"Disagreements by category:\n{disagreements}")
        
        if resolve_method == 'discussion':
            print("\nDisagreements require manual resolution.")
            print("Export and discuss, then update 'final_code' column.")
            
            for cat in code_cols:
                merged[f"final_{cat}"] = None
        
        return merged
    
    def generate_codebook_template(self) -> str:
        """Generate codebook template in markdown."""
        template = """# Codebook

## Study Information
- **Study title**: 
- **Coder(s)**:
- **Date**:

## Categories

"""
        for cat in self.categories:
            template += f"""### {cat}

**Definition**: [Clear definition of what this category means]

**Inclusion criteria**: 
- [Criterion 1]
- [Criterion 2]

**Exclusion criteria**:
- [What does NOT count]

**Examples**:
1. [Example text that fits this category]
2. [Another example]

**Edge cases**:
- [Ambiguous case and how to handle it]

---

"""
        
        template += """## Coding Rules

1. Code based on explicit content, not inference
2. When uncertain, mark for discussion
3. [Additional rules]

## Disagreement Resolution

[Describe process for handling disagreements]
"""
        
        return template


def run_content_analysis_pipeline(
    data: pd.DataFrame,
    text_column: str,
    id_column: str,
    categories: List[str],
    sample_size: int = 500
) -> Dict:
    """
    Complete content analysis pipeline.
    
    Returns materials for manual coding + reliability testing.
    """
    pipeline = ContentAnalysisPipeline(categories=categories)
    
    # Create materials
    coding_sheet = pipeline.create_coding_sheet(
        data, text_column, id_column, sample_size
    )
    
    reliability_sample = pipeline.create_reliability_sample(coding_sheet)
    
    codebook_template = pipeline.generate_codebook_template()
    
    return {
        'pipeline': pipeline,
        'coding_sheet': coding_sheet,
        'reliability_sample': reliability_sample,
        'codebook_template': codebook_template,
        'next_steps': [
            "1. Complete codebook using template",
            "2. Train coders on codebook",
            "3. Have both coders code reliability sample independently",
            "4. Calculate reliability — must achieve κ ≥ 0.7",
            "5. Resolve disagreements, refine codebook if needed",
            "6. Code full sample (can split between coders)",
            "7. Report reliability metrics in methods section"
        ]
    }
```

---

## LLM-Assisted Content Analysis

```python
"""
Hybrid human-LLM content analysis.
LLM does initial coding; humans validate and correct.
"""

async def llm_content_analysis(
    texts: List[str],
    categories: Dict[str, str],  # {category: definition}
    model: str = "google/gemini-2.0-flash",
    validation_sample_size: int = 200
) -> Dict:
    """
    LLM-assisted content analysis with required human validation.
    """
    
    # Build prompt with category definitions
    cat_text = "\n".join([f"- {cat}: {defn}" for cat, defn in categories.items()])
    
    prompt_template = f"""Classify this text into exactly one category.

Categories:
{cat_text}

Text: "{{text}}"

Respond with ONLY the category name, nothing else."""
    
    # LLM coding
    results = []
    for text in texts:
        prompt = prompt_template.format(text=text)
        response = await call_llm(model, prompt)
        
        # Parse response
        label = response.strip()
        if label not in categories:
            label = 'UNRECOGNIZED'
        
        results.append({
            'text': text,
            'llm_label': label,
            'raw_response': response
        })
    
    df = pd.DataFrame(results)
    
    # Create validation sample
    validation_sample = df.sample(n=min(validation_sample_size, len(df)))
    validation_sample['human_label'] = None
    validation_sample['agree'] = None
    
    return {
        'results': df,
        'validation_sample': validation_sample,
        'instructions': """
⚠️ VALIDATION REQUIRED

Before using these results:
1. Human-code the validation sample
2. Calculate LLM-human agreement (κ)
3. If κ < 0.7, do NOT use LLM labels — code manually
4. If κ ≥ 0.7, can use LLM labels with documented accuracy
5. Report LLM-human agreement in methods section
        """,
        'distribution': df['llm_label'].value_counts().to_dict()
    }
```

---

## Reporting Template

```markdown
## Content Analysis Methods

### Codebook
- **Categories**: [List]
- **Source**: [Developed for study / Adapted from X]
- **Attached**: [Link to full codebook]

### Sampling
- **Population**: N items
- **Sample**: n items
- **Method**: [Random / Stratified / Purposive]
- **Justification**: [Why this sampling approach]

### Coding Procedure
- **Coders**: [Number and training]
- **Process**: [How coding was done]
- **Disagreement resolution**: [Method]

### Inter-Coder Reliability
- **Reliability sample**: n items (X% of sample)
- **Cohen's κ**: [value] ([interpretation])
- **Krippendorff's α**: [value] (if applicable)
- **Percent agreement**: [value]%

### Category Distribution
| Category | n | % |
|----------|---|---|
| [Cat 1] | X | X% |
| [Cat 2] | X | X% |
...

### Limitations
1. [Limitation 1]
2. [Limitation 2]
```
