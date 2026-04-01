from dataclasses import dataclass


@dataclass
class Agent:
    name: str
    role: str

    def say(self, message: str) -> str:
        return f"[{self.name} | {self.role}] {message}"
