# Autonomous Research with Cross-Agent Review

**Purpose:** Agents independently analyze data, generate hypotheses, test them, write results, then critique each other's work.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        SAMPLE DATA                               │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│      AGENT A (GLM)      │     │     AGENT B (Kimi)      │
│                         │     │                         │
│  1. Explore data        │     │  1. Explore data        │
│  2. Generate RQs        │     │  2. Generate RQs        │
│  3. Run analysis        │     │  3. Run analysis        │
│  4. Write results       │     │  4. Write results       │
└───────────┬─────────────┘     └───────────┬─────────────┘
            │                               │
            │         CROSS-REVIEW          │
            │◄──────────────────────────────┤
            ├──────────────────────────────►│
            │                               │
            ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│   Agent B critiques     │     │   Agent A critiques     │
│   Agent A's work        │     │   Agent B's work        │
└───────────┬─────────────┘     └───────────┬─────────────┘
            │                               │
            └───────────────┬───────────────┘
                            ▼
              ┌─────────────────────────┐
              │    MAIN (Opus 4.5)      │
              │                         │
              │  Synthesize findings    │
              │  Reconcile disagreements│
              │  Final report           │
              └─────────────────────────┘
```

---

## Phase 1: Parallel Independent Analysis

Both agents receive the same data and work independently.

### Agent Prompt Template

```markdown
# Research Task

You have been given a dataset to analyze. Your task:

## 1. Data Exploration (10 min)
- What's in this data? (variables, timeframe, N)
- Data quality issues?
- Initial patterns you notice?

