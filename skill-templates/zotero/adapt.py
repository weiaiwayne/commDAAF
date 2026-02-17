#!/usr/bin/env python3
"""
Zotero Adapter - One-Step Library Analysis & Skill Generation

Combines extraction and generation into a single workflow.
Connects to your Zotero library and generates customized skills.

Usage:
    python adapt.py --user-id YOUR_USER_ID --api-key YOUR_API_KEY

Example:
    python adapt.py --user-id 6345227 --api-key Abc123xyz --output-dir ./my-skills/

This will:
1. Fetch your Zotero library
2. Analyze methods, theories, and platforms
3. Generate customized skill files
4. Output a README with your research profile

Requirements:
    pip install pyzotero
"""

import sys
import argparse
from pathlib import Path

from extractor import ZoteroExtractor
from generator import SkillGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Analyze Zotero library and generate customized skills'
    )
    parser.add_argument('--user-id', required=True, help='Zotero user ID')
    parser.add_argument('--api-key', required=True, help='Zotero API key')
    parser.add_argument('--output-dir', '-o', default='./generated',
                       help='Output directory for generated skills')
    parser.add_argument('--limit', type=int, help='Limit number of items to fetch')
    parser.add_argument('--keep-analysis', action='store_true',
                       help='Keep intermediate analysis files')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("ZOTERO ADAPTER - Communication Research Skill")
    print("=" * 60)
    
    # Step 1: Extract
    print("\n📚 Step 1: Fetching Zotero library...")
    extractor = ZoteroExtractor(args.user_id, args.api_key)
    extractor.fetch_library(limit=args.limit)
    
    # Step 2: Analyze
    print("\n🔍 Step 2: Analyzing library...")
    analysis = extractor.analyze_library()
    
    # Save intermediate files if requested
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    if args.keep_analysis:
        extractor.export_json(str(output_path / 'analysis.json'))
        extractor.export_markdown(str(output_path / 'analysis.md'))
    
    # Step 3: Generate
    print("\n⚙️  Step 3: Generating customized skills...")
    
    # Convert analysis to dict format expected by generator
    from dataclasses import asdict
    analysis_dict = asdict(analysis)
    
    generator = SkillGenerator(analysis_dict)
    files = generator.generate_all(args.output_dir)
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ DONE!")
    print("=" * 60)
    
    print(f"\n📊 Library Analysis:")
    print(f"   - Total items: {analysis.total_items}")
    print(f"   - Methods detected: {len(analysis.methods)}")
    print(f"   - Theories detected: {len(analysis.theories)}")
    print(f"   - Platforms detected: {len(analysis.platforms)}")
    
    print(f"\n📁 Generated {len(files)} files in: {args.output_dir}")
    
    print("\n🚀 Next steps:")
    print(f"   1. Review generated files in {args.output_dir}")
    print(f"   2. Add specific citations from your library")
    print(f"   3. Copy to your skill directory:")
    print(f"      cp -r {args.output_dir}/* ~/.openclaw/workspace/skills/comm-research/")
    
    print("\n")


if __name__ == '__main__':
    main()
