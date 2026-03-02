#!/usr/bin/env python3
"""
Xinjiang Cotton Twitter Analysis - Exploratory Tier
AgentAcademy Run 7
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import re
import warnings
warnings.filterwarnings('ignore')

# Configuration
DATA_PATH = "/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/agent-academy/sample-data/#xinjiang_#xinjiangcotton_325to401_withuserinfo.csv"
OUTPUT_PATH = "/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/agent-academy/sample-data/XINJIANG_ANALYSIS_RESULTS.md"

# Frame keywords (dictionary approach)
PRO_CHINA_KEYWORDS = [
    'baseless slander', 'baseless', 'slander', 'wonderful land',
    'true picture', 'lies', 'fabricated', 'forced labor narrative',
    'propaganda', 'fake news', 'western media', 'biased'
]

PRO_UYGHUR_KEYWORDS = [
    'genocide', 'concentration camp', 'forced labor',
    'human rights', 'detention', 'reeducation',
    'uyghurlivesmatter', 'closethecamps', 'xinjiangcotton'
]

def load_data():
    """Load and preprocess data."""
    print("Loading data...")
    df = pd.read_csv(DATA_PATH, low_memory=False)
    print(f"Loaded {len(df)} tweets with {len(df.columns)} columns")
    return df

def parse_datetime(df):
    """Parse timestamps."""
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date
    df['hour'] = df['created_at'].dt.hour
    df['day_of_week'] = df['created_at'].dt.day_name()
    return df

def classify_frame(text):
    """
    Classify frame using dictionary approach.
    Returns: 'pro-china', 'pro-uyghur', 'neutral', 'ambiguous', 'mixed'
    """
    if pd.isna(text):
        return 'neutral'

    text_lower = text.lower()

    pro_china_count = sum(1 for kw in PRO_CHINA_KEYWORDS if kw in text_lower)
    pro_uyghur_count = sum(1 for kw in PRO_UYGHUR_KEYWORDS if kw in text_lower)

    if pro_china_count > 0 and pro_uyghur_count > 0:
        return 'mixed'
    elif pro_china_count > 0:
        return 'pro-china'
    elif pro_uyghur_count > 0:
        return 'pro-uyghur'
    else:
        return 'neutral'

def analyze_temporal_dynamics(df):
    """RQ4: Temporal dynamics."""
    print("\n" + "="*60)
    print("RQ4: TEMPORAL DYNAMICS")
    print("="*60)

    # Daily distribution
    daily_counts = df.groupby('date').size().sort_index()
    print(f"\nDaily tweet distribution:")
    for date, count in daily_counts.items():
        print(f"  {date}: {count:,} tweets ({count/len(df)*100:.1f}%)")

    # Check for March 25-26 spike
    spike_date = pd.to_datetime('2021-03-25').date()
    spike_date_2 = pd.to_datetime('2021-03-26').date()

    spike_tweets = df[df['date'].isin([spike_date, spike_date_2])]
    spike_count = len(spike_tweets)
    avg_daily = daily_counts.mean()

    print(f"\n📊 MARCH 25-26 SPIKE ANALYSIS:")
    print(f"  Total tweets March 25-26: {spike_count:,}")
    print(f"  Daily average (all days): {avg_daily:,.0f}")
    print(f"  Spike ratio: {spike_count/2 / avg_daily:.2f}x average")

    if spike_count/2 / avg_daily > 1.5:
        print(f"  ⚠️  CONFIRMED: Significant spike detected")
    else:
        print(f"  ℹ️  No significant spike detected")

    return spike_date, spike_date_2

def analyze_frames(df):
    """RQ2: Narrative frames."""
    print("\n" + "="*60)
    print("RQ2: NARRATIVE FRAMES")
    print("="*60)

    # Classify frames
    df['frame'] = df['text'].apply(classify_frame)

    # Frame distribution
    frame_dist = df['frame'].value_counts()
    print(f"\nFrame distribution:")
    for frame, count in frame_dist.items():
        print(f"  {frame}: {count:,} ({count/len(df)*100:.1f}%)")

    # Frames over time
    print(f"\nFrames by date (key dates):")
    frames_by_date = df.groupby(['date', 'frame']).size().unstack(fill_value=0)
    
    key_dates = [pd.to_datetime('2021-03-25').date(), 
                pd.to_datetime('2021-03-26').date(),
                pd.to_datetime('2021-03-22').date()]
    
    for date in key_dates:
        if date in frames_by_date.index:
            print(f"\n  {date}:")
            date_tweets = frames_by_date.loc[date]
            total = date_tweets.sum()
            for frame in ['pro-china', 'pro-uyghur', 'neutral', 'mixed']:
                count = date_tweets.get(frame, 0)
                pct = count / total * 100 if total > 0 else 0
                print(f"    {frame}: {count:,} ({pct:.1f}%)")

    return df

def analyze_engagement_asymmetries(df):
    """RQ5: Engagement asymmetries."""
    print("\n" + "="*60)
    print("RQ5: ENGAGEMENT ASYMMETRIES")
    print("="*60)

    # Engagement metrics by frame
    engagement_cols = ['retweet_count', 'like_count', 'reply_count', 'quote_count']

    # Separate original tweets and retweets for fair comparison
    df_original = df[df['retweeted'].isna() | (df['retweeted'] == 'NULL')]
    
    print(f"\nEngagement by frame (ORIGINAL TWEETS ONLY, N={len(df_original):,}):")
    print(f"  Note: Median used to reduce skewness impact\n")

    for frame in df_original['frame'].unique():
        frame_data = df_original[df_original['frame'] == frame]
        if len(frame_data) == 0:
            continue
        print(f"\n  {frame.upper()} (N={len(frame_data):,}):")

        for col in engagement_cols:
            values = frame_data[col].dropna()
            if len(values) > 0:
                median_val = np.median(values)
                mean_val = np.mean(values)
                print(f"    {col}: median={median_val:.1f}, mean={mean_val:.1f}")

    # Retweet rate by frame
    print(f"\nRetweet rate by frame (% of tweets that are retweets):")
    for frame in df['frame'].unique():
        frame_data = df[df['frame'] == frame]
        total = len(frame_data)
        rt_count = len(frame_data[frame_data['retweeted'] == 'retweeted'])
        rt_rate = rt_count / total * 100 if total > 0 else 0
        print(f"  {frame}: {rt_rate:.1f}%")

def analyze_state_linked_accounts(df):
    """RQ3: State-linked account patterns."""
    print("\n" + "="*60)
    print("RQ3: STATE-LINKED ACCOUNTS")
    print("="*60)

    # Identify verified accounts
    verified = df[df['verified'] == True]
    print(f"\nVerified accounts: {len(verified)} tweets from {verified['author_id'].nunique()} unique accounts")
    print(f"  % of total: {len(verified)/len(df)*100:.1f}%")

    # Check for state media keywords in username/bio
    state_media_keywords = ['globaltimes', 'xinhua', 'cgtn', 'peoples daily', 'cctv']
    
    def is_state_media(row):
        username = str(row['username']).lower() if pd.notna(row['username']) else ''
        description = str(row['description']).lower() if pd.notna(row['description']) else ''
        text = username + ' ' + description
        return any(kw in text for kw in state_media_keywords)

    df['state_media'] = df.apply(is_state_media, axis=1)
    state_media_tweets = df[df['state_media'] == True]

    print(f"\nState media accounts (by keyword): {len(state_media_tweets)} tweets from {state_media_tweets['author_id'].nunique()} unique accounts")
    print(f"  % of total: {len(state_media_tweets)/len(df)*100:.1f}%")

    # Top accounts by tweet volume
    print(f"\nTop 10 accounts by tweet volume:")
    top_accounts = df.groupby('username').size().sort_values(ascending=False).head(10)
    for i, (username, count) in enumerate(top_accounts.items(), 1):
        print(f"  {i:2d}. {username}: {count:,} tweets")

def analyze_coordinated_amplification(df, spike_date, spike_date_2):
    """RQ1: Coordinated amplification evidence."""
    print("\n" + "="*60)
    print("RQ1: COORDINATED AMPLIFICATION (March 25-26)")
    print("="*60)

    # Filter to spike period
    spike_df = df[df['date'].isin([spike_date, spike_date_2])].copy()

    print(f"\nSpike period analysis:")
    print(f"  Total tweets: {len(spike_df):,}")

    # Analyze by hour for March 25
    mar25_df = spike_df[spike_df['date'] == spike_date]
    hourly_counts = mar25_df.groupby('hour').size().sort_values(ascending=False)

    print(f"\nMarch 25 hourly distribution (top 10 hours):")
    for hour, count in hourly_counts.head(10).items():
        print(f"  {hour:02d}:00: {count:,} tweets")

    # Identify retweet bursts (accounts with multiple retweets in 1-hour window)
    spike_retweets = spike_df[spike_df['retweeted'] == 'retweeted']
    rt_per_account = spike_retweets.groupby('username').size().sort_values(ascending=False)

    print(f"\nAccounts with high retweet volume during spike (>10 retweets):")
    high_rt_accounts = rt_per_account[rt_per_account > 10]
    for username, count in high_rt_accounts.head(20).items():
        print(f"  {username}: {count} retweets")

    # Check for URL/hashtag clustering
    def extract_urls(text):
        if pd.isna(text):
            return []
        url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        return re.findall(url_pattern, str(text))

    spike_df.loc[:, 'urls_list'] = spike_df['text'].apply(extract_urls)
    all_urls = [url for urls in spike_df['urls_list'] for url in urls]
    url_counts = Counter(all_urls)

    print(f"\nTop 10 most-shared URLs during spike:")
    for (url, count) in url_counts.most_common(10):
        if len(url) > 60:
            url = url[:57] + "..."
        print(f"  {url}: {count} shares")

def detect_potential_bots(df):
    """Bot/Automated account detection (heuristics)."""
    print("\n" + "="*60)
    print("BOT DETECTION (Heuristics)")
    print("="*60)

    # Calculate tweets per account
    tweets_per_account = df.groupby('username').size()

    # High activity threshold (>50 tweets/day)
    days = (df['date'].max() - df['date'].min()).days
    high_activity_threshold = 50 * days

    high_activity_accounts = tweets_per_account[tweets_per_account > high_activity_threshold]

    print(f"\nHigh-activity accounts (>50 tweets/day):")
    print(f"  Threshold: {high_activity_threshold} tweets over {days} days")
    print(f"  Found: {len(high_activity_accounts)} accounts")

    # Check for automated usernames
    bot_keywords = ['bot', 'auto', 'rt_', 'news', 'feed', 'mirror']
    df['bot_username'] = df['username'].str.lower().apply(
        lambda x: any(kw in x for kw in bot_keywords) if pd.notna(x) else False
    )

    bot_username_count = df[df['bot_username'] == True]['author_id'].nunique()
    bot_username_tweets = len(df[df['bot_username'] == True])

    print(f"\nAccounts with bot-like usernames:")
    print(f"  Found: {bot_username_count} accounts")
    print(f"  Tweets: {bot_username_tweets:,} ({bot_username_tweets/len(df)*100:.1f}%)")

def main():
    """Main analysis pipeline."""
    print("="*60)
    print("XINJIANG COTTON TWITTER ANALYSIS")
    print("AgentAcademy Run 7 | Exploratory Tier")
    print("="*60)

    # Load and preprocess
    df = load_data()
    df = parse_datetime(df)

    # RQ4: Temporal dynamics first (to get spike dates)
    spike_date, spike_date_2 = analyze_temporal_dynamics(df)
    
    # RQ1: Coordinated amplification
    analyze_coordinated_amplification(df, spike_date, spike_date_2)

    # RQ2: Narrative frames
    df = analyze_frames(df)

    # RQ3: State-linked accounts
    analyze_state_linked_accounts(df)

    # RQ5: Engagement asymmetries
    analyze_engagement_asymmetries(df)

    # Bot detection
    detect_potential_bots(df)

    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print(f"\nConfidence Level: 🟢 EXPLORATORY")
    print(f"⚠️  NOT VALIDATED FOR PUBLICATION")

if __name__ == "__main__":
    main()
