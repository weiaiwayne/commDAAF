#!/usr/bin/env python3
"""
CommDAAF Codebook Generator

Generates operational coding schemes from theoretical constructs.
"""

import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class CodebookEntry:
    """A single construct in the codebook."""
    construct: str
    definition: str
    theoretical_source: str
    decision_rules: List[str]
    anchors: Dict[str, List[str]]
    multilingual_anchors: Optional[Dict[str, List[str]]] = None
    reliability_notes: Optional[str] = None
    common_confusions: Optional[List[str]] = None
    
    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass  
class Codebook:
    """Complete codebook for a content analysis project."""
    name: str
    version: str
    created: str
    constructs: List[CodebookEntry]
    decision_hierarchy: Optional[List[str]] = None
    global_rules: Optional[List[str]] = None
    
    def to_dict(self):
        d = asdict(self)
        d['constructs'] = [c.to_dict() for c in self.constructs]
        return {k: v for k, v in d.items() if v is not None}
    
    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
    
    def to_commdaaf_prompt(self) -> str:
        """Generate a CommDAAF-compliant coding prompt from this codebook."""
        lines = []
        
        # Header
        lines.append("# CONTENT ANALYSIS CODING INSTRUCTIONS")
        lines.append(f"\nCodebook: {self.name} (v{self.version})")
        lines.append(f"Generated: {self.created}")
        lines.append("")
        
        # Task definition
        lines.append("## TASK")
        lines.append("For each text, assign ONE primary code from the categories below.")
        lines.append("Also code valence (positive/negative/neutral) and arousal (low/medium/high).")
        lines.append("")
        
        # Output format
        lines.append("## OUTPUT FORMAT")
        lines.append("Return JSON array with one object per text:")
        lines.append("```json")
        lines.append('[{"id": "...", "code": "...", "valence": "...", "arousal": "...", "confidence": 0.0-1.0, "reasoning": "..."}]')
        lines.append("```")
        lines.append("")
        
        # Global rules
        if self.global_rules:
            lines.append("## GLOBAL RULES")
            for rule in self.global_rules:
                lines.append(f"- {rule}")
            lines.append("")
        
        # Decision hierarchy
        if self.decision_hierarchy:
            lines.append("## DECISION HIERARCHY (when codes overlap)")
            for i, code in enumerate(self.decision_hierarchy, 1):
                lines.append(f"{i}. {code}")
            lines.append("")
        
        # Construct definitions
        lines.append("## CATEGORIES")
        for entry in self.constructs:
            lines.append(f"\n### {entry.construct}")
            lines.append(f"**Definition:** {entry.definition}")
            lines.append(f"**Source:** {entry.theoretical_source}")
            
            if entry.decision_rules:
                lines.append("\n**Decision Rules:**")
                for rule in entry.decision_rules:
                    lines.append(f"- {rule}")
            
            if entry.anchors:
                if 'prototypical' in entry.anchors:
                    lines.append("\n**Examples (YES):**")
                    for ex in entry.anchors['prototypical']:
                        lines.append(f'- "{ex}"')
                
                if 'counter_examples' in entry.anchors:
                    lines.append("\n**Counter-examples (NO):**")
                    for ex in entry.anchors['counter_examples']:
                        lines.append(f'- "{ex}"')
            
            if entry.multilingual_anchors:
                lines.append("\n**Multilingual Examples:**")
                for lang, examples in entry.multilingual_anchors.items():
                    lines.append(f"- [{lang}]: {'; '.join(examples)}")
            
            if entry.common_confusions:
                lines.append(f"\n**Common confusions:** {', '.join(entry.common_confusions)}")
        
        return "\n".join(lines)


# Pre-built codebook templates

