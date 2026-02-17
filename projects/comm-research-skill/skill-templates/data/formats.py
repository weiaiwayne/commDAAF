#!/usr/bin/env python3
"""
Format Detection and Conversion Module

Auto-detects social media data formats and converts to standard schema.
Handles: Twitter, Reddit, Telegram, YouTube, Bluesky, generic CSV/JSON.
"""

import os
import json
import csv
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
from datetime import datetime
import pandas as pd
from dataclasses import dataclass


@dataclass
class StandardSchema:
    """Standard schema for social media data."""
    
    # Required fields
    id: str                      # Unique identifier
    text: str                    # Main text content
    timestamp: datetime          # When posted
    author_id: str              # Author identifier
    
    # Common optional fields
    author_name: Optional[str] = None
    platform: Optional[str] = None
    url: Optional[str] = None
    reply_to: Optional[str] = None
    repost_of: Optional[str] = None
    
    # Engagement metrics
    likes: Optional[int] = None
    shares: Optional[int] = None
    replies: Optional[int] = None
    views: Optional[int] = None
    
    # Platform-specific (preserved)
    raw_data: Optional[Dict] = None


class FormatDetector:
    """Detect social media data format."""
    
    @staticmethod
    def detect_format(path: str) -> Dict[str, Any]:
        """
        Detect format of data file or directory.
        
        Returns dict with:
        - format: str (twitter_v2, reddit_praw, telegram_json, etc.)
        - platform: str (twitter, reddit, telegram, etc.)
        - structure: str (single_file, directory, etc.)
        - confidence: float (0-1)
        """
        path = Path(path)
        
        if path.is_dir():
            return FormatDetector._detect_directory(path)
        elif path.suffix == '.csv':
            return FormatDetector._detect_csv(path)
        elif path.suffix in ['.json', '.jsonl']:
            return FormatDetector._detect_json(path)
        elif path.suffix == '.html':
            return FormatDetector._detect_html(path)
        else:
            return {'format': 'unknown', 'confidence': 0}
    
    @staticmethod
    def _detect_csv(path: Path) -> Dict[str, Any]:
        """Detect CSV format based on columns."""
        try:
            df = pd.read_csv(path, nrows=5)
            columns = set(df.columns.str.lower())
            
            # Twitter CSV patterns
            if {'tweet_id', 'text', 'created_at'} <= columns:
                return {'format': 'twitter_csv', 'platform': 'twitter', 'confidence': 0.9}
            if {'id', 'full_text', 'user'} <= columns:
                return {'format': 'twitter_csv_v1', 'platform': 'twitter', 'confidence': 0.8}
            
            # Reddit patterns
            if {'id', 'body', 'subreddit'} <= columns:
                return {'format': 'reddit_csv', 'platform': 'reddit', 'confidence': 0.9}
            if {'title', 'selftext', 'subreddit'} <= columns:
                return {'format': 'reddit_posts_csv', 'platform': 'reddit', 'confidence': 0.9}
            
            # Generic with common fields
            if {'text', 'timestamp'} <= columns or {'content', 'date'} <= columns:
                return {'format': 'generic_csv', 'platform': 'unknown', 'confidence': 0.5}
            
            return {'format': 'csv_unknown', 'platform': 'unknown', 'confidence': 0.3}
            
        except Exception as e:
            return {'format': 'csv_error', 'error': str(e), 'confidence': 0}
    
    @staticmethod
    def _detect_json(path: Path) -> Dict[str, Any]:
        """Detect JSON format based on structure."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # Try loading first line (JSONL) or full file (JSON)
                first_line = f.readline()
                
            try:
                # Try as JSONL
                sample = json.loads(first_line)
                is_jsonl = True
            except:
                # Try as full JSON
                with open(path, 'r', encoding='utf-8') as f:
                    sample = json.load(f)
                is_jsonl = False
                if isinstance(sample, list) and len(sample) > 0:
                    sample = sample[0]
            
            # Twitter API v2
            if 'data' in sample and 'id' in sample.get('data', [{}])[0]:
                return {'format': 'twitter_v2', 'platform': 'twitter', 'confidence': 0.95}
            
            # Twitter API v1
            if 'id_str' in sample and 'full_text' in sample:
                return {'format': 'twitter_v1', 'platform': 'twitter', 'confidence': 0.95}
            if 'id' in sample and 'text' in sample and 'user' in sample:
                return {'format': 'twitter_v1', 'platform': 'twitter', 'confidence': 0.9}
            
            # Reddit PRAW
            if 'subreddit' in sample and ('body' in sample or 'selftext' in sample):
                return {'format': 'reddit_praw', 'platform': 'reddit', 'confidence': 0.9}
            
            # Reddit Pushshift
            if 'subreddit' in sample and 'created_utc' in sample:
                return {'format': 'reddit_pushshift', 'platform': 'reddit', 'confidence': 0.9}
            
            # Telegram JSON export
            if 'messages' in sample or ('from' in sample and 'text' in sample):
                return {'format': 'telegram_json', 'platform': 'telegram', 'confidence': 0.9}
            
            # Bluesky AT Protocol
            if 'uri' in sample and 'cid' in sample:
                return {'format': 'bluesky_at', 'platform': 'bluesky', 'confidence': 0.9}
            
            # YouTube API
            if 'snippet' in sample and 'videoId' in sample.get('snippet', {}):
                return {'format': 'youtube_api', 'platform': 'youtube', 'confidence': 0.9}
            
            format_type = 'jsonl_unknown' if is_jsonl else 'json_unknown'
            return {'format': format_type, 'platform': 'unknown', 'confidence': 0.3}
            
        except Exception as e:
            return {'format': 'json_error', 'error': str(e), 'confidence': 0}
    
    @staticmethod
    def _detect_html(path: Path) -> Dict[str, Any]:
        """Detect HTML export format."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(5000)  # First 5KB
            
            if 'tgme' in content or 'telegram' in content.lower():
                return {'format': 'telegram_html', 'platform': 'telegram', 'confidence': 0.8}
            
            return {'format': 'html_unknown', 'platform': 'unknown', 'confidence': 0.3}
            
        except Exception as e:
            return {'format': 'html_error', 'error': str(e), 'confidence': 0}
    
    @staticmethod
    def _detect_directory(path: Path) -> Dict[str, Any]:
        """Detect format from directory contents."""
        files = list(path.glob('*'))
        
        # Telegram export structure
        if any(f.name == 'result.json' for f in files):
            return {'format': 'telegram_export', 'platform': 'telegram', 'confidence': 0.95}
        
        # Check first data file
        data_files = [f for f in files if f.suffix in ['.json', '.csv', '.jsonl']]
        if data_files:
            return FormatDetector.detect_format(str(data_files[0]))
        
        return {'format': 'directory_unknown', 'confidence': 0.2}


