from pydantic import BaseModel


# ==========================================================
# KAGGLE REQUEST SCHEMA (ARCHIVED)
# ==========================================================
#
# class TransactionRequest(BaseModel):
#     amount: float
#     merchant: str
#     location: str
#     transactionType: str
#     deviceId: str


# ==========================================================
# BUSINESS MODEL REQUEST SCHEMA (ACTIVE)
# ==========================================================

class TransactionRequest(BaseModel):

    amount: float
    merchant: str
    country: str
    transactionType: str
    deviceId: str
    preferredDevice: str
    persona: str
    hour: int


class PredictionResponse(BaseModel):

    prediction: str
    confidence: float
    
#This file defines exactly what Spring Boot is allowed to send