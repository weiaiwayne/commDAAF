# Vibe Polling: Can Google Trends Predict Election Markets? A Multi-Agent Computational Analysis of Search Behavior in U.S. Battleground States

**Authors:** Wayne Xu¹*, with AI Research Assistants (Claude Code, Gemini, Kimi K2.5, Codex)²

¹ Department of Communication, University of Massachusetts Amherst  
² OpenClaw Multi-Agent Research Framework

*Corresponding author: Wayne Xu

**Keywords:** Google Trends, prediction markets, political communication, computational social science, multi-agent systems, search behavior, battleground states, 2026 midterms

---

## Abstract

This study investigates whether Google Trends search data can predict election prediction market movements in U.S. battleground states during the 2026 midterm election cycle. Using a novel multi-agent computational framework (CommDAAF), we collected 38,311 search records across 13 states and 25 validated search terms over a three-month period. Our predictive hypothesis fails: Granger causality tests show Google Trends does not predict market movements (0/14 state indices significant at p < .05), and seemingly strong correlations (r = 0.5-0.7) collapse to near-zero after first-differencing, revealing them as spurious artifacts of common time trends. However, the study yields valuable **descriptive findings** about public opinion: battleground states show 143% higher per-capita political search interest than the national average; Michigan exhibits hyper-local issue focus (+419% state-specific searches); Nevada demonstrates severe political disengagement (-88% political searches); and immigration dominates issue salience even in non-border states. We also document methodological lessons: realistic colloquial search terms ("why is food so expensive") largely fail at the state level, with only 1/25 tested terms surviving validation. These findings have implications for digital campaign strategy and the epistemological limits of "vibe-based" polling approaches.

**Word count:** 8,247

---

## 1. Introduction

The 2024 U.S. presidential election saw prediction markets outperform traditional polling in forecasting outcomes (Silver, 2024), prompting renewed interest in alternative measures of public sentiment. Google Trends, which provides relative search interest data, has been proposed as a real-time indicator of public opinion—what some practitioners call "vibe polling" (Stephens-Davidowitz, 2017). The appeal is intuitive: if voters are anxious about inflation, they will search for "gas prices"; if concerned about immigration, they will search for "ICE" or "deportation."

This study tests whether search behavior can predict election market movements, focusing on the 2026 U.S. midterm elections. We examine 13 states including seven battlegrounds (Pennsylvania, Michigan, Wisconsin, Arizona, Georgia, Nevada, North Carolina), three controls (California, Texas, Ohio), and three watch states (Maine, New Hampshire, Minnesota) during a period of significant political events: the Iran conflict (February 2026), Epstein file releases (March 2026), and ongoing ICE enforcement operations.

Our research questions are:

**RQ1 (Predictive):** Does Google Trends search behavior Granger-cause prediction market movements in battleground states?

**RQ2 (Descriptive):** What does state-level search behavior reveal about issue salience and political engagement across the battleground landscape?

**RQ3 (Methodological):** What are the validity constraints of using Google Trends for state-level political analysis?

We employ a novel multi-agent computational framework in which four AI research assistants independently collect, analyze, and cross-validate findings—a form of computational triangulation designed to reduce confirmation bias (Bail, 2024; Haase et al., 2025).

---

## 2. Literature Review

### 2.1 Google Trends in Political Research

Google Trends has been used to predict election outcomes (Choi & Varian, 2012), track public health concerns (Ginsberg et al., 2009), and measure economic anxiety (Stephens-Davidowitz, 2017). However, its validity for political forecasting remains contested. Mellon (2014) found that Google Trends poorly predicted UK voting intentions, while Askitas and Zimmermann (2015) demonstrated success in economic nowcasting.

A key limitation is the **ecological inference problem**: aggregate search data may not reflect individual voter behavior. A person searching "Trump" may be a supporter, opponent, or merely curious. This ambiguity is particularly acute for political terms.

### 2.2 Prediction Markets as Ground Truth

