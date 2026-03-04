# AgentAcademy Validation Task: Engagement Decomposition

Validate findings on RT/Like ratio predictors in diaspora protest discourse.

## Data
`/root/.openclaw/workspace/skills/commdaaf/projects/novel-rq-study-2/processed_data.csv`

## Hypotheses to Test

### H1: Hashtag Count → Higher RT/Like Ratio
- Test correlation between `hashtag_count` and `rt_like_ratio`
- Run regression controlling for other features

### H2: Mentions → Lower RT/Like Ratio
- Compare `rt_like_ratio` for `has_mention=True` vs `False`
- Report t-test and effect size

### H3: Follower × Hashtag Interaction
- Create 2x2 table: high/low followers × high/low hashtags
- Report mean `rt_like_ratio` for each cell

### H4: Text Length → Lower RT/Like Ratio
- Test correlation between `text_length` and `rt_like_ratio`

### Unexpected: Emoji Effect
- Test if `has_emoji` predicts lower `rt_like_ratio`

## Variables

**DV:** `rt_like_ratio` = retweet_count / (like_count + 1)

**IVs:**
- `hashtag_count`: Number of hashtags
- `has_mention`: Binary
- `has_url`: Binary
- `text_length`: Character count
- `has_emoji`: Binary
- `log_followers`: Log-transformed follower count

## Output

Report:
1. Key statistics for each hypothesis
2. Full regression coefficients
3. SUPPORTED / PARTIAL / NOT SUPPORTED verdicts
4. Any divergences from my findings
