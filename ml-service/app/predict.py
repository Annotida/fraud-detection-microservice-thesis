from fastapi import APIRouter

from fastapi import HTTPException
import traceback

from app.schemas import TransactionRequest, PredictionResponse
from app.model_loader import model
from app.feature_engineering import build_features

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):

    try:

        features = build_features(transaction)

        prediction = int(model.predict(features)[0])

        probability = float(model.predict_proba(features)[0][1])

    except HTTPException:
        raise

    
    except Exception as e:
        print("\n========== ML ERROR ==========")
        traceback.print_exc()
        print("==============================\n")

        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {str(e)}"
        )

    print(f"Fraud Probability : {probability:.6f}")

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

    print("\n====================================================")
    print("      BUSINESS FRAUD DETECTION PREDICTION")
    print("====================================================")

    print(f"Amount              : R{transaction.amount}")
    print(f"Merchant            : {transaction.merchant}")
    print(f"Country             : {transaction.country}")
    print(f"Transaction Type    : {transaction.transactionType}")
    print(f"Device ID           : {transaction.deviceId}")
    print(f"Preferred Device    : {transaction.preferredDevice}")
    print(f"Persona             : {transaction.persona}")
    print(f"Hour                : {transaction.hour}")

    print("----------------------------------------------------")

    print("Encoded Features")

    print(features)

    print("----------------------------------------------------")

    print(f"Prediction          : {prediction_label}")
    print(f"Confidence          : {confidence:.2f}%")

    print("====================================================\n")

    return PredictionResponse(
        prediction=prediction_label,
        confidence=round(confidence, 2)
    )