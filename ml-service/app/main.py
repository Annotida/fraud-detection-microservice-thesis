from fastapi import FastAPI

app = FastAPI(
    title="Fraud Detection ML Service",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Fraud Detection ML Service is running"
    }