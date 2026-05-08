"""cache/redis_cache.py – Redis/diskcache caching layer (stub)."""
from __future__ import annotations
from typing import Optional


def cache_get(query: str, doc_ids: Optional[list[str]] = None) -> Optional[dict]:
    return None


def cache_set(query: str, value: dict, doc_ids: Optional[list[str]] = None) -> None:
    pass
