/**
 * AgentID - Core Library
 * Decentralized identity for AI agents
 */

import { generateKeyPairSync, sign, verify, createHash } from 'crypto';

const AGENT_ID_PREFIX = 'aa_';

/**
 * Generate a new agent keypair
 * @returns {{ publicKey: string, privateKey: string, agentId: string }}
 */
export function generateIdentity() {
  const { publicKey, privateKey } = generateKeyPairSync('ed25519', {
    publicKeyEncoding: { type: 'spki', format: 'der' },
    privateKeyEncoding: { type: 'pkcs8', format: 'der' }
  });

  const pubKeyBase64 = publicKey.toString('base64');
  const agentId = deriveAgentId(pubKeyBase64);

  return {
    publicKey: pubKeyBase64,
    privateKey: privateKey.toString('base64'),
    agentId
  };
}

/**
 * Derive agent ID from public key
 * @param {string} publicKeyBase64 
 * @returns {string}
 */
export function deriveAgentId(publicKeyBase64) {
  const hash = createHash('sha256')
    .update(publicKeyBase64)
    .digest('base64url')
    .slice(0, 22); // 22 chars = 132 bits of entropy
  return AGENT_ID_PREFIX + hash;
}

/**
 * Sign a message with private key
 * @param {string} message 
 * @param {string} privateKeyBase64 
 * @returns {string}
 */
export function signMessage(message, privateKeyBase64) {
  const privateKeyDer = Buffer.from(privateKeyBase64, 'base64');
  const privateKey = {
    key: privateKeyDer,
    format: 'der',
    type: 'pkcs8'
  };
  
  const signature = sign(null, Buffer.from(message), privateKey);
  return signature.toString('base64');
}

/**
 * Verify a signature
 * @param {string} message 
 * @param {string} signature 
 * @param {string} publicKeyBase64 
 * @returns {boolean}
 */
export function verifySignature(message, signature, publicKeyBase64) {
  try {
    const publicKeyDer = Buffer.from(publicKeyBase64, 'base64');
    const publicKey = {
      key: publicKeyDer,
      format: 'der',
      type: 'spki'
    };
    
    return verify(null, Buffer.from(message), publicKey, Buffer.from(signature, 'base64'));
  } catch (e) {
    return false;
  }
}

/**
 * Create enrollment request
 * @param {string} privateKeyBase64 
 * @param {{ name?: string, framework?: string }} metadata 
 * @returns {{ pubkey: string, agentId: string, metadata: object, timestamp: string, signature: string }}
 */
export function createEnrollmentRequest(publicKeyBase64, privateKeyBase64, metadata = {}) {
  const timestamp = new Date().toISOString();
  const agentId = deriveAgentId(publicKeyBase64);
  
  const payload = JSON.stringify({
    pubkey: publicKeyBase64,
    agentId,
    metadata,
    timestamp
  });
  
  const signature = signMessage(payload, privateKeyBase64);
  
  return {
    pubkey: publicKeyBase64,
    agentId,
    metadata,
    timestamp,
    signature
  };
}

/**
 * Create a signed challenge response
 * @param {string} challenge 
 * @param {string} agentId 
 * @param {string} privateKeyBase64 
 * @returns {{ agentId: string, challenge: string, signature: string }}
 */
export function signChallenge(challenge, agentId, privateKeyBase64) {
  const message = `${agentId}:${challenge}`;
  const signature = signMessage(message, privateKeyBase64);
  
  return {
    agentId,
    challenge,
    signature
  };
}

export default {
  generateIdentity,
  deriveAgentId,
  signMessage,
  verifySignature,
  createEnrollmentRequest,
  signChallenge
};
