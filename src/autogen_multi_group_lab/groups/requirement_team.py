from ..agents.base import Agent
from ..runtime.backend import BackendManager
from ..runtime.schemas import RequirementSpec


class RequirementTeam:
    def __init__(self, backend: BackendManager | None = None) -> None:
        backend = backend or BackendManager()
        self.leader = Agent("A-Leader", "Requirement Lead", backend=backend)
        self.worker_1 = Agent("A-Worker-1", "Requirement Analyst", backend=backend)
        self.worker_2 = Agent("A-Worker-2", "Task Decomposer", backend=backend)

    def run(self, task: str) -> RequirementSpec:
        print(self.leader.say("Received task from UserProxy and starting requirement analysis."))
        print(self.worker_1.say("Extracting intent, scope, and constraints."))
        print(self.worker_2.say("Breaking the work into actionable subtasks."))
        print(self.worker_1.think(f"Summarize the user's intent and constraints for: {task}"))
        print(self.worker_2.think(f"Decompose this task into practical subtasks: {task}"))

        constraints = [
            "Keep the solution simple and runnable.",
            "Provide a clear code example.",
            "Include basic validation through tests.",
        ]
        subtasks = [
            "Clarify expected behavior.",
            "Produce implementation sketch.",
            "Produce tests and acceptance checklist.",
        ]
        acceptance = [
            "The output includes a Python implementation.",
            "The output includes at least one test case.",
            "The result is understandable by a human reviewer.",
        ]

        print(self.leader.say("Merging worker outputs into a requirement spec."))
        return RequirementSpec(
            task_summary=task,
            constraints=constraints,
            subtasks=subtasks,
            acceptance_criteria=acceptance,
        )
