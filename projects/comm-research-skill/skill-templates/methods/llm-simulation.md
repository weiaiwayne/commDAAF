# LLM-Powered Agent-Based Simulation

Simulating social dynamics using LLM agents.

⚠️ **EXPERIMENTAL** — Validation is the "central challenge." Use for exploration, not definitive claims.

---

## Overview

LLM-powered agent-based simulation uses Large Language Models as the "brain" of simulated agents, replacing rule-based decision-making with natural language reasoning.

**Promise:** More realistic, nuanced agent behavior than traditional ABMs
**Challenge:** Validating that simulated behavior matches reality

---

## When to Use LLM Simulation

✅ **Appropriate:**
- Exploring theoretical mechanisms
- Generating hypotheses for empirical testing
- Studying scenarios impossible to observe (counterfactuals)
- Understanding potential dynamics before field studies
- Educational demonstrations

❌ **Not Appropriate:**
- Making empirical claims about real populations
- Policy decisions without empirical validation
- Definitive conclusions about human behavior
- When real observational data is available

---

## Probing Questions (REQUIRED)

```
Q1: What is the purpose of your simulation?
    ✓ Hypothesis generation
    ✓ Theoretical exploration
    ✓ Mechanism testing
    ✗ "Proving" something about reality — SIMULATIONS DON'T PROVE

Q2: How will you validate agent behavior?
    ✓ Compare to empirical distributions
    ✓ Domain expert review
    ✓ Sensitivity analysis
    ✗ "LLM is realistic enough" — VALIDATION REQUIRED

Q3: What claims will you make from simulation results?
    ✓ "Under these assumptions, X could occur"
    ✓ "This mechanism could explain Y"
    ✗ "People do X" — CANNOT CONCLUDE FROM SIMULATION

Q4: How do you justify your persona designs?
    ✓ Based on empirical research
    ✓ Grounded in theory
    ✓ Sensitivity tested
    ✗ "Made them up" — PERSONAS SHAPE RESULTS
```

---

## Architecture

### Basic LLM Agent

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

@dataclass
class LLMAgent:
    """An agent powered by an LLM for social simulation."""
    
    agent_id: str
    persona: str
    model: str = "gpt-4o-mini"  # Cost-effective for many agents
    memory: List[dict] = field(default_factory=list)
    memory_limit: int = 20
    
    def perceive(self, observation: dict):
        """Store observation in memory."""
        self.memory.append({
            'type': 'observation',
            'content': observation,
            'step': len(self.memory)
        })
        
        # Trim old memories
        if len(self.memory) > self.memory_limit:
            self.memory = self.memory[-self.memory_limit:]
    
    def decide(self, options: List[str], context: str = "") -> dict:
        """
        Make a decision based on persona, memory, and options.
        
        Returns: {'choice': str, 'reasoning': str}
        """
        memory_summary = self._summarize_memory()
        
        prompt = f"""You are: {self.persona}

Recent events you remember:
{memory_summary}

Current situation: {context}

Available actions:
{chr(10).join([f"- {opt}" for opt in options])}

Based on your persona and what you know, what do you do?

Respond in JSON format:
{{"choice": "your chosen action", "reasoning": "brief explanation"}}"""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        
        # Log decision
        self.memory.append({
            'type': 'decision',
            'choice': result['choice'],
            'reasoning': result['reasoning']
        })
        
        return result
    
    def generate_content(self, context: str, content_type: str = "post") -> str:
        """Generate content (e.g., social media post) from agent's perspective."""
        
        prompt = f"""You are: {self.persona}

Context: {context}

Write a {content_type} from your perspective. Stay in character.
Be natural and realistic. Output ONLY the {content_type}, nothing else."""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9
        )
        
        return response.choices[0].message.content.strip()
    
    def _summarize_memory(self) -> str:
        """Create a summary of recent memory."""
        if not self.memory:
            return "Nothing notable has happened yet."
        
        recent = self.memory[-10:]
        summary_parts = []
        
        for mem in recent:
            if mem['type'] == 'observation':
                summary_parts.append(f"- Observed: {mem['content']}")
            elif mem['type'] == 'decision':
                summary_parts.append(f"- Decided to: {mem['choice']}")
        
        return "\n".join(summary_parts)
