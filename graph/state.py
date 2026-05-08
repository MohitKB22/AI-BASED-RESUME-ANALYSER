"""graph/state.py – LangGraph shared state schema."""
from __future__ import annotations
from typing import Any, Optional
from typing_extensions import TypedDict
from langchain_core.documents import Document


class ResearchState(TypedDict, total=False):
    query: str
    rewritten_query: str
    doc_ids: Optional[list[str]]
    selected_agent: str
    retrieved_docs: list[Document]
    agent_response: str
    citations: list[str]
    conversation_history: list
    error: Optional[str]
    metadata: dict[str, Any]
