#!/usr/bin/env python3
"""
Search Term Validation Pipeline for VibePoll-2026

CommDAAF v1.0 Requirement: Validate that all search terms are REALISTIC
- Would a real person type this into Google?
- Does the term have actual search volume?
- Does it show temporal variation (not flat)?

Rate Limiting Strategy:
- Google Trends API (via pytrends): ~10 requests/minute safe
- 2-5 second delays between requests
- Exponential backoff on 429 errors
- Max 5 terms per request (API hard limit)
"""

import json
import time
import random
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

from pytrends.request import TrendReq
import pandas as pd

# Configuration
PROJECT_ROOT = Path("/root/.openclaw/workspace/projects/vibe-polling")
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"
OUTPUT_DIR = PROJECT_ROOT / "agents" / "claude-code"

# Rate limiting
MIN_DELAY = 3  # seconds between requests
MAX_DELAY = 6
BACKOFF_MULTIPLIER = 2
MAX_RETRIES = 3

# Validation thresholds
MIN_VOLUME_THRESHOLD = 5  # Minimum average volume (0-100 scale)
MIN_VARIANCE_THRESHOLD = 10  # Minimum variance (to ensure not flat)
ZERO_RATIO_THRESHOLD = 0.7  # Max ratio of zeros allowed


class SearchTermValidator:
    """Validates Google Trends search terms for realistic usage."""

    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=300)  # EST
        self.results: Dict[str, Dict] = {}
        self.errors: List[str] = []

    def _delay(self, attempt: int = 0):
        """Rate limiting with exponential backoff."""
        base_delay = random.uniform(MIN_DELAY, MAX_DELAY)
        delay = base_delay * (BACKOFF_MULTIPLIER ** attempt)
        time.sleep(delay)

    def validate_term(self, term: str, geo: str = 'US',
                      timeframe: str = 'today 3-m') -> Dict:
        """
        Validate a single search term.

        Returns dict with:
        - term: the search term
        - valid: bool
        - avg_volume: float (0-100)
        - variance: float
        - zero_ratio: float (0-1)
        - status: 'PASS' | 'LOW_VOLUME' | 'FLAT' | 'TOO_MANY_ZEROS' | 'ERROR'
        - recommendation: str
        - related_queries: list (for finding better alternatives)
        """
        result = {
            'term': term,
            'valid': False,
            'avg_volume': 0,
            'variance': 0,
            'zero_ratio': 1.0,
            'status': 'PENDING',
            'recommendation': '',
            'related_queries': [],
            'timestamp': datetime.now().isoformat()
        }

        for attempt in range(MAX_RETRIES):
            try:
                # Build payload for single term
                self.pytrends.build_payload([term], geo=geo, timeframe=timeframe)

                # Get interest over time
                interest = self.pytrends.interest_over_time()

                if interest.empty:
                    result['status'] = 'NO_DATA'
                    result['recommendation'] = f"No data returned for '{term}'. May be too niche or misspelled."
                    return result

                # Calculate metrics
                values = interest[term].values
                result['avg_volume'] = float(values.mean())
                result['variance'] = float(values.var())
                result['zero_ratio'] = float((values == 0).sum() / len(values))

                # Get related queries for alternatives
                try:
                    self._delay()
                    related = self.pytrends.related_queries()
                    if term in related and related[term]['top'] is not None:
                        result['related_queries'] = related[term]['top']['query'].head(5).tolist()
                except Exception:
                    pass  # Related queries are optional

                # Validation logic
                if result['avg_volume'] < MIN_VOLUME_THRESHOLD:
                    result['status'] = 'LOW_VOLUME'
                    result['recommendation'] = f"Average volume {result['avg_volume']:.1f} below threshold {MIN_VOLUME_THRESHOLD}. Consider related: {result['related_queries'][:3]}"
                elif result['variance'] < MIN_VARIANCE_THRESHOLD:
                    result['status'] = 'FLAT'
                    result['recommendation'] = f"Search interest is flat (variance={result['variance']:.1f}). May not capture temporal dynamics."
                elif result['zero_ratio'] > ZERO_RATIO_THRESHOLD:
                    result['status'] = 'TOO_MANY_ZEROS'
                    result['recommendation'] = f"{result['zero_ratio']*100:.0f}% of data points are zero. Term may be too obscure."
                else:
                    result['status'] = 'PASS'
                    result['valid'] = True
                    result['recommendation'] = 'Term validated successfully.'

                return result

            except Exception as e:
                error_msg = str(e)
                if '429' in error_msg or 'Too Many Requests' in error_msg:
                    print(f"  Rate limited on '{term}', backing off (attempt {attempt+1})...")
                    self._delay(attempt + 1)
                else:
                    result['status'] = 'ERROR'
                    result['recommendation'] = f"API error: {error_msg[:100]}"
                    self.errors.append(f"{term}: {error_msg}")
                    return result

        result['status'] = 'RATE_LIMITED'
        result['recommendation'] = 'Failed after max retries due to rate limiting.'
        return result

    def validate_category(self, category: str, terms: List[str],
                          sample_size: Optional[int] = None) -> List[Dict]:
        """
        Validate all terms in a category.

        Args:
            category: Category name
            terms: List of search terms
            sample_size: If set, only validate a random sample
        """
        print(f"\n{'='*60}")
        print(f"Validating category: {category.upper()}")
        print(f"{'='*60}")

        if sample_size and len(terms) > sample_size:
            terms = random.sample(terms, sample_size)
            print(f"(Sampling {sample_size} of {len(terms)} terms)")

        results = []
        for i, term in enumerate(terms, 1):
            print(f"  [{i}/{len(terms)}] Checking: '{term}'...", end=" ")

            result = self.validate_term(term)
            results.append(result)

            status_emoji = '✅' if result['valid'] else '❌'
            print(f"{status_emoji} {result['status']} (avg={result['avg_volume']:.1f})")

            self._delay()

        return results

    def run_full_validation(self, term_categories: Dict,
                            sample_per_category: Optional[int] = None) -> Dict:
        """
        Run validation on all categories.

        Args:
            term_categories: Dict from term_categories.json
            sample_per_category: If set, sample this many terms per category
        """
        all_results = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'framework': 'CommDAAF v1.0',
                'validation_tier': 'EXPLORATORY',
                'thresholds': {
                    'min_volume': MIN_VOLUME_THRESHOLD,
                    'min_variance': MIN_VARIANCE_THRESHOLD,
                    'max_zero_ratio': ZERO_RATIO_THRESHOLD
                }
            },
            'categories': {},
            'summary': {
                'total_terms': 0,
                'passed': 0,
                'failed': 0,
                'by_status': {}
            }
        }

        for category, data in term_categories.items():
            if category == 'partisan_pairs':
                # Handle partisan pairs differently - extract all terms
                pairs = data.get('pairs', [])
                terms = []
                for pair in pairs:
                    terms.extend([pair['left'], pair['right']])
                if not terms:
                    continue
            elif category == 'state_specific':
                # Flatten state-specific terms
                terms = []
                for state_terms in data.values():
                    terms.extend(state_terms)
            else:
                terms = data.get('terms', [])

            if not terms:
                continue

            results = self.validate_category(category, terms, sample_per_category)

            all_results['categories'][category] = {
                'results': results,
                'summary': {
                    'total': len(results),
                    'passed': sum(1 for r in results if r['valid']),
                    'failed': sum(1 for r in results if not r['valid'])
                }
            }

            # Update overall summary
            for r in results:
                all_results['summary']['total_terms'] += 1
                if r['valid']:
                    all_results['summary']['passed'] += 1
                else:
                    all_results['summary']['failed'] += 1

                status = r['status']
                all_results['summary']['by_status'][status] = \
                    all_results['summary']['by_status'].get(status, 0) + 1

        return all_results

    def generate_report(self, results: Dict, output_path: Path) -> str:
        """Generate markdown validation report."""

        meta = results['metadata']
        summary = results['summary']

        report = f"""# Search Term Validation Report

**Study:** VibePoll-2026
**Framework:** {meta['framework']}
**Validation Tier:** {meta['validation_tier']}
**Generated:** {meta['timestamp']}

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Terms Validated | {summary['total_terms']} |
| **Passed** | {summary['passed']} ({summary['passed']/max(summary['total_terms'],1)*100:.0f}%) |
| **Failed** | {summary['failed']} ({summary['failed']/max(summary['total_terms'],1)*100:.0f}%) |

### Status Breakdown

| Status | Count |
|--------|-------|
"""
        for status, count in sorted(summary['by_status'].items()):
            emoji = '✅' if status == 'PASS' else '❌'
            report += f"| {emoji} {status} | {count} |\n"

        report += f"""

---

## Validation Thresholds

Per CommDAAF Section 6 requirements:

| Threshold | Value | Rationale |
|-----------|-------|-----------|
| Min Average Volume | {meta['thresholds']['min_volume']} | Terms below this have insufficient search activity |
| Min Variance | {meta['thresholds']['min_variance']} | Flat terms don't capture temporal dynamics |
| Max Zero Ratio | {meta['thresholds']['max_zero_ratio']*100:.0f}% | Too many zeros indicates obscure term |

---

## Category Results

"""

        for category, cat_data in results['categories'].items():
            cat_summary = cat_data['summary']
            pass_rate = cat_summary['passed'] / max(cat_summary['total'], 1) * 100

            report += f"""### {category.upper().replace('_', ' ')}

**Pass Rate:** {cat_summary['passed']}/{cat_summary['total']} ({pass_rate:.0f}%)

| Term | Status | Avg Volume | Variance | Recommendation |
|------|--------|------------|----------|----------------|
"""
            for r in cat_data['results']:
                status_emoji = '✅' if r['valid'] else '❌'
                rec = r['recommendation'][:80] + '...' if len(r['recommendation']) > 80 else r['recommendation']
                report += f"| {r['term']} | {status_emoji} {r['status']} | {r['avg_volume']:.1f} | {r['variance']:.1f} | {rec} |\n"

            report += "\n"

        # Terms to Remove section
        failed_terms = []
        for cat, cat_data in results['categories'].items():
            for r in cat_data['results']:
                if not r['valid']:
                    failed_terms.append({
                        'term': r['term'],
                        'category': cat,
                        'status': r['status'],
                        'recommendation': r['recommendation']
                    })

        if failed_terms:
            report += """---

## Terms to Remove or Modify

The following terms failed validation and should be reviewed:

| Term | Category | Status | Action Required |
|------|----------|--------|-----------------|
"""
            for t in failed_terms:
                report += f"| {t['term']} | {t['category']} | {t['status']} | {t['recommendation'][:60]} |\n"

        report += f"""

---

## Methodology Notes

1. **Data Source:** Google Trends via pytrends (past 3 months, US national)
2. **Rate Limiting:** 3-6 second delays between requests, exponential backoff on 429
3. **Validation Logic:**
   - PASS: Volume ≥ {meta['thresholds']['min_volume']}, variance ≥ {meta['thresholds']['min_variance']}, zeros ≤ {meta['thresholds']['max_zero_ratio']*100:.0f}%
   - LOW_VOLUME: Average search interest below threshold
   - FLAT: Insufficient temporal variation
   - TOO_MANY_ZEROS: Term too obscure for reliable signal

---

*Report generated by Claude Code following CommDAAF v1.0 protocol*
"""

        # Save report
        with open(output_path, 'w') as f:
            f.write(report)

        # Also save raw JSON for programmatic use
        json_path = output_path.with_suffix('.json')
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        return report


