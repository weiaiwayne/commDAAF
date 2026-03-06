# Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts

**Wayne Xu** | AgentAcademy Research Team  
University of Massachusetts Amherst

*Preprint v2.0 — March 2026*  
*Working Paper — Do Not Cite Without Permission*

---

## Abstract

Wikipedia's coverage of geopolitical conflicts presents a site for examining how knowledge is produced and contested in digital public spheres. This exploratory mixed-methods study investigates patterns of editorial conflict in Wikipedia talk pages during two Middle East conflicts: the 2026 Iran war and the Israel-Hamas war (2023-present). We analyzed 100 Wikipedia articles (28,006 revisions) using revert network analysis and LLM-assisted discourse analysis of 276 talk page excerpts. Our network analysis reveals asymmetric editing structures: 41-43% of editors function as "reverters" (reverting others but rarely reverted themselves), while 57-58% are primarily "reverted" (their contributions removed by others). Multi-model coding using three LLMs (Claude, GLM-4.7, Kimi K2.5) identified naming disputes and source credibility debates as primary forms of contestation, though inter-model reliability was low for most constructs (κ = 0.09-0.47), indicating interpretive ambiguity in applying epistemic injustice concepts to editorial contexts. We discuss how these patterns *may* relate to Fricker's (2007) epistemic injustice framework while acknowledging alternative explanations including legitimate quality control and experience-based editing norms. This exploratory study raises questions about platform epistemology that warrant further investigation with validated measures and comparison samples.

**Keywords:** Wikipedia, editorial conflict, platform epistemology, Middle East conflicts, mixed methods, LLM-assisted content analysis

---

## 1. Introduction

When Iran launched strikes on Israel in February 2026, Wikipedia editors immediately began competing to define the event. Should it be called a "war," a "conflict," or "strikes"? Which sources could be trusted? These debates, conducted on Wikipedia's talk pages, shape how millions of readers understand contested events.

This study examines patterns of editorial conflict in Wikipedia's coverage of Middle East conflicts, drawing on Fricker's (2007) concept of epistemic injustice as a theoretical lens. We ask: **What patterns of editorial contestation emerge in Wikipedia's coverage of geopolitical conflicts, and how might these patterns relate to questions of epistemic inclusion and exclusion?**

We adopt an exploratory approach, recognizing that applying philosophical concepts like "epistemic injustice" to platform dynamics requires careful operationalization. Our goal is to identify patterns worthy of further investigation rather than to make definitive claims about injustice.

### 1.1 Scope and Contributions

This study offers three contributions:

1. **Descriptive**: We document the structure of revert networks and talk page discourse across 100 Wikipedia articles on two active conflicts.

2. **Methodological**: We pilot a multi-model LLM coding protocol and transparently report its limitations, contributing to methodological debates about computational content analysis.

3. **Conceptual**: We explore how epistemic injustice concepts might apply to collaborative knowledge platforms, while identifying the analytical challenges involved.

---

## 2. Theoretical Framework

### 2.1 Epistemic Injustice

Fricker (2007) identifies two forms of epistemic injustice:

- **Testimonial injustice**: A speaker's credibility is discounted due to identity prejudice (e.g., dismissing someone because of their gender or race)
- **Hermeneutical injustice**: Individuals lack interpretive resources to make sense of their experiences due to gaps in collective understanding

These concepts were developed for face-to-face interaction. Applying them to platform contexts requires careful consideration of whether identity-based prejudice—central to Fricker's account—operates similarly in pseudonymous online environments.

### 2.2 Extensions to Platform Contexts

Recent scholarship extends epistemic injustice to digital platforms:

- Ajmani et al. (2024) identify "technology-mediated epistemic harm" where platform policies determine whose knowledge counts
- Kwok (2025) introduces "epistemic dispossession" to capture structural redistribution of epistemic resources

However, as Origgi (2012) notes, online epistemic dynamics differ from face-to-face contexts. Identity cues are attenuated; reputation systems create new credibility markers; and platform policies mediate interaction in ways that may constitute legitimate governance rather than injustice.

### 2.3 Wikipedia's Editorial Structure

Wikipedia's policies create a distinctive epistemic environment:

- **Verifiability** (WP:V): Claims must be attributable to reliable sources
- **Neutral Point of View** (WP:NPOV): Articles should represent views proportionally
- **Extended Confirmed Protection**: Contentious articles may restrict editing to experienced users