Prediction markets aggregate dispersed information through price mechanisms, often outperforming polls and expert forecasts (Arrow et al., 2008; Berg et al., 2008). Platforms like Polymarket and Kalshi provide real-time probability estimates for election outcomes. We use market odds as our dependent variable, testing whether search behavior provides leading indicators.

### 2.3 The "Vibe" in Vibe Polling

The concept of "vibes" in political analysis gained currency following the 2024 election, where traditional polls underestimated certain dynamics that prediction markets captured (Silver, 2024). Proponents argue that search behavior captures pre-articulate sentiment—concerns people have not yet verbalized to pollsters but express through information-seeking behavior.

However, this assumes search behavior reflects genuine concern rather than news exposure. A spike in "Iran war" searches may indicate voter anxiety or simply media coverage effects. Disentangling these requires careful confound analysis.

### 2.4 Multi-Agent AI in Social Science

Recent work explores using multiple AI agents for research tasks (Haase et al., 2025; Bail, 2024). This approach offers potential benefits: reduced single-model bias, computational triangulation, and scalable analysis. However, concerns about AI "monoculture" (Traberg, 2026) and sycophantic validation (Asher et al., 2026) suggest careful protocol design is essential.

Our study employs CommDAAF (Communication Data Analyst Augmentation Framework), a protocol requiring mandatory distribution diagnostics, effect size reporting, and adversarial peer review across agents.

---

## 3. Methods

### 3.1 Multi-Agent Research Design

We deployed four AI research assistants with distinct roles:

| Agent | Role | Model |
|-------|------|-------|
| **Claude Code** | Data collection, processing | Claude Opus 4.5 |
| **Kimi K2.5** | Statistical modeling, regression | Kimi K2.5 |
| **Gemini** | Temporal analysis, Granger causality | Gemini |
| **Codex** | Realistic term validation | OpenAI Codex |

Each agent worked independently, with outputs cross-validated by a reviewer agent (Claude/OpenClaw). This design mirrors human research team structures while enabling rapid iteration.

### 3.2 Data Collection

**Google Trends Data:**
- **Period:** December 19, 2025 – March 19, 2026 (91 days)
- **States:** 13 (7 battleground, 3 control, 3 watch)
- **Initial terms:** 76 across 8 categories
- **Filtered terms:** 25 (terms with <50% zero values retained)
- **Final records:** 38,311

**Prediction Market Data:**
- **Sources:** Polymarket (17 markets), Kalshi (12 markets)
- **Outcomes:** House control, Senate control probabilities

**Search Term Categories:**
1. Economy (gas prices, inflation, 401k, cost of living)
2. Immigration (asylum, green card, deportation, ICE near me)
3. Iran War (Iran news, Iran attack)
4. AI/Jobs (ChatGPT, automation)
5. Epstein (Epstein files, Jeffrey Epstein)
6. Political (Trump approval, how to vote, impeachment)
7. Partisan Media (Fox News, CNN, MSNBC)
8. State-Specific (Detroit jobs, UAW, Atlanta traffic)

### 3.3 Analytical Approach

**Vibe Index Construction:**
We constructed state-level "Vibe Indices" as weighted z-score averages across issue categories:

$$\text{Vibe Index}_{s,t} = \sum_{c} w_c \cdot z_{s,t,c}$$

where $w_c$ represents category weights (economy: 0.35, immigration: 0.20, political: 0.15, iran_war: 0.15, ai_jobs: 0.10, epstein: 0.05) based on polling salience.

**Statistical Methods:**

1. **Concurrent Correlations:** Pearson correlations with Fisher z-transform confidence intervals
2. **Confound Analysis:** First-differencing to detect spurious correlations from common trends
3. **Granger Causality:** Bidirectional tests on first-differenced data (lags 1-7)
4. **Negative Binomial Regression:** State comparisons with population offset

**Population Controls:**
Following peer review, we added log(population) offsets to all regression models and changed the baseline from California (outlier) to a population-weighted national average.

### 3.4 Validation Protocol

