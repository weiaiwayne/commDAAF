# Final Study Report — VibePoll-2026 (Gemini Run)

**Framework:** CommDAAF v1.0  
**Validation Tier:** 🟢 EXPLORATORY  
**Date:** 2026-03-20  

## Executive Summary
This study analyzed the correlation between search-based "Vibe Indices" and prediction market odds for the 2026 U.S. Midterm Elections. Following critical peer review, the analysis was restricted to high-signal search terms and expanded to include a population-weighted national index and bidirectional causality testing. 

The core predictive hypothesis of this study **largely FAILS validation at the state level but shows limited viability nationally**: Google Trends search behavior is generally a poor predictor of prediction market movements. While raw correlations appear moderate (e.g., r=0.58 in CA, r=0.50 National), **confound analysis** reveals that for the majority of states, these are overwhelmingly driven by common time trends rather than reactive co-fluctuation. 

However, after applying a 7-day smoothing filter to remove high-frequency noise, a more nuanced picture emerges:
- **National Signal:** The Population-Weighted National Vibe Index maintains a moderate true correlation (r=0.28) even after first-differencing, indicating genuine co-fluctuation with market odds.
- **Granger Causality:** Predictive causality remains very weak. Vibe Index Granger-caused market odds in only 2 of 14 series (AZ, MI). Interestingly, the reverse direction (Markets leading Trends) was significant in 4 series (AZ, GA, PA, and the National aggregate), suggesting that search volume is more often a *reaction* to political news and market shifts than a leading indicator of them.

However, while the predictive value of Google Trends is rejected, the temporal and geographic search patterns yield highly valuable **descriptive findings** about public opinion.

## Descriptive Findings: What Google Trends Reveals About Public Opinion

While spurious correlations negate predictive modeling, temporal search patterns still reveal genuine geographic variations in voter anxiety and issue salience.

### 1. Battleground Voter Engagement
Battleground states are highly engaged digitally. They exhibit **143% higher per-capita political search interest** compared to the national average. 
- **Campaign Implication:** Digital outreach and search-based advertising remain highly viable strategies in key battleground states due to elevated baseline engagement.

### 2. State-Specific Patterns
- **Michigan is Hyper-Local:** Michigan exhibits +419% higher search interest for state-specific and local economic terms (UAW, auto industry, Detroit jobs). Voters care deeply about LOCAL economic issues, rather than national abstract narratives.
  - **Campaign Implication:** Messaging in Michigan must be heavily localized to auto and union-related issues rather than generic macroeconomic talking points.
- **Nevada is Severely Disengaged:** Nevada shows the lowest engagement across all categories, including an 87.9% drop in political searches vs the national average and a 76% drop in immigration searches (despite a large immigrant population). 
  - **Campaign Implication:** Digital-first campaigns will likely fail in Nevada. Campaigns must rely heavily on non-digital outreach (TV, canvassing, union mobilization).

### 3. Issue Salience
- **Immigration Dominates (Even in Non-Border States):** Immigration is highly salient everywhere. Pennsylvania (+24%) and Georgia (+21%) show elevated immigration searches alongside border states like Texas (+26%). `ICE near me` was the only validated realistic search term to perform consistently across all states.
  - **Campaign Implication:** Immigration is a mobilizing issue across the entire map, not just in border states.
- **AI Anxiety is Coastal:** Search interest for AI and job displacement is heavily concentrated in California (+7%). Battleground states are 30-59% lower than CA, with Wisconsin and Nevada showing the lowest engagement (-59% and -58%).
  - **Campaign Implication:** AI displacement messaging will not resonate in Rust Belt or Sun Belt battlegrounds.
- **Economy Searches Are Flat:** Economic anxiety searches show minimal state variation (-6 to +3 vs national). Furthermore, colloquial terms failed due to extreme zero rates (e.g., "why is food so expensive" = 69% zeros). Voters search for specific prices, not abstract economic anxiety.
  - **Campaign Implication:** Campaigns should focus on concrete pocketbook issues (gas, groceries) rather than abstract "economy" rhetoric.
- **War Isn't Personal Yet:** All states are -19% to -23% lower in Iran war searches, and direct draft fear terms ("am I going to be drafted") failed completely with 97% zeros. 
  - **Campaign Implication:** The threat of war with Iran is not yet a voter-mobilizing issue because there are no perceived personal stakes (no draft).
- **Partisan Media Consumption is Equal:** Battleground states match California in Fox/CNN/MSNBC search rates (with the exception of Nevada at -26%).
  - **Campaign Implication:** Battleground voters are consuming partisan media at high rates, making them just as polarized in media diet as safe coastal states.

## Methodological Conclusions
The following critical caveats were established during peer review and highlight key limitations of using Google Trends for predictive election modeling:

1. **Correlations are largely spurious at the state level:** Even after applying a 7-day rolling average to reduce noise, raw r values (ranging from 0.15 to 0.58) frequently collapsed after first-differencing in 8 of the 14 series, indicating the apparent relationship is an artifact of common time trends. However, the **National aggregate** maintained a genuine differenced correlation (r=0.28).
2. **Granger causality fails as a predictor:** Google Trends data is a poor leading indicator of prediction market movements. It only Granger-caused odds in 2/14 cases (AZ, MI). Conversely, Market Odds Granger-caused Trends in 4/14 cases, meaning Search is more often reactive than predictive.
3. **NH/ME are low-confidence:** Data from New Hampshire and Maine suffer from 63-88% zero-rates due to small state populations, making them structurally unreliable for daily search trend analysis.
4. **Realistic terms largely fail:** True colloquial "anxiety" searches (e.g., "why is food so expensive") are too sparse. Only 1 out of 25 proposed colloquial terms (`ICE near me`) was viable at the state level.
5. **National validation overstates usefulness:** Terms that pass volume/variance validation at the national level frequently collapse into zero-heavy noise when broken down to the state level.

---
*End of Report*