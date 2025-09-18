# Data Availability

The analysis relies on a combination of publicly accessible datasets and third-party sources with redistribution restrictions.

- **Publicly accessible (or open under provider terms):**
  - World Bank indicators (most series under CC BY 4.0).
  - WIPO innovation indicators (license varies by edition).
  - Regional/income group classifications (UN/World Bank).

- **Restricted / redistribution-limited:**
  - UNESCO UIS / WIDE (tertiary graduates by ISCED-F, equity tables).
  - OECD employment statistics and PIAAC adult skills.
  - ILO labour market indicators.
  - Oxford Insights AI Readiness, IMF AI preparedness indices.
  - Postings-based labour-demand signals (BLS-like or commercial aggregators).

**Access instructions.** Users must obtain original restricted datasets directly from the providers and comply with their licenses/terms. This repository therefore includes **scripts, processing logic, and source-data CSVs for figures/tables**, but does **not** redistribute licensed raw files.

- A practical checklist of sources, years, licenses, and checksums is maintained in  
  `data/metadata/README_data.md` and `checksums/sha256sum.txt`.

**Reproducible subset.** To enable immediate reproduction of the main statistics and figures without violating third-party terms, the repository provides **journal “Source Data” CSVs** under `results/source_data/`, each mapped 1:1 to a figure or table in the manuscript. These CSVs contain the exact numbers plotted or reported.

**Generated artifacts.** Derived outputs (e.g., Balance Index 2.0 per country, correlation summaries) are produced by the code in this repository. See `results/statistics/STATISTICAL_REPORTING.md` for effect sizes, CIs, and sample sizes, and `data/metadata/PROVENANCE_LOG.md` for data lineage.

**Contact.** For clarifications about data access or scripts, contact the corresponding author: **Seung Jin Kim (@seungjin-data)**.
