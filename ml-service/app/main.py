from fastapi import FastAPI

from app.model_loader import model
from app.predict import router

app = FastAPI(
    title="Fraud Detection ML Service",
    version="1.0",
    description="""
A cloud-native fraud detection microservice built with FastAPI and
Random Forest Machine Learning.

Features:

- Real-time fraud prediction
- Feature engineering pipeline
- Configurable fraud risk profiles
- REST API
- Docker deployment
"""
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "service": "Fraud Detection ML Service",
        "status": "Running"
    }


@app.get("/health")
def health():

    return {
        "status": "UP",
        "service": "Fraud Detection ML Service",
        "model": "Random Forest",
        "model_loaded": model is not None,
        "version": "1.0.0",
        "features": 30
    }