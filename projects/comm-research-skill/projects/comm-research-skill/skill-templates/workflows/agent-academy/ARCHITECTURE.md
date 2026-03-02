# CommDAAF Architecture: Three-Layer Design

> **Attribution**: This architecture is inspired by Xu & Yang (2026), "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Reanalysis." Their key insight: **separate scientific reasoning from computational execution** to enable reproducible, auditable AI-assisted research.
>
> Paper: https://yiqingxu.org/papers/2026_ai/AI_reproducibility.pdf

## Core Principle

> "The system separates scientific reasoning from computational execution: researchers design fixed diagnostic templates, and the workflow automates the acquisition, harmonization, and execution of replication materials using pre-specified, version-controlled code."
> — Xu & Yang (2026)

In CommDAAF, this translates to:
- **Humans** design research frameworks, validation criteria, and interpretation guidelines
- **AI** executes data processing, statistical computation, and report generation
- **Neither** crosses into the other's domain

---

## Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: LLM ORCHESTRATOR                                  │
│  ─────────────────────────────────────────────────────────  │
│  • Routes tasks between agents                              │
│  • Interprets failures and selects recovery strategies      │
│  • Coordinates workflow stages                              │
│  • NEVER performs statistical computation                   │
│                                                             │
│  Models: Claude Opus (coordination), GPT-4o (adversarial)   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 2: SKILL DESCRIPTIONS & KNOWLEDGE BASE               │
│  ─────────────────────────────────────────────────────────  │
│  • SKILL.md — Interface contracts (inputs, outputs, tools)  │
│  • KNOWLEDGE_BASE.md — Resolved failure patterns            │
│  • LESSONS_LEARNED.md — Research methodology lessons        │
│  • Version-controlled; evolves between runs, not during     │
│                                                             │
│  Files: workflows/*.md, methods/*.md, theories/*.md         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 3: DETERMINISTIC COMPUTATION                         │
│  ─────────────────────────────────────────────────────────  │
│  • All statistical analysis in R/Python scripts             │
│  • Same inputs → Same outputs (reproducible)                │
│  • No LLM calls in computation path                         │
│  • Version-controlled diagnostic templates                  │
│                                                             │
│  Scripts: analysis.R, network_metrics.py, validation.py    │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer Responsibilities

### Layer 1: LLM Orchestrator

**What it does:**
- Reads research requests and routes to appropriate agents
- Parses failure logs and matches to known patterns
- Decides which stage to execute next
- Generates candidate fixes for novel failures (human review required)

**What it NEVER does:**
- Compute statistics, correlations, or effect sizes
- Transform data (filtering, aggregation, recoding)
- Generate numbers that appear in final reports

**Implementation:**
```yaml
# Orchestrator decisions are logged, not computed
orchestrator:
  role: coordination
  allowed_actions:
    - route_task
    - interpret_error
    - select_recovery
    - request_human_review
  forbidden_actions:
    - compute_statistic
    - transform_data
    - generate_coefficient
```

### Layer 2: Skill Descriptions & Knowledge Base

**Components:**

1. **Interface Contracts** (SKILL.md, WORKFLOW.md)
   - Required inputs for each stage
   - Expected outputs
   - Permissible tools
   - Execution constraints

2. **Failure Knowledge Base** (KNOWLEDGE_BASE.md)
   - Documented failure patterns
   - Root causes
   - Generalized resolution rules
   - Version history

3. **Research Lessons** (LESSONS_LEARNED.md)
   - Methodology insights from AgentAcademy runs
   - New probing questions
   - Updated checks

**Update Protocol:**
- Updates happen **between runs**, not during
- All changes are version-controlled
- Human review required for new patterns

### Layer 3: Deterministic Computation

**Principle:** Given the same inputs and pipeline version, outputs are identical.

**Implementation:**
```python
# All computation in explicit scripts
def compute_engagement_metrics(df: pd.DataFrame) -> dict:
    """
    Deterministic computation — no LLM involvement.
    Same df → same output, always.
    """
    return {
        'mean_engagement': df['engagement'].mean(),
        'median_engagement': df['engagement'].median(),
        'std_engagement': df['engagement'].std(),
        'n_observations': len(df),
        'computed_at': datetime.now().isoformat(),
        'script_version': '1.0.0'
    }
```

**Audit Trail:**
- Every computation logs inputs, outputs, and script version
- Intermediate artifacts saved to disk
- No hidden state between stages

---

## Information Flow

```
                    DOWNWARD (Instructions)
                           │
    Layer 1 ──────────────▼─────────────────▶ Layer 3
    (Orchestrator)    task dispatch         (Computation)
                           │
                           │
                    UPWARD (Results)
                           │
    Layer 1 ◀─────────────┴─────────────────── Layer 3
    (Orchestrator)    logs, artifacts,        (Computation)
                      error messages
                           │
                           ▼
                      SIDEWAYS (Updates)
                           │
    Layer 2 ◀──────────────┴──────────────────▶ Layer 2
    (Knowledge)    new patterns, lessons      (Knowledge)
                   (between runs only)
```

---

## Cross-Agent Validation

> "For Stata-based studies, the Runner performs cross-language validation. It translates the Stata IV command into an equivalent R specification and re-estimates the model on the same dataset."
> — Xu & Yang (2026)

In CommDAAF, this becomes **cross-model validation**:

```yaml
cross_validation:
  required: true  # MANDATORY, not optional
  
  protocol:
    1. Agent A (GLM) computes key statistics
    2. Agent A exports results to JSON
    3. Agent B (Kimi) independently re-computes on same data
    4. System compares results
    5. Flag divergence > threshold
    
  thresholds:
    coefficient_tolerance: 0.01  # 1% relative difference
    correlation_tolerance: 0.05  # 0.05 absolute difference
    count_tolerance: 0           # Must match exactly
    
  on_divergence:
    - Log discrepancy details
    - Trace computation path
    - Human review required
    - Do not proceed until resolved
```

---

## Credibility Rating Scheme

> Adapted from Xu & Yang (2026) Table S1

| Rating | Warnings | Interpretation | Action |
|--------|----------|----------------|--------|
| **HIGH** | 0 | Methods sound, results robust | Proceed to interpretation |
| **MODERATE** | 1-2 | Some concerns | Flag for human review |
| **LOW** | 3-4 | Substantial validity concerns | Require methodology revision |
| **VERY LOW** | 5+ | Results likely unreliable | Do not publish; redesign study |

**Warning Triggers (Communication Research):**
1. Sample size < 100 for correlational claims
2. Effect size not reported or misclassified
3. No temporal controls (for longitudinal data)
4. Missing bot/coordination check (for social media)
5. Cross-agent validation failed
6. Key assumption not tested
7. Multiple comparisons without correction
8. Claims exceed evidence (per claim-evidence matcher)

---

## Version Control Protocol

Every run is tied to a specific pipeline version:

```json
{
  "run_id": "academy-2026-02-18-001",
  "pipeline_version": "0.7.0",
  "skill_version": "0.7.0",
  "knowledge_base_version": "2026-02-18",
  "agents": {
    "glm": "zai/glm-4.7",
    "kimi": "kimi-coding/k2p5"
  },
  "deterministic_scripts": {
    "analysis.py": "sha256:abc123...",
    "validation.R": "sha256:def456..."
  }
}
```

**Between-run updates:**
- New failure patterns → Add to KNOWLEDGE_BASE.md
- New methodology lessons → Add to LESSONS_LEARNED.md
- Script fixes → Version bump, update hash

**Within-run invariants:**
- No knowledge base modifications
- No script modifications
- Deterministic outputs for fixed inputs

---

## Implementation Checklist

- [ ] Separate orchestration code from computation code
- [ ] Create explicit interface contracts for each agent
- [ ] Implement cross-agent validation as mandatory step
- [ ] Version-control all deterministic scripts
- [ ] Log all intermediate artifacts to disk
- [ ] Add credibility rating to output reports
- [ ] Document failure patterns in KNOWLEDGE_BASE.md

---

## References

Xu, Yiqing and Leo Yang Yang. 2026. "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Reanalysis." Working Paper, Stanford University.
https://yiqingxu.org/papers/2026_ai/AI_reproducibility.pdf