PROTEST_FRAMES_TEMPLATE = Codebook(
    name="Protest Movement Frames",
    version="0.5",
    created=datetime.now().isoformat()[:10],
    decision_hierarchy=[
        "CALL_TO_ACTION (if explicit appeal to act)",
        "INJUSTICE (if perpetrator named/implied)",
        "CONFLICT (if both sides active)",
        "HUMANITARIAN (if victim focus without blame)",
        "HOPE (if future-oriented optimism)",
        "SOLIDARITY (if collective identity emphasis)",
        "INFORMATIONAL (if neutral factual update)"
    ],
    global_rules=[
        "Assign ONE primary frame per text",
        "When multiple frames present, use decision hierarchy",
        "Code what is EMPHASIZED, not merely mentioned",
        "Consider the overall thrust, not isolated words"
    ],
    constructs=[
        CodebookEntry(
            construct="SOLIDARITY",
            definition="Emphasizes collective identity, unity, shared struggle, or group membership",
            theoretical_source="Polletta & Jasper 2001; identity framing",
            decision_rules=[
                "Look for: 'we', 'us', 'together', 'united', collective pronouns",
                "Emphasizes belonging over action or blame",
                "Default frame when content expresses group membership without other dominant elements"
            ],
            anchors={
                "prototypical": [
                    "We stand together with the women of Iran",
                    "United we are unstoppable #WomanLifeFreedom",
                    "Iranian diaspora rises as one"
                ],
                "counter_examples": [
                    "Share this now! (= CALL_TO_ACTION)",
                    "The regime must pay (= INJUSTICE)"
                ]
            },
            common_confusions=["HOPE (future-focused)", "CALL_TO_ACTION (action-focused)"]
        ),
        CodebookEntry(
            construct="INJUSTICE",
            definition="Identifies wrongdoing and explicitly assigns blame to a perpetrator",
            theoretical_source="Gamson 1992; diagnostic framing",
            decision_rules=[
                "Must name or clearly imply a responsible actor (regime, police, government)",
                "Prioritize over HUMANITARIAN when perpetrator is explicit",
                "Distinguish from CONFLICT: INJUSTICE = one-sided blame, CONFLICT = two-sided clash"
            ],
            anchors={
                "prototypical": [
                    "The Islamic Republic killed Mahsa Amini",
                    "Khamenei has blood on his hands",
                    "These murderers in uniform must face justice"
                ],
                "counter_examples": [
                    "She died in custody (no perpetrator = HUMANITARIAN)",
                    "Protesters clashed with security forces (two-sided = CONFLICT)"
                ]
            },
            common_confusions=["HUMANITARIAN (victim-focused)", "CONFLICT (both sides active)"]
        ),
        CodebookEntry(
            construct="CONFLICT",
            definition="Emphasizes active clash, confrontation, or struggle between two or more parties",
            theoretical_source="Semetko & Valkenburg 2000; conflict news frame",
            decision_rules=[
                "Both sides must be portrayed as ACTIVE (not just victim + perpetrator)",
                "Look for: 'clash', 'fight', 'battle', 'versus', 'confront'",
                "Distinguish from INJUSTICE: conflict implies agency on both sides"
            ],
            anchors={
                "prototypical": [
                    "Protesters clash with riot police in Tehran",
                    "Running battles between demonstrators and security forces",
                    "The streets have become a warzone"
                ],
                "counter_examples": [
                    "Police killed protesters (one-sided = INJUSTICE)",
                    "Protesters gathered peacefully (no clash = SOLIDARITY)"
                ]
            },
            reliability_notes="Low reliability in our study (33% 3-way agreement); use with caution",
            common_confusions=["INJUSTICE (one-sided blame)"]
        ),
        CodebookEntry(
            construct="HUMANITARIAN",
            definition="Focuses on human suffering, victims, or humanitarian concern without emphasizing perpetrator",
            theoretical_source="Iyengar 1991; episodic/victim framing",
            decision_rules=[
                "Emphasizes the victim's experience, not who caused it",
                "Look for: sympathy appeals, suffering descriptions, victim identification",
                "If perpetrator is named/blamed, use INJUSTICE instead"
            ],
            anchors={
                "prototypical": [
                    "She was only 22 years old with her whole life ahead",
                    "Families mourn their children lost to violence",
                    "The human cost of this crisis is devastating"
                ],
                "counter_examples": [
                    "The regime killed her (perpetrator named = INJUSTICE)",
                    "We must help them (action appeal = CALL_TO_ACTION)"
                ]
            },
            common_confusions=["INJUSTICE (adds perpetrator)"]
        ),
        CodebookEntry(
            construct="HOPE",
            definition="Expresses optimism, positive future vision, or belief in eventual success",
            theoretical_source="Snow & Benford 1988; prognostic framing",
            decision_rules=[
                "Future-oriented positive sentiment",
                "Look for: 'will win', 'freedom is coming', 'change is possible'",
                "Distinguish from SOLIDARITY: hope emphasizes future, solidarity emphasizes present unity"
            ],
            anchors={
                "prototypical": [
                    "The revolution will succeed",
                    "A free Iran is within reach",
                    "This generation will see change"
                ],
                "counter_examples": [
                    "We stand together (present = SOLIDARITY)",
                    "Fight for freedom (action = CALL_TO_ACTION)"
                ]
            },
            common_confusions=["SOLIDARITY (present-focused)", "CALL_TO_ACTION (action-focused)"]
        ),
        CodebookEntry(
            construct="INFORMATIONAL",
            definition="Neutral factual reporting, updates, or context without emotional framing",
            theoretical_source="Lee & Ma 2012; information utility",
            decision_rules=[
                "Primarily factual, not emotional or mobilizing",
                "Look for: news updates, statistics, context, explainers",
                "Can coexist with other elements but factual thrust dominates"
            ],
            anchors={
                "prototypical": [
                    "Update: Protests reported in 50+ cities across Iran",
                    "Background: Mahsa Amini was detained on September 13",
                    "Internet connectivity down 80% according to NetBlocks"
                ],
                "counter_examples": [
                    "Unbelievable—protests in 50 cities! (emotional = other frame)",
                    "50 cities and counting—join them! (mobilizing = CALL_TO_ACTION)"
                ]
            },
            common_confusions=["CALL_TO_ACTION (when update includes appeal)"]
        ),
        CodebookEntry(
            construct="CALL_TO_ACTION",
            definition="Explicit appeal to audience to do something—share, protest, donate, sign, contact",
            theoretical_source="Benford & Snow 2000; motivational framing",
            decision_rules=[
                "Must contain explicit appeal or imperative",
                "Look for: 'share this', 'retweet', 'sign petition', 'join us', 'donate'",
                "Prioritize over other frames when action appeal is the main thrust"
            ],
            anchors={
                "prototypical": [
                    "SHARE this thread to spread awareness",
                    "Call your representatives NOW",
                    "Sign the petition: [link]"
                ],
                "counter_examples": [
                    "We stand together (no action specified = SOLIDARITY)",
                    "The regime must fall (wish, not action = INJUSTICE/HOPE)"
                ]
            },
            common_confusions=["SOLIDARITY (collective but no action)", "HOPE (aspiration but no action)"]
        )
    ]
)


