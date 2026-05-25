# Week 7: LangGraph — Graph-Based Agent Orchestration

## Goals
- Master LangGraph for building stateful, multi-step agents
- Understand: nodes, edges, state, conditional routing
- This is also prep for LangChain Academy certification

## Daily Plan (5 sessions × 1hr)

### Day 1: LangGraph Fundamentals
- [ ] Complete: https://academy.langchain.com/courses/intro-to-langgraph (start here!)
- [ ] Core concepts: StateGraph, nodes, edges, conditional edges
- [ ] Exercise: simple chatbot with LangGraph

### Day 2: State Management
- [ ] Exercise: agent with persistent state across turns
- [ ] Checkpointing: save/restore agent state
- [ ] Human-in-the-loop: pause execution for user approval

### Day 3: Tool-Calling Agent
- [ ] Exercise: LangGraph agent with tool nodes
- [ ] Pattern: LLM node → conditional edge → tool node → back to LLM
- [ ] Compare with raw tool-use loop from Week 3

### Day 4: Branching + Parallel Execution
- [ ] Exercise: agent that fans out to multiple tools in parallel
- [ ] Implement: map-reduce pattern (split → process → aggregate)
- [ ] Error handling and retry logic

### Day 5: Complex Workflow
- [ ] Exercise: research agent with planning → search → write → review loop
- [ ] Multiple cycles until quality threshold met
- [ ] This is your Self-RAG from Week 5, but properly orchestrated

## Resources
- [LangChain Academy](https://academy.langchain.com/) — FREE, gives certificate
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangGraph Examples](https://github.com/langchain-ai/langgraph/tree/main/examples)

## Certification Note
LangChain Academy courses are FREE and give you a completion certificate.
Complete "Introduction to LangGraph" this week — it counts toward your cert goal.
