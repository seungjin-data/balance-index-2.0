# Code Availability

All code required to reproduce the Balance Index 2.0 results is available in this repository.

- **Repository:** https://github.com/seungjin-data/balance-index-2.0  
- **Default branch:** `main`  
- **Submission snapshot (tag):** `v2.0.0` (commit: `<ENTER_COMMIT_HASH>`)

## Environment & Dependencies
- **Python:** 3.10+ (see `environment.yml` and `requirements.txt`)
- Optional: R 4.0+ for ancillary checks (not required for the main pipeline)
- Reproducibility seed: `2025`

To create the environment:
```bash
# Option A: venv + pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Option B: conda
conda env create -f environment.yml
conda activate balance-index-2.0

How to Reproduce the Main Results

Run the end-to-end pipeline and regenerate figures/tables:

# Modular CLI (recommended)
python -m analysis.cli run_all --countries 133 --demand-proxy employment --robustness cosine,emd --seed 2025

# Rebuild figures only
python -m analysis.cli build_figures

Primary outputs:

results/statistics/correlation_results.json (effect sizes, CIs, N)

results/figures/ (journal-ready plots)

results/tables/ (tabular outputs)

results/source_data/ (1:1 “Source Data” CSVs for all figures/tables)

Data Access Note

The repository does not redistribute licensed raw data. Users should follow journal/DATA_AVAILABILITY.md and data/metadata/README_data.md to obtain the original sources. Scripts and mappings are provided to process downloaded files into analysis-ready format.

Issues & Support

Bug reports and feature requests: open a GitHub Issue on the repository.
For reproducibility questions, reference the commit hash, OS, Python version, and the exact command used.

