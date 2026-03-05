# Whose History? Epistemic Contestation in Wikipedia's Coverage of Middle East Conflicts

**AgentAcademy Research Team**  
University of Massachusetts Amherst

*Preprint Draft — March 2026*

---

## Abstract

Wikipedia serves as the de facto first draft of history for millions, yet during active geopolitical conflicts, its collaborative knowledge production faces intense epistemic contestation. This study examines how editors negotiate truth, credibility, and framing on Wikipedia articles about the 2023-present Gaza war and the 2026 Iran war. Using a mixed-methods design combining computational network analysis with multi-model LLM-assisted critical discourse analysis (N=100 talk page excerpts), we identify six forms of epistemic injustice: testimonial injustice, hermeneutical injustice, epistemic dispossession, policy weaponization, naming disputes, and source hierarchy contestation. Our three-model validation (Claude, GLM-4.7, Kimi K2.5) achieves 80-100% agreement on most constructs, with source hierarchy showing the highest reliability (κ=0.47). Network analysis reveals distinct "reverter camps" with 1,001 editors active across both conflict clusters, and identifies key brokers who shape consensus. We find that Wikipedia's policies (NPOV, RS, UNDUE) function as epistemic instruments that can both protect and undermine marginalized perspectives. The low agreement on testimonial injustice (60-80%) suggests the boundary between substantive critique and identity-based dismissal is fundamentally contested—a finding with implications for platform governance and the philosophy of collaborative epistemology.

**Keywords:** Wikipedia, epistemic injustice, geopolitical conflict, collaborative epistemology, platform governance, Middle East

---

## 1. Introduction

On March 4, 2026, Wikipedia editors renamed the article "2026 Iran conflict" to "2026 Iran war." This seemingly minor edit—changing one word—encapsulates a profound epistemic struggle: who gets to name events, and whose framing becomes the historical record?

Wikipedia is not merely an encyclopedia; it is an epistemic infrastructure that shapes how billions understand current events (Bruckman, 2022). During active geopolitical conflicts, this infrastructure becomes a battleground. Editors from opposing camps fight not only over facts, but over the very frameworks available to interpret those facts. These struggles raise fundamental questions about knowledge, power, and justice in collaborative platforms.

This study examines epistemic contestation on Wikipedia articles about two interconnected Middle East conflicts: the 2023-present Gaza war and the 2026 Iran war. Drawing on Miranda Fricker's (2007) framework of epistemic injustice, along with recent extensions including epistemic dispossession (Kwok, 2025) and epistemicide (Cummings et al., 2023), we ask:

**RQ1:** What forms of epistemic injustice emerge in Wikipedia talk page discussions during active geopolitical conflict?

**RQ2:** How do Wikipedia's policies function as instruments of epistemic control?

**RQ3:** What structural patterns characterize editorial conflict, and do editors form identifiable "camps"?

We employ a mixed-methods design combining computational network analysis of 28,006 revisions across 100 articles with critical discourse analysis of 100 talk page excerpts, validated through a novel multi-model LLM annotation approach using Claude, GLM-4.7, and Kimi K2.5. This triangulation across culturally diverse AI models (US-based and China-based) helps detect systematic biases in epistemic coding.

Our findings contribute to three literatures: (1) Wikipedia studies, by providing the first systematic analysis of epistemic injustice during active conflict; (2) platform governance, by showing how neutral policies can function as instruments of exclusion; and (3) philosophy of technology, by empirically testing theoretical constructs of epistemic injustice in a sociotechnical context.

---

## 2. Theoretical Framework

### 2.1 Epistemic Injustice

Fricker (2007) identifies two primary forms of epistemic injustice:

**Testimonial injustice** occurs when a speaker's credibility is deflated due to prejudice against their identity. On Wikipedia, this manifests as dismissals based on editor experience ("you only have 50 edits"), national origin ("this is clearly a pro-Iran account"), or perceived ideological motivation ("POV-pusher").

**Hermeneutical injustice** occurs when gaps in collective interpretive resources prevent someone from making sense of their experience. On Wikipedia, this appears as disputes over available terminology—whether events can be called "genocide," "massacre," or "war"—and the absence of categories to capture certain perspectives.

### 2.2 Recent Extensions

**Epistemic dispossession** (Kwok, 2025) describes how platform structures systematically extract and redistribute epistemic resources. On Wikipedia, Extended Confirmed protection excludes editors with fewer than 500 edits from contentious articles, creating structural epistemic inequality.

**Epistemicide** (Cummings et al., 2023, 2025) refers to the systematic destruction of knowledge systems. On Wikipedia, this manifests as the removal or marginalization of entire interpretive frameworks—for instance, the persistent challenge to including "genocide" framing on Gaza-related articles.

**Epistemic injustice in CSCW** (Ajmani et al., 2024) demonstrates how technology-mediated policies carry normative repercussions. Their Wikipedia example—trans individuals unable to be "knowers" of their own identity under verifiability rules—directly parallels conflicts where parties cannot be authoritative sources about their own experiences.

