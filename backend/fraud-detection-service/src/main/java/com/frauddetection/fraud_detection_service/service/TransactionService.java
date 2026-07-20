package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.repository.TransactionRepository;

import org.springframework.stereotype.Service;

import java.util.List;

import com.frauddetection.fraud_detection_service.dto.PredictionRequest;
import com.frauddetection.fraud_detection_service.dto.PredictionResponse;

import com.frauddetection.fraud_detection_service.dto.TransactionStatistics;

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
        request.setCountry(transaction.getCountry());
        request.setTransactionType(transaction.getTransactionType());
        request.setDeviceId(transaction.getDeviceId());
        request.setPreferredDevice(transaction.getPreferredDevice());
        request.setPersona(transaction.getPersona());
        request.setHour(transaction.getTimestamp().getHour());

        PredictionResponse response = mlPredictionService.predict(request);

        System.out.println("Prediction: " + response.getPrediction());
        System.out.println("Confidence: " + response.getConfidence());

        transaction.setMlPrediction(response.getPrediction());
        transaction.setMlConfidence(response.getConfidence());

        transaction.setRiskScore(riskScore);
        transaction.setDecision(decision);

        return repository.save(transaction);
    }

    public List<Transaction> getAllTransactions() {

        return repository.findAll();
    }

    public Transaction getTransactionById(Long id) {

    return repository.findById(id)
            .orElseThrow(() ->
                    new RuntimeException("Transaction not found"));
    }

    public List<Transaction> getTransactionsByDecision(String decision) {

        return repository.findByDecision(decision);
    }

        public TransactionStatistics getTransactionStatistics() {

        long total = repository.count();

        long approved = repository.countByDecision("APPROVE");

        long review = repository.countByDecision("REVIEW");

        long rejected = repository.countByDecision("REJECT");

        return new TransactionStatistics(
                total,
                approved,
                review,
                rejected
        );
    }
}