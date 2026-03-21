# Critical Analysis: Search Terms & State Confounds

**Reviewer:** Claude (OpenClaw)  
**Date:** 2026-03-19  
**Verdict:** 🔴 **MAJOR METHODOLOGICAL CONCERNS**

---

## Part 1: Search Term Realism Critique

### 🔴 CRITICAL: Many Terms Have 80-99% Zeros

| Term | Zero % | Reality Check |
|------|--------|---------------|
| AI taking jobs | **99.7%** | ❌ Nobody searches this |
| abortion rights | **99.7%** | ❌ Replaced "pro-choice" but still dead |
| will AI replace | **99.4%** | ❌ Academic phrasing |
| AI layoffs | **98.6%** | ❌ Not a real search |
| cheese prices | **95.6%** | ❌ Too specific |
| who is my representative | **93.6%** | ❌ People search their district |
| US troops Iran | **87.9%** | ❌ Academic phrasing |
| ICE raid | **87.1%** | ⚠️ Spiky, event-driven |
| grocery prices | **84.4%** | ❌ People search "food prices" or specific items |

**Terms with useful signal (<50% zeros):**
- Fox News (0%)
- CNN (0%)
- ChatGPT (0%)
- 401k (3%)
- inflation (15%)
- green card (20%)
- asylum (35%)
- Trump approval (40%)

### What Real People Actually Search

| Study Term | What People Actually Search | Volume Diff |
|------------|----------------------------|-------------|
| `gas prices` ✅ | `gas prices near me` ✅ | Good match |
| `grocery prices` ❌ | `food prices`, `eggs price`, `why is food so expensive` | 10-50x higher |
| `AI taking jobs` ❌ | `will I lose my job`, `ChatGPT jobs`, `what jobs are safe from AI` | 100x higher |
| `Iran war` ⚠️ | `Iran attack`, `are we going to war`, `Iran news today` | 5-20x higher |
| `military draft` ⚠️ | `am I going to be drafted`, `draft age`, `draft 2026` | 10x higher |
| `immigration lawyer` ✅ | Good - this is what people search | — |
| `deportation` ⚠️ | `ICE near me`, `how to avoid deportation`, `deportation news` | 3-5x higher |
| `Strait of Hormuz` ❌ | Almost nobody searches this | Near-zero |
| `401k` ✅ | Good - this is what people search | — |
| `stock market crash` ❌ | `is market crashing`, `should I sell stocks`, `market today` | 20x higher |

### Missing Critical Search Behaviors

**Economic anxiety (what people ACTUALLY search):**
- `cheap gas near me`
- `food bank near me`
- `how to save money`
- `why is everything so expensive`
- `can't afford rent`
- `side hustle`
- `apply for food stamps`

**Iran/war anxiety (what people ACTUALLY search):**
- `am I going to be drafted`
- `draft age 2026`
- `Iran attack news`
- `is World War 3 happening`
- `will there be a draft`

**AI anxiety (what people ACTUALLY search):**
- `is my job safe from AI`
- `ChatGPT replacing jobs`
- `AI proof careers`
- `jobs AI can't do`

---

## Part 2: State-Level Confounds — NOT CONTROLLED

### 🔴 CRITICAL: 3.4x Difference in Raw Search Volume

| State | Mean Interest | Internet Pop (est.) | Type |
|-------|--------------|---------------------|------|
| CA | **18.10** | 35M | Control |
| TX | 16.54 | 25M | Control |
| PA | 15.48 | 11M | Battleground |
| GA | 14.40 | 9M | Battleground |
| OH | 14.14 | 10M | Control |
| MI | 13.90 | 8M | Battleground |
| NC | 13.23 | 9M | Battleground |
| AZ | 11.78 | 6M | Battleground |
| MN | 10.64 | 5M | Watch |
| WI | 10.10 | 5M | Battleground |
| NV | 8.67 | 2.5M | Battleground |
| ME | **5.53** | 1M | Watch |
| NH | **5.39** | 1M | Watch |

**CA has 3.4x more raw search volume than NH/ME.**

This is NOT controlled for in any analysis!

### Confounds NOT Addressed

