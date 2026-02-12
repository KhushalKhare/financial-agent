# Financial AI Agent

A modular AI-powered financial assistant built with Python and FastAPI.

This project demonstrates how agent-based architectures can integrate large language models with structured financial data tools in a clean, production-oriented design.

---

## Overview

The system separates reasoning logic from data retrieval tools and API exposure.
It is fully deployable locally and containerized using Docker.

Architecture flow:

User → FastAPI → Agent → Financial Tools → External APIs → Response

---

## Features

* Agent-based orchestration layer
* Real-time stock market data via `yfinance`
* FastAPI backend for structured API access
* Modular tool abstraction
* Environment-based configuration
* Dockerized deployment
* Local-first setup (no cloud dependency required)

---

## Project Structure

```
financial-agent/
│
├── tools.py          # Financial data retrieval and utilities
├── agent.py          # Agent reasoning and orchestration
├── app.py            # FastAPI application layer
├── run.py            # Entry point
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── .env              # Local environment variables (excluded from Git)
```

---

## Installation (Local)

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/financial-agent.git
cd financial-agent
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Access:

```
http://127.0.0.1:8000
```

---

## Docker Deployment

Build:

```bash
docker build -t financial-agent .
```

Run:

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key financial-agent
```

---

## Design Principles

* Clear separation of concerns (API / Agent / Tools)
* Extensible tool architecture
* Environment-driven configuration
* Reproducible container builds
* Structured system thinking over quick scripting

---

## Purpose

This project was built to explore practical AI agent architecture in a financial use case, focusing on maintainability, extensibility, and production-style structure rather than prompt experimentation alone.

