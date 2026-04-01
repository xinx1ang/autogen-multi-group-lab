from dataclasses import dataclass, field
from typing import List


@dataclass
class RequirementSpec:
    task_summary: str
    constraints: List[str] = field(default_factory=list)
    subtasks: List[str] = field(default_factory=list)
    acceptance_criteria: List[str] = field(default_factory=list)


@dataclass
class ImplementationDraft:
    implementation_summary: str
    changed_files: List[str] = field(default_factory=list)
    code_blocks: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class QaReport:
    status: str
    test_cases: List[str] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)
    recommendation: str = ""


@dataclass
class FinalReport:
    task: str
    requirement_summary: str
    implementation_summary: str
    qa_status: str
    next_action: str
