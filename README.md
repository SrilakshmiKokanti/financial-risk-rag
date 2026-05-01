# \# 💼 Financial Risk RAG \& AI Agent Assistant

# 

# > A production-ready, domain-focused GenAI assistant over financial policy and risk documents — built with RAG, hybrid search, LangChain, LangGraph, FastAPI, and Docker. Fully free to run using Groq LLM + HuggingFace local embeddings.

# 

# !\[Python](https://img.shields.io/badge/Python-3.11-blue)

# !\[FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)

# !\[LangChain](https://img.shields.io/badge/LangChain-0.2.6-orange)

# !\[LangGraph](https://img.shields.io/badge/LangGraph-0.1.9-red)

# !\[Docker](https://img.shields.io/badge/Docker-ready-blue)

# !\[Groq](https://img.shields.io/badge/LLM-Groq-purple)

# !\[License](https://img.shields.io/badge/license-MIT-green)

# 

# \---

# 

# \## 📌 Project Overview

# 

# This project solves a real-world problem in the financial industry: \*\*how do you make large, complex risk policy documents instantly queryable using AI?\*\*

# 

# Instead of manually searching through hundreds of pages of credit risk policies, market risk frameworks, and operational guidelines, this assistant lets you ask natural language questions and get precise, cited answers in seconds.

# 

# \*\*Example:\*\*

# ```

# Q: What is the single obligor credit limit?

# A: According to the credit risk policy, the single obligor credit limit 

# &#x20;  is max 10% of Tier 1 capital.

# &#x20;  Source: docs/credit\_risk\_policy.txt

# ```

# 

# \---

# 

# \## 🎯 Key Features

# 

# | Feature | Details |

# |---|---|

# | 🔍 \*\*Hybrid Search\*\* | Combines BM25 keyword search + FAISS semantic search for best retrieval |

# | 🤖 \*\*LLM Answering\*\* | Uses Groq (free) with llama-3.1-8b-instant for fast responses |

# | 📄 \*\*Document Ingestion\*\* | Upload any PDF or TXT financial document via API |

# | 🔀 \*\*Multi-Provider LLM\*\* | Switch between Groq, OpenAI, Anthropic via one `.env` config |

# | 📊 \*\*Built-in Evals\*\* | Faithfulness, hallucination, and relevance scoring |

# | 🐳 \*\*Dockerized\*\* | One command to run the entire stack |

# | ⚡ \*\*FastAPI\*\* | Production-grade REST API with auto Swagger docs |

# | 🔁 \*\*CI Pipeline\*\* | GitHub Actions runs tests + evals on every push |

# 

# \---

# 

# \## 🏗️ System Architecture

# 

# ```

# ┌─────────────────────────────────────────────────────┐

# │                   User / Client                      │

# │         (Swagger UI / curl / Frontend)               │

# └──────────────────────┬──────────────────────────────┘

# &#x20;                      │ HTTP POST /chat

# &#x20;                      ▼

# ┌─────────────────────────────────────────────────────┐

# │                  FastAPI Server                      │

# │              (uvicorn on port 8000)                  │

# │                                                      │

# │   /health   /chat   /ingest                          │

# └──────────────────────┬──────────────────────────────┘

# &#x20;                      │

# &#x20;                      ▼

# ┌─────────────────────────────────────────────────────┐

# │              Hybrid RAG Retriever                    │

# │                                                      │

# │   ┌─────────────────┐    ┌──────────────────┐       │

# │   │  BM25 Retriever │    │  FAISS Retriever  │       │

# │   │ (keyword match) │    │ (semantic search) │       │

# │   └────────┬────────┘    └────────┬─────────┘       │

# │            │     40% weight       │  60% weight      │

# │            └──────────┬───────────┘                  │

# │                       │                              │

# │              EnsembleRetriever                       │

# │            (top-k merged results)                    │

# └──────────────────────┬──────────────────────────────┘

# &#x20;                      │ Retrieved Context

# &#x20;                      ▼

# ┌─────────────────────────────────────────────────────┐

# │                  LLM (via Groq)                      │

# │          llama-3.1-8b-instant (free)                 │

# │                                                      │

# │  System Prompt + Context + Question → Answer         │

# └──────────────────────┬──────────────────────────────┘

# &#x20;                      │

# &#x20;                      ▼

# ┌─────────────────────────────────────────────────────┐

# │                API Response                          │

# │  { answer, sources, latency\_ms }                     │

# └─────────────────────────────────────────────────────┘

# ```

# 

# \---

# 

# \## 🧱 Tech Stack

# 

# | Layer | Technology | Why |

# |---|---|---|

# | \*\*LLM\*\* | Groq llama-3.1-8b-instant | Free, ultra-fast (560 tokens/sec) |

# | \*\*Embeddings\*\* | HuggingFace all-MiniLM-L6-v2 | Free, runs locally, no API needed |

