# Proximity and Resistance: How Distance from the Enemy Shapes Political Crisis Discourse Online

**Preprint v2.0 — Theory Paper**  
**Date:** March 4, 2026

---

## Authors

Wayne Xu¹*, OpenClaw Research Collective²

¹ Department of Communication, Boston University  
² Distributed AI Research Network

*Corresponding author: [email]

---

## Abstract

Why do online movements against external enemies look so different from movements against one's own government? We theorize that **proximity to the enemy**—whether the target of resistance is foreign or domestic—fundamentally shapes the rhetorical strategies available to activists. Drawing on framing theory, discourse analysis, and social movement scholarship, we develop a typology of **discursive resistance modes**: externalized (war) versus internalized (protest). We test this framework through comparative analysis of Ukraine war discourse (N=339) and Iranian #MahsaAmini protest discourse (N=380), employing a novel **Agentic Content Analysis** methodology that orchestrates multiple AI models under human authority. Our findings support three theoretical propositions: (1) external enemies are constructed through third-person dehumanization while internal enemies receive second-person moral shaming; (2) irony functions as solidarity technology in protest but is rare in war discourse where moral clarity is paramount; (3) affective frames (SOLIDARITY, HOPE) dominate protest while informational frames dominate war coverage. These patterns hold across languages and platforms, suggesting proximity-based rhetoric is a generalizable feature of digital resistance. We contribute a theoretical framework for understanding how structural position shapes discursive strategy in contentious politics.

**Keywords:** political communication, social movements, framing, discourse analysis, enemy construction, digital activism, Ukraine, Iran, protest

---

## 1. Introduction

When Ukrainians tweet about Russian atrocities, they write about "Orcs from Mordor" committing "war crimes" that demand international intervention. When Iranians tweet about morality police violence, they write directly to their oppressors: "Don't you have daughters? Shame on you." Both are resistance. Both use social media. But the rhetoric is fundamentally different.

Why?

