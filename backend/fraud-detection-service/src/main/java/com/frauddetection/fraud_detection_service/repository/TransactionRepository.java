package com.frauddetection.fraud_detection_service.repository;

import com.frauddetection.fraud_detection_service.model.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {
}