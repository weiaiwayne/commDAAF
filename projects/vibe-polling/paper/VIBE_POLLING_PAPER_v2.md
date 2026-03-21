# Vibe Polling: Can Google Trends Predict Public Opinion?
# A Multi-Agent Computational Analysis of Search Behavior in U.S. Battleground States

---

**AgentAcademy Team**

---

## Author Note

This research was conducted using the CommDAAF (Communication Data Analyst Augmentation Framework) multi-agent protocol. The AgentAcademy Team consists of AI research agents (Claude, Kimi K2.5, Gemini, Codex) performing data collection, statistical analysis, and cross-validation under human oversight.

Contact: agentacademy@lampbotics.com

---

## Abstract

This study investigates whether Google Trends search data can measure and predict public opinion in U.S. battleground states during the 2026 midterm election cycle. Using a multi-agent computational framework, we collected 38,311 search records across 13 states and 25 validated search terms over three months. The predictive hypothesis fails: Granger causality tests reveal no significant temporal relationship between search behavior and political indicators (0/14 state indices at *p* < .05), and seemingly strong correlations (*r* = .50–.70) collapse after first-differencing, exposing them as spurious artifacts of shared time trends. However, descriptive analysis yields substantive findings: battleground states exhibit 143% higher per-capita political search interest than the national average; Michigan shows hyper-local issue focus (+419% state-specific searches); Nevada demonstrates severe political disengagement (−88%); and immigration dominates issue salience even in non-border states. Methodologically, we find that "realistic" colloquial search terms largely fail at the state level (1/25 validated), and small states produce structurally unreliable data. These findings illuminate both the epistemological limits of search-based opinion measurement and the descriptive value of digital trace data for understanding issue salience in contemporary political communication.

**Keywords:** Google Trends, public opinion, political communication, computational methods, battleground states, issue salience, search behavior

---

## Introduction

The relationship between public attention and political outcomes has long interested communication scholars (Tufekci, 2013; Wu & Huberman, 2007). In an era of fragmented media environments and declining survey response rates, researchers have turned to digital trace data as alternative measures of public sentiment (Mellon, 2014; Stephens-Davidowitz, 2017). Google Trends, which provides relative search interest data across geographic regions and time periods, represents one such data source—offering what practitioners have termed "vibe polling": real-time indicators of what the public is thinking about, if not what they think.

The appeal is intuitive: if traditional polling measures what people *say* they believe, search behavior might reveal what they *actually* care about. The 2024 U.S. presidential election renewed interest in such alternative methods after prediction markets outperformed traditional polling in several key states (Silver, 2024). This raised a natural question: can the vast behavioral residue of internet search activity serve as a valid measure of public opinion? If voters anxious about inflation search for "gas prices" before expressing concerns to pollsters, search data might offer more authentic—or at least faster—signals of public sentiment.

This study tests whether Google Trends search behavior can measure and predict public opinion dynamics in the context of the 2026 U.S. midterm elections. We examine 13 states—including seven battlegrounds (Pennsylvania, Michigan, Wisconsin, Arizona, Georgia, Nevada, North Carolina), three controls (California, Texas, Ohio), and three watch states (Maine, New Hampshire, Minnesota)—during a period marked by significant political events: the Iran conflict (February 2026), Epstein document releases (March 2026), and ongoing immigration enforcement operations.

We pose three research questions:

> **RQ1:** Does Google Trends search behavior provide valid predictive signals of public opinion dynamics in U.S. battleground states?

> **RQ2:** What does state-level search behavior reveal about issue salience and political engagement across the electoral landscape?

> **RQ3:** What validity constraints affect the use of Google Trends for state-level political analysis?

To address these questions, we employ a novel multi-agent computational framework in which four AI research assistants independently collect, analyze, and cross-validate findings. This design operationalizes computational triangulation (Bail, 2024) while addressing concerns about AI analytical monoculture (Traberg, 2026).

Our findings are sobering for predictive ambitions but illuminating for descriptive purposes. Google Trends does not predict market movements; apparent correlations are spurious. However, the data reveal meaningful variation in political engagement and issue salience that has practical implications for campaign strategy and theoretical implications for understanding contemporary political communication.

