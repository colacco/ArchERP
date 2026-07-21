from pydantic import BaseModel

class UpdateResearchProjectRequest(BaseModel):
    title: str | None =  None
    description: str | None =  None
    objective: str | None =  None
    research_area: str | None =  None
    sub_area: str | None =  None
    instituition: str | None =  None
    keywords: list[str] | None =  None
    status: str | None =  None
    visibility: str | None =  None