#!/usr/bin/env python3
"""
Data Quality Validators

Check data quality and report issues before analysis.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta
import re


class DataQualityReport:
    """Generate data quality report."""
    
    def __init__(self, df: pd.DataFrame, text_column: str = 'text'):
        self.df = df
        self.text_column = text_column
        self.issues = []
        self.warnings = []
        self.stats = {}
    
    def run_all_checks(self) -> Dict[str, Any]:
        """Run all quality checks."""
        self._check_completeness()
        self._check_duplicates()
        self._check_text_quality()
        self._check_timestamps()
        self._check_language()
        self._check_bots_spam()
        
        return {
            'stats': self.stats,
            'issues': self.issues,
            'warnings': self.warnings,
            'passed': len(self.issues) == 0,
            'summary': self._generate_summary()
        }
    
    def _check_completeness(self):
        """Check for missing values."""
        missing = self.df.isnull().sum()
        total = len(self.df)
        
        self.stats['completeness'] = {}
        
        for col in self.df.columns:
            pct_missing = missing[col] / total * 100
            self.stats['completeness'][col] = {
                'missing': int(missing[col]),
                'pct_missing': round(pct_missing, 2)
            }
            
            if pct_missing > 50:
                self.issues.append(f"Column '{col}' is {pct_missing:.1f}% missing")
            elif pct_missing > 10:
                self.warnings.append(f"Column '{col}' is {pct_missing:.1f}% missing")
    
    def _check_duplicates(self):
        """Check for duplicate records."""
        # Exact duplicates
        exact_dups = self.df.duplicated().sum()
        
        # Text duplicates
        if self.text_column in self.df.columns:
            text_dups = self.df[self.text_column].duplicated().sum()
        else:
            text_dups = 0
        
        self.stats['duplicates'] = {
            'exact_duplicates': int(exact_dups),
            'text_duplicates': int(text_dups),
            'pct_text_duplicates': round(text_dups / len(self.df) * 100, 2)
        }
        
        if text_dups / len(self.df) > 0.1:
            self.warnings.append(f"{text_dups} duplicate texts ({text_dups/len(self.df)*100:.1f}%)")
    
    def _check_text_quality(self):
        """Check text content quality."""
        if self.text_column not in self.df.columns:
            self.issues.append(f"Text column '{self.text_column}' not found")
            return
        
        texts = self.df[self.text_column].dropna()
        
        # Length statistics
        lengths = texts.str.len()
        word_counts = texts.str.split().str.len()
        
        self.stats['text_quality'] = {
            'avg_length': round(lengths.mean(), 1),
            'median_length': round(lengths.median(), 1),
            'avg_words': round(word_counts.mean(), 1),
            'min_words': int(word_counts.min()),
            'max_words': int(word_counts.max()),
        }
        
        # Check for very short texts
        short_texts = (word_counts < 5).sum()
        if short_texts / len(texts) > 0.3:
            self.warnings.append(
                f"{short_texts} texts ({short_texts/len(texts)*100:.1f}%) have <5 words. "
                "Topic modeling may be unreliable."
            )
        
        # Check for very long texts (might be spam)
        very_long = (word_counts > 500).sum()
        if very_long > 0:
            self.warnings.append(f"{very_long} texts have >500 words (check for spam)")
        
        # Empty texts
        empty = (texts.str.strip() == '').sum()
        if empty > 0:
            self.warnings.append(f"{empty} empty text fields")
        
        # URL-only texts
        url_pattern = r'^https?://\S+$'
        url_only = texts.str.match(url_pattern).sum()
        if url_only > 0:
            self.warnings.append(f"{url_only} texts are URL-only")
    
    def _check_timestamps(self):
        """Check timestamp validity."""
        if 'timestamp' not in self.df.columns:
            self.warnings.append("No timestamp column found")
            return
        
        timestamps = pd.to_datetime(self.df['timestamp'], errors='coerce')
        
        valid = timestamps.notna().sum()
        invalid = timestamps.isna().sum()
        
        self.stats['timestamps'] = {
            'valid': int(valid),
            'invalid': int(invalid),
            'min_date': str(timestamps.min()) if valid > 0 else None,
            'max_date': str(timestamps.max()) if valid > 0 else None,
        }
        
        if invalid > 0:
            self.warnings.append(f"{invalid} invalid timestamps")
        
        # Check for future dates
        future = (timestamps > datetime.now()).sum()
        if future > 0:
            self.warnings.append(f"{future} timestamps are in the future")
        
        # Check for very old dates (before platform existed)
        very_old = (timestamps < datetime(2000, 1, 1)).sum()
        if very_old > 0:
            self.warnings.append(f"{very_old} timestamps before year 2000")
    
    def _check_language(self):
        """Check language distribution (basic detection)."""
        if self.text_column not in self.df.columns:
            return
        
        texts = self.df[self.text_column].dropna()
        
        # Simple language detection based on character patterns
        def detect_script(text):
            if pd.isna(text):
                return 'unknown'
            text = str(text)
            
            # Check for non-Latin scripts
            if re.search(r'[\u4e00-\u9fff]', text):  # Chinese
                return 'chinese'
            if re.search(r'[\u0400-\u04ff]', text):  # Cyrillic
                return 'cyrillic'
            if re.search(r'[\u0600-\u06ff]', text):  # Arabic
                return 'arabic'
            if re.search(r'[\u0900-\u097f]', text):  # Devanagari
                return 'devanagari'
            if re.search(r'[\u3040-\u309f\u30a0-\u30ff]', text):  # Japanese
                return 'japanese'
            if re.search(r'[\uac00-\ud7af]', text):  # Korean
                return 'korean'
            
            return 'latin'
        
        scripts = texts.apply(detect_script)
        script_counts = scripts.value_counts()
        
        self.stats['language'] = {
            'script_distribution': script_counts.to_dict(),
            'primary_script': script_counts.index[0] if len(script_counts) > 0 else 'unknown',
            'multilingual': len(script_counts) > 1
        }
        
        if len(script_counts) > 1:
            non_primary = script_counts.iloc[1:].sum()
            pct_other = non_primary / len(texts) * 100
            if pct_other > 10:
                self.warnings.append(
                    f"Multilingual data detected ({pct_other:.1f}% non-primary script). "
                    "Consider language-specific analysis."
                )
    
    def _check_bots_spam(self):
        """Check for potential bot/spam indicators."""
        if self.text_column not in self.df.columns:
            return
        
        texts = self.df[self.text_column].dropna()
        
        # Repetitive content
        text_counts = texts.value_counts()
        highly_repeated = (text_counts > 5).sum()
        
        self.stats['spam_indicators'] = {
            'repeated_texts': int(highly_repeated),
        }
        
        if highly_repeated > 10:
            self.warnings.append(
                f"{highly_repeated} texts appear >5 times. "
                "Check for bot activity or data duplication."
            )
        
        # Check for suspicious patterns
        if 'author_id' in self.df.columns:
            author_counts = self.df['author_id'].value_counts()
            high_volume = (author_counts > author_counts.quantile(0.99)).sum()
            
            if high_volume > 0:
                self.stats['spam_indicators']['high_volume_authors'] = int(high_volume)
                self.warnings.append(
                    f"{high_volume} authors in top 1% by volume. "
                    "Review for bot/spam accounts."
                )
    
    def _generate_summary(self) -> str:
        """Generate human-readable summary."""
        summary = []
        
        summary.append(f"Dataset: {len(self.df):,} records")
        
        if 'text_quality' in self.stats:
            summary.append(f"Avg text length: {self.stats['text_quality']['avg_words']:.0f} words")
        
        if 'timestamps' in self.stats and self.stats['timestamps']['min_date']:
            summary.append(
                f"Date range: {self.stats['timestamps']['min_date'][:10]} to "
                f"{self.stats['timestamps']['max_date'][:10]}"
            )
        
        if 'language' in self.stats:
            summary.append(f"Primary script: {self.stats['language']['primary_script']}")
        
        if self.issues:
            summary.append(f"\n⚠️ {len(self.issues)} ISSUES (must address)")
        
        if self.warnings:
            summary.append(f"⚡ {len(self.warnings)} warnings (review recommended)")
        
        return '\n'.join(summary)


def validate_data(df: pd.DataFrame, text_column: str = 'text') -> Dict[str, Any]:
    """
    Run data quality validation.
    
    Args:
        df: DataFrame to validate
        text_column: Name of text column
    
    Returns:
        Quality report with stats, issues, and warnings
    """
    report = DataQualityReport(df, text_column)
    return report.run_all_checks()


def validate_for_method(df: pd.DataFrame, method: str) -> Dict[str, Any]:
    """
    Validate data for specific analysis method.
    
    Args:
        df: DataFrame to validate
        method: Analysis method (sentiment, topic, network, coordination)
    
    Returns:
        Method-specific validation report
    """
    base_report = validate_data(df)
    
    method_warnings = []
    method_ok = True
    
    if method == 'sentiment':
        # Check for sarcasm-prone content
        if 'text_quality' in base_report['stats']:
            avg_words = base_report['stats']['text_quality']['avg_words']
            if avg_words < 10:
                method_warnings.append(
                    "Very short texts — context may be insufficient for sentiment"
                )
    
    elif method == 'topic':
        # Topic modeling needs longer documents
        if 'text_quality' in base_report['stats']:
            avg_words = base_report['stats']['text_quality']['avg_words']
            if avg_words < 30:
                method_warnings.append(
                    f"Average {avg_words:.0f} words/doc — too short for LDA. "
                    "Use BERTopic or aggregate documents."
                )
                method_ok = False
        
        if len(df) < 500:
            method_warnings.append(
                f"Only {len(df)} documents — topic modeling may be unreliable. "
                "Consider 1000+ documents."
            )
    
    elif method == 'network':
        # Network analysis needs connections
        if 'author_id' not in df.columns:
            method_warnings.append("No author_id — cannot build user network")
            method_ok = False
    
    elif method == 'coordination':
        # Coordination detection needs timestamps
        if 'timestamp' not in df.columns:
            method_warnings.append("No timestamps — cannot detect temporal coordination")
            method_ok = False
        
        if len(df) < 1000:
            method_warnings.append(
                "Small dataset — coordination patterns may be coincidental"
            )
    
    return {
        **base_report,
        'method': method,
        'method_warnings': method_warnings,
        'method_ok': method_ok
    }


# CLI
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate social media data')
    parser.add_argument('path', help='Path to data file')
    parser.add_argument('--method', '-m', help='Validate for specific method')
    parser.add_argument('--text-column', '-t', default='text', help='Text column name')
    
    args = parser.parse_args()
    
    from formats import load_social_media_data
    
    df = load_social_media_data(args.path)
    
    if args.method:
        report = validate_for_method(df, args.method)
    else:
        report = validate_data(df, args.text_column)
    
    print("\n" + "="*50)
    print("DATA QUALITY REPORT")
    print("="*50)
    print(report['summary'])
    
    if report['issues']:
        print("\n⚠️ ISSUES:")
        for issue in report['issues']:
            print(f"  - {issue}")
    
    if report['warnings']:
        print("\n⚡ WARNINGS:")
        for warning in report['warnings']:
            print(f"  - {warning}")
    
    if args.method and report.get('method_warnings'):
        print(f"\n📊 {args.method.upper()} METHOD WARNINGS:")
        for warning in report['method_warnings']:
            print(f"  - {warning}")
