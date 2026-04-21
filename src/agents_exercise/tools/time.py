"""Tool to get the current time."""

from datetime import datetime


def get_current_time() -> str:
    """
    Gets the current time.

    Returns:
        The current time in a readable format
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
