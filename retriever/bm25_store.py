"""retriever/bm25_store.py – BM25 sparse store (stub)."""
from __future__ import annotations
from typing import Optional
from langchain_core.documents import Document


class BM25Store:
    corpus_size: int = 0

    def search(
        self,
        query: str,
        k: int = 10,
        filter_doc_ids: Optional[list[str]] = None,
    ) -> list[Document]:
        return []


_store: Optional[BM25Store] = None


def get_bm25_store() -> BM25Store:
    global _store
    if _store is None:
        _store = BM25Store()
    return _store