def main():
    """Main validation pipeline."""

    print("=" * 70)
    print("VibePoll-2026 Search Term Validation Pipeline")
    print("CommDAAF v1.0 - EXPLORATORY Tier")
    print("=" * 70)

    # Load term categories
    with open(REFERENCE_DIR / "term_categories.json") as f:
        term_categories = json.load(f)

    # Count total terms
    total_terms = 0
    for cat, data in term_categories.items():
        if cat == 'partisan_pairs':
            pairs = data.get('pairs', [])
            total_terms += len(pairs) * 2
        elif cat == 'state_specific':
            for terms in data.values():
                total_terms += len(terms)
        else:
            total_terms += len(data.get('terms', []))

    print(f"\nTotal terms to validate: {total_terms}")
    print(f"Estimated time: {total_terms * 5 / 60:.1f} minutes")
    print("\nStarting validation...\n")

    # Run validation
    validator = SearchTermValidator()
    results = validator.run_full_validation(term_categories)

    # Generate report
    output_path = OUTPUT_DIR / "search_term_validation.md"
    report = validator.generate_report(results, output_path)

    print("\n" + "=" * 70)
    print("VALIDATION COMPLETE")
    print("=" * 70)
    print(f"\nResults saved to: {output_path}")
    print(f"JSON data saved to: {output_path.with_suffix('.json')}")
    print(f"\nSummary: {results['summary']['passed']}/{results['summary']['total_terms']} terms passed")

    if validator.errors:
        print(f"\nWarnings/Errors encountered: {len(validator.errors)}")
        for err in validator.errors[:5]:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