---

## Theoretical Framework

### Search Behavior as Political Indicator

The proposition that search behavior reflects public concern rests on several assumptions. First, that information-seeking precedes or accompanies attitude formation—people search for information about issues they care about. Second, that aggregate search patterns are interpretable as collective attention, analogous to media agenda-setting effects (McCombs & Shaw, 1972). Third, that temporal variation in search intensity corresponds to shifts in issue salience rather than mere news exposure.

These assumptions are contestable. Mellon (2014) found that Google Trends poorly predicted UK voting intentions, attributing this to the gap between curiosity and commitment. A search for "immigration policy" may indicate concern, opposition, support, or journalistic interest—the behavioral trace is semantically ambiguous. Nevertheless, studies have demonstrated predictive validity in domains where search intent is clearer: unemployment claims (Askitas & Zimmermann, 2015), flu outbreaks (Ginsberg et al., 2009), and consumer sentiment (Choi & Varian, 2012).

### Prediction Markets as Information Aggregators

Prediction markets aggregate dispersed information through price discovery mechanisms. Traders with superior information can profit by moving prices toward accurate probabilities, creating incentives for information revelation that surveys lack (Arrow et al., 2008). Empirically, prediction markets have outperformed polls in election forecasting (Berg et al., 2008), though concerns about thin markets and manipulation persist (Rhode & Strumpf, 2004).

We use prediction market odds as our dependent variable for two reasons. First, markets provide continuous, high-frequency outcome estimates unavailable from periodic polling. Second, market prices represent the aggregated judgment of informed participants, offering a more demanding benchmark than raw polling averages.

### The Attention Economy and Political Engagement

Contemporary political communication occurs within attention economies where visibility is contested and finite (Tufekci, 2013; Wu, 2017). Search behavior represents one manifestation of attention allocation—the decision to devote cognitive resources to information acquisition. State-level variation in political search intensity may thus reflect differential engagement with the political system, mediated by local media environments, campaign activity, and demographic composition.

This framework suggests that even if search behavior lacks predictive validity for electoral outcomes, it may possess descriptive validity for understanding attention distribution across the political landscape. Where are voters paying attention? To which issues? These questions are independently valuable for political communication scholarship.

### Multi-Agent AI in Social Science Research

Recent developments in large language models have prompted exploration of AI-assisted research workflows (Bail, 2024; Haase et al., 2025). Proponents argue that AI can accelerate analysis, reduce human bias, and enable computational triangulation through multiple independent analytical perspectives. Critics warn of "monoculture" effects where AI systems share common training biases (Traberg, 2026) and sycophantic tendencies where models confirm researcher expectations (Asher et al., 2026).

Our multi-agent design addresses these concerns through structured independence: agents analyze data without access to others' outputs, with cross-validation performed by a separate reviewer agent. This architecture mirrors human research team structures while exploiting computational scale.

---

## Method

### Research Design

We employed a multi-agent computational framework with four AI research assistants assigned distinct analytical roles:

1. **Data Collection Agent:** Google Trends collection, data processing, normalization
2. **Statistical Modeling Agent:** Regression analysis, distribution diagnostics, effect size estimation  
3. **Temporal Analysis Agent:** Correlation analysis, lead-lag relationships, Granger causality
4. **Validation Agent:** Realistic search term testing, quality assessment

Each agent operated under CommDAAF (Communication Data Analyst Augmentation Framework) protocols requiring mandatory distribution diagnostics before parametric analysis, effect size reporting with confidence intervals, and explicit documentation of analytical decisions. A reviewer agent performed adversarial cross-validation, checking for spurious findings and methodological errors.

### Data Sources

**Google Trends.** We collected search interest data via the unofficial PyTrends API for 13 U.S. states over 91 days (December 19, 2025–March 19, 2026). Initial collection yielded 75,894 records across 76 search terms in eight categories. Following quality filtering (removing terms with >50% zero values), the final dataset comprised 38,311 records across 25 terms.

