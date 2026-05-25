# Week 3: Claude Tool Use + Agent Basics

## Goals
- Master Anthropic tool use (function calling)
- Build your first agent that can use tools
- Understand the ReAct pattern (Reason + Act)

## Daily Plan (5 sessions × 1hr)

### Day 1: Claude Tool Use Basics
- [ ] Read: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
- [ ] Exercise: define tools (get_weather, search_db), have Claude call them
- [ ] Understand: tool definition schema, tool_use/tool_result message flow

### Day 2: Multi-Turn Tool Use
- [ ] Exercise: agent that can call multiple tools in sequence
- [ ] Implement: conversation loop that handles tool calls automatically
- [ ] Pattern: user → claude → tool_use → tool_result → claude → response

### Day 3: ReAct Pattern
- [ ] Read: ReAct paper (https://arxiv.org/abs/2210.03629) — skim, don't deep-read
- [ ] Exercise: implement ReAct loop — Thought → Action → Observation → repeat
- [ ] Build: a research agent that searches + summarizes

### Day 4: Agent with RAG Tool
- [ ] Exercise: combine Week 1-2 RAG with tool use
- [ ] Agent has a `search_knowledge_base` tool that queries your vector DB
- [ ] Agent decides WHEN to search vs answer from memory

### Day 5: Go Agent Service
- [ ] Exercise: build the agent loop in Go using Anthropic Go SDK
- [ ] Handle: streaming, tool calls, multi-turn state
- [ ] Repo: https://github.com/anthropics/anthropic-sdk-go

## Resources
- [Anthropic Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Anthropic Go SDK](https://github.com/anthropics/anthropic-sdk-go)
- [Building Effective Agents](https://docs.anthropic.com/en/docs/build-with-claude/agents)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## Key Concepts
- Tool definition (name, description, input_schema)
- Forced tool use vs auto tool choice
- Agent loop: observe → think → act → observe
- When to use agents vs simple prompting
