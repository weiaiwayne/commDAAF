/**
 * AgentID Server - AgentAcademy Identity Registry
 */

import express from 'express';
import cors from 'cors';
import Database from 'better-sqlite3';
import { deriveAgentId, verifySignature } from '../lib/index.js';
import { randomBytes } from 'crypto';

const app = express();
const PORT = process.env.AGENTID_PORT || 3847;
const DB_PATH = process.env.AGENTID_DB || './data/agentid.db';

// Middleware
app.use(cors());
app.use(express.json());

// Initialize database
const db = new Database(DB_PATH);
db.exec(`
  CREATE TABLE IF NOT EXISTS agents (
    agent_id TEXT PRIMARY KEY,
    pubkey TEXT UNIQUE NOT NULL,
    name TEXT,
    framework TEXT,
    metadata TEXT,
    enrolled_at TEXT NOT NULL
  );

  CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id TEXT NOT NULL,
    skill TEXT NOT NULL,
    level TEXT NOT NULL,
    issued_at TEXT NOT NULL,
    issued_by TEXT,
    metadata TEXT,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
    UNIQUE(agent_id, skill)
  );

  CREATE TABLE IF NOT EXISTS challenges (
    challenge TEXT PRIMARY KEY,
    agent_id TEXT,
    created_at TEXT NOT NULL,
    expires_at TEXT NOT NULL
  );
`);

// Prepared statements
const insertAgent = db.prepare(`
  INSERT INTO agents (agent_id, pubkey, name, framework, metadata, enrolled_at)
  VALUES (?, ?, ?, ?, ?, ?)
`);

const getAgent = db.prepare(`SELECT * FROM agents WHERE agent_id = ?`);
const getAgentByPubkey = db.prepare(`SELECT * FROM agents WHERE pubkey = ?`);

const insertCredential = db.prepare(`
  INSERT OR REPLACE INTO credentials (agent_id, skill, level, issued_at, issued_by, metadata)
  VALUES (?, ?, ?, ?, ?, ?)
`);

const getCredentials = db.prepare(`SELECT * FROM credentials WHERE agent_id = ?`);

const insertChallenge = db.prepare(`
  INSERT INTO challenges (challenge, agent_id, created_at, expires_at)
  VALUES (?, ?, ?, ?)
`);

const getChallenge = db.prepare(`SELECT * FROM challenges WHERE challenge = ?`);
const deleteChallenge = db.prepare(`DELETE FROM challenges WHERE challenge = ?`);

// Clean expired challenges periodically
setInterval(() => {
  db.prepare(`DELETE FROM challenges WHERE expires_at < ?`).run(new Date().toISOString());
}, 60000);

// ============ API Routes ============

/**
 * POST /api/agents/enroll
 * Register a new agent
 */
