from __future__ import annotations

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path


# Load .env so GROQ_API_KEY is available
load_dotenv()

from agent import Agent  # your existing Agent class

app = FastAPI(
    title="Agentic Finance Research Agent",
    version="1.0.0",
    description="Tool-using financial research agent (Groq + yfinance). Local deployment.",
)

BASE_DIR = Path(__file__).resolve().parent

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE_DIR / "index.html").read_text(encoding="utf-8")


# Create one agent instance at startup (reuse across requests)
agent = Agent(model="llama-3.1-8b-instant", max_steps=6)


class AnalyzeRequest(BaseModel):
    prompt: str = Field(..., min_length=3, examples=["Analyze Tesla and give me a quick snapshot."])


class AnalyzeResponse(BaseModel):
    output: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    # Basic guardrail: ensure API key exists
    if not os.getenv("GROQ_API_KEY"):
        raise HTTPException(status_code=500, detail="GROQ_API_KEY not set. Check your .env file.")

    try:
        out = agent.run(req.prompt)
        return {"output": out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent failed: {type(e).__name__}: {e}")
