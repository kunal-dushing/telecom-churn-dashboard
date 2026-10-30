\# Telecom Customer Churn Analysis



\## Business question

Which customer groups are associated with churn, and can a baseline model help identify customers at higher risk?



\## Dataset

This project uses IBM's public Telco Customer Churn sample dataset. It contains 7,043 customer records and 21 columns. It is a sample dataset, not live data from an actual telecom company.



\## Data preparation

\- Checked for duplicate rows and missing values.

\- Found 11 blank `TotalCharges` values. All 11 customers had zero months of tenure, so set their total charges to 0.

\- Excluded `customerID` from model features because it is an identifier.



\## Descriptive findings

\- Overall churn rate: 26.5%.

\- Month-to-month contract churn: 42.7% (1,655 of 3,875 customers).

\- One-year contract churn: 11.3% (166 of 1,473 customers).

\- Two-year contract churn: 2.8% (48 of 1,695 customers).

\- Churn was 47.4% among customers with 0–12 months of tenure and 9.5% among customers with 49–72 months.

\- Fiber optic customers had a 41.9% churn rate in this sample.



\## Model

A logistic regression pipeline was trained with a stratified 80/20 train-test split. Numeric features were standardized and categorical features were one-hot encoded. Class weighting was used to account for the difference in class sizes.



Test-set results:

\- Accuracy: 0.74

\- Churn precision: 0.50

\- Churn recall: 0.78

\- Churn F1-score: 0.61

\- ROC-AUC: 0.842



The model found 293 of 374 churners in the test set and incorrectly flagged 288 customers who stayed.



\## Recommendations to investigate

\- Review onboarding and support for customers in their first year.

\- Test suitable renewal offers for month-to-month customers.

\- Investigate fiber service quality, pricing, and support experience.

\- Evaluate retention offers with a controlled experiment before broad rollout.



\## Limitations

These are associations in a sample dataset, not proof of what causes churn. Model performance is measured on one held-out split and may change on new data. False positives have a cost, so a real retention team should choose a contact threshold based on intervention capacity and costs. Test-set predictions are for evaluation, not a live customer contact list.



\## Project files

\- `Telco-Customer-Churn.csv` — original data

\- `Telco-Customer-Churn-clean.csv` — cleaned copy

\- `churn\_by\_contract.png` — contract churn chart

\- `churn\_model.py` — model training and evaluation

\- `churn\_model.joblib` — saved trained model

\- `test\_predictions.csv` — held-out test predictions
## Run the dashboard

Open PowerShell in this project folder and install the required packages:

```powershell
python -m pip install -r requirements.txt