```

### Simulation Environment

```python
@dataclass
class SimulationEnvironment:
    """Environment for multi-agent simulation."""
    
    agents: List[LLMAgent]
    state: dict = field(default_factory=dict)
    history: List[dict] = field(default_factory=list)
    step_count: int = 0
    
    def broadcast(self, message: dict):
        """Send observation to all agents."""
        for agent in self.agents:
            agent.perceive(message)
    
    def step(self, scenario: str) -> List[dict]:
        """
        Run one simulation step.
        
        Each agent observes, decides, and acts.
        """
        self.step_count += 1
        step_results = []
        
        # Each agent takes action
        for agent in self.agents:
            # Agent decides
            decision = agent.decide(
                options=self._get_available_actions(agent),
                context=scenario
            )
            
            # Record result
            result = {
                'step': self.step_count,
                'agent_id': agent.agent_id,
                'action': decision['choice'],
                'reasoning': decision['reasoning']
            }
            step_results.append(result)
            
            # Update environment state
            self._apply_action(agent, decision['choice'])
        
        # Broadcast results to all agents
        self.broadcast({
            'step': self.step_count,
            'actions': step_results
        })
        
        self.history.extend(step_results)
        return step_results
    
    def _get_available_actions(self, agent: LLMAgent) -> List[str]:
        """Define available actions (customize per simulation)."""
        return [
            "Post supportive content",
            "Post critical content",
            "Share someone else's post",
            "Stay silent",
            "Engage in discussion"
        ]
    
    def _apply_action(self, agent: LLMAgent, action: str):
        """Apply action effects to environment (customize per simulation)."""
        if action not in self.state:
            self.state[action] = 0
        self.state[action] += 1
```

---

## Example: Opinion Dynamics Simulation

```python
def run_opinion_simulation(
    topic: str,
    personas: List[dict],
    n_steps: int = 20,
    events: List[dict] = None
) -> dict:
    """
    Simulate opinion dynamics around a topic.
    
    personas: [{"id": str, "description": str, "initial_stance": str}]
    events: [{"step": int, "description": str}] - External events to inject
    """
    
    # Create agents
    agents = []
    for p in personas:
        agent = LLMAgent(
            agent_id=p['id'],
            persona=f"{p['description']}. Initial stance on {topic}: {p['initial_stance']}"
        )
        agents.append(agent)
    
    env = SimulationEnvironment(agents=agents)
    
    # Run simulation
    for step in range(n_steps):
        # Check for external events
        scenario = f"Discussion about {topic} continues."
        if events:
            for event in events:
                if event['step'] == step:
                    scenario = event['description']
        
        # Run step
        results = env.step(scenario)
        
        print(f"Step {step + 1}:")
        for r in results:
            print(f"  {r['agent_id']}: {r['action']}")
    
    return {
        'history': env.history,
        'final_state': env.state,
        'n_steps': n_steps,
        'n_agents': len(agents)
    }

# Example usage
personas = [
    {
        "id": "activist",
        "description": "Environmental activist, passionate about climate action",
        "initial_stance": "Strongly pro-climate policy"
    },
    {
        "id": "skeptic", 
        "description": "Small business owner concerned about economic impacts",
        "initial_stance": "Skeptical of aggressive climate regulations"
    },
    {
        "id": "moderate",
        "description": "Parent trying to balance environment and economy",
        "initial_stance": "Open to solutions that work for everyone"
    },
    {
        "id": "scientist",
        "description": "Climate researcher who values evidence-based discussion",
        "initial_stance": "Supports policy based on scientific consensus"
    }
]

events = [
    {"step": 5, "description": "Breaking: New study shows faster ice melt than predicted"},
    {"step": 10, "description": "Major employer announces layoffs citing climate regulations"},
    {"step": 15, "description": "Local flooding affects many community members"}
]