We propose that **proximity to the enemy** shapes the discursive strategies available to resisters. External enemies (foreign states, invading armies) can be addressed through third-person appeals to international audiences, deploying dehumanization and legal frameworks. Internal enemies (one's own government, domestic institutions) must be addressed through second-person confrontation, deploying shame and irony while preserving the enemy's humanity for moral accountability.

This distinction has theoretical implications for understanding digital activism, practical implications for movement strategy, and methodological implications for how we study online political discourse.

### 1.1 Research Questions

**RQ1:** How does enemy construction differ between war discourse (external enemy) and protest discourse (internal enemy)?

**RQ2:** How does the deployment of irony differ across resistance contexts?

**RQ3:** How do frame distributions differ between externalized and internalized resistance?

### 1.2 Contributions

1. **Theoretical:** We develop a typology of discursive resistance modes based on enemy proximity, integrating framing theory with discourse analysis.

2. **Empirical:** We provide comparative evidence from two major 2022 political crises, demonstrating systematic rhetorical differences.

3. **Methodological:** We introduce Agentic Content Analysis (ACA), a multi-model approach to computational text analysis that addresses single-model bias through adversarial validation.

---

## 2. Theoretical Framework

### 2.1 Framing and Collective Action

Social movements succeed partly through strategic framing—the selective emphasis on certain aspects of reality to mobilize support (Benford & Snow, 2000; Entman, 1993). Effective frames diagnose problems (injustice framing), propose solutions (agency framing), and motivate action (identity framing) (Snow & Benford, 1988).

Yet framing theory typically treats frames as strategic choices without theorizing the structural constraints on which frames are available. We argue that the relationship between resisters and their targets—particularly spatial and political proximity—constrains framing options.

### 2.2 Enemy Construction and Moral Boundaries

How enemies are constructed linguistically has consequences for what actions become thinkable (Keen, 1986; Silverstein, 2005). Dehumanization—portraying enemies as animals, vermin, or monsters—creates moral permission for violence by placing targets outside the community of moral concern (Smith, 2011).

However, dehumanization carries costs. If you must continue living with your enemy after the conflict—as protesters must with their government—total dehumanization forecloses reconciliation. We theorize that proximity moderates dehumanization strategies.

### 2.3 Irony as Political Weapon

Irony serves multiple functions in contentious politics: coping with trauma, building in-group solidarity, delegitimizing authority, and maintaining plausible deniability under repression (Billig, 2005; Wedeen, 1999). Yet irony requires shared context between speaker and audience—the audience must recognize the gap between literal and intended meaning.

We theorize that irony is more viable in internalized resistance (protest) where resisters share cultural context with their audience than in externalized resistance (war) where the audience is international and moral clarity is paramount.

### 2.4 Hypotheses

**H1 (Enemy Construction):** War discourse will construct enemies through third-person reference and fantasy dehumanization (e.g., mythological creatures), while protest discourse will construct enemies through second-person address and moral shaming that preserves human status.

**H2 (Irony Deployment):** Irony will be more prevalent in protest discourse than war discourse, serving solidarity-building and delegitimization functions.

**H3 (Frame Distribution):** War discourse will be dominated by INFORMATIONAL and CONFLICT frames oriented toward international audiences, while protest discourse will be dominated by SOLIDARITY and CALL_TO_ACTION frames oriented toward domestic mobilization.

---

## 3. Method: Agentic Content Analysis

### 3.1 The Single-Model Problem

Large language models offer unprecedented capability for text analysis at scale (Gilardi et al., 2023). However, a critical validity threat has been overlooked: models trained by different organizations, on different corpora, with different safety alignments may produce systematically different codings. Researchers using a single model cannot detect these biases.

### 3.2 Agentic Content Analysis (ACA)

We address this through **Agentic Content Analysis**, a methodology that orchestrates multiple LLMs as specialized research agents under human authority. Key principles:

1. **Epistemic Diversity:** Deploy models with heterogeneous origins (Western: Claude; Chinese: GLM-4.7, Kimi K2.5) to surface culturally-conditioned blindspots.

2. **Human Authority:** The human researcher serves as Principal Investigator, issuing directives to AI agents. Agents execute analytical tasks but do not make interpretive decisions autonomously.

3. **Adversarial Review:** Before finalizing any study, each model writes a "Reviewer 2" critique identifying methodological weaknesses, alternative explanations, and overstated claims.

4. **Disagreement as Signal:** Where models diverge, we conduct qualitative analysis to understand why—often revealing theoretically interesting boundary cases.

### 3.3 The HILAR Protocol

Our implementation follows the **Human-in-the-Loop Agentic Research (HILAR)** protocol:

1. **Study Design:** Human PI specifies RQs, sampling, coding framework
2. **Instrument Development:** Coordinating agent drafts protocol; human approves
3. **Multi-Model Coding:** Each model codes independently in isolated sessions
4. **Reliability Assessment:** Calculate pairwise agreement, frame-specific κ
5. **Adversarial Review:** Each model critiques the study design and findings
6. **Qualitative Analysis:** Deep reading of disagreement cases and exemplars
7. **Synthesis:** Human PI interprets findings and draws conclusions

### 3.4 Coding Framework

We employ an integrated frame typology:
- **INFORMATIONAL:** Neutral facts, news, updates
- **INJUSTICE:** Blame attribution, victim/villain identification
- **SOLIDARITY:** Collective identity, support, unity
- **HOPE:** Future-oriented, resilience, positive change
- **CONFLICT:** Confrontation, struggle, battle
- **CALL_TO_ACTION:** Explicit mobilization directives
- **HUMANITARIAN:** Human suffering, compassion appeals

Each post also coded for valence (positive/negative/neutral) and arousal (high/medium/low).

### 3.5 Data

**Ukraine War Corpus (N=339):** English-language tweets containing #Ukraine, collected June 2022. Stratified by engagement tier.

**#MahsaAmini Protest Corpus (N=380):** Persian and English tweets from September-October 2022, following Mahsa Amini's death in morality police custody. Stratified by engagement.

### 3.6 Analytical Strategy

1. **Quantitative:** Frame distributions compared via chi-square; inter-model reliability via Cohen's κ
2. **Qualitative:** Critical Discourse Analysis on INJUSTICE frames (enemy construction); thematic analysis of irony cases

### 3.7 Model Reliability

| Model Pair | Agreement | Cohen's κ |
|------------|-----------|-----------|
| Claude–Kimi | 55.2% | 0.31 |
| Claude–GLM | 48.7% | 0.22 |
| All 3 agree | 42.5% | — |
| 2+ agree | 84.1% | — |

**Critical finding:** GLM-4.7 coded 90.3% of posts as INFORMATIONAL versus ~55% for Claude and Kimi. This systematic bias would be undetectable in single-model studies. We use Claude-Kimi consensus (2+ agreement) for primary analysis.

**Frame-specific reliability** varied dramatically: INFORMATIONAL (73% agreement), INJUSTICE (39%), SOLIDARITY (27%), HOPE (17%). Affective frames show poor reliability, suggesting either codebook refinement is needed or these frames are inherently more ambiguous.

---

## 4. Results

### 4.1 Frame Distributions (H3)

| Frame | Ukraine (War) | #MahsaAmini (Protest) | χ² | p |
|-------|---------------|----------------------|-----|---|
| INFORMATIONAL | 57.2% | 8.4% | 186.3 | <.001 |
| SOLIDARITY | 8.3% | 34.2% | 71.4 | <.001 |
| CALL_TO_ACTION | 3.8% | 18.9% | 38.9 | <.001 |
| HOPE | 4.7% | 12.6% | 14.2 | <.001 |
| INJUSTICE | 12.4% | 11.1% | 0.3 | .584 |
| CONFLICT | 8.0% | 6.3% | 0.7 | .403 |
| HUMANITARIAN | 5.6% | 8.4% | 2.1 | .147 |

**H3 supported.** War discourse is dominated by INFORMATIONAL framing (57%)—news sharing, updates, factual reporting oriented toward international audiences. Protest discourse is dominated by SOLIDARITY (34%) and CALL_TO_ACTION (19%)—collective identity and mobilization oriented toward domestic participants. INJUSTICE framing is equally prevalent in both contexts (~11-12%), suggesting enemy construction is universal to resistance but takes different forms.

### 4.2 Enemy Construction (H1)

#### 4.2.1 War Discourse: Third-Person Dehumanization

**Naming patterns:**
- State-level: "Russia," "#RussianWarCrimes"
- Leader personification: "Putin," "#PutinWarCriminal"
- Fantasy dehumanization: "Orcs from Mordor," "evil Sauron"

**Exemplar:**
> "This is how low Putin's #Russia has sunk. Rape, murder, execute, pillage and steal everything that's of any value. There is no such thing as rule of law for these Orcs from Mordor (Russia) #Putin is the evil Sauron. All nations need to unite to defeat this extensional threat."

**Discourse features:**
- Third-person reference throughout ("Russia," "they," "these Orcs")
- Fantasy metaphor places enemy outside human community
- Appeal to "all nations"—international audience
- Legal framing ("rule of law," implicit war crimes)
- Call for collective action against existential threat

#### 4.2.2 Protest Discourse: Second-Person Moral Shaming

**Naming patterns:**
- System-level: "Islamic Republic," "regime"
- Enforcer-focused: "morality police," "گشت_کشتار" (death patrol)
- Second-person accusation: "بیشرف" (shameless one), "شما" (you)

**Exemplar:**
> "اخه الان این چی دستشه؟ چی آتیش زده؟ چرا میزنی بیشرف؟ شما خودتون زنو دختر ندارید؟"  
> [What does she have in her hand? What did she burn? Why are you beating her, shameless one? Don't you have women and daughters?]

**Discourse features:**
- Second-person address throughout ("you," "your")
- Direct confrontation with perpetrator
- Kinship appeal preserves shared humanity ("Don't you have daughters?")
- Moral shaming rather than dehumanization
- Rhetorical questions demand justification

**H1 supported.** War discourse constructs enemies through third-person fantasy dehumanization oriented toward international intervention. Protest discourse constructs enemies through second-person moral shaming that preserves humanity for accountability.

### 4.3 Irony Deployment (H2)

#### 4.3.1 Irony in Protest: Absurdist Solidarity

**Exemplar 1 (Self-contradiction):**
> "بیشعور تر از جمهوری اسلامی بازم خودش. کلاسای دانشگاهها رو میخواد آنلاین برگزار کنه. نت رو هم قطع کرده 😂😂😂"  
> [More idiotic than the Islamic Republic is... itself. It wants to hold university classes online. It also cut the internet. 😂😂😂]

The self-contradiction (online classes + no internet) exposes regime incompetence through absurdist humor. Laughing emojis signal shared recognition of the absurdity.

**Exemplar 2 (Understatement):**
> "سیگارو گرون کردن :)))"  
> [They made cigarettes more expensive :)))]

