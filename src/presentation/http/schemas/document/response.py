from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class DocumentResponse(BaseModel):
    model_config = {"from_attributes": True}
    project_id: UUID
    author_id: UUID
    
    title: str
    description: str
    type: str
    
    format: str
    file_url: str | None
    content: str | None

    created_at: datetime
    update_at: datetime