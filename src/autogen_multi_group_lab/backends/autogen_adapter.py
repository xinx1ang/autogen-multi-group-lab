from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class AutoGenAdapter:
    model: str = "gpt-4o-mini"

    def dependency_status(self) -> tuple[bool, str]:
        try:
            import autogen_agentchat  # type: ignore  # noqa: F401
            import autogen_core  # type: ignore  # noqa: F401
        except Exception as exc:
            return False, f"missing-python-packages({exc.__class__.__name__})"
        if not os.getenv("OPENAI_API_KEY"):
            return False, "missing-OPENAI_API_KEY"
        return True, "ready"

    def is_available(self) -> bool:
        ok, _ = self.dependency_status()
        return ok

    def generate(self, agent_name: str, role: str, prompt: str) -> str:
        if not self.is_available():
            _, reason = self.dependency_status()
            raise RuntimeError(
                "AutoGen backend is not available: "
                f"{reason}. Install autogen-agentchat/autogen-core and set OPENAI_API_KEY."
            )

        try:
            from openai import OpenAI
        except Exception as exc:
            raise RuntimeError(f"OpenAI client import failed: {exc}") from exc

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        system_prompt = (
            f"You are {agent_name}, acting as {role} in a multi-agent software-factory demo. "
            "Reply concisely, practically, and in plain engineering language."
        )
        response = client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        text = getattr(response, "output_text", "").strip()
        if not text:
            text = "(empty model response)"
        return f"[{agent_name} | {role}] {text}"
