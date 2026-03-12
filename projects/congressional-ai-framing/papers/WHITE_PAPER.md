# How Congress Talks About AI
## A Data-Driven Analysis of 192 Congressional Hearings

**March 2026**

---

# Executive Summary

## Key Findings at a Glance

| Finding | Implication |
|---------|-------------|
| **90% of AI hearings occurred after ChatGPT** (Nov 2022) | Congress is reactive, not proactive, on AI policy |
| **"National security" is the #1 frame** (22% of hearings) | AI policy is being securitized—treated as a geopolitical threat |
| **"Economic opportunity" is #2** (21% of hearings) | "Beat China" narrative combines security + innovation |
| **Civil rights concerns emerged only in 2023** | Privacy, bias, and discrimination are afterthoughts |
| **Senate emphasizes security 55% more than House** | Chamber differences will shape legislative outcomes |

## The Bottom Line

**Congress frames AI primarily as a competition to win, not a technology to govern.**

This framing—emphasizing China competition and economic opportunity over risks and rights—will shape the AI policies that emerge. Stakeholders should expect:

- ✅ Strong support for AI R&D investment and talent pipelines
- ✅ Export controls and technology restrictions targeting adversaries
- ⚠️ Limited momentum for comprehensive AI safety regulation
- ⚠️ Rights-based concerns (bias, privacy) treated as secondary

---

# 1. Introduction

Between 2007 and 2026, Congress held **192 hearings** with substantive AI content. We analyzed these hearings to understand how legislators frame AI—because framing shapes policy.

**Method**: We used advanced AI systems (Kimi K2.5 and Claude Opus 4.5) to code each hearing, achieving 72% agreement between coders. This approach allowed analysis at scale while maintaining research-grade reliability.

---

# 2. The AI Attention Explosion

![Temporal Trend](figures/fig1_temporal_trend.png)

### Before ChatGPT (2007-2022)
- **20 hearings** over 15 years
- Average: 1.3 hearings per year
- Focus: workforce, automation, early exploration

### After ChatGPT (2023-2026)
- **172 hearings** in 3 years
- Average: 57 hearings per year
- Focus: China competition, regulation, safety

**Insight**: Congressional attention increased **44x** after ChatGPT. This reactive pattern suggests policy is being developed under pressure rather than through deliberate foresight.

---

# 3. How Congress Frames AI

![Frame Distribution](figures/fig2_frame_distribution.png)

## The Top 3 Frames (62% of hearings)

### 🔴 Sovereignty (22%)
*"We're in an AI arms race with China"*

- National security implications
- Technology competition with adversaries
- Export controls and talent pipelines
- Defense and intelligence applications

**Example hearings**: 
- "Artificial Intelligence and National Security"
- "Winning the AI Competition with China"

### 🟢 Innovation (21%)
*"AI will create jobs and grow the economy"*

- Economic opportunity and competitiveness
- Scientific advancement and R&D
- Startup ecosystems and talent
- U.S. technological leadership

**Example hearings**:
- "The Promise of AI in American Agriculture"
- "AI for Drug Discovery and Healthcare"

### 🔵 Governance (19%)
*"How should we regulate AI?"*

- Regulatory frameworks and oversight
- Federal vs. state authority
- Sector-specific vs. horizontal rules
- Compliance and auditing

**Example hearings**:
- "Establishing Rules for AI Transparency"
- "The NIST AI Risk Management Framework"

## The Remaining Frames (38%)

| Frame | % | Description |
|-------|---|-------------|
| Risk/Harm | 10.5% | Deepfakes, child safety, discrimination |
| Risk/Safety | 9.9% | Existential risk, autonomous weapons |
| Rights | 9.3% | Privacy, algorithmic bias, civil liberties |
| Risk/Economic | 5.2% | Job displacement, inequality |
| Technical | 2.9% | How AI systems work |

---

# 4. Senate vs. House: Different Priorities

![Chamber Comparison](figures/fig3_chamber_comparison.png)

| Frame | House | Senate | Difference |
|-------|-------|--------|------------|
| **Sovereignty** | 18% | 28% | Senate +55% |
| **Innovation** | 23% | 15% | House +53% |
| **Risk/Harm** | 9% | 15% | Senate +67% |

