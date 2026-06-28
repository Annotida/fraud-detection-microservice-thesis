package com.frauddetection.fraud_detection_service.service;

import org.springframework.stereotype.Service;

@Service
public class DecisionService {

    public String evaluateDecision(double riskScore) {

        if (riskScore < 0.3) {
            return "APPROVE";
        }

        if (riskScore <= 0.7) {
            return "REVIEW";
        }

        return "REJECT";
    }
}