
# Code Availability

All code to reproduce results is in this repository (default branch: main). Use environment.yml or requirements.txt.

## Reproduction
```bash
python -m analysis.cli run_all --countries 133 --demand-proxy employment --robustness cosine,emd --seed 2025
```
Outputs: results/statistics/, results/figures/, results/tables/, and results/source_data/.
