# AgentAcademy Run 7 - Xinjiang Cotton Campaign Analysis

**Date:** February 20, 2026, 05:30 UTC  
**Dataset:** #xinjiang_#xinjiangcotton_325to401_withuserinfo.csv  
**Records:** 92,038 tweets  
**Date range:** March 20 - April 1, 2021

## Context
The Xinjiang cotton controversy erupted in late March 2021 when Chinese consumers organized boycotts against H&M, Nike, and other Western brands that had expressed concerns about forced labor in Xinjiang cotton production. This dataset captures tweets using #Xinjiang and #XinjiangCotton hashtags during this period.

## Dataset Characteristics
- **Languages:** 85% English, 4% Chinese, 2% French, others
- **Peak activity:** March 25-26 (34,516 tweets combined)
- **Key hashtags:** #Xinjiang, #China, #XinjiangCotton, #Uyghurs
- **Fields:** Full tweet metadata + user info (followers, verified status, location, etc.)

## Research Questions for 3-Model Analysis

### RQ1: Coordinated Amplification Detection
Is there evidence of coordinated inauthentic behavior in the tweet volume spike on March 25-26? Look for:
- Duplicate/near-duplicate content
- Account creation date clustering
- Unusual posting velocity patterns
- Network of synchronized accounts

### RQ2: Narrative Framing Analysis
What are the competing narrative frames, and which accounts promote each?
- Pro-China frame: "Western lies", "economic attack", "sovereignty"
- Pro-Uyghur frame: "genocide", "forced labor", "human rights"
- Compare engagement metrics between frames

### RQ3: State-Linked Account Behavior
Are there identifiable patterns suggesting state-linked amplification?
- Verified accounts (especially media)
- Account descriptions mentioning state media
- Location patterns (China vs diaspora vs Western)

### RQ4: Temporal Dynamics
How did the conversation evolve over the 13-day period?
- What triggered the March 25 spike?
- How quickly did each narrative establish dominance?
- Weekend vs weekday patterns

### RQ5: Engagement Asymmetries
Which content types drove engagement?
- Retweet vs original content ratios
- Media (URLs) presence
- Reply patterns (debate vs echo chamber)

## CommDAAF Critical Checks
- [ ] Temporal periodization for the spike
- [ ] Language-specific analysis (not just English)
- [ ] Account creation date analysis
- [ ] Engagement normalization by follower count
- [ ] Duplicate content detection

## Output Files Expected
- XINJIANG_Claude.md
- XINJIANG_GLM.md  
- XINJIANG_Kimi.md
- XINJIANG_SYNTHESIS_RUN7.md
