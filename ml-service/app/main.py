from fastapi import FastAPI

from app.model_loader import model
from app.predict import router

app = FastAPI(
    title="Fraud Detection ML Service",
    version="2.0",
    description="""
Cloud-native AI fraud detection microservice built with FastAPI and
a Business Random Forest Machine Learning model.

Features:

- Real-time fraud prediction
- Business transaction feature encoding
- LabelEncoder preprocessing
- REST API
- Docker deployment
"""
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "service": "Fraud Detection ML Service",
        "status": "Running",
        "model": "Business Random Forest"
    }


@app.get("/health")
def health():

    # ==========================================================
    # KAGGLE MODEL HEALTH (ARCHIVED)
    # ==========================================================
    #
    # return {
    #     "status": "UP",
    #     "service": "Fraud Detection ML Service",
    #     "model": "Random Forest",
    #     "model_loaded": model is not None,
    #     "version": "1.0.0",
    #     "features": 30
    # }

    # ==========================================================
    # BUSINESS MODEL HEALTH (ACTIVE)
    # ==========================================================

    return {
        "status": "UP",
        "service": "Fraud Detection ML Service",
        "model": "Business Random Forest",
        "model_loaded": model is not None,
        "version": "2.0.0",
        "features": 8,
        "categorical_features": 6,
        "numeric_features": 2
    }