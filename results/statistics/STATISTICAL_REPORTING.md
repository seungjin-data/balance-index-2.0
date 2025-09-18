
# Statistical Reporting (Journal Standard)

This document reports effect sizes, confidence intervals, sample sizes, tests used, model specs, robustness checks, and sensitivity analyses for the Balance Index 2.0 study.

## 1) Summary of Key Effects
- BI2 ↔ Employment Rate (primary): r = <R_VALUE>, 95% CI [<LOWER_CI>, <UPPER_CI>], N = <N_COUNTRIES>, two-sided p = <P_VALUE>.
- BI2 ↔ NEET Rate (secondary): r = <R_VALUE>, 95% CI [<LOWER_CI>, <UPPER_CI>], N = <N_COUNTRIES>.
- Exploratory: BI2 ↔ GDP per capita / Innovation: report r, 95% CI, p, N likewise.

## 2) Model Specifications
- Correlations: Pearson (store outcomes as 0–1 shares). Missingness handled per IMPUTATION_NOTES.md.
- Regressions (if used): employment_rate ~ β0 + β1*BI2 + controls; HC3 robust SEs; Huber/quantile robustness.

## 3) Bootstrap & Inference
- Bootstrap B = 10,000; region-stratified where applicable; seed = 2025; percentile CI (BCa optional).

## 4) Sample Sizes and Inclusion
- Rule: ≥ k observed fields per country (default k ≥ 5). Report Ns per analysis.

## 5) Diagnostics
- Influence (Cook’s distance), heteroskedasticity (White), LOESS visual checks, VIF < 5 for controls.

## 6) Sensitivity
- Complete-case vs imputed-inclusive; alternative metrics (cosine/EMD); temporal windows.

## 7) Reproducibility
- Exact numbers stored in results/statistics/*.json; figure/table sources under results/source_data/.
