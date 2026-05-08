"""
config.py – Application settings via pydantic-settings.
Load values from .env file automatically.
"""
from __future__ import annotations
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # LLM
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    # Retrieval
    top_k_retrieval: int = 10
    top_k_rerank: int = 5

    # Paths
    documents_dir: Path = Path("data/documents")
    faiss_index_dir: Path = Path("data/faiss_index")
    diskcache_dir: Path = Path("data/diskcache")

    # Redis (optional)
    redis_url: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