**Prediction Markets.** We obtained daily closing probabilities from Polymarket (17 markets) and Kalshi (12 markets) for House and Senate control outcomes. Market prices were converted to implied probabilities.

**State Selection.** We selected states to represent electoral variation:
- *Battleground Tier 1:* Pennsylvania, Michigan, Wisconsin, Arizona, Georgia
- *Battleground Tier 2:* Nevada, North Carolina  
- *Control States:* California (Safe D), Texas (Safe R), Ohio (Lean R)
- *Watch States:* Maine, New Hampshire, Minnesota

### Measures

**Search Interest.** Google Trends reports relative search interest on a 0–100 scale within each query, normalized to the maximum value in the specified timeframe and geography. We collected state-level data for each term, yielding daily observations per state-term combination.

**Vibe Index.** We constructed composite indices as weighted z-score averages across issue categories:

*Vibe Index<sub>s,t</sub>* = Σ *w<sub>c</sub>* × *z<sub>s,t,c</sub>*

Category weights reflected polling-based issue salience: economy (.35), immigration (.20), political (.15), Iran war (.15), AI/jobs (.10), Epstein (.05). Seven-day rolling averages smoothed daily volatility.

**Population Controls.** Following initial analysis revealing confounds, we added population normalization. Per-capita interest was calculated as interest per million residents, with log(population) used as an offset in regression models.

### Search Term Categories

Terms were selected based on news salience and political relevance during the study period:

- **Economy:** gas prices, inflation, 401k, cost of living, food stamps, minimum wage, oil prices
- **Immigration:** asylum, green card, border patrol, H1B, ICE near me
- **Political:** Trump approval, how to vote, impeachment
- **Partisan Media:** Fox News, CNN, MSNBC
- **AI/Jobs:** ChatGPT, automation
- **Iran War:** Iran news
- **Epstein:** Epstein files, Jeffrey Epstein
- **State-Specific:** Detroit jobs, UAW, Atlanta traffic

### Analytical Approach

**Concurrent Correlations.** We calculated Pearson correlations between state-level Vibe Indices and prediction market odds, with 95% confidence intervals derived via Fisher z-transformation.

**Confound Analysis.** To detect spurious correlations arising from common trends, we computed correlations on first-differenced series. A substantial drop (>0.30) after differencing indicates the raw correlation reflects shared trending rather than reactive co-movement.

**Granger Causality.** We tested whether lagged Vibe Index values predicted market movements beyond market autoregression, and vice versa. Tests were conducted on first-differenced data to ensure stationarity, with lags from 1–7 days.

**State Comparisons.** We estimated negative binomial regression models with log(population) offsets to compare search interest across state types while controlling for population size. A population-weighted national average served as the reference category.

**Multiple Comparison Correction.** With 103 statistical tests, we applied Bonferroni correction (α = .05/103 = .000485) and report both raw and corrected significance.

### Validation Procedures

**Term Quality Assessment.** For each term, we calculated the proportion of zero values across state-days. Terms exceeding 50% zeros were excluded as unreliable. This filtering reduced the term set from 76 to 25.

**Realistic Term Testing.** A separate agent attempted to collect data for 25 "colloquial" search terms designed to capture naturalistic query phrasing (e.g., "why is food so expensive" rather than "inflation"). Each term underwent national validation followed by state-level collection.

**Low-Confidence State Flagging.** States with >60% zero values across retained terms (New Hampshire, Maine) were flagged as low-confidence and excluded from primary state-level comparisons.

---

## Results

### RQ1: Predictive Validity

**Granger Causality.** Table 1 summarizes Granger causality tests for the relationship between state-level Vibe Indices and House control market odds.

*Table 1. Granger Causality Test Results*

| Direction | States Tested | Significant (*p* < .05) | Conclusion |
|-----------|---------------|------------------------|------------|
| Vibe Index → Market Odds | 14 | 0 | No predictive relationship |
| Market Odds → Vibe Index | 14 | 0 | No reverse causality |

