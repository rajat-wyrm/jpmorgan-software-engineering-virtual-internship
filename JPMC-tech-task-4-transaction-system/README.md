# Task 4: Transaction Processing System with Kafka and Spring Boot

## Overview
This is a Spring Boot microservice that processes financial transactions using Apache Kafka, JPA for persistence, and integrates with an external Incentive API.

## Architecture
- **Kafka Consumer**: Listens for transaction messages on 'transactions' topic
- **Transaction Service**: Processes transactions, validates amounts, updates balances
- **JPA Repositories**: User and Transaction entities with H2 database
- **REST Controller**: Provides balance query endpoints
- **External API Integration**: Calls Incentive API for bonus calculations

## Technologies
- Java 17
- Spring Boot 3.1
- Apache Kafka
- Spring Data JPA
- H2 Database
- Maven
- JUnit 5 & Mockito
- Docker

## Project Structure
src/main/java/com/jpmc/transaction/
├── config/           - Kafka and app configuration
├── controller/       - REST endpoints
├── service/          - Business logic
├── repository/       - Data access
├── model/            - JPA entities
└── dto/              - Data transfer objects

src/test/java/com/jpmc/transaction/
├── service/          - Unit tests
└── *Test.java        - Integration tests

## How to Run

### Using Maven
cd JPMC-tech-task-4-transaction-system
mvn clean install
mvn spring-boot:run

### Using Docker
cd JPMC-tech-task-4-transaction-system
docker-compose up --build

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/users/{userId}/balance | Get user's current balance |

### Example Request
curl http://localhost:8080/api/v1/users/1/balance

### Example Response
{
  "userId": 1,
  "balance": 1050.00,
  "timestamp": "2024-03-05T15:30:00Z"
}

## Kafka Topics

| Topic Name | Description |
|------------|-------------|
| transactions | Incoming transaction messages |

### Sample Transaction Message
{
  "transactionId": "tx-123456",
  "userId": 1,
  "amount": 100.00,
  "type": "DEPOSIT"
}

## Testing

Run tests with Maven:
mvn test

Test coverage includes:
- Unit tests for service layer
- Integration tests with embedded Kafka
- REST endpoint tests
- Database repository tests

## Configuration

Key properties in application.properties:

spring.kafka.bootstrap-servers=localhost:9092
spring.kafka.consumer.group-id=transaction-group
spring.datasource.url=jdbc:h2:mem:transactiondb
spring.jpa.hibernate.ddl-auto=create-drop
incentive.api.url=http://localhost:8081/v1/calculate

## Features Implemented

✅ Kafka integration for high-volume message processing
✅ Transaction validation and persistence
✅ User balance management with JPA
✅ External Incentive API integration
✅ REST endpoints for balance queries
✅ Comprehensive test suite
✅ Docker containerization
✅ Embedded Kafka for integration testing

## Key Learnings
- Enterprise microservices architecture with Spring Boot
- Real-time message processing with Kafka
- Transaction management in distributed systems
- External API integration patterns
- Test-driven development with embedded Kafka
- Containerization with Docker
