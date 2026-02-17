# Data Sources — Post-API Era Reality (2026)

## Quick Reference

| Source | Access | Cost | Wait Time | Recommendation |
|--------|--------|------|-----------|----------------|
| **Existing Datasets** | Open | Free | None | ⭐ START HERE |
| **Bluesky** | Open API | Free | None | ⭐ Recommended |
| **Telegram** | API | Free | Days | ✅ Works well |
| **YouTube** | API key | Free tier | Hours | ✅ Works |
| **GDELT** | Open | Free | None | ✅ News/events |
| **MediaCloud** | API key | Free | Days | ✅ News |
| **Reddit** | Restricted | $$$ | Weeks | ⚠️ Consider archives |
| **TikTok** | Research API | Free | 4-8 weeks | ⚠️ Application required |
| **Meta** | Content Library | Free | 6-12 weeks | ⚠️ Application required |
| **Twitter/X** | API | $5K+/mo | Days | 💰 Usually unavailable |

## Existing Datasets (START HERE)

Most research questions can be answered with archived data:

| Repository | Focus | Access |
|------------|-------|--------|
| [Harvard Dataverse](https://dataverse.harvard.edu) | Social science | Open |
| [ICPSR](https://www.icpsr.umich.edu) | Survey + social media | Institutional |
| [Zenodo](https://zenodo.org) | Research data | Open |
| [OSF](https://osf.io) | Preregistrations + data | Open |
| [Kaggle](https://kaggle.com/datasets) | ML-ready datasets | Open |

**Search strategy**: "[platform] dataset [topic] site:dataverse.harvard.edu OR site:zenodo.org"

## Open Platforms (No Application)

### Bluesky
- **Access**: AT Protocol, completely open
- **Auth**: None required for public data
- **Limits**: None
- **Best for**: Real-time discourse, growing community

### Telegram
- **Access**: API with account
- **Auth**: API ID + hash
- **Limits**: Rate limits
- **Best for**: Public channels, group discussions

### YouTube
- **Access**: Data API v3
- **Auth**: API key (free tier)
- **Limits**: 10,000 units/day
- **Best for**: Comments, video metadata

## Gated Platforms (Application Required)

### Meta Content Library
- **Wait**: 6-12 weeks
- **Eligibility**: Academic institution required
- **Data**: Public Facebook/Instagram posts
- **Apply**: [Meta Content Library](https://developers.facebook.com/docs/content-library-api)

### TikTok Research API
- **Wait**: 4-8 weeks
- **Eligibility**: US/EU academic researchers
- **Data**: Public videos, limited
- **Apply**: [TikTok Research API](https://developers.tiktok.com/products/research-api)

## Expensive Platforms

### Twitter/X
- **Cost**: $5,000+/month (Basic API)
- **Reality**: Most researchers can't afford this
- **Alternatives**: 
  - Existing datasets (pre-2023)
  - Bluesky for similar content
  - News coverage via MediaCloud

### Reddit
- **Cost**: Negotiated (expensive)
- **Alternatives**:
  - Pushshift archives (historical)
  - Academic partnerships

## Decision Tree

```
Do you NEED new data collection?
│
├─ NO → Use existing datasets (Harvard, ICPSR, Zenodo)
│
└─ YES → Which platform?
    │
    ├─ Twitter → Can you afford $5K/mo?
    │   ├─ NO → Use existing datasets or Bluesky
    │   └─ YES → Proceed with API
    │
    ├─ Bluesky → Proceed (open)
    │
    ├─ TikTok → Apply for Research API (4-8 weeks)
    │
    ├─ Meta → Apply for Content Library (6-12 weeks)
    │
    └─ Other → Check platform docs
```

## Honest Advice

1. **Start with existing data** — It's faster, cheaper, and often better documented
2. **Budget time for applications** — Meta/TikTok take months
3. **Don't promise Twitter access** — Most institutions can't afford it
4. **Consider Bluesky** — Growing community, completely open
5. **Archive what you collect** — Platforms revoke access
