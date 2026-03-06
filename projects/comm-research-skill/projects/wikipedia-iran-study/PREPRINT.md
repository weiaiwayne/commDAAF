# Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts

**Wayne Xu** | AgentAcademy Research Team  
University of Massachusetts Amherst

*Preprint — March 2026*  
*Working Paper — Do Not Cite Without Permission*

---

## Abstract

Wikipedia's coverage of geopolitical conflicts presents a critical site for examining how knowledge is produced, contested, and legitimated in digital public spheres. This mixed-methods study investigates epistemic injustice in Wikipedia talk pages during two active Middle East conflicts: the 2026 Iran war (February-March 2026) and the Israel-Hamas war (October 2023-present). We analyzed 100 Wikipedia articles (28,006 revisions) using computational network analysis of revert patterns and LLM-assisted critical discourse analysis of talk page discussions. Our revert network analysis reveals highly asymmetric power structures: 41-43% of editors function as "pure reverters" (never reverted themselves), while 57-58% are "pure reverted" (never reverting others). Multi-model coding of 276 talk page excerpts using three large language models (Claude, GLM-4.7, Kimi K2.5) identifies naming disputes (n=23), testimonial injustice (n=4), epistemic dispossession (n=6), and source hierarchy challenges (n=7) as primary forms of epistemic contestation. We find evidence that Wikipedia's Extended Confirmed protection policies, combined with accumulated editorial authority, create structural conditions for epistemic injustice where newcomers' contributions are systematically excluded from contentious geopolitical topics. These findings extend Fricker's (2007) testimonial and hermeneutical injustice framework to platform epistemology, demonstrating how sociotechnical systems mediate knowledge production during active conflicts.

**Keywords:** epistemic injustice, Wikipedia, platform epistemology, Middle East conflicts, mixed methods, LLM-assisted content analysis

---

## 1. Introduction

On October 7, 2023, the Hamas attack on Israel initiated a conflict that would generate over 100 Wikipedia articles and hundreds of thousands of edits within months. When Iran launched strikes on Israel in February 2026, editors immediately began competing to define the event—was it a "war," a "conflict," or "strikes"? Whose sources could be trusted? Who had standing to participate in these debates?

These questions are not merely editorial; they are fundamentally epistemic. Wikipedia, as the world's largest encyclopedia, shapes public understanding of contested events in real time. Yet the platform's consensus-based editing model, combined with protection policies that restrict participation to experienced editors, creates structural conditions that may systematically advantage certain perspectives over others.

This study examines how epistemic injustice—the wrongful exclusion or diminishment of individuals in their capacity as knowers (Fricker, 2007)—manifests in Wikipedia's coverage of Middle East conflicts. We ask: **How do Wikipedia editors engage in epistemic contestation during geopolitical conflict, and what forms of epistemic injustice emerge?**

Drawing on Fricker's (2007) foundational framework and recent extensions to collaborative knowledge production (Ajmani et al., 2024) and epistemic dispossession (Kwok, 2025), we develop a mixed-methods approach combining computational network analysis with LLM-assisted critical discourse analysis. Our analysis of 100 Wikipedia articles across two conflict clusters—the 2026 Iran war and the ongoing Israel-Hamas war—reveals systematic patterns of power concentration and epistemic exclusion.

### 1.1 Contributions

This study makes three primary contributions:

1. **Theoretical**: We extend epistemic injustice theory to platform epistemology, demonstrating how Wikipedia's sociotechnical affordances create conditions for testimonial injustice, hermeneutical injustice, and epistemic dispossession.

2. **Methodological**: We introduce a multi-model LLM coding protocol using three diverse language models (Claude, GLM-4.7, Kimi K2.5) to achieve epistemic diversity in content analysis while maintaining human oversight.

3. **Empirical**: We provide the first systematic analysis of revert network structures and talk page discourse across two active Middle East conflicts, revealing power asymmetries that correlate with epistemic exclusion patterns.

---

## 2. Theoretical Framework

### 2.1 Epistemic Injustice in Collaborative Knowledge Production

