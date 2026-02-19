# CNN News Dataset Analysis

**Analysis Date:** 2026-02-19  
**Dataset:** CNN.pkl (cleaned version)  
**Total Articles:** 983  
**Date Range:** January 2, 2015 – December 8, 2015

---

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| Total Articles | 983 |
| Columns | id, content, date, source |
| Date Range | 2015-01-02 to 2015-12-08 |
| Source | CNN (LexisNexis archive format) |

---

## 2. Content Type Distribution

The dataset contains a mix of TV transcripts and written articles:

| Content Type | Count | Percentage | Mean Word Count |
|--------------|-------|------------|-----------------|
| TV Transcripts | 368 | 37.4% | 4,480 words |
| Written Articles | 615 | 62.6% | 713 words |

**Key Finding:** Transcripts are approximately 6.3x longer than articles on average (4,480 vs 713 words). This significant structural difference has important implications for text analysis methodologies—treating both content types as equivalent would introduce substantial bias.

---

## 3. Temporal Patterns in 2015

### Monthly Distribution

| Month | Articles | Notes |
|-------|----------|-------|
| January | 115 | Charlie Hebdo attack (Jan 7), Ferguson investigation |
| February | 45 | Lowest monthly volume |
| March | 75 | Ferguson police chief resigns |
| April | 59 | Baltimore protests begin (Freddie Gray) |
| May | 63 | Amtrak crash |
| **June** | **171** | **Peak volume—Charleston church shooting (Jun 17)** |
| July | 111 | Chattanooga shooting |
| August | 107 | Campaign coverage increases |
| **September** | **41** | **Lowest monthly volume** |
| October | 83 | Oregon college shooting |
| November | 51 | Paris attacks (Nov 13) |
| December | 62 | San Bernardino attack (Dec 2) |

**Temporal Analysis:**
- **June spike (171 articles)** represents 4.2x the September nadir (41 articles), indicating event-driven coverage centered on the Charleston church shooting
- January peak (115) corresponds to Charlie Hebdo attack aftermath and Ferguson DOJ report
- The dataset shows non-uniform temporal distribution characteristic of crisis-focused sampling

### Day of Week Distribution

| Day | Count | Percentage |
|-----|-------|------------|
| Friday | 208 | 21.2% |
| Saturday | 207 | 21.1% |
| Thursday | 136 | 13.8% |
| Tuesday | 125 | 12.7% |
| Wednesday | 124 | 12.6% |
| Sunday | 98 | 10.0% |
| Monday | 85 | 8.6% |

**Finding:** Friday-Saturday account for 42.3% of all articles, suggesting either weekend-focused sampling bias or a pattern of weekend breaking news coverage. The Monday low (8.6%) is notable and warrants investigation into whether this reflects CNN's publication patterns or sampling methodology.

---

## 4. Thematic Focus

### Law Enforcement Coverage

| Metric | Value |
|--------|-------|
| Total law enforcement keyword mentions | 5,224 |
| Articles with law enforcement terms | 921 (93.7%) |

**Top Law Enforcement Terms:**

| Keyword | Frequency |
|---------|-----------|
| police | 9,511 |
| officer | 5,738 |
| gun | 6,378 |
| shooting | 5,208 |

**Analysis:** Law enforcement is the dominant thematic category, present in 93.7% of all articles. The high frequency of "police" (9,511) and "officer" (5,738) suggests the dataset is heavily focused on police-involved incidents, accountability, and reform discourse.

### Racial Coverage

| Metric | Value |
|--------|-------|
| Total racial keyword mentions | 2,317 |
| Articles with racial terms | 690 (70.2%) |

**Top Racial Terms:**

| Keyword | Frequency |
|---------|-----------|
| black | 2,112 |
| white | 1,455 |
| ferguson | 1,478 |
| charleston | 1,852 |

**Analysis:** Racial discourse appears in 70.2% of articles, with near-parity between "black" (2,112) and "white" (1,455) mentions. However, qualitative context matters:
- "Ferguson" (1,478) references a specific event focal point
- "Charleston" (1,852) appears frequently due to the June spike
- The near-equal frequency suggests comparative framing potential for racial discourse analysis

### Violence-Related Terminology

| Keyword | Frequency |
|---------|-----------|
| shooting | 5,208 |
| killed | 2,428 |
| victim | 1,844 |
| terror | 2,513 |

**Finding:** Violence-related terminology dominates the corpus, with "shooting" being the 2nd most frequent term overall. This aligns with the law enforcement focus and suggests the dataset is heavily weighted toward crisis event coverage.

### Thematic Cross-Reference

The convergence of law enforcement (93.7% prevalence) and racial terms (70.2% prevalence) suggests strong thematic overlap. Many articles likely discuss police violence, accountability, and racial justice—a reflection of 2015's emergence as a watershed year for Black Lives Matter discourse.

---

## 5. Methodological Implications

### 5.1 Content Type Stratification Required
The 6.3x word count differential between transcripts and articles precludes treating them as equivalent units. Future analyses should:
- Stratify by content type
- Compute type-specific baselines
- Consider normalizing by word count for frequency-based metrics

### 5.2 Temporal Bias Awareness
The June spike (4.2x monthly variation) and weekend concentration (42.3% Fri-Sat) indicate non-random sampling. Research questions should account for:
- Event-driven coverage patterns
- Potential over-representation of crisis narratives
- Weekday vs. weekend framing differences

### 5.3 Thematic Focus Validation
The high prevalence of law enforcement (93.7%) and violence terminology validates this dataset for:
- Police accountability discourse analysis
- Gun violence framing studies
- Crisis communication research
- Racial justice media coverage

---

## 6. Limitations

1. **Sampling Provenance Unknown:** Dataset curation methodology unclear (systematic vs. event-based vs. keyword-curated)
2. **Single Source:** CNN-only data prevents outlet comparison studies
3. **Section Metadata:** Many articles lack section categorization
4. **Temporal Scope:** Limited to 2015, precluding longitudinal analysis

---

## 7. Recommendations for Analysis

Based on these findings, recommended analytical approaches include:

1. **Comparative Framing Analysis:** Compare "police" + "black" vs. "police" + "white" collocates to identify differential framing patterns
2. **Event-Based Case Studies:** Deep-dive analysis of June (Charleston), January (Charlie Hebdo), and November (Paris) as natural experiments
3. **Content-Type Comparison:** Analyze whether transcripts vs. articles differ in police/victim language attribution
4. **Temporal Narrative Tracking:** Trace keyword trajectories before/after major events (e.g., "police brutality" mentions post-Ferguson)

---

*Analysis completed using pandas and natural language processing techniques.*
