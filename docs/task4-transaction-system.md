# Task 4: Transaction Processing System with Kafka and Spring Boot

## Overview
Built a high-performance transaction processing system using Spring Boot and Apache Kafka for JPMorgan Chase's Software Engineering job simulation.

## Key Implementations

### 1. Kafka Integration
- Configured Kafka consumer for high-volume transaction messages
- Implemented deserialization for custom transaction objects
- Used embedded Kafka for integration testing
- Managed message acknowledgment and error handling

### 2. Transaction Processing
- Validated incoming transactions against business rules
- Persisted transactions using Spring Data JPA
- Implemented atomic balance updates across user accounts
- Used H2 in-memory database for development

### 3. External API Integration
- Connected to external Incentive API using RestTemplate
- Processed incentive responses asynchronously
- Integrated incentives into transaction workflow
- Implemented fallback mechanisms for API failures

### 4. RESTful API
- Developed endpoint for balance queries
- Returned JSON responses with proper HTTP status codes
- Maintained clean architecture (Controller -> Service -> Repository)
- Added comprehensive error handling

## Technologies
- Java 17
- Spring Boot 3.1
- Apache Kafka
- Spring Data JPA
- H2 Database
- Maven
- JUnit 5

## How to Run
cd JPMC-tech-task-4-transaction-system
mvn clean install
mvn spring-boot:run

## API Endpoints
- GET /api/v1/users/{userId}/balance - Get user balance