results = run_opinion_simulation(
    topic="local climate policy",
    personas=personas,
    n_steps=20,
    events=events
)
```

---

## Example: Misinformation Spread Simulation

```python
def run_misinfo_simulation(
    claim: str,
    fact_check: str,
    agent_types: dict,  # {"type": n_agents}
    n_steps: int = 30
) -> dict:
    """
    Simulate how misinformation spreads and how corrections propagate.
    """
    
    agent_personas = {
        "believer": "Someone inclined to believe sensational claims without verification",
        "skeptic": "Critical thinker who verifies claims before sharing",
        "amplifier": "Highly active user who shares content frequently",
        "corrector": "Person who actively counters misinformation with facts",
        "passive": "Lurker who rarely posts but observes everything"
    }
    
    agents = []
    for agent_type, count in agent_types.items():
        for i in range(count):
            agents.append(LLMAgent(
                agent_id=f"{agent_type}_{i}",
                persona=agent_personas[agent_type]
            ))
    
    env = SimulationEnvironment(agents=agents)
    
    # Initialize with misinformation
    env.broadcast({
        'type': 'new_claim',
        'content': claim,
        'source': 'viral_post'
    })
    
    # Run simulation
    for step in range(n_steps):
        scenario = "You see the ongoing discussion about this claim in your feed."
        
        # Inject fact-check at step 10
        if step == 10:
            env.broadcast({
                'type': 'fact_check',
                'content': fact_check,
                'source': 'official_factchecker'
            })
            scenario = "A fact-check has been published about the viral claim."
        
        results = env.step(scenario)
    
    # Analyze results
    action_counts = {}
    for entry in env.history:
        action = entry['action']
        if action not in action_counts:
            action_counts[action] = 0
        action_counts[action] += 1
    
    return {
        'history': env.history,
        'action_distribution': action_counts,
        'spread_pattern': analyze_spread_pattern(env.history)
    }

def analyze_spread_pattern(history: List[dict]) -> dict:
    """Analyze how content spread over time."""
    
    shares_over_time = {}
    corrections_over_time = {}
    
    for entry in history:
        step = entry['step']
        action = entry['action'].lower()
        
        if 'share' in action:
            shares_over_time[step] = shares_over_time.get(step, 0) + 1
        if 'correct' in action or 'fact' in action:
            corrections_over_time[step] = corrections_over_time.get(step, 0) + 1
    
    return {
        'shares_by_step': shares_over_time,
        'corrections_by_step': corrections_over_time
    }
```

---

## Scaling: LLM Archetypes

For large-scale simulations (thousands+ agents), use **archetypes** instead of individual LLM calls:

```python
class ArchetypeBasedSimulation:
    """
    Use pre-computed archetype responses for efficiency.
    Based on MIT Media Lab approach (2025).
    """
    
    def __init__(self, archetypes: List[dict]):
        """
        archetypes: [
            {
                "name": "skeptic",
                "description": "...",
                "response_patterns": {
                    "new_claim": ["verify", "ignore", "question"],
                    "fact_check": ["accept", "share_correction", "dismiss"],
                    ...
                },
                "response_weights": {
                    "new_claim": [0.3, 0.5, 0.2],
                    ...
                }
            }
        ]
        """
        self.archetypes = {a['name']: a for a in archetypes}
    
    def precompute_responses(self, scenarios: List[str], model: str = "gpt-4o"):
        """
        Pre-compute archetype responses to common scenarios.
        Do this ONCE, then reuse for many simulation runs.
        """
        for archetype_name, archetype in self.archetypes.items():
            for scenario in scenarios:
                if scenario not in archetype.get('response_patterns', {}):
                    # Generate response distribution for this archetype
                    responses = self._generate_archetype_responses(
                        archetype['description'],
                        scenario,
                        model
                    )
                    archetype['response_patterns'][scenario] = responses
    
    def get_agent_action(self, archetype_name: str, scenario: str) -> str:
        """
        Get action for agent based on archetype probability distribution.
        No LLM call needed — uses pre-computed patterns.
        """
        archetype = self.archetypes[archetype_name]
        
        if scenario in archetype['response_patterns']:
            patterns = archetype['response_patterns'][scenario]
            weights = archetype.get('response_weights', {}).get(
                scenario, 
                [1/len(patterns)] * len(patterns)
            )
            return random.choices(patterns, weights=weights)[0]
        else:
            # Fallback to default behavior
            return random.choice(["observe", "ignore"])
