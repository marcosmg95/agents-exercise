"""Tools available for the agent."""

from langchain_core.tools import tool

from agents_exercise.tools.calculator import calculator
from agents_exercise.tools.search import search_information
from agents_exercise.tools.time import get_current_time

TOOLS = {
    "calculator": calculator,
    "search": search_information,
    "get_time": get_current_time,
}


@tool
def calculator_tool(expression: str) -> str:
    """Calculates the result of a mathematical expression (e.g., '2 + 2 * 3')."""
    return calculator(expression)


@tool
def get_time_tool() -> str:
    """Gets the current date and time."""
    return get_current_time()


@tool
def search_tool(query: str) -> str:
    """Searches for information about a topic or person."""
    return search_information(query)


LANGCHAIN_TOOLS = [calculator_tool, get_time_tool, search_tool]

__all__ = [
    "TOOLS",
    "LANGCHAIN_TOOLS",
    "calculator",
    "search_information",
    "get_current_time",
    "calculator_tool",
    "get_time_tool",
    "search_tool",
]
