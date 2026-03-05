# Task 4: Transaction Processing System

## Overview
Spring Boot microservice with Kafka integration for processing financial transactions.

## Structure
src/
├── main/
│   ├── java/com/jpmc/transaction/
│   │   ├── config/     - Kafka and app configuration
│   │   ├── controller/ - REST endpoints
│   │   ├── service/    - Business logic
│   │   ├── repository/ - Data access
│   │   ├── model/      - JPA entities
│   │   ├── dto/        - Data transfer objects
│   │   └── kafka/      - Kafka consumers
│   └── resources/
│       └── application.properties
└── test/               - Unit and integration tests

## Dependencies
- Spring Boot Web
- Spring Data JPA
- Spring Kafka
- H2 Database
- Lombok

## Run Instructions
mvn clean package
java -jar target/transaction-system-1.0.0.jar
