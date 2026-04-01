from ..agents.base import Agent
from ..runtime.backend import BackendManager
from ..runtime.schemas import FinalReport
from .implementation_team import ImplementationTeam
from .qa_team import QATeam
from .requirement_team import RequirementTeam


class UserProxyTeam:
    def __init__(self, backend: BackendManager | None = None) -> None:
        backend = backend or BackendManager()
        self.user_proxy = Agent("D-UserProxy", "UserProxy Agent", backend=backend)
        self.requirement_team = RequirementTeam(backend=backend)
        self.implementation_team = ImplementationTeam(backend=backend)
        self.qa_team = QATeam(backend=backend)

    def run(self, task: str) -> tuple[FinalReport, str]:
        print(self.user_proxy.say("Accepted the user task and dispatching to Requirement Team."))
        spec = self.requirement_team.run(task)
        draft = self.implementation_team.run(spec)
        qa = self.qa_team.run(spec, draft)

        next_action = "Return result to user" if qa.status == "pass" else "Send back to Implementation Team"
        final = FinalReport(
            task=task,
            requirement_summary=f"Generated {len(spec.subtasks)} subtasks and {len(spec.acceptance_criteria)} acceptance criteria.",
            implementation_summary=draft.implementation_summary,
            qa_status=qa.status,
            next_action=next_action,
        )

        full_output = [
            "\n=== FINAL REPORT ===",
            f"Task: {final.task}",
            f"Requirement summary: {final.requirement_summary}",
            f"Implementation summary: {final.implementation_summary}",
            f"QA status: {final.qa_status}",
            f"Next action: {final.next_action}",
            "\n=== GENERATED CODE DRAFT ===",
            draft.code_blocks[0],
            "\n=== QA TEST CASES ===",
            *qa.test_cases,
        ]
        return final, "\n".join(full_output)
