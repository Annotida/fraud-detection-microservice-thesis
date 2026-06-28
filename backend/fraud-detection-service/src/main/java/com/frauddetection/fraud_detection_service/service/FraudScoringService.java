package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.model.Transaction;
import org.springframework.stereotype.Service;

@Service
public class FraudScoringService {

    public double calculateRiskScore(Transaction transaction) {

        double score = 0.1;

        if (transaction.getAmount() > 1000) {
            score += 0.3;
        }

        if (transaction.getAmount() > 5000) {
            score += 0.3;
        }

        if ("Dubai".equalsIgnoreCase(transaction.getLocation())) {
            score += 0.2;
        }

        if ("Luxury Store".equalsIgnoreCase(transaction.getMerchant())) {
            score += 0.2;
        }

        return Math.min(score, 1.0);
    }
}