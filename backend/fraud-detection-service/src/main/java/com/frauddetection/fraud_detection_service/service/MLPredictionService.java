package com.frauddetection.fraud_detection_service.service;

import com.frauddetection.fraud_detection_service.dto.PredictionRequest;
import com.frauddetection.fraud_detection_service.dto.PredictionResponse;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.server.ResponseStatusException;

@Service
public class MLPredictionService {

        private static final String ML_API = "http://fraud-ml:8000/predict";

        private final RestTemplate restTemplate = new RestTemplate();

        public PredictionResponse predict(PredictionRequest request) {

                HttpHeaders headers = new HttpHeaders();
                headers.setContentType(MediaType.APPLICATION_JSON);

                HttpEntity<PredictionRequest> entity =
                        new HttpEntity<>(request, headers);

                try {

                        ResponseEntity<PredictionResponse> response =
                                restTemplate.postForEntity(
                                        ML_API,
                                        entity,
                                        PredictionResponse.class
                                );

                        return response.getBody();

                } catch (HttpClientErrorException ex) {

                        throw new ResponseStatusException(
                                ex.getStatusCode(),
                                ex.getResponseBodyAsString()
                        );
                }

                catch (Exception ex) {
                        
                        throw new ResponseStatusException(
                                HttpStatus.INTERNAL_SERVER_ERROR,
                                "Unable to contact the ML prediction service."
                );
                }
        }
}