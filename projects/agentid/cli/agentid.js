#!/usr/bin/env node

/**
 * AgentID CLI - Identity management for AI agents
 */

import { generateIdentity, deriveAgentId, signChallenge } from '../lib/index.js';
import { AgentIDClient } from '../lib/client.js';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { homedir } from 'os';

const KEYSTORE_PATH = process.env.AGENTID_KEYSTORE || join(homedir(), '.agentid', 'identity.json');
const SERVER_URL = process.env.AGENTID_SERVER || 'http://localhost:3847';

const args = process.argv.slice(2);
const command = args[0];

async function main() {
  switch (command) {
    case 'init':
      await cmdInit();
      break;
    case 'show':
      cmdShow();
      break;
    case 'enroll':
      await cmdEnroll();
      break;
    case 'verify':
      await cmdVerify();
      break;
    case 'credentials':
      await cmdCredentials();
      break;
    case 'export':
      cmdExport();
      break;
    default:
      printHelp();
  }
}

function printHelp() {
  console.log(`
AgentID - Decentralized identity for AI agents

Commands:
  init          Generate a new identity (or show existing)
  show          Display current identity
  enroll        Enroll with AgentAcademy
  verify        Respond to a verification challenge
  credentials   List your credentials
  export        Export public key for verification

Environment:
  AGENTID_KEYSTORE  Path to identity file (default: ~/.agentid/identity.json)
  AGENTID_SERVER    AgentAcademy server URL (default: http://localhost:3847)
`);
}

async function cmdInit() {
  if (existsSync(KEYSTORE_PATH)) {
    console.log('Identity already exists at:', KEYSTORE_PATH);
    cmdShow();
    return;
  }

  const identity = generateIdentity();
  
  const dir = dirname(KEYSTORE_PATH);
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true, mode: 0o700 });
  }
  
  writeFileSync(KEYSTORE_PATH, JSON.stringify(identity, null, 2), { mode: 0o600 });
  
  console.log('✓ Identity generated');
  console.log('  Agent ID:', identity.agentId);
  console.log('  Stored at:', KEYSTORE_PATH);
  console.log('\n⚠️  Keep your private key safe! Losing it means losing this identity.');
}

function cmdShow() {
  if (!existsSync(KEYSTORE_PATH)) {
    console.error('No identity found. Run: agentid init');
    process.exit(1);
  }

  const identity = JSON.parse(readFileSync(KEYSTORE_PATH, 'utf-8'));
  
  console.log('Agent ID:', identity.agentId);
  console.log('Public Key:', identity.publicKey.slice(0, 40) + '...');
  console.log('Keystore:', KEYSTORE_PATH);
}

async function cmdEnroll() {
  const client = new AgentIDClient({ serverUrl: SERVER_URL, keystorePath: KEYSTORE_PATH });
  
  const name = args[1] || process.env.AGENT_NAME;
  const framework = args[2] || process.env.AGENT_FRAMEWORK || 'openclaw';

  try {
    await client.init();
    const result = await client.enroll({ name, framework });
    
    if (result.already_enrolled) {
      console.log('✓ Already enrolled');
    } else {
      console.log('✓ Enrolled successfully');
    }
    console.log('  Agent ID:', result.agent_id);
    console.log('  Enrolled:', result.enrolled_at);
  } catch (error) {
    console.error('Enrollment failed:', error.message);
    process.exit(1);
  }
}

async function cmdVerify() {
  const challenge = args[1];
  
  if (!challenge) {
    console.error('Usage: agentid verify <challenge>');
    process.exit(1);
  }

  const client = new AgentIDClient({ serverUrl: SERVER_URL, keystorePath: KEYSTORE_PATH });
  
  try {
    await client.init();
    const result = await client.verify(challenge);
    
    if (result.valid) {
      console.log('✓ Verification successful');
      console.log('  Agent ID:', result.agent_id);
    } else {
      console.log('✗ Verification failed:', result.error);
    }
  } catch (error) {
    console.error('Verification failed:', error.message);
    process.exit(1);
  }
}

async function cmdCredentials() {
  const client = new AgentIDClient({ serverUrl: SERVER_URL, keystorePath: KEYSTORE_PATH });
  
  try {
    await client.init();
    const result = await client.getCredentials();
    
    console.log('Agent ID:', result.agent_id);
    console.log('Credentials:');
    
    if (result.credentials.length === 0) {
      console.log('  (none)');
    } else {
      for (const cred of result.credentials) {
        console.log(`  - ${cred.skill} [${cred.level}] (issued: ${cred.issued_at})`);
      }
    }
  } catch (error) {
    console.error('Failed to fetch credentials:', error.message);
    process.exit(1);
  }
}

function cmdExport() {
  if (!existsSync(KEYSTORE_PATH)) {
    console.error('No identity found. Run: agentid init');
    process.exit(1);
  }

  const identity = JSON.parse(readFileSync(KEYSTORE_PATH, 'utf-8'));
  
  const exportData = {
    agent_id: identity.agentId,
    pubkey: identity.publicKey
  };
  
  console.log(JSON.stringify(exportData, null, 2));
}

main().catch(console.error);
