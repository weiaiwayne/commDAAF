#!/usr/bin/env python3
"""AgentAcademy Validation: Engagement Decomposition Analysis"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

# Load data
df = pd.read_csv('/root/.openclaw/workspace/skills/commdaaf/projects/novel-rq-study-2/processed_data.csv')

print("=" * 70)
print("AGENTACADEMY VALIDATION: ENGAGEMENT DECOMPOSITION ANALYSIS")
print("=" * 70)
print(f"\nDataset: {len(df)} observations\n")
print(f"Variables: rt_like_ratio (DV), hashtag_count, has_mention, has_url,")
print(f"           text_length, has_emoji, log_followers")
print("\n" + "=" * 70)

# ============================================================================
# H1: Hashtag Count → Higher RT/Like Ratio
# ============================================================================
print("\n[H1] HASHTAG COUNT → HIGHER RT/LIKE RATIO")
print("-" * 50)

# Correlation
corr, pval = stats.pearsonr(df['hashtag_count'], df['rt_like_ratio'])
print(f"Pearson r: {corr:.4f} (p = {pval:.4f})")

# Spearman (non-parametric)
spearman_r, spearman_p = stats.spearmanr(df['hashtag_count'], df['rt_like_ratio'])
print(f"Spearman ρ: {spearman_r:.4f} (p = {spearman_p:.4f})")

print(f"\nHashtag Count Statistics:")
print(f"  Mean: {df['hashtag_count'].mean():.2f}")
print(f"  SD: {df['hashtag_count'].std():.2f}")
print(f"  Range: {df['hashtag_count'].min()} - {df['hashtag_count'].max()}")

# Hashtag count distribution by ratio tertiles (3 bins due to many zeros)
df['rt_ratio_bin'] = pd.cut(df['rt_like_ratio'], bins=[-0.1, 0.1, 0.5, 5.0], labels=['Zero/Near-Zero','Medium','High'])
quartile_hashtags = df.groupby('rt_ratio_bin')['hashtag_count'].mean()
print(f"\nMean hashtag count by RT/Like ratio bins:")
for q, val in quartile_hashtags.items():
    if pd.notna(q):
        print(f"  {q}: {val:.2f}")
print(f"\nMean hashtag count by RT/Like ratio bins:")
for q, val in quartile_hashtags.items():
    print(f"  {q}: {val:.2f}")

h1_verdict = "SUPPORTED" if spearman_r > 0 and spearman_p < 0.05 else "NOT SUPPORTED" if spearman_p < 0.05 else "PARTIAL"
print(f"\n>>> H1 VERDICT: {h1_verdict}")

# ============================================================================
# H2: Mentions → Lower RT/Like Ratio
# ============================================================================
print("\n" + "=" * 70)
print("\n[H2] MENTIONS → LOWER RT/LIKE RATIO")
print("-" * 50)

# Group comparison
has_mention = df[df['has_mention'] == True]['rt_like_ratio']
no_mention = df[df['has_mention'] == False]['rt_like_ratio']

print(f"With mentions: n={len(has_mention)}, M={has_mention.mean():.4f}, SD={has_mention.std():.4f}")
print(f"Without mentions: n={len(no_mention)}, M={no_mention.mean():.4f}, SD={no_mention.std():.4f}")

# T-test
t_stat, t_pval = stats.ttest_ind(has_mention, no_mention)
print(f"\nIndependent t-test: t = {t_stat:.4f}, p = {t_pval:.4f}")

# Effect size (Cohen's d)
pooled_std = np.sqrt(((len(has_mention)-1)*has_mention.var() + (len(no_mention)-1)*no_mention.var()) / (len(has_mention)+len(no_mention)-2))
cohens_d = (has_mention.mean() - no_mention.mean()) / pooled_std
print(f"Cohen's d: {cohens_d:.4f}")

# Mann-Whitney U (non-parametric)
u_stat, u_pval = stats.mannwhitneyu(has_mention, no_mention, alternative='two-sided')
print(f"Mann-Whitney U: U = {u_stat:.0f}, p = {u_pval:.4f}")

h2_verdict = "SUPPORTED" if t_stat < 0 and t_pval < 0.05 else "NOT SUPPORTED" if t_stat > 0 and t_pval < 0.05 else "PARTIAL" if t_pval < 0.05 else "NOT SUPPORTED"
print(f"\n>>> H2 VERDICT: {h2_verdict}")

# ============================================================================
# H3: Follower × Hashtag Interaction (2x2)
# ============================================================================
print("\n" + "=" * 70)
print("\n[H3] FOLLOWER × HASHTAG INTERACTION (2×2 TABLE)")
print("-" * 50)

# Create dichotomous variables
median_followers = df['log_followers'].median()
median_hashtags = df['hashtag_count'].median()

df['high_followers'] = df['log_followers'] > median_followers
df['high_hashtags'] = df['hashtag_count'] > median_hashtags

# 2x2 table
print(f"\nMedian splits: log_followers > {median_followers:.2f}, hashtag_count > {median_hashtags:.2f}")
print(f"\n2×2 Table: Mean RT/Like Ratio")
print("-" * 40)

interaction_table = df.groupby(['high_followers', 'high_hashtags'])['rt_like_ratio'].agg(['mean', 'std', 'count'])
interaction_table.index = interaction_table.index.map({(False, False): 'Low F / Low H', 
                                                       (False, True): 'Low F / High H',
                                                       (True, False): 'High F / Low H',
                                                       (True, True): 'High F / High H'})
print(interaction_table)

# Simple effects
print(f"\nCell Means:")
for idx, row in interaction_table.iterrows():
    print(f"  {idx}: M = {row['mean']:.4f}, SD = {row['std']:.4f}, n = {int(row['count'])}")

# Two-way ANOVA approximation
import statsmodels.formula.api as smf
model = smf.ols('rt_like_ratio ~ C(high_followers) * C(high_hashtags)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(f"\nTwo-way ANOVA:")
print(anova_table)

# Check interaction
interaction_p = anova_table.loc['C(high_followers):C(high_hashtags)', 'PR(>F)']
h3_verdict = "SUPPORTED" if interaction_p < 0.05 else "NOT SUPPORTED"
print(f"\n>>> H3 VERDICT: {h3_verdict} (interaction p = {interaction_p:.4f})")

# ============================================================================
# H4: Text Length → Lower RT/Like Ratio
# ============================================================================
print("\n" + "=" * 70)
print("\n[H4] TEXT LENGTH → LOWER RT/LIKE RATIO")
print("-" * 50)

# Correlation
corr_len, pval_len = stats.pearsonr(df['text_length'], df['rt_like_ratio'])
print(f"Pearson r: {corr_len:.4f} (p = {pval_len:.4f})")

# Spearman
spearman_r_len, spearman_p_len = stats.spearmanr(df['text_length'], df['rt_like_ratio'])
print(f"Spearman ρ: {spearman_r_len:.4f} (p = {spearman_p_len:.4f})")

print(f"\nText Length Statistics:")
print(f"  Mean: {df['text_length'].mean():.1f}")
print(f"  SD: {df['text_length'].std():.1f}")
print(f"  Range: {df['text_length'].min()} - {df['text_length'].max()}")

h4_verdict = "SUPPORTED" if corr_len < 0 and pval_len < 0.05 else "NOT SUPPORTED" if corr_len > 0 and pval_len < 0.05 else "PARTIAL" if pval_len < 0.05 else "NOT SUPPORTED"
print(f"\n>>> H4 VERDICT: {h4_verdict}")

# ============================================================================
# UNEXPECTED: Emoji Effect
# ============================================================================
print("\n" + "=" * 70)
print("\n[UNEXPECTED] EMOJI EFFECT")
print("-" * 50)

has_emoji = df[df['has_emoji'] == True]['rt_like_ratio']
no_emoji = df[df['has_emoji'] == False]['rt_like_ratio']

print(f"With emoji: n={len(has_emoji)}, M={has_emoji.mean():.4f}, SD={has_emoji.std():.4f}")
print(f"Without emoji: n={len(no_emoji)}, M={no_emoji.mean():.4f}, SD={no_emoji.std():.4f}")

# T-test
t_stat_emoji, t_pval_emoji = stats.ttest_ind(has_emoji, no_emoji)
print(f"\nIndependent t-test: t = {t_stat_emoji:.4f}, p = {t_pval_emoji:.4f}")

# Mann-Whitney
u_stat_emoji, u_pval_emoji = stats.mannwhitneyu(has_emoji, no_emoji, alternative='two-sided')
print(f"Mann-Whitney U: p = {u_pval_emoji:.4f}")

emoji_verdict = "SIGNIFICANT" if t_pval_emoji < 0.05 else "NOT SIGNIFICANT"
print(f"\n>>> EMOJI EFFECT: {emoji_verdict} (lower ratio with emoji: {t_stat_emoji < 0})")

# ============================================================================
# FULL REGRESSION MODEL
# ============================================================================
print("\n" + "=" * 70)
print("\n[FULL REGRESSION MODEL]")
print("-" * 50)
print("DV: rt_like_ratio")
print("IVs: hashtag_count, has_mention, has_url, text_length, has_emoji, log_followers")
print("-" * 50)

# Prepare variables
X = df[['hashtag_count', 'has_mention', 'has_url', 'text_length', 'has_emoji', 'log_followers']].copy()
X['has_mention'] = X['has_mention'].astype(int)
X['has_url'] = X['has_url'].astype(int)
X['has_emoji'] = X['has_emoji'].astype(int)

y = df['rt_like_ratio']

# Add constant
X_const = add_constant(X)

# Fit OLS
model = OLS(y, X_const).fit()
print(model.summary())

# ============================================================================
# MODEL DIAGNOSTICS
# ============================================================================
print("\n" + "=" * 70)
print("\n[MODEL DIAGNOSTICS]")
print("-" * 50)
print(f"R-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")
print(f"F-statistic: {model.fvalue:.4f} (p = {model.f_pvalue:.4e})")
print(f"AIC: {model.aic:.2f}, BIC: {model.bic:.2f}")

# VIF for multicollinearity
from statsmodels.stats.outliers_influence import variance_inflation_factor
print(f"\nVariance Inflation Factors (VIF):")
for i, var in enumerate(X.columns):
    vif = variance_inflation_factor(X_const.values, i+1)
    print(f"  {var}: {vif:.3f}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("\n[SUMMARY OF FINDINGS]")
print("=" * 70)
print(f"\nH1 (Hashtag Count → Higher RT/Like):     {h1_verdict}")
print(f"H2 (Mentions → Lower RT/Like):           {h2_verdict}")
print(f"H3 (Follower × Hashtag Interaction):     {h3_verdict}")
print(f"H4 (Text Length → Lower RT/Like):        {h4_verdict}")
print(f"Emoji Effect:                            {emoji_verdict}")

print("\n" + "=" * 70)
print("KEY REGRESSION COEFFICIENTS (p < 0.05)")
print("=" * 70)
significant = model.pvalues[model.pvalues < 0.05]
for var in significant.index:
    if var != 'const':
        coef = model.params[var]
        pval = model.pvalues[var]
        print(f"  {var}: β = {coef:.6f}, p = {pval:.4f}")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