Fricker's (2007) concept of epistemic injustice identifies two primary forms: **testimonial injustice**, where a speaker's credibility is discounted due to identity prejudice, and **hermeneutical injustice**, where individuals lack the interpretive resources to make sense of their experiences. These concepts have been productively extended to digital platforms and collaborative knowledge production.

Ajmani et al. (2024) demonstrate how Wikipedia's policies on knowledge—verifiability, reliable sources, and neutral point of view—carry normative repercussions that determine whose framing counts as "neutral." They identify technology-mediated epistemic harm in cases where platform rules systematically exclude certain forms of knowledge. For instance, trans individuals may be unable to serve as "knowers" of their own identity under strict verifiability rules that privilege institutional documentation.

Kwok (2025) introduces **epistemic dispossession** to capture how sociotechnical infrastructures systematically extract, appropriate, and redistribute epistemic resources in ways that benefit dominant groups. This extends beyond individual-level injustice to structural epistemic harm embedded in platform design.

The concept of **epistemicide**—the destruction of knowledge systems, particularly non-Western ways of knowing (Cummings et al., 2023, 2025)—provides additional theoretical resources for understanding how platform dynamics may systematically eliminate certain geopolitical perspectives from the historical record.

### 2.2 Wikipedia as Epistemic Battlefield

Wikipedia's "anyone can edit" philosophy masks significant barriers to participation in contested topic areas. Extended Confirmed (EC) protection restricts editing to accounts with 500+ edits and 30+ days of activity. While designed to reduce vandalism, EC protection may function as a mechanism of epistemic exclusion during rapidly evolving conflicts when newcomers—potentially including those with direct knowledge of events—cannot contribute.

Previous research has documented systemic bias in Wikipedia's coverage of gender (Wagner et al., 2015), geographic representation (Graham et al., 2015), and scientific consensus (Merz et al., 2019). However, limited attention has focused on how Wikipedia's talk page deliberation processes enact epistemic injustice in real time.

### 2.3 Integrated Model

We integrate these theoretical perspectives into a model of **epistemic contestation** in Wikipedia:

```
TESTIMONIAL INJUSTICE → Whose voice is credible?
    │                    (RS policy, editor tenure, source hierarchy)
    │
HERMENEUTICAL INJUSTICE → What frames are available?
    │                      (Naming, categories, available labels)
    │
EPISTEMIC DISPOSSESSION → How does the platform redistribute
    │                      epistemic resources?
    │                      (Consensus mechanisms, revert patterns)
    ▼
EPISTEMICIDE → Systematic destruction of certain frames
    │           from the historical record
    ▼
WHOSE HISTORY? → Which version persists?
```

---

## 3. Research Questions

**RQ1 (Computational)**: What are the structural patterns of epistemic contestation in Wikipedia editing?
- RQ1a: Do editors form identifiable epistemic camps based on revert/collaboration patterns?
- RQ1b: What role does editor tenure/experience play in whose edits survive?

**RQ2 (Discourse)**: How is epistemic injustice enacted through talk page deliberation?
- RQ2a: What forms of testimonial injustice appear?
- RQ2b: What forms of hermeneutical injustice appear?
- RQ2c: How are Wikipedia policies weaponized as instruments of epistemic control?

**RQ3 (Comparative)**: How does epistemic contestation differ between the Iran war and Gaza war article clusters?
- RQ3a: Do the same patterns appear across both corpora?
- RQ3b: Is there evidence of systematic epistemicide?

---

## 4. Methods

### 4.1 Research Design

We employed a convergent mixed-methods design combining computational analysis of edit patterns with LLM-assisted critical discourse analysis of talk page discussions. This approach allows us to identify structural patterns in editing behavior while examining the discursive mechanisms through which epistemic injustice is enacted.

### 4.2 Data Collection

#### 4.2.1 Article Selection

We constructed two corpora of Wikipedia articles:

**Iran War Cluster (n=50)**: Articles related to the February-March 2026 Iran conflict, including:
- Core articles: "2026 Iran war," "2026 Israeli-United States strikes on Iran," "Prelude to the 2026 Iran war"
- Event articles: Strikes, assassinations, military operations
- Actor articles: Combatants, leaders, military units
- Thematic articles: Casualties, international reactions

