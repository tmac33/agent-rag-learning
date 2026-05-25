# Week 8: Multi-Agent Systems

## Goals
- Build systems where multiple specialized agents collaborate
- Understand delegation, handoff, and coordination patterns
- Compare frameworks: CrewAI, AutoGen, native LangGraph

## Daily Plan (5 sessions × 1hr)

### Day 1: Multi-Agent Patterns
- [ ] Read: https://docs.anthropic.com/en/docs/build-with-claude/agents
- [ ] Patterns: supervisor, peer-to-peer, hierarchical, swarm
- [ ] When to use multi-agent vs single capable agent

### Day 2: LangGraph Multi-Agent
- [ ] Exercise: supervisor agent routes tasks to specialized sub-agents
- [ ] Implement: researcher agent + writer agent + reviewer agent
- [ ] LangGraph: each agent is a subgraph

### Day 3: CrewAI
- [ ] `pip install crewai`
- [ ] Exercise: define agents with roles, goals, backstories
- [ ] Build: content creation crew (researcher, writer, editor)
- [ ] Docs: https://docs.crewai.com/

### Day 4: Agent Handoff + Communication
- [ ] Exercise: agent A produces output → agent B consumes it
- [ ] Shared state vs message passing
- [ ] Error handling: what if an agent fails or loops?

### Day 5: Build a Code Review Multi-Agent
- [ ] Exercise: system with planner + coder + reviewer + tester agents
- [ ] Input: task description → Output: reviewed code
- [ ] This mirrors real engineering workflows you know

## Resources
- [CrewAI Docs](https://docs.crewai.com/)
- [AutoGen](https://github.com/microsoft/autogen)
- [LangGraph Multi-Agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/)
- [Anthropic Multi-Agent Patterns](https://docs.anthropic.com/en/docs/build-with-claude/agents)

## Key Concepts
- Agent specialization vs generalization
- Communication protocols between agents
- Supervisor vs decentralized coordination
- Preventing infinite loops and managing costs
