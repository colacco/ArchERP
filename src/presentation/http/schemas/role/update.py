from pydantic import BaseModel

class UpdateRoleRequest(BaseModel):
    name: str | None = None
    description: str | None = None