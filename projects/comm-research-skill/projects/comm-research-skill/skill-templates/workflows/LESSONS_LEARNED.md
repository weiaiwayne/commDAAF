# AgentAcademy: Lessons Learned

This document captures methodological insights discovered through **AgentAcademy** — CommDAAF's incubator where AI agents learn from mistakes through adversarial peer review. Each lesson comes from real errors caught when independent AI analysts reviewed each other's work.

The academy works like this:
1. Multiple agents independently analyze the same dataset
2. Agents cross-review and critique each other's work
3. Errors and insights are documented here
4. Lessons become new probing questions and checks
5. Future agents benefit from accumulated wisdom

---

## Run 1: @EastLosHighShow Twitter Analysis (Feb 2026)

**Dataset:** 3,153 tweets from TV show account (2014-2018)  
**Agents:** GLM-4.7 + Kimi K2.5  
**Grade:** C+

### Lessons Learned

#### 1. Effect Size Misclassification
**Error:** GLM labeled δ=0.40 as "large" effect  
**Correct:** δ=0.40 is "medium" per Cohen (1988): small=0.2, medium=0.5, large=0.8  
**Fix Added:** Effect size reference table in critical-checks.md with explicit "don't round up" rule

#### 2. Temporal Validity for Multi-Year Data
**Error:** Neither analyst checked year distribution before running year-level comparisons  
**Problem:** 2018 had only 3 tweets — statistically meaningless for comparison  
**Fix Added:** Sample balance check requiring minimum N per group

#### 3. Platform Change Blind Spot
**Error:** Neither controlled for Twitter algorithm changes (2016) or character limit change (2017)  
**Fix Added:** Context change documentation check for longitudinal analysis

#### 4. Correlation Sign Error
**Error:** Kimi reported negative correlation but concluded positive relationship  
**Fix Added:** Directional consistency check requiring explicit sign verification

---

## Run 2: #EndSARS Twitter Analysis (Feb 2026)

**Dataset:** 299,410 tweets from Nigerian protest movement (Oct-Nov 2020)  
**Sample:** 10,000 tweets (8K retweets, 2K originals)  
**Agents:** GLM-4.7 + Kimi K2.5 (parallel analysis, then cross-review)

### Lessons Learned

#### 5. Correlation Transformation for Skewed Data
**Error:** GLM reported r=0.412, Kimi reported r=0.251 for same relationship  
**Explanation:** GLM used raw follower counts; Kimi log-transformed  
**Impact:** Raw correlation inflated by outliers (Twitter followers are heavily right-skewed)  
**Correct approach:** Log-transform (r=0.251) is methodologically sound; report both  
**Fix Added:** Correlation transformation check in critical-checks.md

#### 6. Bot Detection Blind Spot
**Error:** GLM barely mentioned bots; Kimi found ~10% of top activity from automated accounts (@RTEndSars, @TheEndSarsBot, @sorosokebot)  
**Impact:** Missing bots can dramatically skew engagement and network metrics  
**Fix Added:** Bot/automated account detection checklist in critical-checks.md and network analysis probing questions

#### 7. Phase Classification Inconsistency
**Error:** GLM labeled 571 tweets/bin as "Low" but 327 tweets/bin as "Moderate"  
**Impact:** Direct contradiction undermines credibility  
**Fix Added:** Phase classification consistency check requiring documented thresholds

#### 8. Retweet Rate Context Interpretation
**Finding:** Both found 80% retweet rate but interpreted differently:
- GLM: "solidarity signaling" and "low-cost amplification"
- Kimi: "safety-seeking behavior in authoritarian context"  
**Lesson:** High retweet rates have multiple valid interpretations depending on political context  
**Fix Added:** Retweet rate interpretation check requiring context consideration

#### 9. Convergent Findings (What Both Got Right)
- Hybrid network structure (decentralized participation + centralized amplification)
- Same top influencers identified with identical mention counts
- Three temporal phases with declining virality
- Follower count > content features for engagement prediction
- Appropriate non-parametric test choices for skewed data

---

## AgentAcademy Methodology

### How It Works

1. **Enrollment:** Multiple AI models are given the same dataset and research brief
2. **Independent Analysis:** Each agent works alone — no coordination, no peeking
3. **Peer Review:** Agents critique each other's work (cross-review)
4. **Synthesis:** Identify convergent findings (high confidence) vs divergent findings (investigate)
5. **Lesson Extraction:** Errors become new probing questions and checks
6. **Curriculum Update:** Skill pack improves with each cohort

### Why It Works

- **Epistemic diversity:** Different models have different blind spots
- **No deference:** Models don't hesitate to criticize each other
- **Convergence = confidence:** When both models agree, finding is robust
- **Divergence = uncertainty:** Disagreement surfaces genuine ambiguity
- **Continuous improvement:** Each run makes the framework stronger

---

## Checklist Updates Triggered by These Runs

| Lesson | File Updated | Section Added |
|--------|--------------|---------------|
| Effect size classification | critical-checks.md | universal_check_7 (enhanced) |
| Correlation transformation | critical-checks.md | universal_check_7b (new) |
| Sample balance | critical-checks.md | universal_check_4 (enhanced) |
| Bot detection | critical-checks.md | universal_check_6c (new) |
| Phase consistency | critical-checks.md | universal_check_6b (new) |
| Retweet interpretation | critical-checks.md | retweet_rate_interpretation (new) |
| Bot check | PROBING_QUESTIONS.md | Network Analysis Q6 (new) |
| Correlation transform | PROBING_QUESTIONS.md | Sentiment Analysis Q7 (new) |

---

## Future Runs

This document will be updated after each cross-agent red-teaming run. The goal is continuous improvement of CommDAAF's methodological guardrails based on real errors caught in practice.

**To add a lesson:**
1. Run parallel analysis with 2+ models
2. Conduct cross-review
3. Identify errors or insights
4. Document here with: Error → Explanation → Fix
5. Update relevant probing questions or checks

---

*Last updated: 2026-02-17*
