package com.frauddetection.fraud_detection_service.controller;

import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.service.TransactionService;

import org.springframework.web.bind.annotation.*;

import java.util.List;

import com.frauddetection.fraud_detection_service.dto.TransactionStatistics;

@RestController
@RequestMapping("/api/transactions")
public class TransactionController {

    private final TransactionService service;

    public TransactionController(TransactionService service) {
        this.service = service;
    }

    @PostMapping
    public Transaction createTransaction(@RequestBody Transaction transaction) {
        return service.saveTransaction(transaction);
    }

    @GetMapping
    public List<Transaction> getAllTransactions() {
        return service.getAllTransactions();
    }

    @GetMapping("/stats")
    public TransactionStatistics getTransactionStatistics() {

        return service.getTransactionStatistics();
    }

    @GetMapping("/decision/{decision}")
    public List<Transaction> getTransactionsByDecision(
            @PathVariable String decision) {

        return service.getTransactionsByDecision(decision);
    }

    @GetMapping("/{id}")
    public Transaction getTransaction(@PathVariable Long id) {
        return service.getTransactionById(id);
    }
}