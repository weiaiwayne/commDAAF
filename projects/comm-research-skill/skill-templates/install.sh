#!/bin/bash
#
# Communication Research Skill Installer
#
# Installs the skill to your OpenClaw workspace.
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/.../install.sh | bash
#   # or
#   ./install.sh [--workspace /path/to/workspace]
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Defaults
WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"
SKILL_NAME="comm-research"

# Parse args
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --workspace) WORKSPACE="$2"; shift ;;
        --help) 
            echo "Usage: $0 [--workspace /path/to/workspace]"
            exit 0
            ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

SKILL_DIR="$WORKSPACE/skills/$SKILL_NAME"

echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Communication Research Skill Installer                  ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check workspace exists
if [ ! -d "$WORKSPACE" ]; then
    echo -e "${YELLOW}Creating workspace: $WORKSPACE${NC}"
    mkdir -p "$WORKSPACE"
fi

# Create skill directory
echo -e "${GREEN}Installing to: $SKILL_DIR${NC}"
mkdir -p "$SKILL_DIR"

# Get script directory (where we're installing from)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Copy files
echo "Copying skill files..."
cp -r "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/"
cp -r "$SCRIPT_DIR/agents" "$SKILL_DIR/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/data-sources" "$SKILL_DIR/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/methods" "$SKILL_DIR/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/workflows" "$SKILL_DIR/" 2>/dev/null || true
cp -r "$SCRIPT_DIR/zotero" "$SKILL_DIR/" 2>/dev/null || true

# Create requirements file
echo "Creating requirements.txt..."
cat > "$SKILL_DIR/requirements.txt" << 'EOF'
# Communication Research Skill Dependencies

# Data collection
praw>=7.7.0          # Reddit API
google-api-python-client>=2.100.0  # YouTube API
telethon>=1.30.0     # Telegram API
atproto>=0.0.30      # Bluesky AT Protocol
mediacloud>=4.0.0    # News media API

# Analysis
networkx>=3.0        # Network analysis
python-igraph>=0.10  # Fast graph algorithms
pandas>=2.0          # Data manipulation
numpy>=1.24          # Numerical computing

# NLP
bertopic>=0.15       # Topic modeling
sentence-transformers>=2.2  # Embeddings

# Zotero integration
pyzotero>=1.5.0      # Zotero API

# Utilities
tqdm>=4.65           # Progress bars
python-dotenv>=1.0   # Environment variables
EOF

# Check for Python
if command -v python3 &> /dev/null; then
    echo ""
    echo -e "${YELLOW}Install Python dependencies?${NC}"
    echo "  pip install -r $SKILL_DIR/requirements.txt"
    echo ""
    read -p "Install now? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        pip install -r "$SKILL_DIR/requirements.txt"
    fi
fi

echo ""
echo -e "${GREEN}✅ Installation complete!${NC}"
echo ""
echo "Skill installed to: $SKILL_DIR"
echo ""
echo "Next steps:"
echo "  1. Add API credentials to OpenClaw config"
echo "  2. (Optional) Run Zotero adapter to customize:"
echo "     cd $SKILL_DIR/zotero"
echo "     python adapt.py --user-id YOUR_ID --api-key YOUR_KEY"
echo ""
echo "Usage:"
echo "  'Analyze coordinated behavior on Telegram about [topic]'"
echo "  'Research [phenomenon] on Reddit'"
echo "  'Run topic modeling on [dataset]'"
echo ""
