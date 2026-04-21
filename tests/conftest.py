"""Shared pytest fixtures."""

import pytest

from agents_exercise.agent import ConversationAgent


@pytest.fixture
def agent() -> ConversationAgent:
    """Return a fresh ConversationAgent for each test."""
    return ConversationAgent()
