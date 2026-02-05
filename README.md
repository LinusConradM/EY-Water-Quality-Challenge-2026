# 🌊 EY Water Quality Challenge 2026

**Forecasting Water Quality Using AI, Satellite Imagery & Environmental Data**

[![Challenge](https://img.shields.io/badge/EY_Challenge-2026-0066cc?style=for-the-badge)](https://challenge.ey.com/)
[![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)

---

## 👨‍💻 About Me

**Conrad Linus Muhirwe**  
MS Analytics Student | American University (May 2026)

Bridging 10+ years of banking expertise in audit and compliance with cutting-edge AI/ML capabilities. This challenge combines my domain knowledge in financial risk assessment with emerging skills in predictive modeling and environmental data science.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/LinusConradM)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat&logo=gmail&logoColor=white)](mailto:linusconradm@gmail.com)

---

## 🎯 Challenge Overview

### The Problem
In 2022, only 73% of the global population had access to safely managed drinking water. Climate change is increasing water stress and pollution through rising temperatures and extreme weather events. The UN warns that inadequate water quality monitoring could put 4.8 billion people at risk by 2030.

### The Goal
Build AI models to forecast water quality across rivers, lakes, and streams using:
- 🛰️ **Landsat Satellite Imagery** - Spectral data capturing water properties
- 🌡️ **TerraClimate Data** - Weather and environmental variables
- 📊 **Historical Water Quality Measurements** - Ground truth data

### Impact
- Predict water safety for human health
- Reveal effects of climate and environmental shifts
- Inform data-driven policies for communities worldwide

**Competition Period:** January 20 - March 13, 2026  
**Prize Pool:** $10,000 USD  
**Participants:** 45,000+ from 146 countries

---

## 🔬 My Approach

### Phase 1: Data Exploration ✅ (In Progress)
- [ ] Analyze water quality training dataset structure
- [ ] Explore Landsat satellite features (spectral bands, vegetation indices)
- [ ] Examine TerraClimate environmental variables (temperature, precipitation, soil moisture)
- [ ] Identify missing data patterns and outliers
- [ ] Understand temporal and spatial distributions

### Phase 2: Feature Engineering (Upcoming)
- [ ] Extract spectral indices (NDVI, NDWI, turbidity proxies)
- [ ] Create temporal features (seasonality, trends, lag variables)
- [ ] Engineer spatial features (location clusters, proximity measures)
- [ ] Aggregate climate data (rolling averages, anomalies)
- [ ] Domain-specific features informed by banking risk assessment methodologies

### Phase 3: Model Development (Upcoming)
- [ ] **Baseline:** Implement benchmark model
- [ ] **Linear Models:** Ridge, Lasso regression with feature selection
- [ ] **Tree-Based:** Random Forest, XGBoost, LightGBM
- [ ] **Deep Learning:** Neural networks for complex patterns (if compute allows)
- [ ] **Ensemble:** Stacking/blending top performers

### Phase 4: Optimization & Validation (Upcoming)
- [ ] Hyperparameter tuning (Grid Search, Bayesian Optimization)
- [ ] Cross-validation strategy (time-series aware splits)
- [ ] Feature selection and dimensionality reduction
- [ ] Model interpretability (SHAP values, feature importance)
- [ ] Final ensemble and submission

---

## 📁 Repository Structure
```
EY-Water-Quality-Challenge-2026/
│
├── 📓 Notebooks
│   ├── getting_started_notebook.ipynb
│   ├── BENCHMARK_MODEL_NOTEBOOK_SNOWFLAKE.ipynb
│   ├── landsat_demo_notebook_snowflake.ipynb
│   ├── TERRACLIMATE_DEMONSTRATION_NOTEBOOK_SNOWFLAKE.ipynb
│   └── [MY_SOLUTION.ipynb] (coming soon)
│
├── 📊 Data
│   ├── water_quality_training_dataset.csv
│   ├── landsat_features_training.csv
│   ├── landsat_features_validation.csv
│   ├── terraclimate_features_training.csv
│   └── terraclimate_features_validation.csv
│
├── 🛠️ Scripts
│   └── scripts/
│
└── 📄 Documentation
    ├── README.md
    ├── requirements.txt
    └── submission_template.csv
```

---

## 🛠️ Tech Stack

### Core Technologies
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)

### Data Science & ML
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=for-the-badge)

### Visualization
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

