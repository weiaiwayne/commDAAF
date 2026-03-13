/**
 * AgentID Data Access Routes
 * Provides enrolled agents access to AgentAcademy materials
 */

import { Router } from 'express';
import { readFileSync, existsSync, readdirSync, statSync } from 'fs';
import { join, extname } from 'path';

const router = Router();
const ACADEMY_DATA = process.env.ACADEMY_DATA || './data/academy';

// Load agents store (shared with main server)
function loadAgents() {
  const file = process.env.AGENTID_DATA 
    ? `${process.env.AGENTID_DATA}/agents.json`
    : './data/agents.json';
  if (!existsSync(file)) return {};
  return JSON.parse(readFileSync(file, 'utf-8'));
}

// Middleware: require enrolled agent
function requireEnrolled(req, res, next) {
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ 
      error: 'Missing authorization',
      hint: 'Use: Authorization: Bearer <agent_id>'
    });
  }

  const agentId = authHeader.slice(7);
  const agents = loadAgents();

  if (!agents[agentId]) {
    return res.status(403).json({ 
      error: 'Agent not enrolled',
      hint: 'Enroll first via POST /api/agents/enroll'
    });
  }

  req.agent = agents[agentId];
  req.agentId = agentId;
  next();
}

/**
 * GET /api/academy
 * Get index of all available materials
 */
router.get('/', requireEnrolled, (req, res) => {
  const indexPath = join(ACADEMY_DATA, 'index.json');
  
  if (!existsSync(indexPath)) {
    return res.status(500).json({ error: 'Academy index not found' });
  }

  const index = JSON.parse(readFileSync(indexPath, 'utf-8'));
  
  res.json({
    agent_id: req.agentId,
    access_level: 'enrolled',
    ...index
  });
});

/**
 * GET /api/academy/collections
 * List all collections
 */
router.get('/collections', requireEnrolled, (req, res) => {
  const indexPath = join(ACADEMY_DATA, 'index.json');
  const index = JSON.parse(readFileSync(indexPath, 'utf-8'));
  
  const collections = Object.entries(index.collections).map(([id, col]) => ({
    id,
    name: col.name,
    description: col.description,
    status: col.status,
    resource_count: Object.keys(col.resources).length
  }));

  res.json({ collections });
});

/**
 * GET /api/academy/collections/:id
 * Get a specific collection with its resources
 */
router.get('/collections/:id', requireEnrolled, (req, res) => {
  const indexPath = join(ACADEMY_DATA, 'index.json');
  const index = JSON.parse(readFileSync(indexPath, 'utf-8'));
  
  const collection = index.collections[req.params.id];
  
  if (!collection) {
    return res.status(404).json({ error: 'Collection not found' });
  }

  res.json({
    id: req.params.id,
    ...collection,
    _links: {
      self: `/api/academy/collections/${req.params.id}`,
      resources: Object.keys(collection.resources).map(key => ({
        name: key,
        url: `/api/academy/files/${collection.resources[key]}`
      }))
    }
  });
});

/**
 * GET /api/academy/prompts
 * List all prompts
 */
router.get('/prompts', requireEnrolled, (req, res) => {
  const promptsDir = join(ACADEMY_DATA, 'prompts');
  
  if (!existsSync(promptsDir)) {
    return res.json({ prompts: [] });
  }

  const prompts = readdirSync(promptsDir)
    .filter(f => f.endsWith('.md'))
    .map(f => ({
      name: f.replace('.md', ''),
      file: f,
      url: `/api/academy/files/prompts/${f}`
    }));

  res.json({ prompts });
});

/**
 * GET /api/academy/logs
 * Get run logs
 */
router.get('/logs', requireEnrolled, (req, res) => {
  const logsDir = join(ACADEMY_DATA, 'logs');
  
  if (!existsSync(logsDir)) {
    return res.json({ logs: [] });
  }

  const logs = readdirSync(logsDir)
    .filter(f => f.endsWith('.json'))
    .map(f => ({
      name: f.replace('.json', ''),
      file: f,
      url: `/api/academy/files/logs/${f}`
    }));

  res.json({ logs });
});

/**
 * GET /api/academy/files/*
 * Get a specific file
 */
router.get('/files/*', requireEnrolled, (req, res) => {
  const relativePath = req.params[0];
  
  // Security: prevent directory traversal
  if (relativePath.includes('..') || relativePath.startsWith('/')) {
    return res.status(400).json({ error: 'Invalid path' });
  }
  
  const filePath = join(ACADEMY_DATA, relativePath);

  if (!existsSync(filePath)) {
    return res.status(404).json({ error: 'File not found' });
  }

  const stat = statSync(filePath);
  if (stat.isDirectory()) {
    return res.status(400).json({ error: 'Cannot serve directory' });
  }

  const ext = extname(filePath);
  const content = readFileSync(filePath, 'utf-8');

  if (ext === '.json') {
    res.json(JSON.parse(content));
  } else if (ext === '.md') {
    res.type('text/markdown').send(content);
  } else {
    res.type('text/plain').send(content);
  }
});

/**
 * GET /api/academy/search
 * Search across materials
 */
router.get('/search', requireEnrolled, (req, res) => {
  const query = (req.query.q || '').toLowerCase();
  
  if (!query || query.length < 2) {
    return res.status(400).json({ error: 'Query too short (min 2 chars)' });
  }

  const results = [];
  
  // Search through files
  const searchDir = (dir, basePath = '') => {
    if (!existsSync(dir)) return;
    
    for (const item of readdirSync(dir)) {
      const itemPath = join(dir, item);
      const relativePath = basePath ? `${basePath}/${item}` : item;
      
      const stat = statSync(itemPath);
      
      if (stat.isDirectory()) {
        searchDir(itemPath, relativePath);
      } else if (item.endsWith('.md') || item.endsWith('.json')) {
        const content = readFileSync(itemPath, 'utf-8');
        
        if (content.toLowerCase().includes(query)) {
          // Find matching lines
          const lines = content.split('\n');
          const matches = lines
            .map((line, i) => ({ line: i + 1, text: line }))
            .filter(l => l.text.toLowerCase().includes(query))
            .slice(0, 3);

          results.push({
            file: relativePath,
            url: `/api/academy/files/${relativePath}`,
            matches
          });
        }
      }
    }
  };

  searchDir(ACADEMY_DATA);

  res.json({ 
    query,
    count: results.length,
    results: results.slice(0, 20)
  });
});

export default router;
