#!/usr/bin/env python3
"""
Visualization Generation for VibePoll-2026

CommDAAF v1.0 - EXPLORATORY Tier
Generates descriptive figures for the study.

Outputs:
- state_issue_heatmap.png
- term_timeseries.png
- battleground_vs_control.png
- vibe_index_timeseries.png
"""

import json
import logging
from datetime import datetime
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
LOG_DIR = PROJECT_ROOT / "logs"

# State classifications
BATTLEGROUND_STATES = ['PA', 'MI', 'WI', 'AZ', 'GA', 'NV', 'NC']
CONTROL_STATES = ['CA', 'TX', 'OH']
WATCH_STATES = ['ME', 'NH', 'MN']

# Key events for annotation (March 2026 context)
KEY_EVENTS = [
    ('2026-02-28', 'Iran War\nBegins'),
    ('2026-03-01', 'Epstein Files\nReleased'),
    ('2026-03-10', 'ICE Phase 2\nAnnounced'),
]

# Setup
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


def load_data():
    """Load processed data files."""
    trends = pd.read_parquet(PROCESSED_DIR / "trends_normalized.parquet")
    salience = pd.read_csv(PROCESSED_DIR / "issue_salience.csv")
    vibe = pd.read_csv(PROCESSED_DIR / "vibe_indices.csv")

    # Convert dates
    trends['date'] = pd.to_datetime(trends['date'])
    salience['date'] = pd.to_datetime(salience['date'])
    vibe['date'] = pd.to_datetime(vibe['date'])

    return trends, salience, vibe


def create_state_issue_heatmap(trends: pd.DataFrame, output_path: Path):
    """Create heatmap of issue salience by state."""
    logger.info("Creating state-issue heatmap...")

    # Filter to weighted categories
    categories = ['economy', 'immigration', 'iran_war', 'ai_jobs', 'political', 'epstein']
    df = trends[trends['category'].isin(categories)].copy()

    # Calculate mean salience per state-category
    heatmap_data = df.groupby(['state', 'category'])['z_combined'].mean().unstack()

    # Reorder states: battleground, control, watch
    state_order = BATTLEGROUND_STATES + CONTROL_STATES + WATCH_STATES
    state_order = [s for s in state_order if s in heatmap_data.index]
    heatmap_data = heatmap_data.loc[state_order]

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        heatmap_data,
        cmap='RdYlBu_r',
        center=0,
        annot=True,
        fmt='.2f',
        linewidths=0.5,
        ax=ax,
        cbar_kws={'label': 'Mean Z-Score (Issue Salience)'}
    )

    # Add state type separators
    ax.axhline(y=len(BATTLEGROUND_STATES), color='black', linewidth=2)
    ax.axhline(y=len(BATTLEGROUND_STATES) + len(CONTROL_STATES), color='black', linewidth=2)

    # Labels
    ax.set_title('Issue Salience by State\nVibePoll-2026 (Dec 2025 - Mar 2026)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Issue Category', fontsize=12)
    ax.set_ylabel('State', fontsize=12)

    # Add annotations for state types
    ax.text(-0.5, len(BATTLEGROUND_STATES)/2, 'Battleground', ha='right', va='center',
            fontsize=10, fontweight='bold', rotation=90)
    ax.text(-0.5, len(BATTLEGROUND_STATES) + len(CONTROL_STATES)/2, 'Control', ha='right', va='center',
            fontsize=10, fontweight='bold', rotation=90)
    ax.text(-0.5, len(BATTLEGROUND_STATES) + len(CONTROL_STATES) + len(WATCH_STATES)/2, 'Watch', ha='right', va='center',
            fontsize=10, fontweight='bold', rotation=90)

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"Saved: {output_path}")


