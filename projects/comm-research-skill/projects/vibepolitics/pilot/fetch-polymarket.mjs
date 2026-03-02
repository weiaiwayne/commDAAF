#!/usr/bin/env node
/**
 * VibePolitics Pilot Study - Polymarket Data Fetcher
 * Fetches US politics and economy prediction markets
 */

import { writeFileSync } from 'fs';

const GAMMA_API = 'https://gamma-api.polymarket.com';

// Fetch all active markets
async function fetchMarkets() {
  console.log('📊 Fetching Polymarket data...\n');
  
  // Get events related to US politics
  const politicsKeywords = [
    'trump', 'biden', 'congress', 'senate', 'house', 'republican', 'democrat',
    'election', 'president', 'governor', 'midterm', 'impeach', 'veto',
    'supreme court', 'legislation', 'policy', 'tariff', 'immigration',
    'deportation', 'executive order', 'cabinet', 'federal', 'approval'
  ];
  
  const economyKeywords = [
    'fed', 'interest rate', 'inflation', 'recession', 'gdp', 'unemployment',
    'stock', 'sp500', 's&p', 'nasdaq', 'bitcoin', 'crypto', 'treasury',
    'debt ceiling', 'deficit', 'trade', 'economy'
  ];
  
  let allMarkets = [];
  
  // Fetch active markets
  try {
    const response = await fetch(`${GAMMA_API}/markets?active=true&closed=false&limit=500`);
    if (!response.ok) throw new Error(`API error: ${response.status}`);
    const markets = await response.json();
    console.log(`Found ${markets.length} active markets total`);
    allMarkets = markets;
  } catch (e) {
    console.error('Error fetching markets:', e.message);
    return null;
  }
  
  // Filter for politics
  const politicsMarkets = allMarkets.filter(m => {
    const text = `${m.question || ''} ${m.description || ''}`.toLowerCase();
    return politicsKeywords.some(kw => text.includes(kw));
  });
  
  // Filter for economy
  const economyMarkets = allMarkets.filter(m => {
    const text = `${m.question || ''} ${m.description || ''}`.toLowerCase();
    return economyKeywords.some(kw => text.includes(kw));
  });
  
  console.log(`\n🏛️  Politics markets: ${politicsMarkets.length}`);
  console.log(`💰 Economy markets: ${economyMarkets.length}`);
  
  // Process markets for analysis
  const processMarket = (m) => ({
    id: m.id,
    slug: m.slug,
    question: m.question,
    description: m.description?.slice(0, 300),
    outcomes: m.outcomes,
    outcomePrices: m.outcomePrices,
    volume: parseFloat(m.volume) || 0,
    volume24hr: parseFloat(m.volume24hr) || 0,
    liquidity: parseFloat(m.liquidity) || 0,
    spread: m.spread,
    createdAt: m.createdAt,
    endDate: m.endDate,
    // Price data
    bestBid: m.bestBid,
    bestAsk: m.bestAsk,
    lastTradePrice: m.lastTradePrice,
    // Changes
    oneDayPriceChange: m.oneDayPriceChange,
    // Computed
    midPrice: m.outcomePrices ? parseFloat(m.outcomePrices[0]) : null,
    volumeToLiquidity: m.liquidity > 0 ? (parseFloat(m.volume24hr) || 0) / parseFloat(m.liquidity) : 0
  });
  
  const politics = politicsMarkets.map(processMarket).sort((a, b) => b.volume - a.volume);
  const economy = economyMarkets.map(processMarket).sort((a, b) => b.volume - a.volume);
  
  // Remove duplicates (some markets match both)
  const economyIds = new Set(economy.map(m => m.id));
  const politicsOnly = politics.filter(m => !economyIds.has(m.id) || politics.indexOf(m) < 20);
  
  const data = {
    fetchedAt: new Date().toISOString(),
    totalActive: allMarkets.length,
    politics: {
      count: politicsOnly.length,
      markets: politicsOnly.slice(0, 50) // Top 50 by volume
    },
    economy: {
      count: economy.length,
      markets: economy.slice(0, 30) // Top 30 by volume
    }
  };
  
  // Save raw data
  writeFileSync('/root/.openclaw/workspace/projects/vibepolitics/pilot/polymarket_data.json', 
    JSON.stringify(data, null, 2));
  
  console.log('\n✅ Data saved to pilot/polymarket_data.json');
  
  // Print top markets
  console.log('\n📈 TOP POLITICS MARKETS (by volume):');
  console.log('─'.repeat(80));
  politicsOnly.slice(0, 15).forEach((m, i) => {
    const price = m.midPrice ? `${(m.midPrice * 100).toFixed(1)}%` : '?';
    const change = m.oneDayPriceChange ? `${m.oneDayPriceChange > 0 ? '+' : ''}${(m.oneDayPriceChange * 100).toFixed(1)}%` : '';
    const vol = m.volume > 1e6 ? `$${(m.volume/1e6).toFixed(1)}M` : `$${(m.volume/1e3).toFixed(0)}K`;
    console.log(`${i+1}. [${price}] ${m.question?.slice(0, 55)}... | Vol: ${vol} ${change}`);
  });
  
  console.log('\n💹 TOP ECONOMY MARKETS (by volume):');
  console.log('─'.repeat(80));
  economy.slice(0, 10).forEach((m, i) => {
    const price = m.midPrice ? `${(m.midPrice * 100).toFixed(1)}%` : '?';
    const change = m.oneDayPriceChange ? `${m.oneDayPriceChange > 0 ? '+' : ''}${(m.oneDayPriceChange * 100).toFixed(1)}%` : '';
    const vol = m.volume > 1e6 ? `$${(m.volume/1e6).toFixed(1)}M` : `$${(m.volume/1e3).toFixed(0)}K`;
    console.log(`${i+1}. [${price}] ${m.question?.slice(0, 55)}... | Vol: ${vol} ${change}`);
  });
  
  return data;
}

// Run
fetchMarkets().catch(console.error);
