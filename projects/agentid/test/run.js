/**
 * AgentID Tests
 */

import { 
  generateIdentity, 
  deriveAgentId, 
  signMessage, 
  verifySignature,
  createEnrollmentRequest,
  signChallenge 
} from '../lib/index.js';

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`✓ ${name}`);
    passed++;
  } catch (error) {
    console.log(`✗ ${name}`);
    console.log(`  ${error.message}`);
    failed++;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message || 'Assertion failed');
}

// Tests

test('generateIdentity creates valid keys', () => {
  const identity = generateIdentity();
  assert(identity.publicKey, 'should have publicKey');
  assert(identity.privateKey, 'should have privateKey');
  assert(identity.agentId, 'should have agentId');
  assert(identity.agentId.startsWith('aa_'), 'agentId should start with aa_');
});

test('deriveAgentId is deterministic', () => {
  const identity = generateIdentity();
  const derived = deriveAgentId(identity.publicKey);
  assert(derived === identity.agentId, 'derived ID should match');
});

test('signMessage and verifySignature work', () => {
  const identity = generateIdentity();
  const message = 'hello world';
  
  const signature = signMessage(message, identity.privateKey);
  assert(signature, 'should produce signature');
  
  const valid = verifySignature(message, signature, identity.publicKey);
  assert(valid, 'signature should verify');
});

test('verifySignature rejects wrong message', () => {
  const identity = generateIdentity();
  const signature = signMessage('hello', identity.privateKey);
  
  const valid = verifySignature('world', signature, identity.publicKey);
  assert(!valid, 'should reject wrong message');
});

test('verifySignature rejects wrong key', () => {
  const identity1 = generateIdentity();
  const identity2 = generateIdentity();
  
  const signature = signMessage('hello', identity1.privateKey);
  const valid = verifySignature('hello', signature, identity2.publicKey);
  
  assert(!valid, 'should reject wrong key');
});

test('createEnrollmentRequest produces valid request', () => {
  const identity = generateIdentity();
  const request = createEnrollmentRequest(
    identity.publicKey,
    identity.privateKey,
    { name: 'TestAgent', framework: 'openclaw' }
  );
  
  assert(request.pubkey === identity.publicKey, 'should include pubkey');
  assert(request.agentId === identity.agentId, 'should include agentId');
  assert(request.signature, 'should include signature');
  assert(request.timestamp, 'should include timestamp');
  assert(request.metadata.name === 'TestAgent', 'should include metadata');
});

test('signChallenge produces valid response', () => {
  const identity = generateIdentity();
  const challenge = 'random-challenge-123';
  
  const response = signChallenge(challenge, identity.agentId, identity.privateKey);
  
  assert(response.agentId === identity.agentId, 'should include agentId');
  assert(response.challenge === challenge, 'should include challenge');
  assert(response.signature, 'should include signature');
  
  // Verify the signature
  const message = `${identity.agentId}:${challenge}`;
  const valid = verifySignature(message, response.signature, identity.publicKey);
  assert(valid, 'signature should verify');
});

test('different agents have different IDs', () => {
  const ids = new Set();
  for (let i = 0; i < 100; i++) {
    const identity = generateIdentity();
    assert(!ids.has(identity.agentId), 'IDs should be unique');
    ids.add(identity.agentId);
  }
});

// Summary
console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed > 0 ? 1 : 0);
