import joblib

def save_model(model):

    joblib.dump(model, "models/fraud_model.pkl")

    print("\nModel saved successfully.")