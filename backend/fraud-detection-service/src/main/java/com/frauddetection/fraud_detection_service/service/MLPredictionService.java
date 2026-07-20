package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.dto.PredictionRequest;
import com.frauddetection.fraud_detection_service.dto.PredictionResponse;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class MLPredictionService {

    // ==========================================================
    // KAGGLE MODEL (ARCHIVED)
    // ==========================================================
    //
    // Previous implementation communicated with the FastAPI
    // service using the Kaggle feature set.
    // Retained for dissertation comparison.
    //
    // private static final String ML_API =
    //         "http://fraud-ml:8000/predict";
    //
    // ==========================================================
    // BUSINESS MODEL (ACTIVE)
    // ==========================================================

    private static final String ML_API =
            "http://fraud-ml:8000/predict";

    private final RestTemplate restTemplate = new RestTemplate();

    public PredictionResponse predict(PredictionRequest request) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<PredictionRequest> entity =
                new HttpEntity<>(request, headers);

        ResponseEntity<PredictionResponse> response =
                restTemplate.postForEntity(
                        ML_API,
                        entity,
                        PredictionResponse.class
                );

        return response.getBody();
    }
}