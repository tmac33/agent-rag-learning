# Week 13-14: Capstone Project

## Project: Intelligent Document Assistant

A production-grade Agentic RAG system that showcases your full stack:
Go backend + Python agents + advanced RAG + multi-agent orchestration.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Client    │────▶│  Go Gateway  │────▶│  Agent Workers  │
│  (Web/CLI)  │◀────│  (API+Stream)│◀────│  (Python/LG)    │
└─────────────┘     └──────┬───────┘     └────────┬────────┘
                           │                       │
                    ┌──────▼───────┐        ┌──────▼────────┐
                    │   pgvector   │        │  Tool Services │
                    │  (vectors)   │        │  (search, calc)│
                    └──────────────┘        └───────────────┘
```

## Features to Implement

### Core (Week 13)
- [ ] Document ingestion pipeline (PDF, markdown, web pages)
- [ ] Multi-strategy retrieval (vector + keyword + graph)
- [ ] Agentic RAG with self-correction
- [ ] Streaming responses via SSE

### Advanced (Week 14)
- [ ] Multi-agent: router → researcher → writer → fact-checker
- [ ] Long-term memory (remembers past conversations)
- [ ] Citation tracking (every claim linked to source)
- [ ] Evaluation dashboard (RAGAS metrics)
- [ ] Cost tracking and optimization

## Tech Stack
- **Go**: API gateway, streaming, ingestion pipeline, pgvector queries
- **Python**: LangGraph agents, LLM calls, evaluation
- **Postgres + pgvector**: vector storage
- **Redis/NATS**: Go ↔ Python communication
- **Docker**: containerized deployment

## Deliverables
- [ ] GitHub repo with clean README
- [ ] Architecture documentation
- [ ] Demo video (2-3 min)
- [ ] Blog post explaining key design decisions
- [ ] Deployed demo (Railway/Fly.io/Cloud Run)

## Why This Project Works for Job Applications
1. Shows Go expertise (not just another Python-only RAG)
2. Demonstrates distributed systems thinking
3. Production-quality (not a notebook demo)
4. Combines latest AI techniques with solid engineering
