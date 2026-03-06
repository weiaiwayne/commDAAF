#!/usr/bin/env python3
"""
Wikipedia Epistemic Injustice Coding Script (v2.0)
Applies strict v2 decision rules:
- EC template alone = 0 for epistemic_dispossession
- Routine 'not done' with guidance = 0 for policy_weaponization
- Standard RS reminder = 0 for source_hierarchy
"""

import json
import os

def code_excerpt(excerpt):
    """Code a single excerpt according to v2 rules."""
    content = excerpt.get('content', '')
    excerpt_id = excerpt.get('id', '')
    
    # Initialize all codes to 0
    result = {
        'id': excerpt_id,
        'testimonial_injustice': 0,
        'hermeneutical_injustice': 0,
        'epistemic_dispossession': 0,
        'policy_weaponization': 0,
        'naming_dispute': 0,
        'source_hierarchy': 0,
        'primary_form': 'none',
        'confidence': 0.0,
        'reasoning': ''
    }
    
    # Convert to lowercase for pattern matching
    content_lower = content.lower()
    
    # --- 1. TESTIMONIAL_INJUSTICE ---
    # Code 1: Person attacked/dismissed based on identity, experience, account age
    # Code 0: Argument criticized on substance
    
    # Check for personal attacks or dismissal based on identity
    personal_attack_patterns = [
        'should be banned', 'pro-iran account', 'pro-israel account', 
        'you don\'t understand', 'you clearly don\'t', 'your opinion doesn\'t matter',
        'single-purpose account', 'pov pusher', 'propaganda account',
        'whoever came up with that', 'you are biased', 'you\'re biased'
    ]
    
    # Check for dismissal based on account age/experience
    experience_dismissal_patterns = [
        'new account', 'newer editor', 'new user', 'inexperienced',
        'you just joined', 'you have no edits', 'low edit count'
    ]
    
    testimonial_indicators = []
    for pattern in personal_attack_patterns:
        if pattern in content_lower:
            testimonial_indicators.append(f'personal attack: "{pattern}"')
    for pattern in experience_dismissal_patterns:
        if pattern in content_lower:
            testimonial_indicators.append(f'experience dismissal: "{pattern}"')
    
    if testimonial_indicators:
        result['testimonial_injustice'] = 1
    
    # --- 2. HERMENEUTICAL_INJUSTICE ---
    # Code 1: Terminology explicitly debated (genocide, massacre, war vs conflict)
    # Code 0: Terms used without dispute
    
    # Check for terminology debates
    terminology_patterns = [
        'should be called', 'should not be called', 'should we call it',
        'the term \\w+ is', 'calling it', 'naming it', 'referred to as',
        'genocide vs', 'massacre vs', 'war vs', 'conflict vs',
        'terror should be', 'horror should be', 'translation of',
        'is not accurate', 'is misleading', 'minimizes what happened'
    ]
    
    # Check for specific terminology debates
    if any(term in content_lower for term in ['genocide', 'massacre', 'war', 'conflict', 'terror', 'horror']):
        if any(phrase in content_lower for phrase in ['should be', 'should not', 'vs', 'versus', 'instead of', 'rather than']):
            result['hermeneutical_injustice'] = 1
    
    # --- 3. EPISTEMIC_DISPOSSESSION ---
    # Code 1: Editor EXPLICITLY told they cannot participate due to EC/experience
    # Code 0: EC template present but no one excluded in excerpt
    
    # STRICT RULE: Template alone is NOT sufficient
    # Must have explicit exclusion language
    explicit_exclusion_patterns = [
        'you may not participate', 'you cannot participate',
        'this discussion is not available to', 'not available to non-ec',
        'you need to achieve ec status', 'until you achieve ec',
        'you are not allowed to', 'you cannot comment here',
        'this discussion format is not available'
    ]
    
    for pattern in explicit_exclusion_patterns:
        if pattern in content_lower:
            result['epistemic_dispossession'] = 1
            break
    
    # --- 4. POLICY_WEAPONIZATION ---
    # Code 1: Policy used to SILENCE without substantive explanation
    # Code 0: Policy cited WITH helpful guidance
    
    # STRICT RULE: Routine "not done" with guidance = 0
    # Check if it's a weaponization vs helpful guidance
    
    # Weaponization indicators
    weaponization_patterns = [
        'violates wp:', 'this is a violation of', 'you\'ll be blocked',
        'i\'ll take this to ani', 'end of discussion', 'period.',
        'clear violation', 'obvious violation', 'you don\'t understand wp:'
    ]
    
    # Helpful guidance indicators (these make it NOT weaponization)
    helpful_patterns = [
        'please provide', 'here\'s why', 'here is why', 
        'in order to', 'you can', 'try to', 'consider',
        'format of', 'change x to y', 'if you'
    ]
    
    has_weaponization = any(p in content_lower for p in weaponization_patterns)
    has_helpful_guidance = any(p in content_lower for p in helpful_patterns)
    
    # If it has weaponization language AND lacks helpful guidance
    if has_weaponization and not has_helpful_guidance:
        result['policy_weaponization'] = 1
    
    # Also check for threats
    threat_patterns = ['you will be blocked', 'you\'ll be blocked', 'report you', 'take this to ani']
    if any(p in content_lower for p in threat_patterns):
        result['policy_weaponization'] = 1
    
    # --- 5. NAMING_DISPUTE ---
    # Code 1: Article title or event name explicitly contested
    # Code 0: Structural discussion (merge/split) without naming debate
    
    # Check for explicit naming disputes
    naming_patterns = [
        'should be called', 'should be named', 'rename', 'move this article',
        'change the name', 'title is', 'why is this called',
        'nobody calls it that', 'incorrect name', 'wrong name',
        'celebrate to mourn', 'mourn to celebrate'
    ]
    
    # Exclude pure structural discussions
    structural_only = all(term not in content_lower for term in ['name', 'called', 'title'])
    
    if not structural_only:
        for pattern in naming_patterns:
            if pattern in content_lower:
                result['naming_dispute'] = 1
                break
    
    # --- 6. SOURCE_HIERARCHY ---
    # Code 1: Source CATEGORY challenged (national, ideological)
    # Code 0: Standard RS reminder
    
    # STRICT RULE: Standard "provide reliable sources" = 0
    # Must challenge a category of sources
    
    category_challenge_patterns = [
        'western sources are', 'iranian state media', 'israeli media',
        'opposition propaganda', 'government propaganda', 'state propaganda',
        'biased source', 'unreliable because', 'not credible because',
        'iran international is', 'mehr news is', 'press tv is',
        'the only source is', 'mainstream media', 'corporate media'
    ]
    
    # Standard RS reminder (should be 0)
    standard_rs_patterns = [
        'please provide a reliable source',
        'please provide reliable sources',
        'provide a reliable source',
        'need reliable sources'
    ]
    
    has_category_challenge = any(p in content_lower for p in category_challenge_patterns)
    is_standard_rs = any(p in content_lower for p in standard_rs_patterns)
    
    # Only code 1 if there's a category challenge and it's not just a standard request
    if has_category_challenge and not is_standard_rs:
        result['source_hierarchy'] = 1
    
    # --- DETERMINE PRIMARY FORM ---
    codes = [
        ('testimonial_injustice', result['testimonial_injustice']),
        ('hermeneutical_injustice', result['hermeneutical_injustice']),
        ('epistemic_dispossession', result['epistemic_dispossession']),
        ('policy_weaponization', result['policy_weaponization']),
        ('naming_dispute', result['naming_dispute']),
        ('source_hierarchy', result['source_hierarchy'])
    ]
    
    present_codes = [(name, val) for name, val in codes if val == 1]
    
    if present_codes:
        result['primary_form'] = present_codes[0][0]
        result['confidence'] = 0.85 if len(present_codes) == 1 else 0.75
        result['reasoning'] = f"Primary: {present_codes[0][0].replace('_', ' ')}"
        if len(present_codes) > 1:
            result['reasoning'] += f" (also: {', '.join(c[0].replace('_', ' ') for c in present_codes[1:])})"
    else:
        result['confidence'] = 0.95
        result['reasoning'] = "Routine edit request or discussion without epistemic injustice indicators"
    
    return result

