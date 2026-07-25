from dataclasses import dataclass
from uuid import UUID

@dataclass
class CreateResearchProjectInput():
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
