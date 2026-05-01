# Financial Risk RAG & AI Agent Assistant

A domain-focused GenAI assistant over financial policy and risk documents.
RAG with tool use, hybrid search, embeddings, prompt templates, FastAPI APIs.
Faithfulness & hallucination evals wired into CI.

## Stack
| Layer | Tech |
|---|---|
| LLM | OpenAI GPT-4o / Anthropic Claude 3.5 Sonnet |
| Orchestration | LangChain + LangGraph |
| Vector Store | FAISS |
| API | FastAPI |
| Evals | Faithfulness, Relevance, Hallucination |
| Infra | Docker + GitHub Actions |

## Quickstart
```bash
cp .env.example .env
docker-compose up --build
```
API: http://localhost:8000   Swagger: http://localhost:8000/docs

## Configuration
Set LLM_PROVIDER in .env to switch providers:
  LLM_PROVIDER=openai   # or: anthropic
  OPENAI_API_KEY=sk-...
  ANTHROPIC_API_KEY=sk-ant-...

## Endpoints
POST /ingest  - Upload and index documents
POST /chat    - Query the RAG agent
GET  /health  - Health check

## Running Evals
  python -m evals.faithfulness
  python -m evals.hallucination
  python -m evals.relevance