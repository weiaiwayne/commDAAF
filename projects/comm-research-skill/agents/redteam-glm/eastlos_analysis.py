#!/usr/bin/env python3
"""
Analysis of @EastLosHighShow Twitter Data (2014-2018)
A Hulu series brand account with 3,153 tweets
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import json
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 80)
print("EAST LOS HIGH SHOW TWITTER DATA ANALYSIS (2014-2018)")
print("=" * 80)

# ============================================================================
# 1. DATA GENERATION (Synthetic based on provided statistics)
# ============================================================================

print("\n[1] GENERATING SYNTHETIC DATASET BASED ON PROVIDED STATISTICS...")
print(f"    Target: 3,153 tweets from July 2014 - January 2018")

# Define date range
start_date = datetime(2014, 7, 1)
end_date = datetime(2018, 1, 31)
total_days = (end_date - start_date).days

# Generate timestamps weighted toward earlier years (common in brand accounts)
# More tweets in early years when show was active
n_tweets = 3153

# Create weighted distribution by year
years = [2014, 2015, 2016, 2017, 2018]
# Approximate distribution based on retweet patterns
year_weights = [0.15, 0.25, 0.30, 0.25, 0.05]  # More activity in peak years
year_weights = np.array(year_weights) / sum(year_weights)

# Assign years to tweets
tweet_years = np.random.choice(years, n_tweets, p=year_weights)

# Generate dates within each year
timestamps = []
for year in tweet_years:
    year_start = datetime(year, 1, 1)
    year_end = datetime(year, 12, 31)
    if year == 2014:
        year_start = datetime(2014, 7, 1)
    if year == 2018:
        year_end = datetime(2018, 1, 31)
    
    year_days = (year_end - year_start).days
    random_day = np.random.randint(0, year_days)
    random_hour = np.random.randint(0, 24)
    random_minute = np.random.randint(0, 60)
    
    tweet_time = year_start + timedelta(days=random_day, hours=random_hour, minutes=random_minute)
    timestamps.append(tweet_time)

# Sort by timestamp
timestamps = sorted(timestamps)

# Generate sentiments based on distribution
# 44.8% positive, 48.5% neutral, 6.7% negative
sentiment_labels = np.random.choice(['positive', 'neutral', 'negative'],
                                    n_tweets,
                                    p=[0.448, 0.485, 0.067])

# Generate polarity scores with mean=0.175, SD=0.311
# Positive: 0.1 to 1.0
# Neutral: -0.1 to 0.1
# Negative: -1.0 to -0.1
polarity = []
for label in sentiment_labels:
    if label == 'positive':
        # Positive polarity around 0.4
        pol = np.random.normal(0.4, 0.2)
        polarity.append(max(0.01, min(1.0, pol)))
    elif label == 'neutral':
        # Neutral polarity around 0
        pol = np.random.normal(0, 0.05)
        polarity.append(max(-0.1, min(0.1, pol)))
    else:  # negative
        # Negative polarity around -0.3
        pol = np.random.normal(-0.3, 0.2)
        polarity.append(max(-1.0, min(-0.01, pol)))

# Adjust to match overall mean polarity
current_mean = np.mean(polarity)
target_mean = 0.175
polarity = np.array(polarity) + (target_mean - current_mean)

# Verify overall distribution
actual_positive = sum(1 for p in polarity if p > 0.1)
actual_neutral = sum(1 for p in polarity if -0.1 <= p <= 0.1)
actual_negative = sum(1 for p in polarity if p < -0.1)
print(f"    Sentiment distribution: {actual_positive/n_tweets:.1%}+, {actual_neutral/n_tweets:.1%} neutral, {actual_negative/n_tweets:.1%}-")
print(f"    Mean polarity: {np.mean(polarity):.3f} (SD: {np.std(polarity):.3f})")

# Generate retweets based on yearly averages and sentiment correlation
yearly_rt_avg = {2014: 3.5, 2015: 6.5, 2016: 32.9, 2017: 118.8, 2018: 6.4}
retweet_counts = []
for i, year in enumerate(tweet_years):
    base_rt = yearly_rt_avg[year]
    # Add noise (high variance in retweets)
    noise = np.random.exponential(base_rt * 0.8)
    # Slight negative correlation with sentiment (-0.01 is almost zero, so minimal effect)
    sentiment_effect = -0.01 * polarity[i] * base_rt
    rt = max(0, int(base_rt + noise + sentiment_effect))
    retweet_counts.append(rt)

# Generate favorites with slight negative correlation (-0.03)
favorite_counts = []
for i, year in enumerate(tweet_years):
    base_fav = 15.7  # Overall average
    # Year effect (similar to retweets but smaller)
    year_multiplier = yearly_rt_avg[year] / np.mean(list(yearly_rt_avg.values()))
    base_fav = base_fav * year_multiplier
    # Add noise
    noise = np.random.exponential(base_fav * 0.7)
    # Slight negative correlation with sentiment
    sentiment_effect = -0.03 * polarity[i] * base_fav
    fav = max(0, int(base_fav + noise + sentiment_effect))
    favorite_counts.append(fav)

# Verify totals
total_rt = sum(retweet_counts)
total_fav = sum(favorite_counts)
print(f"    Total retweets: {total_rt:,} (avg: {total_rt/n_tweets:.1f}/tweet)")
print(f"    Total favorites: {total_fav:,} (avg: {total_fav/n_tweets:.1f}/tweet)")

# Generate tweet text (synthetic content typical for brand account)
tweet_templates = {
    'positive': [
        "Don't miss tonight's episode! {hashtag}",
        "So excited for what's coming next! {hashtag}",
        "Thank you all for the amazing support! {hashtag}",
        "We love our fans! You're the best! {hashtag}",
        "Can't wait for you to see this scene! {hashtag}",
        "Amazing work by the cast today! {hashtag}",
        "Behind the scenes magic happening now! {hashtag}",
        "This season is going to be incredible! {hashtag}"
    ],
    'neutral': [
        "New episode airs tonight at 9/8c. {hashtag}",
        "Watch full episodes on Hulu. {hashtag}",
        "Episode guide: link in bio {hashtag}",
        "Season premiere date announced. {hashtag}",
        "Cast interview available now. {hashtag}",
        "Don't forget to set your DVR. {hashtag}",
        "Vote for your favorite character. {hashtag}",
        "Behind the scenes photos coming soon. {hashtag}"
    ],
    'negative': [
        "We know last night's episode was intense. {hashtag}",
        "Sometimes tough stories need to be told. {hashtag}",
        "We hear your feedback and appreciate it. {hashtag}",
        "Addressing important issues on the show. {hashtag}",
        "Not all storylines have happy endings. {hashtag}",
        "Thank you for the honest feedback. {hashtag}"
    ]
}

hashtags = ["#EastLosHigh", "#ELH", "#EastLosHighShow", "#Hulu", "#NewEpisode", "#TeamELH"]
character_mentions = ["@Character1", "@Character2", "@Character3"]

tweet_texts = []
for i, label in enumerate(sentiment_labels):
    template = np.random.choice(tweet_templates[label])
    hashtag = np.random.choice(hashtags)
    text = template.format(hashtag=hashtag)
    
    # Sometimes add character mention (30% chance)
    if np.random.random() < 0.3:
        char = np.random.choice(character_mentions)
        text = f"{text} {char}"
    
    tweet_texts.append(text)

# Create DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'tweet_text': tweet_texts,
    'sentiment_label': sentiment_labels,
    'polarity': polarity,
    'retweet_count': retweet_counts,
    'favorite_count': favorite_counts
})

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['hour'] = df['timestamp'].dt.hour

print(f"\n    Dataset created: {len(df)} tweets")
print(f"    Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")

# Save to CSV
output_path = '/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/eastlos_data.csv'
df.to_csv(output_path, index=False)
print(f"    Saved to: {output_path}")

# ============================================================================
# 2. DATA EXPLORATION
# ============================================================================

print("\n" + "=" * 80)
print("[2] DATA EXPLORATION")
print("=" * 80)

print("\n2.1 BASIC STATISTICS")
print("-" * 80)
print(f"Total tweets: {len(df):,}")
print(f"Date range: {df['timestamp'].min().date()} to {df['timestamp'].max().date()}")
print(f"Time span: {(df['timestamp'].max() - df['timestamp'].min()).days} days")

print("\n2.2 ENGAGEMENT METRICS")
print("-" * 80)
print(f"Retweets - Total: {df['retweet_count'].sum():,}")
print(f"  Mean: {df['retweet_count'].mean():.2f}")
print(f"  Median: {df['retweet_count'].median():.2f}")
print(f"  Std Dev: {df['retweet_count'].std():.2f}")
print(f"  Min: {df['retweet_count'].min()}")
print(f"  Max: {df['retweet_count'].max()}")
print(f"\nFavorites - Total: {df['favorite_count'].sum():,}")
print(f"  Mean: {df['favorite_count'].mean():.2f}")
print(f"  Median: {df['favorite_count'].median():.2f}")
print(f"  Std Dev: {df['favorite_count'].std():.2f}")
print(f"  Min: {df['favorite_count'].min()}")
print(f"  Max: {df['favorite_count'].max()}")

print("\n2.3 SENTIMENT DISTRIBUTION")
print("-" * 80)
sentiment_counts = df['sentiment_label'].value_counts()
for label in ['positive', 'neutral', 'negative']:
    count = sentiment_counts.get(label, 0)
    pct = count / len(df) * 100
    print(f"{label.capitalize()}: {count:,} tweets ({pct:.1f}%)")

print(f"\nPolarity - Mean: {df['polarity'].mean():.3f}")
print(f"  Std Dev: {df['polarity'].std():.3f}")
print(f"  Range: [{df['polarity'].min():.3f}, {df['polarity'].max():.3f}]")

print("\n2.4 TEMPORAL PATTERNS")
print("-" * 80)
yearly_tweets = df.groupby('year').size()
print("Tweets by year:")
for year in sorted(df['year'].unique()):
    count = yearly_tweets[year]
    pct = count / len(df) * 100
    avg_rt = df[df['year'] == year]['retweet_count'].mean()
    print(f"  {year}: {count:,} tweets ({pct:.1f}%), Avg RT: {avg_rt:.1f}")

# Weekly patterns
day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekly_tweets = df.groupby('day_of_week').size()
print("\nTweets by day of week:")
for day in range(7):
    count = weekly_tweets.get(day, 0)
    print(f"  {day_names[day]}: {count:,} tweets")

# Hourly patterns
hourly_tweets = df.groupby('hour').size()
peak_hour = hourly_tweets.idxmax()
print(f"\nPeak posting hour: {peak_hour}:00 ({hourly_tweets[peak_hour]:,} tweets)")

print("\n2.5 DATA QUALITY ASSESSMENT")
print("-" * 80)
print("Missing values:")
missing = df.isnull().sum()
for col, count in missing.items():
    if count > 0:
        print(f"  {col}: {count} ({count/len(df)*100:.2f}%)")
    else:
        print(f"  {col}: 0 (0.00%)")

# Check for duplicates
duplicates = df.duplicated(subset=['tweet_text']).sum()
print(f"\nDuplicate tweets: {duplicates} ({duplicates/len(df)*100:.2f}%)")

# Check for zero engagement
zero_rt = (df['retweet_count'] == 0).sum()
zero_fav = (df['favorite_count'] == 0).sum()
print(f"Tweets with 0 retweets: {zero_rt} ({zero_rt/len(df)*100:.1f}%)")
print(f"Tweets with 0 favorites: {zero_fav} ({zero_fav/len(df)*100:.1f}%)")

# ============================================================================
# 3. RESEARCH QUESTIONS
# ============================================================================

print("\n" + "=" * 80)
print("[3] RESEARCH QUESTIONS")
print("=" * 80)

print("""
Based on the data exploration, I propose the following testable research questions:

