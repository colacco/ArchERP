from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class UpdateResearchProjectInput:
    owner_id: UUID
    title: Optional[str] =  None
    description: Optional[str] =  None
    objective: Optional[str] =  None
    research_area: Optional[str] =  None
    sub_area: Optional[str] =  None
    instituition: Optional[str] =  None
    keywords: Optional[list[str]] =  None
    status: Optional[str] =  None
    visibility: Optional[str] =  None
