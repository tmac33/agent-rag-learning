# Week 11: RAG Evaluation + Observability

## Goals
- Build systematic evaluation for your RAG systems
- Set up tracing and observability
- Know if your system is actually working well

## Daily Plan (5 sessions × 1hr)

### Day 1: RAG Evaluation Metrics
- [ ] Learn: faithfulness, answer relevancy, context precision, context recall
- [ ] Read: https://docs.ragas.io/en/stable/
- [ ] Exercise: install RAGAS, evaluate your Week 9 agentic RAG

### Day 2: Building Eval Datasets
- [ ] Exercise: create question-answer-context triples from your documents
- [ ] Synthetic generation: use LLM to generate Q&A pairs
- [ ] Manual curation: hand-pick 20 hard questions

### Day 3: LangSmith Tracing
- [ ] Set up: https://smith.langchain.com/ (free tier)
- [ ] Exercise: trace your LangGraph agent, visualize execution flow
- [ ] Identify: where does it fail? Which steps are slow?

### Day 4: A/B Testing Retrieval
- [ ] Exercise: compare retrieval strategies on same eval set
- [ ] Metrics: hit rate, MRR, nDCG
- [ ] Build: simple eval harness that runs comparisons

### Day 5: Cost + Latency Optimization
- [ ] Profile: token usage per query, latency breakdown
- [ ] Optimize: caching, prompt compression, smaller models for routing
- [ ] Exercise: reduce cost by 50% with minimal quality loss

## Resources
- [RAGAS](https://docs.ragas.io/en/stable/)
- [LangSmith](https://smith.langchain.com/)
- [Anthropic Eval Guide](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)

## Key Concepts
- Faithfulness (does answer match retrieved context?)
- Retrieval metrics (precision, recall, MRR)
- End-to-end vs component evaluation
- Cost-quality tradeoff optimization
