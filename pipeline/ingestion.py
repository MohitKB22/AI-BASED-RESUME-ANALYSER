"""pipeline/ingestion.py – PDF ingestion pipeline (stub)."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class IngestResult:
    success: bool
    doc_id: str = ""
    filename: str = ""
    pages_parsed: int = 0
    chunks_indexed: int = 0
    latency_ms: int = 0
    error: Optional[str] = None


def ingest_pdf(
    file_path: Path,
    doc_id: str,
    save_original: bool = False,
) -> IngestResult:
    """Stub: replace with real PDF parsing + chunking + indexing logic."""
    return IngestResult(
        success=False,
        doc_id=doc_id,
        filename=file_path.name,
        error="Ingestion pipeline not yet implemented.",
    )
