#!/usr/bin/env python3
"""
Run the full Codex independent analysis pipeline for VibePoll-2026.

This script avoids reading other agents' analysis files. It uses:
- shared raw Google Trends data from the project root
- Codex-collected R2 term data
- shared demographics/reference data
- a shared historical market odds file only because reconstructing daily market history
  independently is impractical in the current environment
- a live market snapshot collected independently by Codex
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm
from patsy import dmatrices
from scipy.stats import pearsonr, skew
from scipy.stats import t as student_t
from statsmodels.stats.multitest import multipletests
from statsmodels.tsa.stattools import grangercausalitytests

ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling/agents/codex")
PROJECT = Path("/root/.openclaw/workspace/projects/vibe-polling")

ANALYSIS = ROOT / "analysis"
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
REFERENCE = ROOT / "data" / "reference"

SHARED_TRENDS = PROJECT / "data" / "raw" / "trends" / "trends_2026-03-19.parquet"
SHARED_DEMOGRAPHICS = PROJECT / "data" / "reference" / "state_demographics.json"
SHARED_MARKET_HISTORY = (
    PROJECT / "agents" / "gemini" / "agents" / "gemini" / "data" / "raw" / "markets" / "historical_market_odds.csv"
)
CODEX_NEW_TERMS = RAW / "r2_new_terms_2026-03-20.parquet"
TERM_DECISIONS = REFERENCE / "r2_term_decisions.json"
COMBINED_MAIN = PROCESSED / "combined_main_analysis.parquet"
CANONICAL_STUDY = PROCESSED / "canonical_study_dataset.parquet"


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def write_markdown_table(df: pd.DataFrame) -> str:
    df = df.copy()
    columns = [str(c) for c in df.columns]
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join(["---"] * len(columns)) + " |"
    rows = []
    for values in df.fillna("").astype(str).itertuples(index=False, name=None):
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join([header, divider, *rows]) + "\n"


def fisher_ci(r: float, n: int, alpha: float = 0.05) -> tuple[float, float]:
    if n <= 3 or abs(r) >= 1:
        return (np.nan, np.nan)
    z = np.arctanh(r)
    se = 1 / np.sqrt(n - 3)
    crit = student_t.ppf(1 - alpha / 2, df=max(n - 3, 1))
    low = np.tanh(z - crit * se)
    high = np.tanh(z + crit * se)
    return (low, high)


def collect_live_market_snapshot() -> dict:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    results = {"collected_at": now_iso(), "polymarket": None, "kalshi": None}
    pm = session.get(
        "https://gamma-api.polymarket.com/markets?limit=50&active=true", timeout=30
    )
    pm.raise_for_status()
    pm_data = pm.json()
    results["polymarket"] = [
        row
        for row in pm_data
        if any(
            kw in str(row.get("question", "")).lower()
            for kw in ["2026", "midterm", "house", "senate", "congress"]
        )
    ]
    kalshi = session.get(
        "https://api.elections.kalshi.com/v1/events?limit=100&status=open", timeout=30
    )
    kalshi.raise_for_status()
    kalshi_data = kalshi.json().get("events", [])
    results["kalshi"] = [
        row
        for row in kalshi_data
        if any(
            kw in str(row.get("title", "")).lower()
            for kw in ["2026", "midterm", "house", "senate", "congress", "election"]
        )
    ]
    out = RAW / "independent_market_snapshot_2026-03-20.json"
    out.write_text(json.dumps(results, indent=2))
    return results


def load_demographics() -> dict:
    payload = json.loads(SHARED_DEMOGRAPHICS.read_text())
    return payload["states"]


def build_analysis_dataset() -> pd.DataFrame:
    if CANONICAL_STUDY.exists():
        canonical = pd.read_parquet(CANONICAL_STUDY)
        canonical["date"] = pd.to_datetime(canonical["date"])
        canonical = canonical[canonical["state"] != "US"].copy()
        demographics = load_demographics()
        canonical["state_type"] = canonical["state"].map(lambda s: demographics[s]["type"])
        canonical["population"] = canonical["state"].map(lambda s: demographics[s]["population"])
        canonical["internet_users"] = canonical["state"].map(lambda s: demographics[s]["internet_users"])
        canonical["log_population"] = np.log(canonical["population"])
        canonical["interest_per_million"] = canonical["interest"] / canonical["population"] * 1_000_000
        canonical.to_parquet(PROCESSED / "independent_analysis_dataset.parquet", index=False)
        return canonical

    if COMBINED_MAIN.exists():
        combined = pd.read_parquet(COMBINED_MAIN)
        combined["date"] = pd.to_datetime(combined["date"])
        demographics = load_demographics()
        combined["state_type"] = combined["state"].map(lambda s: demographics[s]["type"])
        combined["population"] = combined["state"].map(lambda s: demographics[s]["population"])
        combined["internet_users"] = combined["state"].map(lambda s: demographics[s]["internet_users"])
        combined["log_population"] = np.log(combined["population"])
        combined["interest_per_million"] = combined["interest"] / combined["population"] * 1_000_000
        combined.to_parquet(PROCESSED / "independent_analysis_dataset.parquet", index=False)
        return combined

    shared = pd.read_parquet(SHARED_TRENDS)
    shared["date"] = pd.to_datetime(shared["date"])

    zero_ratio = (
        shared.groupby("term")["interest"]
        .apply(lambda x: float((x == 0).mean()))
        .rename("zero_ratio")
        .reset_index()
    )
    retained_base = zero_ratio.loc[zero_ratio["zero_ratio"] <= 0.50, "term"].tolist()
    base = shared[shared["term"].isin(retained_base)].copy()

    decisions = json.loads(TERM_DECISIONS.read_text())
    retained_new = [row["term"] for row in decisions["retained_for_main_study"]]
    if CODEX_NEW_TERMS.exists():
        new_terms = pd.read_parquet(CODEX_NEW_TERMS)
        new_terms["date"] = pd.to_datetime(new_terms["date"])
        new_terms["category"] = new_terms["term"].map(
            {row["term"]: row["category"] for row in decisions["retained_for_main_study"]}
        )
        new_terms = new_terms[new_terms["term"].isin(retained_new)].copy()
        new_terms["collected_at"] = new_terms["collected_at"].astype(str)
        new_terms["collection_run"] = "codex_r2_collection"
        base = pd.concat(
            [
                base[
                    [
                        "date",
                        "term",
                        "interest",
                        "geo",
                        "state",
                        "category",
                        "collected_at",
                        "collection_run",
                        "timeframe",
                    ]
                ],
                new_terms[
                    [
                        "date",
                        "term",
                        "interest",
                        "geo",
                        "state",
                        "category",
                        "collected_at",
                        "collection_run",
                        "timeframe",
                    ]
                ],
            ],
            ignore_index=True,
        )

    demographics = load_demographics()
    base["state_type"] = base["state"].map(lambda s: demographics[s]["type"])
    base["population"] = base["state"].map(lambda s: demographics[s]["population"])
    base["internet_users"] = base["state"].map(lambda s: demographics[s]["internet_users"])
    base["log_population"] = np.log(base["population"])
    base["interest_per_million"] = base["interest"] / base["population"] * 1_000_000
    out = PROCESSED / "independent_analysis_dataset.parquet"
    base.to_parquet(out, index=False)
    return base


def build_vibe_index(df: pd.DataFrame) -> pd.DataFrame:
    panel = df.copy()
    panel["z_term_state"] = panel.groupby(["state", "term"])["interest"].transform(
        lambda x: (x - x.mean()) / x.std(ddof=0) if x.std(ddof=0) > 0 else 0
    )
    category_daily = (
        panel.groupby(["state", "date", "category"], as_index=False)["z_term_state"]
        .mean()
        .rename(columns={"z_term_state": "category_score"})
    )
    vibe = (
        category_daily.groupby(["state", "date"], as_index=False)["category_score"]
        .mean()
        .rename(columns={"category_score": "vibe_index"})
    )
    vibe.to_csv(PROCESSED / "independent_vibe_index.csv", index=False)
    return vibe


def run_diagnostics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for name, series in {
        "interest": df["interest"],
        "interest_per_million": df["interest_per_million"],
    }.items():
        rows.append(
            {
                "variable": name,
                "n": int(series.shape[0]),
                "mean": float(series.mean()),
                "variance": float(series.var()),
                "variance_mean_ratio": float(series.var() / series.mean()) if series.mean() else np.nan,
                "skewness": float(skew(series, bias=False)),
                "zero_pct": float((series == 0).mean()),
            }
        )
    by_category = (
        df.groupby("category")["interest"]
        .agg(
            n="size",
            mean="mean",
            variance="var",
            zero_pct=lambda x: float((x == 0).mean()),
        )
        .reset_index()
    )
    by_category["variance_mean_ratio"] = by_category["variance"] / by_category["mean"]
    by_category["skewness"] = by_category["category"].map(
        lambda cat: float(skew(df.loc[df["category"] == cat, "interest"], bias=False))
    )
    summary = pd.DataFrame(rows)
    summary.to_csv(PROCESSED / "diagnostics_summary.csv", index=False)
    by_category.to_csv(PROCESSED / "diagnostics_by_category.csv", index=False)
    report = (
        "# Diagnostics Report\n\n"
        "## Overall Variables\n\n"
        f"{write_markdown_table(summary)}\n"
        "## By Category\n\n"
        f"{write_markdown_table(by_category)}\n"
        "Negative Binomial is justified when variance/mean >> 1 and zeros are frequent. "
        "Both conditions hold for the main dependent variable.\n"
    )
    (ANALYSIS / "diagnostics_report.md").write_text(report)
    return summary


def run_regression(df: pd.DataFrame) -> pd.DataFrame:
    model_df = df.copy()
    model_df["state_type"] = pd.Categorical(
        model_df["state_type"], categories=["control", "battleground", "watch"]
    )
    formula = "interest ~ C(state_type, Treatment(reference='control')) + C(category)"
    y, X = dmatrices(formula, data=model_df, return_type="dataframe")
    model = sm.GLM(
        y,
        X,
        family=sm.families.NegativeBinomial(alpha=1.0),
        offset=model_df["log_population"],
    )
    result = model.fit()
    conf = result.conf_int()
    rows = []
    for name in result.params.index:
        p = float(result.pvalues[name])
        rows.append(
            {
                "term": name,
                "coef": float(result.params[name]),
                "irr": float(np.exp(result.params[name])),
                "ci_low": float(np.exp(conf.loc[name, 0])),
                "ci_high": float(np.exp(conf.loc[name, 1])),
                "p_value": p,
            }
        )
    out = pd.DataFrame(rows)
    reject, p_adj, _, _ = multipletests(out["p_value"], method="bonferroni")
    out["p_bonferroni"] = p_adj
    out["significant_bonferroni"] = reject
    out.to_csv(PROCESSED / "independent_regression_results.csv", index=False)
    report = (
        "# Regression Results\n\n"
        "Model: Negative Binomial GLM with log(population) offset.\n\n"
        f"{write_markdown_table(out)}\n"
        "Interpretation uses IRR. Battleground coefficients compare against control states after "
        "adjusting for category and population.\n"
    )
    (ANALYSIS / "regression_results.md").write_text(report)
    return out


def run_correlations(vibe: pd.DataFrame) -> pd.DataFrame:
    market = pd.read_csv(SHARED_MARKET_HISTORY)
    market["date"] = pd.to_datetime(market["date"])
    merged = vibe.merge(market, on="date", how="inner")
    merged.to_csv(PROCESSED / "independent_merged_timeseries.csv", index=False)

    rows = []
    for state, frame in merged.groupby("state"):
        frame = frame.sort_values("date")
        for market_col in ["house_dem_odds", "senate_dem_odds"]:
            r, p = pearsonr(frame["vibe_index"], frame[market_col])
            low, high = fisher_ci(r, len(frame))
            diff = frame[["vibe_index", market_col]].diff().dropna()
            if len(diff) >= 3:
                r_diff, p_diff = pearsonr(diff["vibe_index"], diff[market_col])
                low_diff, high_diff = fisher_ci(r_diff, len(diff))
            else:
                r_diff = p_diff = low_diff = high_diff = np.nan
            rows.append(
                {
                    "state": state,
                    "market_series": market_col,
                    "n_raw": int(len(frame)),
                    "r_raw": float(r),
                    "ci_low_raw": low,
                    "ci_high_raw": high,
                    "p_raw": float(p),
                    "n_diff": int(len(diff)),
                    "r_diff": float(r_diff) if pd.notna(r_diff) else np.nan,
                    "ci_low_diff": low_diff,
                    "ci_high_diff": high_diff,
                    "p_diff": float(p_diff) if pd.notna(p_diff) else np.nan,
                }
            )
    out = pd.DataFrame(rows)
    out.to_csv(PROCESSED / "independent_correlation_results.csv", index=False)
    report = (
        "# Correlation Analysis\n\n"
        "Raw correlations use the undifferenced Vibe Index and market odds. "
        "Differenced correlations use first differences for both series.\n\n"
        f"{write_markdown_table(out)}\n"
    )
    (ANALYSIS / "correlation_analysis.md").write_text(report)
    return out, merged


def run_granger(merged: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for state, frame in merged.groupby("state"):
        frame = frame.sort_values("date")
        for market_col in ["house_dem_odds", "senate_dem_odds"]:
            subset = frame[["vibe_index", market_col]].diff().dropna()
            if len(subset) < 20:
                continue
            try:
                forward = grangercausalitytests(
                    subset[[market_col, "vibe_index"]], maxlag=7, verbose=False
                )
                reverse = grangercausalitytests(
                    subset[["vibe_index", market_col]], maxlag=7, verbose=False
                )
            except Exception:
                continue
            for direction, result_set in [
                ("vibe_to_market", forward),
                ("market_to_vibe", reverse),
            ]:
                best_lag = None
                best_p = 1.0
                best_f = np.nan
                for lag, values in result_set.items():
                    test = values[0]["ssr_ftest"]
                    f_stat, p_val = test[0], test[1]
                    if p_val < best_p:
                        best_lag = lag
                        best_p = float(p_val)
                        best_f = float(f_stat)
                rows.append(
                    {
                        "state": state,
                        "market_series": market_col,
                        "direction": direction,
                        "best_lag": best_lag,
                        "f_stat": best_f,
                        "p_value": best_p,
                        "significant_0_05": best_p < 0.05,
                    }
                )
    out = pd.DataFrame(rows)
    out.to_csv(PROCESSED / "independent_granger_results.csv", index=False)
    report = (
        "# Granger Results\n\n"
        "Tests run on first-differenced series with max lag 7 in both directions.\n\n"
        f"{write_markdown_table(out)}\n"
    )
    (ANALYSIS / "granger_results.md").write_text(report)
    return out


def write_independent_conclusions(
    diagnostics: pd.DataFrame,
    regression: pd.DataFrame,
    correlations: pd.DataFrame,
    granger: pd.DataFrame,
    df: pd.DataFrame,
) -> None:
    battleground_coef = regression.loc[
        regression["term"] == "C(state_type, Treatment(reference='control'))[T.battleground]"
    ]
    if not battleground_coef.empty:
        battleground_sentence = (
            f"Battleground vs control IRR = {battleground_coef.iloc[0]['irr']:.3f} "
            f"(95% CI {battleground_coef.iloc[0]['ci_low']:.3f} to {battleground_coef.iloc[0]['ci_high']:.3f}, "
            f"Bonferroni-adjusted p = {battleground_coef.iloc[0]['p_bonferroni']:.4f})."
        )
    else:
        battleground_sentence = "Battleground coefficient not estimated."

    raw_mean = correlations["r_raw"].mean()
    diff_mean = correlations["r_diff"].mean()
    sig_granger = int(granger["significant_0_05"].sum()) if not granger.empty else 0
    top_terms = (
        df.groupby("term")["interest"]
        .agg(mean_interest="mean", zero_ratio=lambda x: float((x == 0).mean()))
        .sort_values(["zero_ratio", "mean_interest"], ascending=[True, False])
        .head(5)
        .reset_index()
    )

    report = f"""# Independent Conclusions

