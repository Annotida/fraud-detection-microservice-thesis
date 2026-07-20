import pandas as pd

from app.schemas import TransactionRequest
from app.model_loader import label_encoders

def build_features(transaction: TransactionRequest):

    data = pd.DataFrame([{
        "persona": transaction.persona,
        "merchant": transaction.merchant,
        "amount": transaction.amount,
        "country": transaction.country,
        "transaction_type": transaction.transactionType,
        "device": transaction.deviceId,
        "preferred_device": transaction.preferredDevice,
        "hour": transaction.hour
    }])

    categorical_columns = [
        "persona",
        "merchant",
        "country",
        "transaction_type",
        "device",
        "preferred_device"
    ]

    from fastapi import HTTPException

    for column in categorical_columns:

        value = data[column].iloc[0]

        encoder = label_encoders[column]

        if value not in encoder.classes_:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown {column}: '{value}'. The model was not trained with this value."
            )

        data[column] = encoder.transform(data[column])

    return data