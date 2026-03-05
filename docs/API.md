# API Documentation

## Task 1 - Stock Data Feed (Python Socket Server)
- **Host**: localhost:9999
- **Protocol**: TCP Socket
- **Data Format**: CSV
- **Message Types**:
  - SUBSCRIBE:symbol - Subscribe to specific stock
  - quit - Disconnect

## Task 2 - Perspective Integration (REST + WebSocket)
- **Base URL**: http://localhost:8080
- **WebSocket**: ws://localhost:8080

### REST Endpoints
- GET /api/historical/:symbol - Get historical data

### WebSocket Messages
- Client to Server:
  { "type": "subscribe", "symbols": ["JPM", "GS"] }

- Server to Client:
  { "type": "data", "data": [...] }

## Task 3 - Trading Dashboard
- **Base URL**: http://localhost:8080
- **WebSocket**: ws://localhost:8080

### Data Format
{
  "timestamp": "2024-03-05T10:00:00Z",
  "symbol": "JPM",
  "price": 145.67,
  "volume": 5432,
  "change": 1.23
}
