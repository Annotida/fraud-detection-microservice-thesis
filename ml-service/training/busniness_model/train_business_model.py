import joblib
from pathlib import Path

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

DATASET_PATH = Path(__file__).parent / "datasets" / "business_transactions.csv"

MODEL_DIR = Path(__file__).parent / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "fraud_model_business.pkl"

ENCODER_PATH = MODEL_DIR / "label_encoders.pkl"

print("=" * 50)
print("Loading dataset...")
print("=" * 50)

df = pd.read_csv(DATASET_PATH)

print(df.head())

print("\nDataset Shape:", df.shape)

# ==========================================
# PREPARE FEATURES
# ==========================================

columns_to_drop = [
    "transaction_id",
    "timestamp",
    "customer_id",
    "fraud_score"
]

X = df.drop(columns=columns_to_drop + ["label"])

expected_features = [
    "persona",
    "merchant",
    "amount",
    "country",
    "transaction_type",
    "device",
    "preferred_device",
    "hour"
]

if list(X.columns) != expected_features:
    raise ValueError(
        f"Unexpected feature order.\nExpected: {expected_features}\nGot: {list(X.columns)}"
    )

y = df["label"]

print("\nFeatures Used For Training:")
print(X.columns.tolist())

print("\nTarget Distribution:")
print(y.value_counts())

label_encoders = {}

categorical_columns = [

    "persona",
    "merchant",
    "country",
    "transaction_type",
    "device",
    "preferred_device"

]

for column in categorical_columns:

    encoder = LabelEncoder()

    X[column] = encoder.fit_transform(X[column].astype(str))

    label_encoders[column] = encoder
    
    
X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,
    random_state=42,
    stratify=y

)

print("\nTraining Random Forest...\n")

model = RandomForestClassifier(

    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1

)

model.fit(X_train, y_train)

print("Training Complete.")

#Predictions
predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)[:, 1]

#Evaluation

accuracy = accuracy_score(y_test, predictions)

precision = precision_score(y_test, predictions)

recall = recall_score(y_test, predictions)

f1 = f1_score(y_test, predictions)

auc = roc_auc_score(y_test, probabilities)

print("\n========== MODEL RESULTS ==========")

print(f"Accuracy : {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall   : {recall:.4f}")

print(f"F1 Score : {f1:.4f}")

print(f"AUC ROC  : {auc:.4f}")

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

#Save Model

joblib.dump(model, MODEL_PATH)

joblib.dump(label_encoders, ENCODER_PATH)

print("\nModel Saved")

print(MODEL_PATH)

print("\nEncoders Saved")

print(ENCODER_PATH)

print("\nFeature Order Used By Model:")

print(list(X.columns))