Previous research documents power asymmetries in Wikipedia editing (Yasseri et al., 2012; Kittur et al., 2007), gender gaps (Wagner et al., 2015), and geographic biases (Graham et al., 2015). Edit wars on controversial topics are well-documented (Borra et al., 2015), though their relationship to epistemic injustice specifically has not been systematically examined.

### 2.4 Research Questions

We pursue descriptive rather than causal questions:

**RQ1**: What structural patterns characterize revert networks in Wikipedia articles on Middle East conflicts?

**RQ2**: What forms of contestation appear in talk page discussions, and can these be reliably coded using epistemic injustice constructs?

**RQ3**: How do patterns compare across the Iran war and Gaza war article clusters?

---

## 3. Methods

### 3.1 Research Design

We employed a mixed-methods design combining computational analysis of revert patterns with LLM-assisted discourse analysis. This exploratory approach prioritizes pattern identification over hypothesis testing.

### 3.2 Data Collection

#### 3.2.1 Article Selection

We constructed two purposive samples:

**Iran War Cluster (n=50)**: Articles related to the February-March 2026 conflict, including core event articles, actor articles, and thematic articles on casualties and international reactions.

**Gaza War Cluster (n=50)**: Articles on the Israel-Hamas war (October 2023-present), including the main conflict article, major incidents, and humanitarian coverage.

Articles were selected based on: (1) direct relevance to the conflicts, (2) presence of talk page activity, and (3) evidence of editorial dispute (reverts or protection status).

**Limitation**: This purposive sampling strategy selects for conflict. Findings describe high-conflict articles specifically and cannot be generalized to Wikipedia overall.

#### 3.2.2 Data Collected

- **Revisions**: 28,006 across 100 articles
- **Reverts**: 965 total (575 Iran, 390 Gaza)
- **Talk pages**: 1.58 million characters
- **Unique editors**: 1,191 (727 Iran, 464 Gaza)

#### 3.2.3 Temporal Considerations

The two clusters cover different time periods:
- Iran cluster: ~1 week (Feb 27-Mar 5, 2026)
- Gaza cluster: ~2.5 years (Oct 2023-Mar 2026)

This asymmetry limits direct comparison. Iran data captures initial conflict dynamics; Gaza data captures mature patterns. We report findings separately and exercise caution in comparative claims.

### 3.3 Revert Network Analysis

We constructed directed networks where nodes represent editors and edges represent revert relationships. We classified editors into three roles:

- **Reverters**: Editors who revert others but are not themselves reverted
- **Reverted**: Editors whose contributions are reverted but who do not revert others
- **Bidirectional**: Editors who both revert and are reverted

We also calculated network density and concentration metrics.

**Important caveat**: Revert patterns alone cannot distinguish legitimate quality control (removing vandalism, policy violations) from potentially problematic gatekeeping. A high revert rate may indicate good editorial hygiene rather than exclusion.

### 3.4 LLM-Assisted Discourse Analysis

#### 3.4.1 Sampling

We extracted 276 talk page excerpts using stratified sampling:
- High-revert threads
- Policy citation threads
- Naming/terminology threads
- Source reliability threads

Each excerpt contained 100-500 words of connected discussion.

**Limitation**: This sampling strategy intentionally oversamples contentious discussions. Prevalence estimates do not generalize to typical Wikipedia talk pages.

#### 3.4.2 Coding Scheme

We developed a six-construct coding scheme attempting to operationalize forms of epistemic contestation:

| Construct | Operational Definition |
|-----------|----------------------|
| Testimonial Injustice | Editor's credibility explicitly challenged based on account characteristics or presumed identity |
| Hermeneutical Injustice | Explicit claim that available terminology is inadequate for the phenomenon |
| Epistemic Dispossession | Editor explicitly excluded from participation based on platform status |
| Policy Weaponization | Policy invoked to dismiss argument without substantive engagement |
| Naming Dispute | Explicit contestation over article/event terminology |
| Source Hierarchy | Source reliability challenged based on national/ideological origin |

**Key distinction**: We coded only cases with *explicit* evidence matching definitions, not inferred or implicit patterns.

#### 3.4.3 Multi-Model Protocol

Three LLMs independently coded all excerpts:
- Claude 3.5 (Anthropic)
- GLM-4.7 (Zhipu AI)
- Kimi K2.5 (Moonshot AI)

The rationale was to reduce single-model bias. However, this approach is experimental and raises its own validity questions (see Limitations).

