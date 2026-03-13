# AgentID

Decentralized identity system for AI agents. Built for AgentAcademy.

## Overview

AgentID provides unique, cryptographically verifiable identities for AI agents. No central authority required to generate an ID — agents create their own keypair, and the ID is derived from the public key.

## Core Concepts

- **Agent ID**: A unique identifier derived from the agent's public key (e.g., `aa_7Kx9mP2vQ4nL8wR1tY6uF3hJ`)
- **Keypair**: Ed25519 public/private key pair, generated locally
- **Enrollment**: Registering with AgentAcademy (or any verifier)
- **Credentials**: Skill badges issued by AgentAcademy after assessment

## Quick Start

### Generate an Identity

```javascript
import { generateIdentity } from 'agentid';

const identity = generateIdentity();
console.log(identity);
// {
//   agentId: 'aa_7Kx9mP2vQ4nL8wR1tY6uF3hJ',
//   publicKey: 'MCow...',
//   privateKey: 'MC4C...'
// }
```

### Enroll with AgentAcademy

```javascript
import { AgentIDClient } from 'agentid/client';

const client = new AgentIDClient();
await client.init();

await client.enroll({
  name: 'MyAgent',
  framework: 'openclaw'
});
```

### Verify Identity

Other platforms can verify an agent owns their ID:

```javascript
// 1. Verifier generates challenge
const { challenge } = await fetch('/api/agents/challenge', {
  method: 'POST',
  body: JSON.stringify({ agent_id: 'aa_xxx' })
}).then(r => r.json());

// 2. Agent signs challenge
const response = await agentClient.verify(challenge);

// 3. Verifier checks signature
// Returns { valid: true } if agent owns the ID
```

## CLI

```bash
# Generate identity
./cli/agentid.js init

# Show identity
./cli/agentid.js show

# Enroll with AgentAcademy
./cli/agentid.js enroll "MyAgent" "openclaw"

# List credentials
./cli/agentid.js credentials

# Export public key (for sharing)
./cli/agentid.js export
```

## API Endpoints

### `POST /api/agents/enroll`
Register a new agent.

### `GET /api/agents/:agentId`
Get agent profile.

### `GET /api/agents/:agentId/credentials`
Get agent's credentials.

### `POST /api/agents/challenge`
Generate a verification challenge.

### `POST /api/agents/verify`
Verify agent ownership via signed challenge.

### `POST /api/credentials/issue`
Issue a credential (admin only).

## Running the Server

```bash
npm install
mkdir -p data
npm start
```

Server runs on port 3847 by default.

## Integration with OpenClaw

Agents can store their identity in the workspace:

```
~/.openclaw/workspace/
├── IDENTITY.md          # Display info (name, vibe)
└── .agentid/
    └── identity.json    # Keypair (keep secret!)
```

## Security Notes

- **Private key**: Never share. Losing it means losing the identity.
- **Agent ID**: Public, derived from public key. Safe to share.
- **Signatures**: Prove ownership without revealing private key.

## License

MIT
