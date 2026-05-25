"""
Week 1, Day 1: Your First RAG Pipeline (No Framework)
======================================================
Pipeline: Load → Chunk → Vectorize → Retrieve → Generate

This uses:
  - TF-IDF for vectorization (simple, fast, no API needed for embedding)
  - Claude via Bedrock for generation (uses your existing env vars)

WHY TF-IDF first: so you can SEE what "retrieval" actually does without
black-box embeddings. Day 2 we'll swap in real embeddings and compare.

RUN:  cd day1-rag-demo && uv run main.py
"""

import os
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import anthropic


# ===========================================================
# Stage 1: LOAD — Get documents into memory
# ===========================================================
def load_documents(docs_dir: Path) -> list[str]:
    """Load all .txt files from a directory."""
    docs_dir.mkdir(exist_ok=True)

    if not any(docs_dir.glob("*.txt")):
        # Create sample docs so you can run immediately
        (docs_dir / "rag_overview.txt").write_text("""
Retrieval-Augmented Generation (RAG) is a technique that enhances LLM responses
by retrieving relevant information from a knowledge base before generating an answer.
RAG was introduced by Facebook AI Research (now Meta AI) in 2020.
The key insight is that LLMs can hallucinate facts, but if you provide them with
retrieved evidence in the prompt, they generate more accurate and grounded responses.
RAG does not require retraining the model, making it much cheaper than fine-tuning.
""")
        (docs_dir / "rag_pipeline.txt").write_text("""
The RAG pipeline consists of these stages:
1. Document Loading: Read documents from sources like PDF, web pages, databases.
2. Chunking: Split documents into smaller pieces (typically 256-1024 tokens).
3. Embedding: Convert text chunks into numerical vectors using a model like text-embedding-3-small.
4. Indexing: Store vectors in a vector database like Pinecone, pgvector, or ChromaDB.
5. Retrieval: Given a user query, embed it and find similar chunks via cosine similarity.
6. Generation: Pass the retrieved chunks as context to an LLM to generate the final answer.
The quality of each stage affects the final output significantly.
""")
        (docs_dir / "rag_vs_finetuning.txt").write_text("""
RAG vs Fine-tuning — when to use which:

RAG is better when:
- You need up-to-date information (knowledge base can be updated without retraining)
- You need citations and source attribution
- You have domain-specific documents to search over
- Budget is limited (no GPU training costs)

Fine-tuning is better when:
- You need to change the model's style, tone, or format
- You need consistent behavior on specific tasks
- You have high-quality training examples
- Latency matters (no retrieval step needed)

In practice, many production systems combine both: fine-tune for style,
RAG for factual grounding.
""")
        (docs_dir / "chunking_strategies.txt").write_text("""
Chunking is one of the most impactful decisions in RAG system design.

Fixed-size chunking: Split every N tokens. Simple but may break mid-sentence.
Sentence-based chunking: Split on sentence boundaries. Preserves meaning better.
Semantic chunking: Use embeddings to detect topic shifts. Most sophisticated.
Recursive character splitting: Try splitting on paragraphs, then sentences, then words.

Key parameters:
- Chunk size: 256 tokens gives precision, 1024 gives more context per chunk.
- Chunk overlap: 50-100 tokens of overlap prevents losing information at boundaries.

The optimal strategy depends on your documents and queries.
Technical docs with clear sections work well with larger chunks.
FAQs and Q&A pairs work well with small, precise chunks.
""")
        print("  Created 4 sample documents in ./docs/")
        print("  TIP: Replace with your own .txt files and re-run!\n")

    texts = []
    for f in sorted(docs_dir.glob("*.txt")):
        texts.append(f.read_text().strip())
        print(f"  Loaded: {f.name} ({len(f.read_text().split())} words)")
    return texts


# ===========================================================
# Stage 2: CHUNK — Split documents into smaller pieces
# ===========================================================
def chunk_documents(documents: list[str], chunk_size: int = 200, overlap: int = 50) -> list[str]:
    """Split documents into overlapping chunks by character count."""
    chunks = []
    for doc in documents:
        words = doc.split()
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            if len(chunk.strip()) > 20:
                chunks.append(chunk.strip())
    return chunks


