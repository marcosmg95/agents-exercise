# Agents exercise with LangGraph

A hands-on exercise for learning to build intelligent agents using LangGraph.

## Step 1: Initial setup

### 1.1 Clone the repository

```bash
git clone <REPOSITORY_URL>
cd agents-exercise
```

### 1.2 Get an API key (important)

1. Go to https://aistudio.google.com/app/apikey
2. Create a new API key (it's free)
3. Copy the key

### 1.3 Configure .env

```bash
# Copy the example file
cp .env.example .env

# Edit .env and paste your API key:
# GOOGLE_API_KEY=your_api_key_here
```

**Important:**
- Never commit the `.env` file to the repository
- Each student must use their own API key

### 1.4 Install dependencies

```bash
# Install the project and its dependencies
uv sync

# Install development dependencies (for tests)
uv pip install -e ".[dev]"
```

## Step 2: Understanding the structure

```
agents-exercise/
├── src/agents_exercise/
│   ├── __init__.py
│   ├── py.typed
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── core.py           # Agent implementation
│   │   └── state.py          # Agent state management
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── prompts.yaml      # Prompt templates
│   └── tools/
│       ├── __init__.py
│       ├── calculator.py     # Calculator tool
│       ├── search.py         # Search tool
│       └── time.py           # Time tool
├── scripts/
│   ├── example.py            # Run agent examples
│   └── interactive.py        # Interactive shell for testing
├── tests/
│   ├── test_agent.py         # Agent tests
│   └── test_tools.py         # Tool tests
├── pyproject.toml
├── .env.example
└── README.md
```

## Step 3: See the agent in action

The agent is already implemented and working. You can see it in action in two ways:

### Option 1: Run examples

```bash
python scripts/example.py
```

This runs a series of predefined examples showing the agent in action.

### Option 2: Interactive shell

```bash
python scripts/interactive.py
```

Or from VS Code, open the command palette (Ctrl+Shift+D) and select "Interactive agent".

In the shell you can:
- Type any prompt (e.g., "What is 2 + 2?")
- Use `clear` to reset the conversation
- Use `exit` or `quit` to exit

## Step 4: Run tests

### 4.1 Run all tests

```bash
pytest
```

### 4.2 Run specific tests

```bash
# Only tool tests
pytest tests/test_tools.py -v

# Only agent tests
pytest tests/test_agent.py -v

# With coverage
pytest --cov=src/agents_exercise
```

### 4.3 Tests from VS Code

Open the command palette (Ctrl+Shift+D) to see available options:
- "Run all tests" - Runs all tests
- "Run tests with coverage" - With coverage report
- "Run agent tests" - Agent tests only
- "Run tool tests" - Tool tests only
- "Interactive agent" - Interactive shell

## Step 5: How the agent works

The agent implemented in `src/agents_exercise/agent/core.py` does the following:

1. **Receives user input** via `process_input(user_input)`

2. **Detects intent:**
   - If it contains a math expression → uses the `calculator` tool
   - If it asks about the time → uses the `get_time` tool
   - If it requests information → uses the `search` tool

3. **Invokes the appropriate tool** with `invoke_tool()`

4. **Returns the response** to the user

5. **Maintains conversation history** in `state.conversation_history`

### Available tools

- **calculator**: Evaluates math expressions
- **search**: Searches for information (simulated)
- **get_time**: Returns the current time

## Preliminary exercises

Learn to:
1. Set up a Python development environment with `uv`
2. Use modern dependencies like LangGraph and Gemini AI
3. Understand how an agent processes input and uses tools
4. Write and run automated tests

## Completion checklist

- [ ] Environment configured (`uv sync`)
- [ ] `.env` created with API key
- [ ] Ran `scripts/example.py` successfully
- [ ] Ran the interactive shell (`scripts/interactive.py`)
- [ ] All tests pass (`pytest`)
- [ ] Explored the agent code in `src/agents_exercise/agent/core.py`
- [ ] Understand how the agent detects intents and uses tools

## Useful resources

- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain documentation](https://python.langchain.com/)
- [Gemini AI Studio](https://aistudio.google.com/)

## Frequently asked questions

**Q: Do I need to pay for the Gemini API?**
A: No, the free Gemini AI Studio API is completely free.

**Q: Where is the agent implementation?**
A: In `src/agents_exercise/agent/core.py`. It is already complete and working.

**Q: How do I run the agent interactively?**
A: Run `python scripts/interactive.py` or use VS Code with Ctrl+Shift+D and select "Interactive agent".

**Q: Can I modify the agent?**
A: Of course, it's your code. Modify `core.py` to experiment with different intent detection logic.

---

## Student tasks

Once you have understood how the base agent works, here are 14 tasks to go deeper into LangGraph and intelligent agents. The first seven are beginner-friendly — start there if you are new to Python or LLM development.

### Task 1: Prompt engineering
**Difficulty:** Beginner

Improve the agent's behavior purely through prompt changes in `prompts/prompts.yaml` — no Python required.

**Requirements:**
- Rewrite the system prompt to give clearer, more explicit instructions for when to use each tool
- Add a behavioral rule (e.g., always respond concisely, always use bullet points for lists, never make up facts)
- Add at least two few-shot examples showing the expected tool-use pattern
- Verify the changes improve output quality using the interactive shell
- Write a test that validates the prompt file loads correctly and contains the expected sections

**Files to modify:** `src/agents_exercise/prompts/prompts.yaml`, `tests/`

---

### Task 2: Implement the real search tool
**Difficulty:** Beginner

The current `search.py` returns a hardcoded stub (`"Simulated result for: {query}"`). Replace it with a real implementation.

**Requirements:**
- Implement the tool using a free API — e.g., [DuckDuckGo Instant Answer API](https://duckduckgo.com/api) or [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/) (no API key required for either)
- Handle error cases: network failure, empty results, malformed response
- Keep the existing tool name and signature so nothing else breaks
- Update `tests/test_tools.py` to test the real implementation (mock the HTTP calls — no live network in tests)

**Files to modify:** `src/agents_exercise/tools/search.py`, `tests/test_tools.py`

---

### Task 3: Custom tool implementation - domain-specific helper
**Difficulty:** Beginner

Implement a new specialized tool (e.g., unit converter, JSON validator, weather API integration, etc.) that extends the agent's capabilities.

**Requirements:**
- Define the tool schema with clear input/output
- Implement robust input validation
- Integrate the tool with the agent using LangChain tool binding
- Write tests for the tool
- Document usage examples

**Files to modify:** `src/agents_exercise/tools/`, `tests/`

---

### Task 4: Extend the calculator tool
**Difficulty:** Beginner

The calculator currently supports only basic arithmetic (`+`, `-`, `*`, `/`, `**`). Extend it to support common math functions.

**Requirements:**
- Add support for `sqrt`, `abs`, `round`, `floor`, and `ceil`
- Keep the safe AST-based evaluator — do not use `eval()`
- Update the tool's docstring to document the new functions
- Add tests for each new function and for invalid inputs

**Files to modify:** `src/agents_exercise/tools/calculator.py`, `tests/test_tools.py`

---

### Task 5: Add a `help` command to the interactive shell
**Difficulty:** Beginner

Students typing in the interactive shell have no way to discover available commands or example queries. Add a `help` command.

**Requirements:**
- Typing `help` prints available shell commands (`clear`, `exit`, `quit`, `save`) and 3-5 example queries they can try
- Output is readable and well-formatted
- No changes to the agent or tools — shell script only
- Add a simple test or manual verification step documenting expected output

**Files to modify:** `scripts/interactive.py`

---

### Task 6: Conversation export
**Difficulty:** Beginner

Add a `save` command to the interactive shell that writes the current conversation to a file so users can review it later.

**Requirements:**
- Typing `save` writes the full conversation history to a `.json` file with a timestamped filename (e.g., `conversation_2026-04-21_14-30.json`)
- Each entry includes the role (`user`/`assistant`) and the message text
- Print a confirmation message with the file path after saving
- Handle the case where there is nothing to save yet
- Write a test that verifies the exported file structure

**Files to modify:** `scripts/interactive.py`, `tests/`

---

### Task 7: Config validation & friendly startup errors
**Difficulty:** Beginner

Currently, a missing or invalid `.env` file causes an unreadable crash. Improve the startup experience with clear, actionable error messages.

**Requirements:**
- On startup, validate that `GOOGLE_API_KEY` is set and non-empty
- If missing, print a human-readable error explaining how to create `.env` and where to get an API key, then exit cleanly (no stack trace)
- If the key looks obviously wrong (e.g., all whitespace), warn the user before the first API call
- Write tests that verify the validation logic with missing and invalid keys

**Files to modify:** `src/agents_exercise/config.py`, `tests/`

---

### Task 8: Comprehensive agent testing suite
**Difficulty:** Intermediate

Expand the existing test suite to cover multi-turn flows, tool failures, error recovery, and edge cases. A basic suite already exists — the goal is to increase coverage and robustness.

**Requirements:**
- Multi-turn tests with persistent context
- Tool failure tests (error, empty result)
- Edge case tests (empty input, very long input, special characters)
- Error recovery tests
- Mocking of external tools (no real API calls in tests)
- Coverage >80% of agent code
- Parameterized tests for multiple scenarios
- CI/CD ready fixture setup in `conftest.py`

**Files to modify:** `tests/test_agent.py`, `tests/conftest.py`

---

### Task 9: Agent observability & tool call tracking
**Difficulty:** Intermediate

Instrument the agent to record and monitor all tool invocations, execution times, success/failure rates, and call sequences.

**Requirements:**
- Detailed logging of each tool invocation (what, when, result)
- Performance metrics (latency, success/failure)
- Summary report showing:
  - Most used tools
  - Frequently failing tools
  - Average execution time
  - Typical tool sequences
- Export data to JSON/CSV for analysis
- Tests for the monitoring module

**Files to modify:** `src/agents_exercise/agent/core.py`, create `src/agents_exercise/monitoring.py`

---

### Task 10: Safety guardrails & execution constraints
**Difficulty:** Intermediate

Implement safety guardrails for the agent: input validation, rate limiting, tool whitelisting, timeouts, and output verification.

**Requirements:**
- Input validation (detect malicious/unauthorized queries)
- Rate limiting (maximum calls per minute)
- Tool whitelist per user/session
- Tool execution timeout (maximum 30 seconds)
- Output validation (filtered/verified content)
- Logging of blocked attempts
- "Strict" vs "permissive" mode
- Tests for each guardrail

**Files to modify:** `src/agents_exercise/agent/core.py`, create `src/agents_exercise/guardrails.py`

---

### Task 11: Persistent conversation state with context management
**Difficulty:** Intermediate

Implement a conversational memory system that maintains context across sessions. State currently lives only in memory — persist it and manage long conversations gracefully.

**Requirements:**
- Extend `AgentState` with persistence (SQLite or file-based)
- Implement automatic summarization of long conversations to avoid exceeding the context window
- Allow the agent to restore a previous session on startup
- Tests for multi-turn conversations across sessions

**Files to modify:** `src/agents_exercise/agent/state.py`, `src/agents_exercise/agent/core.py`

---

### Task 12: Custom conditional routing logic
**Difficulty:** Intermediate-Advanced

Implement an explicit intent classifier that routes user queries to the most appropriate tool or chain, rather than relying solely on the LLM's judgment.

**Requirements:**
- Intent classifier (math, research, time, general, custom)
- Router that maps intents to specific tools/chains
- Confidence scores for each classification
- Fallback to generic LLM handling if confidence is low
- Support for multi-tool intents (e.g., "search + calculate")
- Logging of routing decisions and accuracy metrics
- Tests with example queries for each intent

**Files to modify:** `src/agents_exercise/agent/core.py`, create `src/agents_exercise/router.py`

---

### Task 13: Streaming responses & real-time token feedback
**Difficulty:** Intermediate-Advanced

Implement token-by-token response streaming using LangGraph's streaming APIs so users see output as it is generated.

**Requirements:**
- Implement streaming in `process_input()` using LangGraph streaming APIs
- Display tokens as they arrive in the interactive shell
- Show tool invocations as they occur
- Show the agent's intermediate reasoning steps
- Compatible with `scripts/interactive.py`
- Error handling during streaming
- Tests to verify that all tokens are delivered correctly

**Files to modify:** `src/agents_exercise/agent/core.py`, `scripts/interactive.py`

---

### Task 14: Multi-path conversation branches & exploration
**Difficulty:** Advanced

Allow the agent to explore multiple response paths in parallel. The user can say "try something else" or "use tool X instead" to fork and compare different approaches.

**Requirements:**
- Implement state forking in the graph
- Allow rollback to previous conversation points
- Named branch system (e.g., "math-branch", "search-branch")
- Compare results between different branches
- Branch persistence (save/load)
- Tests for multi-branch flows

**Files to modify:** `src/agents_exercise/agent/core.py`, `src/agents_exercise/agent/state.py`

---

## Recommended progression

**Phase 1 - Foundations (Beginner):**
- Task 1: Prompt engineering
- Task 2: Implement the search tool
- Task 3: Custom tool implementation
- Task 4: Extend the calculator tool
- Task 5: Help command
- Task 6: Conversation export
- Task 7: Config validation

**Phase 2 - Robustness (Intermediate):**
- Task 8: Testing suite
- Task 9: Observability
- Task 10: Safety guardrails

**Phase 3 - Intelligence (Intermediate):**
- Task 11: Persistent conversation state
- Task 12: Custom routing

**Phase 4 - Advanced features:**
- Task 13: Streaming responses
- Task 14: Multi-path branches

## Evaluation criteria

For each task:
- Code works correctly
- Tests pass and coverage >70%
- Readable and well-documented code
- Edge cases considered
- README updated with usage instructions
