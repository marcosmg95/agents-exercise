"""Conversational agent with LangGraph."""

from typing import Literal

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from agents_exercise.agent.state import AgentState, GraphState
from agents_exercise.config import Config
from agents_exercise.prompts import SYSTEM_PROMPT
from agents_exercise.tools import LANGCHAIN_TOOLS, TOOLS

# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------


class ConversationAgent:
    """Conversational agent based on LangGraph + Gemini."""

    def __init__(self, config: Config | None = None):
        self._config = config or Config()
        self.state = AgentState()
        self.model_name = self._config.model_name
        # Accumulated LangGraph messages for multi-turn context
        self._graph_messages: list[BaseMessage] = [SystemMessage(content=SYSTEM_PROMPT)]
        self._llm_with_tools = None  # built lazily on first process_input call
        self._graph = None  # built lazily on first process_input call

    # ------------------------------------------------------------------
    # Graph nodes and routing
    # ------------------------------------------------------------------

    def _call_llm(self, state: GraphState) -> GraphState:
        response = self._llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    def _should_continue(self, state: GraphState) -> Literal["tools", "__end__"]:
        last = state["messages"][-1]
        if getattr(last, "tool_calls", None):
            return "tools"
        return "__end__"

    # ------------------------------------------------------------------
    # Graph construction
    # ------------------------------------------------------------------

    def _build_graph(self) -> StateGraph:
        llm = ChatGoogleGenerativeAI(
            model=self.model_name, google_api_key=self._config.google_api_key
        )
        self._llm_with_tools = llm.bind_tools(LANGCHAIN_TOOLS)
        tool_node = ToolNode(LANGCHAIN_TOOLS)

        graph = StateGraph(GraphState)
        graph.add_node("agent", self._call_llm)
        graph.add_node("tools", tool_node)
        graph.set_entry_point("agent")
        graph.add_conditional_edges(
            "agent",
            self._should_continue,
            {"tools": "tools", "__end__": END},
        )
        graph.add_edge("tools", "agent")
        return graph.compile()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def process_input(self, user_input: str) -> str:
        """Processes user input by executing the LangGraph graph."""
        if self._graph is None:
            self._graph = self._build_graph()

        self.state.current_input = user_input
        self.state.messages.append(f"User: {user_input}")

        self._graph_messages.append(HumanMessage(content=user_input))
        result = self._graph.invoke({"messages": self._graph_messages})

        # Persist accumulated messages (tools + AI turns) for next invocation
        self._graph_messages = result["messages"]

        raw = result["messages"][-1].content
        if isinstance(raw, list):
            response = "".join(
                block.get("text", "") for block in raw if block.get("type") == "text"
            )
        else:
            response = raw
        self.state.messages.append(f"Agent: {response}")
        self.state.conversation_history.append(
            {"user": user_input, "agent": response, "tool_used": None}
        )
        return response

    def invoke_tool(self, tool_name: str, **kwargs) -> str:
        """Directly invokes a tool by name."""
        if tool_name not in TOOLS:
            return f"Tool '{tool_name}' not found"
        try:
            return TOOLS[tool_name](**kwargs)
        except Exception as e:
            return f"Error invoking {tool_name}: {str(e)}"

    def reset_conversation(self) -> None:
        """Resets the conversation state."""
        self.state = AgentState()
        self._graph_messages = [SystemMessage(content=SYSTEM_PROMPT)]


def create_agent(config: Config | None = None) -> ConversationAgent:
    """Factory function to create a ConversationAgent."""
    return ConversationAgent(config=config)
