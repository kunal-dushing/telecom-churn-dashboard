# Telecom Customer Churn Analysis

> **Live demo:** [Open the Telecom Churn Analysis website](https://telecom-churn-project-sable.vercel.app/)

A portfolio project exploring customer churn patterns in IBM's public Telco Customer Churn sample dataset. The website presents descriptive findings, a baseline churn model, and retention ideas for further investigation.

## Project highlights

- 7,043 customer records across 21 columns
- Overall churn rate: **26.5%** (1,869 customers)
- Contract churn: month-to-month **42.7%**, one year **11.3%**, two year **2.8%**
- Tenure churn: 0–12 months **47.4%**, 13–24 months **28.7%**, 25–48 months **20.4%**, 49–72 months **9.5%**
- Fiber optic churn rate: **41.9%** in this sample
- Logistic regression baseline: **0.842 ROC-AUC**, **78% churn recall**, **50% churn precision** on a stratified held-out test set

## Live website

The Vercel website is a static, filterable dashboard in `public/index.html`. Its sidebar filters recalculate the selected customer totals and contract/tenure charts using aggregate data in `public/churn_segments.json`. Model metrics and interpretation notes are also shown. The Vercel settings are defined in `vercel.json`.

## Local interactive dashboard

The repository also contains a Streamlit dashboard with filters for contract type and internet service.

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Run the analysis

```powershell
python churn_model.py
```

This trains and evaluates the baseline model, then saves `churn_model.joblib` and `test_predictions.csv`.

To preview the static site locally, run this from the project root:

```powershell
python -m http.server 8000 --directory public
```

Then open [http://localhost:8000](http://localhost:8000).

## Data preparation

- The original sample CSV is kept as `Telco-Customer-Churn.csv`.
- Eleven blank `TotalCharges` entries all belonged to customers with zero tenure; they were converted to 0 in `Telco-Customer-Churn-clean.csv`.
- No duplicate rows were found.
- `customerID` is excluded from the model features because it is an identifier.

## Project structure

```text
telecom-churn-project/
├── public/
│   ├── index.html                    # Filterable static website served by Vercel
│   └── churn_segments.json           # Segment aggregates used by dashboard filters
├── app.py                            # Local interactive Streamlit dashboard
├── churn_model.py                    # Model training and evaluation
├── churn_model.joblib                # Saved trained pipeline
├── churn_by_contract.png             # Contract churn chart
├── Telco-Customer-Churn.csv          # Original public sample data
├── Telco-Customer-Churn-clean.csv    # Cleaned data used by the project
├── test_predictions.csv              # Held-out test predictions
├── requirements.txt                  # Python dependencies
├── vercel.json                       # Vercel static-site configuration
└── README.md
```

## Technology

- Python, pandas, scikit-learn, joblib
- Streamlit for the local interactive dashboard
- HTML and CSS for the static website
- Vercel for web hosting

## Interpretation and limitations

This is a fictional company sample dataset, not live customer data from a telecom operator. Segment differences and model coefficients are associations; they do not establish causes. Model results come from one train-test split and should be validated on new data. Retention ideas should be tested before broad rollout, and churn scores should not be used as automatic decisions.

## Dataset source

[IBM Telco Customer Churn sample repository](https://github.com/IBM/telco-customer-churn-on-icp4d)


