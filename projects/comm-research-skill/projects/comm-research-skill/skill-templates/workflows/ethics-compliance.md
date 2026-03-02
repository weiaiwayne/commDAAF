# Research Ethics & Compliance Workflow

Guidance for ethical computational communication research.

---

## Core Principles

1. **Minimize harm** — even to public figures
2. **Respect autonomy** — people's data is about them
3. **Be transparent** — about methods, limitations, funding
4. **Consider downstream use** — how might your findings be misused?
5. **Document everything** — ethics is auditable

---

## IRB/Ethics Board Decision Tree

```
START: Do I need ethics approval?

├─ Are you collecting data FROM people (surveys, interviews)?
│   └─ YES → IRB Required
│
├─ Are you intervening/manipulating (experiments)?
│   └─ YES → IRB Required
│
├─ Are you collecting data ABOUT people (observation, social media)?
│   │
│   ├─ Is the data publicly available?
│   │   │
│   │   ├─ YES, and:
│   │   │   ├─ No direct contact with subjects → May be exempt
│   │   │   ├─ Analyzing public posts only → May be exempt
│   │   │   └─ BUT: check institution policy (some require review anyway)
│   │   │
│   │   └─ NO (private data) → IRB Required
│   │
│   └─ Could your analysis harm subjects?
│       ├─ YES → IRB review recommended even if exempt
│       └─ NO → Document your reasoning
│
└─ When in doubt → Submit for IRB determination
```

### "Public Data" Isn't a Free Pass

Common misconception: "It's public, so no ethics apply."

**Reality:**
- Public ≠ consent to research
- People have different expectations by platform
- Scale matters (analyzing 1 post vs 1M posts)
- Context collapse: tweet about health → in medical study
- Aggregation can reveal private info

**Best Practice:** Even for public data, document:
- Why this data is appropriate to use
- What harm could come from analysis
- How you're protecting subjects

---

## Platform-Specific Ethics

### Twitter/X
```yaml
considerations:
  - Public tweets ≠ consent to research
  - Deleted tweets: ethically problematic to retain
  - Private/protected accounts: need explicit consent
  - Quotes in papers: can identify users
  - Bot detection: false positives harm real people
  
best_practices:
  - Paraphrase rather than quote when possible
  - Don't identify accounts unless public figures
  - If quoting: consider if it could harm speaker
  - Check if tweet still exists before publishing
```

### TikTok
```yaml
considerations:
  - Young user base (many minors)
  - Personal/vulnerable content common
  - Creators are often identifiable
  - Video content = harder to anonymize
  
best_practices:
  - Extra scrutiny for content involving minors
  - Aggregate analysis over individual examples
  - Consider: would creator want this in a paper?
  - If using video stills: blur/anonymize
```

### Reddit
```yaml
considerations:
  - Pseudonymous but traceable
  - Some subreddits expect privacy (support groups)
  - Quotes easily searchable
  
best_practices:
  - Paraphrase, don't quote
  - Don't identify subreddits for sensitive topics
  - Some communities have research norms—check
```

### Telegram
```yaml
considerations:
  - Public channels ≠ public groups
  - Many channels in authoritarian contexts
  - Users may face real-world risk if identified
  
best_practices:
  - Consider political context of users
  - Extra care with channels from repressive regimes
  - Anonymize group names for sensitive topics
```

---

## Data Protection Regulations

### GDPR (EU Data)

If you're processing data about EU residents:

```yaml
gdpr_requirements:
  legal_basis:
    options:
      - Consent (explicit, documented)
      - Legitimate interest (research, balanced against rights)
      - Public interest (scientific research exemption)
    
  data_minimization:
    - Collect only what's necessary
    - Delete when no longer needed
    - Anonymize when possible
    
  documentation:
    - Data protection impact assessment (DPIA) for high-risk
    - Records of processing activities
    - Privacy notice if collecting directly
    
  rights:
    - Right to access (subjects can ask what you have)
    - Right to deletion (within limits for research)
    - Right to object
    
  practical:
    - Check if your institution has GDPR guidance
    - Many universities have data protection officers
    - "Scientific research" has some exemptions but not blanket permission
```

### DSA (Digital Services Act)

EU law mandating platform data access for researchers:

