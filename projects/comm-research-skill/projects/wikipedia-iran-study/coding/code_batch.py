#!/usr/bin/env python3
"""
Code Wikipedia talk page excerpts for epistemic injustice using v2 rules.
"""

import json
import sys
from pathlib import Path

def code_entry(entry):
    """Code a single entry according to v2 rules."""
    content = entry.get('content', '').lower()
    
    # Initialize all codes to 0
    codes = {
        'testimonial_injustice': 0,
        'hermeneutical_injustice': 0,
        'epistemic_dispossession': 0,
        'policy_weaponization': 0,
        'naming_dispute': 0,
        'source_hierarchy': 0
    }
    
    reasoning_parts = []
    
    # 1. TESTIMONIAL_INJUSTICE: Person attacked/dismissed based on identity, experience, account age
    # Look for identity-based attacks
    identity_patterns = [
        'pro-iran account', 'pro-israel account', 'pro-palestinian account',
        'should be banned', 'vandal', 'troll', 'sock puppet',
        'is clearly a', 'you are a', 'you seem to be'
    ]
    
    # Look for account age/experience attacks
    experience_patterns = [
        'new editor', 'inexperienced', 'account age', 'days old',
        'edit count', 'number of edits'
    ]
    
    for pattern in identity_patterns + experience_patterns:
        if pattern in content:
            # Check if it's actually attacking someone
            if any(word in content for word in ['attack', 'dismiss', 'you should', 'you are']):
                codes['testimonial_injustice'] = 1
                reasoning_parts.append(f"Identity/experience-based language found")
                break
    
    # 2. HERMENEUTICAL_INJUSTICE: Terminology explicitly debated
    terminology_disputes = [
        'genocide', 'massacre', 'terror', 'horror', 'war vs conflict',
        'should be called', 'should be named', 'change to', 'rename to',
        'is not accurate', 'is misleading', 'is euphemistic'
    ]
    
    for term in terminology_disputes:
        if term in content:
            # Check if there's an actual dispute about the term
            dispute_indicators = ['dispute', 'debate', 'contested', 'should be', 'change']
            if any(indicator in content for indicator in dispute_indicators):
                codes['hermeneutical_injustice'] = 1
                reasoning_parts.append(f"Terminology dispute: '{term}'")
                break
    
    # 3. EPISTEMIC_DISPOSSESSION: Editor EXPLICITLY told they cannot participate due to EC/experience
    # V2 rule: EC template alone = 0
    # Must have explicit exclusion language
    exclusion_phrases = [
        'may not participate until', 'cannot participate until',
        'is not available to non-ec', 'must be ec',
        'only ec editors', 'restricted to ec', 'excluded from discussion'
    ]
    
    for phrase in exclusion_phrases:
        if phrase in content:
            codes['epistemic_dispossession'] = 1
            reasoning_parts.append(f"Explicit exclusion: '{phrase[:50]}...'")
            break
    
    # 4. POLICY_WEAPONIZATION: Policy used to SILENCE without substantive explanation
    # V2 rule: Routine 'not done' with guidance = 0
    # Must be policy used to shut down without help
    
    # Look for policy citations
    policy_patterns = ['wp:', 'per wp:', 'wikipedia:', 'violates']
    
    # Check if policy is used to shut down
    weaponization_indicators = [
        'stop', 'threat', 'will take to', 'i\'ll report',
        'enforced', 'not allowed', 'prohibited', 'blocked'
    ]
    
    # Check if there's helpful guidance
    helpful_guidance = [
        'please provide', 'here\'s why', 'see wp:', 'per policy',
        'because', 'reason is', 'explanation', 'guidance'
    ]
    
    has_policy = any(policy in content for policy in policy_patterns)
    has_weaponization = any(ind in content for ind in weaponization_indicators)
    has_guidance = any(guidance in content for guidance in helpful_guidance)
    
    # Check for "not done" with policy
    if 'not done' in content and has_policy:
        if has_weaponization and not has_guidance:
            codes['policy_weaponization'] = 1
            reasoning_parts.append("Policy used to silence without guidance")
        # V2 rule: "not done" with guidance = 0
        # (already set to 0)
    
    # Also check for explicit threats
    threat_patterns = ['take to ani', 'take to drn', 'will be reported', 'enforcement', 'blocked']
    if any(threat in content for threat in threat_patterns):
        codes['policy_weaponization'] = 1
        reasoning_parts.append("Policy threat detected")
    
    # 5. NAMING_DISPUTE: Article title or event name explicitly contested
    naming_patterns = [
        'should be called', 'should be named', 'rename to', 'change title',
        'why is this called', 'naming', 'what should this be called',
        'requested move', 'move discussion'
    ]
    
    for pattern in naming_patterns:
        if pattern in content:
            codes['naming_dispute'] = 1
            reasoning_parts.append(f"Naming dispute: '{pattern[:30]}...'")
            break
    
    # 6. SOURCE_HIERARCHY: Source CATEGORY challenged (national, ideological)
    # V2 rule: Standard RS reminder = 0
    # Must challenge source CATEGORY, not just request sources
    
    source_category_challenges = [
        'propaganda', 'is opposition', 'is biased', 'is state media',
        'is pro-', 'is anti-', 'is affiliated with',
        'is a regime mouthpiece', 'is a government mouthpiece',
        'is not credible because', 'is unreliable because'
    ]
    
    # Check for standard RS requests (not hierarchy)
    standard_rs_patterns = [
        'please provide a reliable source', 'need a reliable source',
        'provide sources', 'citations needed', 'reference needed',
        'per wp:rs', 'per reliable sources'
    ]
    
    # Check for actual category challenges
    for challenge in source_category_challenges:
        if challenge in content:
            codes['source_hierarchy'] = 1
            reasoning_parts.append(f"Source category challenged: '{challenge[:40]}...'")
            break
    
    # Check if it's just standard RS reminder (V2 rule: 0)
    # If it's just asking for sources without challenging category
    has_standard_rs = any(pattern in content for pattern in standard_rs_patterns)
    if has_standard_rs and codes['source_hierarchy'] == 0:
        # It's a standard RS reminder - leave as 0
        pass  # V2 rule applied
    
    # Build result
    reasoning = "Routine interaction" if not reasoning_parts else "; ".join(reasoning_parts)
    confidence = 0.85
    
    # Determine primary form if any code is 1
    primary_form = "none"
    if codes['testimonial_injustice'] == 1:
        primary_form = "testimonial_injustice"
    elif codes['hermeneutical_injustice'] == 1:
        primary_form = "hermeneutical_injustice"
    elif codes['epistemic_dispossession'] == 1:
        primary_form = "epistemic_dispossession"
    elif codes['policy_weaponization'] == 1:
        primary_form = "policy_weaponization"
    elif codes['naming_dispute'] == 1:
        primary_form = "naming_dispute"
    elif codes['source_hierarchy'] == 1:
        primary_form = "source_hierarchy"
    
    return {
        'id': entry.get('id'),
        'testimonial_injustice': codes['testimonial_injustice'],
        'hermeneutical_injustice': codes['hermeneutical_injustice'],
        'epistemic_dispossession': codes['epistemic_dispossession'],
        'policy_weaponization': codes['policy_weaponization'],
        'naming_dispute': codes['naming_dispute'],
        'source_hierarchy': codes['source_hierarchy'],
        'primary_form': primary_form,
        'confidence': confidence,
        'reasoning': reasoning
    }

def process_batch(input_file, output_file):
    """Process a batch of entries."""
    with open(input_file, 'r', encoding='utf-8') as f:
        entries = json.load(f)
    
    coded_entries = [code_entry(entry) for entry in entries]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(coded_entries, f, indent=2)
    
    print(f"Processed {len(coded_entries)} entries from {input_file} -> {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python code_batch.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_batch(input_file, output_file)