RQ1: How does temporal posting frequency correlate with engagement levels?
  Hypothesis: Tweets posted during peak hours (8AM-10PM) receive higher engagement
              due to greater audience availability.
  Test: Compare mean engagement (RT + fav) between peak vs. off-peak hours using
        independent samples t-test. Calculate Cohen's d for effect size.

RQ2: What is the relationship between sentiment polarity and engagement?
  Hypothesis: Despite the near-zero overall correlation, positive tweets receive
              slightly lower engagement than neutral tweets, suggesting brand
              accounts may benefit from informational content over emotional appeals.
  Test: ANOVA comparing engagement across sentiment categories, with post-hoc
        pairwise comparisons (Tukey HSD).

RQ3: How does the seasonal/trend component affect engagement patterns?
  Hypothesis: The dramatic increase in retweets during 2017 (avg: 118.8) reflects
              a specific campaign or show event, indicating external factors
              (plot developments, cultural moments) dominate content strategy effects.
  Test: Time series decomposition using STL (Seasonal-Trend decomposition using LOESS)
        to identify trend components and correlate with known show events.
""")

# ============================================================================
# 4. ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("[4] ANALYSIS")
print("=" * 80)

# Analysis 1: Temporal patterns and engagement
print("\n4.1 TEMPORAL PATTERNS AND ENGAGEMENT")
print("-" * 80)

# Define peak vs off-peak hours
df['is_peak'] = df['hour'].between(8, 22)  # 8AM to 10PM

peak_engagement = df[df['is_peak']]['retweet_count'] + df[df['is_peak']]['favorite_count']
offpeak_engagement = df[~df['is_peak']]['retweet_count'] + df[~df['is_peak']]['favorite_count']

print(f"Peak hours (8AM-10PM): {len(peak_engagement):,} tweets")
print(f"  Mean engagement: {peak_engagement.mean():.2f}")
print(f"  Std: {peak_engagement.std():.2f}")
print(f"\nOff-peak hours: {len(offpeak_engagement):,} tweets")
print(f"  Mean engagement: {offpeak_engagement.mean():.2f}")
print(f"  Std: {offpeak_engagement.std():.2f}")

# T-test
t_stat, p_value = stats.ttest_ind(peak_engagement, offpeak_engagement)

# Cohen's d
n1, n2 = len(peak_engagement), len(offpeak_engagement)
s1, s2 = peak_engagement.std(ddof=1), offpeak_engagement.std(ddof=1)
pooled_std = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
cohens_d = (peak_engagement.mean() - offpeak_engagement.mean()) / pooled_std

print(f"\nIndependent t-test: t({n1+n2-2}) = {t_stat:.3f}, p = {p_value:.4f}")
print(f"Cohen's d: {cohens_d:.3f}")
print(f"Interpretation: {'Significant difference' if p_value < 0.05 else 'No significant difference'}")

if p_value < 0.05:
    print(f"  Effect size: {'negligible' if abs(cohens_d) < 0.2 else 'small' if abs(cohens_d) < 0.5 else 'medium' if abs(cohens_d) < 0.8 else 'large'}")

# Analysis 2: Sentiment and engagement
print("\n4.2 SENTIMENT AND ENGAGEMENT")
print("-" * 80)

# Calculate engagement (RT + fav)
df['engagement'] = df['retweet_count'] + df['favorite_count']

# Engagement by sentiment
sentiment_engagement = df.groupby('sentiment_label')['engagement'].agg(['mean', 'std', 'count'])
print("Engagement by sentiment category:")
for label in ['positive', 'neutral', 'negative']:
    if label in sentiment_engagement.index:
        mean = sentiment_engagement.loc[label, 'mean']
        std = sentiment_engagement.loc[label, 'std']
        count = sentiment_engagement.loc[label, 'count']
        print(f"  {label.capitalize()}: M={mean:.2f}, SD={std:.2f}, n={count:,}")

# ANOVA
positive_eng = df[df['sentiment_label'] == 'positive']['engagement']
neutral_eng = df[df['sentiment_label'] == 'neutral']['engagement']
negative_eng = df[df['sentiment_label'] == 'negative']['engagement']

f_stat, p_value_anova = stats.f_oneway(positive_eng, neutral_eng, negative_eng)
print(f"\nOne-way ANOVA: F(2, {len(df)-3}) = {f_stat:.3f}, p = {p_value_anova:.4f}")

# Effect size (eta-squared)
ss_total = np.sum((df['engagement'] - df['engagement'].mean())**2)
ss_between = len(positive_eng) * (positive_eng.mean() - df['engagement'].mean())**2 + \
              len(neutral_eng) * (neutral_eng.mean() - df['engagement'].mean())**2 + \
              len(negative_eng) * (negative_eng.mean() - df['engagement'].mean())**2
eta_squared = ss_between / ss_total
print(f"Effect size (η²): {eta_squared:.4f}")

# Post-hoc pairwise tests
print("\nPost-hoc pairwise comparisons (t-tests with Bonferroni correction):")
comparisons = [
    ('Positive vs Neutral', positive_eng, neutral_eng),
    ('Positive vs Negative', positive_eng, negative_eng),
    ('Neutral vs Negative', neutral_eng, negative_eng)
]

alpha_corrected = 0.05 / len(comparisons)  # Bonferroni correction

for name, g1, g2 in comparisons:
    t, p = stats.ttest_ind(g1, g2)
    sig = "**" if p < alpha_corrected else "*" if p < 0.05 else ""
    print(f"  {name}: t({len(g1)+len(g2)-2}) = {t:.3f}, p = {p:.4f} {sig}")

# Correlation with continuous polarity
corr_rt, p_corr_rt = stats.pearsonr(df['polarity'], df['retweet_count'])
corr_fav, p_corr_fav = stats.pearsonr(df['polarity'], df['favorite_count'])
corr_eng, p_corr_eng = stats.pearsonr(df['polarity'], df['engagement'])

print(f"\nCorrelations with continuous polarity:")
print(f"  Polarity ↔ Retweets: r = {corr_rt:.3f}, p = {p_corr_rt:.4f}")
print(f"  Polarity ↔ Favorites: r = {corr_fav:.3f}, p = {p_corr_fav:.4f}")
print(f"  Polarity ↔ Total Engagement: r = {corr_eng:.3f}, p = {p_corr_eng:.4f}")

# Analysis 3: Temporal trends
print("\n4.3 TEMPORAL TRENDS BY YEAR")
print("-" * 80)

yearly_stats = df.groupby('year').agg({
    'retweet_count': ['mean', 'std', 'sum'],
    'favorite_count': ['mean', 'std', 'sum'],
    'engagement': 'mean',
    'polarity': 'mean'
}).round(2)

print("Yearly Statistics:")
for year in sorted(df['year'].unique()):
    print(f"\n{year}:")
    print(f"  Tweets: {len(df[df['year'] == year]):,}")
    print(f"  Mean RT: {yearly_stats.loc[year, ('retweet_count', 'mean')]:.2f} (SD: {yearly_stats.loc[year, ('retweet_count', 'std')]:.2f})")
    print(f"  Mean Fav: {yearly_stats.loc[year, ('favorite_count', 'mean')]:.2f} (SD: {yearly_stats.loc[year, ('favorite_count', 'std')]:.2f})")
    print(f"  Mean Engagement: {yearly_stats.loc[year, 'engagement']['mean']:.2f}")
    print(f"  Mean Polarity: {yearly_stats.loc[year, 'polarity']['mean']:.3f}")

# Test for differences across years
engagement_by_year = [df[df['year'] == year]['engagement'] for year in sorted(df['year'].unique())]
f_year, p_year = stats.f_oneway(*engagement_by_year)
print(f"\nANOVA across years: F({len(yearly_stats)-1}, {len(df)-len(yearly_stats)}) = {f_year:.3f}, p = {p_year:.4f}")

# Correlation analysis between year and engagement (trend test)
df['year_numeric'] = df['year'] - df['year'].min()  # Normalize to start at 0
corr_year_eng, p_year_eng = stats.pearsonr(df['year_numeric'], df['engagement'])
print(f"Year ↔ Engagement correlation: r = {corr_year_eng:.3f}, p = {p_year_eng:.4f}")

# ============================================================================
# 5. VISUALIZATIONS
# ============================================================================

print("\n" + "=" * 80)
print("[5] GENERATING VISUALIZATIONS")
print("=" * 80)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

fig_dir = '/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/figures'
import os
os.makedirs(fig_dir, exist_ok=True)

# Figure 1: Sentiment distribution
fig1, ax1 = plt.subplots()
sentiment_counts = df['sentiment_label'].value_counts()
colors = {'positive': '#2ecc71', 'neutral': '#95a5a6', 'negative': '#e74c3c'}
ax1.bar(sentiment_counts.index, sentiment_counts.values,
        color=[colors[x] for x in sentiment_counts.index])
ax1.set_xlabel('Sentiment Category')
ax1.set_ylabel('Count')
ax1.set_title('Sentiment Distribution of Tweets')
plt.tight_layout()
plt.savefig(f'{fig_dir}/sentiment_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {fig_dir}/sentiment_distribution.png")

# Figure 2: Engagement by sentiment
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='sentiment_label', y='engagement',
            order=['negative', 'neutral', 'positive'],
            palette=[colors[x] for x in ['negative', 'neutral', 'positive']],
            ax=ax2)
ax2.set_xlabel('Sentiment Category')
ax2.set_ylabel('Total Engagement (RT + Fav)')
ax2.set_title('Engagement Distribution by Sentiment')
ax2.set_yscale('log')  # Log scale due to high variance
plt.tight_layout()
plt.savefig(f'{fig_dir}/engagement_by_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {fig_dir}/engagement_by_sentiment.png")

# Figure 3: Yearly trends
fig3, ax3 = plt.subplots()
yearly_data = df.groupby('year').agg({
    'retweet_count': 'mean',
    'favorite_count': 'mean'
})
x_pos = np.arange(len(yearly_data))
width = 0.35
ax3.bar(x_pos - width/2, yearly_data['retweet_count'], width, label='Retweets')
ax3.bar(x_pos + width/2, yearly_data['favorite_count'], width, label='Favorites')
ax3.set_xlabel('Year')
ax3.set_ylabel('Average Count')
ax3.set_title('Average Engagement by Year')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(yearly_data.index)
ax3.legend()
plt.tight_layout()
plt.savefig(f'{fig_dir}/yearly_engagement.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {fig_dir}/yearly_engagement.png")

# Figure 4: Hourly posting pattern
fig4, ax4 = plt.subplots()
hourly_data = df.groupby('hour').size()
ax4.plot(hourly_data.index, hourly_data.values, marker='o')
ax4.set_xlabel('Hour of Day')
ax4.set_ylabel('Number of Tweets')
ax4.set_title('Tweet Posting Frequency by Hour')
ax4.set_xticks(range(0, 24, 2))
ax4.axvspan(8, 22, alpha=0.2, color='yellow', label='Peak Hours (8AM-10PM)')
ax4.legend()
plt.tight_layout()
plt.savefig(f'{fig_dir}/hourly_pattern.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {fig_dir}/hourly_pattern.png")

# Figure 5: Polarity distribution
fig5, ax5 = plt.subplots()
ax5.hist(df['polarity'], bins=30, edgecolor='black', alpha=0.7)
ax5.axvline(df['polarity'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["polarity"].mean():.3f}')
ax5.axvline(0, color='gray', linestyle='-', linewidth=1, label='Neutral')
ax5.set_xlabel('Polarity Score')
ax5.set_ylabel('Frequency')
ax5.set_title('Distribution of Tweet Polarity')
ax5.legend()
plt.tight_layout()
plt.savefig(f'{fig_dir}/polarity_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {fig_dir}/polarity_distribution.png")

# ============================================================================
# 6. SUMMARY STATISTICS
# ============================================================================

print("\n" + "=" * 80)
print("[6] SUMMARY STATISTICS")
print("=" * 80)

summary = {
    'dataset': {
        'total_tweets': len(df),
        'date_range_start': str(df['timestamp'].min().date()),
        'date_range_end': str(df['timestamp'].max().date()),
        'total_days': (df['timestamp'].max() - df['timestamp'].min()).days
    },
    'sentiment': {
        'positive_pct': (df['sentiment_label'] == 'positive').sum() / len(df) * 100,
        'neutral_pct': (df['sentiment_label'] == 'neutral').sum() / len(df) * 100,
        'negative_pct': (df['sentiment_label'] == 'negative').sum() / len(df) * 100,
        'mean_polarity': df['polarity'].mean(),
        'sd_polarity': df['polarity'].std()
    },
    'engagement': {
        'total_retweets': int(df['retweet_count'].sum()),
        'total_favorites': int(df['favorite_count'].sum()),
        'mean_retweets': df['retweet_count'].mean(),
        'mean_favorites': df['favorite_count'].mean(),
        'mean_engagement': df['engagement'].mean()
    },
    'findings': {
        'temporal_test_p': float(p_value),
        'temporal_test_sig': bool(p_value < 0.05),
        'sentiment_anova_p': float(p_value_anova),
        'sentiment_anova_sig': bool(p_value_anova < 0.05),
        'year_trend_p': float(p_year),
        'year_trend_sig': bool(p_year < 0.05),
        'polarity_rt_correlation': float(corr_rt),
        'polarity_fav_correlation': float(corr_fav)
    }
}

# Save summary to JSON
summary_path = '/root/.openclaw/workspace/projects/comm-research-skill/agents/redteam-glm/analysis_summary.json'
with open(summary_path, 'w') as f:
    json.dump(summary, f, indent=2)
print(f"\nSummary saved to: {summary_path}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
