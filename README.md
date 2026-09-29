# Enterprise AI Copilot

A Python starter structure for a retrieval-augmented generation (RAG) application.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```i

Set `LLM_API_KEY` in `.env` before configuring an LLM provider. Start the local Qdrant service with `docker compose up -d`.

## Run the API

```powershell
uvicorn main:app --reload
```

The starter health check is available at `http://127.0.0.1:8000/health`. Ingestion, retrieval, generation, and evaluation modules are structure placeholders and still need their implementations.