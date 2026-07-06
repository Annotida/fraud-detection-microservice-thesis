import joblib

MODEL_PATH = "models/fraud_model.pkl"

model = joblib.load(MODEL_PATH)

print("Random Forest model loaded successfully.")