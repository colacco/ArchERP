from dataclasses import dataclass
from uuid import UUID

@dataclass
class CreateUserInput():
    name: str
    email: str
    password: str
    role_id: UUID
