package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.repository.TransactionRepository;
import org.springframework.stereotype.Service;

import com.frauddetection.fraud_detection_service.dto.PredictionRequest;
import com.frauddetection.fraud_detection_service.dto.PredictionResponse;

@Service
public class TransactionService {

    private final TransactionRepository repository;
    private final FraudScoringService fraudScoringService;
    private final DecisionService decisionService;
    private final MLPredictionService mlPredictionService;

    public TransactionService(
            TransactionRepository repository,
            FraudScoringService fraudScoringService,
            DecisionService decisionService,
            MLPredictionService mlPredictionService) {

        this.repository = repository;
        this.fraudScoringService = fraudScoringService;
        this.decisionService = decisionService;
        this.mlPredictionService = mlPredictionService;
    }

    public Transaction saveTransaction(Transaction transaction) {

        double riskScore = fraudScoringService.calculateRiskScore(transaction);

        String decision = decisionService.evaluateDecision(riskScore);

        PredictionRequest request = new PredictionRequest();

        request.setAmount(transaction.getAmount());
        request.setMerchant(transaction.getMerchant());
        request.setLocation(transaction.getLocation());
        request.setTransactionType(transaction.getTransactionType());
        request.setDeviceId(transaction.getDeviceId());

        PredictionResponse response = mlPredictionService.predict(request);

        transaction.setMlPrediction(response.getPrediction());
        transaction.setMlConfidence(response.getConfidence());

        transaction.setRiskScore(riskScore);
        transaction.setDecision(decision);

        return repository.save(transaction);
    }
}