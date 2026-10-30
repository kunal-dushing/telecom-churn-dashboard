import pandas as pd
import streamlit as st

st.set_page_config(page_title="Telecom Churn Dashboard", layout="wide")
st.title("Telecom Customer Churn Dashboard")
st.caption("Exploration of IBM's public sample dataset—not live company data.")

@st.cache_data
def load_data():
    data = pd.read_csv("Telco-Customer-Churn-clean.csv")
    data["Tenure group"] = pd.cut(
        data["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=["0–12 months", "13–24 months", "25–48 months", "49–72 months"],
    )
    return data

df = load_data()

st.sidebar.header("Filter customers")
contracts = st.sidebar.multiselect(
    "Contract type",
    options=sorted(df["Contract"].unique()),
    default=sorted(df["Contract"].unique()),
)
services = st.sidebar.multiselect(
    "Internet service",
    options=sorted(df["InternetService"].unique()),
    default=sorted(df["InternetService"].unique()),
)

filtered = df[
    df["Contract"].isin(contracts)
    & df["InternetService"].isin(services)
]

if filtered.empty:
    st.warning("Choose at least one contract type and one internet service.")
    st.stop()

customer_count = len(filtered)
churned_count = int((filtered["Churn"] == "Yes").sum())
churn_rate = (churned_count / customer_count) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Customers in selection", f"{customer_count:,}")
col2.metric("Churned customers", f"{churned_count:,}")
col3.metric("Churn rate", f"{churn_rate:.1f}%")

st.subheader("Churn rate by contract")
contract_summary = (
    filtered.groupby("Contract", observed=True)
    .agg(
        Customers=("Churn", "size"),
        Churned=("Churn", lambda values: (values == "Yes").sum()),
    )
    .reset_index()
)
contract_summary["Churn rate (%)"] = (
    contract_summary["Churned"] / contract_summary["Customers"] * 100
).round(1)
st.bar_chart(contract_summary, x="Contract", y="Churn rate (%)")
st.dataframe(contract_summary)

st.subheader("Churn rate by customer tenure")
tenure_summary = (
    filtered.groupby("Tenure group", observed=True)
    .agg(
        Customers=("Churn", "size"),
        Churned=("Churn", lambda values: (values == "Yes").sum()),
    )
    .reset_index()
)
tenure_summary["Churn rate (%)"] = (
    tenure_summary["Churned"] / tenure_summary["Customers"] * 100
).round(1)
st.bar_chart(tenure_summary, x="Tenure group", y="Churn rate (%)")
st.dataframe(tenure_summary)

st.subheader("Baseline model evaluation")
m1, m2, m3 = st.columns(3)
m1.metric("Accuracy", "0.74")
m2.metric("Churn recall", "0.78")
m3.metric("ROC-AUC", "0.842")

st.write(
    "On the held-out test set, the model found 293 of 374 customers who churned. "
    "It also flagged 288 customers who stayed. These results are a baseline, "
    "not a guarantee of performance on new customers."
)