from src.domain.entities.research_project import ResearchProject
from src.domain.enums.research_project.status import ResearchProjectStatus
from src.domain.enums.research_project.visibility import ResearchProjectVisibility
from src.domain.repositories.research_project_repository import ResearchProjectRepository
from src.domain.exceptions.research_project.invalid_status import InvalidResearchProjectStatus
from src.domain.exceptions.research_project.invalid_visibility import InvalidResearchProjectVisibility

from src.application.dtos.research_project.list import ListResearchProjectInput
from src.application.dtos.research_project.research_project_output import ResearchProjectOutput
from src.application.dtos.shared.paginated_output import PaginatedOutput

class ListResearchProject():
    def __init__(self, repository: ResearchProjectRepository):
        self._repository = repository

    def execute(self, dto: ListResearchProjectInput) -> PaginatedOutput[ResearchProjectOutput]:
        status: ResearchProjectStatus | None = None
        visibility: ResearchProjectVisibility | None = None
        
        items: list[ResearchProjectOutput] = []
        offset: int = 0
        limit: int = 20

        if dto.limit is not None:
            limit = min(dto.limit, 100)

        if dto.offset is not None:
            offset = dto.offset

        if dto.status is not None:
            try:
                status = ResearchProjectStatus(dto.status)
            except ValueError:
                raise InvalidResearchProjectStatus(dto.status) from None

        if dto.visibility is not None:
            try:
                visibility = ResearchProjectVisibility(dto.visibility)
            except ValueError:
                raise InvalidResearchProjectVisibility(dto.visibility) from None

        count: int = self._repository.count_research_projects(status, visibility, dto.start_date, dto.end_date)
        research_projects: list[ResearchProject] = self._repository.list_research_projects(limit, offset, status, visibility, dto.start_date, dto.end_date)
        

        for rp in research_projects:
            items.append(ResearchProjectOutput.from_entity(rp))

        return PaginatedOutput(items, count, limit, offset)