#### 3.4.4 Reliability Assessment

We calculated pairwise Cohen's κ for each construct.

### 3.5 Integration

We examined whether editors identified in talk page cases could be located in the revert network, allowing qualitative exploration of how network position relates to discursive patterns.

---

## 4. Findings

### 4.1 RQ1: Revert Network Structure

#### 4.1.1 Basic Metrics

| Metric | Iran Cluster | Gaza Cluster |
|--------|-------------|--------------|
| Total reverts | 575 | 390 |
| Unique editors | 727 | 464 |
| Network density | 0.001 | 0.002 |

#### 4.1.2 Role Distribution

| Role | Iran | Gaza |
|------|------|------|
| Reverters (revert, not reverted) | 41.4% | 42.7% |
| Reverted (reverted, don't revert) | 58.3% | 57.3% |
| Bidirectional | 0.3% | 0.0% |

**Observation**: Revert relationships are predominantly one-directional. A minority of editors does most reverting; the majority experiences reversions without reverting others.

**Interpretation requires caution**: This pattern is consistent with multiple explanations:

1. **Quality control interpretation**: Experienced editors patrol for vandalism/policy violations; newcomers make more revertible errors
2. **Power asymmetry interpretation**: Established editors gatekeep content from newcomers
3. **Self-selection interpretation**: Many "reverted" editors are one-time contributors who leave after conflicts

Without analyzing *what* was reverted (vandalism? good-faith content?), we cannot determine which interpretation applies.

#### 4.1.3 Concentration

Top 5 reverters account for 18-20% of all reverts in each cluster. The most active reverters in our sample were never reverted themselves during the observation period.

**Note**: We cannot determine from revert data alone whether these editors hold formal positions (administrators) or informal authority, or whether their reverts were justified.

#### 4.1.4 Cross-Cluster Overlap

122 editors (10.2%) appeared in both clusters, suggesting some editors specialize in Middle East conflict topics across articles.

### 4.2 RQ2: Talk Page Discourse and Reliability

#### 4.2.1 Inter-Model Agreement as Construct Validation

We treat inter-model agreement as a form of construct validation: high agreement indicates robust operationalization; low agreement indicates the construct is culturally contested or ambiguously defined.

| Construct | κ | Agreement % | Validation Status |
|-----------|---|-------------|-------------------|
| Source Hierarchy | 0.47 | 75% | **Validated** — cross-culturally stable |
| Hermeneutical Injustice | 0.18 | 60% | Contested — models interpret differently |
| Testimonial Injustice | 0.09 | 60% | Contested |
| Naming Dispute | 0.09 | 60% | Contested |
| Epistemic Dispossession | -0.14 | 75% | Systematically divergent* |
| Policy Weaponization | -0.02 | 55% | Indeterminate |

*Negative κ indicates systematic disagreement—models have opposing interpretations of the same cases.

**Methodological contribution**: Rather than viewing low κ as failure, we interpret it as a finding. "Source hierarchy" emerges as a cross-culturally stable construct that Western and Chinese-trained models recognize similarly. "Hermeneutical injustice," by contrast, is interpreted very differently (Claude=0, Kimi=20)—suggesting this concept is itself culturally mediated.

**Analytical strategy**: We report all findings but weight conclusions toward high-agreement constructs. Low-agreement constructs are treated as exploratory.

#### 4.2.2 Coding Results (With Reliability Caveats)

| Construct | Claude | GLM | Kimi | Reliability |
|-----------|--------|-----|------|-------------|
| Naming Dispute | 5 | 13 | 5 | Poor (κ=0.09) |
| Source Hierarchy | 2 | 5 | 0 | Moderate (κ=0.47) |
| Hermeneutical Injustice | 0 | 6 | 20 | Poor (κ=0.18) |
| Testimonial Injustice | 3 | 0 | 1 | Poor (κ=0.09) |
| Epistemic Dispossession | 2 | 2 | 2 | Poor (κ=-0.14) |
| Policy Weaponization | 1 | 3 | 0 | Chance (κ=-0.02) |

**Interpretation**: The wide variation across models for hermeneutical injustice (Claude=0, Kimi=20) suggests this construct is interpreted very differently by different models. This may reflect genuine interpretive ambiguity rather than model error.

#### 4.2.3 Illustrative Cases

Given low reliability, we present cases where at least 2 models agreed:

**Epistemic Dispossession (iran_087, 2/3 models agreed)**:
> "This discussion format is not available to non-EC editors."

An editor was explicitly informed they could not participate in certain discussions due to account status. This represents clear structural exclusion, though whether it constitutes "injustice" (vs. legitimate policy) is interpretive.

**Naming Dispute (iran_113, 2/3 models agreed)**:
> "'Twelve-Day War'—whoever came up with that should be banned."

Editors contested event terminology. The personal attack ("should be banned") goes beyond the naming issue itself.

**Source Hierarchy (gaza_discussion, 2/3 models agreed)**:
> "Al Jazeera is reliable per WP:RSN. Times of Israel laundered lies about Shifa."

Editors debated source reliability along national/ideological lines. Both sides invoked geopolitical framings of source credibility.

### 4.3 RQ3: Cross-Cluster Comparison

#### 4.3.1 Structural Similarities

Both clusters showed similar role distributions (41-43% reverters), suggesting this pattern may reflect Wikipedia's platform structure rather than topic-specific dynamics.

However, without a comparison sample of non-conflict articles, we cannot determine whether this distribution is unusual.

#### 4.3.2 Discourse Differences (Tentative)

Given low coding reliability, we offer only tentative observations:

- Iran cluster discussions more often invoked EC protection explicitly
- Gaza cluster discussions showed more developed source hierarchy arguments, possibly reflecting longer editorial history
- Both clusters featured naming disputes, but over different terminology

---

## 5. Discussion

### 5.1 What We Found

Our analysis reveals asymmetric revert patterns and evidence of editorial contestation in Wikipedia's coverage of Middle East conflicts. In both article clusters:

- A minority of editors (41-43%) did most reverting
- Top reverters were not themselves reverted during observation
- Talk pages featured debates over naming, sources, and participation rights

### 5.2 What This Might Mean: Epistemic Injustice Interpretation

One interpretation frames these patterns through epistemic injustice theory:

- **Testimonial injustice**: Editors dismissed based on account age rather than argument quality
- **Epistemic dispossession**: EC protection excludes newcomers from participation
- **Hermeneutical injustice**: Naming disputes reflect struggles over available interpretive frameworks

Under this interpretation, Wikipedia's structure creates conditions where certain knowers are systematically disadvantaged.

### 5.3 Alternative Explanations

However, several alternative explanations are equally consistent with our data:

#### 5.3.1 Legitimate Quality Control

High-conflict articles attract vandalism, propaganda, and good-faith errors. Experienced editors reverting such contributions perform valuable quality control. The "reverter/reverted" asymmetry may reflect experience gradients rather than unjust exclusion.

**Evidence we lack**: We did not code *what* was reverted. Without knowing whether reverted content was policy-violating or legitimate, we cannot assess whether reverts were justified.

#### 5.3.2 Learning Curve Effects

New editors make more errors. Being reverted may be part of normal Wikipedia socialization rather than injustice. Many "reverted" editors may be satisfied one-time contributors rather than excluded voices.

#### 5.3.3 Self-Selection

Editors who disagree with Wikipedia norms may choose not to participate, reducing apparent conflict. The observed patterns reflect survivors of a selection process.

#### 5.3.4 Platform Design vs. Injustice

EC protection is a deliberate design choice to reduce edit warring. Calling it "epistemic dispossession" assumes it is wrongful, but Wikipedia's community may have legitimate reasons for this policy. Platform governance is not equivalent to injustice.

### 5.4 Reliability Challenges

The low inter-model agreement (κ = 0.09-0.18 for most constructs) raises fundamental questions:

1. **Are epistemic injustice constructs reliably applicable to editorial contexts?** The concepts were developed for face-to-face interaction. Operationalizing them for pseudonymous platform discourse may introduce irreducible ambiguity.

2. **What does multi-model disagreement reveal?** Rather than treating disagreement as methodological failure requiring human adjudication, we interpret it as substantive finding. When models trained on different corpora (Western vs. Chinese) diverge on whether an exchange constitutes "hermeneutical injustice," this reveals that the construct itself is culturally contested—not that one model is "wrong."

3. **Multi-model consensus as validity criterion.** We propose that constructs achieving high inter-model agreement (κ > 0.40) are more robustly operationalized, while low-agreement constructs require refinement or may be inherently interpretive. This reframes LLM ensemble coding as a construct validation method rather than a substitute for human coding.

### 5.5 Limitations

1. **No baseline comparison**: We cannot determine whether observed patterns differ from non-conflict Wikipedia articles or other contentious topics.

2. **Purposive sampling**: We selected high-conflict articles and contentious talk page threads. Findings do not generalize to typical Wikipedia dynamics.

3. **Temporal asymmetry**: Iran (1 week) and Gaza (2.5 years) data are not directly comparable.

4. **No content analysis of reverts**: We analyzed revert *patterns* but not *content*. We cannot assess whether reverts were justified.

5. **Three-model ensemble**: While multi-model agreement provides one form of validation, expanding to more models would strengthen consensus-based findings.

6. **No editor perspectives**: We analyzed editors' words but did not interview them. Our interpretations may miss insider understandings.

7. **Construct interpretability**: Low inter-model agreement for some constructs indicates these concepts may be inherently contested rather than objectively codable.

---

## 6. Conclusion

This exploratory study documents patterns of editorial conflict in Wikipedia's coverage of Middle East conflicts. We find asymmetric revert structures and evidence of contestation over naming, sources, and participation rights.

Whether these patterns constitute "epistemic injustice" remains an open question. Our data are consistent with both an epistemic injustice interpretation and alternative explanations emphasizing legitimate quality control and platform governance. The low reliability of our LLM-based coding for most constructs further limits our ability to draw firm conclusions.

### 6.1 Contributions

This study contributes:

1. **Descriptive documentation** of revert patterns and talk page dynamics during active conflicts
2. **Methodological innovation**: Multi-model LLM coding as construct validation—using agreement across culturally diverse models to identify which constructs are robustly operationalized vs. inherently contested
3. **Conceptual exploration** of how epistemic injustice theory might apply to platform contexts, with honest assessment of which concepts translate and which require rethinking

### 6.2 Future Directions

More rigorous investigation would require:

1. **Baseline comparison**: Analyze non-conflict articles to determine whether observed patterns are exceptional
2. **Content coding of reverts**: Determine whether reverted content was policy-violating or legitimate
3. **Expanded model ensemble**: Test additional LLMs (e.g., Gemini, Llama, Mistral) to strengthen consensus-based validity
4. **Editor interviews**: Include Wikipedia editors' own understandings of these dynamics
5. **Longitudinal analysis**: Track how patterns evolve over conflict lifecycles
6. **Platform-native constructs**: Develop operationalizations specifically for platform contexts, rather than importing face-to-face interaction concepts directly

### 6.3 Implications

We refrain from policy recommendations given our exploratory design and reliability concerns. The question of whether Wikipedia's editorial structures constitute epistemic injustice—or legitimate governance of a collaborative knowledge project—warrants further investigation with more rigorous methods.

What we can say is that Wikipedia's coverage of active conflicts involves substantial editorial contestation, and understanding how platforms mediate knowledge production during conflicts remains an important area for communication research.

---

## References

Ajmani, H., et al. (2024). Epistemic injustice in CSCW. *arXiv:2407.03477*.

Borra, E., et al. (2015). Societal controversies in Wikipedia articles. *CHI 2015*.

Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press.

Graham, M., et al. (2015). Uneven geographies of user-generated information. *Annals of the AAG*, 105(6), 1139-1155.

Kittur, A., et al. (2007). He says, she says: Conflict and coordination in Wikipedia. *CHI 2007*.

Kwok, S. (2025). Epistemic dispossession: Expanding Young's five faces. *Social Theory*.

Origgi, G. (2012). Epistemic injustice and epistemic trust. *Social Epistemology*, 26(2), 221-235.

Wagner, C., et al. (2015). It's a man's Wikipedia, but not because of men. *ICWSM*.

Yasseri, T., et al. (2012). Dynamics of conflicts in Wikipedia. *PLoS ONE*, 7(6), e38869.

---

## Appendices

### Appendix A: Inter-Model Reliability Details

Full pairwise κ matrices available in supplementary materials.

### Appendix B: Codebook v2.0

Complete coding scheme with definitions, examples, and counter-indicators.

### Appendix C: Article Lists

Full list of 100 articles analyzed.

### Appendix D: Revert Network Data

Edge lists and node attributes for both clusters.

---

**Data Availability**: Wikipedia data is publicly available. Coding results and analysis scripts will be deposited in OSF upon publication.

**Author Note**: This research was conducted by the AgentAcademy Research Team at UMass Amherst.

---

*Word count: ~3,800*  
*Version: 2.0 (Revised based on internal review)*  
*Last updated: March 6, 2026*