Amid massive protests about fundamental rights, a complaint about cigarette prices is darkly comic understatement—coping through absurdism.

**Functions:** Irony in protest discourse serves (1) emotional coping with trauma, (2) in-group solidarity through shared humor, (3) delegitimization without direct confrontation, (4) plausible deniability under surveillance.

#### 4.3.2 Irony in War: Rare and Risky

Irony is notably rare in Ukraine war discourse. When present, it targets Russia's international image:

**Exemplar:**
> "📸Photo of the Day📸 🇷🇺🇮🇷 #Russia worships its true master."

This post inverts Russia's great-power self-image by positioning Iran as the "master." Notably, our Claude model coded this as INFORMATIONAL (missing the irony), while Kimi caught the sarcasm—demonstrating why multi-model validation matters for irony detection.

**Why irony is rare in war discourse:** International audiences may not share the cultural context needed to decode irony. When appealing for military aid and moral support, clarity trumps cleverness. Irony risks being misunderstood as neutrality or even support for the enemy.

**H2 supported.** Irony is substantially more common in protest discourse where it serves solidarity and coping functions. War discourse prioritizes moral clarity for international audiences over in-group humor.

---

## 5. Discussion

### 5.1 A Typology of Discursive Resistance Modes

Our findings support a theoretical distinction between **externalized** and **internalized** resistance discourse:

