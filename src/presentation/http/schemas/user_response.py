from uuid import UUID
from pydantic import BaseModel

class UserResponse(BaseModel):
    model_config = {"from_attributes": True} 
    id: UUID
    role_id: UUID
    name: str
    email: str