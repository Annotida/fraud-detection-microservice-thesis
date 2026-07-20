package com.frauddetection.fraud_detection_service.controller;

import com.frauddetection.fraud_detection_service.dto.TransactionStatistics;
import com.frauddetection.fraud_detection_service.model.Transaction;
import com.frauddetection.fraud_detection_service.service.TransactionService;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;

import org.springframework.web.bind.annotation.*;

import java.util.List;

@Tag(
    name = "Fraud Detection API",
    description = "REST API for submitting, retrieving, and analysing banking transactions using the AI-driven fraud detection service."
)
@RestController
@RequestMapping("/api/transactions")
public class TransactionController {

    private final TransactionService service;

    public TransactionController(TransactionService service) {
        this.service = service;
    }

    @Operation(
        summary = "Submit a transaction",
        description = "Processes a banking transaction through the fraud detection engine, stores it in the database, and returns the prediction."
    )
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Transaction processed successfully"),
        @ApiResponse(responseCode = "400", description = "Invalid transaction data"),
        @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @PostMapping
    public Transaction createTransaction(@RequestBody Transaction transaction) {
        return service.saveTransaction(transaction);
    }

    @Operation(
        summary = "Retrieve all transactions",
        description = "Returns every transaction stored in the fraud detection database."
    )
    @ApiResponse(responseCode = "200", description = "Transactions retrieved successfully")
    @GetMapping
    public List<Transaction> getAllTransactions() {
        return service.getAllTransactions();
    }

    @Operation(
        summary = "Retrieve transaction statistics",
        description = "Returns aggregated statistics including transaction counts and fraud decisions."
    )
    @ApiResponse(responseCode = "200", description = "Statistics retrieved successfully")
    @GetMapping("/stats")
    public TransactionStatistics getTransactionStatistics() {
        return service.getTransactionStatistics();
    }

    @Operation(
        summary = "Retrieve transactions by decision",
        description = "Returns transactions filtered by their decision outcome (APPROVE, REVIEW or REJECT)."
    )
    @ApiResponse(responseCode = "200", description = "Transactions retrieved successfully")
    @GetMapping("/decision/{decision}")
    public List<Transaction> getTransactionsByDecision(@PathVariable String decision) {
        return service.getTransactionsByDecision(decision);
    }

    @Operation(
        summary = "Retrieve a transaction by ID",
        description = "Returns a single transaction using its unique identifier."
    )
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "Transaction found"),
        @ApiResponse(responseCode = "404", description = "Transaction not found")
    })
    @GetMapping("/{id}")
    public Transaction getTransaction(@PathVariable Long id) {
        return service.getTransactionById(id);
    }
}