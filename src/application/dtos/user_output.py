from uuid import UUID
from dataclasses import dataclass

@dataclass
class UserOutput():
    id: UUID
    role_id: UUID
    name: str
    email: str
