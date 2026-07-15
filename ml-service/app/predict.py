from fastapi import APIRouter
from app.schemas import TransactionRequest, PredictionResponse
from app.model_loader import model
from app.feature_engineering import build_features

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):

    # Build feature vector
    features = build_features(transaction)

    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    prediction_label = (
        "FRAUD"
        if prediction == 1
        else "LEGITIMATE"
    )

    confidence = (
        probability * 100
        if prediction == 1
        else (1 - probability) * 100
    )

    # ============================
    # Logging
    # ============================

    print("\n====================================================")
    print("           AI FRAUD DETECTION PREDICTION")
    print("====================================================")

    print(f"Amount              : R{transaction.amount}")
    print(f"Merchant            : {transaction.merchant}")
    print(f"Location            : {transaction.location}")
    print(f"Transaction Type    : {transaction.transactionType}")
    print(f"Device ID           : {transaction.deviceId}")

    print("----------------------------------------------------")

    print("Feature Vector")

    print(features)

    print("----------------------------------------------------")

    print(f"Prediction          : {prediction_label}")
    print(f"Confidence          : {confidence:.2f}%")

    print("====================================================\n")

    return PredictionResponse(
        prediction=prediction_label,
        confidence=round(confidence, 2)
    )