def create_term_timeseries(trends: pd.DataFrame, output_path: Path):
    """Create time series of top terms with event annotations."""
    logger.info("Creating term time series...")

    # Select top terms by mean interest
    top_terms = trends.groupby('term')['interest'].mean().nlargest(8).index.tolist()

    # Filter to top terms and aggregate across states
    df = trends[trends['term'].isin(top_terms)].copy()
    ts = df.groupby(['date', 'term'])['interest'].mean().reset_index()

    # Create figure
    fig, ax = plt.subplots(figsize=(14, 8))

    for term in top_terms:
        term_data = ts[ts['term'] == term]
        ax.plot(term_data['date'], term_data['interest'], label=term, linewidth=2, alpha=0.8)

    # Add event annotations
    for event_date, event_label in KEY_EVENTS:
        try:
            event_dt = pd.to_datetime(event_date)
            if event_dt >= ts['date'].min() and event_dt <= ts['date'].max():
                ax.axvline(x=event_dt, color='red', linestyle='--', alpha=0.7)
                ax.text(event_dt, ax.get_ylim()[1] * 0.95, event_label,
                       ha='center', va='top', fontsize=9, color='red',
                       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        except:
            pass

    # Formatting
    ax.set_title('Top Search Terms Over Time\nVibePoll-2026', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Search Interest (0-100)', fontsize=12)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    plt.xticks(rotation=45)

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"Saved: {output_path}")


def create_battleground_vs_control(trends: pd.DataFrame, output_path: Path):
    """Compare issue salience between battleground and control states."""
    logger.info("Creating battleground vs control comparison...")

    # Classify states
    trends['state_type'] = trends['state'].apply(
        lambda x: 'Battleground' if x in BATTLEGROUND_STATES
        else 'Control' if x in CONTROL_STATES
        else 'Watch'
    )

    # Filter to main categories
    categories = ['economy', 'immigration', 'iran_war', 'ai_jobs', 'political']
    df = trends[trends['category'].isin(categories)].copy()

    # Calculate mean salience by state type and category
    comparison = df.groupby(['state_type', 'category'])['z_combined'].mean().unstack()

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))

    x = np.arange(len(categories))
    width = 0.25

    for i, state_type in enumerate(['Battleground', 'Control', 'Watch']):
        if state_type in comparison.index:
            values = [comparison.loc[state_type, cat] if cat in comparison.columns else 0 for cat in categories]
            ax.bar(x + i*width, values, width, label=state_type, alpha=0.8)

    ax.set_title('Issue Salience: Battleground vs Control States\nVibePoll-2026', fontsize=14, fontweight='bold')
    ax.set_xlabel('Issue Category', fontsize=12)
    ax.set_ylabel('Mean Z-Score', fontsize=12)
    ax.set_xticks(x + width)
    ax.set_xticklabels([c.replace('_', ' ').title() for c in categories], rotation=45, ha='right')
    ax.legend()
    ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"Saved: {output_path}")


def create_vibe_index_timeseries(vibe: pd.DataFrame, output_path: Path):
    """Create Vibe Index time series for all states."""
    logger.info("Creating Vibe Index time series...")

    fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    state_groups = [
        ('Battleground States', BATTLEGROUND_STATES, 'tab:blue'),
        ('Control States', CONTROL_STATES, 'tab:orange'),
        ('Watch States', WATCH_STATES, 'tab:green')
    ]

    for ax, (title, states, color) in zip(axes, state_groups):
        for state in states:
            state_data = vibe[vibe['state'] == state].sort_values('date')
            if len(state_data) > 0:
                ax.plot(state_data['date'], state_data['vibe_index_7d'],
                       label=state, linewidth=2, alpha=0.7)

        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_ylabel('Vibe Index (7-day avg)', fontsize=10)
        ax.legend(loc='upper left', ncol=len(states), fontsize=9)
        ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

        # Add event lines
        for event_date, event_label in KEY_EVENTS:
            try:
                event_dt = pd.to_datetime(event_date)
                if event_dt >= vibe['date'].min() and event_dt <= vibe['date'].max():
                    ax.axvline(x=event_dt, color='red', linestyle='--', alpha=0.5)
            except:
                pass

    axes[-1].set_xlabel('Date', fontsize=12)
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    axes[-1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    plt.xticks(rotation=45)

    fig.suptitle('Vibe Index Over Time by State Type\nVibePoll-2026', fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)

    logger.info(f"Saved: {output_path}")


def main():
    """Generate all figures."""
    logger.info("=" * 60)
    logger.info("Generating Figures for VibePoll-2026")
    logger.info("=" * 60)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data
    trends, salience, vibe = load_data()
    logger.info(f"Loaded: {len(trends)} trends, {len(salience)} salience, {len(vibe)} vibe records")

    # Generate figures
    create_state_issue_heatmap(trends, OUTPUT_DIR / "state_issue_heatmap.png")
    create_term_timeseries(trends, OUTPUT_DIR / "term_timeseries.png")
    create_battleground_vs_control(trends, OUTPUT_DIR / "battleground_vs_control.png")
    create_vibe_index_timeseries(vibe, OUTPUT_DIR / "vibe_index_timeseries.png")

    logger.info("=" * 60)
    logger.info("ALL FIGURES GENERATED")
    logger.info("=" * 60)

    print("\n" + "=" * 60)
    print("FIGURES GENERATED")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print("\nFiles:")
    for f in OUTPUT_DIR.glob("*.png"):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
