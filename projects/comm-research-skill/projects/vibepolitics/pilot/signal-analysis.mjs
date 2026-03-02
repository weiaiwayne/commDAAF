#!/usr/bin/env node
/**
 * VibePolitics Pilot Study - Signal Detection Analysis
 * Implements simplified versions of our proposed algorithms
 */

import { readFileSync, writeFileSync } from 'fs';

// Load market data
const data = JSON.parse(readFileSync('/root/.openclaw/workspace/projects/vibepolitics/pilot/polymarket_data.json', 'utf8'));

console.log('🔬 VibePolitics Signal Detection Analysis');
console.log('═'.repeat(70));
console.log(`Data fetched: ${data.fetchedAt}`);
console.log(`Politics markets: ${data.politics.count} | Economy markets: ${data.economy.count}\n`);

// Combine all markets for analysis
const allMarkets = [...data.politics.markets, ...data.economy.markets];

// ============================================================================
// SIGNAL 1: Volume-Price Decoupling Index (VPDI)
// High volume with small price change suggests contested information
// ============================================================================
function calculateVPDI(market) {
  const vol24h = market.volume24hr || 0;
  const priceChange = Math.abs(market.oneDayPriceChange || 0);
  const liquidity = market.liquidity || 1;
  
  // Normalize volume by liquidity
  const normalizedVol = vol24h / liquidity;
  
  // VPDI = high when volume is high but price change is low
  // (suggests buyers and sellers are evenly matched = contested)
  if (priceChange < 0.001) return normalizedVol > 0.5 ? 1.0 : 0;
  
  const vpdi = normalizedVol / (priceChange * 10 + 0.1);
  return Math.min(vpdi, 1.0); // Cap at 1.0
}

// ============================================================================
// SIGNAL 2: Rapid Directional Shift (RDS)
// Large price change in 24h suggests potential opinion shift
// ============================================================================
function calculateRDS(market) {
  const priceChange = market.oneDayPriceChange || 0;
  const vol24h = market.volume24hr || 0;
  const liquidity = market.liquidity || 1;
  
  // RDS is high when price moved significantly with volume support
  const magnitude = Math.abs(priceChange);
  const volumeSupport = Math.min(vol24h / (liquidity * 2), 1);
  
  // Threshold: >5% move with volume is notable
  if (magnitude < 0.03) return 0;
  
  return Math.min(magnitude * volumeSupport * 5, 1.0);
}

// ============================================================================
// SIGNAL 3: Market Significance Score (MSS)
// Combination of volume, liquidity, and market maturity
// ============================================================================
function calculateMSS(market) {
  const vol = market.volume || 0;
  const liq = market.liquidity || 0;
  const vol24h = market.volume24hr || 0;
  
  // Log-scale volume (millions)
  const volScore = Math.min(Math.log10(vol + 1) / 7, 1); // 10M = 1.0
  const liqScore = Math.min(Math.log10(liq + 1) / 5, 1); // 100K = 1.0
  const activityScore = Math.min(vol24h / 50000, 1); // 50K/day = 1.0
  
  return (volScore * 0.4 + liqScore * 0.3 + activityScore * 0.3);
}

// ============================================================================
// SIGNAL 4: Uncertainty Index (UI)
// Markets near 50% with tight spreads indicate genuine uncertainty
// ============================================================================
function calculateUI(market) {
  const price = market.midPrice;
  if (!price) return 0;
  
  // Distance from 50%
  const distFrom50 = Math.abs(price - 0.5);
  
  // UI is high when price is near 50%
  const uncertaintyFromPrice = 1 - (distFrom50 * 2);
  
  // Boost if there's volume (people trading at uncertain price)
  const volBoost = market.volume24hr > 10000 ? 1.2 : 1.0;
  
  return Math.min(uncertaintyFromPrice * volBoost, 1.0);
}

// ============================================================================
// SIGNAL 5: Attention Score (based on 24h activity)
// ============================================================================
function calculateAttention(market) {
  const vol24h = market.volume24hr || 0;
  const totalVol = market.volume || 1;
  
  // What % of all-time volume happened in last 24h?
  const recentActivity = vol24h / totalVol;
  
  // High attention = lots of recent activity relative to history
  return Math.min(recentActivity * 10, 1.0);
}

// ============================================================================
// Run Analysis
// ============================================================================
console.log('🎯 SIGNAL ANALYSIS RESULTS');
console.log('─'.repeat(70));

const analyzed = allMarkets.map(m => ({
  ...m,
  signals: {
    VPDI: calculateVPDI(m),
    RDS: calculateRDS(m),
    MSS: calculateMSS(m),
    UI: calculateUI(m),
    ATT: calculateAttention(m)
  },
  compositeScore: 0
}));

