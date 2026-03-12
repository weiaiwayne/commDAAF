# The Competition Frame: How Congress Constructs AI as a Geopolitical Race

**Wayne Xu**  
Department of Communication, University of Massachusetts Amherst

---

## Abstract

Congressional attention to artificial intelligence has surged since 2022, yet how legislators frame this technology remains understudied. This analysis of 192 congressional hearings reveals that AI discourse is dominated by a **competition frame**—geopolitical sovereignty claims (22%) combined with economic opportunity narratives (21%)—positioning AI development as a race against China. This framing marginalizes alternatives emphasizing civil liberties (9%) or algorithmic harms (11%). The competition frame has policy consequences: by defining AI as a race to be won, Congress privileges acceleration over precaution, investment over regulation. Methodologically, we demonstrate that large language models can achieve substantial reliability (κ = .66) as content coders when document-type bias is addressed through targeted prompt engineering.

---

"We are in a technological competition with China that will determine the future of the 21st century." This declaration, delivered by Senator Mark Kelly in January 2024, has become routine in congressional AI discourse. Since ChatGPT's release in November 2022, such framings have proliferated, constructing AI development as a matter of national urgency requiring American mobilization. The construction is neither natural nor inevitable—it reflects choices about how to define a complex technology as a policy problem.

Framing research has long demonstrated that problem definition is itself political (Entman, 1993; Gamson & Modigliani, 1989). When Congress frames AI as competition with China, it privileges certain policy responses—investment, acceleration, military applications—while marginalizing others: precautionary regulation, civil liberties protections, international cooperation. The frames that dominate legislative discourse shape the legislation that emerges (Baumgartner & Jones, 1993).

This study documents the consolidation of what we term the **competition frame** in congressional AI discourse. Drawing on 192 hearings from the 117th through 119th Congresses, we find that competition framing—combining geopolitical sovereignty claims with economic opportunity narratives—accounts for 43% of hearings. Rights-based framing appears in only 9%. The competition frame has achieved dominance; alternatives have been marginalized.

## Framing Emerging Technologies

The construction of new technologies as policy problems has been central to political communication research since Gamson and Modigliani's (1989) study of nuclear power discourse. They demonstrated that competing frames—"progress" versus "runaway technology"—shaped both public opinion and policy trajectories. Frames are not merely rhetorical packaging; they constitute the problems that policy addresses.

AI presents distinctive framing challenges. Unlike nuclear power or genetic engineering, AI is not a single technology but a family of techniques spanning military systems, consumer products, creative tools, and scientific research. This heterogeneity creates multiple entry points: AI can be constructed as economic engine, security threat, civil liberties concern, labor disruption, or scientific frontier. Which construction dominates is empirically open—and consequential.

Recent scholarship documents AI's emergence as a political issue. Cave and Dihal (2019) identify recurring "hopes and fears" in AI discourse. Ulnicane and colleagues (2021) trace how "AI nationalism" frames proliferate across national contexts. Bradford (2020) analyzes how the EU's regulatory approach shapes global governance frames. Yet systematic analysis of AI framing in legislative contexts remains limited.

Congressional hearings represent a distinctive arena for framing analysis. Unlike media discourse, congressional framing carries direct policy implications: the frames that dominate legislative discourse shape legislation (Baumgartner & Jones, 1993). Kingdon's (1995) multiple streams framework suggests that ChatGPT functioned as a "focusing event" creating a policy window for AI issues. The question is how that window has been filled—what frames have been selected, and what alternatives foreclosed.

## Method

We collected hearing transcripts from the Government Publishing Office (GovInfo) API, searching for hearings containing "artificial intelligence" in the CHRG collection. Initial retrieval yielded 1,754 hearings. To distinguish hearings substantively about AI from those mentioning it incidentally, we applied a density threshold based on AI term frequency, retaining 192 hearings.

The sample is concentrated in the 118th and 119th Congresses (2023–2026): 90% of hearings occurred after ChatGPT's release. This concentration reflects both genuine policy attention and AI hype cycle effects we cannot disentangle. With only 20 pre-2023 hearings, temporal inference is limited.

We developed an eight-frame typology: sovereignty, innovation, governance, harm, safety, rights, economic risk, and technical. Two large language models—Kimi K2.5 and Claude Opus 4.5—served as independent coders. Initial reliability was poor (κ = .21) due to document-type bias: models coded the procedural nature of hearings (congressional governance activity) rather than AI content framing. A targeted prompt revision—"code the dominant MESSAGE about AI, NOT the document type"—improved reliability to κ = .66. Per-frame reliability varied: sovereignty and harm achieved strong reliability (κ > .70); rights fell below threshold (κ = .52).

## Findings

### The Dominance of Competition Framing

