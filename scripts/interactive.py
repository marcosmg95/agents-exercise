"""
Interactive agent shell - talk with the agent in real time.

Type your prompts and the agent will respond with tool usage or conversation.
Type 'exit' or 'quit' to exit the shell.
Type 'clear' to reset the conversation.
"""

from agents_exercise import create_agent


def main():
    """Interactive shell for the agent."""
    agent = create_agent()

    print("=" * 60)
    print("Interactive Agent Shell")
    print("=" * 60)
    print("\nThe agent can:")
    print("  - Perform mathematical calculations (e.g., what is 2 + 2)")
    print("  - Get the current time (e.g., what time is it)")
    print("  - Search for information (e.g., search for Python)")
    print("\nSpecial commands:")
    print("  - 'clear' to reset the conversation")
    print("  - 'exit' or 'quit' to exit")
    print("=" * 60)
    print()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nGoodbye!")
                break

            if user_input.lower() == "clear":
                agent.reset_conversation()
                print("Conversation reset.\n")
                continue

            response = agent.process_input(user_input)
            print(f"Agent: {response}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