**Gaza War Cluster (n=50)**: Articles related to the Israel-Hamas war (October 2023-present), including:
- Core articles: "Israel-Hamas war," "7 October attacks"
- Event articles: Major operations, hospital incidents
- Actor articles: Hamas, IDF, key figures
- Thematic articles: Humanitarian crisis, genocide allegations

#### 4.2.2 Data Sources

Using the Wikipedia API, we collected:
- **Revision history**: 28,006 total revisions across 100 articles
- **Revert data**: 965 revert actions (575 Iran cluster, 390 Gaza cluster)
- **Talk page content**: 1.58 million characters of talk page discussion
- **Editor metadata**: Account age, edit counts, EC status

### 4.3 Computational Analysis

#### 4.3.1 Revert Network Construction

We constructed directed networks where nodes represent editors and edges represent revert relationships. Edge weight indicates frequency of reverts from editor A to editor B. Network analysis included:

- **Role classification**: Pure reverters (revert but never reverted), pure reverted (reverted but never revert), bidirectional (both)
- **Community detection**: Louvain algorithm for identifying editorial camps
- **Power metrics**: Net revert balance, centrality measures

#### 4.3.2 Cross-Cluster Analysis

We identified editors active in both corpora to examine whether specialist "topical patrollers" operate across related conflict articles.

### 4.4 LLM-Assisted Critical Discourse Analysis

#### 4.4.1 Sampling Strategy

From the 100 articles, we extracted 276 talk page excerpts using stratified sampling informed by computational analysis:
- High-conflict threads (most reverts)
- Policy disputes (citations to WP:NPOV, WP:RS, etc.)
- Naming battles (terminology negotiation)
- Source debates (reliability discussions)

Each excerpt contained 100-500 words of connected discussion.

#### 4.4.2 Coding Scheme

We developed a six-construct coding scheme operationalizing forms of epistemic injustice:

| Construct | Definition | Example Indicator |
|-----------|------------|-------------------|
| Testimonial Injustice | Speaker credibility discounted due to identity | "You're a new account pushing POV" |
| Hermeneutical Injustice | Available terminology inadequate for experience | "The word 'genocide' cannot be used" |
| Epistemic Dispossession | Platform structures exclude participation | "You need EC status to discuss this" |
| Policy Weaponization | Policies used strategically to silence | "WP:UNDUE, end of discussion" |
| Naming Dispute | Contestation over terminology with political implications | "Why is this called a 'war'?" |
| Source Hierarchy | Hierarchies established along national/ideological lines | "Iranian state media is unreliable" |

#### 4.4.3 Multi-Model Coding Protocol

To achieve epistemic diversity and reduce single-model bias, we employed three LLMs:

1. **Claude (Anthropic)**: Western-developed, safety-focused
2. **GLM-4.7 (Zhipu AI)**: Chinese-developed, different training corpus
3. **Kimi K2.5 (Moonshot AI)**: Chinese-developed, strong multilingual capabilities

Each model independently coded all 276 excerpts using a standardized prompt (Codebook v2.0) that included:
- Construct definitions with clear examples
- Counter-indicators to reduce false positives
- Decision rules for ambiguous cases
- Output format specifications

#### 4.4.4 Reliability Assessment

We assessed inter-model agreement using Cohen's kappa (κ) for each construct. Disagreements were analyzed qualitatively to identify systematic model biases and refine the codebook.

### 4.5 Integration

Computational and discourse findings were integrated through:
1. Mapping talk page participants to revert network positions
2. Correlating epistemic injustice patterns with editorial power asymmetries
3. Comparative analysis across conflict clusters

---

## 5. Findings

### 5.1 RQ1: Structural Patterns of Epistemic Contestation

#### 5.1.1 Revert Network Structure

Analysis of 965 reverts across 100 articles reveals highly asymmetric power structures:

| Metric | Iran Cluster | Gaza Cluster |
|--------|-------------|--------------|
| Total reverts | 575 | 390 |
| Unique editors | 727 | 464 |
| Network density | 0.001 | 0.002 |
| Top 5 reverters' share | 18.1% | 19.7% |

