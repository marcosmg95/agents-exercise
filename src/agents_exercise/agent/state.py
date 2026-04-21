"""Agent state."""

from dataclasses import dataclass, field
from typing import Annotated, Any, Dict, List, Optional

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


@dataclass
class AgentState:
    """External agent state (human-readable history for tests and UI)."""

    messages: List[str] = field(default_factory=list)
    current_input: Optional[str] = None
    tool_results: Dict[str, Any] = field(default_factory=dict)
    conversation_history: List[Dict[str, str]] = field(default_factory=list)


class GraphState(TypedDict):
    """Internal graph state for LangGraph (accumulates messages with add_messages)."""

    messages: Annotated[List[BaseMessage], add_messages]
