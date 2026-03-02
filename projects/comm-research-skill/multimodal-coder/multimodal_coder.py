#!/usr/bin/env python3
"""
CommDAAF Multimodal Coder

Code images, videos, and image-text combinations in social media content.
"""

import json
import base64
import subprocess
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, field, asdict
from pathlib import Path
from enum import Enum

class ImageTextRelationship(Enum):
    ILLUSTRATIVE = "illustrative"      # Image depicts what text describes
    COMPLEMENTARY = "complementary"    # Image adds info not in text
    CONTRADICTORY = "contradictory"    # Image contradicts text (irony)
    SYMBOLIC = "symbolic"              # Image represents abstract concept
    DECORATIVE = "decorative"          # Image adds aesthetic, not info
    EVIDENTIAL = "evidential"          # Image as proof/documentation


class VisualFrame(Enum):
    PROTEST = "protest"                # Crowds, signs, resistance
    VIOLENCE = "violence"              # Conflict, injuries, destruction
    HUMANITARIAN = "humanitarian"      # Victims, suffering, grief
    HOPE = "hope"                      # Celebration, unity, victory
    AUTHORITY = "authority"            # Officials, police, institutions
    EVERYDAY = "everyday"              # Normal life, domestic
    DOCUMENTARY = "documentary"        # Screenshots, data, maps


class MemeType(Enum):
    REACTION = "reaction"              # Express emotion to content
    OBJECT_LABELING = "object_labeling"  # Assign meaning to elements
    TEXT_HEAVY = "text_heavy"          # Multiline text with image
    DEEP_FRIED = "deep_fried"          # Intentionally degraded
    FORMAT_SPECIFIC = "format_specific"  # Platform conventions


@dataclass
class ImageAnalysis:
    """Container for image analysis results."""
    image_type: str  # photograph, illustration, screenshot, meme
    visual_frame: Optional[str] = None
    key_elements: List[str] = field(default_factory=list)
    faces_detected: int = 0
    dominant_emotion: Optional[str] = None
    text_in_image: bool = False
    ocr_text: Optional[str] = None
    color_mood: Optional[str] = None
    confidence: float = 0.0
    
    def to_dict(self):
        return asdict(self)


@dataclass
class MultimodalPost:
    """Container for multimodal post analysis."""
    post_id: str
    platform: str
    # Text components
    caption: Optional[str] = None
    ocr_text: Optional[str] = None
    hashtags: List[str] = field(default_factory=list)
    mentions: List[str] = field(default_factory=list)
    # Image components
    image_analysis: Optional[ImageAnalysis] = None
    # Combined analysis
    image_text_relationship: Optional[str] = None
    relationship_explanation: Optional[str] = None
    combined_frame: Optional[str] = None
    combined_valence: Optional[str] = None
    combined_arousal: Optional[str] = None
    # Metadata
    confidence: float = 0.0
    flags: List[str] = field(default_factory=list)
    
    def to_dict(self):
        d = asdict(self)
        if self.image_analysis:
            d['image_analysis'] = self.image_analysis.to_dict()
        return d


@dataclass 
class MemeAnalysis:
    """Container for meme analysis."""
    template_name: Optional[str] = None
    template_id: Optional[str] = None
    meme_type: Optional[str] = None
    text_slots: Dict[str, str] = field(default_factory=dict)
    sentiment: Optional[str] = None
    political_valence: Optional[str] = None
    virality_potential: Optional[str] = None
    
    def to_dict(self):
        return asdict(self)


@dataclass
class VideoAnalysis:
    """Container for video analysis."""
    duration_seconds: float = 0.0
    format: Optional[str] = None  # original, duet, stitch, etc.
    keyframes: List[ImageAnalysis] = field(default_factory=list)
    text_overlays: List[str] = field(default_factory=list)
    transitions: List[str] = field(default_factory=list)
    sound_id: Optional[str] = None
    sound_name: Optional[str] = None
    
    def to_dict(self):
        d = asdict(self)
        d['keyframes'] = [kf.to_dict() for kf in self.keyframes]
        return d


