##  Financial AI Agent

An end-to-end AI-powered financial assistant built with Python and FastAPI.
The agent can fetch financial market data, process user queries, and generate structured responses using LLM-based reasoning.

---

## Features

* AI-powered financial query handling
* Real-time stock data retrieval (via `yfinance`)
* Modular agent architecture
* FastAPI backend for API exposure
* Dockerized for container deployment
* Environment-based configuration
* Local deployment support (no cloud required)

---

##  Project Structure

```
financial-agent/
│
├── tools.py          # Financial data tools (market data, utilities)
├── agent.py          # Agent logic and reasoning layer
├── app.py            # FastAPI API layer
├── run.py            # Application entry point
├── requirements.txt  # Dependencies
├── Dockerfile        # Container configuration
├── .dockerignore
└── .env              # Environment variables (not committed)
```

---

##  Installation (Local)

### 1️ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/financial-agent.git
cd financial-agent
```

### 2️ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️ Configure environment

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶ Run the Application

```bash
uvicorn app:app --reload
```

Then open:

```
http://127.0.0.1:8000
```

---

##  Run with Docker

```bash
docker build -t financial-agent .
docker run -p 8000:8000 financial-agent
```

---

##  Architecture Overview

User → FastAPI → Agent → Tools → External APIs → Response

* The **Agent** handles reasoning and orchestration.
* **Tools** fetch structured financial data.
* The system separates heavy processing from API handling for better scalability.

---

##  Use Case

This project demonstrates:

* Agent-based AI architecture
* Tool integration
* Financial data processing
* Production-ready API structuring
* Containerized deployment

Built as a portfolio project to showcase AI engineering and agent design capabilities.