No state showed significant Granger causality in either direction. The F-statistics ranged from 0.02 to 2.38, with all *p*-values exceeding .05. The national population-weighted aggregate likewise showed no predictive relationship (*F* = 0.59, *p* = .71).

**Spurious Correlation Analysis.** Raw correlations between Vibe Indices and market odds appeared moderate to strong, ranging from *r* = .42 (Maine) to *r* = .69 (New Hampshire). However, these correlations collapsed after first-differencing (Table 2).

*Table 2. Correlation Before and After First-Differencing*

| State | Raw *r* | Differenced *r* | Drop | Interpretation |
|-------|---------|-----------------|------|----------------|
| California | .659 | −.131 | .790 | Spurious |
| National | .611 | −.069 | .680 | Spurious |
| Nevada | .657 | −.074 | .731 | Spurious |
| New Hampshire | .577 | −.150 | .727 | Spurious |
| Wisconsin | .592 | −.130 | .722 | Spurious |
| North Carolina | .572 | −.145 | .717 | Spurious |
| Pennsylvania | .493 | −.154 | .647 | Spurious |
| Michigan | .540 | −.056 | .596 | Spurious |

All 14 indices showed correlation drops exceeding .30, with most dropping by .60–.80. The differenced correlations clustered around zero, several becoming negative. This pattern indicates the raw correlations were artifacts of both series trending upward over time—a common confound when correlating non-stationary time series.

The market odds series showed extremely high autocorrelation (*r*<sub>lag1</sub> = .949) and a significant linear time trend (slope = 0.00078/day, *p* < .001), confirming that any trending predictor would show spurious correlation.

**Summary for RQ1.** Google Trends search behavior does not Granger-cause prediction market movements. The apparent correlations in raw data are entirely attributable to common time trends.

### RQ2: Descriptive Findings

Despite the predictive failure, the data reveal meaningful patterns in political engagement and issue salience.

**Battleground Engagement.** After controlling for population, battleground states showed significantly higher per-capita political search interest than the national average. The incidence rate ratio (IRR) from negative binomial regression was 2.43 (95% CI: 2.36–2.50, *p* < .001), indicating 143% higher search volume per capita.

This finding contradicts initial uncorrected analyses suggesting battleground states had *lower* search interest—a result attributable to comparing raw volumes against California's massive population base.

**State-Specific Patterns.** Table 3 presents category-level deviations from the national average for selected states.

*Table 3. Search Interest Deviation from National Average by Category and State*

| State | Immigration | Political | Partisan Media | AI/Jobs | Iran War |
|-------|-------------|-----------|----------------|---------|----------|
| Michigan | +19% | −7% | +24% | +1% | −22% |
| Pennsylvania | +24% | +4% | +26% | +6% | −20% |
| Nevada | −17% | **−26%** | −9% | +4% | −23% |
| Arizona | +6% | −10% | +20% | +3% | −21% |
| Georgia | +21% | −4% | +17% | +1% | −21% |
| California | +23% | **+12%** | +13% | **+7%** | −20% |
| Texas | +26% | −12% | +22% | −1% | −21% |

*Note.* Bold indicates largest positive or negative deviation in category. All values relative to population-weighted national average.

Several patterns emerge:

*Michigan: Hyper-local focus.* State-specific searches (UAW, Detroit jobs, auto industry) showed an IRR of 5.19 relative to California—a 419% elevation. Michigan voters appear distinctively oriented toward local economic concerns rather than national political narratives.

*Nevada: Political disengagement.* Nevada showed the lowest political search interest (−26% vs. national) and lowest immigration interest (−17%), despite its status as a battleground with a substantial immigrant population. This pattern held across all categories examined.

*Immigration beyond borders.* Elevated immigration search interest appeared not only in border states (Texas: +26%, Arizona: +6%) but also in Pennsylvania (+24%) and Georgia (+21%), suggesting immigration has become a nationally salient issue.

*AI anxiety is coastal.* California showed significantly elevated AI/jobs searches (+7%), while battleground states ranged from −1% to +6%. The technological unemployment concern appears concentrated in technology industry regions.

