import joblib
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

#Paths

DATASET_PATH = Path(__file__).parent / "datasets" / "business_transactions.csv"

MODEL_PATH = Path(__file__).parent / "models" / "fraud_model_business.pkl"

ENCODER_PATH = Path(__file__).parent / "models" / "label_encoders.pkl"

OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

#Load

print("=" * 50)
print("Loading Dataset and Model")
print("=" * 50)

df = pd.read_csv(DATASET_PATH)

model = joblib.load(MODEL_PATH)

label_encoders = joblib.load(ENCODER_PATH)

print("Dataset Loaded")

print("Model Loaded")

print("Encoders Loaded")

#prepare data

columns_to_drop = [
    "transaction_id",
    "timestamp",
    "customer_id",
    "fraud_score"
]

X = df.drop(columns=columns_to_drop + ["label"])

y = df["label"]

categorical_columns = [
    "persona",
    "merchant",
    "country",
    "transaction_type",
    "device",
    "preferred_device"
]

for column in categorical_columns:
    X[column] = label_encoders[column].transform(X[column])
    
#train/test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

#predict

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

# MODEL METRICS

accuracy = accuracy_score(y_test, predictions)

precision = precision_score(y_test, predictions)

recall = recall_score(y_test, predictions)

f1 = f1_score(y_test, predictions)

auc = roc_auc_score(y_test, probabilities)

print("\n========== MODEL PERFORMANCE ==========")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"AUC ROC  : {auc:.4f}")

#save metrics to file

metrics_file = OUTPUT_DIR / "metrics.txt"

with open(metrics_file, "w") as f:
    f.write("Business Fraud Detection Model Evaluation\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Accuracy : {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall   : {recall:.4f}\n")
    f.write(f"F1 Score : {f1:.4f}\n")
    f.write(f"AUC ROC  : {auc:.4f}\n")

print(f"\nMetrics saved to: {metrics_file}")

#confusion matrix

cm = confusion_matrix(y_test, predictions)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.title("Confusion Matrix")

plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=300)

plt.close()

#roc curve

RocCurveDisplay.from_predictions(y_test, probabilities)

plt.title("ROC Curve")

plt.savefig(OUTPUT_DIR / "roc_curve.png", dpi=300)

plt.close()

#precision-recall curve

PrecisionRecallDisplay.from_predictions(y_test, probabilities)

plt.title("Precision-Recall Curve")

plt.savefig(OUTPUT_DIR / "precision_recall_curve.png", dpi=300)

plt.close()

#feature importance

feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

feature_importance = feature_importance.sort_values()

plt.figure(figsize=(10,6))

feature_importance.plot(kind="barh")

plt.title("Feature Importance")

plt.xlabel("Importance")

plt.tight_layout()

plt.savefig(OUTPUT_DIR / "feature_importance.png", dpi=300)

plt.close()

#final message

print("\nEvaluation completed successfully!")

print(f"\nResults saved to:\n{OUTPUT_DIR}")