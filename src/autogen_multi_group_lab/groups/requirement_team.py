from ..agents.base import Agent
from ..runtime.schemas import RequirementSpec


class RequirementTeam:
    def __init__(self) -> None:
        self.leader = Agent("A-Leader", "Requirement Lead")
        self.worker_1 = Agent("A-Worker-1", "Requirement Analyst")
        self.worker_2 = Agent("A-Worker-2", "Task Decomposer")

    def run(self, task: str) -> RequirementSpec:
        print(self.leader.say("Received task from UserProxy and starting requirement analysis."))
        print(self.worker_1.say("Extracting intent, scope, and constraints."))
        print(self.worker_2.say("Breaking the work into actionable subtasks."))

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