```

---

## Validation Framework

### 1. Behavioral Validation

```python
def validate_agent_behavior(
    simulated_actions: List[dict],
    empirical_distribution: dict
) -> dict:
    """
    Compare simulated action distribution to empirical data.
    """
    
    # Get simulated distribution
    sim_counts = {}
    for action in simulated_actions:
        a = action['action']
        sim_counts[a] = sim_counts.get(a, 0) + 1
    
    total = sum(sim_counts.values())
    sim_dist = {k: v/total for k, v in sim_counts.items()}
    
    # Compare to empirical
    from scipy.stats import wasserstein_distance
    
    # Align categories
    all_actions = set(sim_dist.keys()) | set(empirical_distribution.keys())
    
    sim_vec = [sim_dist.get(a, 0) for a in sorted(all_actions)]
    emp_vec = [empirical_distribution.get(a, 0) for a in sorted(all_actions)]
    
    distance = wasserstein_distance(sim_vec, emp_vec)
    
    return {
        'simulated_distribution': sim_dist,
        'empirical_distribution': empirical_distribution,
        'wasserstein_distance': distance,
        'interpretation': 'lower is better, < 0.1 is good'
    }
```

### 2. Sensitivity Analysis

```python
def sensitivity_analysis(
    simulation_fn,
    base_params: dict,
    param_variations: dict,
    n_runs: int = 10
) -> dict:
    """
    Test how sensitive results are to parameter changes.
    """
    
    results = {'base': [], 'variations': {}}
    
    # Run base simulation multiple times
    for _ in range(n_runs):
        results['base'].append(simulation_fn(**base_params))
    
    # Vary each parameter
    for param, values in param_variations.items():
        results['variations'][param] = {}
        
        for value in values:
            varied_params = base_params.copy()
            varied_params[param] = value
            
            runs = []
            for _ in range(n_runs):
                runs.append(simulation_fn(**varied_params))
            
            results['variations'][param][value] = runs
    
    return results
```

### 3. Face Validity

```yaml
face_validity_checklist:
  - [ ] Domain expert reviewed persona designs
  - [ ] Agent behaviors seem plausible
  - [ ] No obvious absurdities in simulation output
  - [ ] Results align with theoretical expectations
  - [ ] Surprising results have potential explanations
```

---

## Reporting Requirements

```yaml
publication_requirements:
  methods_section:
    - LLM model and version used
    - Persona descriptions (full text in appendix)
    - Environment/action specifications
    - Number of agents and steps
    - Temperature and other parameters
    
  validation_section:
    - Behavioral validation results
    - Sensitivity analysis results
    - Face validity assessment
    
  limitations_section:
    - "Results reflect LLM behavior, not real humans"
    - "Findings are exploratory, not confirmatory"
    - "Personas are simplifications"
    - Specific limitations of your simulation
    
  appendix:
    - Full prompt templates
    - Complete persona descriptions
    - Simulation code or link to repository
```

---

## Known Limitations

```yaml
critical_limitations:
  epistemic:
    - LLMs trained on text, not human behavior
    - Personas are researcher constructs
    - "Reasoning" may not match human cognition
    
  technical:
    - Expensive at scale (many LLM calls)
    - Non-deterministic (hard to replicate exactly)
    - Sensitive to prompt wording
    
  validation:
    - No ground truth for simulated behavior
    - Empirical validation is expensive
    - Face validity is subjective
    
  scope:
    - Cannot prove claims about reality
    - Cannot replace empirical research
    - Results contingent on assumptions
```

---

## Key Citations

```bibtex
@article{Gao2024,
  title={Large language models empowered agent-based modeling and simulation: 
         a survey and perspectives},
  author={Gao, Chen and others},
  journal={Humanities and Social Sciences Communications},
  year={2024}
}

@article{MITArchetypes2025,
  title={Scaling LLM-Guided Agent Simulations to Millions},
  author={MIT Media Lab},
  booktitle={AAMAS},
  year={2025}
}

@article{ValidationChallenge2025,
  title={Validation is the central challenge for generative social simulation},
  author={Guo and others},
  journal={Artificial Intelligence Review},
  year={2025}
}
```

---

*LLM simulation is a tool for exploration, not confirmation. Validate extensively and claim carefully.*
