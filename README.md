# AI-Driven Real-Time Fraud Detection Microservice

## Design and Development of an AI-Driven Real-Time Fraud Detection Microservice Using Java Spring Boot and Machine Learning for Banking Transactions

This project presents the design and implementation of an AI-driven fraud detection microservice capable of analysing banking transactions in real time using a machine learning model,
deployed alongside a Java Spring Boot REST API. 
The system demonstrates how cloud-native microservices and machine learning can be combined to improve fraud detection while maintaining low response times and high prediction accuracy.

Features:

Fraud Detection REST API
Machine Learning Prediction
Random Forest Model
PostgreSQL Database
Docker Deployment
Swagger Documentation
Apache JMeter Performance Testing
Statistics Endpoint

System Architecture:



Technology Stack:

| Technology  | Purpose             |
| ----------- | ------------------- |
| Java 21     | Backend             |
| Spring Boot | REST API            |
| Python 3.12 | Machine Learning    |
| FastAPI     | ML Microservice     |
| PostgreSQL  | Database            |
| Docker      | Containerisation    |
| Swagger     | API Documentation   |
| JMeter      | Performance Testing |


Folder Structure:

backend/
ml-service/
database/
evaluation/
README.md
docker-compose.yml


Installation:

git clone https://github.com/Annotida/fraud-detection-microservice-thesis.git
cd fraud-detection-microservice-thesis
docker compose up --build


API Endpoint:

/api/transactions

Performance Results:

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 96.17% |
| Precision | 93.99% |
| Recall    | 90.75% |
| F1 Score  | 92.34% |
| AUC       | 99.28% |

Future Improvements:

Frontend Dashboard
Apache Kafka
Cloud Deployment
Continuous Model Training
Learning Models

Repository:

This repository accompanies the undergraduate honours dissertation submitted to Open Institute of Technology(OPIT) Malta.
The repository is provided for academic and research purposes.




