# AgentAcademy Field Notes

## Note 1: Asymmetric Skill Loading (2026-02-19)

### Observation

During the 7-day AgentAcademy sprint, we discovered an unintended methodological asymmetry:

| Model | CommDAAF Loaded | Environment |
|-------|-----------------|-------------|
| Claude | ✅ Yes | OpenClaw session with full skill |
| GLM-4 | ❌ No | Raw prompt via opencode |
| Kimi K2.5 | ❌ No | Raw prompt via opencode |

Claude receives the full CommDAAF framework:
- Preflight checks
- Critical methodology warnings
- Nudge system for explicit choices
- Tiered validation protocols
- Effect size benchmarks

GLM and Kimi receive only the analysis prompt—no guardrails, no methodology scaffolding.

### Implication

This creates two interpretations:

**Interpretation A: Confound**
The 3-model comparison isn't apples-to-apples. Claude's outputs may be better *because* of CommDAAF, not because of model capability.

**Interpretation B: Natural Experiment**
We're accidentally testing "raw model" vs "framework-guided model." When all three converge on findings despite this asymmetry, that's *stronger* evidence—the raw models found the same patterns without scaffolding.

### What We're Learning

The 3-model convergences we've found (Cuban state media, Kashmir coordination, CNN law enforcement dominance) emerged across this asymmetry. GLM and Kimi reached similar conclusions without CommDAAF's methodology prompts.

This suggests:
1. **The patterns are robust** — detectable with or without framework guidance
2. **CommDAAF's value may be in guardrails, not discovery** — preventing false positives rather than enabling true positives
3. **Raw models can do exploratory analysis** — but may need frameworks for confirmatory/publication work

### Next Steps

Options for future runs:
1. **Keep asymmetry** — continue natural experiment, document as limitation
2. **Inject skill** — prepend SKILL.md to GLM/Kimi prompts for fair comparison
3. **A/B test** — run same dataset with and without CommDAAF on same model

For now, we're documenting this as a methodological note and continuing with the current setup. The convergence data remains valuable.

---

*Field note by AgentAcademy automated research system*
*Sprint: Feb 18-25, 2026*
