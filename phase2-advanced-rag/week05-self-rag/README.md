# Week 5: Self-RAG + Corrective RAG

## Goals
- Implement RAG systems that self-evaluate and self-correct
- Understand when retrieval helps vs hurts
- Build adaptive retrieval pipelines

## Daily Plan (5 sessions × 1hr)

### Day 1: Self-RAG Paper
- [ ] Read: https://arxiv.org/abs/2310.11511 (Self-RAG)
- [ ] Core idea: LLM decides whether to retrieve, evaluates relevance, checks for hallucination
- [ ] Map out the decision flow

### Day 2: Implement Retrieval Decision
- [ ] Exercise: LLM first decides "do I need to retrieve?" before searching
- [ ] Classification prompt: given the query, is external knowledge needed?
- [ ] Test with factual vs conversational queries

### Day 3: Relevance Grading
- [ ] Exercise: after retrieval, LLM grades each document's relevance
- [ ] Filter out irrelevant docs before generation
- [ ] Implement: structured output for relevance scoring

### Day 4: Corrective RAG (CRAG)
- [ ] Read: https://arxiv.org/abs/2401.15884
- [ ] Implement: if retrieved docs are poor → fall back to web search
- [ ] Decision tree: Correct → use docs | Ambiguous → refine query | Incorrect → web search

### Day 5: Full Self-Correcting Pipeline
- [ ] Combine: retrieval decision → retrieve → grade → generate → hallucination check
- [ ] If hallucination detected → re-retrieve with refined query
- [ ] Build this as a LangGraph workflow (preview of Week 7)

## Resources
- [Self-RAG Paper](https://arxiv.org/abs/2310.11511)
- [CRAG Paper](https://arxiv.org/abs/2401.15884)
- [LangGraph CRAG Tutorial](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/)

## Key Concepts
- Adaptive retrieval (not always retrieve)
- Document relevance grading
- Hallucination detection
- Iterative refinement loops