```yaml
dsa_article_40:
  what_it_provides:
    - Right to request data from Very Large Online Platforms (VLOPs)
    - Platforms must provide "vetted researcher" access
    - Access to platform data AND algorithms (in theory)
    
  how_to_use:
    - Apply through platform's DSA compliance portal
    - Need: academic affiliation, research plan, ethics approval
    - National Digital Services Coordinator can assist
    
  current_status_2026:
    - Implementation varies by platform
    - Meta, TikTok, X have portals
    - Response times: weeks to months
    - Better for established researchers/institutions
    
  limitations:
    - Platforms interpret requirements narrowly
    - "Vetted researcher" status is gatekept
    - Enforcement is slow
```

### US Regulations

```yaml
us_landscape:
  ferpa:
    applies_to: Educational records
    relevance: If studying students via institutional data
    
  hipaa:
    applies_to: Health information
    relevance: If analyzing health-related content
    
  childrens_privacy:
    coppa: Under-13 data has special protections
    relevance: TikTok, gaming platforms with young users
    
  state_laws:
    - California CCPA/CPRA
    - Various state privacy laws emerging
    check: Where are your subjects located?
```

---

## Ethical Decision Framework

### Before Data Collection

```markdown
## Pre-Collection Ethics Checklist

1. **Necessity**
   - [ ] Is this data actually needed for my RQ?
   - [ ] Could I answer this with less sensitive data?
   - [ ] What's the minimum data I need?

2. **Source Appropriateness**
   - [ ] Is this the right platform/population to study?
   - [ ] What are user expectations on this platform?
   - [ ] Are there vulnerable populations in my sample?

3. **Legal Compliance**
   - [ ] Do I have legal basis (consent, legitimate interest)?
   - [ ] Does my institution have relevant policies?
   - [ ] Have I checked platform ToS?

4. **Risk Assessment**
   - [ ] What could go wrong?
   - [ ] Who could be harmed?
   - [ ] How would I handle a data breach?
```

### During Analysis

```markdown
## Analysis Ethics Checklist

1. **Data Security**
   - [ ] Is data stored securely?
   - [ ] Who has access?
   - [ ] Is access logged?

2. **Anonymization**
   - [ ] Have I removed direct identifiers?
   - [ ] Could individuals be re-identified?
   - [ ] Am I aggregating appropriately?

3. **Fairness**
   - [ ] Could my analysis unfairly characterize groups?
   - [ ] Am I aware of my own biases?
   - [ ] Have I considered alternative interpretations?
```

### Before Publication

```markdown
## Publication Ethics Checklist

1. **Individual Protection**
   - [ ] Are any individuals identifiable?
   - [ ] Would quoted users want to be in this paper?
   - [ ] Could publication harm any subjects?

2. **Group Protection**
   - [ ] Am I fairly representing communities studied?
   - [ ] Could findings be used to harm these groups?
   - [ ] Have I considered context and nuance?

3. **Downstream Use**
   - [ ] How might these findings be misused?
   - [ ] Should I add caveats about misuse?
   - [ ] Are my claims appropriately hedged?

4. **Transparency**
   - [ ] Are my methods reproducible?
   - [ ] Have I disclosed limitations?
   - [ ] Have I disclosed funding/conflicts?
```

---

## Specific Ethical Scenarios

### Coordinated Behavior Detection

**The Risk:** False positives → falsely accusing people of being "bots" or "coordinated actors"

```yaml
scenario: You detect coordination patterns

ethical_requirements:
  - NEVER claim "bots" from temporal patterns alone
  - NEVER claim "foreign influence" without strong evidence
  - Consider: could this be organic activism?
  - Consider: are these people at risk if identified?
  
before_publishing:
  - What's your false positive rate?
  - Did you validate with ground truth?
  - What if you're wrong about some accounts?
  - Add appropriate uncertainty language
  
language_to_avoid:
  - "These accounts are bots"
  - "This is a coordinated campaign"
  - "Foreign interference detected"
  
language_to_use:
  - "These accounts exhibit coordinated posting patterns"
  - "We observe temporal synchronization that may indicate coordination"
  - "Further investigation would be needed to determine authenticity"
```

### Identifying Misinformation Spreaders

**The Risk:** Publicly identifying accounts → harassment, doxxing

```yaml
scenario: You identify accounts spreading misinformation

considerations:
  - Public figures vs private individuals
  - Scale of spread (1 post vs 1000 posts)
  - Intent: malicious vs misinformed
  - Could identification lead to harm?
  
best_practices:
  - Public figures: more acceptable to identify
  - Private individuals: anonymize unless compelling reason
  - Consider: "superspreader" with 10 followers is not actually influential
  - Aggregate metrics over individual naming
  
exception_cases:
  - Account is already known/public
  - Clear public interest (e.g., verified official account)
  - Account holder has consented
```