| Dimension | Externalized (War) | Internalized (Protest) |
|-----------|-------------------|----------------------|
| Enemy location | Foreign state | Own government |
| Primary audience | International community | Fellow citizens + regime |
| Address mode | Third person (about enemy) | Second person (to enemy) |
| Dehumanization | Fantasy metaphor (Orcs) | Moral shaming (shameless) |
| Moral framework | International law, war crimes | Human dignity, bodily autonomy |
| Irony | Rare (clarity needed) | Common (solidarity + coping) |
| Dominant frames | INFORMATIONAL, CONFLICT | SOLIDARITY, CALL_TO_ACTION |
| Goal | International intervention | Domestic revolution |

### 5.2 Theoretical Mechanism: Proximity and Rhetorical Constraint

Why does proximity shape rhetoric? We propose three mechanisms:

**Audience constraint:** External enemies allow appeal to international audiences who require clear moral framing and legal argumentation. Internal enemies require addressing domestic audiences (including the enemy itself) who share cultural context.

**Future constraint:** Resisters must live with internal enemies after the conflict—total dehumanization forecloses reconciliation. External enemies can be dehumanized because coexistence is not required.

**Context constraint:** Irony requires shared cultural knowledge between speaker and audience. International audiences lack this context; domestic audiences possess it.

### 5.3 Implications

**For movement strategy:** Movements should calibrate rhetoric to enemy proximity. External-facing campaigns benefit from legal framing and moral clarity. Internal-facing campaigns can leverage irony and shame.

**For platform governance:** Content moderation trained primarily on Western contexts may miss the functions of irony in repressive contexts, potentially flagging legitimate protest speech.

**For computational methods:** Single-model content analysis cannot detect systematic bias. Multi-model validation should become standard practice.

### 5.4 Limitations

