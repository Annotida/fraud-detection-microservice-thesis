from fastapi import FastAPI
from app.predict import router

app = FastAPI(
    title="Fraud Detection ML Service",
    version="1.0"
)

app.include_router(router)