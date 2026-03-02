# Zotero Adapter

**Auto-customize skills based on your research library.**

## What It Does

The Zotero Adapter reads your reference library and generates domain-specific skills based on:
- **Methods** you frequently use (network analysis, topic modeling, etc.)
- **Theories** you engage with (attention economy, framing, etc.)
- **Platforms** you study (Twitter, Reddit, Telegram, etc.)
- **Topics** you research (misinformation, polarization, etc.)

## Quick Start

### 1. Get Your Zotero Credentials

1. Go to [zotero.org/settings/keys](https://www.zotero.org/settings/keys)
2. Create a new API key with read access
3. Note your User ID (shown on the same page)

### 2. Install Requirements

```bash
pip install pyzotero
```

### 3. Run the Adapter

```bash
# One-step: analyze + generate
python adapt.py --user-id YOUR_USER_ID --api-key YOUR_API_KEY

# Or step-by-step:
python extractor.py --user-id YOUR_USER_ID --api-key YOUR_API_KEY --output analysis
python generator.py --analysis analysis.json --output-dir ./generated/
```

### 4. Review & Install

```bash
# Review what was generated
cat generated/README.md

# Copy to your skills
cp -r generated/* ~/.openclaw/workspace/skills/comm-research/
```

## Files

| File | Description |
|------|-------------|
| `adapt.py` | One-step analysis + generation |
| `extractor.py` | Fetch and analyze Zotero library |
| `generator.py` | Generate customized skill files |

## Output Structure

```
generated/
├── README.md           # Your research profile
├── config.json         # Customized priorities
├── methods/
│   ├── network-analysis.md
│   ├── coordinated-behavior.md
│   └── llm-annotation.md
└── theories/
    ├── attention-economy.md
    └── artificial-sociality.md
```

## How Detection Works

The adapter scans your paper titles, abstracts, and tags for patterns:

**Methods:** network analysis, topic modeling, sentiment analysis, LLM annotation, coordinated behavior detection, etc.

**Theories:** attention economy, networked publics, framing, agenda setting, diffusion, etc.

**Platforms:** Twitter, Reddit, Telegram, YouTube, TikTok, etc.

**Topics:** misinformation, polarization, health communication, political communication, etc.

## Customization

Generated files are starting points. Edit them to:
- Add specific citations from your library
- Adjust method parameters for your use cases
- Add notes based on your experience
- Integrate with your existing workflows

## Privacy

The adapter:
- Only reads metadata (titles, abstracts, tags)
- Does not upload anything
- Processes locally
- Does not store your API key

## Example Output

From a library focused on coordinated behavior research:

```markdown
## Your Research Profile

### Top Methods
- Network Analysis (12 papers)
- Coordinated Behavior (8 papers)
- LLM Annotation (5 papers)

### Top Platforms
- Telegram (9 papers)
- Twitter (7 papers)
- Reddit (4 papers)

### Recommended Skills
- methods/coordinated-behavior.md (HIGH priority)
- methods/network-analysis.md (HIGH priority)
- data-sources/telegram.md (recommended)
```

## Troubleshooting

**"pyzotero not installed"**
```bash
pip install pyzotero
```

**"API key invalid"**
- Check key has read permissions
- Verify user ID is correct (not username)

**"No items found"**
- Check library isn't empty
- Try with `--limit 100` to test

---

*Part of the Communication Research Skill for OpenClaw*
