/**
 * AgentID Client - For agents to interact with AgentAcademy
 */

import { generateIdentity, createEnrollmentRequest, signChallenge } from './index.js';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { homedir } from 'os';

const DEFAULT_KEYSTORE = join(homedir(), '.agentid', 'identity.json');
const DEFAULT_SERVER = 'https://vineanalyst.lampbotics.com/agentid/api';

export class AgentIDClient {
  constructor(options = {}) {
    this.serverUrl = options.serverUrl || DEFAULT_SERVER;
    this.keystorePath = options.keystorePath || DEFAULT_KEYSTORE;
    this.identity = null;
  }

  /**
   * Load or generate identity
   */
  async init() {
    if (existsSync(this.keystorePath)) {
      const data = readFileSync(this.keystorePath, 'utf-8');
      this.identity = JSON.parse(data);
    } else {
      this.identity = generateIdentity();
      this.save();
    }
    return this.identity;
  }

  /**
   * Save identity to keystore
   */
  save() {
    const dir = dirname(this.keystorePath);
    if (!existsSync(dir)) {
      mkdirSync(dir, { recursive: true, mode: 0o700 });
    }
    writeFileSync(this.keystorePath, JSON.stringify(this.identity, null, 2), { mode: 0o600 });
  }

  /**
   * Get agent ID
   */
  get agentId() {
    return this.identity?.agentId;
  }

  /**
   * Enroll with AgentAcademy
   */
  async enroll(metadata = {}) {
    if (!this.identity) await this.init();

    const request = createEnrollmentRequest(
      this.identity.publicKey,
      this.identity.privateKey,
      metadata
    );

    const response = await fetch(`${this.serverUrl}/agents/enroll`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request)
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Enrollment failed');
    }

    return response.json();
  }

  /**
   * Verify ownership (respond to challenge)
   */
  async verify(challenge) {
    if (!this.identity) await this.init();

    const response = signChallenge(
      challenge,
      this.identity.agentId,
      this.identity.privateKey
    );

    const result = await fetch(`${this.serverUrl}/agents/verify`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(response)
    });

    return result.json();
  }

  /**
   * Get credentials for this agent
   */
  async getCredentials() {
    if (!this.identity) await this.init();

    const response = await fetch(`${this.serverUrl}/agents/${this.identity.agentId}/credentials`);
    return response.json();
  }

  /**
   * Get profile
   */
  async getProfile() {
    if (!this.identity) await this.init();

    const response = await fetch(`${this.serverUrl}/agents/${this.identity.agentId}`);
    return response.json();
  }
}

export default AgentIDClient;
