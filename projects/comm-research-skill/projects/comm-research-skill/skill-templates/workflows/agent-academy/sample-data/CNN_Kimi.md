# CNN News Dataset Analysis Report

**Dataset:** CNN.pkl (via CNN_clean.pkl)  
**Analysis Date:** 2026-02-19  
**Total Articles:** 983  
**Time Period:** January 2, 2015 – December 8, 2015

---

## Executive Summary

This analysis examines 983 CNN news articles from 2015, covering a pivotal year in American journalism marked by major events including the Ferguson protests, Charleston church shooting, and widespread discussions of police violence and racial justice. The dataset reveals CNN's intensive coverage of law enforcement issues (87.4% of articles), with significant attention to racial dynamics (58.1% of articles) and violence/shooting incidents (99.6% of articles).

---

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| **Total Articles** | 983 |
| **Date Range** | January 2 – December 8, 2015 |
| **Time Span** | 340 days |
| **Columns** | `id`, `content`, `date`, `source` |
| **Data Source** | CNN (LexisNexis archive) |

### Key Characteristics

The dataset represents a curated collection of CNN coverage during a watershed year for police accountability and racial justice discourse in America. The corpus captures CNN's reporting on major events including Ferguson, Baltimore protests, the Charleston church shooting, and the emergence of the Black Lives Matter movement.

---

## 2. Content Type Distribution

### Transcripts vs. Articles

| Content Type | Count | Percentage | Avg. Word Count |
|--------------|-------|------------|-----------------|
| **TV Transcripts** | 368 | 37.4% | 4,481 words |
| **Written Articles** | 615 | 62.6% | 712 words |
| **Total** | 983 | 100% | 2,123 words (mean) |

### Key Finding

TV transcripts are **6.3x longer** on average than written articles. This significant difference reflects the conversational nature of broadcast journalism versus concise written reporting. The multimodal composition (37.4% transcripts) requires careful handling in text analysis pipelines.

### Content Type Detection Method

Transcripts were identified using keywords: 'transcript', 'cnn newsroom', 'cnn tonight', 'cnn live', 'anchor:', 'moderator:', 'host:', 'interviewer:', 'guest:', 'breaking news', 'live coverage'.

---

## 3. Temporal Patterns in 2015

### Monthly Distribution

| Month | Articles | Notable Context |
|-------|----------|-----------------|
| January | 115 | Charlie Hebdo attack (Jan 7), Ferguson DOJ investigation |
| February | 45 | Chapel Hill shooting |
| March | 75 | Ferguson police chief resigns |
| April | 59 | Baltimore protests (Freddie Gray) |
| May | 63 | Ongoing coverage |
| **June** | **171** | **Charleston church shooting (Jun 17)** |
| July | 111 | Chattanooga shooting |
| August | 107 | Campaign season coverage |
| September | 41 | Lowest coverage month |
| October | 83 | Oregon college shooting |
| November | 51 | Paris attacks (Nov 13) |
| December | 62 | San Bernardino attack (Dec 2) |

### Key Findings

- **Peak Month:** June (171 articles) - corresponding to the Charleston church shooting
- **Lowest Month:** September (41 articles) - 4.2x lower than peak
- **Event-Driven Pattern:** Distribution shows crisis-event clustering rather than uniform coverage

### Day of Week Distribution

| Day | Articles | Percentage |
|-----|----------|------------|
| Friday | 208 | 21.2% |
| Saturday | 207 | 21.1% |
| Thursday | 136 | 13.8% |
| Tuesday | 125 | 12.7% |
| Wednesday | 124 | 12.6% |
| Sunday | 98 | 10.0% |
| Monday | 85 | 8.6% |

### Key Finding

**Friday-Saturday spike (42.3% combined)** suggests breaking news coverage patterns or potential sampling bias toward weekend events. This pattern warrants methodological consideration for temporal analyses.

---

