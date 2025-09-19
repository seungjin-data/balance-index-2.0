# Code Availability

All code to reproduce results is in this repository (default branch: main). Use `environment.yml` or `requirements.txt`.

**Submission snapshot:** commit `f5a2c09` on branch `main` (tag `v2.0.0` will reference this snapshot).

## Reproduction
```bash
python -m analysis.cli run_all --countries 133 --demand-proxy employment --robustness cosine,emd --seed 2025
