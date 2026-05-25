# Week 6: Graph RAG + Knowledge Graphs

## Goals
- Understand why vector-only RAG fails for global/synthesis questions
- Build a knowledge graph from documents
- Implement Microsoft's GraphRAG approach

## Daily Plan (5 sessions × 1hr)

### Day 1: Why Graph RAG?
- [ ] Read: https://microsoft.github.io/graphrag/
- [ ] Understand: vector RAG = local lookup, Graph RAG = global reasoning
- [ ] Example: "What are the main themes across all documents?" → vector RAG fails

### Day 2: Knowledge Graph Construction
- [ ] Exercise: use LLM to extract entities and relationships from text
- [ ] Store in: NetworkX (Python) or Neo4j
- [ ] Prompt engineering for entity extraction

### Day 3: Community Detection + Summarization
- [ ] Exercise: run Leiden algorithm to find document communities
- [ ] Summarize each community with LLM
- [ ] Build hierarchical summaries (community → global)

### Day 4: GraphRAG Query Modes
- [ ] Implement: local search (entity-focused, similar to vector RAG)
- [ ] Implement: global search (community summaries → map-reduce answer)
- [ ] Compare results on different query types

### Day 5: Hybrid Architecture
- [ ] Combine: vector RAG (detail queries) + Graph RAG (synthesis queries)
- [ ] Router: classify query → route to appropriate RAG strategy
- [ ] Evaluate on mixed query set

## Resources
- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
- [GraphRAG Paper](https://arxiv.org/abs/2404.16130)
- [Neo4j + LangChain](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)
- [NetworkX](https://networkx.org/)

## Key Concepts
- Entity extraction and relationship mapping
- Community detection (Leiden algorithm)
- Hierarchical summarization
- Local vs global search strategies
- When to use Graph RAG vs vector RAG