def generate_codebook(
    constructs: List[str],
    theory_sources: Dict[str, str],
    languages: List[str] = None,
    template: str = "protest_frames"
) -> Codebook:
    """
    Generate a codebook from specifications.
    
    Args:
        constructs: List of construct names to include
        theory_sources: Dict mapping constructs to theoretical sources
        languages: List of language codes for multilingual anchors
        template: Base template to use ('protest_frames' or 'custom')
    
    Returns:
        Codebook object
    """
    if template == "protest_frames":
        # Filter template to requested constructs
        filtered = [c for c in PROTEST_FRAMES_TEMPLATE.constructs 
                   if c.construct.lower() in [x.lower() for x in constructs]]
        
        return Codebook(
            name=PROTEST_FRAMES_TEMPLATE.name,
            version=PROTEST_FRAMES_TEMPLATE.version,
            created=datetime.now().isoformat()[:10],
            constructs=filtered,
            decision_hierarchy=[h for h in PROTEST_FRAMES_TEMPLATE.decision_hierarchy
                               if any(c.lower() in h.lower() for c in constructs)],
            global_rules=PROTEST_FRAMES_TEMPLATE.global_rules
        )
    else:
        raise ValueError(f"Unknown template: {template}")


def export_commdaaf_prompt(codebook: Codebook, output_path: str = None) -> str:
    """Export codebook as CommDAAF-compliant coding prompt."""
    prompt = codebook.to_commdaaf_prompt()
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(prompt)
    
    return prompt


if __name__ == "__main__":
    # Demo: generate and export protest frames codebook
    codebook = PROTEST_FRAMES_TEMPLATE
    
    print("=== Codebook JSON ===")
    print(codebook.to_json())
    
    print("\n\n=== CommDAAF Prompt ===")
    print(codebook.to_commdaaf_prompt())
