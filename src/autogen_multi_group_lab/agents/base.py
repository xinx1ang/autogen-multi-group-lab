from dataclasses import dataclass, field

from ..runtime.backend import BackendManager


@dataclass
class Agent:
    name: str
    role: str
    backend: BackendManager = field(default_factory=BackendManager)

    def say(self, message: str) -> str:
        return f"[{self.name} | {self.role}] {message}"

    def think(self, prompt: str) -> str:
        return self.backend.generate(self.name, self.role, prompt)
