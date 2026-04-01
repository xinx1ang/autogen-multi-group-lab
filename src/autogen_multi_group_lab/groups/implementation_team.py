from ..agents.base import Agent
from ..runtime.backend import BackendManager
from ..runtime.schemas import ImplementationDraft, RequirementSpec


class ImplementationTeam:
    def __init__(self, backend: BackendManager | None = None) -> None:
        backend = backend or BackendManager()
        self.leader = Agent("B-Leader", "Engineering Lead", backend=backend)
        self.worker_1 = Agent("B-Worker-1", "Backend Engineer", backend=backend)
        self.worker_2 = Agent("B-Worker-2", "Refactor Engineer", backend=backend)

    def run(self, spec: RequirementSpec) -> ImplementationDraft:
        print(self.leader.say("Received requirement spec and assigning implementation work."))
        print(self.worker_1.say("Drafting the core implementation."))
        print(self.worker_2.say("Adding tests, notes, and edge-case coverage."))
        print(self.worker_1.think(f"Propose core implementation details for: {spec.task_summary}"))
        print(self.worker_2.think(f"Propose tests, notes, and edge-case considerations for: {spec.task_summary}"))

        code = '''def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def test_add_basic():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, 1) == 0
'''

        notes = [
            "The MVP emits a code draft instead of writing files automatically.",
            "The implementation is intentionally small so the workflow is easy to inspect.",
            f"Input task was: {spec.task_summary}",
        ]

        print(self.leader.say("Merging implementation worker outputs into a delivery draft."))
        return ImplementationDraft(
            implementation_summary="Prepared a simple Python implementation draft plus tests.",
            changed_files=["generated_example.py"],
            code_blocks=[code],
            notes=notes,
        )
