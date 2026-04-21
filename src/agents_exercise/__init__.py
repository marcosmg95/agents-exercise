"""Ejercicio de Agentes con LangGraph."""

from agents_exercise.config import Config

config = Config()

from agents_exercise.agent import AgentState, ConversationAgent, create_agent
from agents_exercise.prompts import DEFAULT_PROMPT, SYSTEM_PROMPT
from agents_exercise.tools import TOOLS, calculator, get_current_time, search_information

__all__ = [
    "Config",
    "config",
    "ConversationAgent",
    "create_agent",
    "AgentState",
    "TOOLS",
    "calculator",
    "search_information",
    "get_current_time",
    "SYSTEM_PROMPT",
    "DEFAULT_PROMPT",
]

__version__ = "0.1.0"
