package com.frauddetection.fraud_detection_service.dto;

public class PredictionResponse {

    private Integer prediction;
    private Double confidence;

    public PredictionResponse() {
    }

    public Integer getPrediction() {
        return prediction;
    }

    public void setPrediction(Integer prediction) {
        this.prediction = prediction;
    }

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }
}