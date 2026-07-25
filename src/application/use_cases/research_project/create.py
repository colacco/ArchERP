from datetime import datetime
from uuid import uuid4

from src.domain.entities.research_project import ResearchProject
from src.domain.enums.research_project.status import ResearchProjectStatus
from src.domain.enums.research_project.visibility import ResearchProjectVisibility
from src.domain.repositories.research_project_repository import ResearchProjectRepository
from src.domain.exceptions.research_project.invalid_status import InvalidResearchProjectStatus
from src.domain.exceptions.research_project.invalid_visibility import InvalidResearchProjectVisibility

from src.application.dtos.research_project.create import CreateResearchProjectInput
from src.application.dtos.research_project.output import ResearchProjectOutput

class CreateResearchProject():
    def __init__(self, repository: ResearchProjectRepository) -> None:
        self._repository = repository

    def execute(self, dto: CreateResearchProjectInput) -> ResearchProjectOutput:
        finished_at: datetime | None = None

        try:
            status: ResearchProjectStatus = ResearchProjectStatus(dto.status)

            if status == ResearchProjectStatus("finished"):
                    finished_at = datetime.now()
        except ValueError:
            raise InvalidResearchProjectStatus (dto.status) from None

        try:
            visibility: ResearchProjectVisibility = ResearchProjectVisibility(dto.visibility)
        except ValueError:
            raise InvalidResearchProjectVisibility(dto.visibility) from None

        research_project = ResearchProject(
            id= uuid4(),
            owner_id= dto.owner_id,
            title= dto.title,
            description= dto.description,
            objective= dto.objective,
            research_area= dto.research_area,
            sub_area= dto.sub_area,
            instituition= dto.instituition,
            keywords= dto.keywords,
            status= status,
            visibility= visibility,
            created_at= datetime.now(),
            updated_at= datetime.now(),
            finished_at= finished_at
        )

        research_project = self._repository.create_research_project(research_project)

        return ResearchProjectOutput.from_entity(research_project)