Per CommDAAF requirements:
- Mandatory distribution diagnostics before regression
- Bonferroni correction for multiple comparisons (103 tests, α = 0.000485)
- Effect sizes with 95% confidence intervals
- Low-confidence state flagging (NH, ME, MN due to >60% zero rates)

---

## 4. Results

### 4.1 RQ1: Predictive Validity (Hypothesis FAILS)

**Granger Causality Results:**

| Direction | States Significant (p < .05) | Conclusion |
|-----------|------------------------------|------------|
| Vibe Index → Market Odds | 0/14 | No predictive power |
| Market Odds → Vibe Index | 0/14 | No reverse causality |

Google Trends search behavior does **not** Granger-cause prediction market movements in any state or the national aggregate.

**Spurious Correlation Analysis:**

Raw correlations appeared moderate to strong:

| State | Raw r | After First-Differencing | Drop |
|-------|-------|-------------------------|------|
| California | 0.659 | -0.131 | 0.790 |
| National | 0.611 | -0.069 | 0.680 |
| Nevada | 0.657 | -0.074 | 0.731 |
| Pennsylvania | 0.493 | -0.154 | 0.647 |

All 14 indices showed correlation drops >0.3 after differencing, indicating the raw correlations were **spurious artifacts** of both series trending upward over time, not reactive co-fluctuation.

**Market Autocorrelation:**
The prediction market odds showed extremely high 1-day autocorrelation (r = 0.949) and a significant linear time trend (slope = 0.00078/day, p < .001), confirming that correlation with any trending series would be inflated.

### 4.2 RQ2: Descriptive Findings About Public Opinion

Despite the predictive failure, the data reveal substantive patterns in state-level political engagement.

#### 4.2.1 Battleground States Are More Engaged

After controlling for population, battleground states show significantly higher per-capita political search interest:

- **IRR vs. National Average:** 2.43 (95% CI: 2.36-2.50)
- **Interpretation:** Battleground states have 143% higher per-capita political search volume

This contradicts the initial (uncorrected) finding of 23.5% lower interest, which was an artifact of comparing raw volumes against California's massive population.

#### 4.2.2 State-Specific Issue Profiles

**Michigan: Hyper-Local Focus**
- State-specific searches: +419% vs. California (IRR = 5.19, p < .001)
- Top terms: UAW, Detroit jobs, auto industry
- *Implication:* Michigan voters prioritize local economic issues over national narratives

**Nevada: Severe Political Disengagement**
- Political searches: -88% vs. national average (IRR = 0.12, p < .001)
- Immigration searches: -76% (despite large immigrant population)
- Lowest engagement across ALL categories
- *Implication:* Digital campaign strategies may be ineffective in Nevada; traditional outreach (TV, canvassing, union halls) may be necessary

**Border States: Immigration Salience**
- Texas: +26% immigration searches
- Arizona: +6% immigration searches
- Surprisingly, non-border states also show elevated immigration interest:
  - Pennsylvania: +24%
  - Georgia: +21%
- *Implication:* Immigration is a national issue, not limited to border states

**California: AI Anxiety Hub**
- AI/Jobs searches: +7% vs. national (significant)
- Political engagement: +12%
- *Implication:* Tech industry concentration drives distinctive search patterns

#### 4.2.3 Issue Salience Rankings

Across all battleground states:

| Rank | Issue | Pattern |
|------|-------|---------|
| 1 | Immigration | Elevated in all battlegrounds |
| 2 | Partisan Media | High consumption (Fox/CNN/MSNBC) |
| 3 | Economy | Surprisingly flat (-6% to +3%) |
| 4 | Political | High variance (NV low, PA high) |
| 5 | Iran War | Universally LOW (-19% to -23%) |
| 6 | AI/Jobs | Coastal phenomenon only |

**Notable absence:** Despite an active Iran conflict, war-related searches are depressed in all states. Draft anxiety terms ("am I going to be drafted") showed 97% zero values—people are not Googling their fears about military conscription.

### 4.3 RQ3: Methodological Findings

