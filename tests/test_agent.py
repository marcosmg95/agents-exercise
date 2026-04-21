"""Tests for the conversational agent."""

from agents_exercise.agent import AgentState, ConversationAgent, create_agent


class TestAgentState:
    """Tests for the AgentState class."""

    def test_initial_state(self):
        """Test: initial state is correct."""
        state = AgentState()
        assert state.messages == []
        assert state.current_input is None
        assert state.tool_results == {}
        assert state.conversation_history == []

    def test_state_with_messages(self):
        """Test: messages can be added to state."""
        state = AgentState(messages=["Hello", "How are you?"])
        assert len(state.messages) == 2
        assert "Hello" in state.messages


class TestConversationAgent:
    """Tests for the ConversationAgent class."""

    def test_agent_creation(self, agent: ConversationAgent):
        """Test: an agent can be created."""
        assert agent is not None
        assert isinstance(agent.state, AgentState)

    def test_agent_creation_with_factory(self):
        """Test: an agent can be created with factory function."""
        a = create_agent()
        assert a is not None
        assert isinstance(a, ConversationAgent)

    def test_agent_reset_conversation(self, agent: ConversationAgent):
        """Test: conversation can be reset."""
        agent.state.messages = ["message1", "message2"]
        agent.reset_conversation()
        assert agent.state.messages == []

    def test_agent_invoke_tool_calculator(self, agent: ConversationAgent):
        """Test: agent can invoke the calculator tool."""
        result = agent.invoke_tool("calculator", expression="2 + 2")
        assert "4" in result

    def test_agent_invoke_tool_get_time(self, agent: ConversationAgent):
        """Test: agent can invoke the get_time tool."""
        result = agent.invoke_tool("get_time")
        assert "-" in result and ":" in result

    def test_agent_invoke_nonexistent_tool(self, agent: ConversationAgent):
        """Test: agent handles nonexistent tools."""
        result = agent.invoke_tool("nonexistent_tool")
        assert "not found" in result

    def test_agent_process_input_returns_string(self, agent: ConversationAgent):
        """Test: process_input returns a string."""
        result = agent.process_input("What is 2 + 2?")
        assert isinstance(result, str)


class TestAgentIntegration:
    """Integration tests for the agent."""

    def test_agent_workflow(self, agent: ConversationAgent):
        """Test: agent basic workflow works."""
        calc_result = agent.invoke_tool("calculator", expression="5 * 3")
        assert "15" in calc_result

        agent.reset_conversation()
        assert len(agent.state.messages) == 0

    def test_agent_with_multiple_tools(self, agent: ConversationAgent):
        """Test: agent can use multiple tools."""
        result1 = agent.invoke_tool("calculator", expression="10 + 5")
        assert "15" in result1

        result2 = agent.invoke_tool("get_time")
        assert isinstance(result2, str)

        result3 = agent.invoke_tool("search", query="Python")
        assert "Python" in result3
