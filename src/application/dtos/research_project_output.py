from dataclasses import dataclass
from datetime import datetime
from typing import Self
from uuid import UUID

from src.domain.entities.research_project import ResearchProject

@dataclass
class ResearchProjectOutput():
    id: UUID
    owner_id: UUID

    title: str
    description: str
    objective: str
    research_area: str
    sub_area: str
    instituition: str
    keywords: list[str]
    status: str
    visibility: str

    created_at: datetime
    updated_at: datetime
    finished_at: datetime | None

    @classmethod
    def from_entity(cls, research_project: ResearchProject) -> Self:
        return cls(
            id= research_project.id,
            owner_id= research_project.owner_id,
            title= research_project.title,
            description= research_project.description,
            objective= research_project.objective,
            research_area= research_project.research_area,
            sub_area= research_project.sub_area,
            instituition= research_project.instituition,
            keywords= research_project.keywords,
            status= research_project.status.value,
            visibility= research_project.visibility.value,
            created_at= research_project.created_at,
            updated_at= research_project.updated_at,
            finished_at= research_project.finished_at
        )