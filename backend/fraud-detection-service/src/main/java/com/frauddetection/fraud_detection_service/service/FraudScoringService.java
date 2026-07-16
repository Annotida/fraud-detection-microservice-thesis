package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.model.Transaction;
import org.springframework.stereotype.Service;

@Service
public class FraudScoringService {

    public double calculateRiskScore(Transaction transaction) {

        double score = 0.0;

        // -------------------------
        // Amount Risk
        // -------------------------

        if (transaction.getAmount() >= 1000) {
            score += 0.20;
        }

        if (transaction.getAmount() >= 5000) {
            score += 0.20;
        }

        if (transaction.getAmount() >= 10000) {
            score += 0.20;
        }

        // -------------------------
        // Merchant Risk
        // -------------------------

        String merchant = transaction.getMerchant();

        if ("Luxury Store".equalsIgnoreCase(merchant)) {
            score += 0.15;
        }

        if ("Crypto Exchange".equalsIgnoreCase(merchant)) {
            score += 0.20;
        }

        if ("Dark Web Market".equalsIgnoreCase(merchant)) {
            score += 0.30;
        }

        if ("Unknown Merchant".equalsIgnoreCase(merchant)) {
            score += 0.15;
        }

        // -------------------------
        // Location Risk
        // -------------------------

        String location = transaction.getLocation();

        if ("Dubai".equalsIgnoreCase(location)) {
            score += 0.10;
        }

        if ("Russia".equalsIgnoreCase(location)) {
            score += 0.20;
        }

        if ("Nigeria".equalsIgnoreCase(location)) {
            score += 0.15;
        }

        if ("North Korea".equalsIgnoreCase(location)) {
            score += 0.30;
        }

        // -------------------------
        // Transaction Type Risk
        // -------------------------

        String type = transaction.getTransactionType();

        if ("CRYPTO".equalsIgnoreCase(type)) {
            score += 0.20;
        }

        if ("WIRE_TRANSFER".equalsIgnoreCase(type)) {
            score += 0.15;
        }

        // -------------------------
        // Device Risk
        // -------------------------

        String device = transaction.getDeviceId();

        if (!"DEVICE001".equalsIgnoreCase(device)
                && !"DEVICE002".equalsIgnoreCase(device)
                && !"DEVICE003".equalsIgnoreCase(device)) {

            score += 0.15;
        }

        return Math.min(score, 1.0);
    }
}