#!/usr/bin/env python3
"""
Build one canonical Codex-side dataset from all available agent-collected
Google Trends artifacts, preserving provenance and applying a documented
deduplication rule for study use.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling/agents/codex")
PROJECT = Path("/root/.openclaw/workspace/projects/vibe-polling")
PROCESSED = ROOT / "data" / "processed"


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def normalize_shared_base(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path).copy()
    df["date"] = pd.to_datetime(df["date"])
    df["geo"] = df["geo"].astype(str)
    df["collection_time"] = df["collected_at"].astype(str)
    df["source_agent"] = "shared_base"
    df["source_file"] = str(path)
    df["source_kind"] = "base_full_panel"
    df["timeframe"] = df["timeframe"].astype(str)
    return df[
        ["date", "state", "geo", "term", "category", "interest", "collection_time", "collection_run", "timeframe", "source_agent", "source_kind", "source_file"]
    ]


def normalize_codex(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path).copy()
    df["date"] = pd.to_datetime(df["date"])
    if "geo" not in df.columns:
        df["geo"] = "US-" + df["state"].astype(str)
    if "category" not in df.columns:
        val = pd.read_csv(ROOT / "data" / "processed" / "r2_term_validation.csv")
        df["category"] = df["term"].map(dict(zip(val["term"], val["category"])))
    if "collected_at" in df.columns:
        df["collection_time"] = df["collected_at"].astype(str)
    else:
        df["collection_time"] = ""
    if "collection_run" not in df.columns:
        df["collection_run"] = "codex_r2_collection"
    if "timeframe" not in df.columns:
        df["timeframe"] = "today 3-m"
    df["source_agent"] = "codex"
    df["source_file"] = str(path)
    df["source_kind"] = "codex_new_terms"
    return df[
        ["date", "state", "geo", "term", "category", "interest", "collection_time", "collection_run", "timeframe", "source_agent", "source_kind", "source_file"]
    ]


def normalize_kimi(path: Path, kind: str) -> pd.DataFrame:
    df = pd.read_parquet(path).copy()
    df["date"] = pd.to_datetime(df["date"])
    if "geo" not in df.columns:
        if "state_code" in df.columns:
            df["geo"] = df["state_code"].astype(str)
        else:
            df["geo"] = "US-" + df["state"].astype(str)
    if "collection_timestamp" in df.columns:
        df["collection_time"] = df["collection_timestamp"].astype(str)
    elif "collected_at" in df.columns:
        df["collection_time"] = df["collected_at"].astype(str)
    else:
        df["collection_time"] = ""
    if "collection_run" not in df.columns:
        df["collection_run"] = kind
    if "timeframe" not in df.columns:
        df["timeframe"] = "today 3-m"
    if "state_code" in df.columns and "state" not in df.columns:
        df["state"] = df["state_code"].astype(str).str.replace("US-", "", regex=False)
    df["state"] = df["state"].astype(str).str.replace("US-", "", regex=False)
    df["source_agent"] = "kimi"
    df["source_file"] = str(path)
    df["source_kind"] = kind
    return df[
        ["date", "state", "geo", "term", "category", "interest", "collection_time", "collection_run", "timeframe", "source_agent", "source_kind", "source_file"]
    ]


def normalize_gemini(path: Path, kind: str) -> pd.DataFrame:
    df = pd.read_parquet(path).copy()
    df["date"] = pd.to_datetime(df["date"])
    df["interest"] = df["value"].astype(float)
    df["state"] = df["state"].astype(str).str.replace("US-", "", regex=False)
    df["geo"] = df["state"].map(lambda s: "US" if s == "US" else f"US-{s}")
    df["collection_time"] = ""
    df["collection_run"] = kind
    df["timeframe"] = "today 3-m"
    df["source_agent"] = "gemini"
    df["source_file"] = str(path)
    df["source_kind"] = kind
    return df[
        ["date", "state", "geo", "term", "category", "interest", "collection_time", "collection_run", "timeframe", "source_agent", "source_kind", "source_file"]
    ]


def discover_sources() -> list[pd.DataFrame]:
    frames: list[pd.DataFrame] = []

    # Shared/base
    frames.append(normalize_shared_base(PROJECT / "data" / "raw" / "trends" / "trends_2026-03-19.parquet"))

    # Codex
    codex_path = ROOT / "data" / "raw" / "r2_new_terms_2026-03-20.parquet"
    if codex_path.exists():
        frames.append(normalize_codex(codex_path))

    # Kimi - use non-nested unique files only
    kimi_full = PROJECT / "agents" / "kimi-k2.5" / "data" / "raw" / "trends" / "trends_full_2026-03-19.parquet"
    if kimi_full.exists():
        frames.append(normalize_kimi(kimi_full, "kimi_full_panel"))
    kimi_supp = PROJECT / "agents" / "kimi-k2.5" / "data" / "raw" / "trends_supplemental" / "trends_supplemental_2026-03-20.parquet"
    if kimi_supp.exists():
        frames.append(normalize_kimi(kimi_supp, "kimi_supplemental"))
    kimi_realistic = PROJECT / "agents" / "kimi-k2.5" / "agents" / "kimi-k2.5" / "data" / "raw" / "trends_independent" / "trends_realistic_2026-03-19.parquet"
    if kimi_realistic.exists():
        frames.append(normalize_kimi(kimi_realistic, "kimi_realistic_independent"))

    # Gemini
    gemini_full = PROJECT / "agents" / "gemini" / "agents" / "gemini" / "data" / "raw" / "trends" / "trends_full_2026-03-19.parquet"
    if gemini_full.exists():
        frames.append(normalize_gemini(gemini_full, "gemini_full_panel"))
    gemini_extra = PROJECT / "agents" / "gemini" / "agents" / "gemini" / "data" / "raw" / "trends" / "trends_colloquial_extra_2026-03-20_0048.parquet"
    if gemini_extra.exists():
        frames.append(normalize_gemini(gemini_extra, "gemini_colloquial_extra"))

    return frames


def source_priority(kind: str) -> int:
    priorities = {
        "codex_new_terms": 100,
        "shared_base": 90,
        "base_full_panel": 90,
        "kimi_supplemental": 80,
        "gemini_colloquial_extra": 75,
        "kimi_realistic_independent": 70,
        "kimi_full_panel": 60,
        "gemini_full_panel": 50,
    }
    return priorities.get(kind, 10)


def main() -> None:
    frames = discover_sources()
    union = pd.concat(frames, ignore_index=True)
    union["priority"] = union["source_kind"].map(source_priority)
    union["record_key"] = (
        union["date"].dt.strftime("%Y-%m-%d")
        + "|"
        + union["state"].astype(str)
        + "|"
        + union["term"].astype(str)
    )
    union["canonical_built_at"] = now_iso()

    union_out = PROCESSED / "canonical_union_all_agents.parquet"
    union.to_parquet(union_out, index=False)

    dedup = (
        union.sort_values(
            ["record_key", "priority", "collection_time", "source_agent"],
            ascending=[True, False, False, True],
        )
        .drop_duplicates(subset=["record_key"], keep="first")
        .drop(columns=["record_key"])
    )
    canonical_out = PROCESSED / "canonical_study_dataset.parquet"
    dedup.to_parquet(canonical_out, index=False)

    duplicates = union.groupby("record_key").size().reset_index(name="n_sources")
    dup_rows = duplicates[duplicates["n_sources"] > 1]

    metadata = {
        "created_at": now_iso(),
        "union_rows": int(union.shape[0]),
        "canonical_rows": int(dedup.shape[0]),
        "unique_terms_union": int(union["term"].nunique()),
        "unique_terms_canonical": int(dedup["term"].nunique()),
        "source_counts_union": union.groupby(["source_agent", "source_kind"]).size().reset_index(name="rows").to_dict(orient="records"),
        "duplicate_record_keys": int(dup_rows.shape[0]),
        "dedupe_rule": "One canonical row per date-state-term. Keep highest source priority, then latest collection_time, then source_agent lexical order.",
        "priority_order": {
            "codex_new_terms": 100,
            "shared_base/base_full_panel": 90,
            "kimi_supplemental": 80,
            "gemini_colloquial_extra": 75,
            "kimi_realistic_independent": 70,
            "kimi_full_panel": 60,
            "gemini_full_panel": 50
        },
        "files": {
            "union": str(union_out),
            "canonical": str(canonical_out)
        }
    }
    (PROCESSED / "canonical_dataset_metadata.json").write_text(json.dumps(metadata, indent=2))
    dup_rows.to_csv(PROCESSED / "canonical_duplicate_keys.csv", index=False)


if __name__ == "__main__":
    main()
