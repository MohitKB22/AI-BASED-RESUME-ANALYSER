"""pipeline/query_rewriter.py – Query rewriting (stub)."""
from __future__ import annotations
from enum import Enum


class RewriteMode(str, Enum):
    SIMPLE = "simple"
    HyDE = "hyde"


def rewrite_query(
    query: str,
    mode: RewriteMode = RewriteMode.SIMPLE,
    conversation_context: str = "",
) -> str:
    """Stub: returns the original query unchanged."""
    return query
