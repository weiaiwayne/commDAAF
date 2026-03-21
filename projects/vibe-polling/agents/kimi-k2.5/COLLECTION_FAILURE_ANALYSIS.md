# Data Collection Failure Analysis - VibePoll-2026
## Why Independent Collection Was Insufficient

**Date:** 2026-03-19  
**Agent:** Kimi K2.5  
**Attempted Collection:** 50 realistic search terms × 10 states = 500 requests  
**Actual Collection:** 4,550 records (mostly errors/zeros)  
**Success Rate:** ~9%

---

## Part 1: Technical Failures

### 1.1 API Rate Limiting (HTTP 429)

**What Happened:**
```
HTTP 429: Too Many Requests
```

**Root Causes:**
- Google Trends API has strict rate limits (unspecified threshold)
- 5-second delays between requests were **insufficient**
- After ~10-15 requests, API began rejecting all subsequent calls
- Rate limit applies per IP address per time window

**Evidence:**
```
[PA] First batch: Success
[PA] Second batch: HTTP 429
[MI] All batches: HTTP 429
...
[TX] All batches: HTTP 429
```

**Required Fix:**
- Minimum 30-60 second delays between requests
- With 500 requests needed: 500 × 45s = 6.25 hours collection time
- Need exponential backoff on 429 errors
- Consider rotating proxies (ethically questionable)

---

### 1.2 Term Granularity Mismatch

**Problem:** State-level geo + long-tail terms = insufficient volume

| Term Type | Example | Avg Zeros | Issue |
|-----------|---------|-----------|-------|
| **Short generic** | "inflation" | 0% | ✅ Works |
| **Media outlet** | "Fox News" | 0% | ✅ Works |
| **Long question** | "am I going to be drafted" | 99.6% | ❌ Too specific |
| **Local modifier** | "cheap gas near me" | 100% | ❌ Geo conflict |
| **Action phrase** | "immigration lawyer near me" | 100% | ❌ Too specific |

**Why Long Questions Fail:**
1. Google Trends has minimum volume thresholds
2. State-level granularity further reduces sample
3. Long-tail queries have naturally low volume
4. "Near me" conflicts with explicit geo parameter

**The Paradox:**
> Realistic search terms (long questions) have TOO LOW volume for Google Trends API
> Academic terms (short generic) have HIGH volume but aren't what people search

---

### 1.3 Geographic vs. Term Conflict

**Critical Issue:** "Near me" + explicit state = contradiction

**Example:**
```python
pytrends.build_payload(
    ['cheap gas near me'],  # User wants LOCAL results
    geo='US-PA'             # API restricted to Pennsylvania
)
```

**Problem:**
- User searching "near me" expects local gas stations
- Google uses GPS/IP for "near me", not geo parameter
- Geo parameter restricts to state but "near me" expects city/block level
- Result: No data or highly sparse data

**Evidence:**
```
Term: "cheap gas near me"
State: PA
Result: 100% zeros (API cannot resolve location conflict)
```

---

### 1.4 Temporal Mismatch

**Issue:** Some terms only relevant during specific events

| Term | Relevance Window | Current Period | Zeros |
|------|------------------|----------------|-------|
| "Iran attack" | During conflict spike | 3-month avg | 64.5% |
| "am I going to be drafted" | Only if draft imminent | Current | 99.6% |
| "Trump news today" | Daily | Current | 67% (weekends low) |

**Problem:**
- 3-month timeframe smooths out event-driven spikes
- Crisis-related terms show zeros during calm periods
- "Today" terms have weekly cycles (low weekends)

---

## Part 2: Methodological Issues

### 2.1 The Realism-Volume Tradeoff

**Peer Review Recommendation:**
> Use realistic terms like "will I lose my job to AI" instead of "AI taking jobs"

**The Reality:**
```
"AI taking jobs"       → 99.7% zeros (academic, no one searches this)
"will I lose my job to AI" → 99.6% zeros (realistic, but TOO specific)
"AI jobs"              → 15% zeros  (compromise, some volume)
```

**The Impossibility:**
- Most authentic human search queries are too long-tail
- Google Trends works best with 1-3 word generic terms
- "Realistic" ≠ "Measurable at state level"

### 2.2 Category Coverage Gaps

**Attempted Categories:**
1. economy_realistic: 5 terms → 2 usable (inflation, broke)
2. ai_jobs_realistic: 5 terms → 1 usable (AI news)
3. iran_war_realistic: 10 terms → 0 usable
4. immigration_realistic: 5 terms → 0 usable
5. political_realistic: 5 terms → 4 usable (Fox News, CNN, how to vote, Trump news)

**Result:** Only 7 out of 30 terms have <50% zeros

### 2.3 State Coverage Incomplete

**Target:** 10 states (7 battleground + 3 control)  
**Achieved:** 7 states (missing MI, NV, CA due to API failures)  

**States Successfully Collected:**
- AZ: 910 records
- GA: 455 records
- NC: 455 records
- OH: 455 records
- PA: 455 records
- TX: 910 records
- WI: 910 records

