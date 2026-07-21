from copy import deepcopy
from datetime import datetime
from uuid import UUID

from src.domain.entities.research_project import ResearchProject
from src.domain.enums.research_project_status import ResearchProjectStatus
from src.domain.enums.research_project_visibility import ResearchProjectVisibility
from src.domain.exceptions.research_project_not_found import ResearchProjectNotFound
from src.domain.repositories.research_project_repository import ResearchProjectRepository

class InMemoryResearchProjectRepository(ResearchProjectRepository):
    def __init__(self) -> None:
        self._research_projects: list[ResearchProject] = []

    def _filter_research_projects(
        self, status: ResearchProjectStatus | None, 
        visibility: ResearchProjectVisibility | None, 
        start_date: datetime | None, 
        end_date: datetime | None
    ) -> list[ResearchProject]:
        copy_research_projects = deepcopy(self._research_projects)
        filtered_projects: list[ResearchProject] = copy_research_projects

        if status is not None:
            filtered_projects = []

            for rp in copy_research_projects:
                if rp.status == status:
                    filtered_projects.append(rp)

            copy_research_projects = filtered_projects
        
        if visibility is not None:
            filtered_projects = []

            for rp in copy_research_projects:
                if rp.visibility == visibility:
                    filtered_projects.append(rp)

            copy_research_projects = filtered_projects

        if start_date is not None:
            filtered_projects = []

            for rp in copy_research_projects:
                if rp.created_at >= start_date:
                    filtered_projects.append(rp)

            copy_research_projects = filtered_projects

        if end_date is not None:
            filtered_projects = []

            for rp in copy_research_projects:
                if rp.finished_at is not None and rp.finished_at <= end_date:
                   filtered_projects.append(rp)

        return filtered_projects


    def create_research_project(self, research_project: ResearchProject) -> ResearchProject:
        self._research_projects.append(deepcopy(research_project))
        return research_project
    
    def count_research_projects(
        self,
        status: ResearchProjectStatus | None = None,
        visibility: ResearchProjectVisibility | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None
    ) -> int:
        list_projects: list[ResearchProject] = self._filter_research_projects(status, visibility, start_date, end_date)
        
        return len(list_projects)

    def list_research_projects(
        self,
        limit: int,
        offset: int,
        status: ResearchProjectStatus | None = None,
        visibility: ResearchProjectVisibility | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None
    ) -> list[ResearchProject]:
        list_projects: list[ResearchProject] = self._filter_research_projects(status, visibility, start_date, end_date)

        return list_projects[offset : offset + limit]


    def get_research_project_by_id(self, id: UUID) -> ResearchProject | None:
        for item in self._research_projects:
            if item.id == id:
                return deepcopy(item)
            
        return None

    def update_research_project(self, id: UUID, research_project: ResearchProject) -> ResearchProject:
        index: int = 0

        for project in self._research_projects:
            if project.id == id:
                self._research_projects[index] = deepcopy(research_project)

                return research_project
            
            index += 1
        
        raise ResearchProjectNotFound(id)
            
    def delete_research_project(self, id: UUID) -> ResearchProject:
        index: int = 0

        for project in self._research_projects:
            if project.id == id:

                return self._research_projects.pop(index)
            
            index += 1
        
        raise ResearchProjectNotFound(id)