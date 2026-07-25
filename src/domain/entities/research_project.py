from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.domain.enums.research_project.status import ResearchProjectStatus
from src.domain.enums.research_project.visibility import ResearchProjectVisibility

@dataclass
class ResearchProject():
    id: UUID
    owner_id: UUID

    title: str
    description: str
    objective: str
    research_area: str
    sub_area: str
    instituition: str
    keywords: list[str]
    status: ResearchProjectStatus
    visibility: ResearchProjectVisibility

    created_at: datetime
    updated_at: datetime
    finished_at: datetime | None