# Visual frame indicators for classification
VISUAL_FRAME_INDICATORS = {
    VisualFrame.PROTEST: [
        "crowd", "protest sign", "banner", "raised fist", "march",
        "demonstration", "chanting", "megaphone", "gathering"
    ],
    VisualFrame.VIOLENCE: [
        "injury", "blood", "weapon", "fire", "destruction", "clash",
        "tear gas", "smoke", "broken", "damage"
    ],
    VisualFrame.HUMANITARIAN: [
        "crying", "grief", "mourning", "victim", "hospital", "medical",
        "child", "elderly", "suffering", "funeral"
    ],
    VisualFrame.HOPE: [
        "celebration", "smile", "unity", "victory sign", "embrace",
        "flag waving", "joy", "optimism", "sunrise", "rainbow"
    ],
    VisualFrame.AUTHORITY: [
        "police", "military", "official", "uniform", "government building",
        "riot gear", "institution", "court", "parliament"
    ],
    VisualFrame.EVERYDAY: [
        "home", "family", "work", "street scene", "shop", "school",
        "normal activity", "domestic", "routine"
    ],
    VisualFrame.DOCUMENTARY: [
        "screenshot", "graph", "chart", "map", "document", "headline",
        "data visualization", "news clip", "text overlay"
    ]
}

# Common meme templates
KNOWN_MEME_TEMPLATES = {
    "drake_approve": ["Drake Hotline Bling", "Drake Approve/Disapprove"],
    "distracted_boyfriend": ["Distracted Boyfriend", "Man Looking at Other Woman"],
    "two_buttons": ["Two Buttons", "Daily Struggle"],
    "expanding_brain": ["Expanding Brain", "Galaxy Brain"],
    "woman_yelling_cat": ["Woman Yelling at Cat", "Smudge"],
    "change_my_mind": ["Change My Mind", "Steven Crowder"],
    "is_this": ["Is This a Pigeon", "Butterfly Man"],
    "bernie_sanders": ["Bernie Sanders Mittens", "Bernie Chair"],
    "surprised_pikachu": ["Surprised Pikachu"],
    "stonks": ["Stonks", "Meme Man"],
}


def extract_hashtags(text: str) -> List[str]:
    """Extract hashtags from text."""
    import re
    return re.findall(r'#\w+', text)


def extract_mentions(text: str) -> List[str]:
    """Extract @mentions from text."""
    import re
    return re.findall(r'@\w+', text)


