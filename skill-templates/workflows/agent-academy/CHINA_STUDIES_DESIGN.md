# AgentAcademy: China-Related Coordination Studies

> **Context**: Testing claims related to state-aligned information operations, inspired by research on LLM censorship bias in Chinese-trained models (PNAS Nexus, Citizen Lab). If LLMs trained on Chinese data exhibit censorship patterns, do we see similar patterns in social media coordination?
>
> **Datasets Available**:
> - `#xinjiang_#xinjiangcotton_325to401_withuserinfo.csv` — 189K tweets (March 2021)
> - `bios_RT_CN_between60secs_and_1hr.csv` — 11K coordinated user bios
> - `rt_cn_sharedbetween_60secs_and_1hr.csv` — 41K coordinated retweets
> - `HongKong_recent1000k_df.pkl` — 71K Reddit posts
> - `cn_digital_diplomacy_tiktok.rda` — Chinese digital diplomacy on TikTok

---

## Study 1: Coordinated Amplification in Xinjiang Discourse

### Research Question
**RQ1**: Do accounts amplifying pro-CCP Xinjiang narratives exhibit coordinated behavior patterns (temporal clustering, content similarity) distinct from organic users?

### Method
- **Temporal Analysis**: Cluster retweet timing within 60-second windows
- **Content Analysis**: LLM-based frame classification (pro-CCP, critical, neutral, ambiguous)
- **Network Analysis**: Identify retweet cascades from state-affiliated accounts

### Data
- Primary: `#xinjiang_#xinjiangcotton_325to401_withuserinfo.csv`
- Validation: `rt_cn_sharedbetween_60secs_and_1hr.csv`

### Hypothesis
H1a: Accounts retweeting within 60 seconds of state-affiliated sources show higher content similarity than organic retweeters.
H1b: Coordinated accounts have younger account ages and lower follower/following ratios.

### AgentAcademy Protocol
```yaml
agents:
  - GLM-4.7: Temporal clustering + engagement patterns
  - Kimi K2.5: Frame analysis + narrative consistency
cross_validation:
  - Compare coordination scores
  - Validate frame classifications on 100-tweet sample
```

### Credibility Tier: 🔴 Publication

---

## Study 2: Bot Detection in China-Nexus Retweet Networks

### Research Question
**RQ2**: What proportion of accounts participating in coordinated China-related retweets exhibit bot-like characteristics?

### Method
- **Bot Detection Heuristics**:
  - Default profile image
  - Numeric username suffix
  - Account age < 90 days
  - Tweet frequency > 50/day
  - Bio contains specific patterns (empty, copied, propaganda keywords)
- **Network Position**: Centrality in retweet graph

### Data
- Primary: `bios_RT_CN_between60secs_and_1hr.csv` (bios)
- Secondary: `rt_cn_sharedbetween_60secs_and_1hr.csv` (network)

### Variables
| Variable | Operationalization |
|----------|-------------------|
| Bot score | Sum of 5 heuristics (0-5) |
| Coordination score | Degree centrality × timing cluster |
| Account authenticity | Age × follower ratio × profile completeness |

### AgentAcademy Protocol
```yaml
agents:
  - GLM-4.7: Bot heuristic scoring + network metrics
  - Kimi K2.5: Bio text analysis for copied/template patterns
cross_validation:
  - Bot classification agreement (Cohen's κ)
  - Manual audit of top 50 flagged accounts
```

### Credibility Tier: 🟡 Pilot

---

## Study 3: Narrative Framing in #XinjiangCotton Controversy

### Research Question
**RQ3**: How did narrative frames evolve during the Xinjiang cotton boycott controversy (March 2021), and which frames were amplified by coordinated accounts?

### Method
- **Frame Identification**: LLM-assisted frame extraction
  - Economic nationalism ("buy Chinese")
  - Human rights framing (forced labor)
  - Anti-Western imperialism
  - Brand accountability
  - Information warfare ("Western lies")
- **Temporal Evolution**: Frame prevalence over time
- **Coordination-Frame Correlation**: Do coordinated accounts disproportionately amplify specific frames?

### Data
- Primary: `#xinjiang_#xinjiangcotton_325to401_withuserinfo.csv`

### Expected Frames
1. **Defensive nationalism**: Rejecting foreign interference
2. **Counter-narrative**: Denying forced labor claims
3. **Consumer activism**: Boycott Western brands
4. **Information warfare**: Accusing West of disinformation
5. **Worker testimonials**: "Happy workers" content

### AgentAcademy Protocol
```yaml
agents:
  - GLM-4.7: Frame classification + temporal analysis
  - Kimi K2.5: Cross-cultural frame interpretation
divergence_check:
  - Flag frames where agents disagree > 20%
  - Human review of ambiguous cases
```