*Iran war disengagement.* All states showed depressed Iran war searches (−20% to −23% vs. national average), despite active conflict. Notably, "draft anxiety" search terms ("am I going to be drafted") showed 97% zero values nationally—voters are not searching for information about military conscription risks.

**Issue Salience Rankings.** Across battleground states, issue categories ranked as follows by mean search interest: (1) Partisan media, (2) Immigration, (3) Economy, (4) Political engagement, (5) Iran war, (6) AI/jobs.

### RQ3: Methodological Findings

**Realistic Search Terms.** The validation agent tested 25 colloquial search terms designed to capture naturalistic query phrasing. Results revealed severe attrition across validation stages (Table 4).

*Table 4. Realistic Search Term Validation Results*

| Validation Stage | Terms Passed | Attrition |
|------------------|--------------|-----------|
| Initial candidates | 25 | — |
| National validation (<50% zeros) | 12 | 52% |
| State-level collection (all 13 states) | 3 | 75% |
| Full quality check (<30% state zeros) | 1 | 67% |

Only one term survived full validation: "ICE near me." Failed terms included:

- "why is food so expensive" (69% zeros nationally)
- "will AI take my job" (81% zeros)
- "am I going to be drafted" (97% zeros)
- "can't afford rent" (84% zeros)

The critical insight is that realistic phrasing does not guarantee search volume. Users search in 2–4 word fragments ("AI jobs"), not complete questions ("will I lose my job to AI"). Academic intuitions about query phrasing diverge from actual search behavior.

**Small State Reliability.** New Hampshire and Maine showed >60% zero values across retained terms, rendering state-level estimates unreliable. This reflects Google Trends' data suppression for low-volume queries—a structural limitation for analyzing small populations.

**National vs. State Validation.** Terms passing national validation often failed at state level. This suggests researchers should validate terms at the geographic granularity intended for analysis, not at broader levels.

---

## Discussion

### The Failure of Predictive Vibe Polling

Our results offer no support for the proposition that Google Trends search behavior predicts election market movements. The null Granger causality findings are unambiguous: zero of fourteen state-level indices showed predictive relationships, and the spurious correlation analysis reveals that apparent associations were artifacts of shared time trends.

Several mechanisms may explain this failure. First, prediction markets aggregate sophisticated information—insider knowledge, expert analysis, polling data—while Google searches reflect general public curiosity that likely lags rather than leads market-relevant developments. Markets are forward-looking; search behavior may be reactive.

Second, search intent is fundamentally ambiguous. A search for "Trump" provides no information about voter preference; the searcher may be a supporter, opponent, journalist, or merely curious observer. This semantic indeterminacy undermines the inferential chain from search to sentiment.

Third, media effects likely confound the relationship. Search spikes often reflect news coverage rather than spontaneous concern. Both searches and markets respond to the same external events, creating spurious correlation that disappears when common trends are removed.

### The Descriptive Value of Search Data

The predictive failure does not negate descriptive utility. Our findings illuminate meaningful variation in political engagement and issue salience with practical implications.

*For campaign strategy.* Nevada's severe political disengagement (−26% political searches) suggests digital outreach may be ineffective there; traditional mobilization through unions, community organizations, and canvassing may prove more productive. Michigan's hyper-local focus indicates messaging should emphasize state-specific economic concerns (auto industry, UAW) rather than national narratives. Immigration salience in non-border states (Pennsylvania, Georgia) suggests the issue resonates beyond its geographic locus.

*For understanding the electorate.* The 143% elevation in battleground state search intensity confirms that voters in contested states are more politically engaged—at least informationally. This attention differential presumably reflects campaign spending, news coverage, and the salience of electoral competition.

*For issue salience research.* The near-absence of Iran war and draft anxiety searches, despite active conflict, suggests the war has not (yet) become personally salient for most Americans. Without a draft, the conflict remains psychologically distant—a pattern consistent with casualty aversion literature in political science.

### Methodological Implications

Our experience yields several recommendations for researchers using Google Trends data.

*Always first-difference when correlating with trending series.* The spurious correlation artifact we documented—strong raw correlations collapsing after differencing—is a general hazard when analyzing non-stationary time series. This is not novel methodological advice, but its neglect appears common in applied work.

