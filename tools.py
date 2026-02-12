from __future__ import annotations
import yfinance as yf


def get_stock_price(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    hist = t.history(period="5d")
    if hist is None or hist.empty:
        return {"ticker": ticker, "error": "No price data found."}

    close = float(hist["Close"].iloc[-1])
    date = str(hist.index[-1].date())
    return {"ticker": ticker, "close": close, "date": date}


def get_company_snapshot(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    info = getattr(t, "info", {}) or {}
    return {
        "ticker": ticker,
        "name": info.get("shortName") or info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "pe_trailing": info.get("trailingPE"),
        "pe_forward": info.get("forwardPE"),
        "beta": info.get("beta"),
        "currency": info.get("currency"),
    }
