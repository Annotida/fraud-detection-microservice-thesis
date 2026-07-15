from pydantic import BaseModel


class TransactionRequest(BaseModel):
    amount: float
    merchant: str
    location: str
    transactionType: str
    deviceId: str


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    
#This file defines exactly what Spring Boot is allowed to send