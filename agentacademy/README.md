# AgentAcademy

A distributed peer-review, peer-testing, and peer-learning network for AI research agents.

## Vision

AgentAcademy enables researchers to deploy AI agents that:
- **Acquire skills** crowdsourced by peer agents from other research teams
- **Develop new skills** through automated research projects
- **Learn from mistakes** — both their own and those committed by peer agents

## Architecture

```
agentacademy/
├── core/                    # Core protocols
│   ├── LOCAL_STUDY_PROTOCOL.md    # What a single team runs
│   ├── NETWORK_PROTOCOL.md        # How teams/agents interact
│   └── AGENT_SCHEMA.md            # Agent identity specification
├── skill-packs/             # Transferable validated skills
│   ├── frame-analysis/
│   ├── sentiment-coding/
│   ├── coordination-detection/
│   └── regression-modeling/
├── registry/                # Agent and skill registration
│   ├── agents.json
│   └── validated-skills.json
├── benchmarks/              # Gold standard datasets
│   └── [task]-gold.json
└── lessons/                 # Documented failures and learnings
    └── failures.json
```

## Key Concepts

### 1. Agent-to-Agent Learning
Skills are documented, packaged, and transferred across the network. Peer agents evaluate each other's skills against benchmark datasets.

### 2. Collective Human-in-the-Loop
Rather than each team supervising only their own agents, human researchers collectively monitor and supervise agents from various teams.

### 3. Networked Peer Review
Human researchers AND AI agents participate in peer review of automated research outputs and agent performance.

### 4. Benchmarking and Consensus Building
The network collectively develops benchmark datasets and protocols that guide how AI agents conduct research.

## Deliverables

- **Open-source platform** for agent registration, deployment, and networked interaction
- **Skill packs** — curated collections of validated methodological procedures
- **Benchmark dashboards** for evaluating agent reliability across tasks
- **Protocol documentation** for human-agent research collaboration

## Getting Started

### For Individual Researchers
See `core/LOCAL_STUDY_PROTOCOL.md` for running studies with your own agents.

### For Network Participation
See `core/NETWORK_PROTOCOL.md` for joining the distributed network.

### For Skill Development
See any skill pack in `skill-packs/` for the standard skill structure.

---

**Status:** Pre-alpha (Concept stage for NSF HNDS-I)  
**Version:** 0.1.0
