package com.frauddetection.fraud_detection_service.dto;

public class PredictionResponse {

    private String prediction;
    private Double confidence;

    public PredictionResponse() {
    }

    public String getPrediction() {
        return prediction;
    }

    public void setPrediction(String prediction) {
        this.prediction = prediction;
    }

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }
}