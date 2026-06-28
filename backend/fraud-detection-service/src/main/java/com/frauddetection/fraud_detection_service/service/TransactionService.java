package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.repository.TransactionRepository;
import org.springframework.stereotype.Service;

@Service
public class TransactionService {

    private final TransactionRepository repository;
    private final FraudScoringService fraudScoringService;
    private final DecisionService decisionService;

    public TransactionService(
            TransactionRepository repository,
            FraudScoringService fraudScoringService,
            DecisionService decisionService) {

        this.repository = repository;
        this.fraudScoringService = fraudScoringService;
        this.decisionService = decisionService;
    }

    public Transaction saveTransaction(Transaction transaction) {

        double riskScore =
                fraudScoringService.calculateRiskScore(transaction);

        String decision =
                decisionService.evaluateDecision(riskScore);

        transaction.setRiskScore(riskScore);
        transaction.setDecision(decision);

        return repository.save(transaction);
    }
}