// Calculate composite score
analyzed.forEach(m => {
  const s = m.signals;
  // Weighted combination
  m.compositeScore = (
    s.RDS * 0.35 +    // Rapid shifts most important
    s.VPDI * 0.25 +   // Contested markets interesting
    s.MSS * 0.20 +    // Significance matters
    s.UI * 0.10 +     // Uncertainty adds interest
    s.ATT * 0.10      // Recent attention
  );
});

// Sort by composite score
analyzed.sort((a, b) => b.compositeScore - a.compositeScore);

// ============================================================================
// OUTPUT: Top Signal Markets
// ============================================================================
console.log('\n🚨 TOP 20 MARKETS BY SIGNAL STRENGTH\n');
console.log('Score | RDS  | VPDI | MSS  | UI   | ATT  | Market');
console.log('─'.repeat(90));

analyzed.slice(0, 20).forEach((m, i) => {
  const s = m.signals;
  const score = m.compositeScore.toFixed(2);
  const row = [
    score.padStart(5),
    s.RDS.toFixed(2),
    s.VPDI.toFixed(2),
    s.MSS.toFixed(2),
    s.UI.toFixed(2),
    s.ATT.toFixed(2),
    m.question?.slice(0, 50) || 'Unknown'
  ].join(' | ');
  console.log(`${(i+1).toString().padStart(2)}. ${row}`);
});

// ============================================================================
// Identify Notable Patterns
// ============================================================================
console.log('\n\n📊 PATTERN DETECTION');
console.log('═'.repeat(70));

// High RDS (rapid shift)
const rapidShifts = analyzed.filter(m => m.signals.RDS > 0.3);
console.log(`\n🔴 RAPID SHIFTS (RDS > 0.3): ${rapidShifts.length} markets`);
rapidShifts.slice(0, 10).forEach(m => {
  const change = m.oneDayPriceChange ? `${(m.oneDayPriceChange * 100).toFixed(1)}%` : '?';
  console.log(`   • [${change}] ${m.question?.slice(0, 60)}`);
});

// High VPDI (contested)
const contested = analyzed.filter(m => m.signals.VPDI > 0.5 && m.signals.MSS > 0.3);
console.log(`\n🟡 CONTESTED MARKETS (high VPDI + significant): ${contested.length} markets`);
contested.slice(0, 10).forEach(m => {
  const price = m.midPrice ? `${(m.midPrice * 100).toFixed(0)}%` : '?';
  console.log(`   • [${price}] ${m.question?.slice(0, 60)}`);
});

// High uncertainty (near 50%)
const uncertain = analyzed.filter(m => m.signals.UI > 0.7 && m.signals.MSS > 0.3);
console.log(`\n🟠 HIGH UNCERTAINTY (near 50%, significant): ${uncertain.length} markets`);
uncertain.slice(0, 10).forEach(m => {
  const price = m.midPrice ? `${(m.midPrice * 100).toFixed(0)}%` : '?';
  console.log(`   • [${price}] ${m.question?.slice(0, 60)}`);
});

// ============================================================================
// Save Results
// ============================================================================
const results = {
  analysisTime: new Date().toISOString(),
  summary: {
    totalAnalyzed: analyzed.length,
    rapidShifts: rapidShifts.length,
    contestedMarkets: contested.length,
    highUncertainty: uncertain.length
  },
  topSignals: analyzed.slice(0, 30).map(m => ({
    question: m.question,
    slug: m.slug,
    compositeScore: m.compositeScore,
    signals: m.signals,
    price: m.midPrice,
    priceChange24h: m.oneDayPriceChange,
    volume: m.volume,
    volume24h: m.volume24hr,
    liquidity: m.liquidity
  })),
  rapidShifts: rapidShifts.slice(0, 15).map(m => ({
    question: m.question,
    priceChange: m.oneDayPriceChange,
    volume24h: m.volume24hr,
    rds: m.signals.RDS
  })),
  contested: contested.slice(0, 15).map(m => ({
    question: m.question,
    price: m.midPrice,
    vpdi: m.signals.VPDI
  })),
  uncertain: uncertain.slice(0, 15).map(m => ({
    question: m.question,
    price: m.midPrice,
    ui: m.signals.UI
  }))
};

writeFileSync('/root/.openclaw/workspace/projects/vibepolitics/pilot/signal_analysis_results.json',
  JSON.stringify(results, null, 2));

console.log('\n\n✅ Full results saved to pilot/signal_analysis_results.json');
console.log('\n' + '═'.repeat(70));
console.log('🤖 READY FOR AUTONOMOUS INTERPRETATION');
console.log('═'.repeat(70));
