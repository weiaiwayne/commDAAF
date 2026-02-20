import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Load data
df = pd.read_csv('/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/red-teaming/sample-data/endsars_sample_10k.csv')
df['created_at'] = pd.to_datetime(df['created_at'])
df['date'] = df['created_at'].dt.date

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))

# 1. Daily tweet volume
ax1 = plt.subplot(2, 3, 1)
daily_counts = df.groupby('date').size()
ax1.plot(daily_counts.index, daily_counts.values, marker='o', linewidth=2, markersize=6)
ax1.axvline(x=pd.to_datetime('2020-10-26').date(), color='red', linestyle='--', alpha=0.5, label='Phase transition')
ax1.set_xlabel('Date')
ax1.set_ylabel('Tweet Count')
ax1.set_title('Daily Tweet Volume', fontsize=12, fontweight='bold')
ax1.tick_params(axis='x', rotation=45)
ax1.legend()

# 2. Retweet vs Original composition
ax2 = plt.subplot(2, 3, 2)
rt_counts = df['is_retweet'].value_counts()
colors = ['#FF6B6B', '#4ECDC4']
ax2.pie([rt_counts.get(False, 0), rt_counts.get(True, 0)], 
        labels=['Original', 'Retweet'], 
        autopct='%1.1f%%',
        colors=colors,
        explode=(0.05, 0))
ax2.set_title('Tweet Composition', fontsize=12, fontweight='bold')

# 3. Top mentioned accounts
ax3 = plt.subplot(2, 3, 3)
all_mentions = []
for mentions in df['entities_mentions'].dropna():
    if pd.notna(mentions) and mentions != '':
        mention_list = str(mentions).split(',')
        all_mentions.extend([m.strip() for m in mention_list if m.strip()])
mention_counts = Counter(all_mentions)
top_mentions = dict(mention_counts.most_common(10))
ax3.barh(list(top_mentions.keys()), list(top_mentions.values()), color='steelblue')
ax3.set_xlabel('Mentions')
ax3.set_title('Top 10 Mentioned Accounts', fontsize=12, fontweight='bold')
ax3.invert_yaxis()

# 4. Engagement distribution (log scale)
ax4 = plt.subplot(2, 3, 4)
orig_tweets = df[~df['is_retweet']]
ax4.hist(orig_tweets['favorite_count'], bins=50, alpha=0.7, color='coral', edgecolor='white')
ax4.set_xlabel('Favorite Count')
ax4.set_ylabel('Frequency')
ax4.set_title('Engagement Distribution (Original Tweets)', fontsize=12, fontweight='bold')
ax4.set_yscale('log')

# 5. Follower distribution
ax5 = plt.subplot(2, 3, 5)
unique_users = df.drop_duplicates('from_user_id')
followers = unique_users['from_user_followers_count']
followers_capped = np.clip(followers, 0, 100000)  # Cap for visualization
ax5.hist(followers_capped, bins=50, alpha=0.7, color='mediumseagreen', edgecolor='white')
ax5.set_xlabel('Follower Count (capped at 100K)')
ax5.set_ylabel('Number of Users')
ax5.set_title('User Follower Distribution', fontsize=12, fontweight='bold')

# 6. Phase comparison
ax6 = plt.subplot(2, 3, 6)
df['phase'] = pd.cut(
    pd.to_datetime(df['date']),
    bins=pd.to_datetime(['2020-10-20', '2020-10-26', '2020-11-01', '2020-11-06']),
    labels=['Phase 1\n(Oct 21-25)', 'Phase 2\n(Oct 26-31)', 'Phase 3\n(Nov 1-5)']
)
phase_vol = df.groupby('phase').size()
bars = ax6.bar(phase_vol.index, phase_vol.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax6.set_ylabel('Tweet Count')
ax6.set_title('Tweet Volume by Phase', fontsize=12, fontweight='bold')
for bar, val in zip(bars, phase_vol.values):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, f'{val:,}', 
             ha='center', va='bottom', fontsize=9)

plt.suptitle('#EndSARS Twitter Dataset Analysis', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/root/.openclaw/workspace/projects/comm-research-skill/skill-templates/workflows/red-teaming/sample-data/endsars_visualizations.png', dpi=150, bbox_inches='tight')
plt.close()

print("Visualizations saved to endsars_visualizations.png")