# ===========================================================
# Stage 3: VECTORIZE — Convert text to numbers (TF-IDF)
# ===========================================================
def build_index(chunks: list[str]):
    """Build a TF-IDF index from chunks.

    TF-IDF = Term Frequency × Inverse Document Frequency
    High score = word appears often in THIS chunk but rarely in others.
    This is a "sparse" vector — most values are 0.

    Later we'll replace this with "dense" embeddings from a neural model,
    which capture MEANING not just word overlap.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(chunks)
    return vectorizer, vectors


# ===========================================================
# Stage 4: RETRIEVE — Find relevant chunks for a query
# ===========================================================
def retrieve(query: str, vectorizer, vectors, chunks: list[str], top_k: int = 3) -> list[tuple[str, float]]:
    """Find the top_k most similar chunks to the query."""
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, vectors).flatten()
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [(chunks[i], float(scores[i])) for i in top_indices]


# ===========================================================
# Stage 5: GENERATE — Ask Claude to answer using retrieved context
# ===========================================================
def generate(query: str, retrieved_chunks: list[tuple[str, float]], client) -> str:
    """Send query + retrieved context to Claude for answer generation."""
    context = "\n\n---\n\n".join(
        f"[Source {i+1}, relevance={score:.3f}]\n{text}"
        for i, (text, score) in enumerate(retrieved_chunks)
    )

    response = client.messages.create(
        model="anthropic.claude-sonnet-4-20250514-v1:0",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Answer the question based ONLY on the provided context.
If the context doesn't contain enough information, say "I don't have enough information to answer this."

Context:
{context}

Question: {query}

Answer:"""
        }]
    )
    return response.content[0].text


# ===========================================================
# MAIN — Run the full pipeline
# ===========================================================
def main():
    print("=" * 60)
    print("  RAG Pipeline Demo — Week 1, Day 1")
    print("=" * 60)

    # Load
    print("\n📄 STAGE 1: Loading documents...")
    docs_dir = Path(__file__).parent / "docs"
    documents = load_documents(docs_dir)

    # Chunk
    print(f"\n✂️  STAGE 2: Chunking {len(documents)} documents...")
    chunks = chunk_documents(documents, chunk_size=80, overlap=20)
    print(f"  → {len(chunks)} chunks created")
    print(f"  → First chunk: '{chunks[0][:80]}...'")

    # Vectorize
    print(f"\n🔢 STAGE 3: Building TF-IDF index...")
    vectorizer, vectors = build_index(chunks)
    print(f"  → Vocabulary size: {len(vectorizer.vocabulary_)} unique terms")
    print(f"  → Each chunk is a vector of {vectors.shape[1]} dimensions")
    print(f"  → (Most values are 0 — this is a 'sparse' representation)")

    # Set up Claude client (uses your Bedrock env vars)
    client = anthropic.Anthropic()

    # Query loop
    demo_queries = [
        "What are the steps in a RAG pipeline?",
        "When should I use RAG instead of fine-tuning?",
        "What is the best chunk size?",
        "How does Kubernetes work?",  # NOT in docs — watch what happens!
    ]

    print(f"\n🔍 STAGE 4-5: Retrieval + Generation")
    print("=" * 60)

    for q in demo_queries:
        print(f"\n{'─'*60}")
        print(f"  QUERY: {q}")
        print(f"{'─'*60}")

        # Retrieve
        results = retrieve(q, vectorizer, vectors, chunks, top_k=3)
        print(f"\n  📎 Retrieved chunks:")
        for i, (text, score) in enumerate(results):
            print(f"     [{i+1}] score={score:.3f} | '{text[:70]}...'")

        # Generate
        answer = generate(q, results, client)
        print(f"\n  💬 Answer: {answer}")

    # Interactive
    print(f"\n\n{'='*60}")
    print("  💬 YOUR TURN — Ask anything (type 'quit' to exit)")
    print("  Try questions IN and NOT IN the documents!")
    print(f"{'='*60}\n")

    while True:
        try:
            q = input("Question: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("quit", "exit", "q", ""):
            break
        results = retrieve(q, vectorizer, vectors, chunks, top_k=3)
        print(f"\n  Retrieved (top scores): {[f'{s:.3f}' for _, s in results]}")
        answer = generate(q, results, client)
        print(f"\n  Answer: {answer}\n")

    print("\nDone! Things to think about:")
    print("  1. TF-IDF only matches WORDS, not MEANING. 'car' won't match 'vehicle'.")
    print("  2. Notice how the 'Kubernetes' question gets low scores but still gets an answer?")
    print("     → That's the model following your 'only use context' instruction.")
    print("  3. Tomorrow we'll replace TF-IDF with neural embeddings and see the difference.")


if __name__ == "__main__":
    main()
