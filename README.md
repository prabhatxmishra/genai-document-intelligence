# GenAI Document Intelligence & QA System

Enterprise-style GenAI project with:
- Spring Boot (Main Backend)
- FastAPI + Hugging Face (GenAI Microservice)
- ChromaDB (Vector Database)
- PostgreSQL (Users & Metadata)
- RAG-based Question Answering
- Docker & CI/CD (Planned)

## Current Status
✅ Basic LLM Chat API using Hugging Face  
🚧 PDF Upload & RAG in progress

## How to Run (GenAI Service)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload