from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class ResearchProjectResponse(BaseModel):
    model_config = {"from_attributes": True}
    
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