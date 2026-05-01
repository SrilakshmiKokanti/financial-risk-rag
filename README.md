# 💼 Financial Risk RAG & AI Agent Assistant

> A production-ready GenAI assistant over financial policy and risk documents, built with RAG, hybrid search, LangChain, FastAPI, and Docker. Fully free using Groq LLM + HuggingFace embeddings.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.6-orange)](https://langchain.com)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](https://docker.com)
[![Groq](https://img.shields.io/badge/LLM-Groq-purple)](https://console.groq.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📌 Project Overview

This project solves a real-world problem in the financial industry: **how do you make large, complex risk policy documents instantly queryable using AI?**

Instead of manually searching through hundreds of pages of credit risk policies, market risk frameworks, and operational guidelines, this assistant lets you ask natural language questions and get precise, cited answers in seconds.

**Example:**

```
Q: What is the single obligor credit limit?
A: According to the credit risk policy, the single obligor credit limit
   is max 10% of Tier 1 capital.
   Source: docs/credit_risk_policy.txt
```

---

## 🎯 Key Features

| Feature | Details |
|---|---|
| 🔍 **Hybrid Search** | BM25 keyword search + FAISS semantic search combined |
| 🤖 **LLM Answering** | Groq llama-3.1-8b-instant — free and ultra-fast |
| 📄 **Document Ingestion** | Upload any PDF or TXT document via API |
| 🔀 **Multi-Provider LLM** | Switch between Groq, OpenAI, Anthropic via `.env` |
| 📊 **Built-in Evals** | Faithfulness, hallucination, and relevance scoring |
| 🐳 **Dockerized** | One command to run the entire stack |
| ⚡ **FastAPI** | Production-grade REST API with auto Swagger docs |
| 🔁 **CI Pipeline** | GitHub Actions runs tests and evals on every push |

---

## 🏗️ System Architecture

```
User Query
    │
    ▼
FastAPI /chat endpoint
    │
    ▼
Hybrid Retriever
    ├── BM25 Retriever (40%)  — keyword match
    └── FAISS Retriever (60%) — semantic search
    │
    ▼
EnsembleRetriever — top-k merged results
    │
    ▼
Groq LLM (llama-3.1-8b-instant)
System Prompt + Context + Question
    │
    ▼
Response: { answer, sources, latency_ms }
```

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **LLM** | Groq llama-3.1-8b-instant | Free, 560 tokens/sec inference |
| **Embeddings** | HuggingFace all-MiniLM-L6-v2 | Free, runs locally |
| **Vector Store** | FAISS | Fast in-memory similarity search |
| **Keyword Search** | BM25 (rank-bm25) | Exact term matching |
| **Hybrid Search** | LangChain EnsembleRetriever | Best of semantic + keyword |
| **Orchestration** | LangChain + LangGraph | Modular AI pipelines |
| **API** | FastAPI + Uvicorn | Async, high-performance REST |
| **Infra** | Docker + Docker Compose | One-command deployment |
| **CI/CD** | GitHub Actions | Automated tests and evals |
| **Evals** | Custom LLM-as-judge | Quality measurement |

---

## 📁 Project Structure

```
financial-risk-rag/
│
├── app/
│   ├── main.py                   # FastAPI entrypoint
│   ├── config.py                 # LLM provider switcher
│   └── routes/
│       ├── chat.py               # POST /chat
│       └── ingest.py             # POST /ingest
│
├── rag/
│   ├── loader.py                 # Document loader and chunker
│   ├── embedder.py               # HuggingFace embeddings
│   ├── indexer.py                # FAISS index builder
│   └── retriever.py              # Hybrid BM25 + FAISS retriever
│
├── agent/
│   ├── graph.py                  # RAG pipeline
│   ├── tools.py                  # Agent tools
│   └── prompts.py                # System prompts
│
├── evals/
│   ├── faithfulness.py           # Groundedness eval
│   ├── hallucination.py          # Hallucination detection
│   └── relevance.py              # Context relevance eval
│
├── docs/
│   ├── credit_risk_policy.txt
│   ├── market_risk_framework.txt
│   └── operational_risk_guidelines.txt
│
├── tests/
│   ├── test_rag.py
│   └── test_agent.py
│
├── .github/workflows/ci.yml      # GitHub Actions CI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## 🚀 Quickstart

### Prerequisites
- Docker Desktop installed and running
- Free Groq API key from https://console.groq.com

### 1. Clone the repo
```bash
git clone https://github.com/SrilakshmiKokanti/financial-risk-rag.git
cd financial-risk-rag
```

### 2. Set up environment
```bash
cp .env.example .env
```

Edit `.env`:
```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
EMBEDDING_MODEL=all-MiniLM-L6-v2
FAISS_INDEX_PATH=./faiss_index
DOCS_PATH=./docs
```

### 3. Run with Docker
```bash
docker-compose up --build
```

### 4. Open Swagger UI
```
http://localhost:8000/docs
```

---

## 📬 API Reference

### GET /health
```json
{ "status": "ok" }
```

---

### POST /chat

**Request:**
```json
{
  "query": "What is the single obligor credit limit?"
}
```

**Response:**
```json
{
  "answer": "The single obligor credit limit is max 10% of Tier 1 capital.",
  "sources": [
    "./docs/credit_risk_policy.txt"
  ],
  "latency_ms": 1842.3
}
```

---

### POST /ingest
```bash
curl -X POST http://localhost:8000/ingest \
  -F "file=@your_document.pdf"
```

**Response:**
```json
{ "message": "Indexed your_document.pdf successfully." }
```

---

## 🔀 Switching LLM Providers

Update one line in `.env` — no code changes needed:

```env
# Groq (Free)
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_...

# OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...

# Anthropic
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
```

Then restart:
```bash
docker-compose down && docker-compose up
```

---

## 📊 Evaluation Framework

| Eval | What It Measures | Pass Threshold |
|---|---|---|
| Faithfulness | Is the answer grounded in context? | >= 0.7 |
| Hallucination | Does the answer contain made-up info? | >= 0.6 |
| Relevance | Is retrieved context relevant to the query? | >= 0.7 |

Run all evals:
```bash
python -m evals.faithfulness
python -m evals.hallucination
python -m evals.relevance
```

All three run automatically on every push via GitHub Actions.

---

## 🧪 Tests

```bash
pytest tests/ -v
```

---

## 💡 Sample Queries

| Question | Source |
|---|---|
| What is the single obligor credit limit? | credit_risk_policy.txt |
| What are the VaR limits for market risk? | market_risk_framework.txt |
| What controls exist for operational risk? | operational_risk_guidelines.txt |
| What is the BCP recovery time objective? | operational_risk_guidelines.txt |
| How is credit risk provisioned under IFRS 9? | credit_risk_policy.txt |
| What is the maximum FX net open position? | market_risk_framework.txt |

---

## 🗺️ Roadmap

- [ ] Streamlit / React frontend UI
- [ ] Conversation memory (multi-turn chat)
- [ ] Reranking with cross-encoder model
- [ ] Support DOCX, CSV, Excel ingestion
- [ ] Response caching for repeated queries

---

## 👩‍💻 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector databases (FAISS)
- Hybrid search (BM25 + semantic)
- LLM orchestration (LangChain, LangGraph)
- REST API development (FastAPI)
- Containerization (Docker)
- LLM evaluation frameworks
- CI/CD (GitHub Actions)

---

## 📄 License

MIT License — free to use, modify, and distribute.
