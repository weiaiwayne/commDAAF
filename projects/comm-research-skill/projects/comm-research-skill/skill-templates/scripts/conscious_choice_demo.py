#!/usr/bin/env python3
"""
CommDAAF Conscious Choice Demo

Experience what the nudge system feels like.
Forces explicit decisions at key research design points.

Usage: python conscious_choice_demo.py
"""

from datetime import datetime


def header(title):
    print(f"\n{'='*60}")
    print(f"⚠️  {title}")
    print(f"{'='*60}\n")


def get_choice(prompt, options):
    """Force explicit choice."""
    print(f"\n{prompt}")
    print("-" * 50)
    
    for i, (name, desc, risk) in enumerate(options, 1):
        print(f"\n{i}. {name}")
        print(f"   {desc}")
        print(f"   🚨 Risk: {risk}")
    
    print("\n⛔ DEFAULT NOT AVAILABLE — You must choose.")
    
    while True:
        choice = input(f"\nYour choice (1-{len(options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1, options[int(choice) - 1][0]
        print("❌ Invalid. Enter a number.")


def get_justification(min_len=30):
    """Require justification."""
    print("\n📝 JUSTIFY your choice (min 30 characters):")
    
    while True:
        text = input("> ").strip()
        if len(text) >= min_len:
            return text
        print(f"❌ Too brief ({len(text)} chars). Explain more.")


def demo_topic_modeling():
    """Topic modeling nudge demo."""
    header("TOPIC MODELING: DEFAULT ALERT")
    
    print("You're about to run topic modeling with DEFAULT parameters.")
    print("\n🚨 DANGER: Defaults may be WRONG for your data:")
    print("  • min_topic_size=10 assumes ~500+ documents")
    print("  • Generic embedding model may miss domain terms")
    print("  • n_topics not calibrated to your corpus")
    
    options = [
        ("Use defaults (RISKY)", 
         "Quick but may produce invalid topics",
         "High false positive rate, poor coherence"),
        ("Calibrate for my data (RECOMMENDED)",
         "Tune parameters based on data characteristics",
         "Takes more time, requires validation"),
        ("Use domain-specific model",
         "Pre-trained embeddings for your field",
         "Requires finding appropriate model"),
    ]
    
    idx, choice = get_choice("Choose your approach:", options)
    justification = get_justification()
    
    print(f"\n✅ Recorded: {choice}")
    return {'stage': 'topic_modeling', 'choice': choice, 'justification': justification}


def demo_network_edges():
    """Network edge definition nudge."""
    header("NETWORK CONSTRUCTION: ACTIVE CHOICE REQUIRED")
    
    print("❌ 'Standard network' is NOT an option.")
    print("❌ 'Whatever works' is NOT acceptable.")
    
    print("\n📊 TRADE-OFF MATRIX:")
    print("                | Interaction | Thematic | Complexity |")
    print("Retweet         | ★★★★★       | ★☆☆☆☆    | LOW        |")
    print("Mention         | ★★★★☆       | ★☆☆☆☆    | LOW        |")
    print("Semantic        | ★☆☆☆☆       | ★★★★★    | MEDIUM     |")
    
    options = [
        ("Retweet network",
         "Captures: Information diffusion, amplification",
         "Misses conversation; bots inflate metrics"),
        ("Mention network",
         "Captures: Conversation, attention",
         "Misses passive consumption; @mention ≠ endorsement"),
        ("Semantic similarity",
         "Captures: Thematic alignment, echoing",
         "Misses explicit interaction; similarity ≠ agreement"),
    ]
    
    idx, choice = get_choice("Which fits your research question?", options)
    
    print("\n🔍 ALIGNMENT CHECK")
    rq = input("Your research question is about: ").strip()
    justification = get_justification()
    
    print(f"\n✅ Recorded: {choice}")
    return {'stage': 'network_edges', 'choice': choice, 'rq': rq, 'justification': justification}


def demo_validation_tier():
    """Validation tier selection."""
    header("VALIDATION TIER SELECTION")
    
    print("Choose validation level based on your stakes:")
    
    options = [
        ("🟢 EXPLORATORY (30-60 min)",
         "For: Learning, exploring, hypothesis generation",
         "Cannot publish; heavy caveats required"),
        ("🟡 PILOT (2-4 hours)",
         "For: Committee presentation, working paper",
         "Preliminary findings only; moderate caveats"),
        ("🔴 PUBLICATION (1-2 days)",
         "For: Journal submission, dissertation",
         "Full validation required; defensible claims"),
    ]
    
    idx, choice = get_choice("What are your stakes?", options)
    justification = get_justification()
    
    print(f"\n✅ Recorded: {choice}")
    return {'stage': 'validation_tier', 'choice': choice, 'justification': justification}


def demo_assumption_audit():
    """Assumption audit checkpoint."""
    header("ASSUMPTION AUDIT")
    
    print("Before proceeding, make assumptions EXPLICIT.\n")
    
    assumptions = [
        "My sample represents the population I claim",
        "Missing data is random (not systematic)",
        "Platform changes didn't affect behavior during study",
        "My operationalization captures the theoretical concept",
        "I've considered alternative explanations",
    ]
    
    justified = []
    limitations = []
    
    for i, assumption in enumerate(assumptions, 1):
        print(f"\n{i}. {assumption}")
        resp = input("   Can you justify this? (y/n): ").strip().lower()
        
        if resp == 'y':
            detail = input("   Brief justification: ").strip()
            justified.append((assumption, detail))
        else:
            print("   ⚠️ This is a LIMITATION you must acknowledge.")
            limitations.append(assumption)
    
    print(f"\n✅ Justified: {len(justified)}/{len(assumptions)}")
    if limitations:
        print(f"⚠️ Limitations to acknowledge: {len(limitations)}")
    
    return {'stage': 'assumption_audit', 'justified': justified, 'limitations': limitations}


def demo_reflection():
    """Reflection checkpoint."""
    header("REFLECTION CHECKPOINT")
    
    print("Before interpreting results, reflect:\n")
    
    expected = input("1. What did you EXPECT to find?\n   > ").strip()
    found = input("\n2. What did you actually FIND?\n   > ").strip()
    surprise = input("\n3. What was SURPRISING?\n   > ").strip()
    
    print("\n4. What ALTERNATIVE EXPLANATIONS exist?")
    alt1 = input("   Alternative 1: ").strip()
    alt2 = input("   Alternative 2: ").strip()
    
    if not alt1 or not alt2:
        print("\n⛔ WARNING: Without alternatives, you're not thinking critically.")
    
    falsify = input("\n5. What would DISPROVE your interpretation?\n   > ").strip()
    
    if len(falsify) < 10:
        print("⛔ You MUST know what would prove you wrong.")
    
    return {
        'stage': 'reflection',
        'expected': expected,
        'found': found,
        'alternatives': [alt1, alt2],
        'falsifying': falsify
    }


def main():
    print("=" * 60)
    print("  COMMDAAF CONSCIOUS CHOICE DEMO")
    print("  Experience the Nudge System")
    print("=" * 60)
    print("\nThis demo shows how CommDAAF forces explicit choices")
    print("and prevents default-driven research.\n")
    
    input("Press Enter to begin...")
    
    decisions = []
    
    # Run demos
    decisions.append(demo_validation_tier())
    input("\n[Press Enter to continue]")
    
    decisions.append(demo_topic_modeling())
    input("\n[Press Enter to continue]")
    
    decisions.append(demo_network_edges())
    input("\n[Press Enter to continue]")
    
    decisions.append(demo_assumption_audit())
    input("\n[Press Enter to continue]")
    
    decisions.append(demo_reflection())
    
    # Summary
    header("DECISION RECORD SUMMARY")
    
    print(f"Total conscious choices recorded: {len(decisions)}\n")
    
    for i, d in enumerate(decisions, 1):
        stage = d['stage'].replace('_', ' ').title()
        choice = d.get('choice', 'Completed')
        print(f"{i}. {stage}: {choice}")
    
    print("\n" + "=" * 60)
    print("✅ All decisions are:")
    print("   • Explicit (no defaults)")
    print("   • Justified (written reasoning)")
    print("   • Auditable (could go in methods section)")
    print("   • Defensible (ready for Reviewer 2)")
    print("=" * 60)
    print("\nThis is how CommDAAF prevents sleepwalking through research.")


if __name__ == "__main__":
    main()
