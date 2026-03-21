# Google Trends & Time Series Validation

*Lessons from VibePoll-2026 Study (March 2026)*

## Core Lesson: Google Trends Is Harder Than It Looks

The study attempted to use Google Trends to measure public opinion in battleground states. **Core hypothesis failed** — but methodology yielded valuable lessons.

---

## Data Structure Warning

**Google Trends `interest` values are ALREADY NORMALIZED (0-100 scale)**

- They represent search frequency RELATIVE to total searches in that region
- They are NOT absolute search counts
- DO NOT divide by population — this creates artifacts

**WRONG**:
```python
# Creates meaningless values!
interest_per_capita = interest / population
```

**CORRECT**:
```python
# Use raw interest values directly
# Or use population as offset in regression
model = NegBinom(..., offset=np.log(population))
```

---

## Resolution-Matched Validation (Critical Skill)

**Rule**: Validate at the geographic level where you'll analyze.

**Why**: National signal ≠ state-level usability.

| Term | National Zero Rate | State Zero Rate | Usable? |
|------|-------------------|-----------------|---------|
| "inflation" | 2% | 12% | ✅ |
| "why is food so expensive" | 15% | 69% | ❌ |
| "am I going to be drafted" | 40% | 97% | ❌ |

**Protocol**:
1. Validate term nationally first
2. If passes (>50% non-zero), collect at state level
3. Re-compute zero rates at state level
4. Only use terms that pass BOTH checks

---

## "Realistic" Search Terms Fail

**Intuition says**: People search conversational questions.
**Reality shows**: People search 2-4 word fragments.

| Term Type | Example | Survival Rate |
|-----------|---------|---------------|
| Academic phrasing | "inflation concerns" | Low |
| Conversational | "why is food so expensive" | Very Low (69% zeros) |
| Short fragments | "gas prices" | Higher |
| Hyper-local | "ICE near me" | Best (1/25 survived) |

**Lesson**: Test before assuming. "Realistic" ≠ "searchable."

---

## Small State Problem

Google Trends suppresses low-volume results. Small states = unreliable data.

| State | Population | Zero Rate | Recommendation |
|-------|------------|-----------|----------------|
| California | 39M | <5% | ✅ Reliable |
| Texas | 30M | <5% | ✅ Reliable |
| Pennsylvania | 13M | ~20% | ⚠️ Usable with caution |
| New Hampshire | 1.4M | 64% | ❌ Flag as low-confidence |
| Maine | 1.4M | 64% | ❌ Flag as low-confidence |

**Rule**: States <3M population should be flagged as "low confidence" or excluded.

---

## Spurious Correlation Detection

### The Problem
Raw time series often show high correlations because both are trending over time.

**Example from study**:
| State | Raw r | First-Diff r |
|-------|-------|--------------|
| Nevada | .61 | .08 |
| California | .58 | −.13 |
| Wisconsin | .45 | .05 |

### The Solution: First-Differencing + Smoothing

1. **Apply rolling average** (7-day) to reduce noise
2. **Then first-difference** to remove trend
3. **Compare raw vs. differenced** correlations
4. If correlation drops >50%, likely spurious

**WRONG order**:
```python
# Over-amplifies noise!
df['diff'] = df['raw'].diff()
```

**CORRECT order**:
```python
# Smooth first, then difference
df['smoothed'] = df['raw'].rolling(7).mean()
df['diff'] = df['smoothed'].diff()
```

---

## Granger Causality Interpretation

### Test Both Directions
When testing if A causes B, also test if B causes A.

**VibePoll finding**:
- Trends → Markets: 2/14 states significant
- Markets → Trends: 4/14 states significant

**Conclusion**: Markets LEAD trends. Information flows from markets to search, not reverse.

### Report Accurately
Don't summarize from memory. Check the actual table.

**WRONG**: "0/14 states significant" (memory error)
**CORRECT**: "22/60 tests significant at p<.05" (actual count from table)

---

## Rate Limiting & Collection

### Conservative Delays
PyTrends API is fragile. Use conservative delays:

```python
# Recommended: 8-15 second delays
time.sleep(random.uniform(8, 15))
```

### Log Everything
```python
log = {
    'term': term,
    'state': state,
    'timestamp': datetime.now(),
    'success': True/False,
    'retries': n,
    'delay_used': delay
}
```

### One Term at a Time
Multi-term requests are less reliable. Request terms individually for state-level data.

---

## Quality Flags to Embed in Data

Add quality columns to your dataset, not just documentation:

```python
df['zero_rate'] = df.groupby('state')['interest'].transform(
    lambda x: (x == 0).mean()
)
df['low_confidence'] = df['zero_rate'] > 0.50
df['state_pop_small'] = df['population'] < 3_000_000
```

**Why**: Flags travel with data. Documentation can be lost.

---

## What Google Trends CAN'T Do

Based on VibePoll-2026:

- ❌ Predict election outcomes
- ❌ Forecast prediction market movements
- ❌ Replace traditional polling
- ❌ Provide reliable state-level signal for small states
- ❌ Capture nuanced sentiment (only search volume)

## What Google Trends CAN Do

- ✅ Show which issues have relative salience
- ✅ Reveal geographic variation in topic interest
- ✅ Identify hyper-local concerns (Michigan → UAW)
- ✅ Detect disengagement patterns (Nevada → low search)
- ✅ Track national-level trends (with smoothing)

---

## Minimum Checklist for Google Trends Studies

Before collecting:
- [ ] Terms are 2-4 words (not full questions)
- [ ] Terms validated nationally first
- [ ] Zero-rate threshold defined (<50%)

During collection:
- [ ] Conservative rate limiting (8-15s)
- [ ] One term per request for state-level
- [ ] All requests logged

After collection:
- [ ] Re-validate at analysis granularity
- [ ] Flag small states as low-confidence
- [ ] Quality columns embedded in data

Analysis:
- [ ] DO NOT per-capita normalize (already proportional)
- [ ] Smooth before differencing
- [ ] Test both causal directions
- [ ] Report raw AND corrected correlations

---

*Added to CommDAAF: March 2026*
*Source: VibePoll-2026 (Google Trends Public Opinion Study)*