Congressional AI discourse is dominated by competition framing. Sovereignty frames (22%) construct AI as great-power competition, particularly with China:

> "If we don't lead in AI, China will—and that has implications for everything from our military advantage to our economic prosperity."

Innovation frames (21%) complement this by emphasizing opportunity capture:

> "AI represents the greatest economic opportunity of our lifetime. American companies are poised to create millions of jobs."

Together, these frames position AI as a zero-sum contest requiring mobilization. The competition frame now accounts for 43% of hearings.

### What Congress Is Not Saying

Equally revealing is what congressional discourse marginalizes. Rights-based framing—privacy, due process, algorithmic discrimination—appears in only 9% of hearings. Harm framing—bias, manipulation, misinformation—appears in 11%. These concerns, central to academic and advocacy discussions, remain peripheral in legislative deliberation.

When rights issues appear, they are subordinated to competition:

> "We need to address concerns about AI bias, but we can't let those concerns slow us down in the race with China."

Competition framing does not merely dominate; it actively repositions alternatives as obstacles to winning.

### Chamber Patterns

The Senate emphasizes sovereignty framing (28%) more than the House (18%), consistent with its constitutional foreign policy role. This difference approaches significance (p = .10) but requires larger samples to confirm. Committee-level analysis reveals predictable jurisdictional patterns: Armed Services shows 42% sovereignty framing; Judiciary shows 28% rights framing; Commerce shows 35% innovation framing.

## Discussion

### Issue Definition and Its Consequences

The competition frame has concrete policy implications. By constructing AI as a race with China, Congress privileges responses emphasizing speed and investment while marginalizing precaution and cooperation. This echoes earlier technology competitions—Sputnik functioned similarly as a focusing event that shaped not just attention but its direction.

Competition framing provides clear rhetorical advantages: identifiable adversaries (China), simple metrics (leadership), and obvious prescriptions (accelerate). These advantages may explain its dominance over more complex frames acknowledging tradeoffs. But competition framing carries risks: it may encourage corner-cutting on safety, foreclose international cooperation, and embed contestable assumptions—that AI development is a race, that national leadership is possible, that acceleration is desirable—as unexamined premises.

### The Marginalization of Rights

Rights framing (9%) is marginal despite extensive documentation of algorithmic harms in academic and advocacy contexts. Several factors may explain this: rights framing emphasizes constraints that fit awkwardly within competition frames emphasizing speed; rights constituencies may have less access to agenda-setting than industry or security actors; AI-specific harms may lack established policy templates.

The implication: if Congress constructs AI primarily through competition frames, rights protections become afterthoughts rather than design principles—corrections to completed systems rather than constraints on development.

### Methodological Implications

This study demonstrates the feasibility of LLM-based framing analysis while identifying critical considerations. We achieved substantial reliability (κ = .66) through targeted prompt engineering. However, reliability measures inter-LLM agreement, not validity—both models may share training-induced biases. Human validation remains necessary for validity claims. The document-type bias we identified—LLMs coding formal document features rather than content framing—is a consideration for researchers applying similar methods to institutional texts.

## Conclusion

Congressional AI discourse is dominated by competition framing—a construction combining geopolitical sovereignty and economic opportunity that positions AI development as a race requiring American mobilization. This frame marginalizes alternatives emphasizing rights, harms, or precautionary governance.

Frame dominance has consequences. By defining AI as a competition, Congress creates path dependencies that may shape policy for decades. Precaution, cooperation, and rights protection must now contend with an established frame that constructs them as competitive liabilities. The current moment is distinctive: attention is intense but recent, frame competition remains active, outcomes remain undetermined. Understanding how AI is being constructed—and what constructions are marginalized—is crucial for those seeking to shape its governance.

---

## References

Baumgartner, F. R., & Jones, B. D. (1993). *Agendas and instability in American politics*. University of Chicago Press.

Bradford, A. (2020). *The Brussels effect: How the European Union rules the world*. Oxford University Press.

Cave, S., & Dihal, K. (2019). Hopes and fears for intelligent machines in fiction and reality. *Nature Machine Intelligence*, 1(2), 74–78.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51–58.

Gamson, W. A., & Modigliani, A. (1989). Media discourse and public opinion on nuclear power. *American Journal of Sociology*, 95(1), 1–37.

Kingdon, J. W. (1995). *Agendas, alternatives, and public policies* (2nd ed.). HarperCollins.

Ulnicane, I., Knight, W., Leach, T., Stahl, B. C., & Wanjiku, W. G. (2021). Framing governance for a contested emerging technology: Insights from AI policy. *Policy and Society*, 40(2), 158–177.

---

*Wayne Xu is a doctoral candidate in the Department of Communication at the University of Massachusetts Amherst. His research examines computational approaches to political communication.*

*Correspondence: wxu@umass.edu*
