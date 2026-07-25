from uuid import UUID

from pydantic import BaseModel

class UpdateUserRequest(BaseModel):
    name: str | None = None
    email: str | None = None
    role_id: UUID | None = None