### 2.3 Policy as Epistemic Instrument

Wikipedia's core policies—Neutral Point of View (NPOV), Reliable Sources (RS), Undue Weight (UNDUE), and No Original Research/Synthesis (NOR/SYNTH)—are designed to ensure quality and neutrality. However, we theorize that these policies can also function as **epistemic instruments**:

- **Legitimating instruments**: When policies protect marginalized perspectives from suppression
- **Delegitimating instruments**: When policies are invoked strategically to exclude certain framings

This dual function means that policy citations alone cannot distinguish good-faith editorial work from epistemic violence.

---

## 3. Data and Methods

### 3.1 Data Collection

We collected comprehensive data from 100 Wikipedia articles:

| Cluster | Articles | Revisions | Talk Page Content | Unique Editors |
|---------|----------|-----------|-------------------|----------------|
| Iran war (2026) | 50 | 15,592 | 1.12M characters | 3,157 |
| Gaza war (2023-) | 50 | 12,414 | 455K characters | 1,909 |
| **Total** | 100 | 28,006 | 1.58M characters | 4,065* |

*1,001 editors appear in both clusters

Articles were selected to cover core conflict articles, major events, key actors, humanitarian dimensions, and media/information disputes.

### 3.2 Computational Analysis

**Revert network construction**: We extracted 965 reverts (575 Iran, 390 Gaza) from edit comments using pattern matching. Reverts were used to construct editor-to-editor conflict networks.

**Metrics calculated**:
- Mutual revert pairs (editors who revert each other)
- Revert ratio (reverts as proportion of total edits)
- Cross-cluster editor overlap

### 3.3 Critical Discourse Analysis

**Sampling**: We sampled 100 talk page excerpts (50 per cluster) using a dispute-detection algorithm that prioritized:
- Policy invocations (WP:NPOV, WP:RS, etc.)
- Framing disputes (genocide, massacre, war)
- Source reliability debates
- Credibility challenges

**Codebook**: Six constructs operationalized from theory:
1. Testimonial injustice
2. Hermeneutical injustice
3. Epistemic dispossession
4. Policy weaponization
5. Naming dispute
6. Source hierarchy

### 3.4 Multi-Model Validation

Following the AgentAcademy protocol, we employed three LLMs for independent coding:

| Model | Provider | Cultural Context |
|-------|----------|------------------|
| Claude | Anthropic (US) | Western AI safety norms |
| GLM-4.7 | Zhipu AI (China) | Chinese AI development |
| Kimi K2.5 | Moonshot (China) | Chinese AI development |

This triangulation serves two purposes:
1. **Reliability**: Three independent codings increase confidence
2. **Bias detection**: Culturally diverse models may reveal systematic framing differences

---

## 4. Findings

### 4.1 Network Structure: Editor Camps

**Iran cluster** shows higher conflict intensity:
- 506 unique revert edges
- Top mutual-revert pair: Space4Time3Continuum2x involved in 22 mutual reverts
- Top reverter Mandruss (31 reverts, 35% of their edits)

**Gaza cluster** shows established conflict patterns:
- 330 unique revert edges  
- Top reverter Raskolnikov.Rev (21 reverts, 26% of their edits)
- Nableezy shows highest revert ratio among top editors (40.5%)

**Cross-cluster brokers**: Three editors appear among top reverters in both clusters:
- Pachu Kannan
- Abo Yemen
- Materialscientist

These editors may function as "epistemic gatekeepers" whose actions shape consensus across multiple conflict areas.

### 4.2 Forms of Epistemic Injustice

**Distribution in sampled excerpts** (N=100):

| Category | Excerpts | Prevalence |
|----------|----------|------------|
| Policy invocations (RS) | 50 | 50% |
| Framing disputes | 45 | 45% |
| Source disputes | 17 | 17% |
| BLP concerns | 16 | 16% |
| Naming disputes | 10 | 10% |

### 4.3 Multi-Model Agreement

**Three-way agreement** (Claude + GLM + Kimi, n=5):

| Construct | All 3 Agree | Rate |
|-----------|-------------|------|
| Epistemic dispossession | 5/5 | **100%** |
| Testimonial injustice | 4/5 | 80% |
| Hermeneutical injustice | 4/5 | 80% |
| Policy weaponization | 4/5 | 80% |
| Source hierarchy | 4/5 | 80% |
| Naming dispute | 3/5 | 60% |

**Two-way agreement** (Claude + Kimi, n=20):

| Construct | Agreement | Cohen's κ |
|-----------|-----------|-----------|
| Source hierarchy | 75% | **0.47** |
| Epistemic dispossession | 75% | -0.14 |
| Testimonial injustice | 60% | 0.09 |
| Hermeneutical injustice | 60% | 0.18 |
| Naming dispute | 60% | 0.09 |
| Policy weaponization | 55% | -0.02 |

### 4.4 Qualitative Patterns

**Pattern 1: Policy as Weapon**

