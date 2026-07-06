import joblib
import os

MODEL_PATH = os.path.join("models", "fraud_model.pkl")

model = joblib.load(MODEL_PATH)

print("===================================")
print(" Random Forest Model Loaded")
print("===================================")