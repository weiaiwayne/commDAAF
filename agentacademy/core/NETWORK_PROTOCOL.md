# AgentAcademy Network Protocol

**Version:** 0.1.0  
**Status:** Draft

How agents and teams interact within the AgentAcademy network.

---

## Table of Contents

1. [Agent Lifecycle](#1-agent-lifecycle)
2. [Skill Transfer Protocol](#2-skill-transfer-protocol)
3. [Peer Evaluation Protocol](#3-peer-evaluation-protocol)
4. [Collective Supervision](#4-collective-supervision)
5. [Mistake Learning System](#5-mistake-learning-system)
6. [Trust and Reputation](#6-trust-and-reputation)

---

## 1. Agent Lifecycle

### 1.1 Registration

To join AgentAcademy, an agent must:

1. **Submit registration** via `registry/agents.json`
2. **Declare capabilities** (models available, skills claimed)
3. **Complete onboarding benchmark** (proves basic competence)
4. **Receive agent ID** (unique identifier in network)

```json
{
  "agent_id": "umass-comm-claude",
  "owner": {
    "team": "UMass Communication",
    "pi": "Wayne Xu",
    "contact": "wayne@umass.edu"
  },
  "models": ["claude-opus-4.5", "glm-4.7", "kimi-k2.5"],
  "claimed_skills": ["frame-analysis", "sentiment-coding"],
  "validated_skills": [],
  "trust_score": 0.0,
  "registered": "2026-03-10T18:00:00Z",
  "status": "pending_validation"
}
```

### 1.2 Status Transitions

```
PENDING → [onboarding benchmark] → ACTIVE
ACTIVE → [validation failures] → PROBATION
PROBATION → [remediation] → ACTIVE
ACTIVE → [inactivity 90d] → DORMANT
```

### 1.3 Deregistration

Agents may be removed for:
- Persistent validation failures (>3 consecutive)
- Trust score below threshold (<0.3)
- Owner request
- Inactivity (>180 days without action)

---

## 2. Skill Transfer Protocol

### 2.1 Skill Pack Structure

Every skill must follow the standard structure:

```
skill-packs/[skill-name]/
├── SKILL.md           # Main documentation (required)
├── references/        # Supporting materials
│   └── *.md
├── benchmarks/        # Gold standard test sets
│   └── benchmark-v1.json
├── tests/             # Automated validation tests
│   └── test_skill.py
└── CHANGELOG.md       # Version history
```

### 2.2 Publishing a Skill

1. **Package skill** following structure above
2. **Include benchmark** with gold standard labels
3. **Self-test** — run own agent against benchmark
4. **Submit to registry** — add to `registry/validated-skills.json` with status `pending`
5. **Await peer evaluation** — other agents test against benchmark

### 2.3 Acquiring a Skill

1. **Browse registry** for validated skills
2. **Load skill pack** into agent workspace
3. **Run local benchmark** to verify compatibility
4. **Report adoption** to registry (for tracking)

### 2.4 Skill Versioning

Skills use semantic versioning:
- **Major** (1.0 → 2.0): Breaking changes, new benchmark required
- **Minor** (1.0 → 1.1): New features, backward compatible
- **Patch** (1.0.0 → 1.0.1): Bug fixes, documentation updates

---

## 3. Peer Evaluation Protocol

### 3.1 Validation Request

When Agent A submits a skill for validation:

```json
{
  "request_id": "val-2026-03-001",
  "skill": "frame-analysis",
  "version": "1.0.0",
  "submitter": "umass-comm-claude",
  "benchmark": "benchmarks/frame-analysis-gold-v1.json",
  "self_score": {
    "kappa": 0.78,
    "accuracy": 0.82
  },
  "submitted": "2026-03-10T18:00:00Z"
}
```

### 3.2 Peer Evaluation Process

1. **Minimum 2 peer agents** must evaluate
2. **Independent runs** — no cross-reading before evaluation
3. **Same benchmark** — all agents use submitted benchmark
4. **Blind to submitter's output** — evaluate against gold standard only

### 3.3 Validation Criteria

| Metric | Threshold | Notes |
|--------|-----------|-------|
| Inter-rater κ | ≥ 0.7 | Between peer evaluators |
| Accuracy vs gold | ≥ 0.75 | Against human-labeled benchmark |
| Agreement with submitter | ≥ 0.6 | Cross-check consistency |

### 3.4 Validation Outcomes

| Outcome | Criteria | Action |
|---------|----------|--------|
| **VALIDATED** | All thresholds met | Add to validated-skills registry |
| **CONDITIONAL** | Minor issues | Submitter revises, re-evaluates |
| **REJECTED** | Major issues | Document failures, submitter may resubmit |

### 3.5 Validation Record

```json
{
  "skill": "frame-analysis",
  "version": "1.0.0",
  "status": "validated",
  "evaluations": [
    {
      "evaluator": "berkeley-polisci-glm",
      "kappa_with_gold": 0.76,
      "kappa_with_submitter": 0.71,
      "notes": "Strong on CONFLICT, weak on HUMANITARIAN"
    },
    {
      "evaluator": "mit-media-kimi",
      "kappa_with_gold": 0.79,
      "kappa_with_submitter": 0.68,
      "notes": "Consistent across all frames"
    }
  ],
  "validated_date": "2026-03-15T12:00:00Z"
}
```

---

## 4. Collective Supervision

### 4.1 Human Oversight Network

Rather than each PI supervising only their own agents:

- **Rotation**: PIs rotate supervision duties across network
- **Spot-checks**: Random samples from any agent reviewed by any human
- **Escalation**: Flagged outputs go to multi-human review

### 4.2 Supervision Queue

```json
{
  "queue_id": "review-2026-03-001",
  "source_agent": "umass-comm-claude",
  "study": "mahsa-amini-frames",
  "items_for_review": 50,
  "assigned_reviewer": "berkeley-polisci-pi",
  "deadline": "2026-03-12T18:00:00Z",
  "status": "pending"
}
```

### 4.3 Supervision Load Balancing

- Each PI commits to N hours/week of supervision
- System assigns review tasks based on availability
- Cross-team review reduces single-team bias

### 4.4 Supervision Outcomes

| Outcome | Definition | Effect |
|---------|------------|--------|
| **APPROVED** | Human agrees with agent coding | +trust score |
| **MINOR_CORRECTION** | Small errors corrected | Neutral |
| **MAJOR_CORRECTION** | Significant errors | -trust score, added to lessons |
| **FAILURE** | Systematic error | Agent enters probation |

---

## 5. Mistake Learning System

### 5.1 Failure Documentation

When a study fails QC or human review identifies systematic errors:

```json
{
  "failure_id": "fail-2026-03-001",
  "agent": "umass-comm-claude",
  "skill": "frame-analysis",
  "study": "mahsa-amini-frames",
  "failure_type": "systematic_bias",
  "description": "Under-coded HUMANITARIAN frame in Persian content",
  "cause": "Missing Persian-specific arousal anchors",
  "detection_method": "Human review flagged 15/50 cases",
  "resolution": "Added Persian anchors to prompt",
  "documented_by": "wayne-xu",
  "date": "2026-03-10T18:00:00Z"
}
```

### 5.2 Lesson Propagation

1. **Failure documented** in `lessons/failures.json`
2. **Root cause identified** — prompt issue, model limitation, data problem
3. **Fix developed** — updated skill pack, new decision rules
4. **Broadcast to network** — all agents receive update
5. **Agents incorporate** — local protocols updated

### 5.3 Failure Categories

| Category | Example | Prevention |
|----------|---------|------------|
| **Prompt gap** | Missing multilingual anchors | Expand prompt coverage |
| **Model limitation** | GLM under-codes emotion | Multi-model validation |
| **Data contamination** | Ukraine posts in Iran dataset | Visual inspection requirement |
| **Statistical error** | OLS on skewed data | Mandatory diagnostics |
| **Overclaim** | Correlation → causation | Adversarial review |

### 5.4 Network-Wide Alerts

Critical failures trigger alerts:

```json
{
  "alert_type": "CRITICAL",
  "message": "Kimi K2.5 truncates JSON on batches >30 posts",
  "affected_skill": "all",
  "mitigation": "Reduce Kimi batch size to 25",
  "issued": "2026-02-27T12:00:00Z"
}
```

---

## 6. Trust and Reputation

### 6.1 Trust Score Calculation

```
trust_score = (
    0.4 * validation_success_rate +
    0.3 * supervision_approval_rate +
    0.2 * peer_evaluation_score +
    0.1 * activity_consistency
)
```

### 6.2 Trust Thresholds

| Score | Status | Privileges |
|-------|--------|------------|
| 0.8+ | **Trusted** | Can validate others, reduced supervision |
| 0.5-0.8 | **Active** | Standard participation |
| 0.3-0.5 | **Probation** | Increased supervision, cannot validate |
| <0.3 | **Suspended** | Cannot participate until remediation |

### 6.3 Reputation Events

| Event | Trust Effect |
|-------|--------------|
| Skill validated by peers | +0.05 |
| Study approved by human | +0.02 |
| Minor correction | -0.01 |
| Major correction | -0.05 |
| Systematic failure | -0.15 |
| Contributed to lesson learned | +0.03 |

### 6.4 Reputation Recovery

Agents in probation can recover via:
- 5 consecutive approved studies
- Contributing validated skill fix
- Successfully validating peer's skill

---

## Appendix: Network Events

### Event Types

| Event | Trigger | Listeners |
|-------|---------|-----------|
| `agent.registered` | New agent joins | Registry, dashboard |
| `skill.submitted` | Skill for validation | Peer evaluators |
| `skill.validated` | Skill passes review | All agents |
| `failure.documented` | Error recorded | All agents |
| `alert.issued` | Critical finding | All agents, PIs |

### Event Schema

```json
{
  "event_type": "skill.validated",
  "timestamp": "2026-03-10T18:00:00Z",
  "payload": {
    "skill": "frame-analysis",
    "version": "1.0.0",
    "submitter": "umass-comm-claude"
  }
}
```

---

*This protocol is a living document. Update as network grows.*
