# Granger Results

Input dataset: [canonical_study_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/canonical_study_dataset.parquet), filtered to the 13 study states in [independent_analysis_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/independent_analysis_dataset.parquet).

Tests run on first-differenced series with max lag 7 in both directions.

Summary:

- Significant tests at `p < 0.05`: `22/52`
- Directional split: `market_to_vibe = 18`, `vibe_to_market = 4`
- State-market pairs with any significant Granger result: `19/26`
- Bidirectional significance appears in `3/26` pairs: NC house, NV senate, and OH house

Interpretation:

- The table does not support a blanket statement that Granger relationships are absent.
- It also does not support a broad claim that search behavior leads markets.
- The dominant pattern is the reverse: market movements more often precede search movement than search movement precedes market movement.

| state | market_series | direction | best_lag | f_stat | p_value | significant_0_05 |
| --- | --- | --- | --- | --- | --- | --- |
| AZ | house_dem_odds | vibe_to_market | 2 | 1.1603777644808793 | 0.3173531601595885 | False |
| AZ | house_dem_odds | market_to_vibe | 2 | 2.0861639078059784 | 0.12927907751453815 | False |
| AZ | senate_dem_odds | vibe_to_market | 1 | 0.4587860500503735 | 0.4996402345769102 | False |
| AZ | senate_dem_odds | market_to_vibe | 6 | 1.3332641715872797 | 0.25030422568193306 | False |
| CA | house_dem_odds | vibe_to_market | 3 | 1.7362678943808552 | 0.16427750842796995 | False |
| CA | house_dem_odds | market_to_vibe | 2 | 9.660250287777176 | 0.00014091065012274614 | True |
| CA | senate_dem_odds | vibe_to_market | 1 | 1.953910982472563 | 0.16503049943956546 | False |
| CA | senate_dem_odds | market_to_vibe | 6 | 3.0817445626091566 | 0.008510399451411705 | True |
| GA | house_dem_odds | vibe_to_market | 5 | 1.247306864108261 | 0.2932398966994016 | False |
| GA | house_dem_odds | market_to_vibe | 2 | 6.00607049456413 | 0.003390897000382563 | True |
| GA | senate_dem_odds | vibe_to_market | 1 | 0.5987244391716672 | 0.44075558296137185 | False |
| GA | senate_dem_odds | market_to_vibe | 6 | 4.802375385346861 | 0.0002615184739550803 | True |
| ME | house_dem_odds | vibe_to_market | 2 | 0.32148374630257953 | 0.7257835541836757 | False |
| ME | house_dem_odds | market_to_vibe | 4 | 4.294490768486218 | 0.003022654029385981 | True |
| ME | senate_dem_odds | vibe_to_market | 3 | 0.9717426806714212 | 0.409162440615103 | False |
| ME | senate_dem_odds | market_to_vibe | 3 | 2.534685932440493 | 0.061006704883902786 | False |
| MI | house_dem_odds | vibe_to_market | 2 | 4.0088374935438145 | 0.021001670700661106 | True |
| MI | house_dem_odds | market_to_vibe | 3 | 2.5010154074532656 | 0.06362898954652602 | False |
| MI | senate_dem_odds | vibe_to_market | 4 | 0.36436862209889304 | 0.833460845933138 | False |
| MI | senate_dem_odds | market_to_vibe | 6 | 2.84085879237577 | 0.013858530380645379 | True |
| MN | house_dem_odds | vibe_to_market | 5 | 0.9351250672943355 | 0.46190176768448565 | False |
| MN | house_dem_odds | market_to_vibe | 2 | 3.9054873207918264 | 0.023120235539842618 | True |
| MN | senate_dem_odds | vibe_to_market | 3 | 0.9899739656268914 | 0.4006914940034382 | False |
| MN | senate_dem_odds | market_to_vibe | 6 | 2.1532227794300858 | 0.05454554830521477 | False |
| NC | house_dem_odds | vibe_to_market | 2 | 3.6099932067608704 | 0.030461555906486828 | True |
| NC | house_dem_odds | market_to_vibe | 6 | 3.165624980322725 | 0.007178290682072693 | True |
| NC | senate_dem_odds | vibe_to_market | 1 | 3.267911041392242 | 0.07343091549682929 | False |
| NC | senate_dem_odds | market_to_vibe | 6 | 2.109940792006774 | 0.0593504466972383 | False |
| NH | house_dem_odds | vibe_to_market | 3 | 2.691018758583085 | 0.05016941510358888 | False |
| NH | house_dem_odds | market_to_vibe | 4 | 5.899712696792319 | 0.00026682001345419655 | True |
| NH | senate_dem_odds | vibe_to_market | 3 | 2.2939078956640087 | 0.08239581427623928 | False |
| NH | senate_dem_odds | market_to_vibe | 2 | 6.503869397099023 | 0.0021733893970281434 | True |
| NV | house_dem_odds | vibe_to_market | 3 | 1.8480287678244236 | 0.14319998396037653 | False |
| NV | house_dem_odds | market_to_vibe | 2 | 3.953379628734873 | 0.022112672846440615 | True |
| NV | senate_dem_odds | vibe_to_market | 1 | 5.063971782433694 | 0.026454487861698312 | True |
| NV | senate_dem_odds | market_to_vibe | 7 | 2.4756725316944737 | 0.02268746568725395 | True |
| OH | house_dem_odds | vibe_to_market | 3 | 4.110317954394183 | 0.00849661540731898 | True |
| OH | house_dem_odds | market_to_vibe | 5 | 2.410345370441771 | 0.041864565494379086 | True |
| OH | senate_dem_odds | vibe_to_market | 6 | 1.7423058612514817 | 0.11982756967023983 | False |
| OH | senate_dem_odds | market_to_vibe | 7 | 1.1579419314303074 | 0.3349441178003331 | False |
| PA | house_dem_odds | vibe_to_market | 5 | 0.8304842803706652 | 0.5311328875262874 | False |
| PA | house_dem_odds | market_to_vibe | 2 | 4.180230959116849 | 0.017914464848614652 | True |
| PA | senate_dem_odds | vibe_to_market | 2 | 2.736681874776034 | 0.06940893250038042 | False |
| PA | senate_dem_odds | market_to_vibe | 6 | 2.479202096481644 | 0.02864752921072443 | True |
| TX | house_dem_odds | vibe_to_market | 5 | 1.9298367185807839 | 0.0963848409191526 | False |
| TX | house_dem_odds | market_to_vibe | 2 | 5.691875733421446 | 0.004498727871923739 | True |
| TX | senate_dem_odds | vibe_to_market | 1 | 3.130993940837068 | 0.07963938768280199 | False |
| TX | senate_dem_odds | market_to_vibe | 6 | 4.055027887001805 | 0.0011784556020167458 | True |
| WI | house_dem_odds | vibe_to_market | 1 | 1.467325137100711 | 0.22841204718745706 | False |
| WI | house_dem_odds | market_to_vibe | 2 | 5.501076113062655 | 0.005345283430782616 | True |
| WI | senate_dem_odds | vibe_to_market | 1 | 0.7813626212635201 | 0.37868828424802903 | False |
| WI | senate_dem_odds | market_to_vibe | 6 | 1.6097624489736786 | 0.15311307764624504 | False |
