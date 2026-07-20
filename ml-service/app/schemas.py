from pydantic import BaseModel

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