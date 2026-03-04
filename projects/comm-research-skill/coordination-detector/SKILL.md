# Coordination Detector

**Version:** 1.0  
**Status:** Production  
**Maintainer:** CommDAAF Team

---

## Purpose

Identify coordinated inauthentic behavior (CIB) in social media datasets before conducting substantive analysis. Coordination—whether by bots, state actors, or organized campaigns—distorts engagement metrics, inflates apparent consensus, and can invalidate findings if undetected.

This skill provides validated methods for coordination detection while explicitly documenting approaches that **do not work** to prevent wasted effort.

---

## When to Use

**Always run coordination detection when:**
- Analyzing political/contentious topics
- Studying viral content or high-engagement posts
- Examining cross-national discourse (state actors common)
- Investigating hashtag campaigns or trending topics
- Measuring "public opinion" from social media

**Skip only when:**
- Small qualitative samples you've manually vetted
- Private/closed group data (different coordination dynamics)
- Explicitly studying coordination itself (then it's your DV, not confound)

---

## Methods That Work

### 1. Co-Link Detection (CooRnet-Style)

**Principle:** Coordinated accounts share identical URLs within narrow time windows at rates exceeding chance.

**Implementation:**
```
For each URL shared by 2+ accounts:
  1. Extract all shares within time_window (default: 60 seconds)
  2. If n_accounts >= threshold (default: 3):
     Flag as coordinated cluster
  3. Build account co-occurrence network
  4. Identify densely connected components
```

**Validated by:** Giglietto et al. (2020), Righetti & Balluff (2025)

**Thresholds:**
| Time Window | Min Accounts | False Positive Risk |
|-------------|--------------|---------------------|
| 10 sec | 2 | Low (very suspicious) |
| 60 sec | 3 | Low |
| 5 min | 5 | Medium |
| 1 hour | 10 | High (may catch organic) |

**Limitations:** Requires URL-sharing behavior; misses coordination via text-only content.

---

### 2. Temporal Burst Detection

**Principle:** Coordinated campaigns produce unnatural activity spikes—too many posts, too fast, too synchronized.

**Implementation:**
```
1. Bin posts by time interval (1min, 5min, 1hr)
2. Calculate expected rate (baseline from non-peak periods)
3. Flag intervals where:
   - Volume > 3σ above baseline
   - AND account diversity is LOW (few accounts, many posts)
   - AND content similarity is HIGH
4. Examine flagged intervals for coordination signatures
```

**Signatures of coordination:**
- Posts appear at identical seconds (bot synchronization)
- Round-number timing (every 5 min, on the hour)
- Immediate response to trigger events (< 30 sec)
- Activity during off-hours for claimed timezone

**Signatures of organic bursts:**
- Gradual ramp-up, not instant spike
- High account diversity
- Content variation (quotes, reactions, not copy-paste)
- Timing matches news cycle

---

### 3. Content Similarity Clustering

**Principle:** Coordinated accounts share near-identical content (copy-paste, templates, minor variations).

**Implementation:**
```
1. Compute text similarity (Jaccard, cosine, edit distance)
2. Cluster posts with similarity > threshold (default: 0.8)
3. For each cluster:
   - If n_unique_accounts >= 3
   - AND time_spread < 24 hours
   - Flag as coordinated content
4. Examine clusters for template patterns
```

**Detection patterns:**
| Pattern | Example | Confidence |
|---------|---------|------------|
| Identical text | Same tweet from 50 accounts | Very High |
| Template + variable | "I support [NAME] because [REASON]" | High |
| Paraphrase cluster | Same claim, different words | Medium |
| Hashtag stuffing | Same 5+ hashtags, different text | Medium |

**Limitations:** Sophisticated campaigns use diverse content; this catches low-effort coordination only.

---

### 4. Account Characteristic Profiling

**Principle:** Inauthentic accounts share telltale metadata patterns.

**Indicators (weighted scoring):**

| Indicator | Weight | Suspicious Threshold |
|-----------|--------|---------------------|
| Account age | 0.15 | < 30 days |
| Default profile pic | 0.10 | Yes |
| Follower/following ratio | 0.10 | < 0.01 or > 100 |
| Tweet frequency | 0.15 | > 50/day sustained |
| Retweet ratio | 0.15 | > 90% of activity |
| Bio keywords | 0.10 | Generic/templated |
| Name pattern | 0.10 | [Name][Numbers] format |
| Activity hours | 0.15 | 24/7 or wrong timezone |

**Scoring:**
```
bot_score = Σ(indicator_weight × indicator_present)
if bot_score > 0.6: flag_for_review
if bot_score > 0.8: likely_automated
```

**Validation:** Cross-reference with Botometer, manual inspection of high-scorers.

---

### 5. Network Amplification Patterns

**Principle:** Coordinated networks show structural signatures—who amplifies whom reveals organization.

**Implementation:**
```
1. Build directed retweet/reply network
2. Calculate:
   - In-degree concentration (few accounts receiving most amplification)
   - Reciprocity (coordinated accounts often don't follow back)
   - Clustering coefficient (coordinated groups are densely connected)
   - Temporal amplification speed (how fast do RTs appear?)
3. Compare to baseline organic networks
```

**Red flags:**
- Single account receives >10% of all retweets
- Amplification happens < 60 seconds after posting
- Perfect retweet chains (A→B→C→D, no branching)
- Accounts only interact within closed group

---

## Methods That DO NOT Work

### ❌ Cross-Layer Behavioral Discordance (CLBD)

**What it is:** Measuring whether accounts retweet different people than they reply to.

**Why it seems reasonable:** Intuition suggests authentic users would engage consistently across modalities.

**Why it FAILS:**

> **Empirical finding (Xu et al., 2026):** 80% of organic users show zero overlap between retweet and reply targets. Established accounts (>3 years) show MORE discordance (83.5%) than new accounts (53.1%).

**Explanation:** Discordance is normal platform behavior. Users retweet news/experts but reply to friends/community. These are *different* relationships serving *different* functions.

**Do not use CLBD as coordination signal.** It detects user type (broadcaster vs. conversationalist), not authenticity.

---

### ❌ Simple Activity Volume

**What it is:** Flagging accounts that post "too much."

**Why it FAILS:** High-volume authentic accounts exist (journalists, activists, brands). Volume alone has high false positive rate.

**Use instead:** Volume + other signals (timing patterns, content diversity, account age).

---

### ❌ Follower Count Thresholds

**What it is:** Assuming low-follower accounts are bots.

**Why it FAILS:** New authentic users have low followers. Some bot networks cultivate followers. Follower count has weak discrimination.

**Use instead:** Follower/following ratio + account age + activity patterns.

---

## Decision Protocol

```
┌─────────────────────────────────────────────┐
│  COORDINATION DETECTION PROTOCOL            │
└─────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 1. RUN CO-LINK DETECTION      │
    │    (if URL data available)    │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 2. RUN TEMPORAL BURST CHECK   │
    │    Flag unnatural spikes      │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 3. RUN CONTENT SIMILARITY     │
    │    Cluster near-duplicates    │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 4. PROFILE FLAGGED ACCOUNTS   │
    │    Score account metadata     │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 5. BUILD AMPLIFICATION NETWORK│
    │    Check structural patterns  │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 6. MANUAL VALIDATION          │
    │    Inspect top 50 flagged     │
    └───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ 7. REPORT & DECIDE            │
    │    - % flagged                │
    │    - Remove or analyze        │
    │    - Document either way      │
    └───────────────────────────────┘
```

---

## Reporting Template

```markdown
## Coordination Detection Report

**Dataset:** [description]
**N posts:** [number]
**N accounts:** [number]
**Detection date:** [date]

### Methods Applied
- [ ] Co-link detection (window: __ sec, threshold: __ accounts)
- [ ] Temporal burst detection (baseline: __, σ threshold: __)
- [ ] Content similarity (threshold: __, min cluster: __)
- [ ] Account profiling (score threshold: __)
- [ ] Network analysis (metrics: __)

### Findings

| Method | Accounts Flagged | % of Total | Confidence |
|--------|------------------|------------|------------|
| Co-link | | | |
| Temporal | | | |
| Content | | | |
| Profile | | | |
| Network | | | |
| **Combined** | | | |

### Overlap Analysis
[How many accounts flagged by multiple methods?]

### Manual Validation
[Results of inspecting top 50 flagged accounts]

### Decision
- [ ] Remove flagged accounts from analysis
- [ ] Keep but control for in analysis
- [ ] Report as finding (coordination IS the story)
- [ ] No significant coordination detected

### Limitations
[What this detection might have missed]
```

---

## Integration with CommDAAF

### Pre-Analysis Check
```
Before any substantive coding:
1. Run coordination detection
2. Document findings in study protocol
3. Decide handling strategy
4. If removing accounts, report original vs. cleaned N
```

### Multi-Model Validation
```
For disputed flags:
1. Have second model review flagged accounts
2. Calculate inter-model agreement on flags
3. Only remove accounts both models flag
4. Document disagreements
```

### Dual-Sided Detection

**Critical lesson from Belarus/Xinjiang studies:**

> Coordination exists on BOTH sides of controversies. Pro-government AND opposition may use coordinated tactics. Always check both sides or you'll bias your analysis.

```
For any political/contentious topic:
1. Define "sides" in the discourse
2. Run detection on EACH side separately
3. Compare coordination prevalence
4. Report both, not just one
```

---

## Tools & Resources

### Existing Tools
- **CooRnet** (R): https://github.com/fabiogiglietto/CooRnet
- **CooRTweet** (R): Righetti & Balluff 2025
- **Botometer** (API): https://botometer.osome.iu.edu/
- **twarc** (Python): Twitter data collection with coordination fields

### Academic References
- Giglietto, F., et al. (2020). Coordinated link sharing behavior. *Information, Communication & Society*.
- Pacheco, D., et al. (2021). Uncovering coordinated networks on social media. *ICWSM*.
- Nizzoli, L., et al. (2021). Coordinated behavior on social media. *WWW*.
- Righetti, N., & Balluff, P. (2025). CooRTweet. *Computational Communication Research*.

### What NOT to Cite
- Do not cite CLBD-based methods as validated coordination detection (see "Methods That Do Not Work" above)

---

## Changelog

- **v1.0 (2026-03):** Initial release. Includes co-link, temporal, content, profile, and network methods. Documents CLBD as invalid approach based on empirical testing.

---

## Examples

See `EXAMPLES.md` for worked examples on:
- Twitter political campaign (URL coordination)
- Telegram channel network (content similarity)
- Reddit brigade detection (temporal + network)
- YouTube comment coordination (profile + content)
