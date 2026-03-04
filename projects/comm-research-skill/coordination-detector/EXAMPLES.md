# Coordination Detector: Worked Examples

## Example 1: Twitter Political Campaign (URL Coordination)

### Scenario
Dataset of 50,000 tweets about a 2024 election. Researcher suspects astroturfing.

### Detection Process

**Step 1: Extract URL shares**
```python
urls = df[df['urls'].notna()]['urls'].explode()
url_counts = urls.value_counts()
# Found 2,847 unique URLs shared
```

**Step 2: Co-link analysis (60-second window)**
```python
for url in high_frequency_urls:
    shares = df[df['urls'].str.contains(url)]
    shares = shares.sort_values('created_at')
    
    # Sliding window analysis
    for i, share in shares.iterrows():
        window = shares[
            (shares['created_at'] >= share['created_at']) &
            (shares['created_at'] <= share['created_at'] + timedelta(seconds=60))
        ]
        if len(window['user_id'].unique()) >= 3:
            flag_coordination(window)
```

**Step 3: Results**
```
URLs with coordinated sharing: 47
Accounts involved: 312
Coordination clusters: 8 distinct groups

Largest cluster:
- 89 accounts
- Shared 23 URLs within 60 seconds each time
- All accounts created within 2-week period
- Average followers: 47
- Profile pics: 78% default or stock photos
```

**Step 4: Manual validation**
Inspected 20 accounts from largest cluster:
- 18/20 showed clear bot characteristics
- 2/20 possibly authentic but suspicious

**Decision:** Remove 312 flagged accounts (0.6% of dataset). Document in methods.

---

## Example 2: Content Similarity Clustering

### Scenario
Analysis of 10,000 posts about a health policy. Need to check for copy-paste campaigns.

### Detection Process

**Step 1: Compute pairwise similarity**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer(max_features=5000)
tfidf = vectorizer.fit_transform(df['text'])
similarities = cosine_similarity(tfidf)
```

**Step 2: Cluster high-similarity posts**
```python
threshold = 0.85
clusters = []

for i in range(len(similarities)):
    similar_posts = np.where(similarities[i] > threshold)[0]
    if len(similar_posts) >= 3:
        unique_authors = df.iloc[similar_posts]['user_id'].nunique()
        if unique_authors >= 3:
            clusters.append({
                'posts': similar_posts,
                'authors': unique_authors,
                'sample_text': df.iloc[similar_posts[0]]['text']
            })
```

**Step 3: Results**
```
Clusters found: 12
Total posts in clusters: 847
Unique accounts: 203

Example cluster (n=156 posts, 89 accounts):
"The new policy will destroy small businesses and cost 
thousands of jobs. Contact your representative NOW! #StopThePolicy"

Variations found:
- "...cost THOUSANDS of jobs..."
- "...Contact your rep NOW!..."
- Added emojis, minor word changes
```

**Step 4: Assessment**
- Template-based campaign confirmed
- Mix of bots and authentic accounts using shared messaging
- Decided to FLAG but not remove (organic amplification of campaign)

**Documentation:**
```markdown
Content similarity analysis detected coordinated messaging campaign.
847 posts (8.5%) used near-identical templates.
These posts retained in analysis but coded as "campaign_coordinated=True"
for sensitivity analysis.
```

---

## Example 3: Temporal Burst Detection

### Scenario
Studying response to a breaking news event. Need to distinguish organic viral spread from coordinated amplification.

### Detection Process

**Step 1: Bin activity by minute**
```python
df['minute'] = df['created_at'].dt.floor('T')
activity = df.groupby('minute').agg({
    'id': 'count',
    'user_id': 'nunique',
    'text': lambda x: x.str.len().mean()
}).rename(columns={'id': 'posts', 'user_id': 'unique_users'})
```

**Step 2: Calculate baseline and detect anomalies**
```python
baseline_mean = activity['posts'].median()
baseline_std = activity['posts'].std()

activity['z_score'] = (activity['posts'] - baseline_mean) / baseline_std
activity['diversity_ratio'] = activity['unique_users'] / activity['posts']

# Flag: high volume + low diversity
anomalies = activity[
    (activity['z_score'] > 3) & 
    (activity['diversity_ratio'] < 0.3)
]
```

**Step 3: Results**
```
Anomalous minutes detected: 7

Minute 14:23 (highest z-score: 8.4):
- Posts: 342
- Unique users: 67 (diversity: 0.19)
- Same 67 accounts posting 5+ times each in 60 seconds
- All retweets of single source account

