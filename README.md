# Agent + RAG Learning Path

> **A 16-week structured plan for going from "I've called the OpenAI API" to "I can design and ship a production-grade Agentic RAG system."**
> Designed for backend engineers who want depth, not buzzwords.

[![Status](https://img.shields.io/badge/status-in%20progress-yellow.svg)](#progress)
[![Stack](https://img.shields.io/badge/stack-Go%20%2B%20Python-blue.svg)](#why-go--python)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Why this exists

Most "learn RAG in 7 days" tutorials teach you to copy a `.from_documents()` call into a notebook. They don't teach you:

- Why hybrid (BM25 + vector) often beats pure dense retrieval, and when it doesn't
- What chunk size does to answer drift, and why parent-document retrieval exists
- How to design `LangGraph` state so failure recovery is a 3-line change instead of a rewrite
- When to hard-code a workflow vs. let the agent plan
- What `RAGAS` actually measures and what it misses
- How to read a token bill — what `prompt caching` saves vs. what it doesn't

This repo is **my answer** to those gaps: a 16-week, 1-hour-per-night curriculum that takes the questions seriously.

If you're a backend engineer who can read a paper, run `docker compose`, and tolerate 30 minutes of theory before code, this is for you.

---

## Schedule

- **Cadence:** ~1 hour/night, 5 nights/week
- **Duration:** 16 weeks (~80 hours total)
- **Output:** A working Agentic RAG system + week-by-week notes + 2 certifications
- **Stack:** Go (retrieval/services) + Python (agent orchestration) — see [Why Go + Python](#why-go--python)

## Progress

- [ ] **Phase 1** — Foundations (Week 1–3)
- [ ] **Phase 2** — Advanced RAG (Week 4–6)
- [ ] **Phase 3** — Agent Orchestration (Week 7–10)
- [ ] **Phase 4** — Engineering + Capstone (Week 11–14)
- [ ] **Phase 5** — Certification (Week 15–16)

---

## What you'll learn (week by week)

Every week has a detailed `README.md` with a 5-day plan: reading list (papers, docs, blog posts), key concepts to absorb, and hands-on exercises. Click any week to see the full plan.

### Phase 1 — Foundations (Week 1–3)

| Week | Focus | What you'll be able to do |
|------|-------|---------------------------|
| [Week 1: RAG Pipeline](./phase1-foundations/week01-rag-basics) | Load → Chunk → Embed → Store → Retrieve → Generate | Explain why TF-IDF fails on synonyms; build a Go RAG service against pgvector |
| [Week 2: Vector Databases](./phase1-foundations/week02-vector-db) | pgvector, HNSW, IVFFlat, ANN tradeoffs | Pick the right index for your scale; know when you don't need a vector DB |
| [Week 3: Tool Use & Function Calling](./phase1-foundations/week03-agent-tools) | Anthropic / OpenAI tool schemas, idempotency, structured errors | Design tool schemas an agent can actually use safely |

### Phase 2 — Advanced RAG (Week 4–6)

| Week | Focus | What you'll be able to do |
|------|-------|---------------------------|
| [Week 4: Advanced Retrieval](./phase2-advanced-rag/week04-advanced-retrieval) | Query rewriting, HyDE, decomposition, reranking | Improve retrieval quality measurably (not "I think it's better") |
| [Week 5: Self-RAG](./phase2-advanced-rag/week05-self-rag) | Self-reflection loops, retrieve-then-critique, adaptive retrieval | Know when self-RAG is worth the latency, when it isn't |
| [Week 6: Graph RAG](./phase2-advanced-rag/week06-graph-rag) | Knowledge graphs, entity extraction, multi-hop reasoning | Pick graph vs. dense retrieval based on the actual question shape |

### Phase 3 — Agent Orchestration (Week 7–10)

| Week | Focus | What you'll be able to do |
|------|-------|---------------------------|
| [Week 7: LangGraph](./phase3-agent-orchestration/week07-langgraph) | StateGraph, nodes/edges, conditional routing, checkpointers | Build a stateful agent with deterministic recovery |
| [Week 8: Multi-Agent Systems](./phase3-agent-orchestration/week08-multi-agent) | Supervisor, hierarchical, swarm patterns; CrewAI vs. LangGraph | Choose a multi-agent topology — and recognize when one agent is enough |
| [Week 9: Agentic RAG](./phase3-agent-orchestration/week09-agentic-rag) | Agents that decide *how* to retrieve, not just *what* | Combine retrieval + reasoning into a closed feedback loop |
| [Week 10: Memory & Planning](./phase3-agent-orchestration/week10-memory-planning) | Short-term, long-term, episodic memory; ReAct vs. Plan-and-Execute | Decide what your agent should remember and for how long |

### Phase 4 — Engineering + Capstone (Week 11–14)

| Week | Focus | What you'll be able to do |
|------|-------|---------------------------|
| [Week 11: Evaluation](./phase4-engineering/week11-evaluation) | RAGAS, deepeval, human eval, A/B test design | Set up evaluation that catches real regressions, not noise |
| [Week 12: Production](./phase4-engineering/week12-production) | Observability, cost monitoring, prompt caching, rate-limit/quota fallback | Run an LLM service like a backend service |
| [Week 13–14: Capstone](./phase4-engineering/week13-capstone) | Build the *Intelligent Document Assistant* | A real, deployable Agentic RAG system end-to-end |

### Phase 5 — Certification (Week 15–16)

| Week | Focus |
|------|-------|
| [Week 15: Review](./phase5-certification/week15-review) | LangChain Academy course (free) + AWS AI Practitioner / ML Specialty prep |
| [Week 16: Exam](./phase5-certification/week16-exam) | Take the certs while the material is fresh |

---

## The Capstone: Intelligent Document Assistant

Phase 4 ends with a production-shape project that exercises everything you learned:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Client    │────▶│  Go Gateway  │────▶│  Agent Workers  │
│  (Web/CLI)  │◀────│  (API+Stream)│◀────│  (Python/LG)    │
└─────────────┘     └──────┬───────┘     └────────┬────────┘
                           │                       │
                           ▼                       ▼
                    ┌──────────────┐       ┌──────────────┐
                    │   pgvector   │       │  LLM (Claude │
                    │  + Postgres  │       │   / Gemini)  │
                    └──────────────┘       └──────────────┘
```

It's not a notebook. It's a real service: streaming responses, observability, evaluation harness, cost tracking. Full architecture in [`phase4-engineering/week13-capstone/`](./phase4-engineering/week13-capstone).

---

## Why Go + Python?

**Short answer:** ecosystem in Python, performance in Go.

| Layer | Language | Why |
|-------|----------|-----|
| Agent orchestration (LangGraph, CrewAI, AutoGen) | Python | Frameworks are Python-native; ecosystem is years ahead |
| Retrieval, embeddings pipeline, observability, gateway | Go | Hot path; type-safe, memory-efficient, easier to operate at scale |

I don't try to rewrite LangGraph in Go. I let Python do what it's good at, and put the production-shape concerns (gateway, retrieval, streaming, metrics) in Go where they belong. The capstone wires them together via HTTP/gRPC.

This split is the same model I've used in production at work — it's not theoretical.

---

## Philosophy

- **You focus on:** concepts, architecture decisions, evaluating results, writing the Go service
- **The LLM (Claude, GPT, etc.) writes:** Python boilerplate, glue code, demo scripts
- **Reading lists are real, not links to skim:** every week cites primary sources (Anthropic docs, papers, framework guides) — read them properly
- **Hands-on > tutorials:** every week has exercises that *force* the concept (e.g. "find a query where TF-IDF wins and one where dense embeddings win")
- **The repo is messy and public on purpose:** you'll see where I get stuck, change my mind, and rewrite. That's more useful than polished post-hoc tutorials.

---

## How to use this repo

**As a follower:** Star/fork it, then walk the same 16 weeks. File issues with your sticking points — chances are I hit them too.

**As a teacher:** Steal the structure. The week-by-week template (📖 Reading → key concepts → 💻 Practice → 🤔 Reflection questions) is reusable for any technical topic.

**As a recruiter looking at @tmac33:** Yes, this is in-progress. The point of a learning repo isn't to be impressive on day 1 — it's to show structured thinking and follow-through over months. The depth is in the weekly READMEs. Open any of them.

---

## About the author

I'm a senior Go engineer based in Auckland with 10+ years in distributed systems (telecom backend, gRPC, GCP-native). I've shipped LLM features in side projects but want to formalize the foundation before claiming "AI engineer" anywhere.

- GitHub: [@tmac33](https://github.com/tmac33)
- Other repos worth a look: [`go-saga`](https://github.com/tmac33/go-saga) (saga library), [`goauth-demo`](https://github.com/tmac33/goauth-demo) (production-shape Go auth service)

---

## License

MIT — fork freely, no attribution required (though always appreciated).

Drop a ⭐ if this is useful — it also helps me stay accountable to the schedule.
