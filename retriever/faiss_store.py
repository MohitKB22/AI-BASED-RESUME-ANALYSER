"""retriever/faiss_store.py – FAISS vector store (stub)."""
from __future__ import annotations
from typing import Optional
from langchain_core.documents import Document


class FaissStore:
    stored_doc_ids: list[str] = []

    def similarity_search(
        self,
        query: str,
        k: int = 10,
        filter_doc_ids: Optional[list[str]] = None,
    ) -> list[Document]:
        return []


_store: Optional[FaissStore] = None


def get_faiss_store() -> FaissStore:
    global _store
    if _store is None:
        _store = FaissStore()
    return _store
