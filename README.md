# 🏦 JPMorgan Chase Software Engineering Virtual Internship

[![GitHub last commit](https://img.shields.io/github/last-commit/rajat-wyrm/jpmorgan-software-engineering-virtual-internship)](https://github.com/rajat-wyrm/jpmorgan-software-engineering-virtual-internship/commits/main)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rajat-wyrm/jpmorgan-software-engineering-virtual-internship)](https://github.com/rajat-wyrm/jpmorgan-software-engineering-virtual-internship/graphs/commit-activity)
[![GitHub repo size](https://img.shields.io/github/repo-size/rajat-wyrm/jpmorgan-software-engineering-virtual-internship)](https://github.com/rajat-wyrm/jpmorgan-software-engineering-virtual-internship)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

This repository contains my complete work for the **JPMorgan Chase Software Engineering Virtual Experience Program** on Forage.

### 🎯 Program Highlights

- **Tasks Completed**: 4
- **Technologies**: Python, TypeScript, Java, Spring Boot, Kafka, D3.js
- **Total Commits**: 170+
- **Status**: ✅ 100% Complete

---

## 📑 Table of Contents

- Task 1: Stock Price Data Feed
- Task 2: Perspective Integration
- Task 3: Trading Dashboard
- Task 4: Transaction Processing System
- Quick Start Guide
- Repository Structure
- Certificate
- License

---

## 🐍 Task 1: Stock Price Data Feed Interface

**Location:** JPMC-tech-task-1-PY3/

A real-time stock price data feed system with a multi-threaded server and client implementation.

### ✨ Features
- Real-time server broadcasting stock data every 2 seconds
- Stock symbols: JPM, GS, MS, BAC, C
- Data points: timestamp, symbol, price, volume, percentage change
- Client with CSV export functionality
- Multi-threaded client handling

### 🚀 Run Task 1
cd JPMC-tech-task-1-PY3
python server3.py
# In another terminal
python client3.py

[📘 Detailed Documentation](docs/task1-stock-data-feed.md)

---

## 📊 Task 2: Perspective Integration

**Location:** JPMC-tech-task-2-PY3/

Interactive data visualization using Perspective library with real-time WebSocket updates.

### ✨ Features
- TypeScript/Node.js server with Express and WebSocket
- HTML/CSS/JS frontend with Perspective integration
- Live stock data streaming via WebSocket
- Multiple visualization types (grid, chart, heatmap)
- Interactive data filtering

### 🚀 Run Task 2
cd JPMC-tech-task-2-PY3
npm install
npm start
Open browser to http://localhost:8080

[📘 Detailed Documentation](docs/task2-perspective-integration.md)

---

## 📈 Task 3: Trading Dashboard

**Location:** JPMC-tech-task-3-PY3/

Comprehensive trading dashboard with D3.js visualizations and real-time market data.

### ✨ Features
- Price charts with gradient fills
- Volume analysis with bar charts
- Real-time WebSocket updates
- Interactive symbol selection
- Market overview indicators
- Responsive design

### 🚀 Run Task 3
cd JPMC-tech-task-3-PY3
npm install
npm start
Open browser to http://localhost:8080

[📘 Detailed Documentation](docs/task3-data-visualization.md)

---

## ☕ Task 4: Transaction Processing System

**Location:** JPMC-tech-task-4-transaction-system/

Enterprise-grade transaction processing microservice with Kafka integration.

### ✨ Features
- Kafka integration for high-volume message consumption
- Transaction validation and persistence with JPA
- External Incentive API integration
- REST endpoints for balance queries
- Comprehensive test suite with embedded Kafka
- Docker containerization

### 🚀 Run Task 4
cd JPMC-tech-task-4-transaction-system

# Using Maven
./mvnw spring-boot:run

# Using Docker
docker-compose up --build

# Test the API
curl http://localhost:8080/api/v1/users/1/balance

[📘 Detailed Documentation](docs/task4-transaction-system.md)

---

## 🚀 Quick Start Guide

### Clone the Repository
git clone https://github.com/rajat-wyrm/jpmorgan-software-engineering-virtual-internship.git
cd jpmorgan-software-engineering-virtual-internship

### Run All Tasks
Task 1: cd JPMC-tech-task-1-PY3 && python server3.py
Task 2: cd JPMC-tech-task-2-PY3 && npm install && npm start
Task 3: cd JPMC-tech-task-3-PY3 && npm install && npm start
Task 4: cd JPMC-tech-task-4-transaction-system && ./mvnw spring-boot:run

---

## 📁 Repository Structure

jpmorgan-software-engineering-virtual-internship/
├── JPMC-tech-task-1-PY3/                 # Python stock data feed
├── JPMC-tech-task-2-PY3/                 # TypeScript Perspective integration
├── JPMC-tech-task-3-PY3/                 # TypeScript + D3.js dashboard
├── JPMC-tech-task-4-transaction-system/  # Java Spring Boot + Kafka
├── docs/                                 # Detailed documentation
├── certificate/                          # Completion certificate
├── .github/                              # GitHub templates
├── LICENSE                               # MIT License
└── README.md                             # This file

---

## 📊 Repository Statistics

- Total Commits: 170+
- Total Files: 100+
- Python Files: 11
- TypeScript Files: 4
- Java Files: 15+
- Documentation Files: 8
- Tasks Completed: 4/4

---

## 🏆 Certificate

My official completion certificate is available in the [/certificate](./certificate/) directory.

The certificate verifies completion of:
- ✅ Task 1: Stock Price Data Feed Interface
- ✅ Task 2: Perspective Integration
- ✅ Task 3: Trading Dashboard Development
- ✅ Task 4: Transaction Processing System with Kafka

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

Copyright (c) 2024 Rajat Kumar (rajat-wyrm)

---

## 🙏 Acknowledgments

- JPMorgan Chase & Co. for the virtual internship opportunity
- Forage platform for hosting the program
- Open source community for tools and libraries

---

## 📬 Connect with Me

GitHub: [@rajat-wyrm](https://github.com/rajat-wyrm)

---

**⭐ If you find this repository helpful, please consider giving it a star!**

*Last Updated: March 2024*
