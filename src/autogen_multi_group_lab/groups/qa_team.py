from ..agents.base import Agent
from ..runtime.backend import BackendManager
from ..runtime.schemas import ImplementationDraft, QaReport, RequirementSpec


class QATeam:
    def __init__(self, backend: BackendManager | None = None) -> None:
        backend = backend or BackendManager()
        self.leader = Agent("C-Leader", "QA Lead", backend=backend)
        self.worker_1 = Agent("C-Worker-1", "Test Engineer", backend=backend)
        self.worker_2 = Agent("C-Worker-2", "Reviewer", backend=backend)

    def run(self, spec: RequirementSpec, draft: ImplementationDraft) -> QaReport:
        print(self.leader.say("Received implementation draft and starting QA review."))
        print(self.worker_1.say("Checking for implementation + tests coverage."))
        print(self.worker_2.say("Reviewing readability and acceptance alignment."))
        print(self.worker_1.think(f"Generate QA checks for implementation summary: {draft.implementation_summary}"))
        print(self.worker_2.think(f"Review acceptance alignment for task: {spec.task_summary}"))

        issues = []
        joined_code = "\n".join(draft.code_blocks)
        if "def add(" not in joined_code:
            issues.append("Missing required add(a, b) implementation.")
        if "test_" not in joined_code:
            issues.append("Missing test coverage.")

        status = "pass" if not issues else "fail"
        recommendation = "accept" if status == "pass" else "revise"

        print(self.leader.say(f"QA decision = {status}."))
        return QaReport(
            status=status,
            test_cases=[
                "Verify add(1, 2) == 3",
                "Verify add(-1, 1) == 0",
            ],
            issues=issues,
            recommendation=recommendation,
        )
