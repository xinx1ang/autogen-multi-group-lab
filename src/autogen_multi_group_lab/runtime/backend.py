from __future__ import annotations

import os

from ..backends.autogen_adapter import AutoGenAdapter
from ..backends.heuristic import HeuristicBackend


class BackendManager:
    def __init__(self) -> None:
        self.requested = os.getenv("AMGL_BACKEND", "heuristic").strip().lower() or "heuristic"
        self.autogen = AutoGenAdapter(model=os.getenv("AMGL_MODEL", "gpt-4o-mini"))
        self.heuristic = HeuristicBackend()

    def describe(self) -> str:
        if self.requested == "autogen":
            ok, reason = self.autogen.dependency_status()
            if ok:
                return f"autogen(model={self.autogen.model})"
            return f"heuristic(fallback-from-autogen-request:{reason})"
        return "heuristic"

    def generate(self, agent_name: str, role: str, prompt: str) -> str:
        if self.requested == "autogen" and self.autogen.is_available():
            return self.autogen.generate(agent_name, role, prompt)
        return self.heuristic.generate(agent_name, role, prompt)
