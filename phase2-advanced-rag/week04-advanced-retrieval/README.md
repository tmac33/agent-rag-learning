# Week 4: Advanced Retrieval Techniques

## Goals
- Move beyond naive RAG with advanced retrieval strategies
- Implement HyDE, query transformation, and reranking
- Measurably improve retrieval quality

## Daily Plan (5 sessions × 1hr)

### Day 1: Query Transformation
- [ ] Implement: query rewriting (LLM rewrites user query for better retrieval)
- [ ] Implement: query decomposition (break complex query into sub-queries)
- [ ] Compare retrieval results: original vs transformed queries

### Day 2: HyDE (Hypothetical Document Embeddings)
- [ ] Read: HyDE paper (https://arxiv.org/abs/2212.10496)
- [ ] Exercise: generate hypothetical answer → embed that → retrieve similar real docs
- [ ] When it helps vs hurts: factual queries vs exploratory queries

### Day 3: Reranking
- [ ] Implement: retrieve top-50, rerank to top-5 using Cohere Rerank or cross-encoder
- [ ] Compare: with/without reranking on same query set
- [ ] Read: https://docs.cohere.com/docs/reranking

### Day 4: Hybrid Search (Dense + Sparse)
- [ ] Implement: BM25 (keyword) + vector (semantic) combined retrieval
- [ ] Reciprocal Rank Fusion to merge results
- [ ] Exercise: queries where keyword beats semantic and vice versa

### Day 5: Contextual Retrieval (Anthropic Method)
- [ ] Read: https://www.anthropic.com/news/contextual-retrieval
- [ ] Implement: prepend contextual summaries to chunks before embedding
- [ ] Measure improvement on your test set

## Resources
- [Anthropic Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [HyDE Paper](https://arxiv.org/abs/2212.10496)
- [Cohere Rerank](https://docs.cohere.com/docs/reranking)
- [LlamaIndex Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/)

## Key Concepts
- Retrieval precision vs recall tradeoff
- Two-stage retrieval (retrieve broadly, rerank precisely)
- Query-document mismatch problem (why HyDE works)
- Fusion strategies (RRF, weighted combination)
