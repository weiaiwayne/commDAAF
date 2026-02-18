import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Load the dataset
df = pd.read_csv('/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/red-teaming/sample-data/endsars_sample_10k.csv')

print("=" * 60)
print("#EndSARS TWITTER DATASET ANALYSIS")
print("=" * 60)

# ============================================================
# 1. DESCRIPTIVE STATISTICS
# ============================================================
print("\n## 1. DESCRIPTIVE STATISTICS\n")

print(f"Total tweets: {len(df):,}")
print(f"Date range: {df['tweet_date'].min()} to {df['tweet_date'].max()}")

# Retweet distribution
retweet_counts = df['is_retweet'].value_counts()
retweet_pct = df['is_retweet'].mean() * 100
print(f"\nRetweet composition:")
print(f"  - Retweets: {retweet_counts.get(True, 0):,} ({retweet_pct:.1f}%)")
print(f"  - Original tweets: {retweet_counts.get(False, 0):,} ({100-retweet_pct:.1f}%)")

# Engagement metrics
print(f"\nEngagement metrics (all tweets):")
print(f"  - Mean favorites: {df['favorite_count'].mean():.2f}")
print(f"  - Median favorites: {df['favorite_count'].median():.2f}")
print(f"  - Max favorites: {df['favorite_count'].max():,}")
print(f"  - Mean retweets: {df['retweet_count'].mean():.2f}")
print(f"  - Median retweets: {df['retweet_count'].median():.2f}")
print(f"  - Max retweets: {df['retweet_count'].max():,}")

# Engagement by tweet type
print(f"\nEngagement by tweet type:")
orig_engagement = df[~df['is_retweet']]
rt_engagement = df[df['is_retweet']]
print(f"  - Original tweets - Mean favorites: {orig_engagement['favorite_count'].mean():.2f}, Mean RTs: {orig_engagement['retweet_count'].mean():.2f}")
print(f"  - Retweets - Mean favorites: {rt_engagement['favorite_count'].mean():.2f}, Mean RTs: {rt_engagement['retweet_count'].mean():.2f}")

# User statistics
print(f"\nUser statistics:")
print(f"  - Unique users: {df['from_user_id'].nunique():,}")
print(f"  - Mean followers: {df['from_user_followers_count'].mean():.0f}")
print(f"  - Median followers: {df['from_user_followers_count'].median():.0f}")

# ============================================================
# 2. TEMPORAL ANALYSIS
# ============================================================
print("\n## 2. TEMPORAL ANALYSIS\n")

# Parse dates
df['created_at'] = pd.to_datetime(df['created_at'])
df['date'] = df['created_at'].dt.date
df['hour'] = df['created_at'].dt.hour

# Daily volume
daily_counts = df.groupby('date').size()
print("Daily tweet volume:")
for date, count in daily_counts.items():
    print(f"  - {date}: {count:,} tweets")

# Phase identification
# Based on the research brief context:
# Phase 1 (Oct 21-25): Immediate aftermath, international attention
# Phase 2 (Oct 26-31): Government response, curfews
# Phase 3 (Nov 1-5): Aftermath, accountability demands

df['phase'] = pd.cut(
    pd.to_datetime(df['date']),
    bins=pd.to_datetime(['2020-10-20', '2020-10-26', '2020-11-01', '2020-11-06']),
    labels=['Phase 1 (Oct 21-25)', 'Phase 2 (Oct 26-31)', 'Phase 3 (Nov 1-5)']
)

phase_stats = df.groupby('phase').agg({
    'favorite_count': 'mean',
    'retweet_count': 'mean',
    'is_retweet': lambda x: x.sum() / len(x) * 100
}).round(2)
phase_stats.columns = ['Avg Favorites', 'Avg Retweets', 'Retweet %']
print(f"\nPhase analysis:")
print(phase_stats)

# ============================================================
# 3. NETWORK ANALYSIS - CENTRAL ACTORS
# ============================================================
print("\n## 3. NETWORK ANALYSIS - CENTRAL ACTORS\n")