def image_to_base64(image_path: str) -> str:
    """Convert image file to base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def extract_keyframes_ffmpeg(
    video_path: str,
    output_dir: str,
    method: str = "scene_change",
    max_frames: int = 10
) -> List[str]:
    """
    Extract keyframes from video using ffmpeg.
    
    Args:
        video_path: Path to video file
        output_dir: Directory to save frames
        method: 'scene_change', 'uniform', or 'peak_motion'
        max_frames: Maximum frames to extract
    
    Returns:
        List of paths to extracted frame images
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_pattern = str(output_dir / "frame_%03d.jpg")
    
    if method == "scene_change":
        # Extract frames at scene changes
        cmd = [
            "ffmpeg", "-i", video_path,
            "-vf", f"select='gt(scene,0.3)',setpts=N/FRAME_RATE/TB",
            "-frames:v", str(max_frames),
            "-vsync", "vfr",
            output_pattern
        ]
    elif method == "uniform":
        # Extract frames at uniform intervals
        cmd = [
            "ffmpeg", "-i", video_path,
            "-vf", f"fps=fps=1/{max_frames}:round=up",
            "-frames:v", str(max_frames),
            output_pattern
        ]
    else:
        raise ValueError(f"Unknown method: {method}")
    
    try:
        subprocess.run(cmd, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg error: {e.stderr.decode()}")
        return []
    
    # Return list of created frame files
    frames = sorted(output_dir.glob("frame_*.jpg"))
    return [str(f) for f in frames]


def get_video_duration(video_path: str) -> float:
    """Get video duration in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, check=True)
        return float(result.stdout.decode().strip())
    except (subprocess.CalledProcessError, ValueError):
        return 0.0


class MultimodalCoder:
    """
    Main interface for multimodal content coding.
    
    Note: Full implementation requires vision model API integration.
    This provides the framework and heuristic fallbacks.
    """
    
    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        self.vision_available = False  # Set True when API configured
    
    def analyze_image(
        self,
        image_path: str,
        context: Optional[str] = None
    ) -> ImageAnalysis:
        """
        Analyze a single image.
        
        Args:
            image_path: Path to image file
            context: Optional text context for interpretation
        
        Returns:
            ImageAnalysis object
        """
        # Placeholder - in production, call vision API
        # This returns a template for the expected output structure
        
        return ImageAnalysis(
            image_type="photograph",
            visual_frame=None,  # Would be classified by vision model
            key_elements=[],    # Would be extracted by vision model
            faces_detected=0,   # Would be detected by vision model
            dominant_emotion=None,
            text_in_image=False,
            ocr_text=None,
            color_mood=None,
            confidence=0.0
        )
    
    def classify_visual_frame(
        self,
        image_description: str
    ) -> Tuple[VisualFrame, float]:
        """
        Classify visual frame from image description.
        
        Heuristic approach using keyword matching.
        For production, use vision model directly.
        """
        description_lower = image_description.lower()
        
        scores = {}
        for frame, indicators in VISUAL_FRAME_INDICATORS.items():
            score = sum(1 for ind in indicators if ind in description_lower)
            scores[frame] = score
        
        if not any(scores.values()):
            return VisualFrame.EVERYDAY, 0.3
        
        best_frame = max(scores, key=scores.get)
        confidence = min(scores[best_frame] / 3.0, 1.0)  # Normalize
        
        return best_frame, confidence
    
    def classify_image_text_relationship(
        self,
        text: str,
        image_description: str
    ) -> Tuple[ImageTextRelationship, str]:
        """
        Classify relationship between text and image.
        
        Args:
            text: Post text/caption
            image_description: Description of image content
        
        Returns:
            (relationship_type, explanation)
        """
        text_lower = text.lower()
        image_lower = image_description.lower()
        
        # Simple heuristics - production would use LLM reasoning
        
        # Check for evidential markers
        if any(kw in text_lower for kw in ["proof", "evidence", "screenshot", "look at this"]):
            return ImageTextRelationship.EVIDENTIAL, "Text presents image as evidence"
        
        # Check for symbolic language
        if any(kw in text_lower for kw in ["represents", "symbolizes", "stands for", "like a"]):
            return ImageTextRelationship.SYMBOLIC, "Text uses symbolic/metaphorical language"
        
        # Check for irony markers
        if any(kw in text_lower for kw in ["sure", "totally", "definitely"]) and "!" in text:
            return ImageTextRelationship.CONTRADICTORY, "Possible ironic tone detected"
        
        # Check for direct reference
        common_words = set(text_lower.split()) & set(image_lower.split())
        if len(common_words) > 3:
            return ImageTextRelationship.ILLUSTRATIVE, "Image depicts text content"
        
        # Default to complementary
        return ImageTextRelationship.COMPLEMENTARY, "Image adds context to text"
    
    def code_post(
        self,
        text: str,
        image_path: Optional[str] = None,
        image_description: Optional[str] = None,
        platform: str = "twitter",
        post_id: str = "unknown"
    ) -> MultimodalPost:
        """
        Code a multimodal post.
        
        Args:
            text: Post text/caption
            image_path: Path to image file (optional)
            image_description: Pre-extracted image description (optional)
            platform: Social media platform
            post_id: Unique post identifier
        
        Returns:
            MultimodalPost object with all codings
        """
        # Extract text elements
        hashtags = extract_hashtags(text)
        mentions = extract_mentions(text)
        
        # Analyze image if provided
        image_analysis = None
        if image_path:
            image_analysis = self.analyze_image(image_path, context=text)
        
        # Classify image-text relationship
        img_text_rel = None
        rel_explanation = None
        if image_description or (image_analysis and image_analysis.key_elements):
            desc = image_description or " ".join(image_analysis.key_elements)
            rel, explanation = self.classify_image_text_relationship(text, desc)
            img_text_rel = rel.value
            rel_explanation = explanation
        
        # Classify visual frame
        combined_frame = None
        if image_description:
            frame, conf = self.classify_visual_frame(image_description)
            combined_frame = frame.value
        
        # Determine flags
        flags = []
        if not image_path and not image_description:
            flags.append("no_image")
        if len(text) < 10:
            flags.append("minimal_text")
        
        return MultimodalPost(
            post_id=post_id,
            platform=platform,
            caption=text,
            hashtags=hashtags,
            mentions=mentions,
            image_analysis=image_analysis,
            image_text_relationship=img_text_rel,
            relationship_explanation=rel_explanation,
            combined_frame=combined_frame,
            flags=flags
        )
    
    def analyze_meme(
        self,
        image_path: str,
        ocr_text: Optional[str] = None
    ) -> MemeAnalysis:
        """
        Analyze a meme image.
        
        Args:
            image_path: Path to meme image
            ocr_text: Pre-extracted text from meme (optional)
        
        Returns:
            MemeAnalysis object
        """
        # Placeholder - production would use vision model for template matching
        return MemeAnalysis(
            template_name=None,
            template_id=None,
            meme_type=MemeType.TEXT_HEAVY.value,
            text_slots={},
            sentiment=None,
            political_valence=None,
            virality_potential="unknown"
        )
    
    def extract_keyframes(
        self,
        video_path: str,
        method: str = "scene_change",
        max_frames: int = 10,
        output_dir: str = "/tmp/keyframes"
    ) -> List[str]:
        """
        Extract keyframes from video.
        
        Args:
            video_path: Path to video file
            method: Extraction method
            max_frames: Maximum frames to extract
            output_dir: Where to save frames
        
        Returns:
            List of paths to extracted frame images
        """
        return extract_keyframes_ffmpeg(
            video_path=video_path,
            output_dir=output_dir,
            method=method,
            max_frames=max_frames
        )
    
    def analyze_video(
        self,
        video_path: str,
        extract_audio: bool = False,
        max_keyframes: int = 5
    ) -> VideoAnalysis:
        """
        Analyze a video (e.g., TikTok).
        
        Args:
            video_path: Path to video file
            extract_audio: Whether to analyze audio/sound
            max_keyframes: Max keyframes to analyze
        
        Returns:
            VideoAnalysis object
        """
        duration = get_video_duration(video_path)
        
        # Extract and analyze keyframes
        frame_paths = self.extract_keyframes(
            video_path,
            max_frames=max_keyframes
        )
        
        keyframe_analyses = []
        for frame_path in frame_paths:
            analysis = self.analyze_image(frame_path)
            keyframe_analyses.append(analysis)
        
        return VideoAnalysis(
            duration_seconds=duration,
            format="original",  # Would detect duet/stitch in production
            keyframes=keyframe_analyses,
            text_overlays=[],  # Would use OCR in production
            transitions=[],     # Would detect in production
            sound_id=None,
            sound_name=None
        )
    
    def batch_code(
        self,
        posts: List[Dict],
        text_field: str = "text",
        image_field: str = "image_path",
        platform: str = "twitter"
    ) -> List[MultimodalPost]:
        """
        Code multiple posts in batch.
        
        Args:
            posts: List of post dicts
            text_field: Key for text content
            image_field: Key for image path
            platform: Platform name
        
        Returns:
            List of MultimodalPost objects
        """
        results = []
        for i, post in enumerate(posts):
            coded = self.code_post(
                text=post.get(text_field, ""),
                image_path=post.get(image_field),
                platform=platform,
                post_id=post.get("id", str(i))
            )
            results.append(coded)
        
        return results
    
    def generate_coding_prompt(
        self,
        text: str,
        image_base64: Optional[str] = None,
        codes_requested: List[str] = None
    ) -> str:
        """
        Generate a prompt for vision model coding.
        
        Args:
            text: Post text
            image_base64: Base64-encoded image
            codes_requested: Which codes to generate
        
        Returns:
            Formatted prompt for vision model
        """
        codes = codes_requested or [
            "visual_frame", "image_text_relationship", 
            "emotion", "key_elements"
        ]
        
        prompt = f"""Analyze this social media post.

TEXT: {text}

[IMAGE ATTACHED]

Please provide:
"""
        
        code_instructions = {
            "visual_frame": "1. VISUAL_FRAME: Classify the dominant visual frame (PROTEST, VIOLENCE, HUMANITARIAN, HOPE, AUTHORITY, EVERYDAY, DOCUMENTARY)",
            "image_text_relationship": "2. IMAGE_TEXT_REL: How does the image relate to text? (ILLUSTRATIVE, COMPLEMENTARY, CONTRADICTORY, SYMBOLIC, DECORATIVE, EVIDENTIAL)",
            "emotion": "3. EMOTION: What emotion does the image convey? (joy, anger, sadness, fear, surprise, neutral)",
            "key_elements": "4. KEY_ELEMENTS: List 3-5 key visual elements",
            "ocr": "5. OCR_TEXT: Any text visible in the image"
        }
        
        for code in codes:
            if code in code_instructions:
                prompt += code_instructions[code] + "\n"
        
        prompt += "\nProvide output as JSON."
        
        return prompt


# Convenience functions for common operations

def code_instagram_post(
    caption: str,
    image_path: str,
    post_id: str = "unknown"
) -> MultimodalPost:
    """Code an Instagram post."""
    coder = MultimodalCoder()
    return coder.code_post(
        text=caption,
        image_path=image_path,
        platform="instagram",
        post_id=post_id
    )


def code_tweet_with_image(
    tweet_text: str,
    image_path: str,
    tweet_id: str = "unknown"
) -> MultimodalPost:
    """Code a tweet with attached image."""
    coder = MultimodalCoder()
    return coder.code_post(
        text=tweet_text,
        image_path=image_path,
        platform="twitter",
        post_id=tweet_id
    )


def analyze_tiktok(
    video_path: str,
    max_keyframes: int = 5
) -> VideoAnalysis:
    """Analyze a TikTok video."""
    coder = MultimodalCoder()
    return coder.analyze_video(
        video_path=video_path,
        max_keyframes=max_keyframes
    )


if __name__ == "__main__":
    # Demo
    coder = MultimodalCoder()
    
    print("=== Visual Frame Classification ===")
    descriptions = [
        "Large crowd holding signs marching down the street with raised fists",
        "Screenshot of a tweet with engagement statistics",
        "Person crying at a funeral with flowers"
    ]
    
    for desc in descriptions:
        frame, conf = coder.classify_visual_frame(desc)
        print(f"'{desc[:50]}...' -> {frame.value} (conf: {conf:.2f})")
    
    print("\n=== Image-Text Relationship ===")
    pairs = [
        ("Protesters flood the streets!", "large crowd marching with signs"),
        ("Look at this evidence of fraud", "screenshot of document"),
        ("What a beautiful day!", "person looking sad in rain")
    ]
    
    for text, img_desc in pairs:
        rel, explanation = coder.classify_image_text_relationship(text, img_desc)
        print(f"Text: '{text}' + Image: '{img_desc[:30]}' -> {rel.value}")
    
    print("\n=== Full Post Coding ===")
    post = coder.code_post(
        text="Standing together for justice ✊ #MahsaAmini #IranProtests @amnesty",
        image_description="Crowd of protesters with signs, raised fists, daytime",
        platform="twitter",
        post_id="12345"
    )
    print(json.dumps(post.to_dict(), indent=2, default=str))
