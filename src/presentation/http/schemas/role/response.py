from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class RoleResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime