from dataclasses import dataclass


@dataclass
class HeuristicBackend:
    name: str = "heuristic"

    def generate(self, agent_name: str, role: str, prompt: str) -> str:
        return f"[{agent_name} | {role}] heuristic-response: {prompt.strip()}"
