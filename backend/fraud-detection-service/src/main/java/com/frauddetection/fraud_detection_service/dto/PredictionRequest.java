package com.frauddetection.fraud_detection_service.dto;

public class PredictionRequest {

    // ==========================================================
    // KAGGLE MODEL (ARCHIVED)
    // ==========================================================
    //
    // private Double amount;
    // private String merchant;
    // private String location;
    // private String transactionType;
    // private String deviceId;
    //
    // Previous DTO used for the Kaggle Random Forest model.
    // Retained for dissertation comparison.
    //
    // ==========================================================
    // BUSINESS MODEL (ACTIVE)
    // ==========================================================

    private Double amount;

    private String merchant;

    private String country;

    private String transactionType;

    private String deviceId;

    private String preferredDevice;

    private String persona;

    private Integer hour;

    public PredictionRequest() {
    }

    public Double getAmount() {
        return amount;
    }

    public void setAmount(Double amount) {
        this.amount = amount;
    }

    public String getMerchant() {
        return merchant;
    }

    public void setMerchant(String merchant) {
        this.merchant = merchant;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getTransactionType() {
        return transactionType;
    }

    public void setTransactionType(String transactionType) {
        this.transactionType = transactionType;
    }

    public String getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(String deviceId) {
        this.deviceId = deviceId;
    }

    public String getPreferredDevice() {
        return preferredDevice;
    }

    public void setPreferredDevice(String preferredDevice) {
        this.preferredDevice = preferredDevice;
    }

    public String getPersona() {
        return persona;
    }

    public void setPersona(String persona) {
        this.persona = persona;
    }

    public Integer getHour() {
        return hour;
    }

    public void setHour(Integer hour) {
        this.hour = hour;
    }
}