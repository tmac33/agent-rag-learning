# Week 2: Embedding Models + Vector Databases

## Goals
- Understand embedding model selection and tradeoffs
- Hands-on with production vector databases
- Build a RAG system with pgvector (leverage your SQL/infra knowledge)

## Daily Plan (5 sessions × 1hr)

### Day 1: Embedding Deep Dive
- [ ] Read: https://docs.voyageai.com/docs/embeddings
- [ ] Compare: Voyage AI vs OpenAI vs Cohere embeddings
- [ ] Exercise: embed same text with 2 different models, compare similarity scores

### Day 2: pgvector (Postgres + Vectors)
- [ ] Set up: `docker run postgres` with pgvector extension
- [ ] Exercise: create table with vector column, insert embeddings, query with cosine similarity
- [ ] Why this matters: you already know Postgres, this extends your existing stack

### Day 3: Pinecone / Weaviate (Managed)
- [ ] Sign up for Pinecone free tier
- [ ] Exercise: same RAG pipeline but with Pinecone as backend
- [ ] Compare: latency, API ergonomics, filtering capabilities

### Day 4: Chunking Strategies
- [ ] Implement: fixed-size, recursive character, semantic chunking
- [ ] Exercise: same document, 3 chunking strategies, compare retrieval quality
- [ ] Read: https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/

### Day 5: Go RAG Service
- [ ] Exercise: build a Go HTTP service that wraps pgvector
- [ ] Endpoints: POST /ingest (chunk + embed + store), POST /query (embed + retrieve)
- [ ] This is YOUR differentiator — high-performance RAG in Go

## Resources
- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [pgvector Go client](https://github.com/pgvector/pgvector-go)
- [Pinecone Docs](https://docs.pinecone.io/)
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — embedding model benchmarks

## Key Concepts
- Embedding dimensions and their impact on storage/performance
- HNSW vs IVFFlat indexing
- Metadata filtering
- Hybrid search (dense + sparse vectors)
