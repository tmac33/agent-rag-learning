# Week 10: Agent Memory + Planning

## Goals
- Give agents persistent memory across conversations
- Implement planning and task decomposition
- Build agents that learn and improve over time

## Daily Plan (5 sessions × 1hr)

### Day 1: Memory Types
- [ ] Understand: short-term (context window), long-term (vector store), episodic (past interactions)
- [ ] Read: https://langchain-ai.github.io/langgraph/concepts/memory/
- [ ] Exercise: agent with conversation buffer + summary memory

### Day 2: Long-Term Memory Implementation
- [ ] Exercise: agent stores important facts in vector DB between sessions
- [ ] Retrieval: when user asks something, check memory first
- [ ] Pattern: similar to how Claude Code's memory system works (you're using it now!)

### Day 3: Planning and Task Decomposition
- [ ] Exercise: given complex goal → agent creates step-by-step plan
- [ ] Implement: plan → execute step → update plan → repeat
- [ ] Handle: plan revision when a step fails

### Day 4: Reflection and Self-Improvement
- [ ] Exercise: agent reviews its own output and improves it
- [ ] Implement: generate → critique → revise loop
- [ ] Read: Reflexion paper (https://arxiv.org/abs/2303.11366)

### Day 5: Full Agent with Memory + Planning
- [ ] Exercise: personal research assistant that:
  - Remembers past research topics
  - Plans multi-step research tasks
  - Learns user preferences over time
- [ ] This combines everything from Phase 3

## Resources
- [LangGraph Memory](https://langchain-ai.github.io/langgraph/concepts/memory/)
- [MemGPT / Letta](https://github.com/letta-ai/letta)
- [Reflexion Paper](https://arxiv.org/abs/2303.11366)
- [Generative Agents Paper](https://arxiv.org/abs/2304.03442)

## Key Concepts
- Memory architecture (working, episodic, semantic)
- Plan-and-execute vs ReAct
- Reflection and self-critique
- Memory retrieval strategies (recency, relevance, importance)
