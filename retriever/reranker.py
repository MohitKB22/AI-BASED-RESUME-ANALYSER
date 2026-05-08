"""retriever/reranker.py – Cross-encoder reranker (stub)."""
from __future__ import annotations
from langchain_core.documents import Document


def rerank(query: str, documents: list[Document], top_k: int = 5) -> list[Document]:
    """Stub: returns documents unchanged."""
    return documents[:top_k]
