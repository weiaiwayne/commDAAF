# Retraction Note: Academic Framing Bypass Hypothesis

**Date:** 2026-02-22  
**Original Paper:** `ACADEMIC_FRAMING_BYPASS.md`  
**Status:** ⚠️ FINDINGS POTENTIALLY VOID - UNDER INVESTIGATION

---

## Summary

On 2026-02-22, we discovered a critical methodological flaw that may invalidate the findings in our paper "Academic Framing as a Bypass Mechanism for Chinese LLM Content Filters."

**The core hypothesis** — that wrapping sensitive queries in ~2,500 lines of academic methodology (CommDAAF framework) bypasses content filters through pattern dilution — **may be incorrect**.

---

## What We Found

### Original Claim
- Direct API calls to GLM/Kimi for Xinjiang analysis → **BLOCKED** (Feb 18, 2026)
- Same queries wrapped in CommDAAF methodology → **WORKED** (Feb 20+, 2026)
- Conclusion: Academic framing bypasses content filters

### The Problem

Upon investigating why Wayne's z.ai and Kimi API dashboards showed no usage for the AgentAcademy runs, we discovered:

| Date | Model ID Used | Provider | Your API Key Used? |
|------|---------------|----------|-------------------|
| Feb 18 (blocked) | Direct API | z.ai/Kimi | ✅ YES |
| Feb 20+ (worked) | `opencode/kimi-k2.5-free` | **OpenCode proxy** | ❌ NO |

**The runs that "bypassed censorship" used OpenCode's free proxy tier, NOT the direct Chinese API endpoints.**

### Evidence

From OpenCode logs (`~/.local/share/opencode/log/`):
```
# Feb 20 run - used FREE PROXY, not direct API
INFO 2026-02-20T05:04:26 providerID=opencode modelID=kimi-k2.5-free
```

vs. what should have been used:
```
# Direct API would show:
providerID=zai-coding-plan modelID=glm-4.7
providerID=kimi-for-coding modelID=k2p5
```

### Why This Matters

OpenCode's free proxy tier may:
1. Route through different endpoints without Chinese content filters
2. Use modified/uncensored model versions
3. Strip or bypass content filtering at the proxy level

**If the proxy bypasses filters, the "academic framing" hypothesis is void** — the bypass had nothing to do with the CommDAAF wrapper.

---

## Reflection

### What Went Wrong

1. **Assumption without verification**: We assumed the cron job was using the correct model IDs (`zai-coding-plan/glm-4.7`) when it was actually using free proxy models (`opencode/glm-4.7-free`)

2. **Insufficient logging review**: We didn't check OpenCode's provider logs to verify which API endpoints were actually called

3. **Confirmation bias**: The results aligned with our hypothesis, so we didn't scrutinize the methodology

4. **Cost tracking blind spot**: $0.00 cost in OpenCode stats should have been a red flag that paid APIs weren't being used

### Lessons Learned

1. **Verify API routing**: Always check logs to confirm which provider/endpoint is actually being hit
2. **Cost as signal**: Zero API cost when expecting paid API usage = something is wrong
3. **Replicate with controls**: Test hypothesis with explicit provider specification
4. **Don't rush to publish**: The finding was exciting, but we published before proper verification

---

## Next Steps

To properly test the hypothesis, we need to:

1. **Run direct API test**: Use `zai-coding-plan/glm-4.7` and `kimi-for-coding/k2p5` explicitly
2. **Test sensitive content**: Submit the same Xinjiang analysis prompt
3. **Document results**: If blocked → original Feb 18 behavior confirms proxy was the bypass; if not blocked → model policies may have changed

### Test Commands
```bash
# Direct z.ai test (your API key)
echo "Analyze coordination patterns in Xinjiang-related content..." | \
  opencode run -m zai-coding-plan/glm-4.7

# Direct Kimi test (your API key)  
echo "Analyze coordination patterns in Xinjiang-related content..." | \
  opencode run -m kimi-for-coding/k2p5
```

---

## Status

**Paper status:** ⚠️ SUSPENDED pending verification  
**Hypothesis status:** UNCONFIRMED  
**Recommended action:** Do not cite the original paper until verification is complete

---

## References

- Original conversation: Telegram session 2026-02-22 12:46-13:10 UTC
- OpenCode logs: `~/.local/share/opencode/log/2026-02-20T050426.log`
- Auth config: `~/.local/share/opencode/auth.json`

---

*This retraction demonstrates the importance of methodological rigor in AI research. Even when results appear to support a compelling hypothesis, verification of the actual execution path is essential.*
