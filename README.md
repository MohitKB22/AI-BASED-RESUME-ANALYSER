# PaperMind – Multi-Agent RAG System

## Quick Start

### 1. Create your `.env` file
```bash
cp .env.example .env
# Edit .env and set your OPENAI_API_KEY
```

### 2. Create required directories
```bash
mkdir -p data/faiss_index data/documents data/diskcache
```

### 3. Install dependencies
> ⚠️ Python 3.11 or 3.12 recommended. Python 3.14 may lack wheels for faiss-cpu / torch.
```bash
python3.11 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Start the API
```bash
python -m uvicorn api.main:app --reload --port 8000
```

### 5. Start the Streamlit UI (separate terminal)
```bash
streamlit run app.py
```

## Project Structure
```
papermind/
├── api/                  # FastAPI app
│   ├── main.py           # Entry point → uvicorn api.main:app
│   ├── routes.py         # Endpoint definitions
│   └── schemas.py        # Pydantic models
├── agents/               # LangGraph agents
│   ├── router.py         # Query classifier
│   ├── qa_agent.py       # QA agent
│   ├── summarizer.py     # Summarizer agent
│   └── comparator.py     # Comparator agent
├── graph/
│   ├── orchestrator.py   # LangGraph pipeline
│   └── state.py          # Shared state schema
├── retriever/
│   ├── hybrid_retriever.py  # FAISS + BM25 + RRF + Rerank
│   ├── faiss_store.py
│   ├── bm25_store.py
│   └── reranker.py
├── pipeline/
│   ├── ingestion.py      # PDF → chunks → index
│   └── query_rewriter.py
├── cache/
│   └── redis_cache.py
├── prompts/
│   └── agent_prompts.py
├── utils/
│   └── logger.py
├── config.py             # Settings (reads .env)
├── app.py                # Streamlit frontend
├── requirements.txt
├── .env.example          # Copy to .env and fill in keys
└── README.md
```

## Notes on stub modules
Files marked `(stub)` in the source need real implementations:
- `retriever/faiss_store.py` – connect to your FAISS index
- `retriever/bm25_store.py` – connect to your BM25 index
- `retriever/reranker.py` – load a cross-encoder model
- `pipeline/ingestion.py` – parse PDFs with PyMuPDF / pdfplumber
- `pipeline/query_rewriter.py` – call OpenAI for HyDE/rewriting
- `agents/qa_agent.py`, `summarizer.py`, `comparator.py` – implement LLM calls
