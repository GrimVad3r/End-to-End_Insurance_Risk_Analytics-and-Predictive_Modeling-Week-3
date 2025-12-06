# AlphaCare Insurance Solutions - Risk & Predictive Analytics

## Overview

This repository contains a comprehensive insurance analytics project for **AlphaCare Insurance Solutions (ACIS)**, focused on analyzing historical car insurance claim data from South Africa to optimize marketing strategy and identify low-risk customer segments for premium optimization.

**Project Duration:** December 3-9, 2025  
**Data Period:** February 2014 - August 2015

## Business Objective

Analyze historical insurance claim data to:
- Discover "low-risk" customer segments for premium reduction
- Optimize marketing strategy to attract new clients
- Develop risk-based pricing models
- Validate key hypotheses about risk drivers across different demographic and geographic segments

## Project Structure
```
├── .github/
│   └── workflows/          # CI/CD pipelines
├── data/
│   ├── raw/               # Original data files (tracked with DVC)
│   └── processed/         # Cleaned and transformed data
├── notebooks/
│   ├── 01_eda.ipynb      # Exploratory Data Analysis
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data/             # Data processing scripts
│   ├── features/         # Feature engineering
│   ├── models/           # Model training and evaluation
│   └── visualization/    # Plotting utilities
├── tests/                # Unit tests
├── reports/              # Analysis reports and figures
├── .dvc/                 # DVC configuration
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Tasks

### Task 1: Git & GitHub Setup + EDA
- ✅ Repository initialization with version control
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Comprehensive Exploratory Data Analysis
- ✅ Data quality assessment and visualization

**Key Questions Explored:**
- What is the overall Loss Ratio (TotalClaims/TotalPremium)?
- How do claims vary by Province, VehicleType, and Gender?
- What are the distributions of key financial variables?
- Which vehicle makes/models have highest/lowest claims?

### Task 2: Data Version Control (DVC)
- ✅ DVC setup and configuration
- ✅ Local remote storage implementation
- ✅ Data versioning and tracking
- ✅ Reproducible data pipeline

### Task 3: A/B Hypothesis Testing
Statistical validation of key business hypotheses:

**Null Hypotheses Tested:**
1. H₀: No risk differences across provinces
2. H₀: No risk differences between zip codes
3. H₀: No significant margin (profit) difference between zip codes
4. H₀: No significant risk difference between Women and Men

**Metrics Used:**
- **Risk Quantification:** Claim Frequency & Claim Severity
- **Profitability:** Margin (TotalPremium - TotalClaims)

### Task 4: Statistical Modeling
Development of predictive models for:

**1. Claim Severity Prediction (Risk Model)**
- Target: TotalClaims (for policies with claims > 0)
- Metrics: RMSE, R-squared

**2. Premium Optimization (Pricing Framework)**
- Advanced: Probability of claim occurrence (binary classification)
- Risk-Based Premium Formula: `Premium = (P(Claim) × Predicted Severity) + Expenses + Profit`

**Models Implemented:**
- Linear Regression
- Decision Trees
- Random Forests
- XGBoost (Gradient Boosting)

**Model Interpretability:**
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)

## Data Description

### Dataset Features

**Policy Information:**
- UnderwrittenCoverID, PolicyID, TransactionMonth

**Client Demographics:**
- IsVATRegistered, Citizenship, LegalType, Title, Language
- Bank, AccountType, MaritalStatus, Gender

**Geographic Data:**
- Country, Province, PostalCode
- MainCrestaZone, SubCrestaZone

**Vehicle Information:**
- ItemType, VehicleType, Make, Model, RegistrationYear
- Cylinders, Cubiccapacity, Kilowatts, Bodytype, NumberOfDoors
- AlarmImmobiliser, TrackingDevice, NewVehicle, WrittenOff

**Insurance Plan:**
- SumInsured, TermFrequency, CalculatedPremiumPerTerm
- ExcessSelected, CoverCategory, CoverType, CoverGroup
- Section, Product, StatutoryClass

**Financial Metrics:**
- TotalPremium, TotalClaims

## Installation & Setup

### Prerequisites
- Python 3.8+
- Git
- DVC

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/alphacare-insurance-analytics.git
cd alphacare-insurance-analytics
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Initialize DVC:**
```bash
dvc init
dvc remote add -d localstorage /path/to/local/storage
dvc pull
```

## Usage

### Running EDA
```bash
jupyter notebook notebooks/01_eda.ipynb
```

### Hypothesis Testing
```bash
python src/analysis/hypothesis_testing.py
```

### Model Training
```bash
python src/models/train_model.py --model xgboost --target claims
```

### Model Evaluation
```bash
python src/models/evaluate_model.py --model-path models/xgboost_model.pkl
```

## Key Findings

*(This section will be updated as analysis progresses)*

### EDA Insights
- TBD

### Hypothesis Testing Results
- TBD

### Model Performance
- TBD

## Technologies Used

- **Languages:** Python
- **Data Analysis:** pandas, numpy, scipy, statsmodels
- **Visualization:** matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, xgboost
- **Model Interpretation:** SHAP, LIME
- **Version Control:** Git, DVC
- **CI/CD:** GitHub Actions
- **Testing:** pytest

## Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `task-1` - EDA and initial setup
- `task-2` - DVC implementation
- `task-3` - Hypothesis testing
- `task-4` - Statistical modeling

### Commit Convention
Following [Conventional Commits](https://www.conventionalcommits.org/):
```
feat: add new feature
fix: bug fix
docs: documentation changes
test: add tests
refactor: code refactoring
```

### Pull Request Process
1. Create feature branch from `main`
2. Make changes and commit with descriptive messages
3. Push to remote and create PR
4. Ensure CI/CD checks pass
5. Request review and merge

## Testing
```bash
pytest tests/
```

## Contributing
This is an academic project for the 10 Academy KAIM Week 3 challenge. Contributions are limited to team members.


## Timeline

| Date | Milestone |
|------|-----------|
| Dec 03, 2025 | Challenge Introduction |
| Dec 07, 2025 | Interim Submission (Task 1 & 2) |
| Dec 09, 2025 | Final Submission (All Tasks) |

## Deliverables

### Interim Submission (Dec 07, 2025 - 8:00 PM UTC)
- [ ] GitHub repository with merged task-1 and task-2
- [ ] Interim report covering EDA and DVC setup

### Final Submission (Dec 09, 2025 - 8:00 PM UTC)
- [ ] Complete GitHub repository
- [ ] Final report (Medium blog post format)
- [ ] Executive summary for leadership
- [ ] Data-backed recommendations for ACIS
- [ ] Model performance comparison
- [ ] Feature importance analysis

## References

### Insurance Analytics
- [FSRAO Insurance Analytics Guide](https://www.fsrao.ca/media/11501/download)
- [Data Analytics in Insurance - XenonStack](https://www.xenonstack.com/blog/data-analytics-in-insurance)

### Statistical Testing
- [A/B Testing Guide - Medium](https://medium.com/tiket-com/a-b-testing-hypothesis-testing-f9624ea5580e)

### Tools & Technologies
- [DVC Documentation](https://dvc.org/doc/user-guide)
- [XGBoost Guide](https://www.analyticsvidhya.com/blog/2018/09/an-end-to-end-guide-to-understand-the-math-behind-xgboost/)
- [SHAP Documentation](https://shap.readthedocs.io/)

## License
This project is part of the 10 Academy KAIM program and is for educational purposes only.

## Contact
For questions or issues, please open an issue in this repository or contact the facilitators.

---

**Note:** This is an ongoing project. Documentation will be updated as analysis progresses.