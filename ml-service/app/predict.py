from fastapi import APIRouter
from app.schemas import TransactionRequest, PredictionResponse
from app.model_loader import model
from app.feature_engineering import build_features

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):

    features = build_features(transaction)

    prediction = int(model.predict(features)[0])

    probability = float(model.predict_proba(features)[0][1])

    return PredictionResponse(
        prediction=prediction,
        confidence=probability
    )