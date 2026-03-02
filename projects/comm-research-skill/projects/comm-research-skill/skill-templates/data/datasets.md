# Public Research Datasets

Curated list of publicly available datasets for testing, benchmarking, and research.

---

## Quick Reference

| Category | Dataset | Size | Use For |
|----------|---------|------|---------|
| **Network** | SNAP Twitter | 400K+ nodes | Network analysis |
| **Sentiment** | Sentiment140 | 1.6M tweets | Sentiment benchmarking |
| **Topic** | 20 Newsgroups | 20K docs | Topic modeling |
| **Misinformation** | LIAR | 12K statements | Claim classification |
| **Multi-platform** | Pushshift Reddit | Billions | Large-scale analysis |

---

## 1. NETWORK DATASETS

### Stanford SNAP Collection
**URL:** https://snap.stanford.edu/data/

Essential for network analysis testing:

| Dataset | Nodes | Edges | Description |
|---------|-------|-------|-------------|
| `ego-Twitter` | 81K | 1.8M | Twitter ego networks |
| `ego-Facebook` | 4K | 88K | Facebook ego networks |
| `soc-sign-epinions` | 132K | 841K | Signed social network |
| `wiki-Vote` | 7K | 104K | Wikipedia voting |
| `email-Enron` | 37K | 368K | Email network |

```python
# Download SNAP dataset
import urllib.request
url = "https://snap.stanford.edu/data/twitter_combined.txt.gz"
urllib.request.urlretrieve(url, "twitter_network.txt.gz")
```

### Network Repository
**URL:** https://networkrepository.com/

Additional network datasets with ground-truth communities.

---

## 2. SENTIMENT & EMOTION DATASETS

### Sentiment140
**URL:** http://help.sentiment140.com/for-students

- **Size:** 1.6 million tweets
- **Labels:** Positive, Negative, Neutral
- **Format:** CSV
- **Use:** Sentiment analysis benchmarking

```python
# Load Sentiment140
import pandas as pd

# Download from: http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
columns = ['polarity', 'id', 'date', 'query', 'user', 'text']
df = pd.read_csv('training.1600000.processed.noemoticon.csv', 
                 encoding='latin-1', names=columns)
```

### SemEval Twitter Sentiment
**URL:** https://alt.qcri.org/semeval2017/task4/

- **Size:** ~50K tweets
- **Labels:** Very Negative to Very Positive (5-point)
- **Use:** Fine-grained sentiment

### GoEmotions (Google)
**URL:** https://github.com/google-research/google-research/tree/master/goemotions

- **Size:** 58K Reddit comments
- **Labels:** 27 emotion categories + neutral
- **Format:** TSV
- **Use:** Multi-label emotion classification

```python
# Load GoEmotions via HuggingFace
from datasets import load_dataset
dataset = load_dataset("go_emotions")
```

### TweetEval
**URL:** https://github.com/cardiffnlp/tweeteval

Unified benchmark for tweet classification:
- Sentiment (3-class)
- Emotion (4-class)
- Hate speech
- Offensive language
- Irony detection
- Stance detection

```python
from datasets import load_dataset
dataset = load_dataset("tweet_eval", "sentiment")
```

---

## 3. TOPIC MODELING DATASETS

### 20 Newsgroups
**URL:** http://qwone.com/~jason/20Newsgroups/

- **Size:** 20,000 documents
- **Topics:** 20 newsgroups
- **Use:** Topic modeling benchmarking

```python
from sklearn.datasets import fetch_20newsgroups
data = fetch_20newsgroups(subset='all')
```

### Wikipedia Articles
**URL:** https://dumps.wikimedia.org/

- **Size:** Varies
- **Use:** Large-scale topic modeling

### Reuters-21578
**URL:** https://archive.ics.uci.edu/ml/datasets/reuters-21578

- **Size:** 21,578 documents
- **Labels:** 135 categories
- **Use:** Multi-label text classification

---

## 4. MISINFORMATION & FACT-CHECKING

### LIAR Dataset
**URL:** https://www.cs.ucsb.edu/~william/data/liar_dataset.zip

- **Size:** 12,800 statements
- **Labels:** 6 fine-grained labels (pants-fire to true)
- **Source:** PolitiFact
- **Use:** Claim classification

### FakeNewsNet
**URL:** https://github.com/KaiDMML/FakeNewsNet

- **Size:** 23K news articles
- **Labels:** Real/Fake
- **Sources:** PolitiFact, GossipCop
- **Includes:** Social context (user engagements)

