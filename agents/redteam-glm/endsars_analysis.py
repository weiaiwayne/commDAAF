#!/usr/bin/env python3
"""
#EndSARS Twitter Dataset Analysis
CommDAAF Methodology: Exploratory Tier
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from datetime import datetime, timedelta
import json
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# PARAMETER CHOICES (Explicit per CommDAAF methodology)
SAMPLE_SIZE = 10000  # Full sample
TOP_N_USERS = 20     # For network analysis
TOP_N_HASHTAGS = 20  # For content analysis
TOP_N_TOPICS = 5     # For topic modeling
TIME_BIN_HOURS = 12  # For temporal analysis
ENGAGEMENT_QUANTILES = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]

# Load data
print("Loading dataset...")
df = pd.read_csv('/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/red-teaming/sample-data/endsars_sample_10k.csv')

print(f"\nDataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# =============================================================================
# SECTION 1: DESCRIPTIVE STATISTICS
# =============================================================================

print("\n" + "="*80)
print("SECTION 1: DESCRIPTIVE STATISTICS")
print("="*80)

# Basic statistics
print("\n--- Basic Overview ---")
print(f"Total tweets: {len(df):,}")
print(f"Retweets: {df['is_retweet'].sum():,} ({df['is_retweet'].mean()*100:.1f}%)")
print(f"Original tweets: {(~df['is_retweet']).sum():,} ({(~df['is_retweet']).mean()*100:.1f}%)")

# User statistics
print("\n--- User Statistics ---")
print(f"Unique users: {df['from_user_screen_name'].nunique():,}")
print(f"Average followers: {df['from_user_followers_count'].mean():.0f} (median: {df['from_user_followers_count'].median():.0f})")
print(f"Average friends: {df['from_user_friends_count'].mean():.0f} (median: {df['from_user_friends_count'].median():.0f})")
print(f"Average user tweet count: {df['from_user_statuses_count'].mean():.0f} (median: {df['from_user_statuses_count'].median():.0f})")

# Engagement statistics
print("\n--- Engagement Statistics ---")
print(f"Average likes: {df['favorite_count'].mean():.1f} (median: {df['favorite_count'].median():.0f})")
print(f"Average retweets: {df['retweet_count'].mean():.1f} (median: {df['retweet_count'].median():.0f})")
print(f"Max likes: {df['favorite_count'].max():,}")
print(f"Max retweets: {df['retweet_count'].max():,}")

# Temporal range
print("\n--- Temporal Range ---")
df['tweet_date'] = pd.to_datetime(df['tweet_date'])
print(f"Date range: {df['tweet_date'].min().date()} to {df['tweet_date'].max().date()}")
print(f"Days covered: {(df['tweet_date'].max() - df['tweet_date'].min()).days}")

# Language
print("\n--- Language Distribution ---")
lang_dist = df['language'].value_counts()
print(lang_dist.head(10))

# =============================================================================
# SECTION 2: NETWORK STRUCTURE ANALYSIS
# =============================================================================

print("\n" + "="*80)
print("SECTION 2: NETWORK STRUCTURE ANALYSIS")
print("="*80)

# Extract mentioned users from RT structure
def extract_rt_username(content):
    """Extract the username being retweeted from 'RT @username:' pattern"""
    match = re.search(r'RT @([A-Za-z0-9_]+):', str(content))
    return match.group(1) if match else None

# Apply to retweets
df['rt_source'] = df[df['is_retweet']]['content'].apply(extract_rt_username)

# Get top amplifiers (most retweeted accounts)
print("\n--- Top Amplifiers (Most Retweeted Accounts) ---")
top_sources = df['rt_source'].value_counts().head(TOP_N_USERS)
print(top_sources)

# Get top users by follower count
print("\n--- Top Users by Follower Count ---")
top_followers = df[['from_user_screen_name', 'from_user_followers_count']].drop_duplicates().sort_values('from_user_followers_count', ascending=False).head(TOP_N_USERS)
print(top_followers.to_string(index=False))

# Mention network analysis
def extract_mentions(mentions_str):
    """Extract mentioned usernames from entities_mentions column"""
    if pd.isna(mentions_str) or mentions_str == '':
        return []
    # Parse the format which appears to be comma-separated usernames
    mentions = str(mentions_str).split(',')
    return [m.strip() for m in mentions if m.strip()]

# Create mention network
all_mentions = []
for idx, row in df.iterrows():
    mentions = extract_mentions(row['entities_mentions'])
    for mention in mentions:
        all_mentions.append({
            'from': row['from_user_screen_name'],
            'to': mention,
            'tweet_id': row['tweet_id']
        })

mention_df = pd.DataFrame(all_mentions)
if len(mention_df) > 0:
    print("\n--- Most Mentioned Users ---")
    top_mentioned = mention_df['to'].value_counts().head(TOP_N_USERS)
    print(top_mentioned)

# =============================================================================
# SECTION 3: TEMPORAL DYNAMICS
# =============================================================================

print("\n" + "="*80)
print("SECTION 3: TEMPORAL DYNAMICS")
print("="*80)

# Create time bins
df['time_bin'] = df['tweet_date'].dt.floor(f'{TIME_BIN_HOURS}H')
temporal_counts = df.groupby('time_bin').size().reset_index(name='count')

print("\n--- Tweets by Time Period ---")
print(temporal_counts)

# Identify phases
temporal_counts['rolling_avg'] = temporal_counts['count'].rolling(window=3, center=True).mean()

print("\n--- Activity Phases (Based on rolling average) ---")
max_avg = temporal_counts['rolling_avg'].max()
min_avg = temporal_counts['rolling_avg'].min()

# Define phases
temporal_counts['phase'] = 'Moderate'
temporal_counts.loc[temporal_counts['rolling_avg'] >= max_avg * 0.75, 'phase'] = 'Peak'
temporal_counts.loc[temporal_counts['rolling_avg'] <= min_avg * 1.5, 'phase'] = 'Low'

phase_summary = temporal_counts.groupby('phase').agg({
    'count': ['mean', 'std', 'count'],
    'time_bin': ['min', 'max']
})
print(phase_summary)

# Compare retweet vs original over time
temporal_type = df.groupby(['time_bin', 'is_retweet']).size().unstack(fill_value=0)
temporal_type['rt_ratio'] = temporal_type[True] / (temporal_type[True] + temporal_type[False])

print("\n--- Retweet Ratio Over Time ---")
print(temporal_type[['rt_ratio']].describe())

# =============================================================================
# SECTION 4: CONTENT PATTERNS
# =============================================================================

print("\n" + "="*80)
print("SECTION 4: CONTENT PATTERNS")
print("="*80)

# Hashtag analysis
def extract_hashtags(hashtags_str):
    """Extract hashtags from entities_hashtags column"""
    if pd.isna(hashtags_str) or hashtags_str == '':
        return []
    hashtags = str(hashtags_str).split(',')
    return [h.strip() for h in hashtags if h.strip()]

# Get all hashtags
all_hashtags = []
for idx, row in df.iterrows():
    hashtags = extract_hashtags(row['entities_hashtags'])
    all_hashtags.extend(hashtags)

print("\n--- Top Hashtags ---")
hashtag_counts = Counter(all_hashtags)
print(hashtag_counts.most_common(TOP_N_HASHTAGS))

# Content length analysis
df['content_length'] = df['content'].str.len()
df['word_count'] = df['content'].str.split().str.len()

print("\n--- Content Length Statistics ---")
print(f"Character count - Mean: {df['content_length'].mean():.0f} (Median: {df['content_length'].median():.0f})")
print(f"Word count - Mean: {df['word_count'].mean():.1f} (Median: {df['word_count'].median():.0f})")

print("\n--- Content Length: Original vs Retweet ---")
print(df.groupby('is_retweet')[['content_length', 'word_count']].describe())

# Simple keyword analysis
keywords = ['sars', 'police', 'government', 'buhari', 'nigeria', 'shooting', 'kill',
            'protest', 'lekk', 'youth', 'military', 'brutal', 'violence', 'peace',
            'justice', 'accountability', 'blood', 'death', 'pray', 'help']

print("\n--- Keyword Frequencies ---")
keyword_results = {}
for kw in keywords:
    count = df['content'].str.lower().str.contains(kw, na=False).sum()
    keyword_results[kw] = {
        'total': int(count),
        'pct': count / len(df) * 100
    }

for kw, result in sorted(keyword_results.items(), key=lambda x: x[1]['total'], reverse=True):
    print(f"{kw:15s}: {result['total']:5d} ({result['pct']:5.2f}%)")

# =============================================================================
# SECTION 5: ENGAGEMENT PREDICTORS
# =============================================================================

print("\n" + "="*80)
print("SECTION 5: ENGAGEMENT PREDICTORS")
print("="*80)

# Focus on original tweets for engagement analysis
original_tweets = df[~df['is_retweet']].copy()

print(f"\nAnalyzing {len(original_tweets)} original tweets for engagement...")

# Quantile analysis
print("\n--- Engagement Quantiles ---")
print(f"\nLikes distribution:")
print(original_tweets['favorite_count'].quantile(ENGAGEMENT_QUANTILES))
print(f"\nRetweets distribution:")
print(original_tweets['retweet_count'].quantile(ENGAGEMENT_QUANTILES))

# Correlation analysis
print("\n--- Correlations with Engagement (Original Tweets) ---")
engagement_cols = ['favorite_count', 'retweet_count']
predictor_cols = ['content_length', 'word_count', 'from_user_followers_count',
                  'from_user_friends_count', 'from_user_statuses_count']

for eng_col in engagement_cols:
    print(f"\n{eng_col}:")
    for pred_col in predictor_cols:
        corr = original_tweets[[eng_col, pred_col]].corr().iloc[0, 1]
        print(f"  {pred_col:30s}: {corr:.3f}")

# High-engagement tweets
likes_threshold = original_tweets['favorite_count'].quantile(0.90)
rt_threshold = original_tweets['retweet_count'].quantile(0.90)

high_engagement = original_tweets[
    (original_tweets['favorite_count'] >= likes_threshold) |
    (original_tweets['retweet_count'] >= rt_threshold)
]

print(f"\n--- High-Engagement Tweets (top 10% by likes or retweets) ---")
print(f"Count: {len(high_engagement)} / {len(original_tweets)} ({len(high_engagement)/len(original_tweets)*100:.1f}%)")

# Compare high vs low engagement
print("\n--- High vs Low Engagement Feature Comparison ---")
original_tweets['high_engagement'] = (
    (original_tweets['favorite_count'] >= likes_threshold) |
    (original_tweets['retweet_count'] >= rt_threshold)
)

comparison = original_tweets.groupby('high_engagement')[predictor_cols].agg(['mean', 'median'])
print(comparison)

# =============================================================================
# SECTION 6: RETWEET BEHAVIOR
# =============================================================================

print("\n" + "="*80)
print("SECTION 6: RETWEET BEHAVIOR")
print("="*80)

retweets = df[df['is_retweet']].copy()
originals = df[~df['is_retweet']].copy()

print(f"\n--- Retweet vs Original Statistics ---")
print(f"\nUser followers - Retweets: {retweets['from_user_followers_count'].mean():.0f} vs Originals: {originals['from_user_followers_count'].mean():.0f}")
print(f"User friends - Retweets: {retweets['from_user_friends_count'].mean():.0f} vs Originals: {originals['from_user_friends_count'].mean():.0f}")
print(f"User activity - Retweets: {retweets['from_user_statuses_count'].mean():.0f} vs Originals: {originals['from_user_statuses_count'].mean():.0f}")

# Top retweet sources amplification
print("\n--- Top Amplification Sources (Their reach) ---")
top_sources_followers = df[df['rt_source'].isin(top_sources.head(10).index)].groupby('rt_source')['from_user_followers_count'].mean()
print(top_sources_followers)

# =============================================================================
# VISUALIZATIONS
# =============================================================================

print("\n" + "="*80)
print("GENERATING VISUALIZATIONS")
print("="*80)

# Create figure directory
import os
os.makedirs('/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/figures', exist_ok=True)

# 1. Temporal dynamics
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Tweet volume over time
ax1 = axes[0, 0]
temporal_counts.plot(x='time_bin', y='count', ax=ax1, marker='o')
ax1.plot(temporal_counts['time_bin'], temporal_counts['rolling_avg'], '--', label='Rolling avg', linewidth=2)
ax1.set_xlabel('Time')
ax1.set_ylabel('Tweet Count')
ax1.set_title('Tweet Volume Over Time')
ax1.legend()
ax1.tick_params(axis='x', rotation=45)

# Retweet ratio over time
ax2 = axes[0, 1]
temporal_type['rt_ratio'].plot(ax=ax2, marker='s', color='coral')
ax2.axhline(y=df['is_retweet'].mean(), color='gray', linestyle='--', label='Overall mean')
ax2.set_xlabel('Time')
ax2.set_ylabel('Retweet Ratio')
ax2.set_title('Retweet Ratio Over Time')
ax2.legend()
ax2.tick_params(axis='x', rotation=45)

# Top hashtags
ax3 = axes[1, 0]
hashtag_df = pd.DataFrame(hashtag_counts.most_common(TOP_N_HASHTAGS), columns=['hashtag', 'count'])
sns.barplot(data=hashtag_df, x='count', y='hashtag', ax=ax3)
ax3.set_xlabel('Count')
ax3.set_ylabel('Hashtag')
ax3.set_title(f'Top {TOP_N_HASHTAGS} Hashtags')

# Top amplifiers
ax4 = axes[1, 1]
top_sources_df = pd.DataFrame(top_sources.items(), columns=['user', 'count'])
sns.barplot(data=top_sources_df, x='count', y='user', ax=ax4)
ax4.set_xlabel('Retweet Count')
ax4.set_ylabel('User')
ax4.set_title(f'Top {TOP_N_USERS} Amplifiers')

plt.tight_layout()
plt.savefig('/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/figures/fig1_overview.png', dpi=150, bbox_inches='tight')
print("Saved: figures/fig1_overview.png")

# 2. Engagement analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Like distribution
ax1 = axes[0, 0]
sns.histplot(data=original_tweets, x='favorite_count', bins=50, ax=ax1, log_scale=True)
ax1.set_xlabel('Likes')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of Likes (Original Tweets)')

# Retweet distribution
ax2 = axes[0, 1]
sns.histplot(data=original_tweets, x='retweet_count', bins=50, ax=ax2, log_scale=True)
ax2.set_xlabel('Retweets')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Retweets (Original Tweets)')

# Engagement vs followers
ax3 = axes[1, 0]
ax3.scatter(original_tweets['from_user_followers_count'], original_tweets['favorite_count'], alpha=0.3, s=20)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_xlabel('User Followers (log)')
ax3.set_ylabel('Likes (log)')
ax3.set_title('Likes vs User Followers')

# Engagement word count
ax4 = axes[1, 1]
sns.boxplot(data=original_tweets, x='high_engagement', y='word_count', ax=ax4)
ax4.set_xlabel('High Engagement')
ax4.set_ylabel('Word Count')
ax4.set_title('Word Count by Engagement Level')

plt.tight_layout()
plt.savefig('/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/figures/fig2_engagement.png', dpi=150, bbox_inches='tight')
print("Saved: figures/fig2_engagement.png")

# 3. Network structure
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# User distribution
ax1 = axes[0]
sns.histplot(data=df, x='from_user_followers_count', bins=50, ax=ax1, log_scale=True)
ax1.set_xlabel('Followers (log scale)')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of User Followers')

# Top amplifiers
ax2 = axes[1]
top_sources_followers_df = pd.DataFrame({
    'user': top_sources.head(10).index,
    'retweets': top_sources.head(10).values,
    'avg_follower_reach': top_sources_followers.values
})
sns.scatterplot(data=top_sources_followers_df, x='avg_follower_reach', y='retweets', hue='user', ax=ax2, legend=False, s=100)
for idx, row in top_sources_followers_df.iterrows():
    ax2.annotate(row['user'], (row['avg_follower_reach'], row['retweets']), fontsize=8)
ax2.set_xlabel('Average Followers of Retweeters')
ax2.set_ylabel('Times Retweeted')
ax2.set_title('Amplification Sources')
ax2.set_xscale('log')
ax2.set_yscale('log')

plt.tight_layout()
plt.savefig('/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/figures/fig3_network.png', dpi=150, bbox_inches='tight')
print("Saved: figures/fig3_network.png")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
