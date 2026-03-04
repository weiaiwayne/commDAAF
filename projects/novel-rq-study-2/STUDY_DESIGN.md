# Novel Study 2: Engagement Decomposition in Diaspora Protest
## The Architecture of Amplification vs Endorsement

**Date:** 2026-03-04
**Tier:** 🟢 EXPLORATORY
**Sample:** 339 uncoded posts (88% English/diaspora)

---

## Literature Gap

Wayne's Zotero contains:
- Granovetter (1973): "The Strength of Weak Ties" — bridging relationships spread novel information
- Multiple papers on retweet prediction — hashtags, timing, followers predict retweets

**What's missing:** Studies decompose retweet COUNTS but don't compare retweet vs like RATIOS. The ratio reveals whether content is being SPREAD (bridging) vs APPROVED (bonding).

---

## Theoretical Framework

### Weak Ties Theory Applied to Protest

| Engagement Type | Network Function | Theoretical Meaning |
|-----------------|------------------|---------------------|
| **Retweet** | Bridging (weak ties) | "I want others to see this" |
| **Like** | Bonding (strong ties) | "I approve of this" |
| **High RT/Like Ratio** | Information diffusion | Content crosses network boundaries |
| **Low RT/Like Ratio** | Echo chamber | Content stays within existing network |

### Hypotheses

**H1: Hashtag Effect**
Posts with movement hashtags (#MahsaAmini) will have HIGHER RT/Like ratios because hashtags enable discovery across networks (weak tie bridging).

**H2: Mention Effect**
Posts with @mentions will have LOWER RT/Like ratios because mentions signal in-group conversation (strong tie bonding).

**H3: Follower Moderation**
The hashtag effect will be STRONGER for low-follower accounts (need hashtags to bridge) and WEAKER for high-follower accounts (already have reach).

**H4: Content Length**
Longer posts will have LOWER RT/Like ratios (too complex to share broadly; favor careful readers = strong ties).

---

## Operationalizations

### Dependent Variable
- **RT/Like Ratio:** `retweet_count / (like_count + 1)`
- Also test: RT proportion `retweet_count / (retweet_count + like_count + 1)`

### Independent Variables (extracted from text)
- **has_hashtag:** Binary, any # in text
- **hashtag_count:** Number of hashtags
- **has_mention:** Binary, any @ in text
- **mention_count:** Number of mentions
- **has_url:** Binary, any URL in text
- **text_length:** Character count
- **has_emoji:** Binary, any emoji
- **has_persian:** Binary, any Persian/Arabic script (even in English posts)

### Control Variables
- **followers:** Log-transformed
- **engagement_total:** Combined RT + likes
- **tier:** Engagement tier (controls for overall virality)

---

## Analysis Plan

1. **Feature Extraction:** Parse text for hashtags, mentions, URLs, length, emoji, Persian script
2. **Descriptive:** RT/Like ratio distribution by features
3. **Regression:** OLS on RT/Like ratio with features + controls
4. **Interaction:** Test Hashtag × Followers moderation
5. **Multi-Model Validation:** GLM and Kimi independently verify

---

## Why This Is Novel

| Previous Study | This Study |
|----------------|------------|
| Composite engagement | Decomposed RT vs Like |
| Frame effects | Text feature effects |
| What drives virality | What drives SPREADING vs APPROVING |
| Network structure ignored | Weak/strong ties theory |

**This hasn't been done on #MahsaAmini data, and the diaspora sample (88% English) is perfect for testing cross-network bridging.**

---

## Expected Contributions

1. **Theoretical:** Extend weak ties to protest engagement decomposition
2. **Methodological:** Show RT/Like ratio as analytical tool
3. **Practical:** Guide activists on content strategies for spread vs endorsement

---

*Study design generated autonomously by Claude Opus 4.5*