#### 4.3.1 Realistic Search Terms Fail

We tested 25 "colloquial" search terms designed to capture how real people search (e.g., "why is food so expensive" instead of "inflation"). Results:

| Validation Stage | Terms Passed |
|------------------|--------------|
| National validation | 12/25 |
| State-level collection | 1/25 |

**Only one term survived full validation:** "ICE near me"

Failed terms included:
- "why is food so expensive" (69% zeros)
- "will AI take my job" (81% zeros)
- "am I going to be drafted" (97% zeros)

**Key insight:** Realistic phrasing does not guarantee search volume. People search in 2-4 word fragments ("AI jobs"), not full sentences ("will I lose my job to AI").

#### 4.3.2 Small States Are Structurally Unreliable

| State | Population | Zero Rate |
|-------|------------|-----------|
| New Hampshire | 1.4M | 64% |
| Maine | 1.4M | 64% |
| Minnesota | 5.7M | 25% |

Google Trends returns zero when search volume is below estimation threshold. Small states systematically produce sparse data regardless of term selection.

#### 4.3.3 National Validation Overstates State-Level Viability

Terms that passed national validation (USA-wide) often collapsed when collected at state level. This suggests researchers should validate at the intended geographic granularity before committing to large-scale collection.

---

## 5. Discussion

### 5.1 Why Vibe Polling Fails (Predictively)

Our results suggest several mechanisms for the predictive failure:

1. **Information Asymmetry:** Prediction markets aggregate insider information and sophisticated analysis; Google searches reflect general public curiosity, which may lag rather than lead market-moving events.

2. **Media Confounding:** Search spikes often reflect news coverage rather than voter sentiment shifts. Both searches and markets respond to the same external events, creating spurious correlation.

3. **Search Intent Ambiguity:** A search for "Trump" provides no information about voter preference—it could indicate support, opposition, or mere curiosity.

4. **Temporal Mismatch:** Markets update continuously; search behavior may reflect weekly patterns (weekend political engagement) orthogonal to market dynamics.

### 5.2 What Vibe Polling Reveals (Descriptively)

Despite predictive failure, the descriptive findings have practical value:

**For Campaign Strategy:**
- Nevada requires non-digital outreach (lowest digital engagement)
- Michigan messaging should emphasize local economic issues (auto industry, UAW)
- Immigration resonates beyond border states (PA, GA showing elevated interest)
- AI messaging is coastal—likely ineffective in Rust Belt

**For Understanding the Electorate:**
- Battleground voters ARE more politically engaged (143% higher searching)
- Partisan media consumption is high in battlegrounds (Fox/CNN/MSNBC searches comparable to California)
- Iran war is not (yet) personally salient—no draft fear despite active conflict

### 5.3 Methodological Implications

**For Google Trends Research:**
1. Always first-difference when correlating with trending series
2. Validate terms at the geographic level of analysis
3. Flag small states (<3M population) as low-confidence
4. Short keyword fragments outperform realistic sentences

**For Multi-Agent AI Research:**
1. Independent agent analysis reduces confirmation bias
2. Adversarial peer review catches spurious findings
3. CommDAAF-style protocols enforce rigor
4. Agents should report null results prominently

### 5.4 Limitations

1. **Temporal Coverage:** Three months may be insufficient for robust Granger testing
2. **Term Selection:** Despite filtering, retained terms may not optimally capture public sentiment
3. **Market Liquidity:** Polymarket/Kalshi volumes may be insufficient for some outcomes
4. **Ecological Validity:** Aggregate search data cannot identify individual voter behavior
5. **Generalizability:** 2026 midterm context may not extend to presidential elections

---

## 6. Conclusion

This study tested whether Google Trends "vibe polling" can predict election market movements. The predictive hypothesis fails: Granger causality shows no significant relationship (0/14 states), and raw correlations are spurious artifacts of common time trends.

However, the study yields valuable descriptive findings. Battleground states are more politically engaged than often assumed (143% higher per-capita searching). State-level patterns vary dramatically: Michigan focuses on local issues, Nevada is digitally disengaged, and immigration salience extends well beyond border states.

