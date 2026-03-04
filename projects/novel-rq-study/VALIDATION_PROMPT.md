# AgentAcademy Validation Task

You are an independent reviewer validating novel research findings on the #MahsaAmini dataset.

## Your Task

Analyze the merged dataset at `/root/.openclaw/workspace/skills/commdaaf/projects/novel-rq-study/merged_data.csv` to test these hypotheses:

### RQ1: Diaspora Amplification
- Compare engagement between English (`lang='en'`) and Persian (`lang='fa'`) posts
- Calculate mean engagement by Frame × Language
- Test: Does language moderate the frame-engagement relationship?

### RQ2: Temporal Dynamics  
- Compare frame prevalence between `phase='onset'` and `phase='peak'`
- Calculate engagement by Frame × Phase
- Test: Do frames change in effectiveness over time?

### RQ3: Power Law Distribution
- Calculate Gini coefficient for engagement by frame
- Identify which frames have most concentrated vs distributed engagement

### RQ4: Coordination Signals
- Group posts by hour (`created_at` rounded to hour)
- Calculate peak/trough ratios by frame
- Calculate engagement-follower correlation by frame

## Output Format

Provide:
1. Key statistics for each RQ
2. Your conclusions (SUPPORTED / NOT SUPPORTED / PARTIAL)
3. Any divergences from expected patterns

## Data Dictionary

- `id`: Tweet ID
- `text`: Tweet content  
- `engagement`: Log engagement (ln scale)
- `engagement_raw`: Raw engagement (exp of engagement)
- `frame`: SOLIDARITY, INJUSTICE, CALL_TO_ACTION, HOPE, HUMANITARIAN, INFORMATIONAL, CONFLICT
- `lang`: en, fa, ar, und
- `phase`: onset (Sept 16-22), peak (Sept 23+)
- `created_at`: Timestamp
- `followers`: Account follower count

Run your analysis independently. Do not reference any prior conclusions.
