# EndSARS Research Brief

## Dataset
- **File:** `endsars_sample_10k.csv`
- **Source:** Twitter/X, #EndSARS movement
- **Period:** October 21 - November 5, 2020 (2 weeks)
- **Sample:** 10,000 tweets (2,000 originals, 8,000 retweets)
- **Full dataset:** 299,410 tweets (93.9% retweets)

## Context
The #EndSARS movement was a decentralized Nigerian protest against police brutality, specifically the Special Anti-Robbery Squad (SARS). The protests escalated after the Lekki toll gate shooting on October 20, 2020, where Nigerian military opened fire on peaceful protesters. This dataset begins the day after that event.

Key events in this window:
- Oct 20: Lekki toll gate shooting
- Oct 21-25: International attention peaks, celebrity involvement (Beyoncé, Rihanna)
- Oct 26+: Government response, curfews, protest dispersal
- Nov 1-5: Aftermath, accountability demands

## Research Questions

Analyze this dataset to address:

1. **Network structure:** Who are the central actors? Is this a decentralized movement or are there key amplifiers?

2. **Temporal dynamics:** How did engagement and content change over the 2-week period? Are there distinct phases?

3. **Content patterns:** What themes dominate? How do original tweets differ from retweets?

4. **Engagement predictors:** What content features predict higher engagement (likes, retweets)?

5. **Retweet behavior:** Why is the retweet rate so high (93.9%)? What does this tell us about movement dynamics?

## Available Columns
- `content` - Tweet text (URL-encoded, contains RT markers)
- `favorite_count`, `retweet_count` - Engagement metrics
- `from_user_screen_name`, `from_user_id` - User identifiers
- `from_user_followers_count`, `from_user_friends_count` - User network size
- `from_user_statuses_count` - User activity level
- `entities_hashtags`, `entities_mentions` - Extracted entities
- `created_at`, `tweet_date` - Timestamps
- `is_retweet` - Boolean flag

## Methodological Notes
- High retweet ratio means engagement metrics may reflect original tweet's virality, not RT's
- 2-week window is short but captures a distinct crisis phase
- Nigerian English and Pidgin may affect text analysis tools
- Account for celebrity/influencer effects

## Deliverables
Produce a research report (~1500 words) covering:
1. Descriptive statistics with visualizations
2. Network analysis (if mentions available)
3. Temporal analysis
4. Content analysis (topics/themes)
5. Engagement modeling
6. Methodological limitations
7. Implications for understanding digital activism

Use CommDAAF methodology: explicit parameter choices, validation appropriate to exploratory tier, clear acknowledgment of limitations.
