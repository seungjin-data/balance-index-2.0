# Balance Index 2.0 — Global Educational Balance Analysis (Data + Code)

[![DOI (all versions)](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17156762-blue.svg)](https://doi.org/10.5281/zenodo.17156762)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)
![CSV](https://img.shields.io/badge/data-CSV-orange.svg)
![Reproducible](https://img.shields.io/badge/reproducible--research-yes-success.svg)

Dataset + analysis for **Balance Index 2.0** — a global study of educational balance between STEM/Humanities and its relation to employment outcomes in the AI era.  
This repository contains: **CSV dataset (snapshot), README with quick-use instructions, and a data dictionary**.  
The archived dataset is available on **Zenodo**:

- **Dataset snapshot (v2.0.1)**: https://doi.org/10.5281/zenodo.17156763  
- **All versions (latest DOI)**: https://doi.org/10.5281/zenodo.17156762

---

## Table of Contents
- [Research Overview](#research-overview)
- [Research Statistics](#research-statistics)
- [Key Findings](#key-findings)
- [Data Availability](#data-availability)
- [How to Cite](#how-to-cite)
- [Citation](#citation)
- [BibTeX](#bibtex)
- [License](#license)

---

## Research Overview

**22-day comprehensive analysis** across **133 countries**, examining the relationship between **STEM/Humanities education distribution** and **employment outcomes** in the AI era.

**Key Finding**  
Balance Index vs Employment Rate correlation: **r = -0.72*** (p < 0.001)**  
> Interpretation: Countries with stronger *imbalances* in education disciplines tend to show less favorable employment dynamics. Balanced human capital appears linked to healthier labor outcomes.

---

## Research Statistics

- **Countries Analyzed**: 133  
- **Adult Graduates**: 635,316  
- **UNESCO WIDE Observations**: 487,345  
- **International Organizations**: 8  
- **Analysis Period**: 22 days (Aug 28 – Sep 19, 2025)  
- **Statistical Significance**: p < 0.001

---

## Key Findings

### ✅ *Optimal Balance Countries* (Balance Index < 0.05)

| # | Country      | Balance Index | Employment Rate | Region         | Notes                         |
|---|--------------|--------------:|----------------:|----------------|-------------------------------|
| 1 | **Egypt**    | 0.017         | 84.1%           | Africa         | Optimal balance               |
| 2 | **Mexico**   | 0.020         | 69.2%           | North America  | Optimal balance               |
| 3 | **Italy**    | 0.021         | 83.2%           | Europe         | Optimal balance               |
| 21| **Germany**  | 0.449         | 88.4%           | Europe         | *Severe imbalance* (example)  |
|133| **Burkina Faso** | 5.219     | 71.4%           | Africa         | *Check imputation status*     |

> *Note.* The above table illustrates sample entries from the full dataset (`results/source_data/T1_country_rankings_source.csv`).

---

## Data Availability

The dataset analyzed in this study — **Balance Index 2.0 — Data Snapshot (v2.0.1)** — is openly available on Zenodo:  
**https://doi.org/10.5281/zenodo.17156763**

All versions (latest DOI that always resolves to the newest release):  
**https://doi.org/10.5281/zenodo.17156762**

---

## How to Cite

If you use this work, please cite:

**Dataset (snapshot v2.0.1)**  
Kim, SeungJin (2025). *Balance Index 2.0 — Data Snapshot (v2.0.1)*. Zenodo.  
https://doi.org/10.5281/zenodo.17156763

**All versions (latest DOI)**  
Kim, SeungJin (2025). *Balance Index 2.0 — Data Snapshot*. Zenodo.  
https://doi.org/10.5281/zenodo.17156762

---

## Citation

```text
@article{balance_index_2025,
  title   = {Balance Index 2.0: Educational Balance Predicts Employment Success},
  journal = {Nature Human Social and Cultural Dynamics},
  year    = {2025}
}

BibTeX
@dataset{kim_2025_balance_index_2_0_snapshot_v2_0_1,
  author    = {Kim, SeungJin},
  title     = {Balance Index 2.0 — Data Snapshot (v2.0.1)},
  year      = {2025},
  publisher = {Zenodo},
  version   = {v2.0.1},
  doi       = {10.5281/zenodo.17156763},
  url       = {https://doi.org/10.5281/zenodo.17156763}
}

License

This project is licensed under the MIT License. See LICENSE
 for details.
