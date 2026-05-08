"""agents/qa_agent.py – QA agent (stub)."""
from __future__ import annotations
from graph.state import ResearchState


def run_qa_agent(state: ResearchState) -> ResearchState:
    return {**state, "agent_response": "QA agent not yet implemented.", "citations": []}
