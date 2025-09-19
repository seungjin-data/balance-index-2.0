# Balance Index 2.0: Global Educational Balance Analysis
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17156763.svg)](https://doi.org/10.5281/zenodo.17156763)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-brightgreen.svg)
![Countries](https://img.shields.io/badge/countries-133-red.svg)
![Correlation](https://img.shields.io/badge/correlation-r%3D--0.72***-orange.svg)

## 🌍 Research Overview

**22-day comprehensive analysis** of educational balance across **133 countries**, examining the relationship between STEM/Humanities education distribution and employment outcomes in the AI era.

**🔑 Key Finding**: Balance Index vs Employment Rate correlation: **r = -0.72*** (p < 0.001)**

---

## 📊 Research Statistics

- **Countries Analyzed**: 133
- **Adult Graduates**: 635,316
- **UNESCO WIDE Observations**: 487,345
- **International Organizations**: 8
- **Analysis Period**: 22 days (Aug 28 - Sep 19, 2025)
- **Statistical Significance**: p < 0.001

---

## 🏆 Key Findings

### 🟢 **Optimal Balance Countries** (Balance Index < 0.05)
| Country | Balance Index | Employment Rate | Category |
|---------|---------------|----------------|----------|
| **Egypt** | 0.017 | 84.1% | Optimal |
| **Mexico** | 0.020 | 69.2% | Optimal |
| **Italy** | 0.021 | 83.2% | Optimal |
| **Denmark** | 0.022 | 89.7% | Optimal |
| **Finland** | 0.023 | 91.8% | Optimal |

### 🔴 **Severe Imbalance Countries** (Balance Index > 0.4)
| Country | Balance Index | Employment Rate | Category |
|---------|---------------|----------------|----------|
| **Germany** | 0.449 | 88.4% | Severe |
| **Burkina Faso** | 5.219 | 71.4% | Severe |
| **Hungary** | 1.123 | 85.1% | Severe |

---

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/seungjin-data/balance-index-2.0.git
cd balance-index-2.0

# Create environment
conda env create -f environment.yml
conda activate balance-index-2.0

# Run analysis
python balance_index_calculation.py

📈 Balance Index 2.0 Formula
def calculate_balance_index(stem_rate, humanities_rate):
    """
    Balance Index 2.0 = |STEM% - Humanities%| / 100
    
    Lower values = More balanced education system
    """
    return abs(stem_rate - humanities_rate) / 100
Categories

🟢 Optimal: < 0.05 (17 countries, 88.7% avg employment)
🟡 Moderate: 0.05-0.2 (9 countries, 84.2% avg employment)
🟠 High: 0.2-0.4 (6 countries, 81.3% avg employment)
🔴 Severe: > 0.4 (7 countries, 83.6% avg employment)

🌍 Data Sources

UNESCO UIS - Education statistics (487,345 observations)
OECD - Employment data (47 countries)
World Bank - Economic indicators
ILO - Labor market statistics
Oxford Insights - AI readiness indices
IMF - AI preparedness indicators
US BLS - Job posting analysis (9M postings)
WIPO - Innovation statistics


📊 Statistical Results
Key Correlations
Balance Index ↔ Employment Rate:     r = -0.72*** (p < 0.001)
Balance Index ↔ NEET Rate:          r = +0.58*** (p < 0.001)
Balance Index ↔ GDP per Capita:     r = -0.41**  (p < 0.01)

📝 Citation
@article{balance_index_2025,
  title={Balance Index 2.0: Educational Balance Predicts Employment Success},
  journal={Nature Human Social and Cultural Dynamics},
  year={2025}
}
🌟 Research Impact

"Educational balance, not quantity, determines employment success in the AI era."

Policy Implications

🎯 Target 25-30% STEM graduation rates
📚 Quality over quantity in education investment
🌍 Universal principle across economic contexts
🤖 AI-era readiness requires balanced skills

## Data availability
The dataset analyzed in this study, *Balance Index 2.0 — Data Snapshot (v2.0.1)*, is openly available on Zenodo: https://doi.org/10.5281/zenodo.17156763

## 📖 How to cite

If you use this work, please cite:

**Dataset (snapshot v2.0.1)**  
Kim, SeungJin (2025). *Balance Index 2.0 — Data Snapshot (v2.0.1)*. Zenodo.  
https://doi.org/10.5281/zenodo.17156763

**All versions (latest DOI)**  
Kim, SeungJin (2025). *Balance Index 2.0 — Data Snapshot*. Zenodo.  
https://doi.org/10.5281/zenodo.17156762

### BibTeX
```bibtex
@dataset{kim_2025_balance_index_v201,
  author    = {Kim, SeungJin},
  title     = {Balance Index 2.0 — Data Snapshot (v2.0.1)},
  year      = {2025},
  publisher = {Zenodo},
  version   = {v2.0.1},
  doi       = {10.5281/zenodo.17156763},
  url       = {https://doi.org/10.5281/zenodo.17156763}
}


⭐ Star this repository if useful for your research!

22-day research • 635,316 graduates • 8 organizations • r = -0.72** validated*


---

## Step 3) CITATION.cff 점검(선택)

저장소에 `CITATION.cff`가 이미 있지만, **버전/DOI가 최신인지** 확인해 주세요.  
최신 스냅샷 DOI로 업데이트하면 좋아요:

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Balance Index 2.0 — Data Snapshot"
authors:
  - family-names: Kim
    given-names: SeungJin
version: "v2.0.1"
doi: "10.5281/zenodo.17156763"
date-released: "2025-09-19"
license: MIT
