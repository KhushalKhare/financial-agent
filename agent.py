from __future__ import annotations
import json
from typing import Any, Dict, List
from groq import Groq

from tools import get_stock_price, get_company_snapshot

TOOL_DEFS = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the latest close stock price for a ticker symbol (e.g., TSLA, AAPL).",
            "parameters": {
                "type": "object",
                "properties": {"ticker": {"type": "string"}},
                "required": ["ticker"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_company_snapshot",
            "description": "Get a basic company snapshot (sector, market cap, PE, etc.) for a ticker.",
            "parameters": {
                "type": "object",
                "properties": {"ticker": {"type": "string"}},
                "required": ["ticker"],
            },
        },
    },
]

TOOL_REGISTRY = {
    "get_stock_price": get_stock_price,
    "get_company_snapshot": get_company_snapshot,
}


class Agent:
    def __init__(self, model: str = "llama-3.1-8b-instant", max_steps: int = 6):
        self.client = Groq()  # uses GROQ_API_KEY env var by default
        self.model = model
        self.max_steps = max_steps

    def run(self, user_prompt: str) -> str:
        messages: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "You are a financial research agent.\n"
                    "Use tools when needed. If the user didn't provide a ticker, infer a likely ticker.\n"
                    "After tool use, produce a concise structured answer with bullets:\n"
                    "- Company\n"
                    "- Latest price\n"
                    "- Snapshot metrics\n"
                    "- Quick take\n"
                ),
            },
            {"role": "user", "content": user_prompt},
        ]

        for _ in range(self.max_steps):
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=TOOL_DEFS,
                tool_choice="auto",
            )

            msg = resp.choices[0].message

            if not getattr(msg, "tool_calls", None):
                return msg.content or ""

            messages.append(
                {
                    "role": "assistant",
                    "content": msg.content or "",
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": tc.type,
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments,
                            },
                        }
                        for tc in msg.tool_calls
                    ],
                }
            )

            for tc in msg.tool_calls:
                tool_name = tc.function.name
                tool_args = json.loads(tc.function.arguments or "{}")

                fn = TOOL_REGISTRY.get(tool_name)
                if fn is None:
                    tool_result = {"error": f"Unknown tool: {tool_name}"}
                else:
                    try:
                        tool_result = fn(**tool_args)
                    except Exception as e:
                        tool_result = {"error": f"{tool_name} failed: {type(e).__name__}: {e}"}

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps(tool_result),
                    }
                )

        return "Stopped: reached max steps without a final answer."