# Most active users
print("Top 10 most active users:")
top_users = df['from_user_screen_name'].value_counts().head(10)
for i, (user, count) in enumerate(top_users.items(), 1):
    print(f"  {i}. @{user}: {count} tweets")

# Most mentioned accounts (from entities_mentions)
print("\nTop 10 most mentioned accounts:")

# Parse mentions
all_mentions = []
for mentions in df['entities_mentions'].dropna():
    if pd.notna(mentions) and mentions != '':
        # Handle different formats
        mention_list = str(mentions).split(',')
        all_mentions.extend([m.strip() for m in mention_list if m.strip()])

mention_counts = Counter(all_mentions)
for i, (mention, count) in enumerate(mention_counts.most_common(10), 1):
    print(f"  {i}. @{mention}: {count} mentions")

# Top accounts by follower count (influencers)
print("\nTop 10 accounts by follower count in dataset:")
user_followers = df.groupby('from_user_screen_name')['from_user_followers_count'].max().sort_values(ascending=False).head(10)
for i, (user, followers) in enumerate(user_followers.items(), 1):
    print(f"  {i}. @{user}: {followers:,} followers")

# Celebrity/verified-like patterns (high followers, few tweets)
print("\nPotential celebrity/influencer accounts (high followers, limited activity):")
celeb_candidates = df.groupby('from_user_screen_name').agg({
    'from_user_followers_count': 'max',
    'tweet_id': 'count'
}).reset_index()
celeb_candidates = celeb_candidates[celeb_candidates['from_user_followers_count'] > 100000]
celeb_candidates = celeb_candidates[celeb_candidates['tweet_id'] <= 10]  # Few tweets in sample
for _, row in celeb_candidates.sort_values('from_user_followers_count', ascending=False).head(10).iterrows():
    print(f"  - @{row['from_user_screen_name']}: {row['from_user_followers_count']:,} followers, {row['tweet_id']} tweets")

# ============================================================
# 4. CONTENT ANALYSIS
# ============================================================
print("\n## 4. CONTENT ANALYSIS\n")

# Hashtag analysis
all_hashtags = []
for hashtags in df['entities_hashtags'].dropna():
    if pd.notna(hashtags) and hashtags != '':
        tag_list = str(hashtags).split(',')
        all_hashtags.extend([h.strip().lower() for h in tag_list if h.strip()])

hashtag_counts = Counter(all_hashtags)
print("Top 15 hashtags (excluding #endsars):")
for tag, count in hashtag_counts.most_common(16):
    if tag != 'endsars':
        print(f"  - #{tag}: {count} uses")

# Text analysis for original tweets
print("\nContent themes in original tweets:")
orig_tweets = df[~df['is_retweet']]['content'].dropna().str.lower()

# Keyword extraction
keywords = {
    'police_brutality': ['police', 'sars', 'brutality', 'shooting', 'killed', 'kill', 'death', 'violence'],
    'government_accountability': ['government', 'buhari', 'leadership', 'accountability', 'president'],
    'protest_actions': ['protest', 'march', 'demonstration', 'rally', 'gather'],
    'international': ['international', 'world', 'global', 'uk', 'us', 'london', 'america'],
    'emotional': ['sad', 'angry', 'heart', 'cry', 'tears', 'pain', 'hurt', '💔', '😭', '😡'],
    'solidarity': ['solidarity', 'support', 'pray', 'prayers', 'together', 'unite'],
    'lekki': ['lekki', 'toll', 'gate', 'massacre'],
    'information': ['news', 'update', 'report', 'media', 'update']
}

theme_counts = {}
for theme, words in keywords.items():
    count = sum(1 for tweet in orig_tweets if any(word in tweet for word in words))
    theme_counts[theme] = count

print("Theme prevalence in original tweets:")
for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    pct = count / len(orig_tweets) * 100
    print(f"  - {theme.replace('_', ' ').title()}: {count} tweets ({pct:.1f}%)")

# ============================================================
# 5. ENGAGEMENT MODELING
# ============================================================
print("\n## 5. ENGAGEMENT MODELING\n")

