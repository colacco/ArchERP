import uuid
from datetime import datetime
from fastapi import APIRouter, Depends
from typing import Annotated, Any
from uuid import UUID

from src.application.use_cases.create_research_project import CreateResearchProject
from src.application.use_cases.list_research_project import ListResearchProject
from src.application.use_cases.get_research_project import GetResearchProject
from src.application.use_cases.update_research_project import UpdateResearchProject
from src.application.use_cases.delete_research_project import DeleteResearchProject
from src.application.dtos.research_project.create import CreateResearchProjectInput
from src.application.dtos.research_project.update import UpdateResearchProjectInput
from src.application.dtos.shared.paginated_output import PaginatedOutput
from src.application.dtos.research_project.list import ListResearchProjectInput
from src.application.dtos.research_project.research_project_output import ResearchProjectOutput


from src.presentation.http.schemas.research_project.create import CreateResearchProjectRequest
from src.presentation.http.schemas.research_project.update import UpdateResearchProjectRequest
from src.presentation.http.schemas.research_project.response import ResearchProjectResponse
from src.presentation.http.schemas.shared.paginated_response import PaginatedResponse, Metadata
from src.presentation.http.guards import get_current_user
from src.presentation.http.dependencies import (
    make_create_research_project_use_case, 
    make_list_research_project_use_case,
    make_get_research_project_use_case,
    make_update_research_project_use_case,
    make_delete_research_project_use_case
)

router = APIRouter(prefix="/research-projects", tags=["research-projects"], dependencies=[Depends(get_current_user)])

@router.post("/", response_model=ResearchProjectResponse)
def create_research_project(
    body: CreateResearchProjectRequest,
    use_case: Annotated[CreateResearchProject, Depends(make_create_research_project_use_case)], 
    current_user: Annotated[dict[str, Any], Depends(get_current_user)]
) -> ResearchProjectResponse:
    dto = CreateResearchProjectInput(
        owner_id= uuid.UUID(current_user["sub"]),
        title= body.title,
        description= body.description,
        objective= body.objective,
        research_area= body.research_area,
        sub_area= body.sub_area,
        instituition= body.instituition,
        keywords= body.keywords,
        status= body.status,
        visibility= body.visibility
    )

    research_project: ResearchProjectOutput = use_case.execute(dto)

    return ResearchProjectResponse.model_validate(research_project)

@router.get("/", response_model= PaginatedResponse[ResearchProjectResponse])
def list_research_projects(
    use_case: Annotated[ListResearchProject, Depends(make_list_research_project_use_case)],
    limit: int | None = None,
    offset: int | None = None,
    status: str | None = None, 
    visibility: str | None = None, 
    start_date: datetime | None = None, 
    end_date: datetime | None = None,
) -> PaginatedResponse[ResearchProjectResponse]:
    dto = ListResearchProjectInput(
        limit= limit,
        offset= offset,
        status= status,
        visibility= visibility,
        start_date= start_date,
        end_date= end_date
    )
    
    output: PaginatedOutput[ResearchProjectOutput] = use_case.execute(dto)
    data: list[ResearchProjectResponse] = []
    meta: Metadata = Metadata(
        total= output.total, 
        limit= output.limit, 
        offset= output.offset
    )
    
    for outitem in output.items:
        data.append(ResearchProjectResponse.model_validate(outitem))

    return PaginatedResponse(
        data= data, 
        meta= meta
    )

@router.get("/{id}", response_model=ResearchProjectResponse)
def get_research_project_by_id(
    id: UUID, 
    use_case: Annotated[GetResearchProject, Depends(make_get_research_project_use_case)]
) -> ResearchProjectResponse:
    output = use_case.execute(id)

    return ResearchProjectResponse.model_validate(output)

@router.patch("/{id}", response_model=ResearchProjectResponse)
def update_research_project(
    id: UUID,
    body: UpdateResearchProjectRequest,
    use_case: Annotated[UpdateResearchProject, Depends(make_update_research_project_use_case)],
    current_user: Annotated[dict[str, Any], Depends(get_current_user)]
) -> ResearchProjectResponse:
    dto = UpdateResearchProjectInput(
        owner_id= uuid.UUID(current_user["sub"]),
        title= body.title,
        description= body.description,
        objective= body.objective,
        research_area= body.research_area,
        sub_area= body.sub_area,
        instituition= body.instituition,
        keywords= body.keywords,
        status= body.status,
        visibility= body.visibility
    )
    output = use_case.execute(id, dto)
    return ResearchProjectResponse.model_validate(output)

@router.delete("/{id}", status_code=204)
def delete_research_project(
    id: UUID,
    use_case: Annotated[DeleteResearchProject, Depends(make_delete_research_project_use_case)],
    current_user: Annotated[dict[str, Any], Depends(get_current_user)]
) -> None:
    use_case.execute(id, uuid.UUID(current_user["sub"]))