### Credibility Tier: 🔴 Publication

---

## Study 4: Cross-Platform Comparison (Twitter vs Reddit)

### Research Question
**RQ4**: Do Hong Kong-related discussions on Reddit exhibit different coordination patterns than Twitter, given Reddit's different moderation structure?

### Method
- **Platform Comparison**:
  - Twitter (coordination data): Retweet timing, account networks
  - Reddit (HongKong data): Submission timing, subreddit clustering
- **Content Divergence**: Compare dominant narratives across platforms

### Data
- Twitter: `rt_cn_sharedbetween_60secs_and_1hr.csv` (filter HK content)
- Reddit: `HongKong_recent1000k_df.pkl`

### Hypothesis
H4a: Reddit shows less temporal coordination due to different platform affordances.
H4b: Pro-CCP narratives are less prevalent on Reddit than Twitter.

### AgentAcademy Protocol
```yaml
agents:
  - GLM-4.7: Reddit temporal patterns + subreddit analysis
  - Kimi K2.5: Cross-platform narrative comparison
methodological_note:
  - Account for platform differences (Reddit pseudonymity vs Twitter)
  - Cannot directly compare coordination metrics
```

### Credibility Tier: 🟢 Exploratory

---

## Study 5: TikTok Digital Diplomacy Strategies

### Research Question
**RQ5**: What strategies characterize Chinese digital diplomacy on TikTok, and how do they differ from Twitter-based diplomacy?

### Method
- **Content Analysis**: Video content categorization
  - Soft power (culture, tourism, lifestyle)
  - Hard messaging (policy, rebuttals)
  - Wolf warrior (aggressive, confrontational)
  - Humanizing (officials' personal content)
- **Engagement Analysis**: Which strategies generate most engagement?
- **Platform Adaptation**: How does content differ from Twitter accounts?

### Data
- Primary: `cn_digital_diplomacy_tiktok.rda`

### AgentAcademy Protocol
```yaml
agents:
  - GLM-4.7: Content categorization + engagement analysis
  - Kimi K2.5: Cross-platform strategy comparison
limitation:
  - Video content requires metadata analysis (no actual video processing)
  - Engagement metrics may be platform-specific
```

### Credibility Tier: 🟡 Pilot

---

## Execution Schedule

| Run | Study | Dataset | Primary Method | Est. Time |
|-----|-------|---------|----------------|-----------|
| 1 | Study 2 | bios + rt_cn | Bot detection | 30 min |
| 2 | Study 1 | xinjiang | Coordination | 45 min |
| 3 | Study 3 | xinjiang | Frame analysis | 45 min |
| 4 | Study 4 | HK + rt_cn | Cross-platform | 30 min |
| 5 | Study 5 | tiktok | Digital diplomacy | 30 min |

---

## Cross-Study Validation

After completing all studies:

1. **Coordination Score Consistency**: Do accounts flagged as coordinated in Study 1 appear in Study 2's bot list?
2. **Frame-Coordination Link**: Do specific frames (Study 3) correlate with coordination scores (Study 1)?
3. **Platform Effects**: How do findings differ across Twitter/Reddit/TikTok?

---

## Ethical Considerations

1. **No individual targeting**: Report aggregate patterns, not individual accounts
2. **Attribution caution**: Coordination ≠ state direction (could be organic grassroots)
3. **Cultural context**: Some "coordination" may reflect collectivist communication norms
4. **Researcher positionality**: Acknowledge Western research perspective

---

## Connection to LLM Censorship Research

The PNAS Nexus paper and Citizen Lab research show that Chinese-trained LLMs exhibit censorship patterns on sensitive topics (Xinjiang, Hong Kong, Tibet, Taiwan, Tiananmen). 

**Our studies test the social media side**:
- If LLMs are trained on censored data, what does the uncensored Twitter/Reddit discourse look like?
- Do coordinated accounts amplify narratives consistent with censored LLM outputs?
- Can we identify the "information ecosystem" that shapes both LLM training data and social media campaigns?

---

## Output Format

Each study produces:
1. `STUDY_N_ANALYSIS_GLM.md` — GLM-4.7 analysis
2. `STUDY_N_ANALYSIS_KIMI.md` — Kimi K2.5 analysis
3. `STUDY_N_CROSSREVIEW.md` — Cross-agent validation
4. `STUDY_N_SYNTHESIS.md` — Final synthesis with credibility rating

---

*Created: 2026-02-18*
*Framework: CommDAAF AgentAcademy v0.7.0*
