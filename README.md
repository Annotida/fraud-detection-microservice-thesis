# AI-Driven Real-Time Fraud Detection Microservice

![Java](https://img.shields.io/badge/Java-21-orange)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.x-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Postman](https://img.shields.io/badge/Postman-API_Testing-FF6C37)
![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-85EA2D)
![JMeter](https://img.shields.io/badge/Apache_JMeter-Performance_Testing-D22128)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Design and Development of an AI-Driven Real-Time Fraud Detection Microservice Using Java Spring Boot and Machine Learning for Banking Transactions

This project presents the design and implementation of an AI-driven fraud detection microservice capable of analysing banking transactions in real time using a machine learning model,
deployed alongside a Java Spring Boot REST API. 
The system demonstrates how cloud-native microservices and machine learning can be combined to improve fraud detection while maintaining low response times and high prediction accuracy.

**Student**

Anotida Mangwanda

**Institution**

Open Institute of Technology (OPIT), Malta

**Programme**

BSc (Hons) Modern Computer Science

**Supervisor**

Dr Jovan Pehcevski

**Year**

2026

### Features:

- Fraud Detection REST API
- Machine Learning Prediction
- Random Forest Model
- PostgreSQL Database
- Docker Deployment
- Swagger Documentation
- Apache JMeter Performance Testing
- Statistics Endpoint

### System Architecture:

The solution follows a microservice-based architecture where the Java Spring Boot backend receives incoming banking transactions through a REST API. Transactions are forwarded to a Python FastAPI machine learning service, which returns a fraud prediction. Based on the prediction score, the backend applies business decision thresholds to approve, review, or reject the transaction before storing the result in PostgreSQL. Docker Compose orchestrates all services, ensuring consistent deployment and communication between components.

<p align="center">
  <a href="evaluation/notes/system-architecture-diagram.jpg">
    <img src="evaluation/notes/system-architecture-diagram.jpg"
         alt="System Architecture"
         width="700">
  </a>
</p>

### Technology Stack:

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


### Folder Structure:

- backend/
- ml-service/
- postman/
- evaluation/
- README.md
- .gitignore
- LICENSE
- docker-compose.yml


### Installation:

- git clone https://github.com/Annotida/fraud-detection-microservice-thesis.git
- cd fraud-detection-microservice-thesis
- docker compose up --build


### API Endpoint:

/api/transactions

### Machine Learning Development

During the development of this project, two machine learning models were evaluated.

The initial prototype was trained using the publicly available Kaggle Credit Card Fraud Detection dataset. This dataset was selected because it is widely used in fraud detection research and provided a reliable benchmark for developing and validating the machine learning pipeline, REST API integration, and overall system architecture.

As the project progressed, the implementation was enhanced by replacing the initial dataset with a business-oriented synthetic banking transaction dataset. Unlike the Kaggle dataset, which primarily contains anonymised numerical features, the business-oriented dataset includes realistic banking attributes such as customer profiles, merchant information, transaction types, countries, currencies, timestamps, and transaction amounts.

This transition allowed the final fraud detection microservice to better represent real-world banking scenarios and produce predictions using transaction data that more closely resembles those processed by modern financial institutions.

### Performance Results:

The developed system was evaluated using a synthetic banking transaction dataset. Performance was assessed using standard machine learning classification metrics.
The results demonstrate that the system achieves high predictive performance while maintaining low latency suitable for real-time banking environments.

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 96.17% |
| Precision | 93.99% |
| Recall    | 90.75% |
| F1 Score  | 92.34% |
| AUC       | 99.28% |

### Future Improvements:

#### Future enhancements to the system include:

- Development of a responsive web dashboard
- Apache Kafka integration for event-driven processing
- Cloud deployment using AWS or Azure
- Continuous machine learning model retraining
- Support for deep learning fraud detection models
- Real-time monitoring and analytics dashboards

### Repository Information

This repository accompanies the undergraduate honours dissertation submitted to the Open Institute of Technology (OPIT), Malta.

It contains the complete implementation of the proposed fraud detection microservice, including the backend application, machine learning service, Docker configuration, database scripts, API collection, and evaluation resources.

The repository is intended for academic, research, and demonstration purposes.