### Vulnerable Populations

**The Risk:** Research involving sensitive groups

```yaml
vulnerable_populations:
  - Minors (under 18, especially under 13)
  - Mental health communities
  - LGBTQ+ individuals (in hostile contexts)
  - Political dissidents (in authoritarian contexts)
  - Refugees and migrants
  - Any group facing discrimination
  
heightened_requirements:
  - IRB review even if technically exempt
  - Extra anonymization
  - Consider: does this research benefit these communities?
  - Consult community members if possible
  - Avoid extractive research (taking data, giving nothing back)
```

---

## ToS Compliance

### When ToS Violation Might Be Acceptable

Controversial but real consideration:

```yaml
tos_violation_framework:
  
  generally_not_acceptable:
    - Violating ToS for convenience
    - Scraping because API is expensive
    - Ignoring ToS you haven't read
    
  potentially_acceptable:
    - Public interest research
    - Platform is preventing legitimate study
    - Harm of not researching > harm of ToS violation
    - Example: Studying election manipulation on platform that blocks research
    
  requirements_if_violating:
    - Document your reasoning
    - Minimize collection
    - Enhanced data protection
    - Be prepared to defend in publication
    - Consult IRB/ethics board
    - Consider: hiQ Labs v. LinkedIn precedent (public data scraping)
    
  always_unacceptable:
    - Accessing private/protected data
    - Circumventing authentication
    - Overwhelming servers (DDoS-like collection)
    - Selling or misusing data
```

---

## Documentation Templates

### Ethics Statement for Paper

```markdown
## Ethics Statement

This study analyzes publicly available social media data. Our institution's 
IRB determined this research to be [exempt/approved] (Protocol #XXXXX).

**Data Collection:** We collected [description] from [platform] between 
[dates]. All data were publicly posted at time of collection.

**Anonymization:** Individual accounts are not identified in this paper. 
Quoted posts have been paraphrased to prevent searchability.

**Data Security:** Data are stored on encrypted university servers with 
access limited to named researchers.

**Limitations:** Our analysis cannot determine the authenticity or intent 
of accounts. Findings should be interpreted as patterns in public discourse, 
not evidence of specific bad actors.
```

### Data Management Plan

```markdown
## Data Management Plan

**Data Types:**
- Social media posts (text, metadata)
- Network data (edges between accounts)
- Derived data (topic models, sentiment scores)

**Storage:**
- Primary: [Institutional server, encrypted]
- Backup: [Location, encrypted]
- Access log: [Yes, maintained by PI]

**Retention:**
- Raw data: Delete [X months] after publication
- Derived data: Archive with [repository]
- Analysis code: Archive with [repository]

**Sharing:**
- Raw data: Not shared (privacy)
- Derived data: Shared via [repository] with DOI
- Code: Shared via GitHub

**Destruction:**
- Raw data securely deleted via [method]
- Logs maintained showing deletion
```

---

## When You're Uncertain

### Decision Process

```
1. Document your reasoning in writing
2. Consult IRB/ethics board (even for exempt)
3. Consult colleagues/advisors
4. Err on the side of caution
5. If you can't justify it in your methods section, don't do it
```

### Questions to Ask Yourself

1. Would I be comfortable if subjects knew about this research?
2. Would I be comfortable explaining this on a news program?
3. What would a reasonable person in the subject's position expect?
4. What's the worst case if something goes wrong?
5. Does the research benefit outweigh the risks?

---

## Resources

### Readings
- Zimmer, M. (2010). "But the data is already public": on the ethics of research in Facebook
- Fiesler, C. & Proferes, N. (2018). "Participant" perceptions of Twitter research ethics
- Markham, A. & Buchanan, E. (2012). Ethical Decision-Making and Internet Research (AoIR)

### Organizations
- Association of Internet Researchers (AoIR) — ethics guidelines
- ACM SIGCHI — HCI research ethics
- Your institution's IRB/ethics board

### Tools
- Data Protection Impact Assessment templates
- Informed consent templates
- Anonymization toolkits

---

*This document provides guidance, not legal advice. Consult your institution's IRB and legal counsel for specific situations.*
