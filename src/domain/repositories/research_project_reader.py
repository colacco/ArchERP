from typing import Protocol
from uuid import UUID

from src.domain.entities.research_project import ResearchProject

class ResearchProjectReader(Protocol):
    def get_research_project_by_id(self, id: UUID) -> ResearchProject | None:
        pass