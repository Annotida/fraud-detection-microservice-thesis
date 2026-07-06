from fastapi import APIRouter
from app.schemas import TransactionRequest, PredictionResponse
from app.model_loader import model

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):

    # Placeholder feature vector
    # This will be replaced in the next phase with proper feature engineering.
    features = [[
        0,          # Time
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        transaction.amount
    ]]

    prediction = int(model.predict(features)[0])

    probability = float(model.predict_proba(features)[0][1])

    return PredictionResponse(
        prediction=prediction,
        confidence=probability
    )