#!/usr/bin/env python3
"""
Codex-only R2 term validation and collection.

Workflow:
1. Compare reviewer/Codex candidate terms against Claude-covered terms.
2. Validate only uncovered candidate terms nationally.
3. Collect state-level data only for terms that pass validation.

All outputs stay inside agents/codex/.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

import pandas as pd
from pytrends.request import TrendReq

ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling/agents/codex")
REFERENCE = ROOT / "data" / "reference"
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
LOGS = ROOT / "logs"
REPORTS = ROOT / "reports"

CLAUDE_VALIDATION = Path(
    "/root/.openclaw/workspace/projects/vibe-polling/agents/claude-code/search_term_validation.json"
)

STATE_CODES = [
    "US-PA",
    "US-MI",
    "US-WI",
    "US-AZ",
    "US-GA",
    "US-NV",
    "US-NC",
    "US-CA",
    "US-TX",
    "US-OH",
    "US-ME",
    "US-NH",
    "US-MN",
]

MIN_AVG = 5.0
MAX_ZERO_RATIO = 0.50
MIN_VARIANCE = 10.0

VALIDATION_DELAY_RANGE = (20.0, 35.0)
STATE_DELAY_RANGE = (12.0, 20.0)
RETRY_DELAY_SECONDS = 90.0
MAX_RETRIES = 3


@dataclass
class CandidateTerm:
    category: str
    term: str
    source: str
    rationale: str


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def to_simple_markdown(df: pd.DataFrame) -> str:
    columns = [str(col) for col in df.columns]
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join(["---"] * len(columns)) + " |"
    rows = []
    for values in df.fillna("").astype(str).itertuples(index=False, name=None):
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join([header, divider, *rows]) + "\n"


def sleep_range(bounds: Sequence[float], label: str) -> None:
    delay = random.uniform(*bounds)
    print(f"[sleep] {label}: {delay:.1f}s", flush=True)
    time.sleep(delay)


def load_candidates() -> List[CandidateTerm]:
    payload = json.loads((REFERENCE / "candidate_terms_r2.json").read_text())
    rows: List[CandidateTerm] = []
    for category, values in payload.items():
        if category == "metadata":
            continue
        for row in values:
            rows.append(
                CandidateTerm(
                    category=category,
                    term=row["term"],
                    source=row["source"],
                    rationale=row["rationale"],
                )
            )
    return rows


def load_claude_terms() -> Dict[str, Dict]:
    payload = json.loads(CLAUDE_VALIDATION.read_text())
    covered: Dict[str, Dict] = {}
    for category in payload["categories"].values():
        for row in category["results"]:
            covered[row["term"].strip().lower()] = row
    return covered


def build_coverage_report() -> pd.DataFrame:
    claude = load_claude_terms()
    rows = []
    for item in load_candidates():
        claude_row = claude.get(item.term.strip().lower())
        rows.append(
            {
                "category": item.category,
                "term": item.term,
                "source": item.source,
                "rationale": item.rationale,
                "covered_by_claude": claude_row is not None,
                "claude_status": claude_row["status"] if claude_row else None,
                "claude_avg_volume": claude_row["avg_volume"] if claude_row else None,
                "claude_zero_ratio": claude_row["zero_ratio"] if claude_row else None,
            }
        )
    df = pd.DataFrame(rows).sort_values(["covered_by_claude", "category", "term"])
    out_csv = PROCESSED / "candidate_term_coverage.csv"
    out_md = REPORTS / "candidate_term_coverage.md"
    df.to_csv(out_csv, index=False)
    out_md.write_text(to_simple_markdown(df))
    print(f"saved {out_csv}")
    print(f"saved {out_md}")
    return df


def make_client() -> TrendReq:
    return TrendReq(hl="en-US", tz=300)


def fetch_series(
    pytrends: TrendReq, term: str, geo: str, timeframe: str
) -> pd.Series | None:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            pytrends.build_payload([term], geo=geo, timeframe=timeframe)
            df = pytrends.interest_over_time()
            if df.empty:
                return None
            if "isPartial" in df.columns:
                df = df.drop(columns=["isPartial"])
            return df[term]
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] {geo} | {term} | attempt {attempt} failed: {exc}", flush=True)
            if attempt >= MAX_RETRIES:
                return None
            time.sleep(RETRY_DELAY_SECONDS)
    return None


def validate_terms(timeframe: str) -> pd.DataFrame:
    coverage = pd.read_csv(PROCESSED / "candidate_term_coverage.csv")
    uncovered = coverage.loc[~coverage["covered_by_claude"]].copy()
    pytrends = make_client()
    rows = []
    for _, row in uncovered.iterrows():
        term = row["term"]
        print(f"[validate] {term}", flush=True)
        series = fetch_series(pytrends, term, "US", timeframe)
        if series is None:
            rows.append(
                {
                    **row.to_dict(),
                    "validated_at": now_iso(),
                    "geo": "US",
                    "timeframe": timeframe,
                    "status": "ERROR",
                    "avg_volume": None,
                    "variance": None,
                    "zero_ratio": None,
                    "n_obs": 0,
                }
            )
        else:
            values = series.astype(float)
            avg = float(values.mean())
            var = float(values.var())
            zero = float((values == 0).mean())
            status = "PASS"
            if avg < MIN_AVG:
                status = "LOW_VOLUME"
            elif var < MIN_VARIANCE:
                status = "FLAT"
            elif zero > MAX_ZERO_RATIO:
                status = "TOO_MANY_ZEROS"
            rows.append(
                {
                    **row.to_dict(),
                    "validated_at": now_iso(),
                    "geo": "US",
                    "timeframe": timeframe,
                    "status": status,
                    "avg_volume": avg,
                    "variance": var,
                    "zero_ratio": zero,
                    "n_obs": int(values.shape[0]),
                }
            )
        sleep_range(VALIDATION_DELAY_RANGE, "national validation delay")
    df = pd.DataFrame(rows).sort_values(["status", "category", "term"])
    out_csv = PROCESSED / "r2_term_validation.csv"
    out_md = REPORTS / "r2_term_validation.md"
    df.to_csv(out_csv, index=False)
    out_md.write_text(to_simple_markdown(df))
    print(f"saved {out_csv}")
    print(f"saved {out_md}")
    return df


def collect_states(timeframe: str, terms: Iterable[str]) -> pd.DataFrame:
    pytrends = make_client()
    rows: List[pd.DataFrame] = []
    collection_log = []
    for geo in STATE_CODES:
        print(f"[state] {geo}", flush=True)
        for term in terms:
            print(f"  [collect] {term}", flush=True)
            series = fetch_series(pytrends, term, geo, timeframe)
            collection_log.append(
                {
                    "timestamp": now_iso(),
                    "geo": geo,
                    "term": term,
                    "ok": series is not None,
                    "timeframe": timeframe,
                }
            )
            if series is not None:
                df = series.reset_index()
                df.columns = ["date", "interest"]
                df["term"] = term
                df["geo"] = geo
                df["state"] = geo.replace("US-", "")
                rows.append(df)
            sleep_range(STATE_DELAY_RANGE, "state collection delay")
        time.sleep(45.0)
    log_path = LOGS / "state_collection_log.json"
    log_path.write_text(json.dumps(collection_log, indent=2))
    if not rows:
        raise SystemExit("no state-level data collected")
    combined = pd.concat(rows, ignore_index=True)
    combined["collected_at"] = now_iso()
    combined["timeframe"] = timeframe
    out_path = RAW / f"r2_new_terms_{datetime.utcnow().date().isoformat()}.parquet"
    combined.to_parquet(out_path, index=False)
    print(f"saved {out_path}")
    print(f"saved {log_path}")
    return combined


def summarize_collection(df: pd.DataFrame) -> None:
    summary = (
        df.groupby("term")["interest"]
        .agg(
            n_obs="size",
            avg_interest="mean",
            zero_ratio=lambda x: float((x == 0).mean()),
            max_interest="max",
        )
        .reset_index()
        .sort_values(["zero_ratio", "avg_interest"], ascending=[True, False])
    )
    out_csv = PROCESSED / "r2_collection_summary.csv"
    out_md = REPORTS / "r2_collection_summary.md"
    summary.to_csv(out_csv, index=False)
    out_md.write_text(to_simple_markdown(summary))
    print(f"saved {out_csv}")
    print(f"saved {out_md}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["coverage", "validate", "collect"],
        required=True,
    )
    parser.add_argument(
        "--timeframe",
        default="today 3-m",
        help="Google Trends timeframe string",
    )
    parser.add_argument(
        "--terms",
        nargs="*",
        default=[],
        help="Optional explicit term override for collection mode",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mode == "coverage":
        build_coverage_report()
        return 0
    if args.mode == "validate":
        if not (PROCESSED / "candidate_term_coverage.csv").exists():
            build_coverage_report()
        validate_terms(args.timeframe)
        return 0
    if not (PROCESSED / "r2_term_validation.csv").exists() and not args.terms:
        raise SystemExit("run validation first or pass --terms explicitly")
    if args.terms:
        terms = args.terms
    else:
        validation = pd.read_csv(PROCESSED / "r2_term_validation.csv")
        terms = validation.loc[validation["status"] == "PASS", "term"].tolist()
    df = collect_states(args.timeframe, terms)
    summarize_collection(df)
    return 0


if __name__ == "__main__":
    sys.exit(main())