class DataLoader:
    """Load and convert data to standard format."""
    
    def __init__(self):
        self.loaders = {
            'twitter_v1': self._load_twitter_v1,
            'twitter_v2': self._load_twitter_v2,
            'twitter_csv': self._load_twitter_csv,
            'reddit_praw': self._load_reddit,
            'reddit_pushshift': self._load_reddit,
            'reddit_csv': self._load_reddit_csv,
            'telegram_json': self._load_telegram_json,
            'telegram_export': self._load_telegram_export,
            'bluesky_at': self._load_bluesky,
            'youtube_api': self._load_youtube,
            'generic_csv': self._load_generic_csv,
        }
    
    def load(self, path: str, format_hint: str = None) -> pd.DataFrame:
        """
        Load data from path into standardized DataFrame.
        
        Args:
            path: Path to file or directory
            format_hint: Optional format hint to skip detection
        
        Returns:
            DataFrame with standard schema
        """
        if format_hint:
            detected = {'format': format_hint, 'confidence': 1.0}
        else:
            detected = FormatDetector.detect_format(path)
        
        format_type = detected['format']
        
        if format_type in self.loaders:
            df = self.loaders[format_type](path)
            df['_source_format'] = format_type
            df['_source_path'] = path
            return self._validate_schema(df)
        else:
            raise ValueError(f"Unknown format: {format_type}. Detected: {detected}")
    
    def _validate_schema(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ensure required columns exist."""
        required = ['id', 'text', 'timestamp', 'author_id']
        
        for col in required:
            if col not in df.columns:
                df[col] = None
        
        # Convert timestamp to datetime if needed
        if df['timestamp'].dtype != 'datetime64[ns]':
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        
        return df
    
    def _load_twitter_v1(self, path: str) -> pd.DataFrame:
        """Load Twitter API v1 format."""
        with open(path, 'r') as f:
            if path.endswith('.jsonl'):
                data = [json.loads(line) for line in f]
            else:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
        
        records = []
        for tweet in data:
            records.append({
                'id': tweet.get('id_str') or str(tweet.get('id')),
                'text': tweet.get('full_text') or tweet.get('text'),
                'timestamp': tweet.get('created_at'),
                'author_id': tweet.get('user', {}).get('id_str'),
                'author_name': tweet.get('user', {}).get('screen_name'),
                'platform': 'twitter',
                'likes': tweet.get('favorite_count'),
                'shares': tweet.get('retweet_count'),
                'reply_to': tweet.get('in_reply_to_status_id_str'),
                'raw_data': tweet
            })
        
        return pd.DataFrame(records)
    
    def _load_twitter_v2(self, path: str) -> pd.DataFrame:
        """Load Twitter API v2 format."""
        with open(path, 'r') as f:
            response = json.load(f)
        
        tweets = response.get('data', [])
        users = {u['id']: u for u in response.get('includes', {}).get('users', [])}
        
        records = []
        for tweet in tweets:
            author = users.get(tweet.get('author_id'), {})
            records.append({
                'id': tweet.get('id'),
                'text': tweet.get('text'),
                'timestamp': tweet.get('created_at'),
                'author_id': tweet.get('author_id'),
                'author_name': author.get('username'),
                'platform': 'twitter',
                'likes': tweet.get('public_metrics', {}).get('like_count'),
                'shares': tweet.get('public_metrics', {}).get('retweet_count'),
                'replies': tweet.get('public_metrics', {}).get('reply_count'),
                'raw_data': tweet
            })
        
        return pd.DataFrame(records)
    
    def _load_twitter_csv(self, path: str) -> pd.DataFrame:
        """Load Twitter CSV export."""
        df = pd.read_csv(path)
        
        # Normalize column names
        col_map = {
            'tweet_id': 'id',
            'created_at': 'timestamp',
            'user_id': 'author_id',
            'username': 'author_name',
            'screen_name': 'author_name',
            'favorite_count': 'likes',
            'retweet_count': 'shares'
        }
        
        df = df.rename(columns={k: v for k, v in col_map.items() if k in df.columns})
        df['platform'] = 'twitter'
        
        return df
    
    def _load_reddit(self, path: str) -> pd.DataFrame:
        """Load Reddit PRAW or Pushshift format."""
        with open(path, 'r') as f:
            if path.endswith('.jsonl'):
                data = [json.loads(line) for line in f]
            else:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
        
        records = []
        for item in data:
            # Handle both posts and comments
            text = item.get('body') or item.get('selftext') or item.get('title', '')
            
            records.append({
                'id': item.get('id'),
                'text': text,
                'timestamp': datetime.fromtimestamp(item.get('created_utc', 0)),
                'author_id': item.get('author'),
                'author_name': item.get('author'),
                'platform': 'reddit',
                'url': f"https://reddit.com{item.get('permalink', '')}",
                'likes': item.get('score'),
                'replies': item.get('num_comments'),
                'subreddit': item.get('subreddit'),
                'raw_data': item
            })
        
        return pd.DataFrame(records)
    
    def _load_reddit_csv(self, path: str) -> pd.DataFrame:
        """Load Reddit CSV."""
        df = pd.read_csv(path)
        
        # Normalize
        if 'body' in df.columns:
            df['text'] = df['body']
        elif 'selftext' in df.columns:
            df['text'] = df['selftext']
        
        if 'author' in df.columns:
            df['author_id'] = df['author']
            df['author_name'] = df['author']
        
        if 'created_utc' in df.columns:
            df['timestamp'] = pd.to_datetime(df['created_utc'], unit='s')
        
        df['platform'] = 'reddit'
        
        return df
    
    def _load_telegram_json(self, path: str) -> pd.DataFrame:
        """Load Telegram JSON export."""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        messages = data.get('messages', data if isinstance(data, list) else [data])
        
        records = []
        for msg in messages:
            # Handle text that might be a list of objects
            text = msg.get('text', '')
            if isinstance(text, list):
                text = ' '.join(
                    item.get('text', str(item)) if isinstance(item, dict) else str(item)
                    for item in text
                )
            
            records.append({
                'id': str(msg.get('id')),
                'text': text,
                'timestamp': msg.get('date'),
                'author_id': str(msg.get('from_id', '')),
                'author_name': msg.get('from', ''),
                'platform': 'telegram',
                'views': msg.get('views'),
                'forwards': msg.get('forwards'),
                'reply_to': msg.get('reply_to_message_id'),
                'raw_data': msg
            })
        
        return pd.DataFrame(records)
    
    def _load_telegram_export(self, path: str) -> pd.DataFrame:
        """Load Telegram desktop export (directory with result.json)."""
        result_path = Path(path) / 'result.json'
        return self._load_telegram_json(str(result_path))
    
    def _load_bluesky(self, path: str) -> pd.DataFrame:
        """Load Bluesky AT Protocol format."""
        with open(path, 'r') as f:
            if path.endswith('.jsonl'):
                data = [json.loads(line) for line in f]
            else:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
        
        records = []
        for post in data:
            record = post.get('record', post)
            author = post.get('author', {})
            
            records.append({
                'id': post.get('uri', '').split('/')[-1],
                'text': record.get('text', ''),
                'timestamp': record.get('createdAt'),
                'author_id': author.get('did', ''),
                'author_name': author.get('handle', ''),
                'platform': 'bluesky',
                'likes': post.get('likeCount'),
                'shares': post.get('repostCount'),
                'replies': post.get('replyCount'),
                'raw_data': post
            })
        
        return pd.DataFrame(records)
    
    def _load_youtube(self, path: str) -> pd.DataFrame:
        """Load YouTube API format (comments)."""
        with open(path, 'r') as f:
            data = json.load(f)
        
        items = data.get('items', data if isinstance(data, list) else [data])
        
        records = []
        for item in items:
            snippet = item.get('snippet', {})
            top_comment = snippet.get('topLevelComment', {}).get('snippet', snippet)
            
            records.append({
                'id': item.get('id'),
                'text': top_comment.get('textDisplay') or top_comment.get('textOriginal'),
                'timestamp': top_comment.get('publishedAt'),
                'author_id': top_comment.get('authorChannelId', {}).get('value'),
                'author_name': top_comment.get('authorDisplayName'),
                'platform': 'youtube',
                'likes': top_comment.get('likeCount'),
                'video_id': snippet.get('videoId'),
                'raw_data': item
            })
        
        return pd.DataFrame(records)
    
    def _load_generic_csv(self, path: str) -> pd.DataFrame:
        """Load generic CSV with flexible column mapping."""
        df = pd.read_csv(path)
        
        # Try to find standard columns
        text_cols = ['text', 'content', 'body', 'message', 'post', 'tweet']
        time_cols = ['timestamp', 'date', 'time', 'created_at', 'datetime', 'created']
        id_cols = ['id', 'post_id', 'message_id', 'tweet_id']
        author_cols = ['author', 'user', 'username', 'author_id', 'user_id', 'from']
        
        def find_col(candidates):
            for c in candidates:
                matches = [col for col in df.columns if c.lower() in col.lower()]
                if matches:
                    return matches[0]
            return None
        
        col_mapping = {}
        
        text_col = find_col(text_cols)
        if text_col:
            col_mapping[text_col] = 'text'
        
        time_col = find_col(time_cols)
        if time_col:
            col_mapping[time_col] = 'timestamp'
        
        id_col = find_col(id_cols)
        if id_col:
            col_mapping[id_col] = 'id'
        else:
            df['id'] = range(len(df))
        
        author_col = find_col(author_cols)
        if author_col:
            col_mapping[author_col] = 'author_id'
        
        df = df.rename(columns=col_mapping)
        df['platform'] = 'unknown'
        
        return df


# Convenience function
def load_social_media_data(path: str, format_hint: str = None) -> pd.DataFrame:
    """
    Load social media data from any supported format.
    
    Args:
        path: Path to file or directory
        format_hint: Optional format hint (twitter_v1, reddit_praw, etc.)
    
    Returns:
        Standardized DataFrame with columns:
        - id, text, timestamp, author_id (required)
        - author_name, platform, likes, shares, etc. (optional)
    
    Examples:
        >>> df = load_social_media_data("tweets.json")
        >>> df = load_social_media_data("reddit_data.csv")
        >>> df = load_social_media_data("telegram_export/")
    """
    loader = DataLoader()
    return loader.load(path, format_hint)


def detect_format(path: str) -> Dict[str, Any]:
    """
    Detect format of social media data.
    
    Returns dict with format, platform, and confidence.
    """
    return FormatDetector.detect_format(path)


# CLI interface
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Detect and convert social media data')
    parser.add_argument('path', help='Path to data file or directory')
    parser.add_argument('--output', '-o', help='Output CSV path')
    parser.add_argument('--format', '-f', help='Force specific format')
    
    args = parser.parse_args()
    
    # Detect
    detected = detect_format(args.path)
    print(f"Detected format: {detected['format']}")
    print(f"Platform: {detected.get('platform', 'unknown')}")
    print(f"Confidence: {detected.get('confidence', 0):.0%}")
    
    # Load
    df = load_social_media_data(args.path, args.format)
    print(f"\nLoaded {len(df)} records")
    print(f"Columns: {list(df.columns)}")
    
    # Save if requested
    if args.output:
        df.to_csv(args.output, index=False)
        print(f"Saved to {args.output}")
