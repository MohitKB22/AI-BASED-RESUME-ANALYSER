"""agents/summarizer.py – Summarizer agent (stub)."""
from __future__ import annotations
from graph.state import ResearchState


def run_summarizer_agent(state: ResearchState) -> ResearchState:
    return {**state, "agent_response": "Summarizer agent not yet implemented.", "citations": []}
