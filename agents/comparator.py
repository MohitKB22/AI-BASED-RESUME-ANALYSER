"""agents/comparator.py – Comparator agent (stub)."""
from __future__ import annotations
from graph.state import ResearchState


def run_comparator_agent(state: ResearchState) -> ResearchState:
    return {**state, "agent_response": "Comparator agent not yet implemented.", "citations": []}
