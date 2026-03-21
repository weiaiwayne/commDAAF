# Independent Conclusions

This document is based on the canonical combined study dataset:
[canonical_study_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/canonical_study_dataset.parquet).

For modeling and state-level temporal analysis, the national `US` rows were excluded, leaving the 13 study states in:
[independent_analysis_dataset.parquet](/root/.openclaw/workspace/projects/vibe-polling/agents/codex/data/processed/independent_analysis_dataset.parquet).

## Predictive Question

My independent answer is narrower than a blanket null: in this Codex analysis, Google Trends is **not a reliable general-purpose leading indicator** for prediction market movements.

- Raw correlations significant at 0.05 in `13/26` state-market pairs
- First-differenced correlations significant at 0.05 in `2/26` pairs
- Median raw correlation across state-market pairs: `0.184`
- Median first-differenced correlation across state-market pairs: `-0.043`
- Significant Granger tests at 0.05: `22/52`
- Directional split: `market_to_vibe = 18`, `vibe_to_market = 4`
- Bidirectional Granger significance appears in `3` state-market pairs: NC house, NV senate, OH house

The temporal evidence is therefore asymmetric. A substantial share of undifferenced associations appear trend-driven, and when Granger tests are significant they point much more often from markets to search behavior than the reverse. That pattern argues against broad claims that the Vibe Index leads markets, while leaving room for localized or reverse-direction information flow in a small number of state-market pairs.

## Descriptive Value

The data still provide descriptive value about issue salience and digital attention. The most robust new realistic term from the Codex revision pass was `ICE near me`, and it outperformed the other new colloquial additions by a wide margin.

Top retained terms by density and signal:

| term | mean_interest | zero_ratio |
| --- | --- | --- |
| Detroit jobs | 67.38461538461539 | 0.0 |
| ChatGPT | 67.34561213434453 | 0.0 |
| Fox News | 66.04712892741061 | 0.0 |
| military | 56.28909551986475 | 0.0 |
| broke | 53.59340659340659 | 0.0 |


## Regression Takeaway

Battleground vs control IRR = 2.434 (95% CI 2.404 to 2.465, Bonferroni-adjusted p = 0.0000).

This model is descriptive, not causal. It estimates multiplicative differences in expected Google Trends interest after adjusting for population with a log offset and controlling for term category. The dependent variable is the Google Trends interest index in the canonical panel, which remains highly overdispersed and zero-heavy, justifying a Negative Binomial specification but limiting clean substantive claims.

## Search-Term Implication

The term-revision result changes how the whole study should be read:

- realistic phrasing is necessary
- realistic phrasing helps
- realistic phrasing alone is insufficient
- but national viability does not imply state-panel viability
- only a very small number of colloquial additions survive state-level testing

That makes the study stronger as a descriptive mapping of digital attention than as a predictive engine.