# | \*\*Vector Store\*\* | FAISS | Fast similarity search, runs in-memory |

# | \*\*Keyword Search\*\* | BM25 (rank-bm25) | Handles exact term matching |

# | \*\*Hybrid Search\*\* | LangChain EnsembleRetriever | Best of both semantic + keyword |

# | \*\*Orchestration\*\* | LangChain + LangGraph | Modular, production-grade pipelines |

# | \*\*API Framework\*\* | FastAPI + Uvicorn | Async, high-performance REST API |

# | \*\*Containerization\*\* | Docker + Docker Compose | One-command deployment |

# | \*\*CI/CD\*\* | GitHub Actions | Automated testing + evals on push |

# | \*\*Evals\*\* | Custom LLM-as-judge | Faithfulness, hallucination, relevance |

# 

# \---

# 

# \## 📁 Project Structure

# 

# ```

# financial-risk-rag/

# │

# ├── app/                          # FastAPI application

# │   ├── main.py                   # App entrypoint, route registration

# │   ├── config.py                 # LLM provider switcher (Groq/OpenAI/Anthropic)

# │   └── routes/

# │       ├── chat.py               # POST /chat — RAG query endpoint

# │       └── ingest.py             # POST /ingest — document upload endpoint

# │

# ├── rag/                          # Retrieval-Augmented Generation pipeline

# │   ├── loader.py                 # Load \& chunk PDF/TXT documents

# │   ├── embedder.py               # HuggingFace embedding wrapper

# │   ├── indexer.py                # Build \& save FAISS index

# │   └── retriever.py              # Hybrid BM25 + FAISS retriever

# │

# ├── agent/                        # LangGraph AI agent

# │   ├── graph.py                  # RAG pipeline (retrieve → generate)

# │   ├── tools.py                  # Agent tools (doc search, risk scorer)

# │   └── prompts.py                # System prompts for financial domain

# │

# ├── evals/                        # LLM-as-judge evaluation scripts

# │   ├── faithfulness.py           # Is the answer grounded in context?

# │   ├── hallucination.py          # Does the answer contain made-up info?

# │   └── relevance.py              # Is the retrieved context relevant?

# │

# ├── docs/                         # Sample financial documents

# │   ├── credit\_risk\_policy.txt    # Credit risk limits, assessment criteria

# │   ├── market\_risk\_framework.txt # VaR, stress testing, FX/equity limits

# │   └── operational\_risk\_guidelines.txt  # Controls, BCP, KRIs

# │

# ├── tests/                        # Unit tests

# │   ├── test\_rag.py               # Tests for document loading, retrieval

# │   └── test\_agent.py             # Tests for agent response generation

# │

# ├── .github/

# │   └── workflows/

# │       └── ci.yml                # GitHub Actions CI pipeline

# │

# ├── Dockerfile                    # Container build instructions

# ├── docker-compose.yml            # Multi-service orchestration

# ├── requirements.txt              # Python dependencies

# ├── .env.example                  # Environment variable template

# └── README.md                     # You are here!

# ```

# 

# \---

# 

# \## 🚀 Quickstart

# 

# \### Prerequisites

# \- Docker Desktop installed and running

# \- Groq API key (free at https://console.groq.com)

# 

# \### 1. Clone the repo

# ```bash

# git clone https://github.com/SrilakshmiKokanti/financial-risk-rag.git

# cd financial-risk-rag

# ```

# 

# \### 2. Set up environment

# ```bash

# cp .env.example .env

# ```

# 

# Edit `.env`:

# ```env

# LLM\_PROVIDER=groq

# GROQ\_API\_KEY=your\_groq\_api\_key\_here

# GROQ\_MODEL=llama-3.1-8b-instant

# EMBEDDING\_MODEL=all-MiniLM-L6-v2

# FAISS\_INDEX\_PATH=./faiss\_index

# DOCS\_PATH=./docs

# ```

# 

# \### 3. Run with Docker

# ```bash

# docker-compose up --build

# ```

# 

# \### 4. Open Swagger UI

# ```

# http://localhost:8000/docs

# ```

# 

# \---

# 

# \## 📬 API Reference

# 

# \### `GET /health`

# Check if the server is running.

# 

# \*\*Response:\*\*

# ```json

# {"status": "ok"}

# ```

# 

# \---

# 

# \### `POST /chat`

# Ask a question about financial risk documents.

# 

# \*\*Request:\*\*

# ```json

# {

# &#x20; "query": "What is the single obligor credit limit?"

# }

# ```

# 

# \*\*Response:\*\*

# ```json

# {

# &#x20; "answer": "According to the credit risk policy, the single obligor credit limit is max 10% of Tier 1 capital.",

# &#x20; "sources": \[

# &#x20;   "./docs/credit\_risk\_policy.txt",

# &#x20;   "./docs/market\_risk\_framework.txt",

# &#x20;   "./docs/operational\_risk\_guidelines.txt"

# &#x20; ],

