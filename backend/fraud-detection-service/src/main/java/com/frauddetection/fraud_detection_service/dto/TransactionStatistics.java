package com.frauddetection.fraud_detection_service.dto;

public class TransactionStatistics {

    private long totalTransactions;
    private long approved;
    private long review;
    private long rejected;

    public TransactionStatistics() {
    }

    public TransactionStatistics(
            long totalTransactions,
            long approved,
            long review,
            long rejected) {

        this.totalTransactions = totalTransactions;
        this.approved = approved;
        this.review = review;
        this.rejected = rejected;
    }

    public long getTotalTransactions() {
        return totalTransactions;
    }

    public void setTotalTransactions(long totalTransactions) {
        this.totalTransactions = totalTransactions;
    }

    public long getApproved() {
        return approved;
    }

    public void setApproved(long approved) {
        this.approved = approved;
    }

    public long getReview() {
        return review;
    }

    public void setReview(long review) {
        this.review = review;
    }

    public long getRejected() {
        return rejected;
    }

    public void setRejected(long rejected) {
        this.rejected = rejected;
    }
}