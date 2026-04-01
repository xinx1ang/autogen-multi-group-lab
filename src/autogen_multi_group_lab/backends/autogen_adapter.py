from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class AutoGenAdapter:
    model: str = "gpt-4o-mini"

    def is_available(self) -> bool:
        try:
            import autogen_agentchat  # type: ignore  # noqa: F401
            import autogen_core  # type: ignore  # noqa: F401
        except Exception:
            return False
        return bool(os.getenv("OPENAI_API_KEY"))

    def generate(self, agent_name: str, role: str, prompt: str) -> str:
        if not self.is_available():
            raise RuntimeError(
                "AutoGen backend is not available. Install autogen-agentchat/autogen-core and set OPENAI_API_KEY."
            )
        return (
            f"[{agent_name} | {role}] autogen-placeholder-response: "
            f"{prompt.strip()}"
        )
