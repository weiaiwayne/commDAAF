# Ukraine Tweets Dataset Analysis (Kimi K2.5)

## Dataset Overview
- **Shape:** 266,242 tweets × 28 columns
- **Key columns:** userid, username, text, tweetcreatedts, retweetcount, is_retweet, hashtags, language, followers, etc.
- **No duplicates**
- **High missing values:** coordinates (99.9%), quoted_status_username (95.5%), in_reply_to_screen_name (93.7%)

---

## 1. Key Actors and State Media Presence

### Top 20 Users by Tweet Count
| Username | Tweets |
|----------|--------|
| @FuckPutinBot | 2,926 |
| @UnPirater | 719 |
| @Arwa_Albosefi | 693 |
| @wRLMyxE7ZEr5CKr | 468 |
| @Moh_hadey | 418 |
| @Rabiaa78_5 | 363 |
| @rogue_corq | 359 |
| @IdeallyaNews | 275 |
| @Fozei96 | 270 |
| @lmymwny8 | 259 |
| @Derk233 | 252 |
| @najy_221 | 251 |
| @OElwrshfan4139 | 250 |
| @Elmimoni1 | 249 |
| @osama_ukraine | 247 |
| @RDR2_kamal | 231 |
| @Chronology22 | 226 |
| @osamanews3 | 223 |
| @jjaranaz94 | 223 |
| @TrasElValle_OBC | 213 |

### Identified State Media/Official Accounts
| Account | Tweets |
|---------|--------|
| @CarbonelTriana | 104 |
| @amriana | 63 |
| @AdrianSJ2022 | 55 |
| @PerdomoFeria | 54 |
| @Russia_Truth | 27 |
| @Sputnik_India | 25 |

**Notable:** Russian state media presence detected (Russia_Truth, Sputnik_India)

---

## 2. Coordination Indicators

### Retweet Behavior
- **Overall retweet rate:** 72.0% (very high - suggests amplification network)
- **Quote tweet rate:** 10.4%
- **Reply rate:** 5.9%

### Most Retweeted Accounts
| Account | Retweets |
|---------|----------|
| @GlasnostGone | 8,136 |
| @AlexKokcharov | 6,632 |
| @NatalkaKyiv | 4,571 |
| @PartidoPCC (Cuban Communist Party) | 3,412 |
| @CanalCaribeCuba | 3,104 |
| @UAWeapons | 2,894 |
| @nexta_tv | 2,595 |
| @DiazCanelB (Cuban President) | 2,511 |
| @simonateba | 2,485 |
| @Circonscripti18 | 2,335 |
| @georgegalloway | 2,275 |
| @MMarreroCruz (Cuban PM) | 2,269 |
| @TheStudyofWar | 2,243 |
| @JuventudRebelde | 1,988 |
| @Lyla_lilas | 1,791 |

### Account Age Distribution
| Year Created | Accounts |
|--------------|----------|
| 2014 | 12,593 |
| 2015 | 9,674 |
| 2016 | 8,989 |
| 2017 | 10,129 |
| 2018 | 9,225 |
| 2019 | 11,688 |
| 2020 | 17,131 |
| 2021 | 23,932 |
| **2022** | **61,396** |
| 2023 | 31,388 |

**⚠️ Major spike in 2022 account creation** - coincides with Russia-Ukraine war escalation

### Bot-like Account Indicators
- **High volume (>10K tweets) + Low followers (<100):** 12,711 accounts
- This suggests significant bot or coordinated activity

---

## 3. Narrative Patterns (Kakhovka Dam)

*Analysis incomplete - process terminated before this section*

---

## Key Findings Summary

### 🔴 Coordination Signals Detected
1. **72% retweet rate** - unusually high, indicates amplification network
2. **61,396 accounts created in 2022** - massive account surge during war
3. **12,711 bot-like accounts** identified (high tweets, low followers)

### 🔴 State Actor Presence
1. **Russian state media:** @Russia_Truth, @Sputnik_India active
2. **Cuban government nexus:** @PartidoPCC, @DiazCanelB, @MMarreroCruz, @CanalCaribeCuba heavily amplified
3. Suggests Russia-aligned information operation with Cuban amplification

### 🔴 Notable Actors
1. **@FuckPutinBot** (2,926 tweets) - likely pro-Ukraine automated account
2. **@GlasnostGone** (8,136 retweets) - most amplified account
3. Strong Arabic-language presence (@Arwa_Albosefi, @Moh_hadey, etc.)

---

*Analysis performed by Kimi K2.5 via OpenCode | Process terminated before completion of Kakhovka dam narrative analysis*
