from uuid import UUID

from src.domain.entities.research_project import ResearchProject
from src.domain.repositories.research_project_repository import ResearchProjectRepository
from src.domain.exceptions.research_project.not_found import ResearchProjectNotFound

from src.application.dtos.research_project.research_project_output import ResearchProjectOutput

class GetResearchProject():
    def __init__(self, repository: ResearchProjectRepository) -> None:
        self._repository = repository

    def execute(self, id: UUID) -> ResearchProjectOutput:
        research_project: ResearchProject | None = self._repository.get_research_project_by_id(id)
        
        if research_project is None:
            raise ResearchProjectNotFound(id)
        
        return ResearchProjectOutput.from_entity(research_project)