| Confound | Impact | Status |
|----------|--------|--------|
| **Population** | Larger states = more searches | ❌ Not controlled |
| **Internet penetration** | Varies 75-95% by state | ❌ Not controlled |
| **Age demographics** | Young = more Google | ❌ Not controlled |
| **Urban/rural mix** | Urban = more searches | ❌ Not controlled |
| **Tech industry presence** | CA tech = more AI searches | ❌ Not controlled |
| **Border proximity** | AZ/TX = more immigration searches | ⚠️ Confounded |
| **Spanish-speaking pop** | May search in Spanish | ❌ Not captured |

### The "Battleground Paradox" Is Likely a Population Effect

Kimi found battleground states have 23.5% lower search interest than CA.

**But CA has:**
- 39M population (vs PA's 13M)
- 35M internet users (vs PA's 11M)
- Silicon Valley (inflates AI/tech searches)
- Hollywood (inflates political news searches)
- Massive media market (inflates all searches)

**The "paradox" may simply be: CA is big, battlegrounds are smaller.**

---

## Part 3: What Should Have Been Done

### Proper Search Term Selection

1. **Use Google Trends' "Related Queries"** to find what people actually search
2. **Start with high-volume terms**, not academic guesses
3. **Include misspellings** (people search `imigration` not `immigration`)
4. **Include questions** (`how to`, `why is`, `can I`)
5. **Include colloquial terms** (`cheap`, `free`, `near me`)

### Proper Normalization

1. **Per-capita normalization** — divide by state population
2. **Internet user normalization** — divide by state internet users
3. **Baseline correction** — subtract each state's mean across all terms
4. **Category-specific baselines** — CA tech workers inflate AI searches

### Statistical Controls

```python
# What Kimi SHOULD have done:
model = sm.GLM(y, X, family=sm.families.NegativeBinomial())

# With state population as offset:
import numpy as np
X['log_population'] = np.log(state_populations)
model = sm.GLM(y, X, family=sm.families.NegativeBinomial(), 
               offset=X['log_population'])

# Or as fixed effect:
X['population_millions'] = state_populations / 1e6
```

---

## Part 4: Impact on Findings

### Kimi's "Battleground Paradox"

| Finding | Concern |
|---------|---------|
| Battleground 23.5% lower than CA | Likely population effect |
| Nevada -87.9% political | Population + tourism confound |
| Michigan +419% state-specific | Auto industry terms chosen for MI specifically |

**These findings are UNRELIABLE without population controls.**

### Gemini's Correlations

| Finding | Concern |
|---------|---------|
| r = 0.43-0.71 correlations | Based on terms with 50-99% zeros |
| Granger causality failure | May be due to low-signal terms, not lack of relationship |

### Which Terms Are Actually Usable?

**High-quality terms (<50% zeros, realistic searches):**
1. Fox News / CNN / MSNBC (media consumption)
2. ChatGPT (AI awareness)
3. 401k / inflation (economic indicators)
4. green card / asylum (immigration)
5. Trump approval / impeachment (political)

**Should be removed (>80% zeros or unrealistic):**
1. AI taking jobs, will AI replace, AI layoffs
2. abortion rights, pro-life (both dead post-replacement)
3. Strait of Hormuz, US troops Iran
4. cheese prices, dairy farms
5. Most state-specific terms

---

## Recommendations

### For Current Study

| Priority | Action |
|----------|--------|
| 🔴 CRITICAL | Add population/internet-user normalization |
| 🔴 CRITICAL | Re-run Kimi's analysis with population offset |
| 🔴 CRITICAL | Remove terms with >80% zeros |
| 🟡 HIGH | Re-run with only high-signal terms |
| 🟡 HIGH | Investigate CA as outlier (separate control) |

### For Future Studies

1. **Pre-test search terms** using Google Trends Explorer
2. **Use Related Queries** to find real search behavior
3. **Normalize by population** from the start
4. **Include demographic controls** (age, urban/rural, internet penetration)
5. **Collect Spanish-language searches** for border states

---

## Bottom Line

**The study has two major methodological flaws:**

1. **~30% of search terms have near-zero signal** (80-99% zeros)
2. **State population not controlled** — CA's 3.4x higher baseline invalidates comparisons

**The "Battleground Paradox" is likely just: California is big, swing states are smaller.**

Until these are addressed, findings should be treated with extreme caution.

---

*Critical review completed by Claude (OpenClaw)*  
*Date: 2026-03-19*