### Data Sources
- **Landsat 8/9 Satellite Imagery** - Multi-spectral remote sensing data
- **TerraClimate** - University of Idaho climate and hydrology dataset
- **Ground Measurements** - Historical water quality indices

---

## 📊 Results & Performance

*Will be updated as models are developed and evaluated*

### Model Performance

| Model | MAE ↓ | RMSE ↓ | R² ↑ | Notes |
|-------|-------|--------|------|-------|
| Baseline | TBD | TBD | TBD | Simple linear model |
| Random Forest | TBD | TBD | TBD | Tree-based ensemble |
| XGBoost | TBD | TBD | TBD | Gradient boosting |
| Final Ensemble | TBD | TBD | TBD | Best performers combined |

### Leaderboard Position
- **Current Rank:** TBD
- **Score:** TBD

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Snowflake account (120-day trial via EY Challenge)
- Jupyter Notebook
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/LinusConradM/EY-Water-Quality-Challenge-2026.git
cd EY-Water-Quality-Challenge-2026

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

### Quick Start
1. Open `getting_started_notebook.ipynb` for data exploration
2. Run `BENCHMARK_MODEL_NOTEBOOK_SNOWFLAKE.ipynb` for baseline model
3. Explore `landsat_demo_notebook_snowflake.ipynb` and `TERRACLIMATE_DEMONSTRATION_NOTEBOOK_SNOWFLAKE.ipynb`

---

## 💡 Key Insights & Learnings

*Will document findings as the project progresses*

---

## 🔄 Project Timeline

- **Week 1 (Jan 20-26):** ✅ Environment setup, data exploration
- **Week 2 (Jan 27-Feb 2):** 🔄 Feature engineering, baseline model
- **Week 3-6 (Feb 3-Mar 2):** Model development and optimization
- **Week 7 (Mar 3-9):** Final ensemble and validation
- **Week 8 (Mar 10-13):** Final submission and documentation

---

## 📚 Resources

### Challenge Resources
- [EY Challenge Portal](https://challenge.ey.com/)
- [Snowflake Developer Guide](https://www.snowflake.com/en/developers/guides/ey-ai-and-data-challenge/)
- [Original Repository](https://github.com/Snowflake-Labs/EY-AI-and-Data-Challenge)

### Technical Documentation
- [Landsat Data User Handbook](https://www.usgs.gov/landsat-missions/landsat-data-users-handbook)
- [TerraClimate Documentation](https://www.climatologylab.org/terraclimate.html)
- [Snowflake ML Documentation](https://docs.snowflake.com/en/developer-guide/snowpark-ml/index)

---

## 🤝 Connect & Collaborate

Interested in data science, AI/ML, environmental analytics, or financial technology? Let's connect!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LinusConradM)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:linusconradm@gmail.com)

**Open to:**
- Data Analyst positions
- Data Scientist roles  
- AI Engineer opportunities
- Collaborations on ML/AI projects

---

## 📝 License & Acknowledgments

### License
- Challenge materials: Copyright © 2026 EY
- Snowflake scripts: Copyright © 2026 Snowflake Inc. (Apache 2.0 License)
- Original repository: [Snowflake-Labs/EY-AI-and-Data-Challenge](https://github.com/Snowflake-Labs/EY-AI-and-Data-Challenge)

### Acknowledgments
- **EY AI & Data Challenge Program** for organizing this competition
- **Snowflake** for providing the ML platform and infrastructure
- **American University Kogod School of Business** for academic support
- **Harmonia Holdings Group** for foundational AI/ML experience

---

## 🌟 Why This Project Matters

This challenge addresses one of the most pressing global issues: access to safe drinking water. By leveraging AI and satellite technology, we can:

- 🔍 **Monitor** water quality at scale across remote locations
- ⚠️ **Predict** potential contamination events before they impact communities
- 📈 **Track** the effects of climate change on water resources
- 🎯 **Guide** policy decisions with data-driven insights
- 🌍 **Support** UN Sustainable Development Goal 6: Clean Water and Sanitation

---

<div align="center">

**🌊 Clean Water for All 🌍**

*Building a better working world through AI and data innovation*

[![EY Challenge](https://img.shields.io/badge/EY_AI_&_Data_Challenge-2026-0066cc?style=flat-square)](https://challenge.ey.com/)
[![UN SDG 6](https://img.shields.io/badge/UN_SDG-6:_Clean_Water-4C9F38?style=flat-square)](https://sdgs.un.org/goals/goal6)

**Challenge Period:** January 20 - March 13, 2026

</div>