## 2. Research Questions (5 min)
Generate 2-3 testable research questions based on what you see.
Format each as:
- **RQ**: [Question]
- **Hypothesis**: [Expected finding and why]
- **Test**: [How you'll test this]

## 3. Analysis (15 min)
For each RQ:
- Run appropriate analysis
- Document your code/approach
- Report results with uncertainty

## 4. Write-Up (10 min)
Produce a brief research memo:
- Summary of findings
- Methods used
- Limitations
- Implications

## Constraints
- Be explicit about every methodological choice
- Report uncertainty/confidence intervals
- Acknowledge limitations
- Don't overclaim (correlations ≠ causation)

## Data
{data_description}
{data_path_or_content}
```

---

## Phase 2: Cross-Agent Review

After both agents complete Phase 1, they swap outputs.

### Review Prompt Template

```markdown
# Peer Review Task

You are reviewing another researcher's analysis. Your job is adversarial but constructive.

## Their Analysis
{other_agent_output}

## Review Criteria

### 1. Research Questions
- Are the RQs answerable with this data?
- Are hypotheses justified?
- Missing obvious questions?

### 2. Methodology
- Appropriate methods for the RQs?
- Correct implementation?
- Missing controls/confounds?
- Proper validation?

### 3. Results Interpretation
- Do conclusions follow from data?
- Overclaiming? (causal language from correlations)
- Alternative explanations considered?
- Effect sizes vs statistical significance?

### 4. Limitations
- Acknowledged appropriately?
- Missing limitations?

### 5. What They Did Better Than You
- Any insights you missed?
- Methods you should have used?
- Questions you didn't think of?

## Output Format
```yaml
overall_assessment: [strong/adequate/weak]

strengths:
  - [strength 1]
  - [strength 2]

critical_issues:
  - issue: [description]
    severity: [blocker/major/minor]
    suggestion: [how to fix]

methodological_concerns:
  - [concern 1]
  - [concern 2]

things_they_did_better:
  - [insight 1]
  - [insight 2]

verdict: [accept/revise/reject]
```
```

---

## Phase 3: Synthesis

Main agent (Opus) receives:
- Agent A's analysis
- Agent B's critique of A
- Agent B's analysis  
- Agent A's critique of B

### Synthesis Prompt

```markdown
# Research Synthesis

You have two independent analyses of the same dataset, plus cross-reviews.

## Agent A's Work
{agent_a_analysis}

## Agent B's Critique of A
{agent_b_review_of_a}

## Agent B's Work
{agent_b_analysis}

## Agent A's Critique of B
{agent_a_review_of_b}

## Your Task

### 1. Convergent Findings
What did both agents find? These are more robust.

### 2. Divergent Findings
Where do they disagree? Analyze why:
- Different methods?
- Different interpretations?
- One is wrong?

### 3. Methodological Assessment
Whose methods were more appropriate? Why?

### 4. Synthesis Report
Produce a final report that:
- Integrates the strongest findings from both
- Notes where uncertainty remains
- Acknowledges what we can and cannot conclude
- Recommends next steps

### 5. Meta-Learning
What did this dual-analysis reveal that a single analysis would have missed?
```

---

## Implementation

### Using OpenClaw sessions_spawn

```python
async def run_autonomous_research(data_path: str, data_description: str):
    """
    Run full autonomous research workflow with cross-review.
    """
    
    # Phase 1: Parallel analysis
    agent_a_task = f"""
    Analyze this dataset and produce a research memo.
    
    Data: {data_path}
    Description: {data_description}
    
    Follow the research protocol:
    1. Explore data
    2. Generate 2-3 RQs with hypotheses
    3. Test hypotheses
    4. Write up findings with limitations
    """
    
    agent_b_task = agent_a_task  # Same task, different agent
    
    # Spawn both agents in parallel
    result_a = await sessions_spawn(
        task=agent_a_task,
        agentId="redteam-glm",  # Uses z.ai GLM-4.7
        label="research-agent-a"
    )
    
    result_b = await sessions_spawn(
        task=agent_b_task,
        agentId="redteam-kimi",  # Uses Kimi K2.5
        label="research-agent-b"
    )
    
    # Wait for both to complete
    analysis_a = await get_result(result_a)
    analysis_b = await get_result(result_b)
    
    # Phase 2: Cross-review
    review_a_task = f"""
    Review this research analysis. Be adversarial but constructive.
    
    Analysis to review:
    {analysis_b}
    
    Evaluate: RQs, methods, interpretation, limitations.
    Note what they did better than you might have.
    """
    
    review_b_task = f"""
    Review this research analysis. Be adversarial but constructive.
    
    Analysis to review:
    {analysis_a}
    
    Evaluate: RQs, methods, interpretation, limitations.
    Note what they did better than you might have.
    """
    
    critique_a = await sessions_spawn(
        task=review_a_task,
        agentId="redteam-glm",
        label="review-agent-a"
    )
    
    critique_b = await sessions_spawn(
        task=review_b_task,
        agentId="redteam-kimi", 
        label="review-agent-b"
    )
    
    review_of_b = await get_result(critique_a)  # A reviews B
    review_of_a = await get_result(critique_b)  # B reviews A
    
    # Phase 3: Synthesis (main agent)
    synthesis_task = f"""
    Synthesize these two independent research analyses.
    
    ## Agent A (GLM) Analysis:
    {analysis_a}
    
    ## Agent B (Kimi) Critique of A:
    {review_of_a}
    
    ## Agent B (Kimi) Analysis:
    {analysis_b}
    
    ## Agent A (GLM) Critique of B:
    {review_of_b}
    
    Produce:
    1. Convergent findings (both found)
    2. Divergent findings (disagreements + why)
    3. Methodological assessment
    4. Integrated final report
    5. What dual-analysis revealed that single wouldn't
    """
    
    # This runs in main session (Opus 4.5)
    final_report = await synthesize(synthesis_task)
    
    return {
        'agent_a_analysis': analysis_a,
        'agent_b_analysis': analysis_b,
        'review_of_a': review_of_a,
        'review_of_b': review_of_b,
        'synthesis': final_report
    }
```

---

## Sample Data for Testing

Use files in `sample-data/`:

| File | Description | Good for testing |
|------|-------------|------------------|
| `#EndSARS_*.xlsx` | Nigerian protest tweets | Network analysis, sentiment, coordination |
| `UKR-tweets.xlsx` | Ukraine conflict tweets | Framing, stance, temporal patterns |
| `CNN.pkl` | News content | Topic modeling, agenda-setting |

---

## Expected Outputs

### From Each Agent
1. **Data profile** (N, variables, quality)
2. **2-3 RQs** with hypotheses
3. **Analysis code/approach**
4. **Results** with uncertainty
5. **Interpretation** with limitations

### From Cross-Review
1. **Strengths** of other's work
2. **Critical issues** (blocker/major/minor)
3. **What they did better**
4. **Verdict** (accept/revise/reject)

### From Synthesis
1. **Convergent findings** (robust)
2. **Divergent findings** (uncertainty)
3. **Integrated report**
4. **Meta-learning** (what dual revealed)

---

## Why This Works

| Feature | Benefit |
|---------|---------|
| Independent analysis | Different RQs emerge from different perspectives |
| Cross-review | Catches errors, overclaims, missed alternatives |
| "What they did better" | Forces humility, surfaces insights |
| Synthesis | Robust findings survive dual scrutiny |
| Model diversity | Different training → different blind spots |
