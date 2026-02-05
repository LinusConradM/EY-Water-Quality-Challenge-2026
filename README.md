<div align="center">

# 🌊 Forecasting Water Quality in South Africa
## *Using AI and Satellite Data to Ensure Safe Water for All*

[![EY Challenge 2026](https://img.shields.io/badge/EY_Challenge-2026-FFE600?style=for-the-badge&logo=ey&logoColor=black)](https://challenge.ey.com/)
[![Status](https://img.shields.io/badge/Status-In_Progress-orange?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

**Competition Period:** January 20 - March 13, 2026 | **Prize Pool:** $10,000 USD

[View Challenge](https://challenge.ey.com/) • [Explore Code](#) • [Contact Me](mailto:linusconradm@gmail.com)

---

</div>

## 🚨 The Problem

> *"In 2022, 2.2 billion people lacked access to safely managed drinking water. By 2030, inadequate monitoring could put 4.8 billion people at risk."* — United Nations

Water quality is not just an environmental metric—**it's a matter of survival.** Climate change, urbanization, and pollution are accelerating water contamination worldwide. Yet monitoring remains inadequate, especially in vulnerable regions.

**In South Africa:**
- Only **59% of water samples** meet "good" quality standards
- Urban areas like **Cape Town, Pretoria, and Johannesburg** show the poorest water quality
- Traditional monitoring is **expensive, infrequent, and limited in coverage**

**The solution?** Leverage AI and satellite technology to predict water quality at scale, enabling proactive intervention before contamination impacts communities.

---

## 👨‍💻 About This Project

This repository documents my solution for the **2026 EY AI & Data Challenge**, one of the world's largest data competitions focused on sustainability. The challenge: **build machine learning models to forecast water quality across South Africa's river systems** using satellite imagery and climate data.

### 🎯 Project Goal

Predict three critical water quality parameters:

1. **Total Alkalinity** - Buffering capacity against pH changes
2. **Electrical Conductance** - Indicator of dissolved salts/minerals  
3. **Dissolved Reactive Phosphorus** - Nutrient that causes harmful algal blooms

**Target:** Achieve significantly better than baseline performance (R² > 0.20) on 600 validation samples across 19 rivers.

---

## 💼 My Unique Angle

**Conrad Linus Muhirwe**  
*MS Analytics Student, American University (May 2026)*

I bring a unique combination of **10+ years of banking experience** in audit, compliance, and risk assessment, now paired with emerging **AI/ML capabilities**. This project bridges two worlds:

**From Banking:** 

- Risk modeling and spatial pattern analysis
- Regulatory compliance mindset
- Financial impact assessment

**To Environmental AI:**

- Predictive modeling for water quality
- Geospatial feature engineering
- Policy-driven decision support

My banking background in **risk assessment** translates directly to identifying high-risk water contamination zones—similar to credit risk geographic clustering but with life-or-death stakes.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/conrad-linus-m/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/LinusConradM)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:linusconradm@gmail.com)

**🎓 Currently seeking:** Data Analyst | Data Scientist | AI Engineer roles

---

## 🎯 Challenge Overview

### The Mission

Develop machine learning models to:

- ✅ **Predict** water quality parameters at unmeasured locations
- ✅ **Identify** key environmental and climate drivers of water quality
- ✅ **Enable** proactive water management decisions
- ✅ **Scale** solutions to benefit vulnerable communities worldwide

### Why It Matters

- 🌍 **Global Impact:** Addresses UN Sustainable Development Goal 6 (Clean Water & Sanitation)
- 🔬 **Scientific Innovation:** Combines satellite remote sensing with AI for environmental monitoring
- 🏆 **Competition Scale:** 45,000+ participants from 146 countries
- 💰 **Real Stakes:** $10,000 prize pool + career opportunities with EY

### Key Statistics

| Metric | Value |
|--------|-------|
| **People without safe water (2022)** | 2.2 billion |
| **People at risk by 2030** | 4.8 billion |
| **South Africa samples meeting quality standards** | 59% |
| **Water bodies globally with "good" quality** | 56% |

---

## 📊 Challenge Specifications

### Dataset Overview

**Training Data:** South Africa Rivers (2011-2015)

- 📍 **27,957 samples** across **162 locations** and **86 rivers**
- 📅 **9,319 unique measurements** (location + date combinations)
- 🎯 **3 water quality parameters** per sample

**Validation Data:** Different South Africa Regions

- 📍 **600 samples** across **24 locations** and **19 rivers**  
- 📅 **200 unique measurements** to predict
- 🏆 **Goal:** Predict all 3 parameters with high accuracy

### Target Variables

| Parameter | Unit | "Good" Threshold | Training Data Quality | Key Drivers |
|-----------|------|------------------|----------------------|-------------|
| **Total Alkalinity** | mg/L | 20-200 | 78% good | Geology, mining, urban runoff |
| **Electrical Conductance (EC)** | uS/cm | <800 | 84% good | Salinity, agriculture, wastewater |
| **Dissolved Reactive Phosphorus (DRP)** | ug/L | <100 | 84% good | Agricultural runoff, sewage |

### Feature Data Sources

**🛰️ Landsat 8/9 Satellite Imagery**

- 30-meter spatial resolution
- Spectral bands + vegetation indices (NDVI, NDWI)
- Cloud-filtered scenes
- Proxy for urbanization and agricultural impact

**🌡️ TerraClimate Environmental Data**

- 4-kilometer spatial resolution
- 14 climate variables (temperature, precipitation, soil moisture, etc.)
- Monthly data from 1958-present
- Hydrological balance indicators

**➕ Additional Open-Source Data Allowed**

### Evaluation Criteria

**Primary Metric:** Mean R² score across all three water quality parameters
```
Final Score = (R²_Alkalinity + R²_EC + R²_DRP) / 3
```

**Competition Structure:**

1. 🏃 **All Participants:** Compete on leaderboard (unlimited submissions)
2. 🥈 **Top 10:** Semi-finalists (model review: compliance + innovation + efficiency)
3. 🥇 **Top 5:** Finalists (business plan + video presentation required)

**Baseline to Beat:** R² = 0.20 (provided benchmark model)

---

## 📦 Data & Resources

### Development Environment

**Selected Platform:** 💻 **General Platform** (Local Python Environment)

**My Setup:**

- Local development on MacBook Pro
- Python 3.8+ with Jupyter Notebook
- Version control with Git/GitHub
- Full control over code and experiments

---

### 📊 Official Datasets

#### 🎯 Target Dataset

**Training Data:** `water_quality_training_dataset.csv`

- **Parameters:** Total Alkalinity, Electrical Conductance (EC), Dissolved Reactive Phosphorus (DRP)
- **Coverage:** Multiple river locations in South Africa (2011-2015)
- **Size:** 27,957 samples across 162 locations and 86 rivers
- **Purpose:** Train and validate models

**Submission Template:** `submission_template.csv`

- **Points to Predict:** 200 unique (location + date) combinations
- **Required:** Predictions for all 3 water quality parameters
- **Format:** CSV file for leaderboard submission

---

#### 🛰️ Feature Datasets (Examples Provided)

Participants may use **any publicly available datasets**. The challenge provides:

**1. Landsat Level-2 Satellite Data**

- **Source:** NASA/USGS via Microsoft Planetary Computer
- **Resolution:** 30 meters
- **Revisit:** Every 8-16 days
- **Features:** Spectral bands, vegetation indices (NDVI, NDWI), cloud filtering
- **Use Case:** Land use, urbanization, vegetation density

**2. TerraClimate Environmental Data**

- **Source:** University of Idaho via Microsoft Planetary Computer
- **Resolution:** 4 kilometers
- **Temporal Coverage:** 1958-present, monthly
- **Variables:** 14 climate parameters (temperature, precipitation, soil moisture, etc.)
- **Use Case:** Climate drivers, hydrological balance

**Additional Data Sources Allowed:**

- ✅ Must be publicly available and free
- ✅ Must be documented and referenced in model
- ✅ Suitable for geospatial feature extraction

---

### 📓 Notebook Resources

#### Official Challenge Notebooks

| Notebook | Purpose | Status |
|----------|---------|--------|
| `Benchmark_Model_Notebook.ipynb` | Baseline model (R²=0.20) | ⏳ To Run |
| `Landsat_Data_Extraction_Notebook.ipynb` | Extract Landsat features | 📋 Reference |
| `TerraClimate_Data_Extraction_Notebook.ipynb` | Extract TerraClimate features | 📋 Reference |
| `Landsat_Demonstration_Notebook.ipynb` | Cloud filtering examples | 📚 Tutorial |
| `TerraClimate_Demonstration_Notebook.ipynb` | Climate data access demo | 📚 Tutorial |

---

### 📚 Supplementary Materials

#### Official Guidance
- 📄 **Participant Guidance PDF** - Detailed overview of water quality parameters and modeling suggestions
- 🎥 **How to Get Started Video** - Platform setup walkthrough
- 🎥 **Tips for Success Video** - Best practices from organizers

#### Working Files
- 📊 `water_quality_training_dataset.csv` - Training labels
- 🛰️ `landsat_features_training.csv` - Pre-extracted Landsat features (training)
- 🛰️ `landsat_features_validation.csv` - Pre-extracted Landsat features (validation)
- 🌡️ `terraclimate_features_training.csv` - Pre-extracted TerraClimate features (training)
- 🌡️ `terraclimate_features_validation.csv` - Pre-extracted TerraClimate features (validation)
- 📝 `submission_template.csv` - Prediction format template

---

### 🗂️ Data Directory Structure
```
data/
├── raw/                                    # Original datasets
│   ├── water_quality_training_dataset.csv
│   └── submission_template.csv
│
├── features/                               # Pre-extracted features
│   ├── landsat_features_training.csv
│   ├── landsat_features_validation.csv
│   ├── terraclimate_features_training.csv
│   └── terraclimate_features_validation.csv
│
├── processed/                              # My engineered features
│   ├── spatial_features.csv
│   ├── temporal_features.csv
│   └── combined_features.csv
│
└── submissions/                            # Leaderboard submissions
    ├── submission_baseline.csv             # Baseline (R²=0.20)
    ├── submission_v1.csv
    └── submission_v2.csv
```

---

### ⚠️ Important Data Rules

**What You CAN Use:**

- ✅ Any publicly available, free dataset
- ✅ Additional satellite data (Sentinel-2, MODIS, etc.)
- ✅ Topographic data (elevation, slope)
- ✅ Land use/cover datasets
- ✅ Climate reanalysis products

**What You CANNOT Use:**

- ❌ Proprietary/paid datasets
- ❌ Data requiring authentication/licensing
- ❌ Future data (post-2015 for training locations)
- ❌ Validation set labels (obviously!)

**Attribution Requirements:**

- 📝 Document all data sources in your model
- 📝 Provide links to datasets used
- 📝 Explain how features were derived

---

## 📈 Model Performance Tracking

### Current Status

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| **Mean R² Score** | TBD | > 0.40 | 🔄 In Progress |
| **Leaderboard Rank** | TBD | Top 10 | 🎯 Goal |
| **Experiments Completed** | 0 | 15+ | 📊 Planning |

### Experiment Log

| Experiment ID | Date | Model Type | Features | Mean R² | Rank | Notes |
|---------------|------|------------|----------|---------|------|-------|
| **BASELINE** | TBD | Linear Regression | Basic satellite + climate | 0.20 | - | Starting point |
| **EXP-001** | TBD | - | - | TBD | TBD | - |
| **EXP-002** | TBD | - | - | TBD | TBD | - |

*For detailed experiment tracking, see [EXPERIMENTS.md](./experiments/EXPERIMENTS.md)*

---

## 🔬 Approach & Methodology

### Phase 1: Data Exploration ✅ (In Progress)
- [x] Review challenge documentation
- [x] Set up repository structure
- [ ] Run baseline benchmark model
- [ ] Exploratory data analysis (EDA)
- [ ] Understand spatial/temporal patterns
- [ ] Identify data quality issues

### Phase 2: Feature Engineering 🔄 (Planned)
- [ ] **Spectral indices:** NDVI, NDWI, turbidity proxies
- [ ] **Spatial features:** Distance to urban centers, agriculture, water bodies
- [ ] **Temporal features:** Seasonality, rainfall patterns, lag variables
- [ ] **Climate anomalies:** Deviations from historical norms
- [ ] **Domain-specific:** Banking risk assessment-inspired features

### Phase 3: Model Development 📅 (Upcoming)
- [ ] Baseline comparison (Linear, Ridge, Lasso)
- [ ] Tree-based models (Random Forest, XGBoost, LightGBM)
- [ ] Parameter-specific optimization
- [ ] Ensemble methods
- [ ] Hyperparameter tuning

### Phase 4: Validation & Submission 🎯 (Final Week)
- [ ] Cross-validation with spatial awareness
- [ ] Model interpretability (SHAP values)
- [ ] Final ensemble selection
- [ ] Generate predictions for validation set
- [ ] Submit to leaderboard

### Phase 5: Business Plan (If Top 5) 🏆
- [ ] 4-page written document
- [ ] 5-minute video presentation
- [ ] Scaling strategy
- [ ] Socioeconomic impact analysis
- [ ] Policy recommendations

---

## 🛠️ Technical Stack

### Development Environment
![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)

### ML & Data Science
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=for-the-badge)

### Geospatial & Satellite Data
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=for-the-badge)
![Rasterio](https://img.shields.io/badge/Rasterio-4051B5?style=for-the-badge)
![xarray](https://img.shields.io/badge/xarray-3776AB?style=for-the-badge)

### Visualization
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-7db0bc?style=for-the-badge)

### Version Control
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📁 Repository Structure
```
EY-Water-Quality-Challenge-2026/
│
├── 📓 notebooks/
│   ├── official/                                   # Official challenge notebooks
│   │   ├── Benchmark_Model_Notebook.ipynb
│   │   ├── Landsat_Data_Extraction_Notebook.ipynb
│   │   ├── TerraClimate_Data_Extraction_Notebook.ipynb
│   │   ├── Landsat_Demonstration_Notebook.ipynb
│   │   └── TerraClimate_Demonstration_Notebook.ipynb
│   │
│   └── my_work/                                    # My custom notebooks
│       ├── 01_eda_analysis.ipynb
│       ├── 02_feature_engineering.ipynb
│       ├── 03_model_experiments.ipynb
│       └── 04_final_model.ipynb
│
├── 📊 data/
│   ├── raw/
│   │   ├── water_quality_training_dataset.csv
│   │   └── submission_template.csv
│   ├── features/
│   │   ├── landsat_features_training.csv
│   │   ├── landsat_features_validation.csv
│   │   ├── terraclimate_features_training.csv
│   │   └── terraclimate_features_validation.csv
│   ├── processed/
│   │   └── [my engineered features]
│   └── submissions/
│       └── [leaderboard submissions]
│
├── 🛠️ src/
│   ├── data_loader.py                              # Data loading utilities
│   ├── feature_engineering.py                      # Feature creation functions
│   ├── model_utils.py                              # Model training utilities
│   ├── evaluation.py                               # Metrics & validation
│   └── visualization.py                            # Plotting functions
│
├── 📈 results/
│   ├── models/                                     # Saved model files
│   ├── predictions/                                # Prediction outputs
│   └── figures/                                    # Visualizations
│
├── 📝 docs/
│   ├── EXPERIMENTS.md                              # Detailed experiment log
│   ├── DATA_DICTIONARY.md                          # Feature documentation
│   ├── Participant_Guidance.pdf                    # Official guidance
│   └── REFERENCES.md                               # Citations & resources
│
├── README.md                                       # This file
├── requirements.txt                                # Python dependencies
├── .gitignore                                      # Git ignore rules
└── LICENSE                                         # Apache 2.0
```

---

## 🚀 Getting Started

### Prerequisites
```bash
- Python 3.8+
- Jupyter Notebook or JupyterLab
- 16GB+ RAM recommended
- Git for version control
```

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/LinusConradM/EY-Water-Quality-Challenge-2026.git
cd EY-Water-Quality-Challenge-2026

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Mac/Linux
# venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter Notebook
jupyter notebook
```

### Quick Start Guide

1. **Download Challenge Data**
   - Download `General.ZIP` from EY Challenge portal
   - Extract official notebooks to `notebooks/official/`
   - Extract data files to `data/raw/` and `data/features/`

2. **Run the baseline model**
   - Open `notebooks/official/Benchmark_Model_Notebook.ipynb`
   - Execute all cells
   - Record your baseline R² score
   - Make your first leaderboard submission

3. **Explore demonstration notebooks**
   - `Landsat_Demonstration_Notebook.ipynb` - Satellite data techniques
   - `TerraClimate_Demonstration_Notebook.ipynb` - Climate data access

4. **Start your own analysis**
   - Create notebooks in `notebooks/my_work/`
   - Begin with EDA and feature engineering
   - Experiment with different models
   - Track all experiments systematically

---

## 💡 Key Insights & Hypotheses

### Spatial Patterns Observed

- 🔴 **Poor water quality:** Urban centers (Cape Town, Johannesburg, Pretoria)
- 🟢 **Good water quality:** Eastern regions (Durban, Kruger National Park)
- 💡 **Hypothesis:** Urbanization and mining are primary pollution drivers

### Temporal Patterns Expected

- 🌧️ Seasonal rainfall variations should impact all three parameters
- 📅 Lag effects: Previous months' climate affects current water quality
- 🔄 Drought periods (low PDSI) may concentrate pollutants

### Feature Importance Predictions

**Most Likely Important:**

1. Distance to urban centers / population density
2. Proximity to agricultural land
3. Recent precipitation (1-3 month lag)
4. Vegetation health (NDVI)
5. Seasonal indicators

---

## 🌟 Why This Project Matters

> *"Water quality is not just an environmental metric—it is a cornerstone of public health and urban sustainability."*

### Real-World Impact

**If my model achieves Top 5:**

- ✅ Provides open-source tool for water quality monitoring
- ✅ Enables early warning for contamination events
- ✅ Informs policy decisions in vulnerable regions
- ✅ Reduces reliance on expensive traditional monitoring

### Personal Growth

This challenge is helping me:

- 🎓 Apply classroom ML theory to real-world sustainability problems
- 🛰️ Gain experience with satellite data and geospatial analysis
- 💻 Develop end-to-end ML project management skills
- 📊 Build a portfolio-worthy project for career transition

### Career Alignment

Combines my:

- **Past:** Banking risk assessment expertise
- **Present:** MS Analytics studies at American University
- **Future:** Data science career in environmental or financial sectors

---

## 📚 Resources & References

### Official Challenge Resources
- [EY Challenge Portal](https://challenge.ey.com/)
- [Challenge Data Description](https://challenge.ey.com/challenges/2026-optimizing-clean-water-supply/data)
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/)

### Technical Documentation
- [Landsat Data Handbook](https://www.usgs.gov/landsat-missions/landsat-data-users-handbook)
- [TerraClimate Documentation](https://www.climatologylab.org/terraclimate.html)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)

### Academic References
1. Ilic et al. (2025). *Enhancing monitoring for river water quality: satellite data and ML.* Blue-Green Systems 7(2):338-352.
2. Nakkazi et al. (2024). *Linking land use and precipitation to water quality in Lake Victoria.* Environmental Monitoring 196:1104.

---

## 🤝 Connect & Collaborate

I'm actively seeking **Data Analyst, Data Scientist, and AI Engineer** opportunities starting May 2026.

**Interested in:**
- Environmental data science & sustainability
- Financial analytics & risk modeling
- AI/ML for social impact
- Geospatial analysis

**Let's connect:**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/conrad-linus-m/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LinusConradM)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:linusconradm@gmail.com)

---

## 🔄 Project Timeline

- **Week 1 (Jan 20-26):** ✅ Setup, baseline model, EDA
- **Week 2 (Jan 27-Feb 2):** 🔄 Feature engineering, initial improvements
- **Week 3-6 (Feb 3-Mar 2):** Model experimentation & optimization
- **Week 7 (Mar 3-9):** Final ensemble, validation
- **Week 8 (Mar 10-13):** Business plan (if Top 5) & final submission

**Next Milestone:** Run baseline model and establish starting R² score

---

## 📝 License & Acknowledgments

### License
- **Challenge Materials:** © 2026 EY
- **My Code:** Apache 2.0 License
- **Original Challenge Repository:** [Snowflake-Labs/EY-AI-and-Data-Challenge](https://github.com/Snowflake-Labs/EY-AI-and-Data-Challenge)

### Acknowledgments
- **EY AI & Data Challenge Program** for organizing this vital competition
- **American University Kogod School of Business** for academic support
- **Harmonia Holdings Group** for foundational AI/ML training
- **Microsoft Planetary Computer** for satellite data access

---

<div align="center">

## 🌊 Clean Water for All 🌍

*Every model improvement brings us closer to protecting vulnerable communities worldwide.*

[![UN SDG 6](https://img.shields.io/badge/UN_SDG-6:_Clean_Water_&_Sanitation-4C9F38?style=flat-square)](https://sdgs.un.org/goals/goal6)
[![EY Ripples](https://img.shields.io/badge/EY_Ripples-Impact_1B_Lives-FFE600?style=flat-square)](https://www.ey.com/en_gl/corporate-responsibility/ey-ripples)

**Last Updated:** February 5, 2026

</div>