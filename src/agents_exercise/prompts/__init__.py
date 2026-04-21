"""
Prompt templates for the agent.
"""

from pathlib import Path

import yaml

_data = yaml.safe_load((Path(__file__).parent / "prompts.yaml").read_text(encoding="utf-8"))

SYSTEM_PROMPT: str = _data["system_prompt"]
DEFAULT_PROMPT: str = _data["default_prompt"]
