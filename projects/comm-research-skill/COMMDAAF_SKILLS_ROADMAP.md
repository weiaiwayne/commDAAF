# CommDAAF Skills Roadmap: Universally Applicable Modules

*Date: 2026-02-27*

## Current Capabilities (v0.5)
- Frame analysis (7-frame typology)
- Valence/arousal coding
- Multi-model validation
- Reliability assessment (Fleiss' κ, frame-specific)
- Regression guidance (distribution diagnostics)

---

## Proposed New Skills

### 1. 📚 LITERATURE SYNTHESIS
**Use case:** Every project starts with "what does the literature say?"

**Capabilities:**
- Systematic search across databases (Semantic Scholar, OpenAlex, arXiv)
- Citation network mapping (who cites whom)
- Theoretical lineage tracing (concept → foundational paper → descendants)
- Gap identification (what hasn't been studied?)
- Auto-generation of lit review drafts with proper citations

**Why universal:** Every paper needs a lit review. Currently researchers do this manually or use tools like Elicit that don't integrate with analysis.

**CommDAAF integration:** 
```
commdaaf.literature_search(
    concepts=["framing", "virality", "protest"],
    years=(2018, 2026),
    min_citations=10
)
```

---

### 2. 📋 CODEBOOK GENERATOR
**Use case:** Translating theoretical constructs into operational coding schemes

**Capabilities:**
- Input: theoretical construct + key citations
- Output: operational definition, decision rules, anchors/examples
- Auto-generate counter-examples (what does NOT count)
- Suggest reliability thresholds based on construct complexity
- Produce multilingual anchors when needed

**Why universal:** The gap between theory and measurement is where most coding fails. Explicit operationalization prevents drift.

**CommDAAF integration:**
```
commdaaf.generate_codebook(
    construct="injustice frame",
    theory_source="Gamson 1992",
    languages=["en", "fa", "ar"]
)
```

---

### 3. 🎯 SAMPLING STRATEGIST
**Use case:** Deciding what to analyze from large datasets

**Capabilities:**
- Stratified sampling (by engagement, time, source, etc.)
- Purposive sampling (theoretically interesting cases)
- Saturation detection (when have you seen enough?)
- Power analysis for planned comparisons
- Temporal weighting (oversample recent, undersample old)
- Outlier identification (unusual cases worth examining)

**Why universal:** Most datasets are too large to code entirely. Smart sampling is prerequisite to valid inference.

**CommDAAF integration:**
```
commdaaf.sample(
    data=tweets,
    strategy="stratified",
    strata="engagement_tier",
    n_per_stratum=100,
    ensure_coverage=["viral", "zero_engagement"]
)
```

---

### 4. 🔍 COORDINATION DETECTOR
**Use case:** Identifying inauthentic/coordinated behavior in social media data

**Capabilities:**
- Temporal co-posting patterns (burst detection)
- Content similarity clustering (copy-paste detection)
- Network coordination signatures (who amplifies whom)
- Bot likelihood scoring
- Hashtag hijacking detection
- Cross-platform coordination mapping

**Why universal:** Every social media study needs to address "is this organic?" Bots and coordinated campaigns distort findings.

**CommDAAF integration:**
```
commdaaf.detect_coordination(
    posts=tweets,
    methods=["temporal", "content", "network"],
    threshold=0.8
)
```

**Lessons from our work:** Belarus/Xinjiang studies showed dual-sided coordination. Need to check BOTH sides of any controversy.

---

### 5. 🗣️ NARRATIVE ANALYZER
**Use case:** Story structure in news, social media, political communication

**Capabilities:**
- Actor identification (heroes, villains, victims)
- Plot structure (problem → struggle → resolution)
- Causal claims extraction (X caused Y)
- Temporal sequencing (before/after framing)
- Moral of the story inference
- Counter-narrative detection

**Why universal:** Narratives are how humans make sense of events. Distinct from framing (which is about salience/selection).

**CommDAAF integration:**
```
commdaaf.analyze_narrative(
    text=article,
    extract=["actors", "plot", "moral", "causal_claims"]
)
```

---

### 6. 🖼️ MULTIMODAL CODER
**Use case:** Images, videos, memes in social media research

**Capabilities:**
- Image-text relationship (illustrative, contradictory, complementary)
- Visual frame detection (what's shown vs. not shown)
- Meme template identification
- Face/emotion detection in images
- Video keyframe extraction and coding
- Platform-specific formats (TikTok duets, IG carousels)

**Why universal:** Social media is increasingly visual. Text-only analysis misses most content.

**CommDAAF integration:**
```
commdaaf.code_multimodal(
    post=tweet_with_image,
    text_codes=["frame", "valence"],
    image_codes=["visual_frame", "emotional_appeal"]
)
```

---

### 7. 🌐 CROSS-CULTURAL VALIDATOR
**Use case:** Ensuring coding schemes work across languages/cultures

**Capabilities:**
- Back-translation validation
- Cultural anchor calibration (is "high arousal" the same in Persian vs. English?)
- Idiom/metaphor detection and handling
- Code equivalence testing across languages
- Culture-specific construct warnings

**Why universal:** Globalized communication requires cross-cultural validity. Many constructs don't translate directly.

**CommDAAF integration:**
```
commdaaf.validate_crosscultural(
    codebook=my_codebook,
    languages=["en", "zh", "ar", "fa"],
    flag_nonequivalent=True
)
```

---

### 8. 📊 EFFECT SIZE INTERPRETER
**Use case:** Moving from "significant" to "meaningful"

**Capabilities:**
- Auto-calculate Cohen's d, η², IRR, odds ratios
- Benchmark against field norms (what's "large" in comm research?)
- Confidence interval visualization
- Practical significance translation ("posts got 2.7x more engagement")
- Multiple comparison correction (Bonferroni, FDR)
- Power analysis for detected effects

**Why universal:** p-values are not enough. Effect sizes and practical significance are required for interpretation.

**CommDAAF integration:**
```
commdaaf.interpret_effects(
    model=regression_results,
    benchmarks="communication_research",
    report_format="narrative"
)
```

---

### 9. 🔁 REPLICATION ASSISTANT
**Use case:** Reproducing others' analyses or preparing for replication

**Capabilities:**
- Parse published methods sections
- Generate replication protocols
- Identify unstated assumptions
- Flag under-specified procedures
- Compare replication results to original
- Document deviations and their impact

**Why universal:** Replication crisis affects all social science. Making replication easier benefits everyone.

**CommDAAF integration:**
```
commdaaf.generate_replication_protocol(
    paper_doi="10.1234/example",
    data_available=True
)
```

---

### 10. ⚖️ ETHICS CHECKER
**Use case:** Pre-submission ethical review

**Capabilities:**
- Privacy risk assessment (re-identification potential)
- Consent requirement analysis (public vs. private data)
- Vulnerable population flags
- Platform ToS compliance check
- Data retention recommendations
- IRB documentation generation

**Why universal:** Ethical lapses damage researchers and fields. Proactive checking prevents problems.

**CommDAAF integration:**
```
commdaaf.ethics_check(
    data_source="twitter_api",
    contains_pii=True,
    population="activists"
)
```

---

## Priority Matrix

| Skill | Effort | Impact | Priority |
|-------|--------|--------|----------|
| Codebook Generator | Low | High | 🔴 **P1** |
| Effect Size Interpreter | Low | High | 🔴 **P1** |
| Sampling Strategist | Medium | High | 🔴 **P1** |
| Literature Synthesis | High | High | 🟡 P2 |
| Coordination Detector | Medium | Medium | 🟡 P2 |
| Multimodal Coder | High | High | 🟡 P2 |
| Narrative Analyzer | Medium | Medium | 🟢 P3 |
| Cross-Cultural Validator | Medium | Medium | 🟢 P3 |
| Replication Assistant | Low | Medium | 🟢 P3 |
| Ethics Checker | Low | Medium | 🟢 P3 |

---

## Implementation Notes

### Skill Architecture
Each skill should be:
1. **Standalone** - usable without other skills
2. **Composable** - chainable with other skills
3. **Model-agnostic** - work with Claude, GPT, GLM, Kimi, etc.
4. **Auditable** - log decisions for transparency
5. **Configurable** - adjust thresholds, outputs, verbosity

### Integration with Existing CommDAAF
```python
from commdaaf import Pipeline

pipeline = Pipeline()
pipeline.add(SamplingStrategist(strategy="stratified", n=400))
pipeline.add(CodebookGenerator(constructs=["frame", "valence"]))
pipeline.add(MultiModelCoder(models=["claude", "glm", "kimi"]))
pipeline.add(ReliabilityAssessor(metric="fleiss_kappa"))
pipeline.add(EffectSizeInterpreter(benchmarks="comm_research"))
pipeline.run(data=tweets)
```

### Documentation Pattern
Each skill needs:
- SKILL.md (what it does, when to use)
- EXAMPLES.md (worked examples)
- LIMITATIONS.md (what it can't do)
- VALIDATION.md (how we know it works)

---

## Lessons from #MahsaAmini Project

What we wished we had:

1. **Codebook Generator** - We wrote frame definitions manually; could have been templated
2. **Sampling Strategist** - We did stratification manually; should be automated
3. **Effect Size Interpreter** - We computed Cohen's d manually; should be automatic
4. **Cross-Cultural Validator** - Persian/Arabic anchors were afterthoughts; should be systematic
5. **Coordination Detector** - We didn't check for bots; should be standard

What we learned works:
- Multi-model validation is essential
- Frame-specific reliability prevents false confidence
- Distribution diagnostics before regression
- Transparent failure documentation

---

## Next Steps

1. **Implement P1 skills** (Codebook Generator, Effect Size Interpreter, Sampling Strategist)
2. **Test on new dataset** (Ukraine? different topic?)
3. **Write skill documentation** following OpenClaw pattern
4. **Publish skills to ClawHub** for community use
5. **Solicit feedback** from comm researchers

---

## Open Questions

- Should skills be comm-specific or general social science?
- How do we validate skills work correctly? (meta-reliability?)
- What's the right granularity? (10 skills vs. 50 micro-skills?)
- How do we handle skill versioning as models improve?
- Community contribution model?
