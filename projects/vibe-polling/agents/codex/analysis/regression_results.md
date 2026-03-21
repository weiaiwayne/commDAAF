# Regression Results

Input dataset: [canonical_study_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/canonical_study_dataset.parquet), filtered to the 13 study states in [independent_analysis_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/independent_analysis_dataset.parquet).

Model: Negative Binomial GLM with log(population) offset.

Interpretation notes:

- The dependent variable is Google Trends `interest`, a 0-100 relative interest index carried in the canonical panel.
- IRR values are multiplicative effects on expected interest after adjusting for population and category.
- The battleground coefficient therefore means higher expected search interest than the control-state reference category, conditional on those controls.
- The model is descriptive. It does not include time fixed effects, so it should not be read as a causal estimate.

| term | coef | irr | ci_low | ci_high | p_value | p_bonferroni | significant_bonferroni |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Intercept | -18.23484675155649 | 1.2042223337189631e-08 | 1.1252516463095995e-08 | 1.2887352209467944e-08 | 0.0 | 0.0 | True |
| C(state_type, Treatment(reference='control'))[T.battleground] | 0.8896391513717512 | 2.4342510966177557 | 2.4036450479647744 | 2.4652468576431783 | 0.0 | 0.0 | True |
| C(state_type, Treatment(reference='control'))[T.watch] | 1.8906412606379592 | 6.623614782909861 | 6.522569946827253 | 6.726224961945047 | 0.0 | 0.0 | True |
| C(category)[T.ai_jobs] | 3.85776828196445 | 47.35954020240083 | 44.20663702969592 | 50.73731455021401 | 0.0 | 0.0 | True |
| C(category)[T.ai_jobs_realistic] | -0.8832473252992468 | 0.4134381612415579 | 0.2345791324040611 | 0.7286714356005575 | 0.0022530069286554096 | 0.04280713164445278 | True |
| C(category)[T.economy] | 4.030269022000091 | 56.276048706061935 | 52.5566746881171 | 60.2586384462239 | 0.0 | 0.0 | True |
| C(category)[T.economy_colloquial] | 4.015273049412871 | 55.438430767020044 | 51.69099865561003 | 59.457539723429505 | 0.0 | 0.0 | True |
| C(category)[T.economy_realistic] | 3.923346116397056 | 50.56937300188915 | 44.59969095311383 | 57.338098788454815 | 0.0 | 0.0 | True |
| C(category)[T.epstein] | 3.1725012530157115 | 23.86710743358765 | 22.23019417505685 | 25.624554277873642 | 0.0 | 0.0 | True |
| C(category)[T.immigration] | 3.935551197466299 | 51.19035817751964 | 47.78319500163615 | 54.84046787271182 | 0.0 | 0.0 | True |
| C(category)[T.immigration_local] | 4.481344580965312 | 88.35339113241442 | 81.63863816671461 | 95.62043047136679 | 0.0 | 0.0 | True |
| C(category)[T.immigration_realistic] | 2.4586869025893727 | 11.689452068703739 | 10.16879359234105 | 13.437512368177023 | 5.36701046814062e-262 | 1.0197319889467178e-260 | True |
| C(category)[T.iran_war] | 3.561185787854154 | 35.20491796832861 | 32.861230550535225 | 37.715758916902764 | 0.0 | 0.0 | True |
| C(category)[T.iran_war_realistic] | 2.1520551819620937 | 8.602519985975718 | 7.838383658328226 | 9.441149264298083 | 0.0 | 0.0 | True |
| C(category)[T.partisan_pairs] | 4.404640124549576 | 81.82968904743245 | 76.33216252973106 | 87.7231534871213 | 0.0 | 0.0 | True |
| C(category)[T.political] | 3.873157500627413 | 48.09400343492813 | 44.87803719053625 | 51.540426257471104 | 0.0 | 0.0 | True |
| C(category)[T.political_realistic] | 0.9061598391586972 | 2.474800629797085 | 1.8466303569568745 | 3.3166562729625264 | 1.3132397224934122e-09 | 2.495155472737483e-08 | True |
| C(category)[T.state_specific] | 4.037709656391356 | 56.696339886928094 | 52.02649157931112 | 61.78534932869363 | 0.0 | 0.0 | True |
| C(category)[T.war_anxiety] | 2.888448035433199 | 17.96540628069251 | 16.685076811552264 | 19.343981839321174 | 0.0 | 0.0 | True |

Interpretation uses IRR. Battleground coefficients compare against control states after adjusting for category and population.
