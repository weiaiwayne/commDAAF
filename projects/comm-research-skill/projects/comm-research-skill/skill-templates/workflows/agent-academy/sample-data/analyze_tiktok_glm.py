#!/usr/bin/env python3
"""
CommDAAF Analysis: Chinese Digital Diplomacy TikTok Dataset
GLM Model Analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime
import pyreadr
import json
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
print("Loading TikTok dataset...")
data = pyreadr.read_r('cn_digital_diplomacy_tiktok.rda')

# Explore available dataframes
print("\nAvailable dataframes:")
for key in data.keys():
    df = data[key]
    print(f"  {key}: {len(df)} rows × {len(df.columns)} cols")

# Get individual datasets
xinjiang = data['xinjiang']
china = data['china']
taiwan = data['taiwan']
hk = data['hk']
xinjiang_comments = data['xinjiang_comments']

print("\n" + "="*80)
print("DATASET OVERVIEW")
print("="*80)

# Basic info
datasets = {
    'Xinjiang': xinjiang,
    'China': china,
    'Taiwan': taiwan,
    'Hong Kong': hk,
    'Xinjiang Comments': xinjiang_comments
}

for name, df in datasets.items():
    print(f"\n{name}:")
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {list(df.columns)[:10]}...")  # Show first 10 columns
    print(f"  Shape: {df.shape}")

# Analyze video engagement
print("\n" + "="*80)
print("RQ1: STATE MEDIA VS ORGANIC CREATORS ENGAGEMENT PATTERNS")
print("="*80)

def analyze_engagement(df, topic_name):
    """Analyze engagement patterns"""
    results = {}

    # Check available columns
    cols = df.columns.tolist()
    print(f"\n{topic_name} - Available columns: {cols}")

    # Try common engagement metric names
    view_col = None
    like_col = None
    comment_col = None
    share_col = None

    for col in cols:
        col_lower = col.lower()
        if 'play' in col_lower or 'view' in col_lower:
            view_col = col
        if 'like' in col_lower:
            like_col = col
        if 'comment' in col_lower and 'count' in col_lower:
            comment_col = col
        if 'share' in col_lower:
            share_col = col

    results['view_col'] = view_col
    results['like_col'] = like_col
    results['comment_col'] = comment_col
    results['share_col'] = share_col

    # Calculate stats
    if view_col:
        results['total_views'] = df[view_col].sum()
        results['mean_views'] = df[view_col].mean()
        results['median_views'] = df[view_col].median()
        results['max_views'] = df[view_col].max()

    if like_col:
        results['total_likes'] = df[like_col].sum()
        results['mean_likes'] = df[like_col].mean()
        results['median_likes'] = df[like_col].median()

    if comment_col:
        results['total_comments'] = df[comment_col].sum()
        results['mean_comments'] = df[comment_col].mean()

    # Check for state media accounts
    author_col = None
    for col in cols:
        if 'author' in col.lower() or 'user' in col.lower() or 'nickname' in col.lower():
            author_col = col
            break

    results['author_col'] = author_col

    if author_col:
        # Identify People's Daily or similar state media
        state_keywords = ['people', 'daily', 'cctv', 'china daily', 'xinhua', 'cgtn']
        df['is_state'] = df[author_col].str.lower().str.contains('|'.join(state_keywords), na=False)
        state_count = df['is_state'].sum()
        results['state_media_count'] = state_count
        results['state_media_pct'] = (state_count / len(df)) * 100

        if state_count > 0 and view_col:
            state_views = df[df['is_state']][view_col].sum()
            organic_views = df[~df['is_state']][view_col].sum()
            results['state_views'] = state_views
            results['organic_views'] = organic_views
            results['state_avg_views'] = df[df['is_state']][view_col].mean()
            results['organic_avg_views'] = df[~df['is_state']][view_col].mean()

    return results, df, author_col, view_col

# Analyze each topic
engagement_results = {}
for topic_name, df in [('Xinjiang', xinjiang), ('China', china), ('Taiwan', taiwan), ('HK', hk)]:
    print(f"\n--- {topic_name} ---")
    results, df_upd, author_col, view_col = analyze_engagement(df, topic_name)
    engagement_results[topic_name] = (results, df_upd, author_col, view_col)

    if 'total_views' in results:
        print(f"  Total Views: {results['total_views']:,.0f}")
        print(f"  Mean Views: {results['mean_views']:,.0f}")
        print(f"  Median Views: {results['median_views']:,.0f}")

    if 'state_media_count' in results:
        print(f"  State Media Videos: {results['state_media_count']} ({results['state_media_pct']:.1f}%)")
        if 'state_avg_views' in results:
            print(f"    State Media Avg Views: {results['state_avg_views']:,.0f}")
            print(f"    Organic Avg Views: {results['organic_avg_views']:,.0f}")
            ratio = results['state_avg_views'] / results['organic_avg_views'] if results['organic_avg_views'] > 0 else 0
            print(f"    Ratio (State/Organic): {ratio:.2f}x")

# RQ2: Coordinated behavior in Xinjiang comments
print("\n" + "="*80)
print("RQ2: COORDINATED BEHAVIOR IN XINJIANG COMMENTS")
print("="*80)

print(f"\nXinjiang Comments Dataset:")
print(f"  Total comments: {len(xinjiang_comments):,}")
print(f"  Columns: {list(xinjiang_comments.columns)}")

# Check for duplicates
cols = xinjiang_comments.columns.tolist()
text_col = None
author_col = None
time_col = None

for col in cols:
    col_lower = col.lower()
    if 'text' in col_lower or 'content' in col_lower:
        text_col = col
    if 'author' in col_lower or 'user' in col_lower:
        author_col = col
    if 'time' in col_lower or 'date' in col_lower:
        time_col = col

print(f"\nDetected columns:")
print(f"  Text: {text_col}")
print(f"  Author: {author_col}")
print(f"  Time: {time_col}")

coord_analysis = {}

# Duplicate analysis
if text_col:
    exact_duplicates = xinjiang_comments[text_col].duplicated().sum()
    coord_analysis['exact_duplicates'] = exact_duplicates
    coord_analysis['duplicate_pct'] = (exact_duplicates / len(xinjiang_comments)) * 100
    print(f"\nExact duplicate comments: {exact_duplicates:,} ({coord_analysis['duplicate_pct']:.2f}%)")

    # Get most common comments
    comment_counts = xinjiang_comments[text_col].value_counts()
    coord_analysis['top_5_comments'] = comment_counts.head(5).to_dict()
    print(f"\nTop 5 most repeated comments:")
    for i, (comment, count) in enumerate(comment_counts.head(5).items(), 1):
        print(f"  {i}. '{comment[:80]}...' ({count}x)")

# Author analysis
if author_col:
    author_counts = xinjiang_comments[author_col].value_counts()
    coord_analysis['unique_authors'] = len(author_counts)
    coord_analysis['top_authors'] = author_counts.head(10).to_dict()

    print(f"\nAuthor Analysis:")
    print(f"  Unique commenters: {len(author_counts):,}")

    # Check for suspicious patterns
    top_5_authors = author_counts.head(5)
    top_5_total = top_5_authors.sum()
    print(f"  Top 5 authors: {top_5_total} comments ({(top_5_total/len(xinjiang_comments)*100):.1f}%)")
    print(f"\n  Top 10 commenters:")
    for i, (author, count) in enumerate(author_counts.head(10).items(), 1):
        pct = (count / len(xinjiang_comments)) * 100
        print(f"    {i}. {author}: {count} ({pct:.2f}%)")

    # Flag suspicious: >1% of all comments from single author
    suspicious_authors = author_counts[author_counts > len(xinjiang_comments) * 0.01]
    coord_analysis['suspicious_authors'] = len(suspicious_authors)
    if len(suspicious_authors) > 0:
        print(f"\n  ⚠️ FLAG: {len(suspicious_authors)} authors with >1% of all comments")

# Timing analysis (if available)
if time_col:
    try:
        xinjiang_comments['datetime'] = pd.to_datetime(xinjiang_comments[time_col])
        xinjiang_comments['hour'] = xinjiang_comments['datetime'].dt.hour

        hourly_counts = xinjiang_comments['hour'].value_counts().sort_index()
        coord_analysis['hourly_distribution'] = hourly_counts.to_dict()

        print(f"\nTemporal Distribution (Hourly):")
        for hour, count in hourly_counts.items():
            print(f"  {hour:02d}:00: {count:5d} comments")

        # Check for clustering
        peak_hour = hourly_counts.idxmax()
        peak_count = hourly_counts.max()
        avg_hourly = hourly_counts.mean()
        peak_ratio = peak_count / avg_hourly if avg_hourly > 0 else 0

        coord_analysis['peak_hour'] = peak_hour
        coord_analysis['peak_ratio'] = peak_ratio

        if peak_ratio > 3:
            print(f"\n  ⚠️ FLAG: Peak hour ({peak_hour}:00) has {peak_ratio:.1f}x average hourly volume")

    except Exception as e:
        print(f"\nCould not parse timestamps: {e}")

# RQ3: Engagement disparity analysis
print("\n" + "="*80)
print("RQ3: ENGAGEMENT DISPARITY ANALYSIS")
print("="*80)

print("\nComparison across topics:")
print(f"{'Topic':<15} {'Videos':<10} {'Total Views':<15} {'Avg Views':<15} {'Median Views':<15}")
print("-" * 70)

for topic_name, (results, df, _, _) in engagement_results.items():
    if 'total_views' in results:
        print(f"{topic_name:<15} {len(df):<10,} {results['total_views']:>13,.0f} {results['mean_views']:>13,.0f} {results['median_views']:>13,.0f}")

# Calculate ratios
china_views = engagement_results['China'][0].get('total_views', 0)
xinjiang_views = engagement_results['Xinjiang'][0].get('total_views', 0)
taiwan_views = engagement_results['Taiwan'][0].get('total_views', 0)
hk_views = engagement_results['HK'][0].get('total_views', 0)

if xinjiang_views > 0:
    china_xinjiang_ratio = china_views / xinjiang_views
    print(f"\n📊 China vs Xinjiang views ratio: {china_xinjiang_ratio:.1f}x")
    print(f"   China has {(china_xinjiang_ratio-1)*100:.0f}% more total views")

# RQ4: Top accounts analysis
print("\n" + "="*80)
print("RQ4: TOP ACCOUNTS BY TOPIC")
print("="*80)

for topic_name, (results, df, author_col, view_col) in engagement_results.items():
    if author_col and view_col:
        print(f"\n--- {topic_name} ---")

        # Top 10 accounts by views
        top_accounts = df.groupby(author_col)[view_col].sum().sort_values(ascending=False).head(10)

        for i, (account, views) in enumerate(top_accounts.items(), 1):
            views_str = f"{views:,.0f}"
            # Check if state media
            is_state = any(kw in str(account).lower() for kw in ['people', 'daily', 'cctv', 'china daily', 'xinhua', 'cgtn', 'gov'])
            state_flag = " [STATE MEDIA]" if is_state else ""
            print(f"  {i}. {account[:40]:40s}: {views_str:>15s}{state_flag}")

# RQ5: Temporal analysis
print("\n" + "="*80)
print("RQ5: TEMPORAL PATTERNS AND EVENT ALIGNMENT")
print("="*80)

for topic_name, (results, df, author_col, view_col) in engagement_results.items():
    # Try to find time column
    time_col = None
    for col in df.columns:
        col_lower = col.lower()
        if 'time' in col_lower or 'date' in col_lower or 'create' in col_lower:
            time_col = col
            break

    if time_col:
        try:
            print(f"\n--- {topic_name} ---")
            df['datetime'] = pd.to_datetime(df[time_col])

            print(f"Date range: {df['datetime'].min()} to {df['datetime'].max()}")

            # Daily activity
            df['date'] = df['datetime'].dt.date
            daily_counts = df.groupby('date').size()

            if len(daily_counts) > 0:
                peak_day = daily_counts.idxmax()
                peak_count = daily_counts.max()
                avg_daily = daily_counts.mean()

                print(f"Peak day: {peak_day} ({peak_count} videos)")
                print(f"Average daily videos: {avg_daily:.1f}")

                # Check for spikes
                if len(daily_counts) > 1:
                    daily_std = daily_counts.std()
                    if daily_std > 0:
                        z_scores = (daily_counts - avg_daily) / daily_std
                        spike_days = daily_counts[z_scores > 2]

                        if len(spike_days) > 0:
                            print(f"\n  ⚠️ SIGNIFICANT SPIKES (>2σ):")
                            for day, count in spike_days.items():
                                print(f"    {day}: {count} videos (z={(count-avg_daily)/daily_std:.1f})")

        except Exception as e:
            print(f"\n{topic_name}: Could not analyze temporal data - {e}")
    else:
        print(f"\n{topic_name}: No time column found")

# Critical Checks
print("\n" + "="*80)
print("CRITICAL CHECKS (CommDAAF Framework)")
print("="*80)

critical_flags = []

# Check 1: Peak/Trough Ratio
view_totals = {}
for topic, (results, df, _, _) in engagement_results.items():
    if 'total_views' in results:
        view_totals[topic] = results['total_views']

if view_totals:
    max_views = max(view_totals.values())
    min_views = min(view_totals.values())
    peak_trough_ratio = max_views / min_views if min_views > 0 else 0

    print(f"\n🔍 PEAK/TROUGH RATIO CHECK")
    print(f"   Peak (China): {max_views:,.0f}")
    print(f"   Trough (Xinjiang): {min_views:,.0f}")
    print(f"   Ratio: {peak_trough_ratio:.1f}x")

    if peak_trough_ratio > 4:
        flag = f"⚠️ FLAG: Peak/trough ratio {peak_trough_ratio:.1f}x exceeds 4:1 threshold"
        print(f"   {flag}")
        critical_flags.append(flag)

# Check 2: Duplicate content (coordination indicator)
if 'duplicate_pct' in coord_analysis:
    print(f"\n🔍 DUPLICATE CONTENT CHECK")
    print(f"   Exact duplicates: {coord_analysis['exact_duplicates']:,} ({coord_analysis['duplicate_pct']:.2f}%)")

    if coord_analysis['duplicate_pct'] > 5:
        flag = f"⚠️ FLAG: {coord_analysis['duplicate_pct']:.2f}% duplicate comments exceeds 5% threshold"
        print(f"   {flag}")
        critical_flags.append(flag)
        print(f"   → Indicates potential coordinated behavior")

# Check 3: Author concentration
if 'unique_authors' in coord_analysis and len(xinjiang_comments) > 0:
    herfindahl = sum((count/len(xinjiang_comments))**2 for count in coord_analysis.get('top_authors', {}).values())

    print(f"\n🔍 AUTHOR CONCENTRATION CHECK")
    print(f"   Unique authors: {coord_analysis['unique_authors']:,}")
    print(f"   Top 10 authors concentration: {herfindahl:.4f}")

    if herfindahl > 0.1:
        flag = f"⚠️ FLAG: High author concentration (H={herfindahl:.4f})"
        print(f"   {flag}")
        critical_flags.append(flag)

# Check 4: State media presence
print(f"\n🔍 STATE MEDIA PRESENCE CHECK")
for topic, (results, df, _, _) in engagement_results.items():
    if 'state_media_count' in results:
        print(f"   {topic}: {results['state_media_count']} videos ({results['state_media_pct']:.1f}%)")

        if results['state_media_pct'] > 20:
            flag = f"⚠️ FLAG: {topic} has {results['state_media_pct']:.1f}% state media content"
            critical_flags.append(flag)

print(f"\n" + "="*80)
print("CRITICAL FLAGS SUMMARY")
print("="*80)
if critical_flags:
    for flag in critical_flags:
        print(flag)
else:
    print("✓ No critical flags detected")

# Save findings
findings = {
    'metadata': {
        'analysis_date': datetime.now().isoformat(),
        'dataset': 'cn_digital_diplomacy_tiktok.rda',
        'model': 'GLM'
    },
    'engagement_analysis': {
        topic: results for topic, (results, _, _, _) in engagement_results.items()
    },
    'coordination_analysis': coord_analysis,
    'view_disparity': {
        'china_views': china_views,
        'xinjiang_views': xinjiang_views,
        'taiwan_views': taiwan_views,
        'hk_views': hk_views,
        'china_xinjiang_ratio': china_views / xinjiang_views if xinjiang_views > 0 else None
    },
    'critical_flags': critical_flags
}

with open('tiktok_analysis_findings.json', 'w') as f:
    json.dump(findings, f, indent=2, default=str)

print(f"\n✓ Analysis complete. Findings saved to tiktok_analysis_findings.json")