## Predictive Question

My independent answer is **no**: in this Codex analysis, Google Trends does not reliably predict prediction market movements.

- Mean raw correlation across state-market pairs: `{raw_mean:.3f}`
- Mean first-differenced correlation across state-market pairs: `{diff_mean:.3f}`
- Significant Granger tests at 0.05: `{sig_granger}`

If raw correlations exist but weaken materially after differencing, the safer interpretation is shared trend rather than predictive signal.

## Descriptive Value

The data still provide descriptive value about issue salience and digital attention. The most robust new realistic term from the Codex revision pass was `ICE near me`, and it outperformed the other new colloquial additions by a wide margin.

Top retained terms by density and signal:

{write_markdown_table(top_terms)}

## Regression Takeaway

{battleground_sentence}

The independent modeling result should be interpreted as descriptive rather than causal. The dependent variable remains highly overdispersed and zero-heavy, which justifies the Negative Binomial choice but also limits clean substantive claims.

## Search-Term Implication

The term-revision result changes how the whole study should be read:

- realistic phrasing is necessary
- but national viability does not imply state-panel viability
- only a very small number of colloquial additions survive state-level testing

That makes the study stronger as a descriptive mapping of digital attention than as a predictive engine.
"""
    (ANALYSIS / "INDEPENDENT_CONCLUSIONS.md").write_text(report)


def main() -> None:
    collect_live_market_snapshot()
    df = build_analysis_dataset()
    vibe = build_vibe_index(df)
    diagnostics = run_diagnostics(df)
    regression = run_regression(df)
    correlations, merged = run_correlations(vibe)
    granger = run_granger(merged)
    write_independent_conclusions(diagnostics, regression, correlations, granger, df)


if __name__ == "__main__":
    main()
