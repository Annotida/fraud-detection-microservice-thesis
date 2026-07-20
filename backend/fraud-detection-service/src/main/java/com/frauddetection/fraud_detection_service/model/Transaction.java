package com.frauddetection.fraud_detection_service.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // ==========================================================
    // CORE TRANSACTION INFORMATION
    // ==========================================================

    private Double amount;

    private String merchant;

    /**
     * Country where the transaction originated.
     * Used by the Business Random Forest model.
     */
    private String country;
    private String location;

    private LocalDateTime timestamp;

    private String status;

    /**
     * ONLINE, POS, ATM, MOBILE_PAYMENT, etc.
     */
    private String transactionType;

    /**
     * Device used for the current transaction.
     */
    private String deviceId;

    /**
     * Customer's usual/preferred device.
     */
    private String preferredDevice;

    /**
     * Customer persona used by the Business ML model.
     * Examples:
     * Student
     * Professional
     * Business Owner
     * Traveller
     * High Risk
     */
    private String persona;

    // ==========================================================
    // RULE ENGINE OUTPUT
    // ==========================================================

    private Double riskScore;

    private String decision;

    // ==========================================================
    // AI MODEL OUTPUT
    // ==========================================================

    private String mlPrediction;

    private Double mlConfidence;

    public Transaction() {
        this.timestamp = LocalDateTime.now();
        this.status = "RECEIVED";
    }

    public Long getId() {
        return id;
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

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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

    public Double getRiskScore() {
        return riskScore;
    }

    public void setRiskScore(Double riskScore) {
        this.riskScore = riskScore;
    }

    public String getDecision() {
        return decision;
    }

    public void setDecision(String decision) {
        this.decision = decision;
    }

    public String getMlPrediction() {
        return mlPrediction;
    }

    public void setMlPrediction(String mlPrediction) {
        this.mlPrediction = mlPrediction;
    }

    public Double getMlConfidence() {
        return mlConfidence;
    }

    public void setMlConfidence(Double mlConfidence) {
        this.mlConfidence = mlConfidence;
    }

    public String getLocation() {
     return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
}

/*package com.frauddetection.fraud_detection_service.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Double amount;
    private String merchant;
    private String location;
    private LocalDateTime timestamp;
    private String status;
    private String transactionType; //will come from ML model
    private String deviceId; //supports fraud patterns
    private Double riskScore; //classification feature
    private String decision;

    private String mlPrediction;
    private Double mlConfidence;

    public Transaction() {
        this.timestamp = LocalDateTime.now();
        this.status = "RECEIVED";
    }

    public Long getId() {
        return id;
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

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getDecision() {
        return decision;
    }

    public void setDecision(String decision) {
        this.decision = decision;
    }      
    
    public Double getRiskScore() {
        return riskScore;
    }

    public void setRiskScore(Double riskScore) {
        this.riskScore = riskScore;
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

    public String getMlPrediction() {
        return mlPrediction;
    }

    public void setMlPrediction(String mlPrediction) {
        this.mlPrediction = mlPrediction;
    }

    public Double getMlConfidence() {
        return mlConfidence;
    }

    public void setMlConfidence(Double mlConfidence) {
        this.mlConfidence = mlConfidence;
    }    
    }
*/