app.post('/api/agents/enroll', (req, res) => {
  try {
    const { pubkey, agentId, metadata, timestamp, signature } = req.body;

    if (!pubkey || !signature) {
      return res.status(400).json({ error: 'Missing pubkey or signature' });
    }

    // Verify agent ID derivation
    const expectedAgentId = deriveAgentId(pubkey);
    if (agentId !== expectedAgentId) {
      return res.status(400).json({ error: 'Invalid agent ID derivation' });
    }

    // Verify signature
    const payload = JSON.stringify({ pubkey, agentId, metadata, timestamp });
    if (!verifySignature(payload, signature, pubkey)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Check if already enrolled
    const existing = getAgentByPubkey.get(pubkey);
    if (existing) {
      return res.status(200).json({
        agent_id: existing.agent_id,
        enrolled_at: existing.enrolled_at,
        already_enrolled: true
      });
    }

    // Enroll
    const enrolled_at = new Date().toISOString();
    insertAgent.run(
      agentId,
      pubkey,
      metadata?.name || null,
      metadata?.framework || null,
      JSON.stringify(metadata || {}),
      enrolled_at
    );

    res.status(201).json({
      agent_id: agentId,
      enrolled_at,
      already_enrolled: false
    });

  } catch (error) {
    console.error('Enrollment error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /api/agents/:agentId
 * Get agent profile
 */
app.get('/api/agents/:agentId', (req, res) => {
  const agent = getAgent.get(req.params.agentId);
  
  if (!agent) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  res.json({
    agent_id: agent.agent_id,
    name: agent.name,
    framework: agent.framework,
    enrolled_at: agent.enrolled_at
  });
});

/**
 * GET /api/agents/:agentId/credentials
 * Get agent credentials
 */
app.get('/api/agents/:agentId/credentials', (req, res) => {
  const agent = getAgent.get(req.params.agentId);
  
  if (!agent) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  const credentials = getCredentials.all(req.params.agentId);

  res.json({
    agent_id: agent.agent_id,
    credentials: credentials.map(c => ({
      skill: c.skill,
      level: c.level,
      issued_at: c.issued_at,
      issued_by: c.issued_by
    }))
  });
});

/**
 * POST /api/agents/challenge
 * Generate a challenge for verification
 */
app.post('/api/agents/challenge', (req, res) => {
  const { agent_id } = req.body;

  if (!agent_id) {
    return res.status(400).json({ error: 'Missing agent_id' });
  }

  const agent = getAgent.get(agent_id);
  if (!agent) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  const challenge = randomBytes(32).toString('base64url');
  const created_at = new Date().toISOString();
  const expires_at = new Date(Date.now() + 5 * 60 * 1000).toISOString(); // 5 min

  insertChallenge.run(challenge, agent_id, created_at, expires_at);

  res.json({ challenge, expires_at });
});

/**
 * POST /api/agents/verify
 * Verify agent owns their ID via signed challenge
 */
app.post('/api/agents/verify', (req, res) => {
  try {
    const { agentId, challenge, signature } = req.body;

    if (!agentId || !challenge || !signature) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Get challenge
    const challengeRecord = getChallenge.get(challenge);
    if (!challengeRecord) {
      return res.status(400).json({ error: 'Invalid or expired challenge' });
    }

    // Check expiry
    if (new Date(challengeRecord.expires_at) < new Date()) {
      deleteChallenge.run(challenge);
      return res.status(400).json({ error: 'Challenge expired' });
    }

    // Check agent ID matches
    if (challengeRecord.agent_id !== agentId) {
      return res.status(400).json({ error: 'Challenge not for this agent' });
    }

    // Get agent
    const agent = getAgent.get(agentId);
    if (!agent) {
      return res.status(404).json({ error: 'Agent not found' });
    }

    // Verify signature
    const message = `${agentId}:${challenge}`;
    const valid = verifySignature(message, signature, agent.pubkey);

    // Clean up challenge
    deleteChallenge.run(challenge);

    if (!valid) {
      return res.status(401).json({ valid: false, error: 'Invalid signature' });
    }

    res.json({
      valid: true,
      agent_id: agentId,
      verified_at: new Date().toISOString()
    });

  } catch (error) {
    console.error('Verification error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * POST /api/credentials/issue
 * Issue a credential to an agent (admin only for now)
 */
app.post('/api/credentials/issue', (req, res) => {
  try {
    const { agent_id, skill, level, issued_by, metadata } = req.body;

    // TODO: Add admin auth

    if (!agent_id || !skill || !level) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const agent = getAgent.get(agent_id);
    if (!agent) {
      return res.status(404).json({ error: 'Agent not found' });
    }

    const issued_at = new Date().toISOString();
    insertCredential.run(
      agent_id,
      skill,
      level,
      issued_at,
      issued_by || 'agentacademy',
      JSON.stringify(metadata || {})
    );

    res.status(201).json({
      agent_id,
      skill,
      level,
      issued_at
    });

  } catch (error) {
    console.error('Credential issue error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /api/stats
 * Public stats
 */
app.get('/api/stats', (req, res) => {
  const agentCount = db.prepare('SELECT COUNT(*) as count FROM agents').get().count;
  const credentialCount = db.prepare('SELECT COUNT(*) as count FROM credentials').get().count;

  res.json({
    agents_enrolled: agentCount,
    credentials_issued: credentialCount
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'agentid' });
});

// Start server
app.listen(PORT, () => {
  console.log(`AgentID server running on port ${PORT}`);
  console.log(`Database: ${DB_PATH}`);
});

export default app;
