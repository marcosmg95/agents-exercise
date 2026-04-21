"""
Example agent runs - shows the agent handling different types of queries.
"""

from agents_exercise import create_agent

EXAMPLES = [
    "What is 15 * 7?",
    "What time is it?",
    "Search for information about LangGraph",
    "Calculate (100 + 50) / 3",
    "Search for Python programming language",
]


def run_examples():
    """Run a series of predefined examples showing the agent in action."""
    agent = create_agent()

    print("=" * 60)
    print("Agent examples")
    print("=" * 60)

    for i, prompt in enumerate(EXAMPLES, 1):
        print(f"\n[Example {i}/{len(EXAMPLES)}]")
        print(f"User: {prompt}")
        try:
            response = agent.process_input(prompt)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 60)
    print("All examples completed.")
    print("=" * 60)


if __name__ == "__main__":
    run_examples()