### COVID-19 Misinformation
**URL:** https://github.com/MickeysClubhouse/COVID-19-rumor-dataset

Various COVID misinformation datasets for health communication research.

---

## 5. REDDIT DATASETS

### Pushshift Reddit Archives
**URL:** https://files.pushshift.io/reddit/

- **Size:** Billions of posts/comments
- **Format:** JSONL (compressed)
- **Coverage:** 2005-2023 (partial after 2023)

```python
# Sample: Load one month of comments
import zstandard
import json

with open('RC_2020-01.zst', 'rb') as fh:
    dctx = zstandard.ZstdDecompressor()
    with dctx.stream_reader(fh) as reader:
        for line in reader:
            comment = json.loads(line)
            # Process comment
```

### Subreddit-specific Datasets

| Subreddit | Dataset | Size | Topic |
|-----------|---------|------|-------|
| r/politics | Political discourse | Large | Political comm |
| r/science | Science discussion | Large | Science comm |
| r/changemyview | Persuasion | 34K | Argumentation |
| r/AskReddit | Q&A | Massive | General |

---

## 6. TWITTER/X DATASETS

### DocNow Tweet Catalog
**URL:** https://catalog.docnow.io/

Curated collections of Tweet IDs for research events:
- Elections
- Social movements
- Breaking news
- Public health events

**Note:** Must hydrate IDs using Twitter API (costs apply post-2023)

### TweetSets Archive
**URL:** https://tweetsets.library.gwu.edu/

George Washington University collections.

### Internet Archive Twitter Stream
**URL:** https://archive.org/details/twitterstream

Historical Twitter samples (check availability).

---

## 7. TELEGRAM DATASETS

### Telegram Dataset (TGDataset)
**URL:** https://github.com/nicola-seb/telegram-dataset

Public Telegram channels and groups data.

### COVID Telegram Dataset
Various research-specific Telegram datasets in academic repositories.

---

## 8. YOUTUBE DATASETS

### YouTube-8M
**URL:** https://research.google.com/youtube8m/

- **Size:** 8 million videos
- **Labels:** 4,800 classes
- **Use:** Video classification

### YouTube Comments Datasets
**URL:** Various on Kaggle

Search Kaggle for "YouTube comments" for labeled comment datasets.

---

## 9. MULTI-PLATFORM / CROSS-PLATFORM

### Social Computing Data Repository (ASU)
**URL:** http://socialcomputing.asu.edu/pages/datasets

Multiple platforms: Twitter, Digg, YouTube, MySpace

### Harvard Dataverse - Social Media
**URL:** https://dataverse.harvard.edu/

Search for social media research datasets.

### ICPSR Social Media Archive
**URL:** https://www.icpsr.umich.edu/

Requires institutional access for some datasets.

---

## 10. COORDINATED BEHAVIOR / BOT DETECTION

### Cresci Bot Dataset
**URL:** https://botometer.osome.iu.edu/bot-repository/datasets.html

Labeled bot/human accounts for validation.

### Twitterbot Dataset
Human-annotated Twitter bot datasets for research.

---

## Dataset Selection Guide

| Research Task | Recommended Dataset | Why |
|---------------|---------------------|-----|
| **Sentiment benchmarking** | Sentiment140, TweetEval | Large, labeled, standard |
| **Network analysis** | SNAP Twitter | Clean, documented |
| **Topic modeling** | 20 Newsgroups | Standard benchmark |
| **Misinformation** | LIAR, FakeNewsNet | Labeled claims |
| **Reddit research** | Pushshift | Comprehensive |
| **Emotion detection** | GoEmotions | Fine-grained labels |
| **Bot detection** | Cresci Dataset | Verified labels |

---

## Data Citation Template

When using public datasets, cite properly:

```bibtex
@misc{sentiment140,
  author = {Go, Alec and Bhayani, Richa and Huang, Lei},
  title = {Twitter Sentiment Classification using Distant Supervision},
  year = {2009},
  url = {http://help.sentiment140.com/for-students}
}

@inproceedings{liar,
  author = {Wang, William Yang},
  title = {``Liar, Liar Pants on Fire'': A New Benchmark Dataset for Fake News Detection},
  booktitle = {ACL},
  year = {2017}
}
```

---

## Ethical Considerations

1. **Check terms of use** for each dataset
2. **Respect privacy** — don't re-identify anonymized users
3. **Acknowledge limitations** — datasets may be biased or outdated
4. **Don't redistribute** without permission
5. **Cite original sources** in publications
