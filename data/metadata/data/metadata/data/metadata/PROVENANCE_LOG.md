# Data Provenance Log (for Journal Submission)

This log documents **who/when/how** each dataset or output was created, including scripts, inputs, commit hashes, seeds, and checksums.

---

## 1) Environment & Repository
- **Repository:** https://github.com/seungjin-data/balance-index-2.0
- **Default branch:** `main`
- **Tag / snapshot for submission:** `v2.0.0` (commit: `<ENTER_COMMIT_HASH>`)
- **Python:** 3.10+ (see `environment.yml`, `requirements.txt`)
- **OS (dev):** `<e.g., Ubuntu 22.04>`  
- **Hardware (if relevant):** `<CPU/GPU/RAM>`  
- **Random seeds:** `2025` (unless otherwise noted)

---

## 2) Raw Source Files (expected in `data/raw/`)
| Provider | File | Retrieved on | Access method | License/Terms | SHA256 |
|---|---|---:|---|---|---|
| UNESCO UIS | `unesco_wide_data.csv` | `<YYYY-MM-DD>` | portal/API | redistribution restricted | `<SHA256>` |
| OECD | `oecd_employment_data.csv` | `<YYYY-MM-DD>` | portal/API | attribution required | `<SHA256>` |
| ILO | `ilo_youth_employment.csv` | `<YYYY-MM-DD>` | portal/API | provider terms | `<SHA256>` |
| World Bank | `world_bank_indicators.csv` | `<YYYY-MM-DD>` | API | CC BY 4.0 (most series) | `<SHA256>` |
| … | … | … | … | … | … |

> Record checksums in `checksums/sha256sum.txt` (generate via `sha256sum <file>`).

---

### Step 3.1 — Field harmonization
- **Script:** `analysis/02_harmonize_fields.py`  
- **Inputs:** `data/raw/unesco_wide_data.csv`, `data/metadata/field_mappings.json`  
- **Outputs:** `data/interim/uis_harmonized.parquet`  
- **Commit:** `<HASH>` (author: Seung Jin Kim, date: `<YYYY-MM-DD>`)  
- **Notes:** Applied ISCED-F mapping; normalized field shares to sum to 1.

### Step 3.2 — Demand vector construction
- **Script:** `analysis/03_build_demand.py`  
- **Inputs:** `data/raw/oecd_employment_data.csv`, `.../bls_job_postings.csv`  
- **Outputs:** `data/interim/demand_vectors.parquet`  
- **Commit:** `<HASH>`  
- **Notes:** Built employment-based demand; alternative proxies (AI skills, earnings) flagged.

### Step 3.3 — BI2 computation
- **Script:** `analysis/04_compute_bi2.py`  
- **Inputs:** `data/interim/uis_harmonized.parquet`, `data/interim/demand_vectors.parquet`  
- **Outputs:** `data/processed/bi2_country_level.parquet`, `results/tables/table_1_country_rankings.csv`  
- **Commit:** `<HASH>`  
- **Parameters:** metric=`symmetric_KL`; seed=`2025`  
- **Notes:** Also computed cosine/EMD as robustness (see `results/statistics/`).

### Step 3.4 — Statistics & figures
- **Script:** `analysis/05_statistics.py`, `analysis/06_visualize.py`  
- **Inputs:** `data/processed/bi2_country_level.parquet`, outcomes (OECD/ILO/WB)  
- **Outputs:** `results/statistics/correlation_results.json`, figures under `results/figures/`  
- **Commit:** `<HASH>`  
- **Notes:** Bootstrapped Pearson; region/income stratified analyses.

---

## 4) Imputation & Flags
- **Imputation log:** `IMPUTATION_NOTES.md` (method, scope, diagnostics)  
- **Column used:** `is_imputed` (0/1). Any derived variable affected is documented there.

---

## 5) Source Data for Figures/Tables
- Stored under `results/source_data/` with **1:1 file-to-figure mapping**:
  - `F1_world_map_source.csv`
  - `F2_correlation_source.csv`
  - `T1_country_rankings_source.csv`
  - …

> Each file contains exactly the columns required to regenerate the corresponding figure/table.

---

## 6) Reproducibility Command
```bash
# create/activate env (see README)
python -m analysis.cli run_all \
  --countries 133 \
  --demand-proxy employment \
  --robustness cosine,emd \
  --seed 2025
7) Change History (high level)
v2.0.0 (<YYYY-MM-DD>): 133 countries; BI2 (symmetric KL); bootstrap validation; full figures/tables exported.

v1.5.0: Added statistical validation; improved mapping tables.

v1.0.0: Initial BI2 framework and pipeline skeleton.