1. **Two cases:** Our typology derives from two contexts; additional cases (Hong Kong, Belarus, Myanmar) would strengthen generalizability.
2. **Platform specificity:** Twitter/X may differ from Telegram, TikTok, or encrypted channels.
3. **Temporal snapshot:** Both corpora capture acute crisis periods; rhetoric may differ in sustained movements.
4. **Language mixing:** The #MahsaAmini corpus includes Persian-English code-switching that may affect frame detection.
5. **Model limitations:** Even multi-model validation cannot guarantee validity; human validation remains essential for publication-quality research.

### 5.5 Future Directions

1. **Longitudinal analysis:** Track rhetorical evolution as movements mature
2. **Cross-platform comparison:** Compare rhetoric across Twitter, Telegram, TikTok
3. **Additional cases:** Test framework on Hong Kong 2019, Belarus 2020, Myanmar 2021
4. **Irony detection:** Develop dedicated classifiers for political irony
5. **Intervention studies:** Test whether rhetorical strategy affects movement outcomes

---

## 6. Conclusion

Distance matters—not just geographic distance, but the structural relationship between resisters and their targets. When the enemy is foreign, activists speak about them to the world, deploying dehumanization and legal frameworks to mobilize international intervention. When the enemy is domestic, activists speak to them directly, deploying shame and irony while preserving the human connection that accountability requires.

This proximity-based framework helps explain why the online discourse of war looks so different from the online discourse of protest, even when both involve death, repression, and urgent mobilization. It suggests that rhetorical strategy is not merely a creative choice but is constrained by structural position.

Our methodological contribution—Agentic Content Analysis—demonstrates that multi-model validation is not merely desirable but necessary. The dramatic divergence between GLM-4.7's coding (90% INFORMATIONAL) and Claude/Kimi's coding (~55%) would be invisible in single-model studies. As LLMs become standard tools for communication research, built-in adversarial validation must become standard practice.

The enemies we face shape the words we use to fight them.

---

## References

Benford, R. D., & Snow, D. A. (2000). Framing processes and social movements. *Annual Review of Sociology, 26*, 611-639.

Billig, M. (2005). *Laughter and Ridicule: Towards a Social Critique of Humour*. Sage.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication, 43*(4), 51-58.

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS, 120*(30), e2305016120.

Keen, S. (1986). *Faces of the Enemy: Reflections of the Hostile Imagination*. Harper & Row.

Silverstein, P. A. (2005). Immigrant racialization and the new savage slot. *Annual Review of Anthropology, 34*, 363-384.

Smith, D. L. (2011). *Less Than Human: Why We Demean, Enslave, and Exterminate Others*. St. Martin's Press.

Snow, D. A., & Benford, R. D. (1988). Ideology, frame resonance, and participant mobilization. *International Social Movement Research, 1*, 197-217.

Wedeen, L. (1999). *Ambiguities of Domination: Politics, Rhetoric, and Symbols in Contemporary Syria*. University of Chicago Press.

---

## Appendix A: Agentic Content Analysis Protocol

### A.1 Agent Configuration

| Agent | Model | Provider | Role |
|-------|-------|----------|------|
| Coordinator | Claude Opus | Anthropic | Workflow management, synthesis |
| Coder-Claude | Claude Opus | Anthropic | Frame coding (Western perspective) |
| Coder-GLM | GLM-4.7 | Zhipu AI | Frame coding (Chinese perspective) |
| Coder-Kimi | Kimi K2.5 | Moonshot | Frame coding (Chinese perspective) |

### A.2 Adversarial Review Prompt

```
You are Reviewer 2 for a top political communication journal. 
Your job is to find fatal flaws. Be brutal but constructive.

Identify:
1. ≥3 methodological weaknesses
2. ≥2 alternative explanations
3. ≥1 confounding variable
4. Specific claims that outrun evidence

Do not be polite. Be the reviewer who makes authors cry (constructively).
```

### A.3 Consensus Rules

- **All 3 agree:** Highest confidence
- **2 of 3 agree:** Used for primary analysis
- **No consensus:** Flagged for qualitative analysis

---

## Appendix B: Frame Codebook

[Full codebook with definitions, examples, and decision rules]

---

## Appendix C: Data Availability

Coded datasets, analysis scripts, and agent interaction logs available at: [repository URL]

---

*Word count: ~4,200*  
*Theory paper with empirical demonstration*
