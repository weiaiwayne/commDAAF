# Multimodal Coder Skill

Code images, videos, and image-text combinations in social media content.

## When to Use

- Analyzing visual social media content (Instagram, TikTok, memes)
- Studying image-text relationships in posts
- Coding visual frames in news/protest imagery
- Extracting information from video content
- Analyzing meme templates and variations

## Capabilities

1. **Image Frame Analysis** - Visual framing (what's shown/not shown)
2. **Image-Text Relationship** - How visuals relate to text
3. **Meme Template Detection** - Identify and classify meme formats
4. **Emotion/Affect Detection** - Facial expressions, visual mood
5. **Video Keyframe Extraction** - Sample representative frames
6. **Platform-Specific Formats** - TikTok duets, IG carousels, Twitter cards

## Image-Text Relationships

| Relationship | Definition | Example |
|--------------|------------|---------|
| **Illustrative** | Image depicts what text describes | Tweet about protest + photo of crowd |
| **Complementary** | Image adds information not in text | Text: "RIP" + photo of person |
| **Contradictory** | Image contradicts text (irony/sarcasm) | "Great day!" + crying face |
| **Symbolic** | Image represents abstract concept | Freedom + bird flying |
| **Decorative** | Image adds aesthetic, not information | Any post + stock photo |
| **Evidential** | Image as proof/documentation | Claim + screenshot |

## Visual Frame Categories

Adapted from news framing literature for social media:

| Frame | Visual Indicators |
|-------|-------------------|
| **Protest/Resistance** | Crowds, signs, raised fists, confrontation |
| **Violence/Conflict** | Injuries, weapons, destruction, clashes |
| **Humanitarian** | Victims, suffering, grief, medical care |
| **Hope/Victory** | Celebrations, unity symbols, smiles |
| **Authority** | Officials, police, institutional settings |
| **Everyday Life** | Normal activities, domestic scenes |
| **Documentary** | Screenshots, data visualizations, maps |

## Usage

### Basic: Single Image Analysis

```
Analyze this protest image for:
1. Visual frame (what is emphasized?)
2. Emotional tone (affect conveyed)
3. Key visual elements
4. What is NOT shown (framing choices)
```

### Advanced: Image-Text Coding

```
Code this tweet with image:
TEXT: "The revolution will not be televised. It will be tweeted."
IMAGE: [uploaded image]

Output:
1. Text frame: HOPE / CALL_TO_ACTION
2. Visual frame: [depends on image]
3. Image-text relationship: [classify]
4. Combined meaning: [synthesis]
```

### Batch Processing

```
Process these 50 Instagram posts:
1. Extract text (captions + OCR on images)
2. Classify visual frame
3. Code image-text relationship
4. Extract hashtags and mentions
5. Flag posts requiring manual review
```

## Output Format

```json
{
  "post_id": "12345",
  "platform": "instagram",
  "text": {
    "caption": "Standing together for justice ✊",
    "ocr_text": "WOMAN LIFE FREEDOM",
    "hashtags": ["#MahsaAmini", "#IranProtests"],
    "mentions": []
  },
  "image": {
    "type": "photograph",
    "visual_frame": "PROTEST",
    "key_elements": ["crowd", "signs", "raised_fists"],
    "faces_detected": 15,
    "dominant_emotion": "determination",
    "color_mood": "warm",
    "text_in_image": true
  },
  "image_text_relationship": "COMPLEMENTARY",
  "relationship_explanation": "Image shows protest scene; text expresses solidarity",
  "combined_frame": "SOLIDARITY",
  "combined_valence": "positive",
  "combined_arousal": "high",
  "confidence": 0.85,
  "flags": []
}
```

## Meme Analysis

### Template Detection
```python
meme = MultimodalCoder().analyze_meme(image)
# Returns:
{
  "template": "Drake Hotline Bling",
  "template_id": "drake_approve",
  "top_text_slot": "Reading the news",
  "bottom_text_slot": "Reading memes about the news",
  "sentiment": "humorous",
  "political_valence": "neutral",
  "virality_potential": "medium"
}
```

### Common Meme Types
- **Reaction images** - Express emotion to content
- **Object labeling** - Assign meaning to template elements
- **Text-heavy** - Multiline text with image
- **Deep-fried/Ironic** - Intentionally degraded
- **Format-specific** - Platform conventions (TikTok sounds, etc.)

## Video Processing

### Keyframe Extraction
```python
frames = MultimodalCoder().extract_keyframes(
    video_path="video.mp4",
    method="scene_change",  # or "uniform", "peak_motion"
    max_frames=10
)
# Returns list of representative frames for coding
```

### TikTok-Specific
```python
tiktok = MultimodalCoder().analyze_tiktok(
    video_path="tiktok.mp4",
    include_audio=True
)
# Returns:
{
  "format": "duet",  # or "stitch", "original", "green_screen"
  "sound_id": "original_sound_12345",
  "sound_name": "Woman Life Freedom chant",
  "text_overlays": ["When they tell us to be quiet"],
  "visual_frames": [...],
  "transitions": ["cut", "zoom"],
  "duration_seconds": 15
}
```

## Integration with CommDAAF Pipeline

```python
from commdaaf import MultimodalCoder

coder = MultimodalCoder(model="gpt-4o")  # or "claude-3.5-sonnet"

# Single post
result = coder.code_post(
    text="The revolution continues",
    image_path="protest.jpg",
    platform="twitter"
)

# Batch processing
results = coder.batch_code(
    posts=instagram_posts,
    codes=["visual_frame", "image_text_rel", "emotion"],
    output_format="json"
)

# Video keyframes
frames = coder.extract_keyframes(
    video="tiktok.mp4",
    method="scene_change",
    max_frames=5
)
coded_frames = coder.code_images(frames)

# Platform-specific
tiktok_analysis = coder.analyze_tiktok(
    video="video.mp4",
    extract_sound=True
)
```

## Best Practices

### 1. Start with Text
Code text first, then image, then relationship. Text often provides framing context.

### 2. Note What's Absent
Visual framing includes what is NOT shown. Document exclusions.

### 3. Consider Platform Conventions
Instagram aesthetics ≠ Twitter documentation ≠ TikTok entertainment

### 4. Handle OCR Carefully
Text in images may be in multiple languages, stylized, or partially visible.

### 5. Flag Ambiguous Cases
Some images defy simple categorization. Flag for human review.

### 6. Document Your Decisions
Image coding is inherently subjective. Record your reasoning.

## Reliability Considerations

Visual content analysis typically has lower inter-coder reliability than text:

| Content Type | Expected κ Range |
|--------------|------------------|
| Text frames | 0.60 - 0.80 |
| Visual frames | 0.50 - 0.70 |
| Image-text relationship | 0.55 - 0.75 |
| Emotion detection | 0.45 - 0.65 |

**Recommendations:**
- Use detailed coding guides with visual examples
- Code clear cases first, ambiguous cases separately
- Report reliability by category
- Consider majority voting across multiple coders/models

## Limitations

- Vision models may miss cultural/contextual cues
- OCR struggles with stylized text
- Video analysis is computationally expensive
- Meme templates evolve rapidly
- Platform-specific formats require specialized handling
- Visual irony/sarcasm is difficult to detect

## Model Selection

| Model | Strengths | Weaknesses |
|-------|-----------|------------|
| GPT-4o | Excellent image understanding, OCR | Cost, rate limits |
| Claude 3.5 Sonnet | Good reasoning, nuance | Slightly lower image detail |
| Gemini 1.5 Pro | Long video support | May miss subtle cues |
| Llama 3.2 Vision | Open source, fast | Less nuanced than proprietary |

## References

- Brantner, C., Lobinger, K., & Wetzstein, I. (2011). Effects of visual framing.
- Highfield, T., & Leaver, T. (2016). Instagrammatics and digital methods.
- Shifman, L. (2014). Memes in digital culture.
- Zeng, J., & Kaye, D. B. V. (2022). From content moderation to visibility moderation.