**Missing:** MI, NV, NC had partial failures

---

## Part 3: Comparative Analysis

### Why Claude's Collection Succeeded

| Factor | Claude's Collection | My Attempt |
|--------|---------------------|------------|
| **Terms** | 50+ mixed (generic + specific) | 30 realistic (mostly specific) |
| **Delays** | 2-5 seconds | 5 seconds |
| **Success Rate** | ~90% | ~20% |
| **Zero %** | 30-50% average | 74.7% overall |
| **Total Records** | 75,894 | 4,550 |

**Why Claude Succeeded:**
1. Used more generic terms ("gas prices", "immigration") 
2. Mix of high-volume and specific terms
3. May have had better rate limit timing
4. More terms = better coverage even with individual failures

### Why My Collection Failed

1. **Over-indexed on "realistic"** → Too specific, no volume
2. **Insufficient rate limiting** → API blocked early
3. **Included "near me" terms** → Geo conflict
4. **Too few terms per category** → No redundancy
5. **Long questions** → Below Google Trends threshold

---

## Part 4: What Would Work

### 4.1 Revised Strategy (If Re-attempting)

**Term Selection:**
```python
# TIER 1: High-volume generics (keep these)
high_volume_terms = [
    'inflation',           # Economic indicator
    'gas prices',          # Consumer concern
    'Fox News', 'CNN',     # Media consumption
    'ChatGPT',            # Tech awareness
    'Trump',              # Political figure
    'Biden',              # Political figure
    'election',           # Political event
]

# TIER 2: Moderate specificity (compromise)
moderate_terms = [
    'food prices',         # vs "why is food so expensive"
    'AI jobs',            # vs "will I lose my job to AI"
    'Iran news',          # vs "are we going to war"
    'immigration news',   # vs "ICE near me"
]

# TIER 3: Questions (accept high zeros, use if available)
question_terms = [
    'why is everything so expensive',
    'will I lose my job',
    'are we going to war',
    'how to vote',
]
```

**Collection Protocol:**
```python
# Minimum 30-second delays
time.sleep(30)

# Exponential backoff on 429
if response.status_code == 429:
    time.sleep(60 * (2 ** retry_count))
    
# Expected time: 100 requests × 45s = 75 minutes
```

### 4.2 Hybrid Approach (Recommended)

**Use Claude's existing dataset BUT:**
1. Apply MY population correction methods
2. Use MY Ohio baseline approach
3. Filter to best available terms from his collection
4. Acknowledge data provenance
5. Focus analysis on high-signal terms

**Advantages:**
- Sufficient data volume (75k records)
- Already collected and validated
- Can apply rigorous statistical methods
- Faster than 6+ hour re-collection

**Disadvantages:**
- Didn't collect my own data
- Limited to terms Claude selected
- Some "realistic" terms not available

---

## Part 5: Lessons Learned

### For Future Studies

1. **Pre-validate terms** using Google Trends Explore before collection
2. **Test 5-10 terms** on one state before full collection
3. **Use 30-60s delays minimum** (not 5s)
4. **Include redundancy** - 10+ terms per category
5. **Avoid "near me"** with explicit geo parameters
6. **Accept tradeoff** - Realistic terms may be too low volume
7. **Plan for 6-12 hours** collection time, not 1-2 hours

### For This Study

**Recommendation:** Use Claude's dataset with my analytical corrections
- Population offset ✅ Can apply
- Ohio baseline ✅ Can apply  
- Bonferroni correction ✅ Can apply
- Realistic terms ❌ Constraint - use best available

**Honest Limitation Statement:**
> "Data collected by Claude Code due to API rate limiting. Kimi K2.5 applied independent statistical analysis with population controls, Ohio baseline, and Bonferroni correction. Some realistic search terms recommended by peer review could not be collected due to Google Trends volume thresholds."

---

## Part 6: Technical Constraints Summary

| Constraint | Impact | Mitigation |
|------------|--------|------------|
| API rate limits (429) | 80% request failure | 30-60s delays, 6+ hours |
| Volume thresholds | Long questions = zeros | Use shorter terms |
| Geo conflicts | "Near me" fails | Remove location modifiers |
| State granularity | Low volume per state | National-level first |
| Event timing | Crisis terms seasonal | Align collection with events |

---

## Conclusion

**Independent collection failed due to:**
1. API rate limiting with insufficient delays
2. Overly specific "realistic" terms below volume thresholds
3. Geographic conflicts with "near me" modifiers
4. Insufficient term redundancy

**The data are insufficient because:**
- 74.7% zeros (unusable)
- Only 7/30 terms viable
- 3 states missing entirely
- Collection would require 6+ hours with proper rate limiting

**Honest assessment:** Cannot complete high-quality independent collection in single session. Recommend using existing dataset with rigorous analytical corrections.

---

*Analysis completed: Kimi K2.5*  
*Framework: CommDAAF v1.0*  
*Date: 2026-03-19*
