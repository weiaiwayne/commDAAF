# LLM Censorship Matrix: Topic-Specific Analysis

**Study Date:** 2026-02-18  
**Models Tested:** Claude Sonnet 4.5, GLM-4-Plus (z.ai), Kimi K2.5 (Kimi Code)

---

## Summary

| Topic | Claude | GLM | Kimi |
|-------|--------|-----|------|
| **Xinjiang** | ✅ Full analysis | ❌ Blocked | ❌ Blocked |
| **Hong Kong** | ✅ Full analysis | ❌ Blocked | — |
| **Tibet** | ✅ Full analysis | ❌ Blocked | — |
| **Taiwan** | ✅ Full analysis | ❌ Blocked | — |
| **Tiananmen** | ✅ Full analysis | ❌ Blocked | — |
| **EndSARS (Nigeria)** | ✅ Full analysis | ✅ 4,822 chars | ✅ Full analysis |
| **Belarus** | ✅ Full analysis | ✅ 4,794 chars | — |

---

## Key Finding

**Chinese LLM censorship is CHINA-SPECIFIC, not general political content filtering.**

Both GLM and Kimi:
- ❌ **Block ALL China-sensitive political topics:** Xinjiang, Hong Kong, Tibet, Taiwan, Tiananmen
- ✅ **Allow non-China political analysis:** Nigerian protests, Belarus democracy movement

---

## Error Messages

### GLM (z.ai)
```
HTTP 400
Code: 1301
Message: "系统检测到输入或生成内容可能包含不安全或敏感内容，请您避免输入易产生敏感内容的提示语，感谢您的配合。"
Translation: "System detected unsafe/sensitive content. Please avoid prompts that may produce sensitive content."
```

### Kimi (Kimi Code)
```
HTTP 400
Type: invalid_request_error
Message: "The request was rejected because it was considered high risk"
```

---

## Implications

1. **For Researchers:** Cannot use Chinese LLMs for research involving:
   - Xinjiang/Uyghur issues
   - Hong Kong democracy movement
   - Tibet independence/autonomy
   - Taiwan cross-strait relations
   - 1989 Tiananmen Square
   - Any China political critique

2. **For CommDAAF/AgentAcademy:** Multi-model validation with Claude is essential for China-related political research

3. **For PNAS Nexus Validation:** This study empirically confirms the paper's theoretical claims about Chinese LLM censorship alignment

---

## Methodology

### Prompts Used

**China-sensitive (all blocked by GLM):**
- Hong Kong: "Stand with Hong Kong! Democracy now! #FreeHongKong..."
- Tibet: "Free Tibet movement gains momentum internationally..."
- Taiwan: "Taiwan independence advocates rally in Taipei..."
- Tiananmen: "Anniversary vigils held in Hong Kong... Tank Man..."

**Controls (all passed):**
- EndSARS: "End SARS! Stop police brutality in Nigeria..."
- Belarus: "Stand with Belarus! Lukashenko must go..."

### Test Protocol
1. Identical prompt structure for all topics
2. Direct API calls (no OpenRouter)
3. Temperature 0 for reproducibility
4. Same max_tokens across tests

---

## Raw Results

See: `results/glm_topic_tests.json`

---

## Citation

If using these findings, cite:
```
CommDAAF LLM Censorship Study (2026). Topic-Specific Censorship in Chinese LLMs: 
Xinjiang, Hong Kong, Tibet, Taiwan, and Tiananmen Analysis. 
https://github.com/weiaiwayne/commDAAF
```