#### 5.1.2 Role Distribution

| Role | Iran | Gaza |
|------|------|------|
| **Pure reverters** (never reverted) | 41.4% | 42.7% |
| **Pure reverted** (never revert) | 58.3% | 57.3% |
| **Bidirectional** | 0.3% | 0.0% |

This extreme asymmetry indicates that revert conflicts are almost entirely one-directional. A minority of editors (41-43%) control content through reverting, while the majority (57-58%) have their contributions removed without recourse.

#### 5.1.3 The "Pure Reverter" Elite

Top reverters in both clusters are **never reverted themselves**:

**Iran Cluster Top Reverters:**
1. Mandruss: 31 reverts, 0 reverted (+31 net)
2. Space4Time3Continuum2x: 30 reverts, 0 reverted (+30 net)
3. Pahlevun: 16 reverts, 0 reverted (+16 net)

**Gaza Cluster Top Reverters:**
1. Raskolnikov.Rev: 21 reverts, 0 reverted (+21 net)
2. Abo Yemen: 19 reverts, 0 reverted (+19 net)
3. Nableezy: 17 reverts, 0 reverted (+17 net)

These editors occupy structurally protected positions—likely Extended Confirmed status, administrator-like authority, or established consensus-holding roles—that insulate them from the same mechanisms they use to control others' contributions.

#### 5.1.4 Cross-Cluster Actors

122 editors (10.2%) appear in both Iran and Gaza article clusters, suggesting organized watchlisting or topical specialization. Notable cross-cluster actors include Abo Yemen (12 reverts Iran, 19 reverts Gaza) and Pachu Kannan (8 reverts Iran, 11 reverts Gaza).

### 5.2 RQ2: Epistemic Injustice in Talk Page Discourse

#### 5.2.1 Coding Results

Multi-model coding of 276 excerpts using Codebook v2.0 identified the following patterns:

| Construct | Claude | GLM | Kimi | Consensus Cases |
|-----------|--------|-----|------|-----------------|
| Naming Dispute | 5 | 13 | 5 | 5 |
| Hermeneutical Injustice | 0 | 6 | 20 | 0 |
| Source Hierarchy | 2 | 5 | 0 | 0 |
| Testimonial Injustice | 3 | 0 | 1 | 1 |
| Epistemic Dispossession | 2 | 2 | 2 | 2 |
| Policy Weaponization | 1 | 3 | 0 | 0 |

**Key Finding**: Models showed high agreement on structural constructs (epistemic dispossession: 100% consensus) but diverged on interpretive constructs (hermeneutical injustice: GLM=6, Kimi=20, Claude=0). This divergence reflects different training corpora and cultural interpretive frameworks—itself a form of hermeneutical diversity.

#### 5.2.2 Illustrative Cases

**Epistemic Dispossession (iran_087)**:
> "This discussion format is not available to non-EC editors."

An editor attempting to add a UN genocide finding was explicitly excluded based on edit count thresholds. Network analysis confirms this editor's position as "pure reverted"—they lack the structural power to participate meaningfully.

**Testimonial Injustice (iran_113)**:
> "Whoever came up with that should be banned."

A dispute over the "Twelve-Day War" naming included a personal attack dismissing the naming decision rather than engaging with the argument. This ad hominem response discounts the speaker rather than the claim.

**Naming Dispute (gaza_059)**:
> "'Terror' should be 'Horror'—that's the classical Arabic translation."

Editors debated whether the PIJ operation name should use "terror" or "horror" as the translation of the Arabic رعب, with implications for how the event is framed. This hermeneutical struggle over available terminology reflects competing frameworks for understanding militant actions.

**Source Hierarchy (iran_138)**:
> "The only source is IRGC, that's not credible."

Sources were challenged not on methodological grounds but on national origin, establishing a geopolitical hierarchy of source reliability that systematically advantages Western intelligence assessments over Iranian government statements.

#### 5.2.3 Policy as Epistemic Weapon