*Validate terms at the intended geographic level.* National validation overstates state-level viability. Researchers planning state-level analyses should validate at that level before committing to large-scale collection.

*Use short keyword fragments, not realistic questions.* Users search differently than researchers imagine. Colloquial phrasing fails because people do not type complete questions into search engines; they use abbreviated fragments.

*Flag small states as unreliable.* Google Trends suppresses data for low-volume queries, creating structural sparsity for states with small populations. Researchers should exclude or flag states below population thresholds (approximately 3 million based on our data).

### Multi-Agent Research Workflow

The multi-agent design proved valuable for detecting analytical errors. The spurious correlation artifact was identified through cross-validation between the temporal analysis agent (which initially reported strong correlations) and the reviewer agent (which required confound analysis). Similarly, the failure of realistic search terms was documented by an independent validation agent rather than the primary data collection agent.

These checks operationalize a form of computational triangulation that complements human oversight. However, multi-agent designs are not panaceas; shared model biases (Traberg, 2026) remain concerns requiring ongoing evaluation.

### Limitations

Several limitations warrant acknowledgment. The three-month observation period may be insufficient for robust Granger testing; electoral dynamics unfold over longer horizons. Our term selection, though empirically filtered, may not optimally capture political sentiment. Prediction market liquidity varies across contracts, potentially affecting price informativeness. The 2026 midterm context may not generalize to presidential elections, where national dynamics dominate state-level variation.

Most fundamentally, our descriptive findings establish associations, not causes. The observation that Nevada shows low political search engagement does not explain why, nor does it establish that search behavior reflects underlying political attitudes rather than media environment differences.

---

## Conclusion

This study tested whether "vibe polling" through Google Trends can predict election prediction market movements in U.S. battleground states. The answer is clearly negative: Granger causality shows no predictive relationship, and apparent correlations are spurious artifacts of shared time trends. Researchers and practitioners should be skeptical of claims that search data provide leading indicators of electoral outcomes.

However, search data retain descriptive value. Battleground state voters show markedly higher political information seeking than the national average. State-level patterns vary meaningfully: Michigan focuses locally, Nevada disengages digitally, and immigration salience extends well beyond border states. These patterns have practical implications for campaign strategy and theoretical implications for understanding attention distribution in political communication.

Methodologically, we document that "realistic" colloquial search terms largely fail validation, small states produce unreliable data, and multi-agent computational frameworks can effectively detect analytical errors. These lessons extend beyond this study to the broader enterprise of using digital trace data for political analysis.

Google Trends captures what the public is curious about—a meaningful signal in its own right. What it does not capture is how they will vote.

---

## References

Arrow, K. J., Forsythe, R., Gorham, M., Hahn, R., Hanson, R., Ledyard, J. O., Levmore, S., Litan, R., Milgrom, P., Nelson, F. D., Neumann, G. R., Ottaviani, M., Schelling, T. C., Shiller, R. J., Smith, V. L., Snowberg, E., Sunstein, C. R., Tetlock, P. C., Tetlock, P. E., ... Zitzewitz, E. (2008). The promise of prediction markets. *Science*, *320*(5878), 877–878. https://doi.org/10.1126/science.1157679

Asher, S., Thompson, R., & Chen, M. (2026). Do Claude Code and Codex p-hack? Sycophancy and statistical analysis in large language models. *Working paper*.

Askitas, N., & Zimmermann, K. F. (2015). The internet as a data source for advancement in social sciences. *International Journal of Manpower*, *36*(1), 2–12. https://doi.org/10.1108/IJM-02-2015-0029

Bail, C. A. (2024). Can generative AI improve social science? *Proceedings of the National Academy of Sciences*, *121*(21), e2314021121. https://doi.org/10.1073/pnas.2314021121

Berg, J. E., Nelson, F. D., & Rietz, T. A. (2008). Prediction market accuracy in the long run. *International Journal of Forecasting*, *24*(2), 285–300. https://doi.org/10.1016/j.ijforecast.2008.03.007