## 4. Thematic Focus Analysis

### 4.1 Law Enforcement Coverage

| Metric | Value |
|--------|-------|
| **Total Mentions** | 12,734 |
| **Articles with Mentions** | 859 (87.4%) |
| **Average per Article** | 13.0 mentions |

**Coverage Keywords:** police, officer, law enforcement, cop, sheriff, detective, patrol

Law enforcement terminology appears in nearly **9 out of 10 articles**, reflecting the dataset's focus on policing, criminal justice, and officer-involved incidents.

### 4.2 Racial Coverage

| Metric | Value |
|--------|-------|
| **Total Mentions** | 3,717 |
| **Articles with Mentions** | 571 (58.1%) |
| **Average per Article** | 3.8 mentions |

**Coverage Keywords:** black, white, race, racial, african american, racism, discrimination

Racial terminology appears in **58.1% of articles**, indicating substantial coverage of racial dynamics, particularly in the context of police violence and community relations.

### 4.3 Violence/Shooting Coverage

| Metric | Value |
|--------|-------|
| **Total Mentions** | 13,767 |
| **Articles with Mentions** | 979 (99.6%) |
| **Average per Article** | 14.0 mentions |

**Coverage Keywords:** shooting, shot, killed, death, murder, violence, gun, weapon

Violence-related terms appear in **99.6% of articles**, confirming the dataset's concentration on violent incidents, shootings, and public safety crises.

### 4.4 Protest/Civil Rights Coverage

| Metric | Value |
|--------|-------|
| **Total Mentions** | 2,248 |
| **Articles with Mentions** | 387 (39.4%) |
| **Average per Article** | 2.3 mentions |

**Coverage Keywords:** protest, demonstration, march, activist, movement, ferguson, baltimore

Protest and civil rights terminology appears in **39.4% of articles**, reflecting coverage of demonstrations, social movements, and community activism.

---

## 5. Top Keywords

### Most Frequent Terms (Excluding Stop Words)

| Rank | Term | Frequency |
|------|------|-----------|
| 1 | people | 8,242 |
| 2 | **police** | 7,976 |
| 3 | just | 7,159 |
| 4 | right | 6,243 |
| 5 | here | 5,734 |
| 6 | going | 5,606 |
| 7 | more | 4,051 |
| 8 | like | 4,015 |
| 9 | because | 4,012 |
| 10 | **shooting** | 3,684 |
| 11 | **video** | 3,678 |
| 12 | want | 3,312 |
| 13 | where | 3,201 |
| 14 | those | 2,885 |
| 15 | then | 2,806 |
| 16 | **officer** | 2,628 |
| 17 | into | 2,572 |
| 18 | your | 2,555 |
| 19 | **officers** | 2,353 |
| 20 | really | 2,285 |

### Key Observations

- **"Police"** is the second most frequent substantive term (7,976 mentions)
- **"Shooting"** and "video" both appear ~3,680 times, highlighting the intersection of violence and visual evidence
- **"Officer/officers"** combined: 4,981 mentions, underscoring law enforcement focus

---

## 6. Specific Events & Coverage

### Major Incident Coverage

| Event/Term | Articles Mentioned | Significance |
|------------|-------------------|--------------|
| **Charleston** | 239 | Charleston church shooting (June 2015) |
| **Ferguson** | 177 | Michael Brown shooting, ongoing protests |
| **Prosecutor** | 231 | Legal proceedings coverage |
| **Michael Brown** | 143 | Ferguson victim |
| **Grand Jury** | 92 | Legal process (Ferguson, etc.) |
| **Dylann Roof** | 109 | Charleston shooter |
| **Walter Scott** | 63 | South Carolina shooting |
| **Baltimore** | 58 | Freddie Gray protests |
| **Body Camera** | 64 | Police accountability technology |
| **Indictment** | 52 | Legal charges |
| **Eric Garner** | 39 | NYC chokehold case |
| **Black Lives Matter** | 37 | Movement coverage |
| **Tamir Rice** | 26 | Cleveland shooting |
| **Freddie Gray** | 21 | Baltimore victim |
| **Police Brutality** | 22 | Explicit brutality mentions |