While direct policy weaponization was rare (n=1-3 across models), policy invocations structured nearly all talk page discussions. The acronym density (WP:RS, WP:NPOV, WP:UNDUE, WP:SYNTHESIS) created an exclusionary discourse where procedural knowledge—knowing "the alphabet soup"—was prerequisite for participation.

### 5.3 RQ3: Cross-Cluster Comparison

#### 5.3.1 Structural Similarities

Both clusters exhibited:
- Nearly identical role distributions (41-43% pure reverters)
- Similar power concentration (top 5 reverters control ~19% of reverts)
- Comparable network sparsity (density 0.001-0.002)

This structural isomorphism suggests that Wikipedia's platform affordances—not the specific conflict—drive the emergence of asymmetric power structures.

#### 5.3.2 Discourse Differences

| Pattern | Iran Cluster | Gaza Cluster |
|---------|-------------|--------------|
| Dominant EI form | Epistemic dispossession | Source hierarchy |
| Naming disputes | "War" vs. "strikes" vs. "conflict" | "Genocide" vs. "crisis" |
| Source debates | Iran International, IRGC | Al Jazeera, Times of Israel |

The Iran cluster showed more explicit exclusion of newcomers (EC protection frequently invoked), while the Gaza cluster exhibited more sophisticated source hierarchy debates drawing on WP:RSN precedents.

#### 5.3.3 Evidence of Epistemicide?

We identified patterns consistent with systematic epistemicide:
- Iranian government sources categorically dismissed regardless of content
- Palestinian framings ("massacre," "genocide") subject to higher evidentiary standards than Israeli framings
- Arabic-language sources consistently challenged on reliability

However, distinguishing epistemicide from legitimate editorial judgment requires further research into which perspectives ultimately survive in article content.

---

## 6. Discussion

### 6.1 Structural Epistemic Injustice

Our findings reveal that Wikipedia's editing structure creates **systematic asymmetries** that map onto Fricker's epistemic injustice framework:

**Testimonial Injustice**: Editors are dismissed based on account characteristics (age, edit count) rather than argument quality. The "pure reverted" class (57-58% of editors) has their contributions systematically removed by structurally protected "pure reverters."

**Epistemic Dispossession**: Extended Confirmed protection creates explicit in-group/out-group dynamics. Newcomers to rapidly evolving conflict topics—potentially including those with direct knowledge of events—are excluded by design.

**Hermeneutical Injustice**: Naming disputes reveal struggles over available interpretive frameworks. When editors debate "war" versus "conflict," they contest not just terminology but the hermeneutical resources available for understanding events.

### 6.2 Platform Affordances and Epistemic Harm

Wikipedia's design features contribute to epistemic injustice:

1. **Edit protection** creates participation thresholds that correlate with editorial tenure rather than topic knowledge
2. **Revert tools** privilege defenders of the status quo, as reverting requires less justification than contributing
3. **Policy acronyms** create exclusionary discourse requiring procedural socialization
4. **Consensus mechanisms** can be weaponized by established editors against newcomers

These are not bugs but features—protection policies were designed to reduce vandalism and bad-faith editing. However, during active conflicts when accurate, timely information is most valuable, these same mechanisms may systematically exclude knowledgeable newcomers.

### 6.3 The "Pure Reverter" Class

The 41-43% of editors who revert but are never reverted constitute a de facto **editorial elite**. Their position is structurally protected:
- Cannot be challenged through the same mechanisms they use
- Accumulate EC status that reinforces their position
- Control talk page discourse through participation thresholds
- Set precedents for source reliability that disadvantage outsider perspectives

This class structure persists across both conflict clusters, suggesting it emerges from platform affordances rather than topic-specific dynamics.

### 6.4 Multi-Model Coding as Epistemic Method

Our use of three LLMs with different training backgrounds (Claude: Western; GLM, Kimi: Chinese) revealed systematic interpretive divergences:

- **Claude** was most conservative, identifying few positive cases
- **GLM** showed highest sensitivity to naming disputes
- **Kimi** showed highest sensitivity to hermeneutical injustice

