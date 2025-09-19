# Statistical Reporting

This note summarizes effect sizes, confidence intervals, sample sizes, tests used, model specifications, robustness checks, and sensitivity analyses for the Balance Index 2.0 (BI2) study.

## 1) Summary of Key Effects

- **Primary (Figure 2). BI2 ↔ Employment Rate:**  
  Pearson r = **-0.72**, 95% CI **[-0.78, -0.65]**, N = **133**, two-sided p **< 0.001**.

- **Secondary. BI2 ↔ NEET Rate:**  
  Pearson r = **+0.58**, 95% CI **[+0.47, +0.67]** (approx.), N = **133**, p **< 0.001**.

- **Exploratory. BI2 ↔ GDP per capita / Innovation Index:**  
  GDP per capita: r = **-0.41**, p **< 0.01**;  
  Innovation Index: r = **-0.52**, p **< 0.001**.  
  (Exact CIs are available from the bootstrap results and can be reproduced with the script below.)

## 2) Model Specifications

- **Correlations:** Pearson. Outcomes stored as **shares in [0,1]** (e.g., employment_rate).  
- **Regression robustness (optional):**  
  `employment_rate ~ β0 + β1*BI2 + controls` with **HC3 robust SEs**.  
  Additional checks: Huber and quantile regressions.

## 3) Bootstrap & Inference

- **Bootstrap:** B = **10,000**, region-stratified where applicable; random seed = **2025**.  
- **Intervals:** Percentile CI (BCa optional for figures).  
- **Multiple testing:** Not applied to the primary test; exploratory results are labeled accordingly.

## 4) Sample Sizes and Inclusion

- **Units:** Countries (N = 133).  
- **Inclusion rule:** At least **k ≥ 5** observed fields per country for BI2 computation.  
- **Missingness:** Handled per `data/metadata/IMPUTATION_NOTES.md`; imputed rows flagged as `is_imputed`.

## 5) Diagnostics

- Influence (Cook’s distance), heteroskedasticity (White test), LOESS visual checks.  
- Multicollinearity for control sets: **VIF < 5**.

## 6) Sensitivity Analyses

- **Complete-case vs imputed-inclusive** datasets.  
- **Alternative imbalance metrics:** cosine distance, earth-mover distance (EMD).  
- **Temporal windows:** **2018–2020** vs **2021–2024**; the BI2–employment correlation remains negative in both windows.

## 7) Reproducibility

- Source-data CSVs for figures/tables are in `results/source_data/`.  
- Numerical outputs (including bootstrap arrays and CIs) are saved to `results/statistics/` when running:

```bash
python -m analysis.cli run_all --countries 133 --demand-proxy employment --robustness cosine,emd --seed 2025

Note: Replace any approximate CIs above with exact values from your latest run if they differ. All values are reported in English for journal submission.
