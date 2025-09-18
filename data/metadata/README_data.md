# Data README (for Journal Submission)

This document describes all datasets used in the study, including **source, temporal coverage, license, access method, preprocessing, and checksums**.  
Datasets with redistribution restrictions **must be downloaded directly by users** from the original providers under their licenses.

---

## 0) Files currently included in this repository
- `balance_index_complete.csv`  
  - **Description:** Snapshot table with Balance Index (e.g., BI2) and selected outcomes for reproducibility.  
  - **Columns (example):** `country`, `iso3`, `year`, `bi2`, `employment_rate`, `region`, `is_imputed` …  
  - **Provenance:** Produced by code in this repository (see “Reproducibility Steps”).  
  - **License note:** Code is MIT; derived datasets remain subject to original providers’ licenses.

- `balance_index_calculation.py` (and any modules under `analysis/` if present)  
  - **Description:** Algorithms/scripts to compute BI2 and statistical outputs.

---

## 1) UNESCO UIS / WIDE (source data — redistribution restricted)
- **Content:** Tertiary graduates by ISCED-F fields; WIDE equity tables (gender, location, wealth, etc.).  
- **Coverage:** ~2018–2024 (latest available by country).  
- **Access:** https://uis.unesco.org and https://wide.unesco.org (download CSV/XLSX to `data/raw/`).  
- **License / Terms:** Provider terms apply; redistribution may be restricted.  
- **Preprocessing:** ISCED-F harmonization; ISO3 country codes; handling of missing values (imputation flagged).  
- **Checksums:** Record SHA256 for each raw file in `checksums/sha256sum.txt`.

## 2) OECD Employment / PIAAC (source data — partially restricted)
- **Content:** Employment/unemployment rates by age bands; PIAAC adult skills.  
- **Coverage:** Latest available by country (varies).  
- **Access:** https://data.oecd.org / PIAAC portals (save to `data/raw/`).  
- **License:** OECD terms; attribution required for reuse.  
- **Preprocessing:** Age/sex harmonization; ISO3 alignment; time-consistency checks.  
- **Checksums:** Record SHA256 in `checksums/sha256sum.txt`.

## 3) ILO / World Bank / Oxford Insights / IMF / WIPO / BLS-like postings
- **Content:** Labour statistics (ILO), macro/development indicators (World Bank), AI readiness (Oxford Insights), AI preparedness (IMF), innovation (WIPO), postings-based demand signals (BLS-like).  
- **Coverage:** ~2018–2024.  
- **Access:** Download via each provider’s portal/API to `data/raw/`.  
- **License:** Varies by provider; check terms before use or redistribution.  
- **Preprocessing:** Series alignment, unit normalization, optional log/standardization, ISO3 harmonization.  
- **Checksums:** Record SHA256 in `checksums/sha256sum.txt`.

---

## Reproducibility Steps (overview)
1. Download original source files to `data/raw/` following the instructions above.  
2. Run the pipeline:
   ```bash
   # After creating/activating your environment
   python balance_index_calculation.py
   # or, if using the modular CLI:
   # python -m analysis.cli run_all

Outputs are written to:

results/tables/…

results/statistics/correlation_results.json

results/figures/…

Source Data for Figures and Tables are provided as CSVs under results/source_data/ with a 1:1 mapping to each figure/table name in the manuscript.

Versioning (data snapshots)

v2.0.0 (YYYY-MM-DD): 133 countries; BI2 (symmetric KL) baseline; employment correlation results.

v1.5.0: Statistical validation and bootstrap CIs.

v1.0.0: Initial BI2 framework.

Contact: Seung Jin Kim (@seungjin-data)