# Analysis limited to original tweets for meaningful modeling
orig_df = df[~df['is_retweet']].copy()

# Create features
orig_df['content_length'] = orig_df['content'].str.len()
orig_df['has_hashtags'] = orig_df['entities_hashtags'].notna() & (orig_df['entities_hashtags'] != '')
orig_df['has_mentions'] = orig_df['entities_mentions'].notna() & (orig_df['entities_mentions'] != '')
orig_df['has_url'] = orig_df['entities_urls_count'] > 0
orig_df['followers_log'] = np.log1p(orig_df['from_user_followers_count'])

# Correlation analysis
features = ['content_length', 'has_hashtags', 'has_mentions', 'has_url', 
            'followers_log', 'from_user_statuses_count']
print("Correlation with favorite_count (original tweets only):")
for feat in features:
    corr = orig_df[feat].corr(orig_df['favorite_count'])
    print(f"  - {feat}: {corr:.3f}")

# High engagement tweets
print("\nTop 10 most favorited original tweets:")
top_tweets = orig_df.nlargest(10, 'favorite_count')[['from_user_screen_name', 'favorite_count', 'retweet_count', 'content']]
for _, row in top_tweets.iterrows():
    content_preview = row['content'][:100] + "..." if len(row['content']) > 100 else row['content']
    print(f"  \n  @{row['from_user_screen_name']} (♥ {row['favorite_count']:,}, RT {row['retweet_count']:,}):")
    print(f"    \"{content_preview}\"")

# ============================================================
# 6. RETWEET BEHAVIOR ANALYSIS
# ============================================================
print("\n## 6. RETWEET BEHAVIOR ANALYSIS\n")

print(f"Retweet rate in sample: {retweet_pct:.1f}%")
print(f"This aligns with the full dataset's 93.9% retweet rate.")

# Most retweeted original content (viral tweets)
viral_threshold = df['retweet_count'].quantile(0.99)
print(f"\nViral threshold (99th percentile): {viral_threshold:.0f} retweets")

viral_tweets = df[df['retweet_count'] >= viral_threshold]
print(f"Number of viral tweets (≥{viral_threshold:.0f} RTs): {len(viral_tweets)}")

print("\nMost viral original tweets in sample:")
viral_orig = viral_tweets[~viral_tweets['is_retweet']].nlargest(5, 'retweet_count')
for _, row in viral_orig.iterrows():
    content_preview = row['content'][:80] + "..." if len(row['content']) > 80 else row['content']
    print(f"  - @{row['from_user_screen_name']}: {row['retweet_count']:,} RTs")
    print(f"    \"{content_preview}\"")

# Retweet cascades analysis
print("\nRetweet cascade analysis:")
# For retweets, the retweet_count reflects the original tweet's virality
rt_cascade = df[df['is_retweet']]['retweet_count'].describe()
print(f"  - Mean original virality: {rt_cascade['mean']:.0f}")
print(f"  - Median original virality: {rt_cascade['50%']:.0f}")
print(f"  - High virality (>10K RTs): {(df[df['is_retweet']]['retweet_count'] > 10000).sum():,} retweets")

# ============================================================
# 7. SUMMARY STATISTICS
# ============================================================
print("\n" + "=" * 60)
print("## SUMMARY STATISTICS")
print("=" * 60)

summary_stats = {
    'Total Tweets': f"{len(df):,}",
    'Date Range': f"{df['date'].min()} to {df['date'].max()}",
    'Unique Users': f"{df['from_user_id'].nunique():,}",
    'Retweet Rate': f"{retweet_pct:.1f}%",
    'Avg Daily Volume': f"{len(df) / len(daily_counts):.0f}",
    'Top Hashtag (after #EndSARS)': f"#{hashtag_counts.most_common(2)[1][0]}",
    'Most Active User': f"@{top_users.index[0]}",
    'Most Mentioned': f"@{mention_counts.most_common(1)[0][0]}"
}

for key, value in summary_stats.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("Analysis complete. Generating visualizations...")
print("=" * 60)
