# Week 12: Production Architecture

## Goals
- Design production-grade RAG + Agent systems
- Leverage your Go + distributed systems expertise
- Build something deployable

## Daily Plan (5 sessions × 1hr)

### Day 1: Architecture Design
- [ ] Design: Go API gateway + Python agent workers + pgvector
- [ ] Patterns: async ingestion pipeline, streaming responses, rate limiting
- [ ] Draw architecture diagram for your capstone

### Day 2: Go RAG Service (Production)
- [ ] Build: high-performance Go service with proper error handling
- [ ] Features: connection pooling, graceful shutdown, health checks
- [ ] Use: pgvector-go, chi/echo router, structured logging

### Day 3: Agent Worker (Python)
- [ ] Build: Python worker that executes agent workflows
- [ ] Communication: gRPC or message queue (Redis/NATS) between Go and Python
- [ ] Handle: timeouts, retries, circuit breakers

### Day 4: Streaming + Real-time
- [ ] Implement: SSE/WebSocket streaming from agent to client
- [ ] Go handles the connection, streams tokens from Python agent
- [ ] Exercise: real-time typing indicator + partial results

### Day 5: Docker + Deploy
- [ ] Dockerize: multi-stage builds for Go + Python services
- [ ] docker-compose for local development
- [ ] CI: GitHub Actions for tests + build

## Resources
- [pgvector-go](https://github.com/pgvector/pgvector-go)
- [Anthropic Streaming](https://docs.anthropic.com/en/api/streaming)
- [NATS](https://nats.io/) — lightweight messaging (Go-native)

## Key Concepts
- Separation of concerns: routing (Go) vs intelligence (Python)
- Async processing for document ingestion
- Streaming architecture for LLM responses
- Resilience patterns (circuit breaker, bulkhead, timeout)
