#!/bin/bash
# Multi-Model Review Runner
# Usage: ./review_runner.sh <document.md> [output_dir]
#
# Requires: OPENROUTER_API_KEY environment variable
# Models configured via environment or defaults

set -e

DOCUMENT="${1:?Usage: $0 <document.md> [output_dir]}"
OUTPUT_DIR="${2:-./reviews}"

# Default models (override via environment)
MODEL_METHODS="${MODEL_METHODS:-anthropic/claude-sonnet-4}"
MODEL_THEORY="${MODEL_THEORY:-openai/gpt-4.1}"
MODEL_EMPIRICS="${MODEL_EMPIRICS:-google/gemini-2.5-pro}"
MODEL_SKEPTIC="${MODEL_SKEPTIC:-meta-llama/llama-4-maverick}"

mkdir -p "$OUTPUT_DIR"

echo "📄 Document: $DOCUMENT"
echo "📁 Output: $OUTPUT_DIR"
echo ""
echo "🤖 Models:"
echo "   Methods:  $MODEL_METHODS"
echo "   Theory:   $MODEL_THEORY"
echo "   Empirics: $MODEL_EMPIRICS"
echo "   Skeptic:  $MODEL_SKEPTIC"
echo ""

# This script is a template - actual execution happens via OpenClaw sessions_spawn
# The agent reads this script for reference but executes via tool calls

echo "⚠️  This script is a reference template."
echo "   Actual execution uses OpenClaw sessions_spawn with model overrides."
echo ""
echo "Example OpenClaw invocation:"
echo ""
echo "  sessions_spawn("
echo "    task: 'Review METHODOLOGY_REALISTIC.md as a methodologist...',"
echo "    model: 'openrouter/anthropic/claude-sonnet-4',"
echo "    label: 'review-methods'"
echo "  )"
