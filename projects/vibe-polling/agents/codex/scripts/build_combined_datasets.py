#!/usr/bin/env python3
"""
Build Codex-side merged datasets that combine shared Claude/base trends data
with Codex-collected R2 terms while preserving provenance.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling/agents/codex")
PROJECT = Path("/root/.openclaw/workspace/projects/vibe-polling")

SHARED_TRENDS = PROJECT / "data" / "raw" / "trends" / "trends_2026-03-19.parquet"
CODEX_TERMS = ROOT / "data" / "raw" / "r2_new_terms_2026-03-20.parquet"
TERM_DECISIONS = ROOT / "data" / "reference" / "r2_term_decisions.json"
VALIDATION_RESULTS = ROOT / "data" / "processed" / "r2_term_validation.csv"


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def main() -> None:
    shared = pd.read_parquet(SHARED_TRENDS)
    shared["date"] = pd.to_datetime(shared["date"])
    shared["data_source"] = "shared_base_trends"
    shared["source_agent"] = "claude_or_shared_project_pipeline"

    codex = pd.read_parquet(CODEX_TERMS)
    codex["date"] = pd.to_datetime(codex["date"])
    codex["data_source"] = "codex_r2_collection"
    codex["source_agent"] = "codex"
    if "collected_at" in codex.columns:
        codex = codex.rename(columns={"collected_at": "collection_time"})
    if "collection_time" not in codex.columns:
        codex["collection_time"] = ""
    if "collection_run" not in codex.columns:
        codex["collection_run"] = "codex_r2_collection"
    if "category" not in codex.columns:
        validation = pd.read_csv(VALIDATION_RESULTS)
        codex["category"] = codex["term"].map(dict(zip(validation["term"], validation["category"])))
    codex["collection_run"] = codex["collection_run"].astype(str)
    codex["collection_time"] = codex["collection_time"].astype(str)

    decisions = json.loads(TERM_DECISIONS.read_text())
    retained = [row["term"] for row in decisions["retained_for_main_study"]]

    full_codex = codex[
        ["date", "term", "interest", "geo", "state", "category", "collection_time", "collection_run", "timeframe", "data_source", "source_agent"]
    ].copy()
    shared_base = shared[
        ["date", "term", "interest", "geo", "state", "category", "collected_at", "collection_run", "timeframe", "data_source", "source_agent"]
    ].rename(columns={"collected_at": "collection_time"})

    merged_extended = pd.concat([shared_base, full_codex], ignore_index=True)
    merged_extended["merged_at"] = now_iso()
    merged_extended.to_parquet(ROOT / "data" / "processed" / "combined_extended_terms.parquet", index=False)

    codex_main = full_codex[full_codex["term"].isin(retained)].copy()
    merged_main = pd.concat([shared_base, codex_main], ignore_index=True)
    merged_main["merged_at"] = now_iso()
    merged_main.to_parquet(ROOT / "data" / "processed" / "combined_main_analysis.parquet", index=False)

    metadata = {
        "created_at": now_iso(),
        "shared_base_rows": int(shared_base.shape[0]),
        "codex_extended_rows": int(full_codex.shape[0]),
        "codex_main_rows": int(codex_main.shape[0]),
        "retained_codex_terms": retained,
        "files": {
            "extended": str(ROOT / "data" / "processed" / "combined_extended_terms.parquet"),
            "main": str(ROOT / "data" / "processed" / "combined_main_analysis.parquet"),
        },
    }
    (ROOT / "data" / "processed" / "combined_dataset_metadata.json").write_text(
        json.dumps(metadata, indent=2)
    )


if __name__ == "__main__":
    main()
