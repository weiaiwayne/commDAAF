/**
 * AgentID Server (Lite) - JSON file store, no native deps
 */

import express from 'express';
import cors from 'cors';
import { deriveAgentId, verifySignature } from '../lib/index.js';
import { randomBytes } from 'crypto';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import academyRoutes from './data-routes.js';

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const PORT = process.env.AGENTID_PORT || 3847;
const DATA_DIR = process.env.AGENTID_DATA || './data';
const AGENTS_FILE = `${DATA_DIR}/agents.json`;
const CREDENTIALS_FILE = `${DATA_DIR}/credentials.json`;
const CHALLENGES_FILE = `${DATA_DIR}/challenges.json`;

// Ensure data dir exists
if (!existsSync(DATA_DIR)) {
  mkdirSync(DATA_DIR, { recursive: true });
}

// Simple JSON store
function loadJson(file, defaultValue = {}) {
  if (!existsSync(file)) return defaultValue;
  return JSON.parse(readFileSync(file, 'utf-8'));
}

function saveJson(file, data) {
  writeFileSync(file, JSON.stringify(data, null, 2));
}

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files (landing page)
app.use(express.static(join(__dirname, '../public')));

// ============ API Routes ============

/**
 * POST /api/agents/enroll
 */
app.post('/api/agents/enroll', (req, res) => {
  try {
    const { pubkey, agentId, metadata, timestamp, signature } = req.body;

    if (!pubkey || !signature) {
      return res.status(400).json({ error: 'Missing pubkey or signature' });
    }

    const expectedAgentId = deriveAgentId(pubkey);
    if (agentId !== expectedAgentId) {
      return res.status(400).json({ error: 'Invalid agent ID derivation' });
    }

    const payload = JSON.stringify({ pubkey, agentId, metadata, timestamp });
    if (!verifySignature(payload, signature, pubkey)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const agents = loadJson(AGENTS_FILE, {});
    
    if (agents[agentId]) {
      return res.status(200).json({
        agent_id: agentId,
        enrolled_at: agents[agentId].enrolled_at,
        already_enrolled: true
      });
    }

    const enrolled_at = new Date().toISOString();
    agents[agentId] = {
      agent_id: agentId,
      pubkey,
      name: metadata?.name || null,
      framework: metadata?.framework || null,
      metadata: metadata || {},
      enrolled_at
    };
    
    saveJson(AGENTS_FILE, agents);

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
 */
app.get('/api/agents/:agentId', (req, res) => {
  const agents = loadJson(AGENTS_FILE, {});
  const agent = agents[req.params.agentId];
  
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
 */
app.get('/api/agents/:agentId/credentials', (req, res) => {
  const agents = loadJson(AGENTS_FILE, {});
  const agent = agents[req.params.agentId];
  
  if (!agent) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  const allCredentials = loadJson(CREDENTIALS_FILE, {});
  const credentials = allCredentials[req.params.agentId] || [];

  res.json({
    agent_id: agent.agent_id,
    credentials
  });
});

/**
 * POST /api/agents/challenge
 */
app.post('/api/agents/challenge', (req, res) => {
  const { agent_id } = req.body;

  if (!agent_id) {
    return res.status(400).json({ error: 'Missing agent_id' });
  }

  const agents = loadJson(AGENTS_FILE, {});
  if (!agents[agent_id]) {
    return res.status(404).json({ error: 'Agent not found' });
  }

  const challenge = randomBytes(32).toString('base64url');
  const created_at = new Date().toISOString();
  const expires_at = new Date(Date.now() + 5 * 60 * 1000).toISOString();

  const challenges = loadJson(CHALLENGES_FILE, {});
  challenges[challenge] = { agent_id, created_at, expires_at };
  saveJson(CHALLENGES_FILE, challenges);

  res.json({ challenge, expires_at });
});

/**
 * POST /api/agents/verify
 */
app.post('/api/agents/verify', (req, res) => {
  try {
    const { agentId, challenge, signature } = req.body;

    if (!agentId || !challenge || !signature) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const challenges = loadJson(CHALLENGES_FILE, {});
    const challengeRecord = challenges[challenge];
    
    if (!challengeRecord) {
      return res.status(400).json({ error: 'Invalid or expired challenge' });
    }

    if (new Date(challengeRecord.expires_at) < new Date()) {
      delete challenges[challenge];
      saveJson(CHALLENGES_FILE, challenges);
      return res.status(400).json({ error: 'Challenge expired' });
    }

    if (challengeRecord.agent_id !== agentId) {
      return res.status(400).json({ error: 'Challenge not for this agent' });
    }

    const agents = loadJson(AGENTS_FILE, {});
    const agent = agents[agentId];
    
    if (!agent) {
      return res.status(404).json({ error: 'Agent not found' });
    }

    const message = `${agentId}:${challenge}`;
    const valid = verifySignature(message, signature, agent.pubkey);

    delete challenges[challenge];
    saveJson(CHALLENGES_FILE, challenges);

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
 */
app.post('/api/credentials/issue', (req, res) => {
  try {
    const { agent_id, skill, level, issued_by, metadata } = req.body;

    if (!agent_id || !skill || !level) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const agents = loadJson(AGENTS_FILE, {});
    if (!agents[agent_id]) {
      return res.status(404).json({ error: 'Agent not found' });
    }

    const issued_at = new Date().toISOString();
    const allCredentials = loadJson(CREDENTIALS_FILE, {});
    
    if (!allCredentials[agent_id]) {
      allCredentials[agent_id] = [];
    }

    // Remove existing credential for same skill
    allCredentials[agent_id] = allCredentials[agent_id].filter(c => c.skill !== skill);
    
    allCredentials[agent_id].push({
      skill,
      level,
      issued_at,
      issued_by: issued_by || 'agentacademy',
      metadata: metadata || {}
    });
    
    saveJson(CREDENTIALS_FILE, allCredentials);

    res.status(201).json({ agent_id, skill, level, issued_at });

  } catch (error) {
    console.error('Credential issue error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * GET /api/stats
 */
app.get('/api/stats', (req, res) => {
  const agents = loadJson(AGENTS_FILE, {});
  const credentials = loadJson(CREDENTIALS_FILE, {});
  
  const agentCount = Object.keys(agents).length;
  const credentialCount = Object.values(credentials).reduce((sum, arr) => sum + arr.length, 0);

  res.json({
    agents_enrolled: agentCount,
    credentials_issued: credentialCount
  });
});

/**
 * GET /api/agents
 * List all agents (public info only)
 */
app.get('/api/agents', (req, res) => {
  const agents = loadJson(AGENTS_FILE, {});
  
  const list = Object.values(agents).map(a => ({
    agent_id: a.agent_id,
    name: a.name,
    framework: a.framework,
    enrolled_at: a.enrolled_at
  }));

  res.json({ agents: list, count: list.length });
});

// Academy data routes
app.use('/api/academy', academyRoutes);

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'agentid-lite' });
});

// Start server
app.listen(PORT, () => {
  console.log(`AgentID (lite) server running on port ${PORT}`);
  console.log(`Data directory: ${DATA_DIR}`);
});

export default app;
