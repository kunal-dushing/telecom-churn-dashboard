import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("Telco-Customer-Churn-clean.csv")

# CustomerID identifies a record; it should not be used to predict churn.
X = df.drop(columns=["Churn", "customerID"])
y = df["Churn"]

numeric_features = X.select_dtypes(include="number").columns.tolist()
categorical_features = X.select_dtypes(exclude="number").columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numeric_features),
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
churn_probabilities = model.predict_proba(X_test)[:, 1]

print("Test-set classification report:")
print(classification_report(y_test, predictions, labels=["No", "Yes"]))

print("Confusion matrix (actual rows; predicted columns; order: No, Yes):")
print(confusion_matrix(y_test, predictions, labels=["No", "Yes"]))

print("ROC-AUC:", round(roc_auc_score(y_test, churn_probabilities), 3))
import joblib

joblib.dump(model, "churn_model.joblib")

test_results = pd.DataFrame({
    "customerID": df.loc[X_test.index, "customerID"].values,
    "actual_churn": y_test.values,
    "predicted_churn": predictions,
    "churn_probability": churn_probabilities.round(3),
})
test_results.to_csv("test_predictions.csv", index=False)

print("Saved churn_model.joblib and test_predictions.csv")