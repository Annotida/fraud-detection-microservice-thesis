import pandas as pd

#Required Imports

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
import joblib

# Load the dataset
df = pd.read_csv("data/raw/creditcard.csv")

# Display the first five rows
print(df.head())

# Display the dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display the class distribution
print("\nFraud Class Distribution:")
print(df["Class"].value_counts())

# Display the class percentages
print("\nFraud Class Percentage:")
print(df["Class"].value_counts(normalize=True) * 100)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# Prepare Features and Target
# -------------------------------

X = df.drop("Class", axis=1)
y = df["Class"]

print("\nFeature Matrix Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

# -------------------------------
# Split the Dataset
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Set:")
print(X_train.shape)

print("\nTesting Set:")
print(X_test.shape)

#Using stratify=y ensures the training and test sets maintain the same fraud/non-fraud ratio as the original dataset.

# -------------------------------
# Train the Random Forest Model
# -------------------------------

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed.")

# -------------------------------
# Evaluate the Model
# -------------------------------

print("\nEvaluating Model...")

# Make predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Precision
precision = precision_score(y_test, y_pred)

# Recall
recall = recall_score(y_test, y_pred)

# F1 Score
f1 = f1_score(y_test, y_pred)

print("\nModel Performance")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# -------------------------------
# Logistic Regression Model
# -------------------------------

print("\n===================================")
print("Training Logistic Regression Model")
print("===================================")

logistic_model = LogisticRegression(
    random_state=42,
    max_iter=1000
)

logistic_model.fit(X_train, y_train)

print("Logistic Regression training completed.")

# Predictions
logistic_predictions = logistic_model.predict(X_test)

# Metrics
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
logistic_precision = precision_score(y_test, logistic_predictions)
logistic_recall = recall_score(y_test, logistic_predictions)
logistic_f1 = f1_score(y_test, logistic_predictions)

print("\nLogistic Regression Performance")

print(f"Accuracy : {logistic_accuracy:.4f}")
print(f"Precision: {logistic_precision:.4f}")
print(f"Recall   : {logistic_recall:.4f}")
print(f"F1 Score : {logistic_f1:.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, logistic_predictions))

print("\nClassification Report")
print(classification_report(y_test, logistic_predictions))

#Random Forest is the selected model
#The Random Forest model outperformed Logistic Regression on every evaluation metric.
#For a fraud detection system, the most important metric is often recall,
# because missing fraudulent transactions (false negatives) can be more costly than investigating a few legitimate ones.

#Your results:
#Logistic Regression Recall = 70.41%
#Random Forest Recall = 81.63%
#Random Forest detected 11% more fraud cases than Logistic Regression on this test set.

# -------------------------------
# Save the Best Model
# -------------------------------

print("\nSaving Random Forest Model...")

joblib.dump(model, "models/fraud_model.pkl")

print("Model saved successfully!")