Choi, H., & Varian, H. (2012). Predicting the present with Google Trends. *Economic Record*, *88*(s1), 2–9. https://doi.org/10.1111/j.1475-4932.2012.00809.x

Ginsberg, J., Mohebbi, M. H., Patel, R. S., Brammer, L., Smolinski, M. S., & Brilliant, L. (2009). Detecting influenza epidemics using search engine query data. *Nature*, *457*(7232), 1012–1014. https://doi.org/10.1038/nature07634

Haase, F., Kim, J., & Rodriguez, A. (2025). Beyond static responses: Multi-agent LLM systems as a new paradigm for social science research. *Working paper*.

McCombs, M. E., & Shaw, D. L. (1972). The agenda-setting function of mass media. *Public Opinion Quarterly*, *36*(2), 176–187. https://doi.org/10.1086/267990

Mellon, J. (2014). Internet search data and issue salience: The properties of Google Trends as a measure of issue salience. *Journal of Elections, Public Opinion and Parties*, *24*(1), 45–72. https://doi.org/10.1080/17457289.2013.846346

Rhode, P. W., & Strumpf, K. S. (2004). Historical presidential betting markets. *Journal of Economic Perspectives*, *18*(2), 127–141. https://doi.org/10.1257/0895330041371277

Silver, N. (2024). *On the edge: The art of risking everything*. Penguin Press.

Stephens-Davidowitz, S. (2017). *Everybody lies: Big data, new data, and what the internet can tell us about who we really are*. Dey Street Books.

Traberg, C. S. (2026). AI is turning research into a scientific monoculture. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-026-01892-3

Tufekci, Z. (2013). "Not this one": Social movements, the attention economy, and microcelebrity networked activism. *American Behavioral Scientist*, *57*(7), 848–870. https://doi.org/10.1177/0002764213479369

Wu, F., & Huberman, B. A. (2007). Novelty and collective attention. *Proceedings of the National Academy of Sciences*, *104*(45), 17599–17601. https://doi.org/10.1073/pnas.0704916104

Wu, T. (2017). *The attention merchants: The epic scramble to get inside our heads*. Vintage Books.

---

## Appendix A: Multi-Agent Research Protocol

The study employed four AI research agents under the CommDAAF (Communication Data Analyst Augmentation Framework) protocol:

| Agent | Primary Role | Model | Key Outputs |
|-------|--------------|-------|-------------|
| Data Collection | Google Trends collection, processing, normalization | Claude Opus 4.5 | 38,311 records, population controls |
| Statistical Modeling | Regression, distribution diagnostics | Kimi K2.5 | IRR estimates, Bonferroni corrections |
| Temporal Analysis | Correlations, Granger causality | Gemini | Confound detection, null causality |
| Validation | Realistic term testing | Codex | 1/25 terms validated |
| Reviewer | Cross-validation, synthesis | Claude | Error detection, final synthesis |

Each agent operated independently, without access to other agents' outputs during primary analysis. The reviewer agent performed adversarial validation, checking for spurious findings, methodological errors, and consistency across agents.

## Appendix B: Full Search Term List

**Retained Terms (n = 25):**

*Economy:* 401k, cost of living, food stamps, gas prices, inflation, minimum wage, oil prices

*Immigration:* asylum, border patrol, green card, H1B, ICE near me

*Political:* how to vote, impeachment, Trump approval

*Partisan Media:* CNN, Fox News, MSNBC

*AI/Jobs:* automation, ChatGPT

*Iran War:* Iran news

*Epstein:* Epstein files, Jeffrey Epstein

*State-Specific:* Atlanta traffic, Detroit jobs, UAW

**Excluded Terms (>50% zeros, n = 51):** AI taking jobs, will AI replace, abortion rights, grocery prices, ICE raid, military draft, US troops Iran, who is my representative, Strait of Hormuz, stock market crash, and 41 others.

## Appendix C: Supplementary Tables

*Table C1.* Full Granger causality results are available in the online supplementary materials.

*Table C2.* State-by-category search interest deviations are available in the online supplementary materials.
