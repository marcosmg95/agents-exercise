"""Tests for the available tools."""

from agents_exercise.tools import (
    TOOLS,
    calculator,
    get_current_time,
    search_information,
)


class TestCalculator:
    """Tests for the calculator tool."""

    def test_calculator_addition(self):
        """Test: calculator can add."""
        result = calculator("2 + 2")
        assert "4" in result

    def test_calculator_multiplication(self):
        """Test: calculator can multiply."""
        result = calculator("3 * 4")
        assert "12" in result

    def test_calculator_complex_expression(self):
        """Test: calculator can solve complex expressions."""
        result = calculator("2 + 2 * 3")
        assert "8" in result

    def test_calculator_division(self):
        """Test: calculator can divide."""
        result = calculator("10 / 2")
        assert "5" in result

    def test_calculator_invalid_expression(self):
        """Test: calculator handles errors gracefully."""
        result = calculator("2 +++ 2")
        assert "Error" in result


class TestSearchInformation:
    """Tests for the search tool."""

    def test_search_returns_string(self):
        """Test: search returns a string."""
        result = search_information("Python")
        assert isinstance(result, str)

    def test_search_contains_query(self):
        """Test: result contains the query."""
        query = "Artificial Intelligence"
        result = search_information(query)
        assert query in result


class TestGetCurrentTime:
    """Tests for the get_time tool."""

    def test_time_format(self):
        """Test: time is in correct format."""
        result = get_current_time()
        # Must be in YYYY-MM-DD HH:MM:SS format
        parts = result.split(" ")
        assert len(parts) == 2
        assert "-" in parts[0]  # Date
        assert ":" in parts[1]  # Time

    def test_time_returns_string(self):
        """Test: get_time returns a string."""
        result = get_current_time()
        assert isinstance(result, str)


class TestToolsRegistry:
    """Tests for the tools registry."""

    def test_tools_available(self):
        """Test: all tools are registered."""
        required_tools = ["calculator", "search", "get_time"]
        for tool in required_tools:
            assert tool in TOOLS, f"Tool '{tool}' not found in TOOLS"

    def test_tools_are_callable(self):
        """Test: all tools are callable."""
        for tool_name, tool_func in TOOLS.items():
            assert callable(tool_func), f"'{tool_name}' is not callable"
