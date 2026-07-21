from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from src.domain.entities.research_project import ResearchProject
from src.domain.enums.research_project_status import ResearchProjectStatus
from src.domain.enums.research_project_visibility import ResearchProjectVisibility

class ResearchProjectRepository(ABC):
    @abstractmethod
    def create_research_project(self, research_project: ResearchProject) -> ResearchProject:
        pass

    @abstractmethod
    def count_research_projects(
        self,
        status: ResearchProjectStatus | None = None,
        visibility: ResearchProjectVisibility | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None
    ) -> int:
        pass

    @abstractmethod
    def list_research_projects(
        self,
        limit: int,
        offset: int,
        status: ResearchProjectStatus | None = None,
        visibility: ResearchProjectVisibility | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None
    ) -> list[ResearchProject]:
        pass

    @abstractmethod
    def get_research_project_by_id(self, id: UUID) -> ResearchProject | None:
        pass

    @abstractmethod
    def update_research_project(self, id: UUID, research_project: ResearchProject) -> ResearchProject:
        pass

    @abstractmethod
    def delete_research_project(self, id: UUID) -> ResearchProject:
        pass