Minute 14:47 (z-score: 5.2):
- Posts: 198  
- Unique users: 187 (diversity: 0.94)
- Genuine viral spread, NOT coordination
```

**Step 4: Differentiation**
```
COORDINATED (14:23):           ORGANIC (14:47):
- Low diversity (0.19)         - High diversity (0.94)
- Few accounts, many posts     - Many accounts, ~1 post each
- Identical content (RTs)      - Mixed content (RTs + quotes + original)
- Accounts cluster together    - Accounts are unconnected
```

**Decision:** Remove minute 14:23 cluster from engagement analysis. Keep 14:47 as organic viral moment.

---

## Example 4: Dual-Sided Detection (Critical)

### Scenario
Analyzing discourse about territorial dispute. Two "sides": pro-Country-A and pro-Country-B.

### Detection Process

**Step 1: Classify posts by stance**
```python
# Use keyword/hashtag classification or model coding
df['stance'] = df.apply(classify_stance, axis=1)
# Results: 45% pro-A, 38% pro-B, 17% neutral
```

**Step 2: Run detection on EACH side**
```python
results = {}
for stance in ['pro-A', 'pro-B']:
    subset = df[df['stance'] == stance]
    results[stance] = {
        'colink': run_colink_detection(subset),
        'temporal': run_temporal_detection(subset),
        'content': run_content_similarity(subset),
        'profiles': run_profile_scoring(subset)
    }
```

**Step 3: Compare sides**
```
                    Pro-A       Pro-B
Accounts analyzed:  12,450      9,870
─────────────────────────────────────
Co-link flagged:    234 (1.9%)  891 (9.0%)
Temporal flagged:   156 (1.3%)  445 (4.5%)
Content clusters:   12          47
Profile score >0.6: 445 (3.6%)  1,203 (12.2%)
─────────────────────────────────────
Combined flags:     523 (4.2%)  1,847 (18.7%)
```

**Step 4: Interpretation**

⚠️ **Critical finding:** Pro-B side shows 4x higher coordination rates across ALL methods.

**Do NOT conclude:**
- "Pro-B position is wrong/illegitimate"
- "Pro-A is organic, Pro-B is astroturf"

**DO conclude:**
- "Pro-B discourse shows significantly higher coordination signatures"
- "Engagement metrics for Pro-B should be interpreted with caution"
- "After removing flagged accounts, stance distribution shifts from 45/38 to 52/31"

**Report both sides transparently:**
```markdown
Coordination detection revealed asymmetric patterns. Pro-Country-B 
accounts showed 4.5x higher coordination rates (18.7% vs 4.2%). 
We report results both with and without flagged accounts to assess 
robustness. The substantive finding (X) holds in both analyses, 
though effect size is smaller in cleaned data (d=0.45 vs d=0.62).
```

---

## Example 5: False Positive Analysis

### Scenario
Coordination detection flagged a cluster. Manual review needed.

### Flagged Cluster
```
47 accounts
All shared same URL within 45 seconds
URL: petition.site/save-local-hospital
Created: Mixed ages (some old accounts)
```

### Manual Inspection

**Account sample (n=10):**
| Account | Age | Followers | Location | Assessment |
|---------|-----|-----------|----------|------------|
| @local_mom_jane | 8yr | 234 | Town X | Authentic |
| @townx_teacher | 5yr | 567 | Town X | Authentic |
| @concerned_resident | 2mo | 12 | Town X | Uncertain |
| @save_our_nhs | 3yr | 1.2K | Town X | Activist org |
| ... | | | | |

**Context discovered:**
- Town X had public meeting about hospital closure
- Local Facebook group shared petition link
- Spike represents cross-platform mobilization

### Verdict: FALSE POSITIVE

**Characteristics of organic coordinated action:**
- Accounts have local ties (same town)
- Long account histories with diverse activity
- Clear real-world event trigger
- Natural diversity in followers/activity
- Accounts interact outside this single event

**Lesson:** Not all coordination is inauthentic. Grassroots organizing produces coordination signatures. Context matters.

**Documentation:**
```markdown
Initial detection flagged 47 accounts for URL co-sharing. 
Manual review (n=20) found 95% were authentic local residents 
responding to community meeting. Cluster retained in analysis
and coded as "grassroots_coordinated" rather than removed.
```

---

## Summary: Detection vs. Interpretation

| Finding | Detection | Interpretation |
|---------|-----------|----------------|
| Co-link cluster | Automated | Requires context |
| Temporal burst | Automated | Check diversity ratio |
| Content similarity | Automated | Template ≠ inauthentic |
| Profile scores | Automated | High FP for new accounts |
| Network patterns | Automated | Compare to organic baseline |

**The skill detects patterns. Humans interpret meaning.**

Always ask:
1. Is there a real-world explanation?
2. Are flagged accounts connected outside this event?
3. Does removal change substantive findings?
4. Am I detecting both sides fairly?
