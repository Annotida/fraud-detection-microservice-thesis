package com.frauddetection.fraud_detection_service.controller;

import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.service.TransactionService;
import org.springframework.web.bind.annotation.*;

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
}