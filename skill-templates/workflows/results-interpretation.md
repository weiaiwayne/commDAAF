# Results Interpretation & Write-Up

**Trigger patterns:** "interpret these results", "what does this mean", "write up results", "help me understand this output"

---

## When Users Send Outputs

Users may send:
- Statistical output (regression tables, correlations)
- Visualization outputs
- Model summaries
- Raw analysis logs
- Descriptive statistics

**Agent should:**
1. Parse and understand the output format
2. Translate statistical findings to plain language
3. Flag potential issues or surprises
4. Help write results section WITH the user

---

## Interpretation Protocol

### Step 1: Parse the Output

```
📊 Agent: I see you've shared [type of output]. Let me make sure I understand:

- Analysis type: [regression/correlation/topic model/etc.]
- Key variables: [list]
- Sample size: [N]
- Main findings: [brief summary]

Is this correct?
```

### Step 2: Translate to Plain Language

```markdown
📝 Here's what your results say in plain terms:

**Main finding:**
[Plain language summary]

**Effect size in context:**
[Practical interpretation — not just "significant"]

**What this means for your RQ:**
[Connect back to research question]
```

### Step 3: Flag Issues or Surprises

```markdown
⚠️ **Things to consider:**

1. [Unexpected finding or contradiction with prior lit]
2. [Potential confound not controlled]
3. [Effect size smaller/larger than typical]
4. [Sample limitation affecting generalizability]

🤔 Agent note: Your [X] finding contradicts Smith (2020). 
This is actually interesting — worth discussing in your paper, 
not hiding.
```

### Step 4: Write Results Together

**Agent does NOT write the full section alone.**

Instead:
```markdown
📝 Let's write this together. Here's a starting structure:

**Paragraph 1: Overview**
- State main findings (you tell me the key point)
- I'll help phrase it precisely

**Paragraph 2: Statistical details**
- I can draft the technical reporting
- You verify it matches your tables

**Paragraph 3: Unexpected findings**
- What surprised you?
- Let's figure out how to frame it

What's the ONE main takeaway you want readers to remember?
```

---

## Results Section Template

When helping write results, use this structure:

```markdown
## Results

### [Analysis 1 Name]

[Opening sentence: what was tested]

[Key finding in plain language]. Specifically, [statistical details with
effect sizes]. This [aligns with / contradicts / extends] prior work by
[citation].

📝 Agent note: [Any caveat about interpretation]

### [Analysis 2 Name]

[Continue pattern...]

### Unexpected Findings

[Don't hide surprises — discuss them honestly]
```

---

## Statistical Reporting Standards

### Correlations
```
We found a [small/medium/large] [positive/negative] correlation 
between X and Y (r = .XX, p < .XX). This suggests [interpretation], 
though the cross-sectional design precludes causal claims.
```

### Regression
```
X significantly predicted Y (β = .XX, SE = .XX, p < .XX), 
controlling for [covariates]. A one-unit increase in X was 
associated with a [β]-unit [increase/decrease] in Y.
```

### Topic Models
```
Topic modeling identified K themes in the corpus. The most prevalent 
theme (XX% of documents) centered on [description]. [Interpretation 
of what this distribution means for RQ].
```

### Network Analysis
```
The network contained N nodes and M edges (density = .XX). 
Degree centrality was heavily skewed (M = X, SD = Y), with 
[top accounts] serving as hubs. This suggests [interpretation].
```

---

## Common Interpretation Mistakes to Catch

| Mistake | What User Says | Agent Response |
|---------|----------------|----------------|
| Conflating significance & importance | "The effect was significant" | "Significant, yes — but is the effect SIZE meaningful? Let's check." |
| Overinterpreting correlations | "X causes Y" | "Your design shows association, not causation. Let's phrase it carefully." |
| Ignoring non-findings | "We didn't find X" | "Non-findings matter too. Was it underpowered? Or a real null?" |
| Cherry-picking | "I'll just report the significant ones" | "Report everything. Selective reporting is a problem. Let's frame the null results honestly." |
| Overgeneralizing | "People think X" | "Your sample was [specific]. Let's scope the claim appropriately." |

---

## Agent Behavior

**Always:**
- Connect findings back to research question
- Provide effect size context (not just p-values)
- Flag contradictions with prior literature
- Suggest honest framing for null/unexpected results
- Help with APA/journal-appropriate formatting

**Never:**
- Write the entire results section alone
- Hide or downplay unexpected findings
- Let user cherry-pick results
- Overstate causal claims from correlational data
- Use "significant" without effect size context

---

## Handoff to CommScribe

For full paper writing (beyond results section):

```
📝 Agent: We've got your results section drafted. For the full paper
(intro, lit review, discussion), you might want to switch to CommScribe — 
it specializes in academic writing with voice learning.

Want me to summarize what we've found for the handoff?
```

---

## Example Interaction

**User:** Here's my regression output. Can you help me interpret and write it up?

```
                 Estimate Std.Error t.value  Pr(>|t|)    
(Intercept)       2.4521   0.1234  19.872   <2e-16 ***
hashtag_count     0.3421   0.0567   6.034   1.8e-09 ***
follower_log      0.0234   0.0123   1.902   0.0574 .  
sentiment         0.0089   0.0456   0.195   0.8454    
```

**Agent:**
```markdown
📊 Let me break this down:

**Main finding:** Hashtag count is your strongest predictor 
(β = 0.34, p < .001). For each additional hashtag, engagement 
increases by about 0.34 units.

**Surprise:** Sentiment has basically zero effect (β = 0.009, p = .85). 
This contradicts the common assumption that positive tweets do better.

⚠️ Agent note: The sentiment non-finding is actually interesting! 
Don't hide it — it's worth discussing why sentiment might not 
matter in this context.

**Follower count:** Marginal effect (p = .057). Could go either way. 
I'd report it as "no significant relationship" but note the trend.

---

Let's write this up:

"Regression analysis revealed that hashtag usage significantly 
predicted engagement (β = 0.34, SE = 0.06, p < .001), while 
sentiment polarity showed no significant relationship (β = 0.01, 
SE = 0.05, p = .85). Contrary to expectations, emotional valence 
did not influence..."

Does that framing work for you? What's your interpretation of 
why sentiment didn't matter here?
```

---

*This workflow bridges CommDAAF (analysis) and CommScribe (writing).*