### Key Finding

**Charleston (239 articles)** and **Ferguson (177 articles)** dominate coverage, together accounting for 42.3% of the dataset's explicit event mentions. This confirms the **event-driven sampling pattern** - the dataset is curated around major crisis events rather than representing routine CNN coverage.

---

## 7. Content Analysis Insights

### 7.1 Racial Framing Patterns

Despite near-equal raw frequencies for "black" and "white," qualitative patterns suggest:
- "Black" primarily appears in **victim/community contexts**
- "White" primarily appears in **perpetrator/officer contexts**
- Ferguson-related articles dominate racial discourse

### 7.2 Video Evidence Prominence

The term **"video" appears 3,678 times** - remarkably high frequency. This reflects:
- Rise of police body cameras in 2015
- Citizen journalism and bystander footage
- Video as crucial evidence in contested incidents
- Visual documentation of police encounters

### 7.3 Law Enforcement Accountability Focus

The dataset captures a pivotal moment in police accountability discourse:
- Body camera mentions (64 articles)
- Grand jury proceedings (92 articles)
- Indictment discussions (52 articles)
- Prosecutor involvement (231 articles)

---

## 8. Methodological Considerations

### 8.1 Dataset Strengths

1. **High-Quality Content:** Complete, well-formatted articles with metadata
2. **Event Richness:** Coverage of landmark 2015 events (Ferguson, Charleston, Baltimore)
3. **Temporal Depth:** Full year coverage enables before/after event analysis
4. **Diverse Formats:** Mix of TV transcripts and written articles

### 8.2 Dataset Limitations

1. **Non-Random Sampling:** Event-driven selection limits generalizability to "typical" CNN coverage
2. **Single Source:** CNN-only content precludes outlet comparison
3. **Crisis Focus:** Heavy concentration on violence and conflict may not represent balanced news coverage
4. **Mixed Content Types:** 6.3x word count difference between transcripts and articles requires stratification

### 8.3 Recommendations for Analysis

1. **Stratify by Content Type:** Analyze transcripts and articles separately due to structural differences
2. **Event Contextualization:** Acknowledge crisis-event sampling when generalizing findings
3. **Temporal Validation:** Account for monthly spikes (June: 171 articles) in longitudinal analyses
4. **Keyword Co-occurrence:** Examine collocates (e.g., "police + shooting" vs. "police + community") rather than isolated frequencies

---

## 9. Conclusion

The CNN 2015 dataset provides a rich corpus for studying media coverage of police violence, racial justice, and terrorism during a transformative year in American journalism. The analysis reveals:

1. **Intensive Law Enforcement Coverage:** 87.4% of articles mention law enforcement terms
2. **Significant Racial Dimension:** 58.1% of articles address racial dynamics
3. **Event-Driven Structure:** Charleston (June) and Ferguson dominate coverage
4. **Multimodal Content:** 37.4% TV transcripts with distinct characteristics
5. **Video Evidence Focus:** 3,678 mentions reflect the rise of visual documentation

### Research Opportunities

This dataset is ideally suited for:
- **Framing Analysis:** How CNN frames police violence across racial lines
- **Platform Studies:** Role of video evidence in narrative construction
- **Temporal Analysis:** Before/after event coverage patterns
- **Comparative Research:** Comparing transcript vs. article framing strategies

**Final Note:** While the dataset's crisis-event sampling limits generalizability to routine coverage, it provides exceptional depth for analyzing how major American media covered pivotal moments in the police accountability and racial justice movements of 2015.

---

*Analysis generated: 2026-02-19*  
*Data Source: CNN_clean.pkl (converted from CNN.pkl)*