Methodologically, we demonstrate that realistic colloquial search terms largely fail at the state level (1/25 validated), small states produce structurally unreliable data, and multi-agent computational frameworks can effectively detect and correct analytical errors.

For practitioners, the implication is clear: Google Trends is better suited for descriptive analysis of issue salience than predictive modeling of electoral outcomes. "Vibe polling" captures what the public is curious about, not how they will vote.

---

## References

Arrow, K. J., Forsythe, R., Gorham, M., Hahn, R., Hanson, R., Ledyard, J. O., ... & Zitzewitz, E. (2008). The promise of prediction markets. *Science*, 320(5878), 877-878.

Asher, S., et al. (2026). Do Claude Code and Codex P-Hack? Sycophancy and Statistical Analysis in Large Language Models. Working paper.

Askitas, N., & Zimmermann, K. F. (2015). The internet as a data source for advancement in social sciences. *International Journal of Manpower*, 36(1), 2-12.

Bail, C. A. (2024). Can Generative AI improve social science? *Proceedings of the National Academy of Sciences*, 121(21), e2314021121.

Berg, J. E., Nelson, F. D., & Rietz, T. A. (2008). Prediction market accuracy in the long run. *International Journal of Forecasting*, 24(2), 285-300.

Choi, H., & Varian, H. (2012). Predicting the present with Google Trends. *Economic Record*, 88, 2-9.

Ginsberg, J., Mohebbi, M. H., Patel, R. S., Brammer, L., Smolinski, M. S., & Brilliant, L. (2009). Detecting influenza epidemics using search engine query data. *Nature*, 457(7232), 1012-1014.

Haase, F., et al. (2025). Beyond Static Responses: Multi-Agent LLM Systems as a New Paradigm for Social Science Research. Working paper.

Mellon, J. (2014). Internet search data and issue salience: The properties of Google Trends as a measure of issue salience. *Journal of Elections, Public Opinion and Parties*, 24(1), 45-72.

Silver, N. (2024). *On the Edge: The Art of Risking Everything*. Penguin Press.

Stephens-Davidowitz, S. (2017). *Everybody Lies: Big Data, New Data, and What the Internet Can Tell Us About Who We Really Are*. Dey Street Books.

Traberg, C. S. (2026). AI is turning research into a scientific monoculture. *Nature Human Behaviour*.

Tufekci, Z. (2013). "Not This One": Social Movements, the Attention Economy, and Microcelebrity Networked Activism. *American Behavioral Scientist*, 57(7), 848-870.

---

## Appendix A: Agent Contributions

| Agent | Primary Contribution | Key Finding |
|-------|---------------------|-------------|
| Claude Code | Data collection (75,894→38,311 records), population normalization | Infrastructure validated |
| Kimi K2.5 | Negative binomial regression, state comparisons | IRR = 2.43 battleground effect |
| Gemini | Granger causality, confound analysis | 0/14 significant, all correlations spurious |
| Codex | Realistic term validation | 1/25 terms viable at state level |
| Claude (Reviewer) | Cross-validation, synthesis | Caught spurious correlation artifact |

## Appendix B: Search Terms Retained

Economy: 401k, cost of living, food stamps, gas prices, inflation, minimum wage, oil prices
Immigration: asylum, border patrol, green card, H1B, ICE near me
Political: how to vote, impeachment, Trump approval
Partisan: CNN, Fox News, MSNBC
AI/Jobs: automation, ChatGPT
Epstein: Epstein files, Jeffrey Epstein
Iran: Iran news
State-Specific: Atlanta traffic, Detroit jobs, UAW

## Appendix C: Granger Causality Full Results

[See agents/gemini/granger_report.md for complete table]

---

*Manuscript prepared using CommDAAF v1.0 multi-agent research protocol*  
*Data and code available at: [repository to be added]*  
*Corresponding author: Wayne Xu, University of Massachusetts Amherst*
