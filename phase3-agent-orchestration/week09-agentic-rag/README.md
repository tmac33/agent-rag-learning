# Week 9: Agentic RAG

## Goals
- Build RAG systems where the agent actively controls retrieval
- Agent decides: what to search, when, how to combine results
- This is the convergence of Phase 2 (RAG) + Phase 3 (Agents)

## Daily Plan (5 sessions × 1hr)

### Day 1: Agentic RAG vs Pipeline RAG
- [ ] Understand the shift: fixed pipeline → agent-driven retrieval
- [ ] Agent capabilities: multi-step retrieval, query refinement, source selection
- [ ] Read: https://docs.llamaindex.ai/en/stable/use_cases/agents/

### Day 2: Multi-Source Agent
- [ ] Exercise: agent with tools for different knowledge sources
- [ ] Tools: search_docs, search_web, query_database, ask_expert
- [ ] Agent decides which source to query based on the question

### Day 3: Iterative Retrieval Agent
- [ ] Exercise: agent retrieves → evaluates → decides to retrieve more or answer
- [ ] Multi-hop reasoning: answer requires combining info from multiple retrievals
- [ ] Implement with LangGraph (builds on Week 7)

### Day 4: RAG Agent with Planning
- [ ] Exercise: complex question → agent creates retrieval plan → executes → synthesizes
- [ ] Example: "Compare X and Y" → plan: [search X, search Y, compare]
- [ ] Agent decomposes complex queries into retrieval sub-tasks

### Day 5: Production Agentic RAG
- [ ] Exercise: full system with caching, fallbacks, cost tracking
- [ ] Implement: token budget awareness (don't retrieve too much)
- [ ] Add: citation tracking (which source supported which claim)

## Resources
- [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)
- [LangGraph RAG Agent](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/)
- [Anthropic RAG Patterns](https://github.com/anthropics/anthropic-cookbook)

## Key Concepts
- Agent-controlled retrieval vs fixed pipelines
- Multi-hop reasoning and iterative retrieval
- Source routing and selection
- Cost-aware retrieval (token budgets)
- Citation and provenance tracking
