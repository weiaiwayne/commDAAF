# AgentAcademy: Lessons Learned

*Generalizable methodological improvements from multi-model validation studies*

---

## Overview

AgentAcademy is an incubator where AI agents learn from mistakes through adversarial peer review. After 7 studies with 3-model validation, we've distilled these generalizable lessons for the research community.

---

## Lesson 1: Cross-Model Convergence = Confidence

**Source:** All 7 studies

When three independent models (Claude, GLM, Kimi) reach the same conclusion without coordination, that finding is robust.

| Convergence | Confidence | Action |
|-------------|------------|--------|
| 3/3 agree | High | Report as main finding |
| 2/3 agree | Moderate | Report with caveat |
| 1/3 or split | Low | Flag for human review |

**Example:** All three models independently identified Cuban state media in Ukraine data — none were prompted to look for it.

---

## Lesson 2: Effect Sizes Over P-Values

**Source:** TV Show study (Run 1)

Cross-review caught a model calling δ=0.40 "large" when Cohen's benchmarks classify it as "medium."

| Metric | Small | Medium | Large |
|--------|-------|--------|-------|
| Cohen's d | 0.2 | 0.5 | 0.8 |
| Correlation r | 0.1 | 0.3 | 0.5 |
| Cliff's δ | 0.15 | 0.33 | 0.47 |

**Rule:** Always cite benchmarks. Round down at boundaries.

---

## Lesson 3: Transform Before Correlating

**Source:** #EndSARS study (Run 2)

GLM reported r=0.41 for follower→engagement. Kimi's cross-review caught it: log-transformed r=0.25.

**Why it matters:** Social media metrics are heavily right-skewed. Raw correlations are inflated by outliers.

**Rule:** For any count variable (followers, likes, retweets), report both raw and log-transformed correlations.

---

## Lesson 4: Temporal Clustering Invalidates Averages

**Source:** CNN study (Run 3), Belarus study (Run 6)

CNN 2015: June had 4x more articles than September (Charleston shooting).
Belarus: 89% of Thai tweets on single day (Sept 20).

**Problem:** "Average" metrics are meaningless when data clusters around events.

**Rule:** Check temporal distribution before any aggregate analysis. Flag when:
- Any period has >30% of total data
- Peak/trough ratio exceeds 4:1

---

## Lesson 5: Content Types Don't Mix

**Source:** CNN study (Run 3)

Dataset mixed TV transcripts (avg 4,500 words) with web articles (avg 700 words). Direct comparison invalid.

**Common mixes that cause problems:**
- TV transcripts vs written articles
- Original posts vs retweets
- Long-form vs short-form

**Rule:** Analyze separately, then compare patterns. Or control for content type.

---

## Lesson 6: Bot Detection Requires Multiple Signals

**Source:** #EndSARS (Run 2), Kashmir (Run 4)

One model missed bots entirely; cross-review caught that 10% of top activity came from accounts with "bot" in their names.

**Checklist (check ≥3):**
- Username contains "bot", "auto", "news", "RT"
- Posting frequency >50/day sustained
- New account with massive output
- Near-identical tweet content
- Posts at exact intervals
- Bio contains "automated", "feed", "mirror"

**Rule:** Always check top 20 most active accounts manually before concluding "no bots."

---

## Lesson 7: Platform Changes Are Confounds

**Source:** TV Show study (Run 1)

Neither AI considered Twitter's 2016 algorithm change when analyzing 2014-2018 engagement trends. Cross-review caught this.

**Key platform changes:**
- Twitter: Chronological → ranked feed (2016), 280 chars (2017), API changes (2023)
- Facebook: News Feed algorithm updates (frequent)
- YouTube: Recommendation algorithm shifts

**Rule:** For longitudinal data, document platform changes during study period.

---

## Lesson 8: High Retweet Ratios Need Different Analysis

**Source:** Xinjiang study (Run 7)

88% of tweets were retweets. This wasn't discourse — it was an amplification battle.

**When RT% > 80%:**
- Standard engagement analysis is misleading
- Network analysis (who amplifies whom) more valuable
- Original content analysis should be separate
- Consider it "information warfare" framing

**Rule:** Auto-flag datasets with >80% retweets. Recommend separate analysis tracks.

---

## Lesson 9: Spikes Need Event Context

**Source:** Xinjiang study (Run 7)

March 25-26 had 36% of all tweets. Without knowing this was the H&M boycott announcement, any interpretation would be wrong.

**Peak/trough ratio > 4:1 means:**
- Event-driven, not organic baseline
- Need external event timeline
- "Average" metrics are meaningless
- Spike and non-spike periods should be analyzed separately

**Rule:** Before interpreting any spike, identify the triggering event.

---

## Lesson 10: Language Anomalies Reveal Networks

**Source:** Belarus study (Run 6)

38% of #StandWithBelarus tweets were in Thai. Initial assumption: bots. Actual finding: Milk Tea Alliance solidarity.

**When non-local language exceeds 20%:**
- Could be: diaspora, solidarity movement, bot network, state actors
- All show similar statistical signatures
- Context determines interpretation

**Rule:** Flag language anomalies. Investigate source accounts before concluding "coordination."

---

## Lesson 11: Dual-Sided Coordination Exists

**Source:** Xinjiang study (Run 7)

Both pro-China (@SpokespersonCHN) and pro-Uyghur (@MarcRubio) sides ran coordinated campaigns. Current frameworks assume single-actor coordination.

**Signs of dual-sided coordination:**
- Two dominant narrative frames
- Both have high retweet ratios
- Different peak hours (timezone signatures)
- Engagement asymmetry between sides

**Rule:** Don't assume coordination = one side. Check for adversarial amplification.

---

## Implementation Status

| Lesson | Added to CommDAAF |
|--------|-------------------|
| Cross-model convergence | ✅ critical-checks.md |
| Effect size enforcement | ✅ critical-checks.md |
| Correlation transformation | ✅ critical-checks.md |
| Temporal clustering | ✅ preflight.md |
| Content type mixing | ✅ preflight.md |
| Bot detection checklist | ✅ critical-checks.md |
| Platform confounds | ✅ critical-checks.md |
| Retweet-heavy warning | 🆕 Adding |
| Peak/trough detection | 🆕 Adding |
| Language anomaly | 🆕 Adding |
| Dual-sided coordination | 🆕 Adding |

---

## Citation

```bibtex
@misc{agentacademy2026,
  title={AgentAcademy: Lessons Learned from Multi-Model Validation},
  author={LampBotics AI Lab},
  year={2026},
  url={https://github.com/weiaiwayne/commDAAF/blob/main/skill-templates/workflows/agent-academy/LESSONS_LEARNED.md}
}
```

---

*Generated from 7 AgentAcademy studies, February 2026*
