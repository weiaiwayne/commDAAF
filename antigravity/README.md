# CommDAAF for Google Antigravity

**Computational Communication Research Framework** — Agent Skill for Antigravity

## Quick Install

### Option A: Global Skill (All Projects)

```bash
# Clone to Antigravity global skills
cd ~/.gemini/antigravity/skills
git clone https://github.com/openclaw/commdaaf.git
cd commdaaf && mv antigravity/* . && rm -rf antigravity
```

### Option B: Project Skill (Single Project)

```bash
# In your project root
mkdir -p .agent/skills
cd .agent/skills
git clone https://github.com/openclaw/commdaaf.git
cd commdaaf && mv antigravity/* . && rm -rf antigravity
```

## Directory Structure

```
commdaaf/
├── SKILL.md                    # Main skill definition (with YAML frontmatter)
├── references/
│   ├── methods/
│   │   ├── sentiment-analysis.md
│   │   ├── topic-modeling.md
│   │   ├── network-analysis.md
│   │   ├── coordinated-behavior.md
│   │   ├── frame-analysis.md
│   │   ├── content-analysis.md
│   │   └── llm-annotation.md
│   └── data-sources/
│       └── README.md           # Post-API era data access guide
└── scripts/
    └── zotero_adapt.py         # Optional: customize based on your library
```

## How It Works

Antigravity's agent automatically loads CommDAAF when you mention:
- Sentiment analysis, topic modeling, frame analysis
- Network analysis, coordinated behavior detection
- Social media research, platform data collection
- Content analysis, LLM annotation

The skill enforces:
- **Probing questions** before any analysis
- **Explicit parameter choices** (no silent defaults)
- **Honest data access guidance** (post-API era reality)
- **Validation requirements** for all automated methods

## Usage Examples

```
User: Analyze sentiment in climate tweets

Agent: Before I proceed with sentiment analysis, I need to clarify:
       1. What exactly do you mean by 'sentiment'? (Valence? Emotions? Stance?)
       2. What's your unit of analysis? (Post? User? Time period?)
       3. What approach do you prefer and why? (VADER? LLM?)
       4. How will you handle neutral content?
       5. What's your sarcasm strategy? (Climate = high sarcasm domain)
       6. What's your validation plan?
```

```
User: I need Twitter data for my research

Agent: I need to be honest about Twitter/X data access in 2026:
       
       💰 Twitter API costs $5,000+/month minimum.
       
       Alternatives:
       - Existing datasets (Harvard Dataverse, ICPSR) — FREE
       - Bluesky — Open API, growing community
       - Pre-2023 Twitter archives
       
       What's your budget and timeline?
```

## Optional: Zotero Customization

Customize CommDAAF based on your research library:

```bash
pip install pyzotero

# Get your Zotero user ID from: https://www.zotero.org/settings/keys
python scripts/zotero_adapt.py --user-id YOUR_ID --api-key YOUR_KEY
```

This analyzes your library and generates recommendations based on your methods and domains.

## Verification

After installation, test with:

```
Run topic modeling on my dataset
```

If working correctly, the agent should ask probing questions about:
- Why topic modeling specifically?
- How many topics (K) and why?
- What preprocessing?

If it just runs with defaults → skill not loaded correctly.

## Version

- Name: CommDAAF
- Version: 0.2.0
- Based on: DAAF (Data Analyst Augmentation Framework)
- Platforms: Google Antigravity, OpenClaw, Claude Code
