import joblib
import os

MODEL_PATH = os.path.join("models", "fraud_model_business.pkl")

ENCODER_PATH = os.path.join("models", "label_encoders.pkl")

model = joblib.load(MODEL_PATH)

label_encoders = joblib.load(ENCODER_PATH)

print("===================================")
print(" Business Random Forest Model Loaded")
print(" Label Encoders Loaded")
print("===================================")
