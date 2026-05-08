"""api/schemas.py – Pydantic request/response models."""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class AskRequest(BaseModel):
    query: str
    doc_ids: Optional[list[str]] = None
    conversation_history: Optional[list[dict]] = None


class AskResponse(BaseModel):
    query: str
    rewritten_query: str
    agent: str
    response: str
    citations: list[str] = []
    latency_ms: int = 0
    cached: bool = False


class SummarizeRequest(BaseModel):
    doc_id: str
    style: str = "bullet"


class SummarizeResponse(BaseModel):
    doc_id: str
    summary: str
    citations: list[str] = []
    latency_ms: int = 0


class CompareRequest(BaseModel):
    doc_ids: list[str]
    focus: Optional[str] = None


class CompareResponse(BaseModel):
    doc_ids: list[str]
    comparison: str
    citations: list[str] = []
    latency_ms: int = 0


class IngestResponse(BaseModel):
    doc_id: str
    filename: str
    pages_parsed: int
    chunks_indexed: int
    latency_ms: int
    success: bool
    error: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    indexed_docs: list[str] = []
    bm25_corpus_size: int = 0