### Why This Matters

**Senate**: Constitutional role in foreign policy drives security focus. Armed Services, Foreign Relations, and Intelligence committees dominate AI hearings.

**House**: Closer to constituents and economic interests. Science, Small Business, and Commerce committees emphasize innovation.

**Prediction**: Senate AI legislation will emphasize security restrictions; House will emphasize innovation incentives. Conference negotiations will be contentious.

---

# 5. Frame Evolution Over Time

![Frame Evolution](figures/fig4_frame_evolution.png)

### 2017-2020: The Innovation Era
- Dominant frames: Innovation, Economic Risk
- Tone: Cautiously optimistic
- Key concern: Automation and jobs

### 2021-2022: The Pivot
- Rising frame: Sovereignty
- Trigger: China competition discourse intensifies
- Tone: Urgent, competitive

### 2023-2026: The Securitization
- Dominant frames: Sovereignty, Innovation, Governance
- **New frame**: Rights (first appears in 118th Congress)
- Tone: Alarm + opportunity

### Key Trend: Rights Came Late

Civil liberties and discrimination concerns were **absent** from congressional AI discourse until 2023. This late emergence suggests:

1. Rights advocates were not at the table in early AI policy discussions
2. Concrete harms (deepfakes, bias cases) drove eventual attention
3. Rights framing remains a minority position (9.3%)

---

# 6. Implications for Stakeholders

## For Technology Companies

✅ **Opportunity**: Innovation framing suggests receptivity to R&D investment, tax incentives, and talent pipelines

⚠️ **Risk**: Sovereignty framing may lead to export restrictions, supply chain requirements, and compliance burdens

📋 **Action**: Engage on governance frame—help shape regulatory frameworks before they calcify

## For Civil Society

⚠️ **Challenge**: Rights frame is minority position; advocacy has not penetrated congressional discourse

📋 **Action**: Connect rights concerns to sovereignty frame ("AI bias undermines national competitiveness") or harm frame ("concrete cases of discrimination")

## For Researchers

✅ **Opportunity**: Technical frame is smallest (2.9%)—Congress needs expertise

📋 **Action**: Translate technical knowledge into policy-relevant frames. Lead with implications, not mechanisms.

## For International Partners

⚠️ **Challenge**: Sovereignty frame constructs AI as zero-sum competition

📋 **Action**: Propose cooperative frameworks that address security concerns while enabling collaboration

---

# 7. Methodology Note

## How We Did This

1. **Collected** 561 congressional hearing transcripts via GovInfo API
2. **Filtered** to 193 hearings with substantive AI content
3. **Coded** each hearing using two AI systems (Kimi K2.5, Claude Opus 4.5)
4. **Validated** with inter-rater reliability testing (Cohen's κ = 0.656)

## Reliability Improvement

![Reliability](figures/fig5_reliability.png)

Initial AI coding produced poor results (κ = 0.206) because the AI coders defaulted to "governance" for all congressional hearings. We refined our prompts to focus on **how AI is framed** rather than document type, improving reliability to κ = 0.656 ("substantial agreement").

**Lesson**: AI tools require careful prompt engineering for research applications.

---

# 8. Conclusion

## Congress sees AI as a race to win.

The dominance of sovereignty and innovation frames—combined with the marginalization of rights and safety concerns—signals that AI policy will prioritize:

- **Competition** over cooperation
- **Speed** over caution
- **Economic growth** over equity

Stakeholders seeking to influence AI policy should engage with dominant frames or work to elevate alternatives. The framing battle is far from settled, but the current trajectory favors a security-innovation nexus that may sideline important concerns about AI's impacts on individuals and society.

---

# About This Report

**Author**: AgentAcademy Agents

⚠️ **Disclaimer**: This research was conducted entirely by AI agents. Findings should be validated by human researchers before application.

**Data**: 192 congressional hearings (110th-119th Congress)

**Method**: Multi-model AI content analysis with CommDAAF framework

**Reliability**: Cohen's κ = 0.656 (substantial agreement)

**Contact**: [wayne.xu@umass.edu]

---

*© 2026. This report may be freely distributed with attribution.*
