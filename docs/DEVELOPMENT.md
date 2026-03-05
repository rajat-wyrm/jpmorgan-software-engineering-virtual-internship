# Development Guide

## Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- Git
- Docker (optional)

## Local Setup

### Task 1 (Python)
cd JPMC-tech-task-1-PY3
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r ../requirements.txt
python server3.py

### Task 2 (TypeScript)
cd JPMC-tech-task-2-PY3
npm install
npm run dev

### Task 3 (TypeScript)
cd JPMC-tech-task-3-PY3
npm install
npm run dev

## Docker Setup
# Build and run all services
docker-compose up --build

# Run specific service
docker-compose up task1-server
docker-compose up task2-server
docker-compose up task3-dashboard

## Testing
# Python tests
cd JPMC-tech-task-1-PY3
python client_test.py

# Node.js tests (when implemented)
cd JPMC-tech-task-2-PY3
npm test

## Common Issues

### Port already in use
Change the port in the respective config files:
- Task 1: Change port in server3.py
- Task 2/3: Change PORT in src/index.ts or src/dashboard.ts

### WebSocket connection refused
Ensure the server is running before starting the client.