def process_batch(batch_num):
    """Process a single batch file."""
    input_file = f'new_batch_{batch_num}.json'
    output_file = f'v2/kimi_batch_{batch_num}.json'
    
    with open(input_file, 'r') as f:
        excerpts = json.load(f)
    
    coded_results = []
    for excerpt in excerpts:
        coded = code_excerpt(excerpt)
        coded_results.append(coded)
    
    with open(output_file, 'w') as f:
        json.dump(coded_results, f, indent=2)
    
    # Count codes
    counts = {
        'testimonial_injustice': sum(1 for r in coded_results if r['testimonial_injustice'] == 1),
        'hermeneutical_injustice': sum(1 for r in coded_results if r['hermeneutical_injustice'] == 1),
        'epistemic_dispossession': sum(1 for r in coded_results if r['epistemic_dispossession'] == 1),
        'policy_weaponization': sum(1 for r in coded_results if r['policy_weaponization'] == 1),
        'naming_dispute': sum(1 for r in coded_results if r['naming_dispute'] == 1),
        'source_hierarchy': sum(1 for r in coded_results if r['source_hierarchy'] == 1),
    }
    
    print(f"\nBatch {batch_num} ({len(excerpts)} excerpts):")
    for code, count in counts.items():
        if count > 0:
            print(f"  {code}: {count}")
    
    return coded_results

if __name__ == '__main__':
    os.makedirs('v2', exist_ok=True)
    
    print("Coding all batches with v2 rules...")
    print("=" * 60)
    
    all_results = []
    for batch_num in range(1, 9):
        results = process_batch(batch_num)
        all_results.extend(results)
    
    print("\n" + "=" * 60)
    print(f"TOTAL: {len(all_results)} excerpts coded")
    print("\nOverall counts:")
    total_counts = {
        'testimonial_injustice': sum(1 for r in all_results if r['testimonial_injustice'] == 1),
        'hermeneutical_injustice': sum(1 for r in all_results if r['hermeneutical_injustice'] == 1),
        'epistemic_dispossession': sum(1 for r in all_results if r['epistemic_dispossession'] == 1),
        'policy_weaponization': sum(1 for r in all_results if r['policy_weaponization'] == 1),
        'naming_dispute': sum(1 for r in all_results if r['naming_dispute'] == 1),
        'source_hierarchy': sum(1 for r in all_results if r['source_hierarchy'] == 1),
    }
    for code, count in total_counts.items():
        print(f"  {code}: {count}")
    
    print(f"\nResults saved to v2/kimi_batch_*.json")
