from datetime import datetime
from uuid import UUID

from src.domain.entities.research_project import ResearchProject
from src.domain.enums.research_project.status import ResearchProjectStatus
from src.domain.enums.research_project.visibility import ResearchProjectVisibility
from src.domain.repositories.research_project_repository import ResearchProjectRepository
from src.domain.exceptions.research_project.already_finished import ResearchProjectAlreadyFinished
from src.domain.exceptions.research_project.not_found import ResearchProjectNotFound
from src.domain.exceptions.research_project.invalid_status import InvalidResearchProjectStatus
from src.domain.exceptions.research_project.invalid_visibility import InvalidResearchProjectVisibility
from src.domain.exceptions.auth.unauthorized import Unauthorized

from src.application.dtos.research_project.update import UpdateResearchProjectInput
from src.application.dtos.research_project.research_project_output import ResearchProjectOutput

class UpdateResearchProject():
    def __init__(self, repository: ResearchProjectRepository) -> None:
        self._repository = repository

    def execute(self, id: UUID, dto: UpdateResearchProjectInput) -> ResearchProjectOutput:
        research_project: ResearchProject | None = self._repository.get_research_project_by_id(id)

        if research_project is None:
            raise ResearchProjectNotFound(id)
        
        if research_project.owner_id != dto.owner_id:
            raise Unauthorized()

        if dto.title is not None:
            research_project.title = dto.title

        if dto.description is not None:
            research_project.description = dto.description
        
        if dto.objective is not None:
            research_project.objective = dto.objective
        
        if dto.research_area is not None:
            research_project.research_area = dto.research_area

        if dto.sub_area is not None:
            research_project.sub_area = dto.sub_area

        if dto.instituition is not None:
            research_project.instituition = dto.instituition

        if dto.keywords is not None:
            research_project.keywords = dto.keywords

        if dto.status is not None:
            try:
                if research_project.status == ResearchProjectStatus("finished"):
                    raise ResearchProjectAlreadyFinished()
                
                research_project.status = ResearchProjectStatus(dto.status)

                if research_project.status == ResearchProjectStatus("finished"):
                    research_project.finished_at = datetime.now()

            except ValueError:
                raise InvalidResearchProjectStatus(dto.status)
            
        if dto.visibility is not None:
            try:
                research_project.visibility = ResearchProjectVisibility(dto.visibility)
            except ValueError:
                raise InvalidResearchProjectVisibility(dto.visibility)
            
        research_project.updated_at = datetime.now()

        research_project = self._repository.update_research_project(id, research_project)

        return ResearchProjectOutput.from_entity(research_project)