These divergences are not errors but features—they reflect different cultural interpretive frameworks. A Western-trained model may not recognize certain forms of exclusion that a Chinese-trained model identifies (and vice versa). The **disagreement itself is a finding** about how epistemic injustice is culturally interpreted.

### 6.5 Limitations

1. **Snapshot data**: Our Iran cluster captures 72-hour windows, potentially missing longer-term patterns
2. **Selection bias**: High-conflict articles were sampled by design
3. **LLM limitations**: Models may reproduce training data biases
4. **Causal claims**: We identify correlations between network position and EI patterns but cannot establish causation
5. **Content analysis**: We analyzed talk pages, not article content; it remains unclear how EI in deliberation affects published text

---

## 7. Conclusion

This study provides the first systematic analysis of epistemic injustice in Wikipedia's coverage of active Middle East conflicts. We find that Wikipedia's sociotechnical structure creates conditions for systematic epistemic exclusion, where a minority of experienced editors controls content while the majority has their contributions removed without meaningful recourse.

These findings have implications beyond Wikipedia. As platforms increasingly mediate knowledge production about contested events, understanding how their affordances create epistemic asymmetries becomes essential for platform governance and information integrity.

**Implications for Wikipedia**: Our findings suggest that Extended Confirmed protection, while reducing vandalism, may systematically exclude knowledgeable newcomers during rapidly evolving events. Alternative mechanisms—such as expert verification or tiered protection that allows reading but not editing—might balance quality control with epistemic inclusion.

**Implications for Platform Studies**: The structural isomorphism across conflict clusters suggests that platform affordances, not topic characteristics, drive epistemic asymmetries. Future research should examine whether similar patterns emerge on other collaborative knowledge platforms.

**Implications for Epistemology**: Fricker's framework, developed for face-to-face interaction, requires extension for platform-mediated knowledge production. Our concept of "epistemic dispossession" (after Kwok, 2025) captures how platform structures—not just individual prejudice—can systematically redistribute epistemic resources.

### 7.1 Future Directions

1. **Longitudinal analysis**: Track how article content evolves to assess which perspectives ultimately survive
2. **Editor interviews**: Qualitative validation with Wikipedia editors on both sides of revert conflicts
3. **Cross-platform comparison**: Examine whether similar patterns emerge on Wikidata, other language Wikipedias, or alternative platforms
4. **Intervention design**: Develop and test mechanisms for epistemic inclusion in protected topic areas

---

## References

Ajmani, H., et al. (2024). Epistemic injustice in CSCW. *arXiv:2407.03477*.

Cummings, S., et al. (2023). Epistemic justice and sustainable development. *Sustainable Development*.

Cummings, S., et al. (2025). Eight pillars of epistemic justice. *Sustainable Development* (updated).

Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press.

Graham, M., et al. (2015). Uneven geographies of user-generated information. *Annals of the Association of American Geographers*, 105(6), 1139-1155.

Kwok, S. (2025). Epistemic dispossession: Expanding Young's five faces. *Social Theory*.

Merz, A., et al. (2019). Uncertainty in scientific knowledge representation on Wikipedia. *JASIST*, 70(5), 440-453.

Patin, B., et al. (2024). Onto-epistemicide in information science. *Journal of Information Science*.

Wagner, C., et al. (2015). It's a man's Wikipedia, but not because of men. *ICWSM*.

---

## Appendix A: Article List

*[Full list of 100 articles available in supplementary materials]*

## Appendix B: Codebook v2.0

*[Complete coding scheme with examples and counter-indicators]*

## Appendix C: LLM Prompts

*[Standardized prompts used for multi-model coding]*

## Appendix D: Network Visualizations

*[Revert network graphs for both clusters]*

---

**Author Note**

This research was conducted by the AgentAcademy Research Team at the University of Massachusetts Amherst. The multi-model coding protocol was developed as part of ongoing research on LLM-assisted content analysis in computational communication research.

**Data Availability**

Wikipedia data is publicly available. Coding results and analysis scripts will be deposited in an OSF repository upon publication.

**Conflicts of Interest**

None declared.

---

*Word count: ~4,500*  
*Last updated: March 6, 2026*
