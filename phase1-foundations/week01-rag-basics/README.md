# Week 1: RAG Pipeline — Understand + Run

## Goals
- Understand the RAG pipeline: Load → Chunk → Embed → Store → Retrieve → Generate
- Run each step, understand WHY it works (not how to code it — Claude writes the code)
- Build mental model of tradeoffs at each stage

## Approach
**You focus on:** reading → concepts → architecture decisions → running & evaluating results  
**Claude writes:** all Python/boilerplate code — you just tell it what you want  
**Each day:** 20-30 min reading → 30-40 min hands-on practice

---

## Day 1: RAG Overview — Read + Run First Pipeline

### 📖 Reading (20-30 min)
1. [What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/) — AWS explanation, clear and cert-relevant (10 min)
2. [Anthropic: Citations](https://platform.claude.com/docs/en/docs/build-with-claude/citations) — How Claude handles retrieved documents (10 min)
3. [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — Their approach to improving RAG (10 min)

### Key concepts to absorb:
- Why do LLMs hallucinate? How does retrieval reduce this?
- What's the difference between parametric knowledge (in the model) vs non-parametric (retrieved)?
- RAG pipeline: Load → Chunk → Embed → Store → Retrieve → Generate

### 💻 Practice (30-40 min)
- [ ] Run `day1-rag-demo`: `cd day1-rag-demo && ~/.local/bin/uv run main.py`
- [ ] Observe the TF-IDF scores for each query
- [ ] In interactive mode: try queries IN the docs vs NOT in the docs
- [ ] Notice: "How does Kubernetes work?" gets low scores — RAG knows its limits

### 🤔 Questions to answer after practice:
- What happens when retrieved chunks have low relevance scores?
- Can you trick the system by using different words for the same concept?
- Why might TF-IDF fail for "What is the best way to split text?" (hint: synonyms)

---

## Day 2: Embeddings — Read + Compare TF-IDF vs Neural

### 📖 Reading (20-30 min)
1. [What are embeddings?](https://vickiboykis.com/what_are_embeddings/) — Vicki Boykis' excellent guide, Chapters 1-3 (15 min)
2. [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — Skim to see how Anthropic improves embeddings (10 min)
3. [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — Browse: which models are best? (5 min)

### Key concepts to absorb:
- Sparse vectors (TF-IDF: mostly zeros, matches words) vs Dense vectors (neural: all values, captures meaning)
- Why "car" and "vehicle" are close in dense space but far in TF-IDF
- Cosine similarity: angle between vectors = semantic similarity
- Embedding dimensions (384 vs 768 vs 1536) and the tradeoffs

### 💻 Practice (30-40 min)
- [ ] Claude generates a `day2-embeddings` script using Bedrock Titan Embeddings
- [ ] Run same queries from Day 1, compare which chunks get retrieved
- [ ] Find a query where TF-IDF fails but neural embeddings succeed
- [ ] Find a query where TF-IDF actually wins (exact keyword match)

---

## Day 3: Chunking — Read + Experiment with Strategies

### 📖 Reading (20-30 min)
1. [Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/) — Pinecone guide (15 min)
2. [LlamaIndex: Node Parsers](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/) — Skim the types available (10 min)
3. [Five Levels of Chunking](https://medium.com/@anuragmishra_27746/five-levels-of-chunking-strategies-in-rag-notes-from-gregs-video-7b735895694d) — Greg Kamradt's framework (5 min)

### Key concepts to absorb:
- Fixed-size vs sentence-based vs semantic chunking
- Chunk overlap: why lose some redundancy to avoid split information
- The chunk size sweet spot: too small = no context, too large = diluted retrieval
- How your QUERY type should influence chunk strategy

### 💻 Practice (30-40 min)
- [ ] Claude generates `day3-chunking` with 3 strategies on same document
- [ ] Compare: which strategy retrieves the best chunk for "What is RAG?"
- [ ] Experiment: what happens with chunk_size=50? chunk_size=500?
- [ ] Find a case where a bad chunk boundary splits critical information

---

## Day 4: Vector Databases — Read + Understand Storage/Indexing

### 📖 Reading (20-30 min)
1. [What is a Vector Database?](https://www.pinecone.io/learn/vector-database/) — Pinecone (10 min)
2. [pgvector: Open-Source Vector Similarity](https://github.com/pgvector/pgvector#readme) — README overview (10 min)
3. [HNSW Explained](https://www.pinecone.io/learn/series/faiss/hnsw/) — How approximate nearest neighbor works (10 min)

### Key concepts to absorb:
- Brute-force search (O(n)) vs ANN indexes (O(log n)) — why you need indexes at scale
- HNSW: graph-based, fast, memory-hungry. IVFFlat: partition-based, less memory
- pgvector: Postgres extension = your existing SQL knowledge applies
- Metadata filtering: filter THEN search vs search THEN filter
- When you DON'T need a vector DB (< 10k chunks → brute force is fine)

### 💻 Practice (30-40 min)
- [ ] `docker run` pgvector (Claude provides the commands)
- [ ] Store Day 2's embeddings in pgvector
- [ ] Query with SQL: `SELECT * FROM chunks ORDER BY embedding <=> $query_vec LIMIT 5`
- [ ] Add metadata filtering: only search chunks from specific documents
- [ ] Compare query speed: 100 chunks vs 10,000 chunks

---

## Day 5: Build Go RAG Service (YOU write this)

### 📖 Reading (20-30 min)
1. [pgvector-go](https://github.com/pgvector/pgvector-go#readme) — Go client for pgvector (10 min)
2. [Anthropic Go SDK](https://github.com/anthropics/anthropic-sdk-go#readme) — For calling Claude from Go (10 min)
3. Review your Day 1-4 notes: what architecture makes sense? (10 min)

### Key concepts to absorb:
- HTTP service design: ingest pipeline vs query pipeline
- Separation of concerns: embedding service, vector storage, generation
- Streaming responses: why you want SSE for LLM output
- Error handling for external API calls (embeddings, LLM)

### 💻 Practice (30-40 min)
- [ ] Design the API: `POST /ingest` (text → chunk → embed → store)
- [ ] Design the API: `POST /query` (question → embed → retrieve → generate)
- [ ] Implement in Go with chi/echo + pgvector-go
- [ ] Test with curl: ingest a document, then query it
- [ ] Bonus: add streaming response for the generation step

---

## Summary: What You'll Know After Week 1

| Concept | Day |
|---------|-----|
| RAG pipeline end-to-end | Day 1 |
| Sparse vs Dense embeddings | Day 2 |
| Chunking strategies & tradeoffs | Day 3 |
| Vector storage & indexing | Day 4 |
| Production Go implementation | Day 5 |
