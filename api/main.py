"""
api/main.py – FastAPI application entry point.
"""
from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="PaperMind",
    description="Multi-Agent RAG System for Research Papers",
    version="1.0.0",
)

app.include_router(router, prefix="/api/v1")