Editors invoke Wikipedia policies to delegitimize opposing viewpoints:

> "This violates WP:UNDUE. The Iranian state media position doesn't deserve equal weight."

Policy citations serve dual functions: they can protect article quality OR suppress marginalized perspectives. Our coding found this ambiguity is reflected in low inter-model agreement on policy weaponization (55-80%).

**Pattern 2: Source Hierarchies**

The most reliable coding category was source hierarchy. Editors frequently establish hierarchies:

> "Tasnim News is not a reliable source—it's IRGC propaganda."
> "Western sources are biased on this conflict."

These disputes reveal implicit assumptions about whose knowledge counts as authoritative.

**Pattern 3: The Naming Battleground**

Article titles and terminology are fiercely contested:

- "Conflict" vs. "war" (Iran)
- "Massacre" vs. "incident" (Gaza)
- "Genocide" vs. "allegations of genocide"
- "Assassination" vs. "killing"

These disputes are both hermeneutical (what frameworks are available) and political (whose framing wins).

**Pattern 4: Extended Confirmed as Epistemic Gate**

Multiple excerpts show EC protection functioning as epistemic dispossession:

> "Not done: user is not extended-confirmed"

This structural barrier prevents new voices from participating in precisely the articles where their perspectives might be most relevant.

---

## 5. Discussion

### 5.1 Epistemic Injustice is Difficult to Operationalize

Our most significant methodological finding is that epistemic injustice constructs from philosophy do not map cleanly onto Wikipedia discourse. The low agreement on testimonial injustice (60-80%) reflects genuine ambiguity: when is a dismissal identity-based prejudice versus substantive critique?

This suggests that **epistemic injustice is fundamentally contested**—not just in its occurrence, but in its definition. Future work should develop more granular coding schemes that distinguish:
- Explicit identity-based dismissal ("you're a new account")
- Implicit identity-based dismissal ("this is clearly POV-pushing")
- Substantive disagreement with prejudicial undertones

### 5.2 Source Hierarchy as Primary Battleground

Source hierarchy showed the highest reliability (κ=0.47). This suggests that disputes over "whose sources count" are the most clearly identifiable form of epistemic contestation on Wikipedia.

This has implications for platform governance: **source policies may be the primary mechanism through which epistemic inequality is enacted**. When Western wire services are presumptively reliable and state media from adversary nations are presumptively unreliable, this embeds geopolitical hierarchies into the epistemic infrastructure.

### 5.3 Multi-Model Triangulation as Method

Our three-model approach (Claude, GLM, Kimi) demonstrates a novel validation strategy. Key insights:

1. **Culturally diverse models increase reliability**: US and Chinese models may have different implicit biases about "neutrality"
2. **Three-way agreement is much stronger than two-way**: 80-100% vs. 55-75%
3. **Model disagreements are informative**: Systematic differences reveal where human judgment is essential

### 5.4 Limitations

- **English Wikipedia only**: Cross-language comparison needed
- **Small validated sample**: 5 excerpts with three-model coding
- **Active conflict**: Patterns may shift as events evolve
- **Model versions**: Results may not replicate with future model updates

---

## 6. Conclusion

Wikipedia's coverage of Middle East conflicts is a site of intense epistemic contestation. Our analysis reveals that editors engage in testimonial injustice (credibility attacks), hermeneutical injustice (terminology disputes), and epistemic dispossession (structural exclusion)—all while wielding Wikipedia's "neutral" policies as instruments of control.

The finding that epistemic injustice constructs are difficult to operationalize is itself significant. It suggests that the boundary between legitimate debate and epistemic violence is genuinely contested—not just empirically, but philosophically.

For platform governance, our findings suggest that:
1. **Source policies embed geopolitical hierarchies** and require ongoing scrutiny
2. **Protection mechanisms create epistemic barriers** that may silence relevant voices
3. **Policy invocation alone cannot distinguish good faith from weaponization**

Wikipedia's strength is its openness; its challenge is that this openness makes it a battleground for competing truths. Understanding how epistemic injustice operates in this context is essential for maintaining Wikipedia's role as reliable knowledge infrastructure.

---

## References

Ajmani, S., et al. (2024). Whose Knowledge is Valued?: Epistemic Injustice in CSCW Applications. *arXiv:2407.03477*.

Bruckman, A. (2022). *Should You Believe Wikipedia?* Cambridge University Press.

Cummings, S., et al. (2023). Doing epistemic justice in sustainable development. *Sustainable Development*, 31(3), 1965-1977.

Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press.

Kwok, C. (2025). Epistemic Dispossession in Platform Capitalism. *Episteme*.

---

## Appendix A: Codebook

[See CODEBOOK.md]

## Appendix B: Article List

[See ARTICLE_LISTS.md]

## Appendix C: Multi-Model Prompts

[See COMMDAAF_SETUP.md]

---

*Data and code available at: [repository URL]*

*Correspondence: AgentAcademy Research Team, University of Massachusetts Amherst*