# &#x20; "latency\_ms": 1842.3

# }

# ```

# 

# \---

# 

# \### `POST /ingest`

# Upload your own financial document to index it.

# 

# ```bash

# curl -X POST http://localhost:8000/ingest \\

# &#x20; -F "file=@your\_document.pdf"

# ```

# 

# \*\*Response:\*\*

# ```json

# {"message": "Indexed your\_document.pdf successfully."}

# ```

# 

# \---

# 

# \## 🔀 Switching LLM Providers

# 

# No code changes needed — just update `.env`:

# 

# ```env

# \# Groq (Free)

# LLM\_PROVIDER=groq

# GROQ\_API\_KEY=gsk\_...

# GROQ\_MODEL=llama-3.1-8b-instant

# 

# \# OpenAI

# LLM\_PROVIDER=openai

# OPENAI\_API\_KEY=sk-...

# OPENAI\_MODEL=gpt-4o

# 

# \# Anthropic

# LLM\_PROVIDER=anthropic

# ANTHROPIC\_API\_KEY=sk-ant-...

# ANTHROPIC\_MODEL=claude-3-5-sonnet-20241022

# ```

# 

# Then restart:

# ```bash

# docker-compose down \&\& docker-compose up

# ```

# 

# \---

# 

# \## 📊 Evaluation Framework

# 

# This project includes an LLM-as-judge evaluation framework that scores the quality of RAG responses across three dimensions:

# 

# \### Faithfulness

# Measures whether the answer is grounded in the retrieved context (not hallucinated).

# ```bash

# python -m evals.faithfulness

# ```

# 

# \### Hallucination

# Detects if the answer contains information not present in the source documents.

# ```bash

# python -m evals.hallucination

# ```

# 

# \### Relevance

# Checks whether the retrieved context is actually relevant to the query.

# ```bash

# python -m evals.relevance

# ```

# 

# All three evals run automatically via \*\*GitHub Actions CI\*\* on every push to `main`.

# 

# \---

# 

# \## 🧪 Running Tests

# 

# ```bash

# pytest tests/ -v

# ```

# 

# Expected output:

# ```

# tests/test\_rag.py::test\_load\_documents\_returns\_list PASSED

# tests/test\_rag.py::test\_risk\_score\_critical PASSED

# tests/test\_rag.py::test\_risk\_score\_low PASSED

# tests/test\_agent.py::test\_run\_agent\_returns\_answer PASSED

# ```

# 

# \---

# 

# \## 💡 Sample Queries to Try

# 

# | Question | Source Document |

# |---|---|

# | What is the single obligor credit limit? | credit\_risk\_policy.txt |

# | What are the VaR limits for market risk? | market\_risk\_framework.txt |

# | What controls exist for operational risk? | operational\_risk\_guidelines.txt |

# | What is the BCP recovery time objective? | operational\_risk\_guidelines.txt |

# | How is credit risk provisioned under IFRS 9? | credit\_risk\_policy.txt |

# | What is the maximum FX net open position? | market\_risk\_framework.txt |

# | What is the DV01 limit for interest rate risk? | market\_risk\_framework.txt |

# | What triggers a credit facility early warning? | credit\_risk\_policy.txt |

# 

# \---

# 

# \## 🔁 CI/CD Pipeline

# 

# Every push to `main` triggers the GitHub Actions pipeline:

# 

# ```

# Push to main

# &#x20;   │

# &#x20;   ├── Install dependencies

# &#x20;   ├── Run pytest unit tests

# &#x20;   ├── Run faithfulness eval

# &#x20;   ├── Run hallucination eval

# &#x20;   └── Run relevance eval

# ```

# 

# Pipeline config: `.github/workflows/ci.yml`

# 

# \---

# 

# \## 🗺️ Roadmap

# 

# \- \[ ] Streamlit / React frontend UI

# \- \[ ] Conversation memory (multi-turn chat)

# \- \[ ] Reranking with cross-encoder model

# \- \[ ] Support DOCX, CSV, Excel ingestion

# \- \[ ] User authentication on API

# \- \[ ] Response caching for repeated queries

# \- \[ ] Async document ingestion queue

# 

# \---

# 

# \## 👩‍💻 About

# 

# Built as a portfolio project demonstrating production-grade GenAI engineering — covering the full stack from document ingestion to hybrid retrieval, LLM generation, evaluation, containerization, and CI/CD.

# 

# \*\*Skills demonstrated:\*\*

# \- Retrieval-Augmented Generation (RAG)

# \- Vector databases (FAISS)

# \- Hybrid search (BM25 + semantic)

# \- LLM orchestration (LangChain, LangGraph)

# \- REST API development (FastAPI)

# \- Containerization (Docker)

# \- LLM evaluation frameworks

# \- CI/CD (GitHub Actions)

# 

# \---

# 

# \## 📄 License

# 

# MIT License — free to use, modify, and distribute.

