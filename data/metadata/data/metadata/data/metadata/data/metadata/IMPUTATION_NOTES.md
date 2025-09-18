# Imputation Notes (Missing-Data Handling)

This document specifies **principles, scope, methods, diagnostics, and quality controls** for missing-data handling used in the Balance Index 2.0 pipeline.

---

## 1) Principles
- **Transparency:** Every imputed observation is flagged with `is_imputed = 1`.
- **Minimalism:** Prefer **listwise availability** and **complete-case** stats when feasible; impute only when necessary to preserve country coverage comparability.
- **No leakage:** Imputation uses **within-period** information only (no future leakage).

---

## 2) Scope & Variables
- Variables potentially imputed:
  - `stem_share`, `humanities_share` (or field-level shares used internally)
  - Outcomes: `employment_rate`, `neet_rate` (if country-year gaps exist)
  - Controls: `gdp_per_capita`, `ai_readiness`, `innovation_index` (if used)
- Time coverage: ~2018–2024 (latest available per country).

---

## 3) Methods
- **Field shares (composition):**
  - If some field shares are missing but others are observed, re-normalize observed shares to sum to 1 **only when** missing mass < 10% of categories. Otherwise, mark `is_imputed = 1` and exclude from main analysis or apply multi-variate imputation.
- **Single-value gaps (scalar):**
  - **Forward/Backward fill** (within-country) for **1-year gaps** only.
  - **Median within region–income group** for isolated missing cells (document donor pool).
- **Model-based (optional robustness):**
  - **MICE (Multiple Imputation by Chained Equations)** with predictive mean matching for continuous variables.
  - Number of imputations: `m = 20`, seed = `2025`.
- **Out-of-range handling:** Clamp shares to `[0,1]`, re-normalize distributions to sum to 1.

---

## 4) Flags & Metadata
- Column `is_imputed` (0/1) added to **final, analysis-ready** tables.
- If multiple variables imputed, add per-variable flags (e.g., `is_imputed_employment`, `is_imputed_stem`) in intermediate tables.
- Log decisions in `PROVENANCE_LOG.md` for each step/script.

---

## 5) Diagnostics
- **Missingness Maps:** report per variable × country (counts and %).
- **Before/After Distributions:** compare means/SDs/quantiles for imputed vs. non-imputed subsets.
- **Sensitivity:** re-run key correlations/regressions on **complete cases only**, and report deltas in `results/statistics/…`.
- **Influence:** check whether imputed rows drive results (Cook’s distance / robust regression).

---

## 6) Quality Controls
- Reproducible seed: `2025`.
- Country-level minimum data rule for inclusion in main figures: at least **k fields observed** (default `k ≥ 5`).
- Any country failing QC is included only in supplementary sensitivity.

---

## 7) Reporting in Manuscript
- Methods: briefly describe imputation strategy and flagging.
- Results: disclose **N** by imputation status and note if conclusions change under complete-case analysis.
- Supplementary: provide missingness heatmaps and sensitivity tables.

---

## 8) Minimal Template (to fill if used)
| variable | year | country | method | donor pool | imputations (m) | seed | note |
|---|---:|---|---|---|---:|---:|---|
| employment_rate | 2021 | MEX | region-median | LAC upper-middle | 1 | 2025 | single-year gap |
| stem_share | 2020 | DEU | MICE (PMM) | OECD | 20 | 2025 | field-level vector imputed |

