from uuid import UUID

from src.domain.repositories.research_project_repository import ResearchProjectRepository
from src.domain.exceptions.research_project_not_found import ResearchProjectNotFound
from src.domain.exceptions.unauthorized import Unauthorized

class DeleteResearchProject():
    def __init__(self, repository: ResearchProjectRepository):
        self._repository = repository

    def execute(self, id: UUID, owner_id: UUID):
        research_project = self._repository.get_research_project_by_id(id)

        if research_project is None:
            raise ResearchProjectNotFound(id)
        
        if research_project.owner_id != owner_id:
            raise Unauthorized()
        
        return self._repository.delete_research_project(id)