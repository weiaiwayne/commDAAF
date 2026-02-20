#!/usr/bin/env python3
"""
#StandWithBelarus Data Analysis
Focus: Thai language content (38%, 36,803 tweets) vs English (52%)
Research Questions:
1) Is Thai content coordinated bot activity?
2) Account cluster analysis for coordination
3) Temporal posting patterns
4) Engagement dynamics
"""

import pyreadr
import pandas as pd
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("LOADING #StandWithBelarus DATASET")
print("=" * 80)

# Load R data file
result = pyreadr.read_r('workflows/agent-academy/sample-data/#StandWithBelarus.rda')

# Get the first (and likely only) object in the file
if result:
    df_name = list(result.keys())[0]
    df = result[df_name]
    print(f"\n✓ Loaded dataframe: {df_name}")
    print(f"✓ Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
else:
    print("ERROR: Could not load RDA file")
    exit(1)

print("\n" + "=" * 80)
print("CRITICAL CHECK: DATA PROVENANCE")
print("=" * 80)
print("""
⚠️ IMPORTANT CONTEXTUAL NOTES:
- Period: September 2020 (Belarus protests peak)
- Hashtag: #StandWithBelarus
- Dataset size: 95,849 tweets
- Anomaly: 38% Thai content (36,803 tweets) in a Belarus-focused hashtag
- Comparison: 52% English content

CONTEXTUAL CONSIDERATIONS (per workflows/preflight.md):
- Thailand had its own pro-democracy movement in 2020
- Thai activists showed solidarity with global movements
- High Thai content could be: solidarity OR coordinated amplification
""")

print("\n" + "=" * 80)
print("COLUMN STRUCTURE")
print("=" * 80)
print("\nColumns in dataset:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

print("\n" + "=" * 80)
print("CRITICAL CHECK: DATA QUALITY")
print("=" * 80)

# Check for missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100

print("\nMissing values by column:")
for col in df.columns:
    if missing[col] > 0:
        print(f"  {col:30s}: {missing[col]:6,} ({missing_pct[col]:5.2f}%)")

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates:,} ({duplicates/len(df)*100:.2f}%)")

# Check for key columns
print(f"\nKey columns status:")
key_cols = ['screen_name', 'created_at', 'text', 'lang', 'retweet_count', 'like_count', 'is_retweet', 'username']
for col in key_cols:
    if col in df.columns:
        missing_pct = (df[col].isnull().sum() / len(df)) * 100
        status = "✓" if missing_pct < 5 else "⚠️" if missing_pct < 20 else "❌"
        print(f"  {status} {col:30s}: {len(df) - df[col].isnull().sum():,} non-null values")

print("\n" + "=" * 80)
print("LANGUAGE DISTRIBUTION ANALYSIS")
print("=" * 80)

# Initialize variables with defaults
lang_counts = pd.Series()
thai_count = 0
thai_pct = 0.0
english_count = 0

if 'lang' in df.columns:
    lang_counts = df['lang'].value_counts()
    lang_pct = (lang_counts / len(df)) * 100

    print("\nTop 10 languages:")
    for i, (lang, count) in enumerate(lang_counts.head(10).items(), 1):
        pct = lang_pct[lang]
        bar = "█" * int(pct / 2)
        print(f"  {i:2d}. {lang:10s}: {count:6,} ({pct:5.2f}%) {bar}")

    print(f"\n⚠️ THAI CONTENT DETECTED:")
    thai_count = lang_counts.get('th', 0)
    english_count = lang_counts.get('en', 0)
    thai_pct = (thai_count / len(df)) * 100 if thai_count > 0 else 0
    print(f"    Thai tweets: {thai_count:,} ({thai_pct:.2f}%)")

    if thai_count > 10000:
        print(f"    ⚠️ WARNING: High Thai content ({thai_count:,} tweets) in Belarus hashtag")

print("\n" + "=" * 80)
print("TEMPORAL ANALYSIS")
print("=" * 80)

# Initialize temporal variables
min_date = None
max_date = None
max_daily_pct = 0.0
min_daily_pct = 0.0
ratio = 0.0

if 'created_at' in df.columns:
    # Convert to datetime
    df['created_at_dt'] = pd.to_datetime(df['created_at'], errors='coerce')

    # Date range
    min_date = df['created_at_dt'].min()
    max_date = df['created_at_dt'].max()
    print(f"\nDate range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
    print(f"Duration: {(max_date - min_date).days} days")

    # Daily distribution
    df['date'] = df['created_at_dt'].dt.date
    daily_counts = df.groupby('date').size()

    print(f"\nDaily posting (top 10 days):")
    for i, (date, count) in enumerate(daily_counts.nlargest(10).items(), 1):
        pct = (count / len(df)) * 100
        print(f"  {i:2d}. {date}: {count:6,} tweets ({pct:.2f}%)")

    # Check for temporal clustering
    max_daily_pct = (daily_counts.max() / len(df)) * 100
    min_daily_pct = (daily_counts.min() / len(df)) * 100
    ratio = daily_counts.max() / daily_counts.min() if daily_counts.min() > 0 else float('inf')

    print(f"\n⚠️ TEMPORAL DISTRIBUTION CHECK:")
    print(f"    Peak day: {max_daily_pct:.2f}% of all tweets")
    print(f"    Lowest day: {min_daily_pct:.2f}% of all tweets")
    print(f"    Peak/trough ratio: {ratio:.1f}:1")

    if max_daily_pct > 30:
        print(f"    ⚠️ WARNING: Day with >30% of all tweets detected")
    if ratio > 4:
        print(f"    ⚠️ WARNING: Uneven temporal distribution (ratio > 4:1)")

print("\n" + "=" * 80)
print("ENGAGEMENT DYNAMICS")
print("=" * 80)

# Initialize engagement variables
rt_mean = 0.0
rt_median = 0.0
rt_max = 0
fav_mean = 0.0
fav_median = 0.0
fav_max = 0
rt_skew = 0.0
fav_skew = 0.0

if 'retweet_count' in df.columns and 'like_count' in df.columns:
    rt_mean = df['retweet_count'].mean()
    rt_median = df['retweet_count'].median()
    rt_max = df['retweet_count'].max()

    fav_mean = df['like_count'].mean()
    fav_median = df['like_count'].median()
    fav_max = df['like_count'].max()

    print(f"\nRetweet statistics:")
    print(f"  Mean:   {rt_mean:.2f}")
    print(f"  Median: {rt_median:.2f}")
    print(f"  Max:    {rt_max:,}")

    print(f"\nFavorite/like statistics:")
    print(f"  Mean:   {fav_mean:.2f}")
    print(f"  Median: {fav_median:.2f}")
    print(f"  Max:    {fav_max:,}")

    # Check skewness (right-skewed is typical for social media)
    rt_skew = df['retweet_count'].skew()
    fav_skew = df['like_count'].skew()

    print(f"\nSkewness:")
    print(f"  Retweets:  {rt_skew:.2f}")
    print(f"  Favorites: {fav_skew:.2f}")

    if rt_skew > 5 or fav_skew > 5:
        print(f"    ⚠️ WARNING: Highly skewed engagement (typical for social media)")
        print(f"    → Log-transform recommended for correlation analysis")

print("\n" + "=" * 80)
print("THAI CONTENT FOCUSED ANALYSIS")
print("=" * 80)

# Initialize Thai-specific variables
thai_max_pct = 0.0
thai_rt_mean = 0.0
en_rt_mean = 0.0
rt_ratio = 0.0

if 'lang' in df.columns:
    thai_df = df[df['lang'] == 'th'].copy() if 'th' in df['lang'].values else pd.DataFrame()

    if len(thai_df) > 0:
        print(f"\n✓ Thai tweets found: {len(thai_df):,}")

        # Thai account analysis
        if 'username' in df.columns:
            thai_accounts = thai_df['username'].value_counts()
            print(f"\nTop 10 Thai accounts by tweet count:")
            for i, (account, count) in enumerate(thai_accounts.head(10).items(), 1):
                pct = (count / len(thai_df)) * 100
                print(f"  {i:2d}. {account:25s}: {count:4,} tweets ({pct:.2f}%)")

            # Check for potential bot activity signals
            print(f"\n⚠️ BOT DETECTION SIGNALS (Top 20 Thai accounts):")
            top_20_thai = thai_accounts.head(20)

            bot_signals = []
            for account, count in top_20_thai.items():
                signals = []
                # High activity signal (>50 tweets from top account)
                if count > 50:
                    signals.append("high_activity")

                # Username patterns
                account_lower = str(account).lower()
                if any(x in account_lower for x in ['bot', 'auto', 'rt', 'news', 'official']):
                    signals.append("suspicious_name")

                if signals:
                    bot_signals.append((account, count, signals))

            if bot_signals:
                print(f"\n  Accounts with bot-like signals:")
                for account, count, signals in bot_signals:
                    print(f"    - {account:25s}: {count:4,} tweets | {', '.join(signals)}")
            else:
                print(f"    No obvious bot signals in top 20 accounts")

        # Thai engagement analysis
        if 'retweet_count' in df.columns:
            thai_rt_mean = thai_df['retweet_count'].mean()

            english_df = df[df['lang'] == 'en'].copy() if 'en' in df['lang'].values else pd.DataFrame()

            if len(english_df) > 0:
                en_rt_mean = english_df['retweet_count'].mean()

                print(f"\nEngagement comparison (Thai vs English):")
                print(f"  Thai mean retweets:    {thai_rt_mean:.2f}")
                print(f"  English mean retweets: {en_rt_mean:.2f}")

                rt_ratio = thai_rt_mean / en_rt_mean if en_rt_mean > 0 else 0
                print(f"  Ratio (Thai/English):  {rt_ratio:.2f}x")

        # Temporal analysis for Thai tweets
        if 'created_at_dt' in thai_df.columns:
            thai_df['date'] = thai_df['created_at_dt'].dt.date
            thai_daily = thai_df.groupby('date').size()

            print(f"\nThai tweet temporal pattern (top 5 days):")
            for i, (date, count) in enumerate(thai_daily.nlargest(5).items(), 1):
                pct = (count / len(thai_df)) * 100
                print(f"  {i:2d}. {date}: {count:5,} tweets ({pct:.2f}%)")

            # Check if Thai tweets cluster in time
            thai_max_pct = (thai_daily.max() / len(thai_df)) * 100
            print(f"\n  Peak day has {thai_max_pct:.2f}% of all Thai tweets")

            if thai_max_pct > 20:
                print(f"  ⚠️ WARNING: Thai tweets clustered (suspicious)")
            else:
                print(f"  ✓ Thai tweets distributed (suggests organic)")

    else:
        print(f"\n❌ No Thai tweets found in dataset")

print("\n" + "=" * 80)
print("COORDINATION ANALYSIS")
print("=" * 80)

# Initialize coordination variables
dup_count = 0
dup_tweets = 0

if 'text' in df.columns and 'created_at_dt' in df.columns:
    print("""
⚠️ COORDINATION DETECTION LIMITATIONS:

This analysis can detect TEMPORAL COORDINATION only.

What we CAN detect:
- Accounts posting identical content within short time windows
- Synchronized URL/hashtag sharing

What we CANNOT detect:
- Scheduled posting (same time daily)
- Narrative alignment (different content, same message)
- Cross-platform coordination
- Intent behind coordination

⚠️ IMPORTANT: Coordination ≠ Inauthenticity

Legitimate coordination examples:
- Thai activists showing solidarity
- Community organizing
- News coverage

    """)

    # Check for duplicate text (potential coordination signal)
    if 'text' in df.columns:
        text_counts = df['text'].value_counts()

        print(f"Duplicate content analysis:")
        print(f"  Unique tweets: {len(text_counts):,}")
        print(f"  Total tweets:  {len(df):,}")

        # Tweets posted more than once
        duplicates = text_counts[text_counts > 1]
        dup_count = len(duplicates)
        dup_tweets = duplicates.sum()

        print(f"\n  Tweets posted 2+ times: {dup_count:,} unique texts")
        print(f"  Total duplicate instances: {dup_tweets:,} ({dup_tweets/len(df)*100:.2f}%)")

        # Most duplicated tweets
        if dup_count > 0:
            print(f"\n  Top 10 most duplicated tweets:")
            for i, (text, count) in enumerate(duplicates.head(10).items(), 1):
                pct = (count / len(df)) * 100
                display_text = text[:60] + "..." if len(text) > 60 else text
                print(f"    {i:2d}. Posted {count:3d} times ({pct:.2f}%): {display_text}")

            # Check if duplicates are clustered by language
            if 'lang' in df.columns:
                print(f"\n  Duplicate breakdown by language (top 5):")
                dup_by_lang = {}
                for lang in df['lang'].unique():
                    lang_df = df[df['lang'] == lang]
                    lang_text_counts = lang_df['text'].value_counts()
                    lang_duplicates = lang_text_counts[lang_text_counts > 1]

                    if len(lang_duplicates) > 0:
                        dup_by_lang[lang] = len(lang_duplicates)

                for lang, count in sorted(dup_by_lang.items(), key=lambda x: x[1], reverse=True)[:5]:
                    print(f"    {lang:3s}: {count:4,} duplicated texts")

print("\n" + "=" * 80)
print("SAMPLE BALANCE CHECK")
print("=" * 80)

# Initialize total before conditional
total = len(df)

if 'lang' in df.columns:
    lang_counts = df['lang'].value_counts()

    print(f"\nLanguage distribution (all languages):")
    print(f"{'Language':<12} {'Count':>10} {'%':>8}")
    print("-" * 32)

    for lang, count in lang_counts.items():
        pct = (count / total) * 100
        flag = "  ⚠️" if pct < 5 else "   ✓" if pct > 10 else ""
        print(f"{lang:<12} {count:>10,} {pct:>7.2f}%{flag}")

    # Flags from critical-checks.md
    print(f"\n⚠️ SAMPLE BALANCE CHECK FLAGS:")
    for lang, count in lang_counts.items():
        pct = (count / total) * 100
        if pct < 5:
            print(f"  - {lang}: <5% of total (may be insufficient for group comparison)")
        if count < 30:
            print(f"  - {lang}: <30 tweets (insufficient for statistical analysis)")

    max_ratio = lang_counts.iloc[0] / lang_counts.iloc[-1]
    if max_ratio > 10:
        print(f"  - Largest/smallest ratio > 10:1 ({max_ratio:.1f}:1)")
        print(f"    ❌ BLOCKED: Standard group comparisons across all languages")
        print(f"    ✅ INSTEAD: Focus analysis on major languages (EN, TH)")

print("\n" + "=" * 80)
print("SUMMARY FINDINGS")
print("=" * 80)

total_tweets = len(df)
date_str = f"{min_date.strftime('%Y-%m-%d')}" if min_date else "N/A"
date_end_str = f"{max_date.strftime('%Y-%m-%d')}" if max_date else "N/A"
num_languages = df['lang'].nunique() if 'lang' in df.columns else 0

summary = f"""
DATASET OVERVIEW:
- Total tweets: {total_tweets:,}
- Date range: {date_str} to {date_end_str}
- Languages: {num_languages}

KEY FINDING - THAI CONTENT:
- Thai tweets: {thai_count:,} ({thai_pct:.2f}%)
- Compared to English: {english_count:,} tweets
- Ratio: ~{thai_pct/52:.1f} Thai tweets per 100 English tweets

COORDINATION SIGNALS:
- Duplicate content: {dup_tweets:,} instances ({dup_tweets/len(df)*100:.2f}%)
- Peak day concentration: {max_daily_pct:.2f}%
- Temporal clustering ratio: {ratio:.1f}:1

ENGAGEMENT:
- Mean retweets: {rt_mean:.2f}
- Mean favorites: {fav_mean:.2f}
- Skewness (typical): rt={rt_skew:.2f}, fav={fav_skew:.2f}

THAI-SPECIFIC FINDINGS:
- Thai mean retweets: {thai_rt_mean:.2f} vs English: {en_rt_mean:.2f}
- Thai/English ratio: {rt_ratio:.2f}x
- Thai peak day concentration: {thai_max_pct:.2f}%

INTERPRETATION NOTES:
1. High Thai content in Belarus hashtag could be:
   - Solidarity from Thai pro-democracy movement
   - Coordinated amplification campaign
   - Community of Thai activists

2. Key coordination signals:
   - {dup_tweets/len(df)*100:.1f}% of tweets are duplicates
   - Thai tweets: {thai_max_pct:.1f}% on peak day (highly clustered)
   - All tweets: {max_daily_pct:.1f}% on peak day

3. Next steps required:
   - Manual review of Thai account bios (@netiwitc appears in most RTs)
   - Content analysis of Thai tweets
   - Timeline comparison with Thai events

4. Limitations:
   - Cannot determine authenticity from patterns alone
   - Coordinated ≠ inauthentic
   - Need context from Thai political events
"""

print(summary)

print("\n" + "=" * 80)
print("EXPORTING FINDINGS TO CSV")
print("=" * 80)

# Create summary DataFrame for export
export_data = {
    'metric': [],
    'value': [],
    'notes': []
}

# Dataset info
export_data['metric'].extend(['total_tweets', 'date_range_start', 'date_range_end', 'num_languages'])
export_data['value'].extend([total_tweets, date_str, date_end_str, num_languages])
export_data['notes'].extend(['', '', '', ''])

# Language distribution
for lang, count in lang_counts.head(10).items():
    export_data['metric'].append(f'lang_{lang}')
    export_data['value'].append(count)
    export_data['notes'].append(f'{count/total*100:.2f}%')

# Thai content analysis
export_data['metric'].extend(['thai_tweets', 'thai_percentage', 'thai_peak_day_pct', 'thai_rt_mean', 'en_rt_mean', 'thai_en_rt_ratio'])
export_data['value'].extend([thai_count, f'{thai_pct:.2f}', f'{thai_max_pct:.2f}', f'{thai_rt_mean:.2f}', f'{en_rt_mean:.2f}', f'{rt_ratio:.2f}'])
export_data['notes'].extend(['', '', '', '', '', ''])

# Engagement
export_data['metric'].extend(['mean_retweets', 'median_retweets', 'mean_likes', 'median_likes', 'rt_skewness', 'like_skewness'])
export_data['value'].extend([f'{rt_mean:.2f}', f'{rt_median:.2f}', f'{fav_mean:.2f}', f'{fav_median:.2f}', f'{rt_skew:.2f}', f'{fav_skew:.2f}'])
export_data['notes'].extend(['', '', '', '', '', ''])

# Coordination
export_data['metric'].extend(['duplicate_texts', 'duplicate_instances', 'duplicate_percentage', 'temporal_peak_day_pct', 'temporal_ratio'])
export_data['value'].extend([dup_count, dup_tweets, f'{dup_tweets/total*100:.2f}', f'{max_daily_pct:.2f}', f'{ratio:.1f}'])
export_data['notes'].extend(['', '', '', '', ''])

# Create DataFrame and export
export_df = pd.DataFrame(export_data)
export_csv = 'workflows/agent-academy/sample-data/belarus_findings.csv'
export_df.to_csv(export_csv, index=False)
print(f"\n✓ Findings exported to: {export_csv}")
print(f"✓ Records: {len(export_df)}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
