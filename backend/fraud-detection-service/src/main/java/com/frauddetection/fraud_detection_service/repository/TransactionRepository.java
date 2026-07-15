package com.frauddetection.fraud_detection_service.repository;

import com.frauddetection.fraud_detection_service.model.Transaction;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {

    List<Transaction> findByDecision(String decision);

    long countByDecision(String decision);

    long count();

}