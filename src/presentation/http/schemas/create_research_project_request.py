from pydantic import BaseModel

class CreateResearchProjectRequest(BaseModel):
    title: str
    description: str
    objective: str
    research_area: str
    sub_area: str
    instituition: str
    keywords: list[str]
    status: str
    visibility: str
