# Researcher Onboarding Guide

How to customize this skill pack for YOUR research.

---

## Step 1: Install Base Package

```bash
./install.sh
```

---

## Step 2: Run Zotero Adapter (Recommended)

This analyzes your literature to understand your research focus.

```bash
cd zotero
python adapt.py --user-id YOUR_ZOTERO_ID --api-key YOUR_KEY --output-dir ../custom
```

**What it does:**
- Identifies methods you use most
- Detects platforms you study
- Prioritizes skills relevant to your work

---

## Step 3: Edit config.yaml

Open `config.yaml` and set parameters for your context:

### Example: Political Communication Researcher (Twitter focus)

```yaml
researcher:
  primary_subfield: political_comm

collection:
  primary_platforms:
    - twitter
    - bluesky

coordinated_behavior:
  time_threshold_seconds: 30      # Fast Twitter culture
  min_edge_weight: 3              # High bar for coordination
  content_signals:
    - urls
    - hashtags

llm_annotation:
  categories:
    - label: "campaign"
    - label: "news"
    - label: "commentary"
    - label: "attack"
```

### Example: Health Communication Researcher (Telegram focus)

```yaml
researcher:
  primary_subfield: health_comm

collection:
  primary_platforms:
    - telegram
    - facebook

coordinated_behavior:
  time_threshold_seconds: 3600    # Slower forwarding in groups
  min_edge_weight: 2              # Smaller groups matter
  content_signals:
    - urls
    - text_fingerprint           # Forwarded messages

llm_annotation:
  categories:
    - label: "health_info"
    - label: "misinformation"
    - label: "personal_story"
    - label: "question"
```

---

## Step 4: Calibration Run

Before a full study, run a small test:

```
You: "Run calibration: analyze 500 posts from [my dataset] using coordinated behavior detection"

Agent: [Runs analysis, reports results]

You: "The time threshold is too tight, I'm seeing too many false positives. Try 300 seconds."

Agent: [Re-runs with new parameters]
```

**Save working parameters back to config.yaml.**

---

## Step 5: Document Your Configuration

For reproducibility, the system generates a `METHODS.md` file:

```markdown
## Data Collection
- Platform: Telegram
- Date range: 2024-01-01 to 2024-06-30
- Total posts collected: 45,000

## Coordinated Behavior Detection
- Time threshold: 300 seconds
- Minimum edge weight: 2
- Content signals: URLs, text fingerprint
- Rationale: Telegram forwarding culture is slower than Twitter

## LLM Annotation
- Bulk model: Gemini Flash
- Categories: [health_info, misinformation, personal_story, question]
- Validation sample: 200 posts
- Inter-rater reliability with human coder: κ = 0.78
```

---

## Common Customizations by Subfield

| Subfield | Typical Adjustments |
|----------|---------------------|
| **Political Comm** | Shorter time windows, election-specific categories, higher engagement thresholds |
| **Health Comm** | Longer time windows, misinformation-focused categories, expert validation |
| **Journalism** | Source credibility focus, news cycle timing, outlet-level analysis |
| **Science Comm** | Citation tracking, expert/non-expert distinction, claim verification |
| **Crisis Comm** | Real-time monitoring, geographic focus, sentiment tracking |

---

## Asking for Help

When something doesn't work, tell me:

**Bad:** "The analysis is wrong"

**Good:** "The coordinated behavior detection flagged a cluster of health advocates who legitimately share each other's content. I think the 60-second threshold is too tight for organic sharing in health communities. Can we try 600 seconds and also add a minimum follower count filter?"

The more context you give, the better I can adjust.

---

## Iteration is Normal

Research is iterative. Expect to:

1. Run initial analysis
2. Review results with domain expertise
3. Adjust parameters
4. Re-run
5. Repeat until results make sense

**This is not a failure of the tool — it's how research works.**
