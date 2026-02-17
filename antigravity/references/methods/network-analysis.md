# Network Analysis

## Probing Questions (ALL REQUIRED)

```
Q1: What are your nodes and edges?
    Must be SPECIFIC:
    ✓ "Nodes = users, edges = mentions"
    ✓ "Nodes = posts, edges = shared URLs"
    ✗ "The network" — NOT A DEFINITION
    ✗ "Connections" — WHAT KIND?

Q2: Directed or undirected? Why?
    ✓ Directed (A→B means something different than B→A)
    ✓ Undirected (connection is symmetric)
    Must justify for YOUR network type

Q3: Theoretical justification?
    ✓ Connected to research question
    ✓ Grounded in theory
    ✗ "It's what you can do" — NOT THEORETICAL

Q4: What does high centrality MEAN?
    ✓ Influence (with caveats)
    ✓ Bridging between communities
    ✓ Attention received
    ✗ "Importance" — IMPORTANCE FOR WHAT?
    ✗ "They're central" — TAUTOLOGY

Q5: How will you handle isolates and boundaries?
    ✓ Remove with justification
    ✓ Keep and report
    ✓ Analyze separately
```

## Centrality Measures

| Measure | Meaning | Use When |
|---------|---------|----------|
| **Degree** | Direct connections | Activity level |
| **Betweenness** | Bridge between groups | Information flow |
| **Eigenvector** | Connected to well-connected | Prestige/influence |
| **PageRank** | Like eigenvector, directed | Citation networks |
| **Closeness** | Average distance to all | Speed of spread |

## Community Detection

| Algorithm | Best For | Deterministic |
|-----------|----------|---------------|
| **Louvain** | Large networks | No |
| **Infomap** | Information flow | No |
| **Label Propagation** | Speed | No |
| **Girvan-Newman** | Small networks | Yes |

## Critical Checks

- [ ] Node/edge definitions explicit
- [ ] Directed/undirected justified
- [ ] Centrality interpretation grounded in theory
- [ ] Isolate handling documented
- [ ] Network boundaries justified
